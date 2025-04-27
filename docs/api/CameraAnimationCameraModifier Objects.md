## CameraAnimationCameraModifier Objects

```python
class CameraAnimationCameraModifier(CameraModifier)
```

A camera modifier that plays camera animation sequences.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: CameraAnimationCameraModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current blend alpha.
- ``alpha_in_time`` (float):  [Read-Write] When blending in, alpha proceeds from 0 to 1 over this time
- ``alpha_out_time`` (float):  [Read-Write] When blending out, alpha proceeds from 1 to 0 over this time
- ``camera_owner`` (PlayerCameraManager):  [Read-Write] Camera this object is associated with.
- ``debug`` (bool):  [Read-Write] If true, enables certain debug visualization features.
- ``exclusive`` (bool):  [Read-Write] If true, no other modifiers of same priority allowed.
- ``priority`` (uint8):  [Read-Write] Priority value that determines the order in which modifiers are applied. 0 = highest priority, 255 = lowest.

<a id="unreal.CameraAnimationCameraModifier.stop_camera_animation"></a>

#### stop_camera_animation

```python
def stop_camera_animation(handle: CameraAnimationHandle,
                          immediate: bool = False) -> None
```

x.stop_camera_animation(handle, immediate=False) -> None
Stops the given camera animation instance.

Args:
    handle (CameraAnimationHandle): 
    immediate (bool): True to stop it right now and ignore blend out, false to let it blend out as indicated.

<a id="unreal.CameraAnimationCameraModifier.stop_all_camera_animations_of"></a>

#### stop_all_camera_animations_of

```python
def stop_all_camera_animations_of(sequence: CameraAnimationSequence,
                                  immediate: bool = False) -> None
```

x.stop_all_camera_animations_of(sequence, immediate=False) -> None
Stop playing all instances of the given camera animation sequence.

Args:
    sequence (CameraAnimationSequence): The sequence of which to stop all instances.
    immediate (bool): True to stop it right now and ignore blend out, false to let it blend out as indicated.

<a id="unreal.CameraAnimationCameraModifier.stop_all_camera_animations"></a>

#### stop_all_camera_animations

```python
def stop_all_camera_animations(immediate: bool = False) -> None
```

x.stop_all_camera_animations(immediate=False) -> None
Stop all camera animation instances.

Args:
    immediate (bool): True to stop it right now and ignore blend out, false to let it blend out as indicated.

<a id="unreal.CameraAnimationCameraModifier.play_camera_animation"></a>

#### play_camera_animation

```python
def play_camera_animation(
        sequence: CameraAnimationSequence,
        params: CameraAnimationParams) -> CameraAnimationHandle
```

x.play_camera_animation(sequence, params) -> CameraAnimationHandle
Play a new camera animation sequence.

Args:
    sequence (CameraAnimationSequence): The sequence to use for the new camera animation.
    params (CameraAnimationParams): The parameters for the new camera animation instance.

Returns:
    CameraAnimationHandle:

<a id="unreal.CameraAnimationCameraModifier.is_camera_animation_active"></a>

#### is_camera_animation_active

```python
def is_camera_animation_active(handle: CameraAnimationHandle) -> bool
```

x.is_camera_animation_active(handle) -> bool
Returns whether the given camera animation is playing.

Args:
    handle (CameraAnimationHandle): A handle to a previously started camera animation.

Returns:
    bool: Whether the corresponding camera animation is playing or not.

<a id="unreal.CameraAnimationCameraModifier.get_camera_animation_camera_modifier_from_player_controller"></a>

#### get_camera_animation_camera_modifier_from_player_controller

```python
@classmethod
def get_camera_animation_camera_modifier_from_player_controller(
        cls,
        player_controller: PlayerController) -> CameraAnimationCameraModifier
```

X.get_camera_animation_camera_modifier_from_player_controller(player_controller) -> CameraAnimationCameraModifier
Get Camera Animation Camera Modifier from Player Controller

Args:
    player_controller (PlayerController): 

Returns:
    CameraAnimationCameraModifier:

<a id="unreal.CameraAnimationCameraModifier.get_camera_animation_camera_modifier_from_id"></a>

#### get_camera_animation_camera_modifier_from_id

```python
@classmethod
def get_camera_animation_camera_modifier_from_id(
        cls, world_context_object: Object,
        controller_id: int) -> CameraAnimationCameraModifier
```

X.get_camera_animation_camera_modifier_from_id(world_context_object, controller_id) -> CameraAnimationCameraModifier
Get Camera Animation Camera Modifier from ID

Args:
    world_context_object (Object): 
    controller_id (int32): 

Returns:
    CameraAnimationCameraModifier:

<a id="unreal.CameraAnimationCameraModifier.get_camera_animation_camera_modifier"></a>

#### get_camera_animation_camera_modifier

```python
@classmethod
def get_camera_animation_camera_modifier(
        cls, world_context_object: Object,
        player_index: int) -> CameraAnimationCameraModifier
```

X.get_camera_animation_camera_modifier(world_context_object, player_index) -> CameraAnimationCameraModifier
Get Camera Animation Camera Modifier

Args:
    world_context_object (Object): 
    player_index (int32): 

Returns:
    CameraAnimationCameraModifier:

<a id="unreal.EngineCameraAnimationFunctionLibrary"></a>