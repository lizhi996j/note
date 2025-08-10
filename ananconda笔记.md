## 包管理
### 安装多个包
```bash
conda install numpy pandas matplotlib torch
```
### 查看包的具体信息
```bash
conda list <包名>
```

## 环境管理
### 删除一个环境
```bash
conda env remove -n myenv
```

### 将环境从一个设备迁移到另一个设备
- 方法一：导出环境文件
原设备：
```bash
conda activate myenv
conda env export > myenv.yaml
```
目标设备：
```bash
conda env create -f myenv.yaml -n newname
```

- 方法二：导出包列表
原设备：
```bash
conda list --export >myenv.txt
```
目标设备：
```bash
conda create -n newname -f myenv.txt
```
- 注意： 
1. conda create和conda env create 能解析的文件格式不同；conda env create 能解析yaml文件，而conda create 能解析txt文件；
2. 传递参数时长参数和短参数(-f和--file)有时等价，有时不等价;比如conda env create -f myenv.yaml和conda env create --file myenv.yaml等价，但conda create -f myenv.txt和conda env create --file myenv.txt不等价。
3. **推荐用yaml文件创建**，包列表如何包含pip的包，可能报错；

