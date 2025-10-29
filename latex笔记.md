#### 一些小点
##### Kpathsea是路径查询；
##### 文档类的定义：
LaTeX 的 document class（文档类）是由一个扩展名为 .cls 的文件定义的。例如：

article.cls

report.cls

book.cls

beamer.cls

当您在导言区写：

latex
复制
编辑
\documentclass{article}
LaTeX 就会去搜索并加载 article.cls 这个文件。

这些 .cls 文件一般存放在 TeX 发行版（如 TeX Live、MikTeX、MacTeX）的安装目录下