## EarthZoneShapes Objects

```python
class EarthZoneShapes(StructBase)
```

EarthZoneShapes数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthZoneShapes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lane_profile`` (ZoneLaneProfileRef):  [Read-Write] Common lane template for whole shape
- ``points`` (Array[ZoneShapePoint]):  [Read-Write] Shape points
- ``polygon_routing_type`` (ZoneShapePolygonRoutingType):  [Read-Write] Polygon shape routing type
- ``reverse_lane_profile`` (bool):  [Read-Write] True if lane profile should be reversed
- ``shape_type`` (FZoneShapeType):  [Read-Write] Shape type, spline or polygon
- ``tags`` (ZoneGraphTagMask):  [Read-Write] Zone tags, the lanes inherit zone tags.

<a id="unreal.EarthZoneShapes.__init__"></a>

#### \_\_init\_\_

```python
def __init__(lane_profile: ZoneLaneProfileRef = ["None", []],
             reverse_lane_profile: bool = False,
             points: Array[ZoneShapePoint] = [],
             shape_type: FZoneShapeType = FZoneShapeType.SPLINE,
             polygon_routing_type:
             ZoneShapePolygonRoutingType = ZoneShapePolygonRoutingType.BEZIER,
             tags: ZoneGraphTagMask = []) -> None
```

<a id="unreal.EarthZoneShapes.lane_profile"></a>

#### lane\_profile

```python
@property
def lane_profile() -> ZoneLaneProfileRef
```

(ZoneLaneProfileRef):  [Read-Write] Common lane template for whole shape

<a id="unreal.EarthZoneShapes.lane_profile"></a>

#### lane\_profile

```python
@lane_profile.setter
def lane_profile(value: ZoneLaneProfileRef) -> None
```

<a id="unreal.EarthZoneShapes.reverse_lane_profile"></a>

#### reverse\_lane\_profile

```python
@property
def reverse_lane_profile() -> bool
```

(bool):  [Read-Write] True if lane profile should be reversed

<a id="unreal.EarthZoneShapes.reverse_lane_profile"></a>

#### reverse\_lane\_profile

```python
@reverse_lane_profile.setter
def reverse_lane_profile(value: bool) -> None
```

<a id="unreal.EarthZoneShapes.points"></a>

#### points

```python
@property
def points() -> Array[ZoneShapePoint]
```

(Array[ZoneShapePoint]):  [Read-Write] Shape points

<a id="unreal.EarthZoneShapes.points"></a>

#### points

```python
@points.setter
def points(value: Array[ZoneShapePoint]) -> None
```

<a id="unreal.EarthZoneShapes.shape_type"></a>

#### shape\_type

```python
@property
def shape_type() -> FZoneShapeType
```

(FZoneShapeType):  [Read-Write] Shape type, spline or polygon

<a id="unreal.EarthZoneShapes.shape_type"></a>

#### shape\_type

```python
@shape_type.setter
def shape_type(value: FZoneShapeType) -> None
```

<a id="unreal.EarthZoneShapes.polygon_routing_type"></a>

#### polygon\_routing\_type

```python
@property
def polygon_routing_type() -> ZoneShapePolygonRoutingType
```

(ZoneShapePolygonRoutingType):  [Read-Write] Polygon shape routing type

<a id="unreal.EarthZoneShapes.polygon_routing_type"></a>

#### polygon\_routing\_type

```python
@polygon_routing_type.setter
def polygon_routing_type(value: ZoneShapePolygonRoutingType) -> None
```

<a id="unreal.EarthZoneShapes.tags"></a>

#### tags

```python
@property
def tags() -> ZoneGraphTagMask
```

(ZoneGraphTagMask):  [Read-Write] Zone tags, the lanes inherit zone tags.

<a id="unreal.EarthZoneShapes.tags"></a>

#### tags

```python
@tags.setter
def tags(value: ZoneGraphTagMask) -> None
```

<a id="unreal.EarthPcgPointFragment"></a>