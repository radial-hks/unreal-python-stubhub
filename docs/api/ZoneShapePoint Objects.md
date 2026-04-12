## ZoneShapePoint Objects

```python
class ZoneShapePoint(StructBase)
```

Zone Shape Point

**C++ Source:**

- **Plugin**: ZoneGraph
- **Module**: ZoneGraph
- **File**: ZoneGraphTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``inner_turn_radius`` (float):  [Read-Write] Inner turn radius associated with this point. Used when polygon shape routing is set to 'Arcs'.
- ``lane_connection_restrictions`` (int32):  [Read-Write] Lane connection restrictions
- ``lane_profile`` (uint8):  [Read-Write] Index to external array referring to Lane Profile, or FZoneShapePoint::InheritLaneProfile if we should use Shape's lane profile.
  This is a little awkward indirection, but keeps the point memory usage in check.
- ``position`` (Vector):  [Read-Write] Position of the point
- ``reverse_lane_profile`` (bool):  [Read-Write] True of lane profile should be reversed.
- ``rotation`` (Rotator):  [Read-Write] Rotation of the point. Forward direction of the rotation matches the tangents.
  For Lane Profile points, the forward directions points into the shape so that we can match the incoming lanes rotation.
- ``tangent_length`` (float):  [Read-Write] Length of the Bezier point tangents, or cached half-width of the lane profile.
- ``type`` (FZoneShapePointType):  [Read-Write] Type of the control point

<a id="unreal.ZoneShapePoint.__init__"></a>

#### \_\_init\_\_

```python
def __init__(position: Vector = [0.000000, 0.000000, 0.000000],
             tangent_length: float = 0.000000,
             inner_turn_radius: float = 0.000000,
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             type: FZoneShapePointType = FZoneShapePointType.SHARP,
             lane_profile: int = 0,
             reverse_lane_profile: bool = False,
             lane_connection_restrictions: int = 0) -> None
```

<a id="unreal.ZoneShapePoint.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write] Position of the point

<a id="unreal.ZoneShapePoint.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.ZoneShapePoint.tangent_length"></a>

#### tangent\_length

```python
@property
def tangent_length() -> float
```

(float):  [Read-Write] Length of the Bezier point tangents, or cached half-width of the lane profile.

<a id="unreal.ZoneShapePoint.tangent_length"></a>

#### tangent\_length

```python
@tangent_length.setter
def tangent_length(value: float) -> None
```

<a id="unreal.ZoneShapePoint.inner_turn_radius"></a>

#### inner\_turn\_radius

```python
@property
def inner_turn_radius() -> float
```

(float):  [Read-Write] Inner turn radius associated with this point. Used when polygon shape routing is set to 'Arcs'.

<a id="unreal.ZoneShapePoint.inner_turn_radius"></a>

#### inner\_turn\_radius

```python
@inner_turn_radius.setter
def inner_turn_radius(value: float) -> None
```

<a id="unreal.ZoneShapePoint.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] Rotation of the point. Forward direction of the rotation matches the tangents.
For Lane Profile points, the forward directions points into the shape so that we can match the incoming lanes rotation.

<a id="unreal.ZoneShapePoint.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.ZoneShapePoint.type"></a>

#### type

```python
@property
def type() -> FZoneShapePointType
```

(FZoneShapePointType):  [Read-Write] Type of the control point

<a id="unreal.ZoneShapePoint.type"></a>

#### type

```python
@type.setter
def type(value: FZoneShapePointType) -> None
```

<a id="unreal.ZoneShapePoint.lane_profile"></a>

#### lane\_profile

```python
@property
def lane_profile() -> int
```

(uint8):  [Read-Write] Index to external array referring to Lane Profile, or FZoneShapePoint::InheritLaneProfile if we should use Shape's lane profile.
This is a little awkward indirection, but keeps the point memory usage in check.

<a id="unreal.ZoneShapePoint.lane_profile"></a>

#### lane\_profile

```python
@lane_profile.setter
def lane_profile(value: int) -> None
```

<a id="unreal.ZoneShapePoint.lane_template"></a>

#### lane\_template

```python
@property
def lane_template() -> int
```

deprecated: 'lane_template' was renamed to 'lane_profile'.

<a id="unreal.ZoneShapePoint.lane_template"></a>

#### lane\_template

```python
@lane_template.setter
def lane_template(value: int) -> None
```

<a id="unreal.ZoneShapePoint.reverse_lane_profile"></a>

#### reverse\_lane\_profile

```python
@property
def reverse_lane_profile() -> bool
```

(bool):  [Read-Write] True of lane profile should be reversed.

<a id="unreal.ZoneShapePoint.reverse_lane_profile"></a>

#### reverse\_lane\_profile

```python
@reverse_lane_profile.setter
def reverse_lane_profile(value: bool) -> None
```

<a id="unreal.ZoneShapePoint.lane_connection_restrictions"></a>

#### lane\_connection\_restrictions

```python
@property
def lane_connection_restrictions() -> int
```

(int32):  [Read-Write] Lane connection restrictions

<a id="unreal.ZoneShapePoint.lane_connection_restrictions"></a>

#### lane\_connection\_restrictions

```python
@lane_connection_restrictions.setter
def lane_connection_restrictions(value: int) -> None
```

<a id="unreal.EarthFragment"></a>