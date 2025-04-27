## AvoidanceManager Objects

```python
class AvoidanceManager(Object)
```

Avoidance Manager

**C++ Source:**

- **Module**: Engine
- **File**: AvoidanceManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``artificial_radius_expansion`` (float):  [Read-Write] Multiply the radius of all STORED avoidance objects by this value to allow a little extra room for avoidance maneuvers.
- ``default_time_to_live`` (float):  [Read-Write] How long an avoidance UID must not be updated before the system will put it back in the pool. Actual delay is up to 150% of this value.
- ``delta_time_to_predict`` (float):  [Read-Write] This is how far forward in time (seconds) we extend our velocity cones and thus our prediction
- ``height_check_margin`` (float):  [Read-Write] Allowable height margin between obstacles and agents. This is over and above the difference in agent heights.
- ``lock_time_after_avoid`` (float):  [Read-Write] How long to stay on course (barring collision) after making an avoidance move
- ``lock_time_after_clean`` (float):  [Read-Write] How long to stay on course (barring collision) after making an unobstructed move (should be > 0.0, but can be less than a full frame)

<a id="unreal.AvoidanceManager.register_movement_component"></a>

#### register_movement_component

```python
def register_movement_component(movement_comp: MovementComponent,
                                avoidance_weight: float = 0.500000) -> bool
```

x.register_movement_component(movement_comp, avoidance_weight=0.500000) -> bool
Register with the given avoidance manager.

Args:
    movement_comp (MovementComponent): 
    avoidance_weight (float): When avoiding each other, actors divert course in proportion to their relative weights. Range is 0.0 to 1.0. Special: at 1.0, actor will not divert course at all.

Returns:
    bool:

<a id="unreal.AvoidanceManager.get_object_count"></a>

#### get_object_count

```python
def get_object_count() -> int
```

x.get_object_count() -> int32
Get the number of avoidance objects currently in the manager.

Returns:
    int32:

<a id="unreal.AvoidanceManager.get_new_avoidance_uid"></a>

#### get_new_avoidance_uid

```python
def get_new_avoidance_uid() -> int
```

x.get_new_avoidance_uid() -> int32
Get appropriate UID for use when reporting to this function or requesting RVO assistance.

Returns:
    int32:

<a id="unreal.AvoidanceManager.get_avoidance_velocity_for_component"></a>

#### get_avoidance_velocity_for_component

```python
def get_avoidance_velocity_for_component(
        movement_comp: MovementComponent) -> Vector
```

x.get_avoidance_velocity_for_component(movement_comp) -> Vector
Calculate avoidance velocity for component (avoids collisions with the supplied component)

Args:
    movement_comp (MovementComponent): 

Returns:
    Vector:

<a id="unreal.AmbientSound"></a>