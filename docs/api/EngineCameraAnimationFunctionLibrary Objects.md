## EngineCameraAnimationFunctionLibrary Objects

```python
class EngineCameraAnimationFunctionLibrary(BlueprintFunctionLibrary)
```

Blueprint function library for autocasting a player camera manager into the camera animation camera modifier.
This prevents breaking Blueprints now that APlayerCameraManager::StartCameraShake returns the base class.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: CameraAnimationCameraModifier.h

<a id="unreal.EngineCameraAnimationFunctionLibrary.conv_camera_shake_play_space"></a>

#### conv_camera_shake_play_space

```python
@classmethod
def conv_camera_shake_play_space(
    cls, camera_animation_play_space: CameraAnimationPlaySpace
) -> CameraShakePlaySpace
```

X.conv_camera_shake_play_space(camera_animation_play_space) -> CameraShakePlaySpace
Conv Camera Shake Play Space

Args:
    camera_animation_play_space (CameraAnimationPlaySpace): 

Returns:
    CameraShakePlaySpace:

<a id="unreal.EngineCameraAnimationFunctionLibrary.conv_camera_animation_play_space"></a>

#### conv_camera_animation_play_space

```python
@classmethod
def conv_camera_animation_play_space(
        cls, camera_shake_play_space: CameraShakePlaySpace
) -> CameraAnimationPlaySpace
```

X.conv_camera_animation_play_space(camera_shake_play_space) -> CameraAnimationPlaySpace
Conv Camera Animation Play Space

Args:
    camera_shake_play_space (CameraShakePlaySpace): 

Returns:
    CameraAnimationPlaySpace:

<a id="unreal.EngineCameraAnimationFunctionLibrary.conv_camera_animation_camera_modifier"></a>

#### conv_camera_animation_camera_modifier

```python
@classmethod
def conv_camera_animation_camera_modifier(
    cls, player_camera_manager: PlayerCameraManager
) -> CameraAnimationCameraModifier
```

X.conv_camera_animation_camera_modifier(player_camera_manager) -> CameraAnimationCameraModifier
Conv Camera Animation Camera Modifier

Args:
    player_camera_manager (PlayerCameraManager): 

Returns:
    CameraAnimationCameraModifier:

<a id="unreal.GameplayCamerasFunctionLibrary"></a>