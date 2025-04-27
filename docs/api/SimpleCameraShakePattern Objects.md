## SimpleCameraShakePattern Objects

```python
class SimpleCameraShakePattern(CameraShakePattern)
```

A base class for a simple camera shake.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: SimpleCameraShakePattern.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_in_time`` (float):  [Read-Write] Blend-in time for this shake. Zero or less means no blend-in.
- ``blend_out_time`` (float):  [Read-Write] Blend-out time for this shake. Zero or less means no blend-out.
- ``duration`` (float):  [Read-Write] Duration in seconds of this shake. Zero or less means infinite.

<a id="unreal.PerlinNoiseCameraShakePattern"></a>