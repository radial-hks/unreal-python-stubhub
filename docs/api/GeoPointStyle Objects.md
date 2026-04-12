## GeoPointStyle Objects

```python
class GeoPointStyle(StructBase)
```

Geo Point Style

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISStyleTypeDef.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``point_color`` (str):  [Read-Write] 支持透明度表达
- ``point_shape`` (str):  [Read-Write] Circle/Sphere/Cube...
- ``point_size`` (float):  [Read-Write]

<a id="unreal.GeoPointStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(point_color: str = "",
             point_size: float = 0.000000,
             point_shape: str = "") -> None
```

<a id="unreal.GeoPointStyle.point_color"></a>

#### point\_color

```python
@property
def point_color() -> str
```

(str):  [Read-Write] 支持透明度表达

<a id="unreal.GeoPointStyle.point_color"></a>

#### point\_color

```python
@point_color.setter
def point_color(value: str) -> None
```

<a id="unreal.GeoPointStyle.point_size"></a>

#### point\_size

```python
@property
def point_size() -> float
```

(float):  [Read-Write]

<a id="unreal.GeoPointStyle.point_size"></a>

#### point\_size

```python
@point_size.setter
def point_size(value: float) -> None
```

<a id="unreal.GeoPointStyle.point_shape"></a>

#### point\_shape

```python
@property
def point_shape() -> str
```

(str):  [Read-Write] Circle/Sphere/Cube...

<a id="unreal.GeoPointStyle.point_shape"></a>

#### point\_shape

```python
@point_shape.setter
def point_shape(value: str) -> None
```

<a id="unreal.GeoFeatureStyle"></a>