## EarthRoadInstanceShapeGrammar Objects

```python
class EarthRoadInstanceShapeGrammar(StructBase)
```

定义由形状语法组成的立面布局的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_corner_module`` (str):  [Read-Write] 后端所用模块名称
- ``module_definition`` (Map[Name, EarthShapeGrammarModuleInfo]):  [Read-Write] 键为模块的唯一名称，值为模块信息
- ``module_grammar`` (str):  [Read-Write] 层的模块语法
- ``start_corner_module`` (str):  [Read-Write] 前端所用模块名称

<a id="unreal.EarthRoadInstanceShapeGrammar.__init__"></a>

#### \_\_init\_\_

```python
def __init__(module_definition: Map[Name, EarthShapeGrammarModuleInfo] = {},
             module_grammar: str = "",
             start_corner_module: str = "",
             end_corner_module: str = "") -> None
```

<a id="unreal.EarthRoadInstanceShapeGrammar.module_definition"></a>

#### module\_definition

```python
@property
def module_definition() -> Map[Name, EarthShapeGrammarModuleInfo]
```

(Map[Name, EarthShapeGrammarModuleInfo]):  [Read-Write] 键为模块的唯一名称，值为模块信息

<a id="unreal.EarthRoadInstanceShapeGrammar.module_definition"></a>

#### module\_definition

```python
@module_definition.setter
def module_definition(value: Map[Name, EarthShapeGrammarModuleInfo]) -> None
```

<a id="unreal.EarthRoadInstanceShapeGrammar.module_grammar"></a>

#### module\_grammar

```python
@property
def module_grammar() -> str
```

(str):  [Read-Write] 层的模块语法

<a id="unreal.EarthRoadInstanceShapeGrammar.module_grammar"></a>

#### module\_grammar

```python
@module_grammar.setter
def module_grammar(value: str) -> None
```

<a id="unreal.EarthRoadInstanceShapeGrammar.start_corner_module"></a>

#### start\_corner\_module

```python
@property
def start_corner_module() -> str
```

(str):  [Read-Write] 前端所用模块名称

<a id="unreal.EarthRoadInstanceShapeGrammar.start_corner_module"></a>

#### start\_corner\_module

```python
@start_corner_module.setter
def start_corner_module(value: str) -> None
```

<a id="unreal.EarthRoadInstanceShapeGrammar.end_corner_module"></a>

#### end\_corner\_module

```python
@property
def end_corner_module() -> str
```

(str):  [Read-Write] 后端所用模块名称

<a id="unreal.EarthRoadInstanceShapeGrammar.end_corner_module"></a>

#### end\_corner\_module

```python
@end_corner_module.setter
def end_corner_module(value: str) -> None
```

<a id="unreal.EarthInstancedSplineMeshOverrideFragment"></a>