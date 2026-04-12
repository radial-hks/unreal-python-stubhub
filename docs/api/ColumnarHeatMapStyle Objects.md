## ColumnarHeatMapStyle Objects

```python
class ColumnarHeatMapStyle(StructBase)
```

Columnar Heat Map Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ColumnarHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``brush_diameter`` (float):  [Read-Write] cube:方柱, cylinder:圆柱, needle:针状, frame:线框
- ``columnar_width`` (float):  [Read-Write]
- ``enable_gap`` (bool):  [Read-Write]
- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``mapping_height_range`` (Vector2D):  [Read-Write]
- ``mapping_value_range`` (Vector2D):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.ColumnarHeatMapStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: str = "",
             brush_diameter: float = 0.000000,
             mapping_value_range: Vector2D = [0.000000, 0.000000],
             columnar_width: float = 0.000000,
             mapping_height_range: Vector2D = [0.000000, 0.000000],
             enable_gap: bool = False,
             gradient_setting: Array[str] = []) -> None
```

<a id="unreal.ColumnarHeatMapStyle.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.ColumnarHeatMapStyle.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.ColumnarHeatMapStyle.brush_diameter"></a>

#### brush\_diameter

```python
@property
def brush_diameter() -> float
```

(float):  [Read-Write] cube:方柱, cylinder:圆柱, needle:针状, frame:线框

<a id="unreal.ColumnarHeatMapStyle.brush_diameter"></a>

#### brush\_diameter

```python
@brush_diameter.setter
def brush_diameter(value: float) -> None
```

<a id="unreal.ColumnarHeatMapStyle.mapping_value_range"></a>

#### mapping\_value\_range

```python
@property
def mapping_value_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.ColumnarHeatMapStyle.mapping_value_range"></a>

#### mapping\_value\_range

```python
@mapping_value_range.setter
def mapping_value_range(value: Vector2D) -> None
```

<a id="unreal.ColumnarHeatMapStyle.columnar_width"></a>

#### columnar\_width

```python
@property
def columnar_width() -> float
```

(float):  [Read-Write]

<a id="unreal.ColumnarHeatMapStyle.columnar_width"></a>

#### columnar\_width

```python
@columnar_width.setter
def columnar_width(value: float) -> None
```

<a id="unreal.ColumnarHeatMapStyle.mapping_height_range"></a>

#### mapping\_height\_range

```python
@property
def mapping_height_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.ColumnarHeatMapStyle.mapping_height_range"></a>

#### mapping\_height\_range

```python
@mapping_height_range.setter
def mapping_height_range(value: Vector2D) -> None
```

<a id="unreal.ColumnarHeatMapStyle.enable_gap"></a>

#### enable\_gap

```python
@property
def enable_gap() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ColumnarHeatMapStyle.enable_gap"></a>

#### enable\_gap

```python
@enable_gap.setter
def enable_gap(value: bool) -> None
```

<a id="unreal.ColumnarHeatMapStyle.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.ColumnarHeatMapStyle.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.CreateColumnarHeatMapParams"></a>