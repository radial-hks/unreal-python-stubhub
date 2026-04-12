## HeatMapStyle Objects

```python
class HeatMapStyle(StructBase)
```

Heat Map Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``brush_diameter`` (float):  [Read-Write]
- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``mapping_height_range`` (Vector2D):  [Read-Write]
- ``mapping_value_range`` (Vector2D):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.HeatMapStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: str = "",
             brush_diameter: float = 0.000000,
             mapping_height_range: Vector2D = [0.000000, 0.000000],
             mapping_value_range: Vector2D = [0.000000, 0.000000],
             gradient_setting: Array[str] = []) -> None
```

<a id="unreal.HeatMapStyle.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.HeatMapStyle.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.HeatMapStyle.brush_diameter"></a>

#### brush\_diameter

```python
@property
def brush_diameter() -> float
```

(float):  [Read-Write]

<a id="unreal.HeatMapStyle.brush_diameter"></a>

#### brush\_diameter

```python
@brush_diameter.setter
def brush_diameter(value: float) -> None
```

<a id="unreal.HeatMapStyle.mapping_height_range"></a>

#### mapping\_height\_range

```python
@property
def mapping_height_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.HeatMapStyle.mapping_height_range"></a>

#### mapping\_height\_range

```python
@mapping_height_range.setter
def mapping_height_range(value: Vector2D) -> None
```

<a id="unreal.HeatMapStyle.mapping_value_range"></a>

#### mapping\_value\_range

```python
@property
def mapping_value_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.HeatMapStyle.mapping_value_range"></a>

#### mapping\_value\_range

```python
@mapping_value_range.setter
def mapping_value_range(value: Vector2D) -> None
```

<a id="unreal.HeatMapStyle.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.HeatMapStyle.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.HeatMapData"></a>