# VScode/Cursor 设置：
1. **设置快捷键**：
    - `Ctrl + K Ctrl + S`
    - 打开 `keybinds.json` 文件：
    ```json
    {
        "key": "ctrl+1",
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "(需要插入代码)"
        },
        "when": "editorTextFocus"
    }
    ```
    - `command` 除了以上还有 `type` 选项，用于直接插入指定的文本，不支持设置光标位置
2. **Markdown 在插入行间公式后不显示的问题**：
    - 参考链接: [GitHub Issue #1032](https://github.com/yzhang-gh/vscode-markdown/issues/1032)
    - 解决方案：禁用 `markdown-math` 扩展，使用 `@builtin markdown` 禁用。
3. enable editor preview单击打开文件后无法出现在bar中。
4. activate bar是最左侧一栏
5. vscode 下 git diff 视图：左边是历史，右边是当前的
6. 多行光标：
✅ 在 VS Code 中选中 某单词 批量编辑：
方法一：使用 Ctrl + D（或 Cmd + D on Mac）
将光标放在第一个 某单词 上。

连续按 Ctrl + D（Mac 是 Cmd + D）可以逐个选中下一个相同的单词。

多个光标出现后即可同步修改。

方法二：Ctrl + Shift + L（或 Cmd + Shift + L）
用鼠标或键盘选中一次 某单词。

然后按 Ctrl + Shift + L（Mac 是 Cmd + Shift + L）。

所有相同的文本会被添加为多光标，一起编辑。

方法三：Alt + Click 添加光标到每一行
如果 某单词 分布位置不同，可使用 Alt + Click 手动在每一行上添加光标。

#### cursor pyright设置代码高亮；