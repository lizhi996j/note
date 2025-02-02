import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from datetime import datetime

# 创建一个简单的神经网络
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 1)
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 生成一些示例数据
def generate_data(num_samples=1000):
    X = np.random.randn(num_samples, 10)
    # 创建一个非线性关系的目标值
    y = np.sum(X**2, axis=1, keepdims=True) + np.random.randn(num_samples, 1) * 0.1
    return torch.FloatTensor(X), torch.FloatTensor(y)

def train():
    # 创建模型和优化器
    model = SimpleNet()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    # 创建 TensorBoard writer
    current_time = datetime.now().strftime('%Y%m%d-%H%M%S')
    log_dir = f'runs/experiment_{current_time}'
    writer = SummaryWriter(log_dir)
    
    # 生成训练数据
    X, y = generate_data()
    
    # 记录计算图
    writer.add_graph(model, torch.randn(1, 10))
    
    # 训练循环
    num_epochs = 100
    batch_size = 32
    num_batches = len(X) // batch_size
    
    for epoch in range(num_epochs):
        total_loss = 0
        
        for batch in range(num_batches):
            start_idx = batch * batch_size
            end_idx = start_idx + batch_size
            
            # 获取批次数据
            batch_X = X[start_idx:end_idx]
            batch_y = y[start_idx:end_idx]
            
            # 前向传播
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            
            # 反向传播和优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        # 计算平均损失
        avg_loss = total_loss / num_batches
        
        # 记录损失到 TensorBoard
        writer.add_scalar('Loss/train', avg_loss, epoch)
        
        # 每10个epoch记录一次参数分布和梯度分布
        if epoch % 10 == 0:
            for name, param in model.named_parameters():
                writer.add_histogram(f'Parameters/{name}', param.data, epoch)
                if param.grad is not None:
                    writer.add_histogram(f'Gradients/{name}', param.grad, epoch)
        
        if epoch % 10 == 0:
            print(f'Epoch [{epoch}/{num_epochs}], Loss: {avg_loss:.4f}')
    
    writer.close()

if __name__ == '__main__':
    train()
