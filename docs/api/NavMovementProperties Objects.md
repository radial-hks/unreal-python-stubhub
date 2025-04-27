## NavMovementProperties Objects

```python
class NavMovementProperties(StructBase)
```

Struct to hold properties a user might set for navigation movement

**C++ Source:**

- **Module**: Engine
- **File**: NavigationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fixed_path_braking_distance`` (float):  [Read-Write] Braking distance override used with acceleration driven path following (bUseAccelerationForPaths)
- ``stop_movement_abort_paths`` (bool):  [Read-Write] If set, StopActiveMovement call will abort current path following request
- ``update_nav_agent_with_owners_collision`` (bool):  [Read-Write] If set to true, NavAgentProperties' radius and height will be updated with Owner's collision capsule size
- ``use_acceleration_for_paths`` (bool):  [Read-Write] If set, pathfollowing will control character movement via acceleration values. If false, it will set velocities directly.
- ``use_fixed_braking_distance_for_paths`` (bool):  [Read-Write] If set, FixedPathBrakingDistance will be used for path following deceleration

<a id="unreal.NavMovementProperties.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NavAgentProperties"></a>