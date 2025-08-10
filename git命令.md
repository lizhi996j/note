## git 命令
### git status
1. 一个例子：本地仓库落后远程仓库1个commit，且工作区有修改。
```bash
PS A:\coding\learn_git> git status
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello_world.py

no changes added to commit (use "git add" and/or "git commit -a")
```
最后一行由于没有stage的内容，所以也就没有可以commit的内容.
2. 一个例子：
```bash
git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours) ##### 您的本地分支有 1 个远程没有的提交，远程分支有 1 个您本地没有的提交，两个分支"分歧"了

You have unmerged paths. # 有未解决冲突
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   hello_world.py

no changes added to commit (use "git add" and/or "git commit -a")
```
### git pull = git fetch + git merge
- 拉取远程新提交，当远程没有新提交时无法拉取；当本地分支比远程分支领先时无法拉取；
- 在git pull的时候，工作区的修改如果与远程仓库没冲突（这里值工作区内容不会被覆写）的话可以在工作区不clean的时候拉取；注意就算是本地工作区修改为和远程一样，似乎仍然不能pull;
- --dry-run 的行为特点：
git pull --dry-run 只是模拟拉取操作，它会显示将要下载什么，但不会实际执行合并操作
它主要检查的是网络连接和远程仓库的可访问性，以及显示将要获取的提交
关键点：--dry-run 不会检查本地工作区的文件冲突

### git ls-files 相关
git ls-files 是一个 Git 命令，用来列出当前 Git 仓库中被 Git 跟踪的所有文件。它会显示已添加到 Git 索引（暂存区）的文件

### git diff 相关
- git diff 查看工作区与暂存区差异
git diff -- 文件名：查看具体某个文件 在工作区和暂存区之间的差异
git diff -- 文件名1 文件名2 文件名3：查看多个文件在工作区和暂存区之间的差异
【注意】：查看具体文件的时候 -- 和文件名 之间有一个 空格,文件名1 和 文件名2 和 文件名3之间也有空格
- 查看工作区和版本库之间文件的差异
git diff HEAD : 查看工作区与最新版本库之间的所有的文件差异
git diff 具体某个版本 : 查看工作区与具体某个提交版本之间的所有的文件差异
git diff HEAD -- 文件名 ： 查看工作区与最新版本库之间的 指定文件名的文件差异
git diff HEAD -- 文件名1 文件名2 文件名3 ：查看工作区与最新版本库之间的 指定文件名的多个文件差异
git diff 具体某个版本 -- 文件名 ： 查看工作区与具体某个版本之间的 指定文件名的文件差异
git diff 具体某个版本 -- 文件名1 文件名2 文件名3 ：查看工作区与最具体某个版本之间的 指定文件名的多个文件差异
- 查看暂存区与版本库差异
git diff --cached : 查看暂存区和 上一次提交 的最新版本(HEAD)之间的所有文件差异
git diff --cached 版本号 ： 查看暂存区和 指定版本 之间的所有文件差异
git diff --cached -- 文件名1 文件名2 文件名3 ： 查看暂存区和 HEAD 之间的指定文件差异
git diff --cached 版本号 -- 文件名1 文件名2 文件名3 ： 查看暂存区和 指定版本 之间的指定文件差异
- git diff 版本号1 版本号2 ： 查看两个版本之间的差异
git diff 版本号1 版本号2 -- 文件名1 文件名2 ： 查看两个版本之间的指定文件之间的差异

- --stat 用于输出统计差异；
- 直接带文件夹名可以输出文件夹的差异；

git diff 的输出：统一差异格式（unified diff):
一个例子：
```bash
diff --git a/example.txt b/example.txt ##### a表示左侧，b表示右侧
index 3b18e72..a5f9c1e 100644
--- a/example.txt
+++ b/example.txt
@@ -1,4 +1,5 @@ ###### 表示旧版本的1到4行，新版本的1到5行；
-Hello, world!  #### -表示旧版本有，新版本无
 This is a demo file. ### 没符号表示没变化
+We have added this new line. ### +表示新版本有，旧版本无
 And this line remains unchanged.
+Another addition here.
```

### git stash 相关：
- `git stash list`: 
- `git stash pop [<stash>@{<idx>}] [--index]`: 将指定（默认是最新的）stash 条目中的改动重新应用到当前工作区和暂存区
- `git stash`: 
- `git stash push --staged`:只保留暂存区内容；
- `git stash push file`: stash某文件；
-  

### git checkout 相关
- `git checkout -- <file>`: 还原暂存区版本；
- `git checkout HEAD --<file>`: 还原到最后一次提交，
- `git checkout <branch>`: 切换分支
- `git checkout <commit-id> -- <file-name>`: 将文件还原到指定版本的内容;会同时写入工作区和暂存区；
- 没有`git checkout --cached`命令；

### git reset 相关
- git reset <file>: 将指定文件从暂存区移除，但保留工作区的修改内容。

### git restore
用来替代git checkout和git reset
如果文件被暂存，git restore --staged <file>: 将指定文件从暂存区移除，但保留工作区的修改内容。
如果文件未被暂存，git restore <file>: 会还原成暂存区版本；

### 其它
- git的user.name和user.email设置：
`git config --global user.name "your_name"`
`git config --global user.email "your_email@example.com"`
用来知道是谁提交的代码

- `index`: 暂存区
- `working tree`: 工作区
- vscode 下 git diff 视图：左边是历史，右边是当前的

- `git log`: `git log` 后一直没有光标问题解决：按 `q`
- `git reflog`: 获得版本号

- `git status`
- `git diff <文件名>`

- `git add`
- `git commit`
- `git checkout --<文件名>`: 工作区回到和版本库相同状态（用于撤销修改，撤销删除）

- `git reset --hard HEAD^`: 版本回退 (HEAD 是指向 master 的指针)
- `git reset --hard <版本号>`: 到指定版本

- 追加到上一次提交：（待补充）

- 查看分支：`git branch`
- 创建分支：`git branch <name>`
- 切换分支：`git checkout <name>`
- 创建并切换分支：`git checkout -b <name>`
- 合并某分支到当前分支：`git merge <name>`
- 删除分支：`git branch -d <name>`

- `git clone` 不会把 origin 的分支拉下来

- `git remote -v`

问题：git 比对版本的时候会不会丢失之前工作？


### vscode 中显示的changes:
显示的changes是工作区与暂存区之间的差异；
显示的stage changes是暂存区与版本库之间的差异；

### 疑问
1. 如果给远程推送的时候有覆写，会不会推送成功？
取决于是不是fast forward, 如果一个分支只有另一个分支的历史提交，就会fast forward从而覆写；
2. 在merge的过程中哪些会被判定为冲突？
在一次merge时，本地有但远程没有的似乎没有判定为冲突？

### 小点
#### .gitignore中文件路径规则
.gitignore中默认根目录是仓库目录，可以加/,但不能用./;
加/就是根目录下的，不加/会在仓库所有层级匹配；



## github 网站教程
### review a pull request
Reviewing a pull request is an opportunity to examine another contributor's changes and give them feedback.