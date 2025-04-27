## LegacyCameraShake Objects

```python
class LegacyCameraShake(CameraShakeBase)
```

Legacy camera shake which can do either oscillation or run camera anims.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: LegacyCameraShake.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_blend_in_time`` (float):  [Read-Write] Linear blend-in time.
- ``anim_blend_out_time`` (float):  [Read-Write] Linear blend-out time.
- ``anim_play_rate`` (float):  [Read-Write] Scalar defining how fast to play the anim.
- ``anim_scale`` (float):  [Read-Write] Scalar defining how "intense" to play the anim.
- ``anim_sequence`` (CameraAnimationSequence):  [Read-Write] Source camera animation sequence to play. Can be null.
- ``fov_oscillation`` (FOscillator):  [Read-Write] FOV oscillation
- ``loc_oscillation`` (VOscillator):  [Read-Write] Positional oscillation
- ``oscillation_blend_in_time`` (float):  [Read-Write] Duration of the blend-in, where the oscillation scales from 0 to 1.
- ``oscillation_blend_out_time`` (float):  [Read-Write] Duration of the blend-out, where the oscillation scales from 1 to 0.
- ``oscillation_duration`` (float):  [Read-Write] Duration in seconds of current screen shake. Less than 0 means indefinite, 0 means no oscillation.
- ``oscillator_time_remaining`` (float):  [Read-Write] Time remaining for oscillation shakes. Less than 0.f means shake infinitely.
- ``random_anim_segment`` (bool):  [Read-Write] If true, play a random snippet of the animation of length Duration.  Implies bLoop and bRandomStartTime = true for the AnimSequence.
  If false, play the full anim once, non-looped. Useful for getting variety out of a single looped AnimSequence asset.
- ``random_anim_segment_duration`` (float):  [Read-Write] When bRandomAnimSegment is true, this defines how long the anim should play.
- ``root_shake_pattern`` (CameraShakePattern):  [Read-Write] The root pattern for this camera shake
- ``rot_oscillation`` (ROscillator):  [Read-Write] Rotational oscillation
- ``shake_scale`` (float):  [Read-Write] The overall scale to apply to the shake. Only valid when the shake is active.
- ``single_instance`` (bool):  [Read-Write] If true to only allow a single instance of this shake class to play at any given time.
  Subsequent attempts to play this shake will simply restart the timer.

<a id="unreal.LegacyCameraShake.rot_oscillation"></a>

#### rot_oscillation

```python
@property
def rot_oscillation() -> ROscillator
```

(ROscillator):  [Read-Write] Rotational oscillation

<a id="unreal.LegacyCameraShake.rot_oscillation"></a>

#### rot_oscillation

```python
@rot_oscillation.setter
def rot_oscillation(value: ROscillator) -> None
```

<a id="unreal.LegacyCameraShake.loc_oscillation"></a>

#### loc_oscillation

```python
@property
def loc_oscillation() -> VOscillator
```

(VOscillator):  [Read-Write] Positional oscillation

<a id="unreal.LegacyCameraShake.loc_oscillation"></a>

#### loc_oscillation

```python
@loc_oscillation.setter
def loc_oscillation(value: VOscillator) -> None
```

<a id="unreal.LegacyCameraShake.fov_oscillation"></a>

#### fov_oscillation

```python
@property
def fov_oscillation() -> FOscillator
```

(FOscillator):  [Read-Write] FOV oscillation

<a id="unreal.LegacyCameraShake.fov_oscillation"></a>

#### fov_oscillation

```python
@fov_oscillation.setter
def fov_oscillation(value: FOscillator) -> None
```

<a id="unreal.LegacyCameraShake.oscillator_time_remaining"></a>

#### oscillator_time_remaining

```python
@property
def oscillator_time_remaining() -> float
```

(float):  [Read-Only] Time remaining for oscillation shakes. Less than 0.f means shake infinitely.

<a id="unreal.LegacyCameraShake.start_legacy_camera_shake_from_source"></a>

#### start_legacy_camera_shake_from_source

