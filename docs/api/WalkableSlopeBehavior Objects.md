## WalkableSlopeBehavior Objects

```python
class WalkableSlopeBehavior(EnumBase)
```

Controls behavior of WalkableSlopeOverride, determining how to affect walkability of surfaces for Characters.
see: FWalkableSlopeOverride
see: UCharacterMovementComponent::GetWalkableFloorAngle(), UCharacterMovementComponent::SetWalkableFloorAngle()

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.WalkableSlopeBehavior.WALKABLE_SLOPE_DEFAULT"></a>

#### WALKABLE_SLOPE_DEFAULT

0: Don't affect the walkable slope. Walkable slope angle will be ignored.

<a id="unreal.WalkableSlopeBehavior.WALKABLE_SLOPE_INCREASE"></a>

#### WALKABLE_SLOPE_INCREASE

1: Increase walkable slope.
Makes it easier to walk up a surface, by allowing traversal over higher-than-usual angles.
see: FWalkableSlopeOverride::WalkableSlopeAngle

<a id="unreal.WalkableSlopeBehavior.WALKABLE_SLOPE_DECREASE"></a>

#### WALKABLE_SLOPE_DECREASE

2: Decrease walkable slope.
Makes it harder to walk up a surface, by restricting traversal to lower-than-usual angles.
see: FWalkableSlopeOverride::WalkableSlopeAngle

<a id="unreal.WalkableSlopeBehavior.WALKABLE_SLOPE_UNWALKABLE"></a>

#### WALKABLE_SLOPE_UNWALKABLE

3: Make surface unwalkable.
Note: WalkableSlopeAngle will be ignored.

<a id="unreal.DOFMode"></a>