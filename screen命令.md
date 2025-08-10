## 删除screen 会话
方法1：删除单个 screen 会话
```bash
# 使用 screen ID 删除
screen -S 4090701 -X quit

# 或者使用 screen 名称删除
screen -S pts-6.Ubuntu -X quit
```
-S 指定会话，-X 指定命令
方法2：批量删除多个 screen 会话
方法3：删除所有 detached 的 screen 会话
方法4：进入screen会话后删除