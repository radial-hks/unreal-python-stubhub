## TestCameraShake Objects

```python
class TestCameraShake(CameraShakeBase)
```

Test Camera Shake

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: CameraShakeTestObjects.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``root_shake_pattern`` (CameraShakePattern):  [Read-Write] The root pattern for this camera shake
- ``shake_scale`` (float):  [Read-Write] The overall scale to apply to the shake. Only valid when the shake is active.
- ``single_instance`` (bool):  [Read-Write] If true to only allow a single instance of this shake class to play at any given time.
  Subsequent attempts to play this shake will simply restart the timer.

<a id="unreal.BlueprintCameraDirectorEvaluator"></a>