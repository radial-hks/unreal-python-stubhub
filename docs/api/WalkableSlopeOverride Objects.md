## WalkableSlopeOverride Objects

```python
class WalkableSlopeOverride(StructBase)
```

Struct allowing control over "walkable" normals, by allowing a restriction or relaxation of what steepness is normally walkable.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``walkable_slope_angle`` (float):  [Read-Write] Override walkable slope angle (in degrees), applying the rules of the Walkable Slope Behavior.
  see: GetWalkableSlopeAngle(), SetWalkableSlopeAngle()
- ``walkable_slope_behavior`` (WalkableSlopeBehavior):  [Read-Write] Behavior of this surface (whether we affect the walkable slope).
  see: GetWalkableSlopeBehavior(), SetWalkableSlopeBehavior()

<a id="unreal.WalkableSlopeOverride.__init__"></a>

#### __init__

```python
def __init__(
        walkable_slope_behavior: WalkableSlopeBehavior = WalkableSlopeBehavior.
    WALKABLE_SLOPE_DEFAULT,
        walkable_slope_angle: float = 0.000000) -> None
```

<a id="unreal.WalkableSlopeOverride.walkable_slope_behavior"></a>

#### walkable_slope_behavior

```python
@property
def walkable_slope_behavior() -> WalkableSlopeBehavior
```

(WalkableSlopeBehavior):  [Read-Write] Behavior of this surface (whether we affect the walkable slope).
see: GetWalkableSlopeBehavior(), SetWalkableSlopeBehavior()

<a id="unreal.WalkableSlopeOverride.walkable_slope_behavior"></a>

#### walkable_slope_behavior

```python
@walkable_slope_behavior.setter
def walkable_slope_behavior(value: WalkableSlopeBehavior) -> None
```

<a id="unreal.WalkableSlopeOverride.walkable_slope_angle"></a>

#### walkable_slope_angle

```python
@property
def walkable_slope_angle() -> float
```

(float):  [Read-Write] Override walkable slope angle (in degrees), applying the rules of the Walkable Slope Behavior.
see: GetWalkableSlopeAngle(), SetWalkableSlopeAngle()

<a id="unreal.WalkableSlopeOverride.walkable_slope_angle"></a>

#### walkable_slope_angle

```python
@walkable_slope_angle.setter
def walkable_slope_angle(value: float) -> None
```

<a id="unreal.BodyInstanceCore"></a>