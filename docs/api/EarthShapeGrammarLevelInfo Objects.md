## EarthShapeGrammarLevelInfo Objects

```python
class EarthShapeGrammarLevelInfo(StructBase)
```

定义用于形状语法的层信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthShapeGrammarFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``height`` (float):  [Read-Write] 层高度
- ``left_corner_module`` (str):  [Read-Write] 层左角所用模块名称
- ``min_scale_factor`` (float):  [Read-Write] 最小缩放因子
- ``module_grammar`` (str):  [Read-Write] 层的模块语法
- ``position_offset`` (Vector):  [Read-Write] 层偏移值
- ``right_corner_module`` (str):  [Read-Write] 层右角所用模块名称
- ``scalable`` (bool):  [Read-Write] 层是否可以缩放以适应剩余空间
- ``symbol`` (Name):  [Read-Write] 模块在形状语法中的符号
- ``variations`` (Map[Name, float]):  [Read-Write] 层变体列表
- ``weight`` (float):  [Read-Write] 层权重

<a id="unreal.EarthShapeGrammarLevelInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(symbol: Name = "None",
             module_grammar: str = "",
             left_corner_module: str = "",
             right_corner_module: str = "",
             height: float = 0.000000,
             weight: float = 0.000000,
             min_scale_factor: float = 0.000000,
             scalable: bool = False,
             position_offset: Vector = [0.000000, 0.000000, 0.000000],
             variations: Map[Name, float] = {}) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.symbol"></a>

#### symbol

```python
@property
def symbol() -> Name
```

(Name):  [Read-Write] 模块在形状语法中的符号

<a id="unreal.EarthShapeGrammarLevelInfo.symbol"></a>

#### symbol

```python
@symbol.setter
def symbol(value: Name) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.module_grammar"></a>

#### module\_grammar

```python
@property
def module_grammar() -> str
```

(str):  [Read-Write] 层的模块语法

<a id="unreal.EarthShapeGrammarLevelInfo.module_grammar"></a>

#### module\_grammar

```python
@module_grammar.setter
def module_grammar(value: str) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.left_corner_module"></a>

#### left\_corner\_module

```python
@property
def left_corner_module() -> str
```

(str):  [Read-Write] 层左角所用模块名称

<a id="unreal.EarthShapeGrammarLevelInfo.left_corner_module"></a>

#### left\_corner\_module

```python
@left_corner_module.setter
def left_corner_module(value: str) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.right_corner_module"></a>

#### right\_corner\_module

```python
@property
def right_corner_module() -> str
```

(str):  [Read-Write] 层右角所用模块名称

<a id="unreal.EarthShapeGrammarLevelInfo.right_corner_module"></a>

#### right\_corner\_module

```python
@right_corner_module.setter
def right_corner_module(value: str) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 层高度

<a id="unreal.EarthShapeGrammarLevelInfo.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] 层权重

<a id="unreal.EarthShapeGrammarLevelInfo.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.min_scale_factor"></a>

#### min\_scale\_factor

```python
@property
def min_scale_factor() -> float
```

(float):  [Read-Write] 最小缩放因子

<a id="unreal.EarthShapeGrammarLevelInfo.min_scale_factor"></a>

#### min\_scale\_factor

```python
@min_scale_factor.setter
def min_scale_factor(value: float) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.scalable"></a>

#### scalable

```python
@property
def scalable() -> bool
```

(bool):  [Read-Write] 层是否可以缩放以适应剩余空间

<a id="unreal.EarthShapeGrammarLevelInfo.scalable"></a>

#### scalable

```python
@scalable.setter
def scalable(value: bool) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.position_offset"></a>

#### position\_offset

```python
@property
def position_offset() -> Vector
```

(Vector):  [Read-Write] 层偏移值

<a id="unreal.EarthShapeGrammarLevelInfo.position_offset"></a>

#### position\_offset

```python
@position_offset.setter
def position_offset(value: Vector) -> None
```

<a id="unreal.EarthShapeGrammarLevelInfo.variations"></a>

#### variations

```python
@property
def variations() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write] 层变体列表

<a id="unreal.EarthShapeGrammarLevelInfo.variations"></a>

#### variations

```python
@variations.setter
def variations(value: Map[Name, float]) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo"></a>