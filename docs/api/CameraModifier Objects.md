## CameraModifier Objects

```python
class CameraModifier(Object)
```

A CameraModifier is a base class for objects that may adjust the final camera properties after
being computed by the APlayerCameraManager (
see: ModifyCamera). A CameraModifier can be stateful, and is associated uniquely with a specific APlayerCameraManager.

**C++ Source:**

- **Module**: Engine
- **File**: CameraModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current blend alpha.
- ``alpha_in_time`` (float):  [Read-Write] When blending in, alpha proceeds from 0 to 1 over this time
- ``alpha_out_time`` (float):  [Read-Write] When blending out, alpha proceeds from 1 to 0 over this time
- ``camera_owner`` (PlayerCameraManager):  [Read-Write] Camera this object is associated with.
- ``debug`` (bool):  [Read-Write] If true, enables certain debug visualization features.
- ``exclusive`` (bool):  [Read-Write] If true, no other modifiers of same priority allowed.
- ``priority`` (uint8):  [Read-Write] Priority value that determines the order in which modifiers are applied. 0 = highest priority, 255 = lowest.

<a id="unreal.CameraModifier.exclusive"></a>

#### exclusive

```python
@property
def exclusive() -> bool
```

(bool):  [Read-Only] If true, no other modifiers of same priority allowed.

<a id="unreal.CameraModifier.priority"></a>

#### priority

```python
@property
def priority() -> int
```

(uint8):  [Read-Only] Priority value that determines the order in which modifiers are applied. 0 = highest priority, 255 = lowest.

<a id="unreal.CameraModifier.camera_owner"></a>

#### camera_owner

```python
@property
def camera_owner() -> PlayerCameraManager
```

(PlayerCameraManager):  [Read-Only] Camera this object is associated with.

<a id="unreal.CameraModifier.alpha_in_time"></a>

#### alpha_in_time

```python
@property
def alpha_in_time() -> float
```

(float):  [Read-Only] When blending in, alpha proceeds from 0 to 1 over this time

<a id="unreal.CameraModifier.alpha_out_time"></a>

#### alpha_out_time

```python
@property
def alpha_out_time() -> float
```

(float):  [Read-Only] When blending out, alpha proceeds from 1 to 0 over this time

<a id="unreal.CameraModifier.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Only] Current blend alpha.

<a id="unreal.CameraModifier.is_pending_disable"></a>

#### is_pending_disable

```python
def is_pending_disable() -> bool
```

x.is_pending_disable() -> bool


Returns:
    bool: Returns true if modifier is pending disable, false otherwise.

<a id="unreal.CameraModifier.is_disabled"></a>

#### is_disabled

```python
def is_disabled() -> bool
```

x.is_disabled() -> bool


Returns:
    bool: Returns true if modifier is disabled, false otherwise.

<a id="unreal.CameraModifier.get_view_target"></a>

#### get_view_target

```python
def get_view_target() -> Actor
```

x.get_view_target() -> Actor


Returns:
    Actor: Returns the actor the camera is currently viewing.

<a id="unreal.CameraModifier.enable_modifier"></a>

#### enable_modifier

```python
def enable_modifier() -> None
```

x.enable_modifier() -> None
Enables this modifier.

<a id="unreal.CameraModifier.disable_modifier"></a>

#### disable_modifier

```python
def disable_modifier(immediate: bool = False) -> None
```

x.disable_modifier(immediate=False) -> None
Disables this modifier.

Args:
    immediate (bool): true to disable with no blend out, false (default) to allow blend out

<a id="unreal.CameraModifier.blueprint_modify_post_process"></a>

#### blueprint_modify_post_process

```python
def blueprint_modify_post_process(
        delta_time: float) -> Tuple[float, PostProcessSettings]
```

x.blueprint_modify_post_process(delta_time) -> (post_process_blend_weight=float, post_process_settings=PostProcessSettings)
Called per tick that the modifier is active to allow Blueprinted modifiers to modify the camera's postprocess effects.
Scaling by Alpha happens after this in code, so no need to deal with that in the blueprint.

Args:
    delta_time (float): Change in time since last update

Returns:
    tuple: 

    post_process_blend_weight (float): (out) Blend weight applied to the entire postprocess structure.

    post_process_settings (PostProcessSettings): (out) Post process structure defining what settings and values to override.

<a id="unreal.CameraModifier.blueprint_modify_camera"></a>

#### blueprint_modify_camera

```python
def blueprint_modify_camera(delta_time: float, view_location: Vector,
                            view_rotation: Rotator,
                            fov: float) -> Tuple[Vector, Rotator, float]
```

x.blueprint_modify_camera(delta_time, view_location, view_rotation, fov) -> (new_view_location=Vector, new_view_rotation=Rotator, new_fov=float)
Called per tick that the modifier is active to allow Blueprinted modifiers to modify the camera's transform.
Scaling by Alpha happens after this in code, so no need to deal with that in the blueprint.

Args:
    delta_time (float): Change in time since last update
    view_location (Vector): The current camera location.
    view_rotation (Rotator): The current camera rotation.
    fov (float): The current camera fov.

Returns:
    tuple: 

    new_view_location (Vector): (out) The modified camera location.

    new_view_rotation (Rotator): (out) The modified camera rotation.

    new_fov (float): (out) The modified camera FOV.

<a id="unreal.CameraModifier_CameraShake"></a>