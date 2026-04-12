## VREditorInteractor Objects

```python
class VREditorInteractor(ViewportInteractor)
```

VREditor default interactor

**C++ Source:**

- **Module**: VREditor
- **File**: VREditorInteractor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hand_mesh_component`` (StaticMeshComponent):  [Read-Write] Access to the current handmesh. Use ReplaceHandMeshComponent() to update the entire StaticMeshComponent.
- ``is_undo_redo_swipe_enabled`` (bool):  [Read-Write] Whether swiping left/right on touchpad/joystick triggers undo/redo

<a id="unreal.VREditorInteractor.hand_mesh_component"></a>

#### hand\_mesh\_component

```python
@property
def hand_mesh_component() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Write] Access to the current handmesh. Use ReplaceHandMeshComponent() to update the entire StaticMeshComponent.

<a id="unreal.VREditorInteractor.hand_mesh_component"></a>

#### hand\_mesh\_component

```python
@hand_mesh_component.setter
def hand_mesh_component(value: StaticMeshComponent) -> None
```

<a id="unreal.VREditorInteractor.update_hand_mesh_relative_transform"></a>

#### update\_hand\_mesh\_relative\_transform

```python
def update_hand_mesh_relative_transform() -> None
```

x.update_hand_mesh_relative_transform() -> None
Update Hand Mesh Relative Transform

<a id="unreal.VREditorInteractor.try_override_controller_type"></a>

#### try\_override\_controller\_type

```python
def try_override_controller_type(controller_type: ControllerType) -> bool
```

x.try_override_controller_type(controller_type) -> bool
Temporary set what controller type this is for asymmetric control schemes.
You can't override the controller type when there's already an override.
Remove the temporary controller type with EControllerType::Unknown

Args:
    controller_type (ControllerType): 

Returns:
    bool: true if the controller type was changed

<a id="unreal.VREditorInteractor.setup_component"></a>

#### setup\_component

```python
def setup_component(owning_actor: Actor) -> None
```

x.setup_component(owning_actor) -> None
Sets up all components

Args:
    owning_actor (Actor):

<a id="unreal.VREditorInteractor.set_force_show_laser"></a>

#### set\_force\_show\_laser

```python
def set_force_show_laser(force_show: bool) -> None
```

x.set_force_show_laser(force_show) -> None
Set if we want to force to show the laser

Args:
    force_show (bool):

<a id="unreal.VREditorInteractor.set_force_laser_color"></a>

#### set\_force\_laser\_color

```python
def set_force_laser_color(color: LinearColor) -> None
```

x.set_force_laser_color(color) -> None
Next frame this will be used as color for the laser

Args:
    color (LinearColor):

<a id="unreal.VREditorInteractor.set_controller_type"></a>

#### set\_controller\_type

```python
def set_controller_type(controller_type: ControllerType) -> None
```

x.set_controller_type(controller_type) -> None
Set what controller type this is for asymmetric control schemes

Args:
    controller_type (ControllerType):

<a id="unreal.VREditorInteractor.set_controller_hand_side"></a>

#### set\_controller\_hand\_side

```python
def set_controller_hand_side(controller_hand_side: Name) -> None
```

x.set_controller_hand_side(controller_hand_side) -> None
Sets the EControllerHand for this motioncontroller

Args:
    controller_hand_side (Name):

<a id="unreal.VREditorInteractor.replace_hand_mesh_component"></a>

#### replace\_hand\_mesh\_component

```python
def replace_hand_mesh_component(
        new_mesh: StaticMesh,
        mesh_scale: Vector = [1.000000, 1.000000, 1.000000]) -> None
