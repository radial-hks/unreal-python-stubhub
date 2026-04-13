# Unreal Python StubHub

[![English Docs](https://img.shields.io/badge/docs-English-blue)](README.md)

本项目旨在使用 `pydoc-markdown` 工具将 `UnrealPythonAPI` 目录下的 Python 代码（主要是 Unreal Engine 的 Python API 存根）转换为 Markdown 格式的文档。

## 项目目标

为 Unreal Engine 的 Python API 提供类型存根，并通过 `pydoc-markdown` 自动生成结构清晰、易于导航的 Markdown 文档。使用 [**Context7**](https://context7.com/libraries) 解析文档，再辅以 [**Context7 MCP Server**](https://context7.com/radial-hks/unreal-python-stubhub) 时，用户可以快速生成正确、可靠的代码。

**使用示例**：

以下展示如何使用 Context7 快速实现世界大纲目录树的获取功能：

```python
# 提示词
使用unreal python 创建一个脚本 实现 获取世界大纲中目录树信息 use context7

# 生成路径：Example/get_world_outliner_tree.py
# 执行结果（Basic.level）：
- None
  - Floor
  - PlayerStart_0
- Lighting
  - DirectionalLight_0
  - SkyAtmosphere_0
  - SkyLight_0
  - ExponentialHeightFog_0
  - VolumetricCloud_0
  - StaticMeshActor_1
```

通过这种方式，开发者可以快速获取符合最佳实践的代码实现，显著提升虚幻引擎 Python 开发效率。

## 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/radial-hks/unreal-python-stubhub.git
cd unreal-python-stubhub

# 2. 安装依赖（推荐使用 uv）
uv sync

# 3. 生成文档
uv run python main.py
uv run python split_md.py

# 4. 查看生成的文档
ls docs/api/
```

## 项目架构

```
UnrealPythonAPI/unreal/    # Python API 类型存根（输入）
        ↓
    main.py                # 调用 pydoc-markdown 解析存根，生成 Markdown
        ↓
    split_md.py            # 按类拆分大型 Markdown 文件
        ↓
    docs/api/              # 15,000+ 个独立 Markdown 文档（输出）
      ├─→ Context7 MCP Server    # 供 AI 代码生成工具检索使用
      └─→ graphify               # 构建知识图谱 (26k 节点 / 26k 关系)
```

## 知识图谱 (graphify)

本项目已使用 [**graphify**](https://github.com/safishamsi/graphify) 对 `docs/api/` 下的全部 API 文档构建了知识图谱，将 15,000+ 个独立的 Markdown 文件解析为结构化的图数据。

### 图谱规模

| 指标 | 数值 |
|------|------|
| 节点数 | 26,195 |
| 关系边数 | 26,368 |
| 超边（组关系） | 2,589 |
| 文档运行 | ~700 个 chunk |

### 关系类型

图谱捕获了多种 API 关系：
- **implements** (4,997) — 类的实现关系
- **references** (3,358) — 类型之间的交叉引用
- **semantically_similar_to** (1,912) — 语义相似的 API
- **inherits_from** (489) — 继承关系
- **has_property** (929) — 属性关系
- 以及 calls、extends、uses 等其他关系类型

### 核心节点 (God Nodes)

连接度最高的核心实体：
- **StructBase** (289 连接) — 数据结构基类
- **EnumBase** (163 连接) — 枚举基类
- **Object** (105 连接) — UObject 基类

### 生成的文件

```
docs/api/graphify-out/
├── graph.html          # 交互式可视化图谱（点击节点、搜索、过滤）
├── GRAPH_REPORT.md     # 概览报告（核心节点、社区结构、关键发现）
├── graph.json          # 完整图数据（可查询）
├── stats.json          # 图谱统计信息
└── cache/              # SHA256 缓存（增量更新时跳过已处理文件）
```

### 如何使用

在 Claude Code 或 GitHub Copilot 中直接使用 graphify 命令查询 API 关系：

```bash
# 查询某个类的相关信息
graphify query "what classes inherit from Actor?"

# 查找两个类之间的关系路径
graphify path "Actor" "Pawn"

# 解释某个类的作用和关联
graphify explain "WidgetComponent"

# 在 AI 助手中使用（Claude Code / Copilot）
/graphify query "动画系统相关的类有哪些"
```

> **提示**: 安装 graphify 并执行 `graphify copilot install` 或 `graphify claude install` 后，AI 助手会自动读取 `GRAPH_REPORT.md` 作为上下文，在回答问题前先通过图谱导航而非逐文件搜索。

## 项目规则

为了确保项目顺利进行并生成高质量的文档，请遵循以下规则：

### 1. 代码风格

- **一致性**: 保持代码风格一致。虽然存根文件可能不完全遵循 PEP 8，但新增或修改的代码应尽量保持简洁和可读。
- **存根实现**: 函数和方法体可以使用 `pass` 或 `...` 作为占位符。

### 2. 文档字符串 (Docstrings)

- **必要性**: 所有公共模块、类、函数和方法都必须包含文档字符串。
- **格式**: 推荐使用 Google 风格的文档字符串，以便 `pydoc-markdown` 能正确解析。
- **内容**: 文档字符串应清晰地描述对象的功能、参数、返回值和可能引发的异常。

### 3. 目录结构

- **代码位置**: 所有 Unreal Engine Python API 存根文件必须放置在 `UnrealPythonAPI` 目录下。
- **模块组织**: 保持与 Unreal Engine 官方 Python API 相似的模块结构（例如，所有内容都在 `unreal` 模块下）。**注意: 在启用 Python 插件后会在项目缓存目录中生成一个 `unreal.py` 文件。**
- **文档输出**: 生成的 Markdown 文档位于 `docs/api/` 目录下。

### 4. 依赖管理

- **核心依赖**: 项目的核心依赖是 `pydoc-markdown`，已在 `pyproject.toml` 中定义。
- **环境**: 推荐使用 [uv](https://docs.astral.sh/uv/) 管理项目依赖和虚拟环境。
  ```bash
  # 推荐：使用 uv
  uv sync

  # 或者：使用传统 venv + pip
  python -m venv .venv
  source .venv/bin/activate  # Linux/macOS（Windows: .venv\Scripts\activate）
  pip install -e .
  ```

### 5. 文档生成

- **工具**: 使用 `pydoc-markdown` 结合自定义脚本 `main.py` 生成 Markdown 文档，再使用 `split_md.py` 将较大的 Markdown 文件按照 "Class" 拆分为多个小文件，便于更新及管理。
- **执行 (推荐)**: 运行项目根目录下的 `main.py` 脚本。该脚本会自动处理 `UnrealPythonAPI` 目录下的 `unreal` 模块，并将每个顶级类和函数的文档分别生成到 `docs/api/` 目录下的独立 Markdown 文件中，同时创建一个 `docs/api/index.md` 文件作为入口索引。
  ```bash
  python main.py
  python split_md.py
  ```
  执行后，请查看 `docs/api/` 目录以获取生成的文档。

- **其他执行方式**: 
    - **使用 `pydoc-markdown` CLI**: 直接调用命令行工具。这对于快速生成单个模块或进行特定配置测试可能有用，但推荐使用 `main.py` 以获得拆分后的文档结构。
      ```bash
      # 示例：生成 unreal 模块的完整文档（非拆分）
      pydoc-markdown -I UnrealPythonAPI -m unreal --render-toc > unreal_module_full.md
      ```
    - **使用 `pydoc-markdown` API**: 在其他 Python 脚本中调用其 API。`main.py` 就是一个使用 API 的例子。


### 6. 贡献与维护

- **准确性**: 确保添加或修改的 API 存根与实际的 Unreal Engine Python API 签名一致。
- **完整性**: 鼓励补充缺失的 API 存根和文档字符串。
- **更新**: 随着 Unreal Engine 版本的更新，及时维护和补充 API 存根。