"""
笔记管理器 v2 — 只用阶段1学过的内容
- list / dict / str / for / while / with open
- json 模块（练习提示里提到过，简单用一下）
"""
import json
from pathlib import Path

DATA_DIR: Path = Path(__file__).parent
NOTE_FILE: Path = DATA_DIR / "notes.json"


def main() -> None:
    # 启动时从文件加载笔记（文件不存在就给空列表）
    notes: list[dict] = []
    if NOTE_FILE.exists():
        with open(NOTE_FILE, "r", encoding="utf-8") as f:
            notes = json.load(f)  # json.load 直接把文件还原成 list[dict]
    print(f"已加载 {len(notes)} 条笔记")

    while True:
        print("\n*** 笔记管理器 ***")
        print("1. 写新笔记")
        print("2. 查看所有笔记")
        print("3. 搜索笔记")
        print("4. 退出")
        choice: str = input("请选择: ").strip()

        if choice == "1":
            # ---- 写新笔记 ----
            content: str = input("笔记内容: ").strip()
            if content == "":
                print("  内容不能为空")
                continue

            tags_str: str = input("标签（用逗号分隔）: ").strip()
            tags: list[str] = []
            if tags_str != "":
                for t in tags_str.split(","):
                    t = t.strip()
                    if t != "":
                        tags.append(t)

            note: dict = {
                "date": input("日期: ").strip(),
                "content": content,
                "tags": tags,
            }
            notes.append(note)
            print(f"  已保存！当前共 {len(notes)} 条笔记")

        elif choice == "2":
            # ---- 查看所有笔记 ----
            if len(notes) == 0:
                print("  暂无笔记")
            else:
                print(f"\n共 {len(notes)} 条笔记:")
                for i, note in enumerate(notes):
                    tags_str: str = ", ".join(note["tags"])
                    print(f"  [{i + 1}] {note['date']}  {note['content']}")
                    if note["tags"]:
                        print(f"      标签: {tags_str}")

        elif choice == "3":
            # ---- 搜索笔记 ----
            keyword: str = input("搜索关键词: ").strip().lower()
            if keyword == "":
                print("  关键词不能为空")
                continue

            found_count: int = 0
            for note in notes:
                content_lower: str = note["content"].lower()
                if keyword in content_lower:
                    print(f"  [{note['date']}] {note['content']}")
                    found_count += 1
                else:
                    # 也搜一下标签
                    for tag in note["tags"]:
                        if keyword in tag.lower():
                            print(f"  [{note['date']}] {note['content']}  (标签匹配)")
                            found_count += 1
                            break

            if found_count == 0:
                print(f"  未找到包含「{keyword}」的笔记")
            else:
                print(f"  共找到 {found_count} 条")

        elif choice == "4":
            # ---- 退出前保存 ----
            with open(NOTE_FILE, "w", encoding="utf-8") as f:
                json.dump(notes, f)
            print(f"已保存 {len(notes)} 条笔记，再见！")
            break

        else:
            print("  请输入 1-4")


if __name__ == "__main__":
    main()
