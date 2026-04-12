## RoadHeatMapStyle Objects

```python
class RoadHeatMapStyle(StructBase)
```

Road Heat Map Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RoadHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter`` (Array[str]):  [Read-Write]
- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``mapping_value_range`` (Vector2D):  [Read-Write]
- ``type`` (str):  [Read-Write]
- ``width`` (float):  [Read-Write]

<a id="unreal.RoadHeatMapStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: str = "",
             width: float = 0.000000,
             mapping_value_range: Vector2D = [0.000000, 0.000000],
             gradient_setting: Array[str] = [],
             filter: Array[str] = []) -> None
```

<a id="unreal.RoadHeatMapStyle.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.RoadHeatMapStyle.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.RoadHeatMapStyle.width"></a>

#### width

```python
@property
def width() -> float
```

(float):  [Read-Write]

<a id="unreal.RoadHeatMapStyle.width"></a>

#### width

```python
@width.setter
def width(value: float) -> None
```

<a id="unreal.RoadHeatMapStyle.mapping_value_range"></a>

#### mapping\_value\_range

```python
@property
def mapping_value_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RoadHeatMapStyle.mapping_value_range"></a>

#### mapping\_value\_range

```python
@mapping_value_range.setter
def mapping_value_range(value: Vector2D) -> None
```

<a id="unreal.RoadHeatMapStyle.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RoadHeatMapStyle.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.RoadHeatMapStyle.filter"></a>

#### filter

```python
@property
def filter() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RoadHeatMapStyle.filter"></a>

#### filter

```python
@filter.setter
def filter(value: Array[str]) -> None
```

<a id="unreal.RoadHeatMapData"></a>