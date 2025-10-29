#!/bin/bash

# 定义一个数组，包含空格、通配符、空元素
arr=("AutoInt main.py" "*.py" "" "item4")

echo "1. \${arr[@]} (不带引号的 @):"
printf '[%s]\n' ${arr[@]}
echo ""

echo "2. \"\${arr[@]}\" (带引号的 @):"
printf '[%s]\n' "${arr[@]}"
echo ""

echo "3. \${arr[*]} (不带引号的 *):"
printf '[%s]\n' ${arr[*]}
echo ""

echo "4. \"\${arr[*]}\" (带引号的 *):"
printf '[%s]\n' "${arr[*]}"
echo ""

echo "在 for 循环中的行为:"
echo "- for x in \${arr[@]}:" 
for x in ${arr[@]}; do printf '[%s] ' "$x"; done; echo ""
echo "- for x in \"\${arr[@]}\":" 
for x in "${arr[@]}"; do printf '[%s] ' "$x"; done; echo ""
echo "- for x in \${arr[*]}:" 
for x in ${arr[*]}; do printf '[%s] ' "$x"; done; echo ""
echo "- for x in \"\${arr[*]}\":" 
for x in "${arr[*]}"; do printf '[%s] ' "$x"; done; echo ""