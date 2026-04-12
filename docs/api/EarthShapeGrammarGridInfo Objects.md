## EarthShapeGrammarGridInfo Objects

```python
class EarthShapeGrammarGridInfo(StructBase)
```

定义用于形状语法的网格信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthShapeGrammarFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bottom_level`` (str):  [Read-Write] 网格底部层名称
- ``level_grammar`` (str):  [Read-Write] 网格的层语法
- ``top_level`` (str):  [Read-Write] 网格顶部层名称
- ``weight`` (float):  [Read-Write] 网格权重

<a id="unreal.EarthShapeGrammarGridInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(level_grammar: str = "",
             bottom_level: str = "",
             top_level: str = "",
             weight: float = 0.000000) -> None
```

<a id="unreal.EarthShapeGrammarGridInfo.level_grammar"></a>

#### level\_grammar

```python
@property
def level_grammar() -> str
```

(str):  [Read-Write] 网格的层语法

<a id="unreal.EarthShapeGrammarGridInfo.level_grammar"></a>

#### level\_grammar

```python
@level_grammar.setter
def level_grammar(value: str) -> None
```

<a id="unreal.EarthShapeGrammarGridInfo.bottom_level"></a>

#### bottom\_level

```python
@property
def bottom_level() -> str
```

(str):  [Read-Write] 网格底部层名称

<a id="unreal.EarthShapeGrammarGridInfo.bottom_level"></a>

#### bottom\_level

```python
@bottom_level.setter
def bottom_level(value: str) -> None
```

<a id="unreal.EarthShapeGrammarGridInfo.top_level"></a>

#### top\_level

```python
@property
def top_level() -> str
```

(str):  [Read-Write] 网格顶部层名称

<a id="unreal.EarthShapeGrammarGridInfo.top_level"></a>

#### top\_level

```python
@top_level.setter
def top_level(value: str) -> None
```

<a id="unreal.EarthShapeGrammarGridInfo.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] 网格权重

<a id="unreal.EarthShapeGrammarGridInfo.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.EarthFacadeFragment_Deprecated"></a>