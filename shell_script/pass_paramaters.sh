#!/bin/bash
echo $0 ## 输出的路径似乎和我调用时输入的命令相同
echo $1$2 $3 $4 ## 如果参数不够就是空的
echo '"$@"' ## 
for i in "$@"; do #由于加入引号@会把各个参数当作独立个体，因而循环时会输出多行
    echo $i
done

echo '$@'
for i in $@; do 
    echo $i
done

echo '"$*"'
for i in "$*"; do
    echo $i
done 

echo '$*'
for i in $*; do
    echo $i
done 

echo "$#" #输出输入参数个数；
echo "$@"
echo $@

a=$*
echo $a