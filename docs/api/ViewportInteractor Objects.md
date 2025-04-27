## ViewportInteractor Objects

```python
class ViewportInteractor(Object)
```

Represents the interactor in the world

**C++ Source:**

- **Module**: ViewportInteraction
- **File**: ViewportInteractor.h

<a id="unreal.ViewportInteractor.tick"></a>

#### tick

```python
def tick(delta_time: float) -> None
```

x.tick(delta_time) -> None
Update for this interactor called by the ViewportWorldInteraction

Args:
    delta_time (float):

<a id="unreal.ViewportInteractor.shutdown"></a>

#### shutdown

```python
def shutdown() -> None
```

x.shutdown() -> None
Whenever the ViewportWorldInteraction is shut down, the interacts will shut down as well

<a id="unreal.ViewportInteractor.set_hit_result_gizmo_filter_mode"></a>

#### set_hit_result_gizmo_filter_mode

```python
def set_hit_result_gizmo_filter_mode(
        new_filter: HitResultGizmoFilterMode) -> None
```

x.set_hit_result_gizmo_filter_mode(new_filter) -> None
Sets the current gizmo filter mode used for Interaction

Args:
    new_filter (HitResultGizmoFilterMode):

<a id="unreal.ViewportInteractor.set_dragging_mode"></a>

#### set_dragging_mode

```python
def set_dragging_mode(
        new_dragging_mode: ViewportInteractionDraggingMode) -> None
```

x.set_dragging_mode(new_dragging_mode) -> None
Sets the current dragging mode for this interactor

Args:
    new_dragging_mode (ViewportInteractionDraggingMode):

<a id="unreal.ViewportInteractor.set_can_carry"></a>

#### set_can_carry

```python
def set_can_carry(can_carry: bool) -> None
```

x.set_can_carry(can_carry) -> None
Sets if the interactor can carry an object

Args:
    can_carry (bool):

<a id="unreal.ViewportInteractor.is_hovering_over_gizmo"></a>

#### is_hovering_over_gizmo

```python
def is_hovering_over_gizmo() -> bool
```

x.is_hovering_over_gizmo() -> bool
If the interactor laser is currently hovering over a gizmo handle

Returns:
    bool:

<a id="unreal.ViewportInteractor.handle_input_key_bp"></a>

#### handle_input_key_bp

```python
def handle_input_key_bp(action: ViewportActionKeyInput, key: Key,
                        event: InputEventType) -> bool
```

x.handle_input_key_bp(action, key, event) -> bool
To be overridden. Called by HandleInputKey before delegates and default input implementation

Args:
    action (ViewportActionKeyInput): 
    key (Key): 
    event (InputEventType): 

Returns:
    bool: 

    out_was_handled (bool):

<a id="unreal.ViewportInteractor.handle_input_axis_bp"></a>

#### handle_input_axis_bp

```python
def handle_input_axis_bp(action: ViewportActionKeyInput, key: Key,
                         delta: float, delta_time: float) -> bool
```

x.handle_input_axis_bp(action, key, delta, delta_time) -> bool
To be overridden. Called by HandleInputAxis before delegates and default input implementation

Args:
    action (ViewportActionKeyInput): 
    key (Key): 
    delta (float): 
    delta_time (float): 

Returns:
    bool: 

    out_was_handled (bool):

<a id="unreal.ViewportInteractor.get_world_interaction"></a>

#### get_world_interaction

```python
def get_world_interaction() -> ViewportWorldInteraction
```

x.get_world_interaction() -> ViewportWorldInteraction
Gets the world interaction

Returns:
    ViewportWorldInteraction:

<a id="unreal.ViewportInteractor.get_transform_and_forward_vector"></a>

#### get_transform_and_forward_vector

```python
def get_transform_and_forward_vector() -> Optional[Tuple[Transform, Vector]]
```

x.get_transform_and_forward_vector() -> (out_hand_transform=Transform, out_forward_vector=Vector) or None
Creates a hand transform and forward vector for a laser pointer for a given hand

Returns:
    tuple or None: True if we have motion controller data for this hand and could return a valid result

    out_hand_transform (Transform): The created hand transform

    out_forward_vector (Vector): The forward vector of the hand

<a id="unreal.ViewportInteractor.get_transform"></a>

#### get_transform

```python
def get_transform() -> Transform
```

x.get_transform() -> Transform
Gets the world transform of this interactor

Returns:
    Transform:

<a id="unreal.ViewportInteractor.get_room_space_transform"></a>

#### get_room_space_transform

```python
def get_room_space_transform() -> Transform
```

x.get_room_space_transform() -> Transform
Gets the hand transform of the interactor, in the local tracking space

Returns:
    Transform:

<a id="unreal.ViewportInteractor.get_other_interactor"></a>

#### get_other_interactor

```python
def get_other_interactor() -> ViewportInteractor
```

x.get_other_interactor() -> ViewportInteractor
Gets the paired interactor assigned by the world interaction, can return null when there is no other interactor

Returns:
    ViewportInteractor:

<a id="unreal.ViewportInteractor.get_last_transform"></a>

#### get_last_transform

```python
def get_last_transform() -> Transform
```

x.get_last_transform() -> Transform
Gets the last world transform of this interactor

Returns:
    Transform:

<a id="unreal.ViewportInteractor.get_last_room_space_transform"></a>

#### get_last_room_space_transform

```python
def get_last_room_space_transform() -> Transform
```

x.get_last_room_space_transform() -> Transform
Gets the last hand transform of the interactor, in the local tracking space

Returns:
    Transform:

<a id="unreal.ViewportInteractor.get_laser_pointer"></a>

#### get_laser_pointer

```python
def get_laser_pointer(
    even_if_blocked: bool = False,
    laser_length_override: float = 0.000000
) -> Optional[Tuple[Vector, Vector]]
```

x.get_laser_pointer(even_if_blocked=False, laser_length_override=0.000000) -> (laser_pointer_start=Vector, laser_pointer_end=Vector) or None
Gets the start and end point of the laser pointer for the specified hand

Args:
    even_if_blocked (bool): If true, returns a laser pointer even if the hand has UI in front of it (defaults to false)
    laser_length_override (float): If zero the default laser length (VREdMode::GetLaserLength) is used

Returns:
    tuple or None: True if we have motion controller data for this hand and could return a valid result

    laser_pointer_start (Vector): 

    laser_pointer_end (Vector):

<a id="unreal.ViewportInteractor.get_hover_location"></a>

#### get_hover_location

```python
def get_hover_location() -> Vector
```

x.get_hover_location() -> Vector
Gets the interactor laser hover location

Returns:
    Vector:

<a id="unreal.ViewportInteractor.get_hit_result_gizmo_filter_mode"></a>

#### get_hit_result_gizmo_filter_mode

```python
def get_hit_result_gizmo_filter_mode() -> HitResultGizmoFilterMode
```

x.get_hit_result_gizmo_filter_mode() -> HitResultGizmoFilterMode
Gets current gizmo filter mode used for Interaction

Returns:
    HitResultGizmoFilterMode:

<a id="unreal.ViewportInteractor.get_dragging_mode"></a>

#### get_dragging_mode

```python
def get_dragging_mode() -> ViewportInteractionDraggingMode
```

x.get_dragging_mode() -> ViewportInteractionDraggingMode
Gets the current interactor data dragging mode

Returns:
    ViewportInteractionDraggingMode:

<a id="unreal.ViewportInteractor.can_carry"></a>

#### can_carry

```python
def can_carry() -> bool
```

x.can_carry() -> bool
Gets if the interactor can carry an object

Returns:
    bool:

<a id="unreal.VREditorInteractor"></a>