```

x.replace_hand_mesh_component(new_mesh, mesh_scale=[1.000000, 1.000000, 1.000000]) -> None
Replace the default VR controller mesh with a custom one.

Args:
    new_mesh (StaticMesh): 
    mesh_scale (Vector):

<a id="unreal.VREditorInteractor.is_touching_trackpad"></a>

#### is\_touching\_trackpad

```python
def is_touching_trackpad() -> bool
```

x.is_touching_trackpad() -> bool
Check if the touchpad is currently touched

Returns:
    bool:

<a id="unreal.VREditorInteractor.is_hovering_over_ui"></a>

#### is\_hovering\_over\_ui

```python
def is_hovering_over_ui() -> bool
```

x.is_hovering_over_ui() -> bool
Gets if this interactor is hovering over UI

Returns:
    bool:

<a id="unreal.VREditorInteractor.is_clicking_on_ui"></a>

#### is\_clicking\_on\_ui

```python
def is_clicking_on_ui() -> bool
```

x.is_clicking_on_ui() -> bool
Gets if the interactor is clicking on any UI

Returns:
    bool:

<a id="unreal.VREditorInteractor.init"></a>

#### init

```python
def init(vr_mode: VREditorMode) -> None
```

x.init(vr_mode) -> None
Initialize default values

Args:
    vr_mode (VREditorMode):

<a id="unreal.VREditorInteractor.get_trackpad_position"></a>

#### get\_trackpad\_position

```python
def get_trackpad_position() -> Vector2D
```

x.get_trackpad_position() -> Vector2D
Get the current position of the trackpad or analog stick

Returns:
    Vector2D:

<a id="unreal.VREditorInteractor.get_teleport_actor"></a>

#### get\_teleport\_actor

```python
def get_teleport_actor() -> VREditorTeleporter
```

x.get_teleport_actor() -> VREditorTeleporter
Get Teleport Actor

Returns:
    VREditorTeleporter:

<a id="unreal.VREditorInteractor.get_slide_delta"></a>

#### get\_slide\_delta

```python
def get_slide_delta() -> float
```

x.get_slide_delta() -> float
Returns the slide delta for pushing and pulling objects. Needs to be implemented by derived classes (e.g. touchpad for vive controller or scrollweel for mouse )

Returns:
    float:

<a id="unreal.VREditorInteractor.get_select_and_move_trigger_value"></a>

#### get\_select\_and\_move\_trigger\_value

```python
def get_select_and_move_trigger_value() -> float
```

x.get_select_and_move_trigger_value() -> float
Gets the trigger value

Returns:
    float:

<a id="unreal.VREditorInteractor.get_motion_controller_component"></a>

#### get\_motion\_controller\_component

```python
def get_motion_controller_component() -> MotionControllerComponent
```

x.get_motion_controller_component() -> MotionControllerComponent
Get the motioncontroller component of this interactor

Returns:
    MotionControllerComponent:

<a id="unreal.VREditorInteractor.get_last_trackpad_position"></a>

#### get\_last\_trackpad\_position

```python
def get_last_trackpad_position() -> Vector2D
```

x.get_last_trackpad_position() -> Vector2D
Get the last position of the trackpad or analog stick

Returns:
    Vector2D:

<a id="unreal.VREditorInteractor.get_laser_start"></a>

#### get\_laser\_start

```python
def get_laser_start() -> Vector
```

x.get_laser_start() -> Vector
Getters and setters

Returns:
    Vector:

<a id="unreal.VREditorInteractor.get_laser_end"></a>

#### get\_laser\_end

```python
def get_laser_end() -> Vector
```

x.get_laser_end() -> Vector
Get Laser End

Returns:
    Vector:

<a id="unreal.VREditorInteractor.get_hmd_device_type"></a>

#### get\_hmd\_device\_type

```python
def get_hmd_device_type() -> Name
```

x.get_hmd_device_type() -> Name


Returns:
    Name: Returns the type of HMD we're dealing with

<a id="unreal.VREditorInteractor.get_controller_type"></a>

#### get\_controller\_type

```python
def get_controller_type() -> ControllerType
```

x.get_controller_type() -> ControllerType
Returns what controller type this is for asymmetric control schemes

Returns:
    ControllerType:

<a id="unreal.VREditorInteractor.get_controller_side"></a>

#### get\_controller\_side

```python
def get_controller_side() -> ControllerHand
```

x.get_controller_side() -> ControllerHand
Get the side of the controller

Returns:
    ControllerHand:

<a id="unreal.VREditorInteractor.get_controller_hand_side"></a>

#### get\_controller\_hand\_side

```python
def get_controller_hand_side() -> Name
```

x.get_controller_hand_side() -> Name
Sets the EControllerHand for this motioncontroller

Returns:
    Name:

<a id="unreal.EditorWorldExtension"></a>