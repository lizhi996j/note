import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import ray
from ray import tune
from ray.tune.schedulers import ASHAScheduler
from functools import partial

# 定义一个简单的神经网络
class Net(nn.Module):
    def __init__(self, l1=128, l2=64):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28*28, l1)
        self.fc2 = nn.Linear(l1, l2)
        self.fc3 = nn.Linear(l2, 10)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = self.dropout(self.relu(self.fc1(x)))
        x = self.dropout(self.relu(self.fc2(x)))
        x = self.fc3(x)
        return x

def train_epoch(model, trainloader, optimizer, criterion, device):
    running_loss = 0.0
    correct = 0
    total = 0
    
    for data in trainloader:
        inputs, labels = data
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    return running_loss / len(trainloader), correct / total

def train(config, checkpoint_dir=None):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # 数据加载和预处理
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    trainset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    trainloader = DataLoader(
        trainset, 
        batch_size=int(config["batch_size"]), 
        shuffle=True,
        num_workers=0  # Windows上设置为0避免多进程问题
    )

    # 模型、损失函数和优化器
    model = Net(
        l1=config["layer1_size"],
        l2=config["layer2_size"]
    ).to(device)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config["lr"])

    # 如果有检查点，加载它
    if checkpoint_dir:
        checkpoint = os.path.join(checkpoint_dir, "checkpoint")
        model_state, optimizer_state = torch.load(checkpoint)
        model.load_state_dict(model_state)
        optimizer.load_state_dict(optimizer_state)

    # 训练循环
    for epoch in range(3):  # 为了演示，我们只训练3个epoch
        loss, accuracy = train_epoch(model, trainloader, optimizer, criterion, device)
        
        # 向Ray Tune报告指标
        tune.report(loss=loss, accuracy=accuracy)

        # 保存检查点
        with tune.checkpoint_dir(epoch) as checkpoint_dir:
            save_path = os.path.join(checkpoint_dir, "checkpoint")
            torch.save(
                (model.state_dict(), optimizer.state_dict()),
                save_path)

def main(num_samples=10, max_num_epochs=10):
    # 确保结果目录存在
    local_dir = os.path.abspath("./ray_results")
    os.makedirs(local_dir, exist_ok=True)
    
    # 配置Ray Tune的搜索空间
    config = {
        "layer1_size": tune.choice([64, 128, 256]),
        "layer2_size": tune.choice([32, 64, 128]),
        "lr": tune.loguniform(1e-4, 1e-1),
        "batch_size": tune.choice([32, 64, 128])
    }

    # 设置ASHA调度器
    scheduler = ASHAScheduler(
        max_t=max_num_epochs,
        grace_period=1,
        reduction_factor=2,
        metric="accuracy",  # 使用准确率作为评估指标
        mode="max"         # 目标是最大化准确率
    )

    # 运行优化
    result = tune.run(
        partial(train),
        storage_path=local_dir,  # 使用local_dir而不是storage_path
        resources_per_trial={"cpu": 1, "gpu": 0},
        config=config,
        num_samples=num_samples,
        scheduler=scheduler,
        progress_reporter=tune.CLIReporter(
            parameter_columns=["layer1_size", "layer2_size", "lr", "batch_size"],
            metric_columns=["loss", "accuracy", "training_iteration"]
        )
    )

    # 获取最佳试验结果
    best_trial = result.get_best_trial("accuracy", "max", "last")
    print("Best trial config: {}".format(best_trial.config))
    print("Best trial final validation loss: {}".format(
        best_trial.last_result["loss"]))
    print("Best trial final validation accuracy: {}".format(
        best_trial.last_result["accuracy"]))

if __name__ == "__main__":
    ray.init(ignore_reinit_error=True)
    main(num_samples=4)
