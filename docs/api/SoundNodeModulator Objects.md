## SoundNodeModulator Objects

```python
class SoundNodeModulator(SoundNode)
```

Defines a random volume and pitch modification when a sound starts

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeModulator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``pitch_max`` (float):  [Read-Write] The upper bound of pitch (1.0 is no change).
- ``pitch_min`` (float):  [Read-Write] The lower bound of pitch (1.0 is no change).
- ``volume_max`` (float):  [Read-Write] The upper bound of volume (1.0 is no change).
- ``volume_min`` (float):  [Read-Write] The lower bound of volume (1.0 is no change).

<a id="unreal.SoundNodeOscillator"></a>