```python
@classmethod
def start_legacy_camera_shake_from_source(
    cls,
    player_camera_manager: PlayerCameraManager,
    shake_class: Class,
    source_component: CameraShakeSourceComponent,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> LegacyCameraShake
```

X.start_legacy_camera_shake_from_source(player_camera_manager, shake_class, source_component, scale=1.000000, play_space=CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot=[0.000000, 0.000000, 0.000000]) -> LegacyCameraShake
Backwards compatible method used by core BP redirectors. This is needed because the return value is specifically a legacy camera shake,
which some BP logic often uses directly to set oscillator/anim properties.

Args:
    player_camera_manager (PlayerCameraManager): 
    shake_class (type(Class)): 
    source_component (CameraShakeSourceComponent): 
    scale (float): 
    play_space (CameraShakePlaySpace): 
    user_play_space_rot (Rotator): 

Returns:
    LegacyCameraShake:

<a id="unreal.LegacyCameraShake.start_matinee_camera_shake_from_source"></a>

#### start_matinee_camera_shake_from_source

```python
@classmethod
def start_matinee_camera_shake_from_source(
    cls,
    player_camera_manager: PlayerCameraManager,
    shake_class: Class,
    source_component: CameraShakeSourceComponent,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> LegacyCameraShake
```

deprecated: 'start_matinee_camera_shake_from_source' was renamed to 'start_legacy_camera_shake_from_source'.

<a id="unreal.LegacyCameraShake.start_legacy_camera_shake"></a>

#### start_legacy_camera_shake

```python
@classmethod
def start_legacy_camera_shake(
    cls,
    player_camera_manager: PlayerCameraManager,
    shake_class: Class,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> LegacyCameraShake
```

X.start_legacy_camera_shake(player_camera_manager, shake_class, scale=1.000000, play_space=CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot=[0.000000, 0.000000, 0.000000]) -> LegacyCameraShake
Backwards compatible method used by core BP redirectors. This is needed because the return value is specifically a legacy camera shake,
which some BP logic often uses directly to set oscillator/anim properties.

Args:
    player_camera_manager (PlayerCameraManager): 
    shake_class (type(Class)): 
    scale (float): 
    play_space (CameraShakePlaySpace): 
    user_play_space_rot (Rotator): 

Returns:
    LegacyCameraShake:

<a id="unreal.LegacyCameraShake.start_matinee_camera_shake"></a>

#### start_matinee_camera_shake

```python
@classmethod
def start_matinee_camera_shake(
    cls,
    player_camera_manager: PlayerCameraManager,
    shake_class: Class,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> LegacyCameraShake
```

deprecated: 'start_matinee_camera_shake' was renamed to 'start_legacy_camera_shake'.

<a id="unreal.LegacyCameraShake.receive_stop_shake"></a>

#### receive_stop_shake

```python
def receive_stop_shake(immediately: bool) -> None
```

x.receive_stop_shake(immediately) -> None
Called when the shake is explicitly stopped.

Args:
    immediately (bool):

<a id="unreal.LegacyCameraShake.receive_play_shake"></a>

#### receive_play_shake

```python
def receive_play_shake(scale: float) -> None
```

x.receive_play_shake(scale) -> None
Called when the shake starts playing

Args:
    scale (float):

<a id="unreal.LegacyCameraShake.receive_is_finished"></a>

#### receive_is_finished

```python
def receive_is_finished() -> bool
```

x.receive_is_finished() -> bool
Called to allow a shake to decide when it's finished playing.

Returns:
    bool:

<a id="unreal.LegacyCameraShake.blueprint_update_camera_shake"></a>

#### blueprint_update_camera_shake

```python
def blueprint_update_camera_shake(delta_time: float, alpha: float,
                                  pov: MinimalViewInfo) -> MinimalViewInfo
```

x.blueprint_update_camera_shake(delta_time, alpha, pov) -> MinimalViewInfo
Called every tick to let the shake modify the point of view

Args:
    delta_time (float): 
    alpha (float): 
    pov (MinimalViewInfo): 

Returns:
    MinimalViewInfo: 

    modified_pov (MinimalViewInfo):

<a id="unreal.CameraShake"></a>