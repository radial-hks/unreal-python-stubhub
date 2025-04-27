## SoundfieldEndpointSubmix Objects

```python
class SoundfieldEndpointSubmix(SoundSubmixBase)
```

Sound Submix class meant for sending soundfield-encoded audio to an external endpoint, such as a hardware binaural renderer that supports ambisonics.

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_disable`` (bool):  [Read-Write] Auto-manage enabling and disabling the submix as a CPU optimization. It will be disabled if the submix and all child submixes are silent. It will re-enable if a sound is sent to the submix or a child submix is audible.
- ``auto_disable_time`` (float):  [Read-Write] The minimum amount of time to wait before automatically disabling a submix if it is silent. Will immediately re-enable if source audio is sent to it.
- ``child_submixes`` (Array[SoundSubmixBase]):  [Read-Only] Child submixes to this sound mix
- ``encoding_settings`` (SoundfieldEncodingSettingsBase):  [Read-Write]
- ``endpoint_settings`` (SoundfieldEndpointSettingsBase):  [Read-Write]
- ``soundfield_effect_chain`` (Array[SoundfieldEffectBase]):  [Read-Write]
- ``soundfield_endpoint_type`` (Name):  [Read-Write] Currently used format.

<a id="unreal.SpectatorPawn"></a>