#!/bin/bash
# 1. 查看当前状态
echo "HISTSIZE: '$HISTSIZE'"
history | wc -l

# 2. 设置一个值
HISTSIZE=10
echo "HISTSIZE: '$HISTSIZE'"
history | wc -l


# 3. 清除设置
unset HISTSIZE
echo "HISTSIZE: '$HISTSIZE'"
# 但 history 仍然有默认行为

history | wc -l