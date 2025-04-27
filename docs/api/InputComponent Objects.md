## InputComponent Objects

```python
class InputComponent(ActorComponent)
```

Implement an Actor component for input bindings.

An Input Component is a transient component that enables an Actor to bind various forms of input events to delegate functions.
Input components are processed from a stack managed by the PlayerController and processed by the PlayerInput.
Each binding can consume the input event preventing other components on the input stack from processing the input.
see: https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

**C++ Source:**

- **Module**: Engine
- **File**: InputComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.InputComponent.was_controller_key_just_released"></a>

#### was_controller_key_just_released

```python
def was_controller_key_just_released(key: Key) -> bool
```

x.was_controller_key_just_released(key) -> bool
Returns true if the given key/button was down last frame and up this frame.
deprecated: Use PlayerController.WasInputKeyJustReleased instead.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputComponent.was_controller_key_just_pressed"></a>

#### was_controller_key_just_pressed

```python
def was_controller_key_just_pressed(key: Key) -> bool
```

x.was_controller_key_just_pressed(key) -> bool
Returns true if the given key/button was up last frame and down this frame.
deprecated: Use PlayerController.WasInputKeyJustPressed instead.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputComponent.is_controller_key_down"></a>

#### is_controller_key_down

```python
def is_controller_key_down(key: Key) -> bool
```

x.is_controller_key_down(key) -> bool
Returns true if the given key/button is pressed on the input of the controller (if present)
deprecated: Use PlayerController.IsInputKeyDown instead.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputComponent.get_touch_state"></a>

#### get_touch_state

```python
def get_touch_state(finger_index: int) -> Tuple[float, float, bool]
```

x.get_touch_state(finger_index) -> (location_x=float, location_y=float, is_currently_pressed=bool)
Returns the location of a touch, and if it's held down
deprecated: Use PlayerController.GetInputTouchState instead.

Args:
    finger_index (int32): 

Returns:
    tuple: 

    location_x (float): 

    location_y (float): 

    is_currently_pressed (bool):

<a id="unreal.InputComponent.get_controller_vector_key_state"></a>

#### get_controller_vector_key_state

```python
def get_controller_vector_key_state(key: Key) -> Vector
```

x.get_controller_vector_key_state(key) -> Vector
Returns the vector value for the given key/button.
deprecated: Use PlayerController.GetInputVectorKeyState instead.

Args:
    key (Key): 

Returns:
    Vector:

<a id="unreal.InputComponent.get_controller_mouse_delta"></a>

#### get_controller_mouse_delta

```python
def get_controller_mouse_delta() -> Tuple[float, float]
```

x.get_controller_mouse_delta() -> (delta_x=float, delta_y=float)
Retrieves how far the mouse moved this frame.
deprecated: Use PlayerController.GetInputMouseDelta instead.

Returns:
    tuple: 

    delta_x (float): 

    delta_y (float):

<a id="unreal.InputComponent.get_controller_key_time_down"></a>

#### get_controller_key_time_down

```python
def get_controller_key_time_down(key: Key) -> float
```

x.get_controller_key_time_down(key) -> float
Returns how long the given key/button has been down.  Returns 0 if it's up or it just went down this frame.
deprecated: Use PlayerController.GetInputKeyTimeDown instead.

Args:
    key (Key): 

Returns:
    float:

<a id="unreal.InputComponent.get_controller_analog_stick_state"></a>

#### get_controller_analog_stick_state

```python
def get_controller_analog_stick_state(
        which_stick: ControllerAnalogStick) -> Tuple[float, float]
```

x.get_controller_analog_stick_state(which_stick) -> (stick_x=float, stick_y=float)
Retrieves the X and Y displacement of the given analog stick.  For WhickStick, 0 = left, 1 = right.
deprecated: Use PlayerController.GetInputAnalogStickState instead.

Args:
    which_stick (ControllerAnalogStick): 

Returns:
    tuple: 

    stick_x (float): 

    stick_y (float):

<a id="unreal.InputComponent.get_controller_analog_key_state"></a>

#### get_controller_analog_key_state

```python
def get_controller_analog_key_state(key: Key) -> float
```

x.get_controller_analog_key_state(key) -> float
Returns the analog value for the given key/button.  If analog isn't supported, returns 1 for down and 0 for up.
deprecated: Use PlayerController.GetInputAnalogKeyState instead.

Args:
    key (Key): 

Returns:
    float:

<a id="unreal.InterpToMovementComponent"></a>