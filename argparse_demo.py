import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v",action='count')

parser.add_argument('-o', '--output', required=True, help='输出文件路径')
parser.add_argument('--format', choices=['json', 'xml', 'csv'], default='json', help='输出格式')
sub_parser = parser.add_subparsers(dest="command")
add_parser = sub_parser.add_parser("add")
add_parser.add_argument("-f",help="文件名")
delete_parser = sub_parser.add_parser("delete")
delete_parser.add_argument("-f")
parser.add_argument('input', help='输入文件路径')
arg = parser.parse_args()

print(arg.input)
print(arg.v)

# 关于说明文档:

# 例子：（没有子命令时输出）
# > python argparse_demo.py -h
# usage: argparse_demo.py [-h] [-v] -o OUTPUT [--format {json,xml,csv}] input

# positional arguments:
#   input                 输入文件路径

# optional arguments:
#   -h, --help            show this help message and exit
#   -v
#   -o OUTPUT, --output OUTPUT
#                         输出文件路径
#   --format {json,xml,csv}
#                         输出格式


#例子： 对子命令使用-h 注意要把子命令放在位置参数前面才能直接 子命令 -h, 否则  'python argparse_demo.py data.txt add -h'
# (RecBole) zhi-li@zhi-li-Precision-3660:~/Workspace/Coding/note$ python argparse_demo.py add -h
# usage: argparse_demo.py add [-h] [-f F]

# optional arguments:
#   -h, --help  show this help message and exit
#   -f F        文件名

"""注意：\
 -h是默认添加的
 -o output表示两个都行
"""
