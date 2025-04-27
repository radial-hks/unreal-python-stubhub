## RigidBodyErrorCorrection Objects

```python
class RigidBodyErrorCorrection(StructBase)
```

Rigid body error correction data

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle_lerp`` (float):  [Read-Write] How much to directly lerp to the correct angle.
- ``angular_velocity_coefficient`` (float):  [Read-Write] This is the angular analog to LinearVelocityCoefficient.
- ``error_accumulation_distance_sq`` (float):  [Read-Write] If the body has moved less than the square root of
                this amount towards a resolved state in the previous
                frame, then error may accumulate towards a hard snap.
- ``error_accumulation_seconds`` (float):  [Read-Write] Number of seconds to remain in a heuristically
                unresolveable state before hard snapping.
- ``error_accumulation_similarity`` (float):  [Read-Write] If the previous error projected onto the current error
                is greater than this value (indicating "similarity"
                between states), then error may accumulate towards a
                hard snap.
- ``error_per_angular_difference`` (float):  [Read-Write] Error per degree
- ``error_per_linear_difference`` (float):  [Read-Write] Error per centimeter
- ``linear_velocity_coefficient`` (float):  [Read-Write] This is the coefficient `k` in the differential equation:
                dx/dt = k ( x_target(t) - x(t) ), which is used to update
                the velocity in a replication step.
- ``max_linear_hard_snap_distance`` (float):  [Read-Write]
- ``max_restored_state_error`` (float):  [Read-Write] Maximum allowable error for a state to be considered "resolved"
- ``ping_extrapolation`` (float):  [Read-Write] Value between 0 and 1 which indicates how much velocity
                and ping based correction to use
- ``ping_limit`` (float):  [Read-Write] For the purpose of extrapolation, ping will be clamped to this value
- ``position_lerp`` (float):  [Read-Write] How much to directly lerp to the correct position. Generally
                this should be very low, if not zero. A higher value will
                increase precision along with jerkiness.

<a id="unreal.RigidBodyErrorCorrection.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PhysicalSurfaceName"></a>