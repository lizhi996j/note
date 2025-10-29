### 登录mysql数据库
```bash
mysql -u <username> -p<password> 
```

### 基本操作
#### 查看所有用户
查看用户表`mysql.user`

```sql
select host, user from mysql.user;
```

root 用户（或具有 ALL PRIVILEGES 的超级用户）才可以查看
一个例子：

```bash
mysql> SELECT user, host FROM mysql.user;
+------------------+-----------+
| user             | host      |
+------------------+-----------+
| zhi-li           | %         |
| debian-sys-maint | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+
6 rows in set (0.00 sec)
``` 

其中%代表用户可以从任何主机登录；

#### 查看用户拥有的数据库
```sql
show databases;
```
#### 使用某个数据库
```sql
use <database_name>;
``` 
