## SoundNodeParamCrossFade Objects

```python
class SoundNodeParamCrossFade(SoundNodeDistanceCrossFade)
```

Crossfades between different sounds based on a parameter

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeParamCrossFade.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``cross_fade_input`` (Array[DistanceDatum]):  [Read-Write] Each input needs to have the correct data filled in so the SoundNodeDistanceCrossFade is able
  to determine which sounds to play
- ``param_name`` (Name):  [Read-Write] Parameter controlling cross fades.

<a id="unreal.SoundNodeQualityLevel"></a>