## AvaRadialArrangeModifier Objects

```python
class AvaRadialArrangeModifier(AvaArrangeBaseModifier)
```

Arranges child actors in a circular rings around its center

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaRadialArrangeModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``arrangement`` (AvaRadialArrangement):  [Read-Write] Defines how to arrange the child elements around the center.
- ``base_orientation`` (Rotator):  [Read-Write] Base rotation added on top of the orientation rotation computed
- ``count`` (int32):  [Read-Write] The number of child elements to limit in the arrangement, or -1 if unlimited. Children whose index is greater than or equal to this value will be hidden.
- ``end_angle`` (float):  [Read-Write] The end angle for the arrangement space. 0 = Up, -90 = Left, 90 = Right
- ``flip_orient`` (bool):  [Read-Write] If true, will flip the orientation axis to the opposite direction.
- ``inner_radius`` (float):  [Read-Write] The radius from the center to the first inner ring.
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``orient`` (bool):  [Read-Write] If true, will orient the selected axis torwards the center.
- ``orient_axis`` (AvaAxis):  [Read-Write]
  deprecated: Use OrientationAxis instead
- ``orientation_axis`` (AvaModifiersAxis):  [Read-Write] The axis to look at the center.
- ``outer_radius`` (float):  [Read-Write] The radius from the center to the last outer ring.
- ``rings`` (int32):  [Read-Write] The number of rings.
- ``start_angle`` (float):  [Read-Write] The start angle for the arrangement space and moving clockwise. 0 = Up, -90 = Left, 90 = Right
- ``start_from_outer_radius`` (bool):  [Read-Write] If true, will arrange the child elements starting from the outer radius and moving to the inner radius. Has no effect if only using one ring.

<a id="unreal.AvaRadialArrangeModifier.inner_radius"></a>

#### inner_radius

```python
@property
def inner_radius() -> float
```

(float):  [Read-Write] The radius from the center to the first inner ring.

<a id="unreal.AvaRadialArrangeModifier.inner_radius"></a>

#### inner_radius

```python
@inner_radius.setter
def inner_radius(value: float) -> None
```

<a id="unreal.AvaRadialArrangeModifier.outer_radius"></a>

#### outer_radius

```python
@property
def outer_radius() -> float
```

(float):  [Read-Write] The radius from the center to the last outer ring.

<a id="unreal.AvaRadialArrangeModifier.outer_radius"></a>

#### outer_radius

```python
@outer_radius.setter
def outer_radius(value: float) -> None
```

<a id="unreal.AvaRadialArrangeModifier.start_angle"></a>

#### start_angle

```python
@property
def start_angle() -> float
```

(float):  [Read-Write] The start angle for the arrangement space and moving clockwise. 0 = Up, -90 = Left, 90 = Right

<a id="unreal.AvaRadialArrangeModifier.start_angle"></a>

#### start_angle

```python
@start_angle.setter
def start_angle(value: float) -> None
```

<a id="unreal.AvaRadialArrangeModifier.end_angle"></a>

#### end_angle

```python
@property
def end_angle() -> float
```

(float):  [Read-Write] The end angle for the arrangement space. 0 = Up, -90 = Left, 90 = Right

<a id="unreal.AvaRadialArrangeModifier.end_angle"></a>

#### end_angle

```python
@end_angle.setter
def end_angle(value: float) -> None
```

<a id="unreal.AvaRadialArrangeModifier.orient_axis"></a>

#### orient_axis

```python
@property
def orient_axis() -> AvaAxis
```

(AvaAxis):  [Read-Write]
deprecated: Use OrientationAxis instead

<a id="unreal.AvaRadialArrangeModifier.orient_axis"></a>

#### orient_axis

```python
@orient_axis.setter
def orient_axis(value: AvaAxis) -> None
```

<a id="unreal.AvaRadialArrangeModifier.set_start_from_outer_radius"></a>

#### set_start_from_outer_radius

```python
def set_start_from_outer_radius(start_from_outer_radius: bool) -> None
```

x.set_start_from_outer_radius(start_from_outer_radius) -> None
If true, will arrange the child elements starting from the outer radius and moving to the inner radius. Has no effect if only using one ring.

Args:
    start_from_outer_radius (bool):

<a id="unreal.AvaRadialArrangeModifier.set_start_angle"></a>

#### set_start_angle

```python
def set_start_angle(start_angle: float) -> None
```

x.set_start_angle(start_angle) -> None
Sets the start angle for the arrangement space and moving clockwise. 0 = Up, -90 = Left, 90 = Right

Args:
    start_angle (float):

<a id="unreal.AvaRadialArrangeModifier.set_rings"></a>

#### set_rings

```python
def set_rings(rings: int) -> None
```

x.set_rings(rings) -> None
Sets the number of rings.

Args:
    rings (int32):

<a id="unreal.AvaRadialArrangeModifier.set_outer_radius"></a>

#### set_outer_radius

```python
def set_outer_radius(outer_radius: float) -> None
```

x.set_outer_radius(outer_radius) -> None
Sets the radius from the center to the last outer ring.

Args:
    outer_radius (float):

<a id="unreal.AvaRadialArrangeModifier.set_orientation_axis"></a>

#### set_orientation_axis

```python
def set_orientation_axis(axis: AvaModifiersAxis) -> None
```

x.set_orientation_axis(axis) -> None
Sets the axis to look at the center.

Args:
    axis (AvaModifiersAxis):

<a id="unreal.AvaRadialArrangeModifier.set_orient"></a>

