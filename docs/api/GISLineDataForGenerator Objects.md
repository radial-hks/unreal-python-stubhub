## GISLineDataForGenerator Objects

```python
class GISLineDataForGenerator(StructBase)
```

GISLine Data for Generator

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISLineDecalComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``line_style`` (GeoLineStyle):  [Read-Write]
- ``points`` (Array[Vector]):  [Read-Write]

<a id="unreal.GISLineDataForGenerator.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        points: Array[Vector] = [],
        line_style: GeoLineStyle = ["#FFFFFFFF", 1.000000, "Plane"]) -> None
```

<a id="unreal.GISLineDataForGenerator.points"></a>

#### points

```python
@property
def points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.GISLineDataForGenerator.points"></a>

#### points

```python
@points.setter
def points(value: Array[Vector]) -> None
```

<a id="unreal.GISLineDataForGenerator.line_style"></a>

#### line\_style

```python
@property
def line_style() -> GeoLineStyle
```

(GeoLineStyle):  [Read-Write]

<a id="unreal.GISLineDataForGenerator.line_style"></a>

#### line\_style

```python
@line_style.setter
def line_style(value: GeoLineStyle) -> None
```

<a id="unreal.GeoLineStyle"></a>