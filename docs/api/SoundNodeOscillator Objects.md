## SoundNodeOscillator Objects

```python
class SoundNodeOscillator(SoundNode)
```

Defines how a sound oscillates

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeOscillator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude_max`` (float):  [Read-Write] An amplitude of 0.25 would oscillate between 0.75 and 1.25.
- ``amplitude_min`` (float):  [Read-Write] An amplitude of 0.25 would oscillate between 0.75 and 1.25.
- ``center_max`` (float):  [Read-Write] A center of 0.5 would oscillate around 0.5.
- ``center_min`` (float):  [Read-Write] A center of 0.5 would oscillate around 0.5.
- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``frequency_max`` (float):  [Read-Write] A frequency of 20 would oscillate at 10Hz.
- ``frequency_min`` (float):  [Read-Write] A frequency of 20 would oscillate at 10Hz.
- ``modulate_pitch`` (bool):  [Read-Write] Whether to oscillate pitch.
- ``modulate_volume`` (bool):  [Read-Write] Whether to oscillate volume.
- ``offset_max`` (float):  [Read-Write] Offset into the sine wave. Value modded by 2 * PI.
- ``offset_min`` (float):  [Read-Write] Offset into the sine wave. Value modded by 2 * PI.

<a id="unreal.SoundNodeParamCrossFade"></a>