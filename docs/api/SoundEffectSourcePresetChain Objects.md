## SoundEffectSourcePresetChain Objects

```python
class SoundEffectSourcePresetChain(Object)
```

Chain of source effect presets that can be shared between referencing sounds.

**C++ Source:**

- **Module**: Engine
- **File**: SoundEffectSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chain`` (Array[SourceEffectChainEntry]):  [Read-Write] Chain of source effects to use for this sound source.
- ``play_effect_chain_tails`` (bool):  [Read-Write] Whether to keep the source alive for the duration of the effect chain tails.

<a id="unreal.SoundNode"></a>