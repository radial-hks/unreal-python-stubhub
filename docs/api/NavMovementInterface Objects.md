## NavMovementInterface Objects

```python
class NavMovementInterface(Interface)
```

Nav Movement Interface

**C++ Source:**

- **Module**: Engine
- **File**: NavMovementInterface.h

<a id="unreal.NavMovementInterface.stop_movement_keep_pathing"></a>

#### stop\_movement\_keep\_pathing

```python
def stop_movement_keep_pathing() -> None
```

x.stop_movement_keep_pathing() -> None
Stops movement immediately (reset velocity) but keeps following current path

<a id="unreal.NavMovementInterface.stop_active_movement"></a>

#### stop\_active\_movement

```python
def stop_active_movement() -> None
```

x.stop_active_movement() -> None
Stops applying further movement (usually zeros acceleration).

<a id="unreal.NavMovementInterface.request_path_move"></a>

#### request\_path\_move

```python
def request_path_move(move_input: Vector) -> None
```

x.request_path_move(move_input) -> None
path following: request movement through a new move input (normal vector = full strength)

Args:
    move_input (Vector):

<a id="unreal.NavMovementInterface.request_direct_move"></a>

#### request\_direct\_move

```python
def request_direct_move(move_velocity: Vector, force_max_speed: bool) -> None
```

x.request_direct_move(move_velocity, force_max_speed) -> None
path following: request movement through a velocity directly

Args:
    move_velocity (Vector): 
    force_max_speed (bool):

<a id="unreal.NavMovementInterface.is_swimming"></a>

#### is\_swimming

```python
def is_swimming() -> bool
```

x.is_swimming() -> bool
Returns true if currently swimming (moving through a fluid volume)

Returns:
    bool:

<a id="unreal.NavMovementInterface.is_moving_on_ground"></a>

#### is\_moving\_on\_ground

```python
def is_moving_on_ground() -> bool
```

x.is_moving_on_ground() -> bool
Returns true if currently moving on the ground (e.g. walking or driving)

Returns:
    bool:

<a id="unreal.NavMovementInterface.is_flying"></a>

#### is\_flying

```python
def is_flying() -> bool
```

x.is_flying() -> bool
Returns true if currently flying (moving through a non-fluid volume without resting on the ground)

Returns:
    bool:

<a id="unreal.NavMovementInterface.is_falling"></a>

#### is\_falling

```python
def is_falling() -> bool
```

x.is_falling() -> bool
Returns true if currently falling (not flying, in a non-fluid volume, and not on the ground)

Returns:
    bool:

<a id="unreal.NavMovementInterface.is_crouching"></a>

#### is\_crouching

```python
def is_crouching() -> bool
```

x.is_crouching() -> bool
Returns true if currently crouching

Returns:
    bool:

<a id="unreal.NavMovementInterface.get_velocity_for_nav_movement"></a>

#### get\_velocity\_for\_nav\_movement

```python
def get_velocity_for_nav_movement() -> Vector
```

x.get_velocity_for_nav_movement() -> Vector
Get the current velocity of the agent for nav movement

Returns:
    Vector:

<a id="unreal.NavMovementInterface.get_max_speed_for_nav_movement"></a>

#### get\_max\_speed\_for\_nav\_movement

```python
def get_max_speed_for_nav_movement() -> float
```

x.get_max_speed_for_nav_movement() -> float
Get maximum movement speed of the agent

Returns:
    float:

<a id="unreal.NetworkPhysicsSettingsComponent"></a>