## SoundMix Objects

```python
class SoundMix(Object)
```

Sound Mix

**C++ Source:**

- **Module**: Engine
- **File**: SoundMix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_eq`` (bool):  [Read-Write] Whether to apply the EQ effect
- ``duration`` (float):  [Read-Write] Duration of mix, negative means it will be applied until another mix is set.
- ``eq_priority`` (float):  [Read-Write]
- ``eq_settings`` (AudioEQEffect):  [Read-Write]
- ``fade_in_time`` (float):  [Read-Write] Time taken in seconds for the mix to fade in.
- ``fade_out_time`` (float):  [Read-Write] Time taken in seconds for the mix to fade out.
- ``initial_delay`` (float):  [Read-Write] Initial delay in seconds before the mix is applied.
- ``sound_class_effects`` (Array[SoundClassAdjuster]):  [Read-Write] Array of changes to be applied to groups.

<a id="unreal.SoundMix.sound_class_effects"></a>

#### sound_class_effects

```python
@property
def sound_class_effects() -> Array[SoundClassAdjuster]
```

(Array[SoundClassAdjuster]):  [Read-Only] Array of changes to be applied to groups.

<a id="unreal.SoundMode"></a>