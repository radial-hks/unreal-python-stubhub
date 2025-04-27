## EngineCamerasSubsystem Objects

```python
class EngineCamerasSubsystem(WorldSubsystem)
```

World subsystem that holds global objects for handling camera animation sequences.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: EngineCamerasSubsystem.h

<a id="unreal.EngineCamerasSubsystem.stop_camera_animation"></a>

#### stop_camera_animation

```python
def stop_camera_animation(player_controller: PlayerController,
                          handle: CameraAnimationHandle,
                          immediate: bool = False) -> None
```

x.stop_camera_animation(player_controller, handle, immediate=False) -> None
Stops the given camera animation instance.

Args:
    player_controller (PlayerController): The player controller on which to play the animation.
    handle (CameraAnimationHandle): 
    immediate (bool): True to stop it right now and ignore blend out, false to let it blend out as indicated.

<a id="unreal.EngineCamerasSubsystem.stop_all_camera_animations_of"></a>

#### stop_all_camera_animations_of

```python
def stop_all_camera_animations_of(player_controller: PlayerController,
                                  sequence: CameraAnimationSequence,
                                  immediate: bool = False) -> None
```

x.stop_all_camera_animations_of(player_controller, sequence, immediate=False) -> None
Stop playing all instances of the given camera animation sequence.

Args:
    player_controller (PlayerController): The player controller on which to play the animation.
    sequence (CameraAnimationSequence): The sequence of which to stop all instances.
    immediate (bool): True to stop it right now and ignore blend out, false to let it blend out as indicated.

<a id="unreal.EngineCamerasSubsystem.stop_all_camera_animations"></a>

#### stop_all_camera_animations

```python
def stop_all_camera_animations(player_controller: PlayerController,
                               immediate: bool = False) -> None
```

x.stop_all_camera_animations(player_controller, immediate=False) -> None
Stop all camera animation instances.

Args:
    player_controller (PlayerController): The player controller on which to play the animation.
    immediate (bool): True to stop it right now and ignore blend out, false to let it blend out as indicated.

<a id="unreal.EngineCamerasSubsystem.play_camera_animation"></a>

#### play_camera_animation

```python
def play_camera_animation(
        player_controller: PlayerController, sequence: CameraAnimationSequence,
        params: CameraAnimationParams) -> CameraAnimationHandle
```

x.play_camera_animation(player_controller, sequence, params) -> CameraAnimationHandle
Play a new camera animation sequence.

Args:
    player_controller (PlayerController): The player controller on which to play the animation.
    sequence (CameraAnimationSequence): The sequence to use for the new camera animation.
    params (CameraAnimationParams): The parameters for the new camera animation instance.

Returns:
    CameraAnimationHandle:

<a id="unreal.EngineCamerasSubsystem.is_camera_animation_active"></a>

#### is_camera_animation_active

```python
def is_camera_animation_active(player_controller: PlayerController,
                               handle: CameraAnimationHandle) -> bool
```

x.is_camera_animation_active(player_controller, handle) -> bool
Returns whether the given camera animation is playing.

Args:
    player_controller (PlayerController): The player controller on which to play the animation.
    handle (CameraAnimationHandle): A handle to a previously started camera animation.

Returns:
    bool: Whether the corresponding camera animation is playing or not.

<a id="unreal.GameplayCamerasSubsystem"></a>