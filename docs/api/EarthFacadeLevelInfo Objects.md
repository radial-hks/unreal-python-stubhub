## EarthFacadeLevelInfo Objects

```python
class EarthFacadeLevelInfo(StructBase)
```

用于立面拼装的层信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFacadeFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``grammar`` (str):  [Read-Write] 层的模块语法
- ``height`` (float):  [Read-Write] 层的高度
- ``scalable`` (bool):  [Read-Write] 层是否可以缩放以适应剩余空间
- ``symbol`` (Name):  [Read-Write] 层在形状语法中的符号表示
- ``transform`` (Transform):  [Read-Write] 层的变换信息
- ``use_as_placeholder`` (bool):  [Read-Write] 层是否作为占位符使用

<a id="unreal.EarthFacadeLevelInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    symbol: Name = "None",
    grammar: str = "",
    height: float = 0.000000,
    scalable: bool = False,
    use_as_placeholder: bool = False,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.EarthFacadeLevelInfo.symbol"></a>

#### symbol

```python
@property
def symbol() -> Name
```

(Name):  [Read-Write] 层在形状语法中的符号表示

<a id="unreal.EarthFacadeLevelInfo.symbol"></a>

#### symbol

```python
@symbol.setter
def symbol(value: Name) -> None
```

<a id="unreal.EarthFacadeLevelInfo.grammar"></a>

#### grammar

```python
@property
def grammar() -> str
```

(str):  [Read-Write] 层的模块语法

<a id="unreal.EarthFacadeLevelInfo.grammar"></a>

#### grammar

```python
@grammar.setter
def grammar(value: str) -> None
```

<a id="unreal.EarthFacadeLevelInfo.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 层的高度

<a id="unreal.EarthFacadeLevelInfo.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.EarthFacadeLevelInfo.scalable"></a>

#### scalable

```python
@property
def scalable() -> bool
```

(bool):  [Read-Write] 层是否可以缩放以适应剩余空间

<a id="unreal.EarthFacadeLevelInfo.scalable"></a>

#### scalable

```python
@scalable.setter
def scalable(value: bool) -> None
```

<a id="unreal.EarthFacadeLevelInfo.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@property
def use_as_placeholder() -> bool
```

(bool):  [Read-Write] 层是否作为占位符使用

<a id="unreal.EarthFacadeLevelInfo.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@use_as_placeholder.setter
def use_as_placeholder(value: bool) -> None
```

<a id="unreal.EarthFacadeLevelInfo.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] 层的变换信息

<a id="unreal.EarthFacadeLevelInfo.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.EarthFacadeBaseFragment"></a>