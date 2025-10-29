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
3. **推荐用yaml文件创建**，否则包列表包含pip的包，可能报错；

### 在本地复制环境
```bash
conda create --name new_env_name --clone old_env_name
```
## 额外pip知识
### 一些命令
- pip show <包名>： 用来显示已安装包的详细信息；
### 另一种安装包的方式：从源码安装
pip install -e . --verbose
pip install -e . 会做三件事：
- 把包“链接”到环境：在 site-packages 放一个指向源码目录的链接，能用包名 import。
- 安装依赖与入口脚本：处理 install_requires/pyproject.toml，生成命令行入口。
- 可编辑：改源码立刻生效，无需反复重新安装。

#### 关于入口脚本
项目可以声明命令行可执行文件，安装时 pip 会在环境的 bin/ 目录生成同名可执行脚本，指向你代码中的某个函数，这样你可以直接在终端运行该命令。
