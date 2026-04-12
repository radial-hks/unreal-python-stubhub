## GeoFeatureStyle Objects

```python
class GeoFeatureStyle(StructBase)
```

Geo Feature Style

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISStyleTypeDef.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``based_on_terrain`` (bool):  [Read-Write] 表达是否贴合地形
- ``filter_color`` (str):  [Read-Write]
- ``line_style`` (GeoLineStyle):  [Read-Write]
- ``point_style`` (GeoPointStyle):  [Read-Write]
- ``polygon_style`` (GeoPolygonStyle):  [Read-Write]
- ``style_desc`` (str):  [Read-Write] StyleDesc用于描述材质和纹理等固定表现，每个材质描述对应材质+纹理+其他自定义表达规则（道路、土地类型等）

<a id="unreal.GeoFeatureStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(style_desc: str = "",
             based_on_terrain: bool = False,
             polygon_style: GeoPolygonStyle = [
                 "#FFFFFFFF", False, "#FFFFFFFF", 1.000000, False, 100.000000,
                 "Elevation"
             ],
             line_style: GeoLineStyle = ["#FFFFFFFF", 1.000000, "Plane"],
             point_style: GeoPointStyle = ["#FFFFFFFF", 5.000000, "Circle"],
             filter_color: str = "") -> None
```

<a id="unreal.GeoFeatureStyle.style_desc"></a>

#### style\_desc

```python
@property
def style_desc() -> str
```

(str):  [Read-Write] StyleDesc用于描述材质和纹理等固定表现，每个材质描述对应材质+纹理+其他自定义表达规则（道路、土地类型等）

<a id="unreal.GeoFeatureStyle.style_desc"></a>

#### style\_desc

```python
@style_desc.setter
def style_desc(value: str) -> None
```

<a id="unreal.GeoFeatureStyle.based_on_terrain"></a>

#### based\_on\_terrain

```python
@property
def based_on_terrain() -> bool
```

(bool):  [Read-Write] 表达是否贴合地形

<a id="unreal.GeoFeatureStyle.based_on_terrain"></a>

#### based\_on\_terrain

```python
@based_on_terrain.setter
def based_on_terrain(value: bool) -> None
```

<a id="unreal.GeoFeatureStyle.polygon_style"></a>

#### polygon\_style

```python
@property
def polygon_style() -> GeoPolygonStyle
```

(GeoPolygonStyle):  [Read-Write]

<a id="unreal.GeoFeatureStyle.polygon_style"></a>

#### polygon\_style

```python
@polygon_style.setter
def polygon_style(value: GeoPolygonStyle) -> None
```

<a id="unreal.GeoFeatureStyle.line_style"></a>

#### line\_style

```python
@property
def line_style() -> GeoLineStyle
```

(GeoLineStyle):  [Read-Write]

<a id="unreal.GeoFeatureStyle.line_style"></a>

#### line\_style

```python
@line_style.setter
def line_style(value: GeoLineStyle) -> None
```

<a id="unreal.GeoFeatureStyle.point_style"></a>

#### point\_style

```python
@property
def point_style() -> GeoPointStyle
```

(GeoPointStyle):  [Read-Write]

<a id="unreal.GeoFeatureStyle.point_style"></a>

#### point\_style

```python
@point_style.setter
def point_style(value: GeoPointStyle) -> None
```

<a id="unreal.GeoFeatureStyle.filter_color"></a>

#### filter\_color

```python
@property
def filter_color() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoFeatureStyle.filter_color"></a>

#### filter\_color

```python
@filter_color.setter
def filter_color(value: str) -> None
```

<a id="unreal.GeoFeatureSymbol"></a>