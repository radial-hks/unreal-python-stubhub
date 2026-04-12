## AesBuildingDimensionData Objects

```python
class AesBuildingDimensionData(StructBase)
```

建筑尺寸信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: AesBuildingCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``corner_width`` (float):  [Read-Write] 立面转角宽度
- ``foundation_height`` (float):  [Read-Write] 立面地基高度
- ``top_height`` (float):  [Read-Write] 立面顶端高度
- ``wall_width`` (float):  [Read-Write] 墙体单位宽度

<a id="unreal.AesBuildingDimensionData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(wall_width: float = 0.000000,
             corner_width: float = 0.000000,
             top_height: float = 0.000000,
             foundation_height: float = 0.000000) -> None
```

<a id="unreal.AesBuildingDimensionData.wall_width"></a>

#### wall\_width

```python
@property
def wall_width() -> float
```

(float):  [Read-Write] 墙体单位宽度

<a id="unreal.AesBuildingDimensionData.wall_width"></a>

#### wall\_width

```python
@wall_width.setter
def wall_width(value: float) -> None
```

<a id="unreal.AesBuildingDimensionData.corner_width"></a>

#### corner\_width

```python
@property
def corner_width() -> float
```

(float):  [Read-Write] 立面转角宽度

<a id="unreal.AesBuildingDimensionData.corner_width"></a>

#### corner\_width

```python
@corner_width.setter
def corner_width(value: float) -> None
```

<a id="unreal.AesBuildingDimensionData.top_height"></a>

#### top\_height

```python
@property
def top_height() -> float
```

(float):  [Read-Write] 立面顶端高度

<a id="unreal.AesBuildingDimensionData.top_height"></a>

#### top\_height

```python
@top_height.setter
def top_height(value: float) -> None
```

<a id="unreal.AesBuildingDimensionData.foundation_height"></a>

#### foundation\_height

```python
@property
def foundation_height() -> float
```

(float):  [Read-Write] 立面地基高度

<a id="unreal.AesBuildingDimensionData.foundation_height"></a>

#### foundation\_height

```python
@foundation_height.setter
def foundation_height(value: float) -> None
```

<a id="unreal.AesBuildingStyleData"></a>