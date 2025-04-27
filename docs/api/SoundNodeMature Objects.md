## SoundNodeMature Objects

```python
class SoundNodeMature(SoundNode)
```

This SoundNode uses UEngine::bAllowMatureLanguage to determine whether child nodes
that have USoundWave::bMature=true should be played.

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeMature.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]

<a id="unreal.SoundNodeMixer"></a>