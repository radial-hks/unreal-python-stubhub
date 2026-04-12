## AesFacadeStyleData Objects

```python
class AesFacadeStyleData(StructBase)
```

立面风格信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: AesBuildingCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (Color):  [Read-Write] 立面颜色
- ``height`` (float):  [Read-Write] 立面高度
- ``id`` (int64):  [Read-Only] 立面Id
- ``levels`` (int32):  [Read-Write] 立面层数
- ``name`` (Name):  [Read-Write] 立面名称
- ``orientation`` (FacadeOrientation):  [Read-Write] 立面朝向类型
- ``width`` (float):  [Read-Write] 立面宽度

<a id="unreal.AesFacadeStyleData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: Name = "None",
             orientation: FacadeOrientation = FacadeOrientation.FRONT,
             width: float = 0.000000,
             height: float = 0.000000,
             levels: int = 0,
             color: Color = [0, 0, 0, 0]) -> None
```

<a id="unreal.AesFacadeStyleData.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] 立面名称

<a id="unreal.AesFacadeStyleData.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.AesFacadeStyleData.orientation"></a>

#### orientation

```python
@property
def orientation() -> FacadeOrientation
```

(FacadeOrientation):  [Read-Write] 立面朝向类型

<a id="unreal.AesFacadeStyleData.orientation"></a>

#### orientation

```python
@orientation.setter
def orientation(value: FacadeOrientation) -> None
```

<a id="unreal.AesFacadeStyleData.width"></a>

#### width

```python
@property
def width() -> float
```

(float):  [Read-Write] 立面宽度

<a id="unreal.AesFacadeStyleData.width"></a>

#### width

```python
@width.setter
def width(value: float) -> None
```

<a id="unreal.AesFacadeStyleData.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 立面高度

<a id="unreal.AesFacadeStyleData.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesFacadeStyleData.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] 立面层数

<a id="unreal.AesFacadeStyleData.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.AesFacadeStyleData.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write] 立面颜色

<a id="unreal.AesFacadeStyleData.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.AesMaterialLevelRange"></a>