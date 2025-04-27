## SoundSubmixWithParentBase Objects

```python
class SoundSubmixWithParentBase(SoundSubmixBase)
```

This submix class can be derived from for submixes that output to a parent submix.

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_disable`` (bool):  [Read-Write] Auto-manage enabling and disabling the submix as a CPU optimization. It will be disabled if the submix and all child submixes are silent. It will re-enable if a sound is sent to the submix or a child submix is audible.
- ``auto_disable_time`` (float):  [Read-Write] The minimum amount of time to wait before automatically disabling a submix if it is silent. Will immediately re-enable if source audio is sent to it.
- ``child_submixes`` (Array[SoundSubmixBase]):  [Read-Only] Child submixes to this sound mix
- ``is_dynamic`` (bool):  [Read-Write] Is Submix Dynamic. (i.e. allows connect/disconnect at runtime.)  *
- ``parent_submix`` (SoundSubmixBase):  [Read-Only]

<a id="unreal.SoundSubmixWithParentBase.parent_submix"></a>

#### parent_submix

```python
@property
def parent_submix() -> SoundSubmixBase
```

(SoundSubmixBase):  [Read-Only]

<a id="unreal.SoundSubmixWithParentBase.is_dynamic"></a>

#### is_dynamic

```python
@property
def is_dynamic() -> bool
```

(bool):  [Read-Only] Is Submix Dynamic. (i.e. allows connect/disconnect at runtime.)  *

<a id="unreal.SoundSubmix"></a>