#### set_orient

```python
def set_orient(orient: bool) -> None
```

x.set_orient(orient) -> None
If true, will orient the selected axis torwards the center.

Args:
    orient (bool):

<a id="unreal.AvaRadialArrangeModifier.set_inner_radius"></a>

#### set_inner_radius

```python
def set_inner_radius(inner_radius: float) -> None
```

x.set_inner_radius(inner_radius) -> None
Sets the radius from the center to the first inner ring.

Args:
    inner_radius (float):

<a id="unreal.AvaRadialArrangeModifier.set_flip_orient"></a>

#### set_flip_orient

```python
def set_flip_orient(flip_orient: bool) -> None
```

x.set_flip_orient(flip_orient) -> None
If true, will flip the center orientation to face outwards.

Args:
    flip_orient (bool):

<a id="unreal.AvaRadialArrangeModifier.set_end_angle"></a>

#### set_end_angle

```python
def set_end_angle(end_angle: float) -> None
```

x.set_end_angle(end_angle) -> None
Sets the end angle for the arrangement space. 0 = Up, -90 = Left, 90 = Right

Args:
    end_angle (float):

<a id="unreal.AvaRadialArrangeModifier.set_count"></a>

#### set_count

```python
def set_count(count: int) -> None
```

x.set_count(count) -> None
Sets the number of child elements to use in the arrangement. Children whose index is greater than or equal to this value will be hidden.

Args:
    count (int32):

<a id="unreal.AvaRadialArrangeModifier.set_base_orientation"></a>

#### set_base_orientation

```python
def set_base_orientation(rotation: Rotator) -> None
```

x.set_base_orientation(rotation) -> None
Sets the base rotation

Args:
    rotation (Rotator):

<a id="unreal.AvaRadialArrangeModifier.set_arrangement"></a>

#### set_arrangement

```python
def set_arrangement(arrangement: AvaRadialArrangement) -> None
```

x.set_arrangement(arrangement) -> None
Defines how to arrange the child elements around the center.

Args:
    arrangement (AvaRadialArrangement):

<a id="unreal.AvaRadialArrangeModifier.get_start_from_outer_radius"></a>

#### get_start_from_outer_radius

```python
def get_start_from_outer_radius() -> bool
```

x.get_start_from_outer_radius() -> bool
If true, will arrange the child elements starting from the outer radius and moving to the inner radius. Has no effect if only using one ring.

Returns:
    bool:

<a id="unreal.AvaRadialArrangeModifier.get_start_angle"></a>

#### get_start_angle

```python
def get_start_angle() -> float
```

x.get_start_angle() -> float
Gets the start angle for the arrangement space and moving clockwise. 0 = Up, -90 = Left, 90 = Right

Returns:
    float:

<a id="unreal.AvaRadialArrangeModifier.get_rings"></a>

#### get_rings

```python
def get_rings() -> int
```

x.get_rings() -> int32
Gets the number of rings.

Returns:
    int32:

<a id="unreal.AvaRadialArrangeModifier.get_outer_radius"></a>

#### get_outer_radius

```python
def get_outer_radius() -> float
```

x.get_outer_radius() -> float
Gets the radius from the center to the last outer ring.

Returns:
    float:

<a id="unreal.AvaRadialArrangeModifier.get_orientation_axis"></a>

#### get_orientation_axis

```python
def get_orientation_axis() -> AvaModifiersAxis
```

x.get_orientation_axis() -> AvaModifiersAxis
Gets the axis to look at the center.

Returns:
    AvaModifiersAxis:

<a id="unreal.AvaRadialArrangeModifier.get_orient"></a>

#### get_orient

```python
def get_orient() -> bool
```

x.get_orient() -> bool
If true, will orient the selected axis torwards the center.

Returns:
    bool:

<a id="unreal.AvaRadialArrangeModifier.get_inner_radius"></a>

#### get_inner_radius

```python
def get_inner_radius() -> float
```

x.get_inner_radius() -> float
Gets the radius from the center to the first inner ring.

Returns:
    float:

<a id="unreal.AvaRadialArrangeModifier.get_flip_orient"></a>

#### get_flip_orient

```python
def get_flip_orient() -> bool
```

x.get_flip_orient() -> bool
If true, will flip the center orientation to face outwards.

Returns:
    bool:

<a id="unreal.AvaRadialArrangeModifier.get_end_angle"></a>

#### get_end_angle

```python
def get_end_angle() -> float
```

x.get_end_angle() -> float
Gets the end angle for the arrangement space. 0 = Up, -90 = Left, 90 = Right

Returns:
    float:

<a id="unreal.AvaRadialArrangeModifier.get_count"></a>

#### get_count

```python
def get_count() -> int
```

x.get_count() -> int32
Gets the number of child elements to use in the arrangement. Children whose index is greater than or equal to this value will be hidden.

Returns:
    int32:

<a id="unreal.AvaRadialArrangeModifier.get_base_orientation"></a>

#### get_base_orientation

```python
def get_base_orientation() -> Rotator
```

x.get_base_orientation() -> Rotator
Gets the base rotation

Returns:
    Rotator:

<a id="unreal.AvaRadialArrangeModifier.get_arrangement"></a>

#### get_arrangement

```python
def get_arrangement() -> AvaRadialArrangement
```

x.get_arrangement() -> AvaRadialArrangement
Defines how to arrange the child elements around the center.

Returns:
    AvaRadialArrangement:

<a id="unreal.AvaSplineSweepModifier"></a>