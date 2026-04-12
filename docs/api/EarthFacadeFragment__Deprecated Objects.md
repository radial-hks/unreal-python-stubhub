## EarthFacadeFragment\_Deprecated Objects

```python
class EarthFacadeFragment_Deprecated(EarthEntityFragment)
```

定义立面数据片段的结构体（已废弃）

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFacadeFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] 立面颜色
- ``height`` (float):  [Read-Write] 立面高度，单位为米
- ``height_offset`` (float):  [Read-Write] 立面高度偏移值，单位为米
- ``layouts`` (Array[InstancedStruct]):  [Read-Write] 立面布局数据
- ``level_definition`` (Map[Name, EarthShapeGrammarLevelInfo]):  [Read-Write] 键为层的唯一名称，值为层信息
- ``levels`` (int32):  [Read-Write] 立面层数
- ``module_definition`` (Map[Name, EarthShapeGrammarModuleInfo]):  [Read-Write] 键为模块的唯一名称，值为模块信息
- ``recompute_seed_by_edge`` (bool):  [Read-Write] 是否为每条边重新计算随机种子
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthFacadeFragment_Deprecated.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             height: float = 0.000000,
             height_offset: float = 0.000000,
             levels: int = 0,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             module_definition: Map[Name, EarthShapeGrammarModuleInfo] = {},
             level_definition: Map[Name, EarthShapeGrammarLevelInfo] = {},
             layouts: Array[InstancedStruct] = [],
             recompute_seed_by_edge: bool = False) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 立面高度，单位为米

<a id="unreal.EarthFacadeFragment_Deprecated.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated.height_offset"></a>

#### height\_offset

```python
@property
def height_offset() -> float
```

(float):  [Read-Write] 立面高度偏移值，单位为米

<a id="unreal.EarthFacadeFragment_Deprecated.height_offset"></a>

#### height\_offset

```python
@height_offset.setter
def height_offset(value: float) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] 立面层数

<a id="unreal.EarthFacadeFragment_Deprecated.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] 立面颜色

<a id="unreal.EarthFacadeFragment_Deprecated.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated.module_definition"></a>

#### module\_definition

```python
@property
def module_definition() -> Map[Name, EarthShapeGrammarModuleInfo]
```

(Map[Name, EarthShapeGrammarModuleInfo]):  [Read-Write] 键为模块的唯一名称，值为模块信息

<a id="unreal.EarthFacadeFragment_Deprecated.module_definition"></a>

#### module\_definition

```python
@module_definition.setter
def module_definition(value: Map[Name, EarthShapeGrammarModuleInfo]) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated.level_definition"></a>

#### level\_definition

```python
@property
def level_definition() -> Map[Name, EarthShapeGrammarLevelInfo]
```

(Map[Name, EarthShapeGrammarLevelInfo]):  [Read-Write] 键为层的唯一名称，值为层信息

<a id="unreal.EarthFacadeFragment_Deprecated.level_definition"></a>

#### level\_definition

```python
@level_definition.setter
def level_definition(value: Map[Name, EarthShapeGrammarLevelInfo]) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated.layouts"></a>

#### layouts

```python
@property
def layouts() -> Array[InstancedStruct]
```

(Array[InstancedStruct]):  [Read-Write] 立面布局数据

<a id="unreal.EarthFacadeFragment_Deprecated.layouts"></a>

#### layouts

```python
@layouts.setter
def layouts(value: Array[InstancedStruct]) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated.recompute_seed_by_edge"></a>

#### recompute\_seed\_by\_edge

```python
@property
def recompute_seed_by_edge() -> bool
```

(bool):  [Read-Write] 是否为每条边重新计算随机种子

<a id="unreal.EarthFacadeFragment_Deprecated.recompute_seed_by_edge"></a>

#### recompute\_seed\_by\_edge

```python
@recompute_seed_by_edge.setter
def recompute_seed_by_edge(value: bool) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo"></a>