# 统计所有分支的对白、旁白和选项，含标点，不含角色名和动态插值。
# 启动或 Shift+R 重载时更新；开发模式显示总数，log.txt 记录分文件结果。
init 999 python:
    import os as _wordcount_os
    import re as _wordcount_re

    def _wordcount_text_length(text):
        text = renpy.filter_text_tags(text, allow=set()).replace("{{", "{")
        # 不执行插值表达式；[[ 表示可见的左方括号。
        visible = []
        index = 0
        while index < len(text):
            if text.startswith("[[", index):
                visible.append("[")
                index += 2
            elif text[index] == "[":
                depth = 1
                index += 1
                quote = None
                while index < len(text) and depth:
                    char = text[index]
                    if quote:
                        if char == "\\":
                            index += 2
                            continue
                        if char == quote:
                            quote = None
                    elif char in ("'", '"'):
                        quote = char
                    elif char == "[":
                        depth += 1
                    elif char == "]":
                        depth -= 1
                    index += 1
            else:
                visible.append(text[index])
                index += 1
        text = _wordcount_re.sub(r"\s+", "", "".join(visible))
        if not text or all(char in ".…⋯" for char in text):
            return 0
        return len(text)

    def _wordcount_collect():
        counts = {}
        game_dir = _wordcount_os.path.normpath(config.gamedir)
        for node in renpy.game.script.all_stmts:
            filename = node.filename.replace("\\", "/")
            if _wordcount_os.path.isabs(filename):
                filename = _wordcount_os.path.relpath(filename, game_dir).replace("\\", "/")
            elif filename.startswith("game/"):
                filename = filename[5:]
            else:
                # 排除 Ren'Py 自带脚本。
                continue
            if filename.startswith("../") or filename.startswith("tl/"):
                continue
            if not filename.endswith((".rpy", ".rpyc")):
                continue
            if isinstance(node, renpy.ast.Say):
                texts = [node.what]
            elif isinstance(node, renpy.ast.Menu):
                texts = [caption for caption, condition, block in node.items if caption]
            else:
                continue
            counts[filename] = counts.get(filename, 0) + sum(
                _wordcount_text_length(text) for text in texts
            )
        return counts

    wordcount_by_file = _wordcount_collect()
    total_chars = sum(wordcount_by_file.values())
    renpy.log("剧本纯文字总字符（含标点）：{}".format(total_chars))
    for _wordcount_filename, _wordcount_count in sorted(wordcount_by_file.items()):
        renpy.log("  {}: {}".format(_wordcount_filename, _wordcount_count))
    if config.developer and "wordcount_overlay" not in config.overlay_screens:
        config.overlay_screens.append("wordcount_overlay")

screen wordcount_overlay():
    zorder 100
    if config.developer:
        frame:
            xalign 1.0
            yalign 0.0
            padding (12, 8)
            background "#000a"
            text "剧本字数（含标点）：[total_chars]":
                size 20
                color "#fff"
