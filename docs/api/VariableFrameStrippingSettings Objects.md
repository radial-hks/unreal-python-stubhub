## VariableFrameStrippingSettings Objects

```python
class VariableFrameStrippingSettings(Object)
```

* This is a wrapper for the Variable frame stripping Codec.
* It allows for the mass changing of settings on animation sequences in an editor accessible way.

**C++ Source:**

- **Module**: Engine
- **File**: VariableFrameStrippingSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_stripping_rate`` (PerPlatformInt):  [Read-Write] The number of Frames that are stripped down to one.
  Allows for overrides of that multiplier.
  FrameStrippingRate == 1 would strip no frames, Therefore this is clamped to 2.
- ``use_variable_frame_stripping`` (PerPlatformBool):  [Read-Write] Enables the change from standard 1/2 frame stripping to stripping a higher amount of frames per frame kept

<a id="unreal.AnimCurveCompressionSettings"></a>