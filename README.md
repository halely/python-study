# 🐍 Python Study

> 从零开始系统学习 Python，记录学习笔记和练习代码。

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

---

## 📖 项目简介

本项目是我**系统学习 Python** 的代码仓库，包含从基础语法到进阶主题的完整学习路线。每个知识点都配有：

- 📝 **详细注释**的示例代码
- 🏋️ **动手练习**（综合运用多个知识点）
- 🎯 **真实场景模拟**（成绩分析、购物清单、文本统计等）

代码风格遵循 **PEP 8** 规范，使用 **type annotations**（类型注解）增强可读性。

---

## 📁 项目结构

```
python-study/
├── 01_basics/                     # 阶段1：基础入门
│   ├── 01_data_types.py           #   核心数据类型（list/tuple/dict/set）
│   ├── 02_loops.py                #   循环（for/while/break/continue/else）
│   ├── 03_strings.py              #   字符串操作（切片/方法/f-string/split/join）
│   ├── 04_file_io.py              #   文件读写（with/open/读写/追加/pathlib）
│   ├── exercise_shopping.py       #   练习：购物清单（数据类型）
│   ├── exercise_multiplication.py #   练习：九九乘法表（循环）
│   ├── exercise_password.py       #   练习：密码强度检查器（字符串）
│   ├── exercise_note.py           #   练习：笔记管理器v1（文件读写初版）
│   └── exercise_note_v2.py        #   练习：笔记管理器v2（json存储优化）
├── 02_functions/                  # 阶段2：函数与模块化
│   ├── 01_function_basics.py      #   函数基础（def/return/作用域/lambda）
│   ├── 02_function_advanced_args.py # 进阶参数（*args/**kwargs/默认参数陷阱）
│   ├── 03_module_basics.py        #   模块（import/__name__）
│   ├── 04_exception_handling.py   #   异常处理（try/except/finally/自定义异常）
│   ├── game_utils.py              #   工具模块（猜数字游戏的公共函数）
│   ├── calculator_ops.py          #   运算模块（命令行计算器的核心）
│   ├── exercise_bmi_function.py   #   练习：BMI 函数版
│   ├── exercise_flexible_calculator.py # 练习：灵活计算器（*args）
│   ├── exercise_guess_game_module.py  # 练习：健壮版猜数字（模块+异常）
│   └── exercise_calculator.py     #   综合项目：命令行计算器
├── demo/
│   └── BMI.py                     # 综合练习：BMI 计算器（入门作）
├── text.py                        # 小练习：一元二次方程
├── .gitignore
└── README.md
```

---

## 🎯 学习路线图

### ✅ 阶段 1：基础入门（已完成 — 2026-06-01）

- [x] 核心数据类型：`list`、`tuple`、`dict`、`set` + 列表/字典/集合推导式
- [x] 循环与控制流：`for`、`while`、`break`、`continue`、`else`
- [x] 字符串操作：切片、常用方法、f-string、split/join
- [x] 文件读写：`with open()`、读写/追加模式、`pathlib`、`json` 持久化
- [x] 综合练习：班级成绩分析、猜数字游戏、文本统计分析、购物清单、乘法表、密码检查器、笔记管理器

### ✅ 阶段 2：函数与模块（已完成 — 2026-06-17）

- [x] 函数基础：`def`、`return`、多返回值、作用域 LEGB、`lambda`
- [x] 参数进阶：`*args`、`**kwargs`、默认参数（可变对象陷阱）、解包运算符
- [x] 模块：`import`、`from ... import`、`__name__ == "__main__"`
- [x] 异常处理：`try/except/else/finally`、`raise`、自定义异常、健壮输入验证
- [x] 综合项目：命令行计算器（模块化拆分 + 字典映射 + 历史记录）

### 🚧 阶段 3：面向对象编程（下一步）

- [ ] 函数定义与作用域（`def`、`lambda`、闭包）
- [ ] 参数进阶（`*args`、`**kwargs`、默认参数、类型提示）
- [ ] 模块与包管理（`import`、`__name__`、pip、虚拟环境）
- [ ] 异常处理（`try/except/else/finally`、自定义异常）
- [ ] 常用内置函数（`map`、`filter`、`sorted`、`enumerate`、`zip`）

### 📋 阶段 3：面向对象编程

- [ ] 类与对象（`class`、`__init__`、`self`）
- [ ] 继承与多态
- [ ] 魔术方法（`__str__`、`__repr__`、`__eq__` 等）
- [ ] 属性装饰器（`@property`、`@staticmethod`、`@classmethod`）
- [ ] 数据类（`dataclass`、`NamedTuple`）

### 📋 阶段 4：实用技能

- [ ] 常用标准库（`datetime`、`collections`、`random`、`itertools`）
- [ ] 第三方库入门（`requests`、`pandas`）
- [ ] 日志记录（`logging` 模块）
- [ ] 命令行参数（`argparse`）

### 📋 阶段 5：进阶主题

- [ ] 迭代器与生成器（`yield`、`itertools`）
- [ ] 装饰器（`@decorator`、带参数装饰器）
- [ ] 上下文管理器（`with` 语句、`contextlib`）
- [ ] 并发编程入门（`threading`、`asyncio`）
- [ ] 类型系统深入（`Protocol`、`Generic`、`TypeVar`）

### 📋 阶段 6：实战项目

- [ ] 命令行工具（argparse、Click）
- [ ] Web API 开发（FastAPI / Flask）
- [ ] 数据库操作（SQLAlchemy / SQLite）
- [ ] 网络爬虫（requests + BeautifulSoup）
- [ ] 数据分析初探（pandas + matplotlib）
- [ ] 单元测试（pytest + coverage）

---

## 🚀 快速开始

```bash
# 克隆仓库
git clone git@github.com:halely/python-study.git
cd python-study

# 运行示例（任意文件都可以直接执行）
python 01_basics/01_data_types.py
python 01_basics/02_loops.py
python 01_basics/03_strings.py

# 运行 BMI 计算器（交互式）
python BMI.py
```

> 推荐使用 **Python 3.11+** 以获得最佳体验。

---

## 💡 学习建议

1. **先看后练**：每个文件都有详细注释，先运行看效果，再自己修改参数试试
2. **跟着综合练习做**：每个文件的最后都有一个综合练习，把多个知识点串起来
3. **善用交互环境**：打开 `python` REPL 或使用 Jupyter Notebook 边学边试
4. **多动手改代码**：把示例代码改一改、拆一拆，看会有什么变化

---

## 📚 推荐资源

| 资源 | 说明 |
|------|------|
| [Python 官方文档](https://docs.python.org/zh-cn/3/) | 最好的参考手册 |
| [Real Python](https://realpython.com/) | 高质量英文教程 |
| [Python Cheatsheet](https://www.pythoncheatsheet.org/) | 速查表 |

---

## 📝 许可证

MIT License — 欢迎自由学习和使用。

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
