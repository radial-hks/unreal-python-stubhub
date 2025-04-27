## SoundNodeEnveloper Objects

```python
class SoundNodeEnveloper(SoundNode)
```

Allows manipulation of volume and pitch over a set time period

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeEnveloper.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``duration_after_loop`` (float):  [Read-Write] The time in seconds it takes the evelope to fade out after the last loop is completed.
- ``loop`` (bool):  [Read-Write] If enabled, the envelope will loop using the loop settings.
- ``loop_count`` (int32):  [Read-Write] The number of times the envelope should loop if looping is enabled and the envelope is not set to loop indefinitely.
- ``loop_end`` (float):  [Read-Write] The time in seconds where the envelope's loop ends.
- ``loop_indefinitely`` (bool):  [Read-Write] If enabled, the envelope will continue to loop indefenitely regardless of the Loop Count value.
- ``loop_start`` (float):  [Read-Write] The time in seconds where the envelope's loop begins.
- ``pitch_curve`` (RuntimeFloatCurve):  [Read-Write] The distribution defining the pitch envelope.
- ``pitch_max`` (float):  [Read-Write] The upper bound of pitch (1.0 is no change)
- ``pitch_min`` (float):  [Read-Write] The lower bound of pitch (1.0 is no change)
- ``volume_curve`` (RuntimeFloatCurve):  [Read-Write] The distribution defining the volume envelope.
- ``volume_max`` (float):  [Read-Write] The upper bound of volume (1.0 is no change)
- ``volume_min`` (float):  [Read-Write] The lower bound of volume (1.0 is no change)

<a id="unreal.SoundNodeGroupControl"></a>