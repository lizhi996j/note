import torch
import torch.nn as nn
import torch.nn.functional as F

###用过小数初始化会导致梯度消失，过大初始化会导致梯度爆炸；
###虽然使用了正态分布初始化，但抽样误差被一层层的神经网络方大了，所以最后前向传播的值还是趋向无穷了；
### xavier 初始化可以缓解梯度消失和爆炸的问题，因为他动态调整方差，所使用的方差也比1小很多；
### 再一个由于他调整方差的方式导致每层方差都小；

class MyNN(nn.Module):
    def __init__(self, in_size=256, layer_num=100):
        super(MyNN, self).__init__()
        self.in_size = in_size
        # 100层全连接堆叠起来
        self.FC = nn.Sequential(*[nn.Linear(in_size, in_size, bias=False) for _ in range(layer_num)])
        # 不同初始化方法测试
        self._initialize()
        
    def forward(self, x):
        for (idx, linear) in enumerate(self.FC):
            x = linear(x)
            # 打印每一层的均值和标准差
            print("idx:{}, mean:{}, std:{}".format(idx + 1, x.mean(), x.std()))
            # if torch.isnan(x.mean()) or torch.isnan(x.std()) or torch.isinf(x.mean()) or torch.isinf(x.std()):
            #     break
        return x
    
    def _initialize(self):
        for m in self.modules(): # 看看modules()是什么？
            if isinstance(m, nn.Linear):
                # 固定值
                nn.init.normal_(m.weight.data, mean=0, std=1)
                # nn.init.xavier_normal_(m.weight.data)
        for name, param in self.named_parameters():
            if param.requires_grad:
                print(name, param.mean(), param.std(), param.norm())

if __name__ == '__main__':
    mynn = MyNN(in_size=256, layer_num=100)
    x = torch.randn(8, 256)
    x.requires_grad = True
    x.retain_grad()
    y = mynn(x)
    y.backward(torch.ones_like(y))
    print('x grad mean:', x.grad.mean())
    print('x grad std:', x.grad.std())
    for name, param in mynn.named_parameters():
        if param.requires_grad:
            print(name, param.grad.mean(), param.grad.std(), param.grad.norm())