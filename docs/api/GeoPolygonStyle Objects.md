## GeoPolygonStyle Objects

```python
class GeoPolygonStyle(StructBase)
```

Geo Polygon Style

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISStyleTypeDef.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``extrude`` (bool):  [Read-Write]
- ``extrude_height`` (double):  [Read-Write]
- ``extrude_height_field`` (str):  [Read-Write]
- ``filled_color`` (str):  [Read-Write] 支持透明度表达
- ``outline`` (bool):  [Read-Write]
- ``outline_color`` (str):  [Read-Write]
- ``outline_width`` (float):  [Read-Write]

<a id="unreal.GeoPolygonStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(filled_color: str = "",
             outline: bool = False,
             outline_color: str = "",
             outline_width: float = 0.000000,
             extrude: bool = False,
             extrude_height: float = 0.000000,
             extrude_height_field: str = "") -> None
```

<a id="unreal.GeoPolygonStyle.filled_color"></a>

#### filled\_color

```python
@property
def filled_color() -> str
```

(str):  [Read-Write] 支持透明度表达

<a id="unreal.GeoPolygonStyle.filled_color"></a>

#### filled\_color

```python
@filled_color.setter
def filled_color(value: str) -> None
```

<a id="unreal.GeoPolygonStyle.outline"></a>

#### outline

```python
@property
def outline() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeoPolygonStyle.outline"></a>

#### outline

```python
@outline.setter
def outline(value: bool) -> None
```

<a id="unreal.GeoPolygonStyle.outline_color"></a>

#### outline\_color

```python
@property
def outline_color() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoPolygonStyle.outline_color"></a>

#### outline\_color

```python
@outline_color.setter
def outline_color(value: str) -> None
```

<a id="unreal.GeoPolygonStyle.outline_width"></a>

#### outline\_width

```python
@property
def outline_width() -> float
```

(float):  [Read-Write]

<a id="unreal.GeoPolygonStyle.outline_width"></a>

#### outline\_width

```python
@outline_width.setter
def outline_width(value: float) -> None
```

<a id="unreal.GeoPolygonStyle.extrude"></a>

#### extrude

```python
@property
def extrude() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeoPolygonStyle.extrude"></a>

#### extrude

```python
@extrude.setter
def extrude(value: bool) -> None
```

<a id="unreal.GeoPolygonStyle.extrude_height"></a>

#### extrude\_height

```python
@property
def extrude_height() -> float
```

(double):  [Read-Write]

<a id="unreal.GeoPolygonStyle.extrude_height"></a>

#### extrude\_height

```python
@extrude_height.setter
def extrude_height(value: float) -> None
```

<a id="unreal.GeoPolygonStyle.extrude_height_field"></a>

#### extrude\_height\_field

```python
@property
def extrude_height_field() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoPolygonStyle.extrude_height_field"></a>

#### extrude\_height\_field

```python
@extrude_height_field.setter
def extrude_height_field(value: str) -> None
```

<a id="unreal.GeoPointStyle"></a>