## TouchInputComponent Objects

```python
class TouchInputComponent(ActorComponent)
```

Touch Input Component

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: TouchInputComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``current_angle`` (float):  [Read-Only]
- ``current_finger_count`` (ExistFingerCount):  [Read-Only] 当前手指数量
- ``current_length`` (float):  [Read-Only]
- ``current_pan_location`` (Vector):  [Read-Only]
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``fingers`` (Array[TouchIndex]):  [Read-Only] 手指
- ``initial_angle`` (float):  [Read-Only]
- ``initial_length`` (float):  [Read-Only]
- ``initial_pan_location`` (Vector):  [Read-Only]
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``locations`` (Array[Vector]):  [Read-Only] 位置
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_one_finger_event`` (OnOneFingerPressed):  [Read-Write]
- ``on_two_finger_event`` (OnTwoFingersMove):  [Read-Write]
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.TouchInputComponent.on_one_finger_event"></a>

#### on\_one\_finger\_event

```python
@property
def on_one_finger_event() -> OnOneFingerPressed
```

(OnOneFingerPressed):  [Read-Write]

<a id="unreal.TouchInputComponent.on_one_finger_event"></a>

#### on\_one\_finger\_event

```python
@on_one_finger_event.setter
def on_one_finger_event(value: OnOneFingerPressed) -> None
```

<a id="unreal.TouchInputComponent.on_two_finger_event"></a>

#### on\_two\_finger\_event

```python
@property
def on_two_finger_event() -> OnTwoFingersMove
```

(OnTwoFingersMove):  [Read-Write]

<a id="unreal.TouchInputComponent.on_two_finger_event"></a>

#### on\_two\_finger\_event

```python
@on_two_finger_event.setter
def on_two_finger_event(value: OnTwoFingersMove) -> None
```

<a id="unreal.TouchInputComponent.fingers"></a>

#### fingers

```python
@property
def fingers() -> Array[TouchIndex]
```

(Array[TouchIndex]):  [Read-Only] 手指

<a id="unreal.TouchInputComponent.locations"></a>

#### locations

```python
@property
def locations() -> Array[Vector]
```

(Array[Vector]):  [Read-Only] 位置

<a id="unreal.TouchInputComponent.current_finger_count"></a>

#### current\_finger\_count

```python
@property
def current_finger_count() -> ExistFingerCount
```

(ExistFingerCount):  [Read-Only] 当前手指数量

<a id="unreal.TouchInputComponent.current_angle"></a>

#### current\_angle

```python
@property
def current_angle() -> float
```

(float):  [Read-Only]

<a id="unreal.TouchInputComponent.current_length"></a>

#### current\_length

```python
@property
def current_length() -> float
```

(float):  [Read-Only]

<a id="unreal.TouchInputComponent.current_pan_location"></a>

#### current\_pan\_location

```python
@property
def current_pan_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.TouchInputComponent.initial_length"></a>

#### initial\_length

```python
@property
def initial_length() -> float
```

(float):  [Read-Only]

<a id="unreal.TouchInputComponent.initial_angle"></a>

#### initial\_angle

```python
@property
def initial_angle() -> float
```

(float):  [Read-Only]

<a id="unreal.TouchInputComponent.initial_pan_location"></a>

#### initial\_pan\_location

```python
@property
def initial_pan_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.TouchInputComponent.on_event_touch_released"></a>

#### on\_event\_touch\_released

```python
def on_event_touch_released(finger_index: TouchIndex,
                            location: Vector) -> None
```

x.on_event_touch_released(finger_index, location) -> None
On Event Touch Released

Args:
    finger_index (TouchIndex): 
    location (Vector):

<a id="unreal.TouchInputComponent.on_event_touch_pressed"></a>

#### on\_event\_touch\_pressed

```python
def on_event_touch_pressed(finger_index: TouchIndex, location: Vector) -> None
```

x.on_event_touch_pressed(finger_index, location) -> None
On Event Touch Pressed

Args:
    finger_index (TouchIndex): 
    location (Vector):

<a id="unreal.TouchInputComponent.on_event_touch_moved"></a>

#### on\_event\_touch\_moved

```python
def on_event_touch_moved(finger_index: TouchIndex, location: Vector) -> None
```

x.on_event_touch_moved(finger_index, location) -> None
On Event Touch Moved

Args:
    finger_index (TouchIndex): 
    location (Vector):

<a id="unreal.TouchInputComponent.is_finger_location_exists"></a>

#### is\_finger\_location\_exists

```python
def is_finger_location_exists(finger_index: TouchIndex) -> bool
```

x.is_finger_location_exists(finger_index) -> bool
Is Finger Location Exists

Args:
    finger_index (TouchIndex): 

Returns:
    bool:

<a id="unreal.TouchInputComponent.get_screen_up_vector"></a>

#### get\_screen\_up\_vector

```python
def get_screen_up_vector() -> Vector
```

x.get_screen_up_vector() -> Vector
Get Screen Up Vector

Returns:
    Vector:

<a id="unreal.TouchInputComponent.get_screen_right_vector"></a>

#### get\_screen\_right\_vector

```python
def get_screen_right_vector() -> Vector
```

x.get_screen_right_vector() -> Vector
Get Screen Right Vector

Returns:
    Vector:

<a id="unreal.TouchInputComponent.get_length_and_angle"></a>

#### get\_length\_and\_angle

```python
def get_length_and_angle() -> Tuple[Vector, float, float]
```

x.get_length_and_angle() -> (Vector, out_length=float, out_angle=float)
Get Length and Angle

Returns:
    tuple: 

    out_length (float): 

    out_angle (float):

<a id="unreal.TouchInputComponent.get_fingers_length"></a>

#### get\_fingers\_length

```python
def get_fingers_length() -> int
```

x.get_fingers_length() -> int32
获取手指数量

Returns:
    int32:

<a id="unreal.TouchInputComponent.get_finger_and_location_by_index"></a>

#### get\_finger\_and\_location\_by\_index

```python
def get_finger_and_location_by_index(
        index: int) -> Optional[Tuple[TouchIndex, Vector]]
```

x.get_finger_and_location_by_index(index) -> (out_finger_index=TouchIndex, out_location=Vector) or None
Get Finger and Location by Index

Args:
    index (int32): 

Returns:
    tuple or None: 

    out_finger_index (TouchIndex): 

    out_location (Vector):

<a id="unreal.WdpBasePawn"></a>