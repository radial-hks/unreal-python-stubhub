## LegacyCameraShakeFunctionLibrary Objects

```python
class LegacyCameraShakeFunctionLibrary(BlueprintFunctionLibrary)
```

Blueprint function library for autocasting from a base camera shake to a legacy camera shake.
This prevents breaking Blueprints now that APlayerCameraManager::StartCameraShake returns the base class.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: LegacyCameraShake.h

<a id="unreal.LegacyCameraShakeFunctionLibrary.conv_legacy_camera_shake"></a>

#### conv_legacy_camera_shake

```python
@classmethod
def conv_legacy_camera_shake(
        cls, camera_shake: CameraShakeBase) -> LegacyCameraShake
```

X.conv_legacy_camera_shake(camera_shake) -> LegacyCameraShake
Conv Legacy Camera Shake

Args:
    camera_shake (CameraShakeBase): 

Returns:
    LegacyCameraShake:

<a id="unreal.LegacyCameraShakeFunctionLibrary.conv_matinee_camera_shake"></a>

#### conv_matinee_camera_shake

```python
@classmethod
def conv_matinee_camera_shake(
        cls, camera_shake: CameraShakeBase) -> LegacyCameraShake
```

deprecated: 'conv_matinee_camera_shake' was renamed to 'conv_legacy_camera_shake'.

<a id="unreal.MatineeCameraShakeFunctionLibrary"></a>