## SoundNodeDoppler Objects

```python
class SoundNodeDoppler(SoundNode)
```

Computes doppler pitch shift

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeDoppler.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``doppler_intensity`` (float):  [Read-Write] How much to scale the doppler shift (1.0 is normal).
- ``smoothing_interp_speed`` (float):  [Read-Write] Speed at which to interp pitch scale
- ``use_smoothing`` (bool):  [Read-Write] Whether or not to do a smooth interp to our doppler

<a id="unreal.SoundNodeEnveloper"></a>