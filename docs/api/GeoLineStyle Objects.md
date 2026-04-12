## GeoLineStyle Objects

```python
class GeoLineStyle(StructBase)
```

Geo Line Style

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISStyleTypeDef.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``line_color`` (str):  [Read-Write] 支持透明度表达
- ``line_shape`` (str):  [Read-Write] Plane/Pipe/Rect...
- ``line_width`` (float):  [Read-Write]

<a id="unreal.GeoLineStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(line_color: str = "",
             line_width: float = 0.000000,
             line_shape: str = "") -> None
```

<a id="unreal.GeoLineStyle.line_color"></a>

#### line\_color

```python
@property
def line_color() -> str
```

(str):  [Read-Write] 支持透明度表达

<a id="unreal.GeoLineStyle.line_color"></a>

#### line\_color

```python
@line_color.setter
def line_color(value: str) -> None
```

<a id="unreal.GeoLineStyle.line_width"></a>

#### line\_width

```python
@property
def line_width() -> float
```

(float):  [Read-Write]

<a id="unreal.GeoLineStyle.line_width"></a>

#### line\_width

```python
@line_width.setter
def line_width(value: float) -> None
```

<a id="unreal.GeoLineStyle.line_shape"></a>

#### line\_shape

```python
@property
def line_shape() -> str
```

(str):  [Read-Write] Plane/Pipe/Rect...

<a id="unreal.GeoLineStyle.line_shape"></a>

#### line\_shape

```python
@line_shape.setter
def line_shape(value: str) -> None
```

<a id="unreal.GeoPolygonStyle"></a>