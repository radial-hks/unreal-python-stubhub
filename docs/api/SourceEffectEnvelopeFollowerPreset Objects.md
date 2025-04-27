## SourceEffectEnvelopeFollowerPreset Objects

```python
class SourceEffectEnvelopeFollowerPreset(SoundEffectSourcePreset)
```

Source Effect Envelope Follower Preset

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectEnvelopeFollower.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SourceEffectEnvelopeFollowerSettings):  [Read-Write]

<a id="unreal.SourceEffectEnvelopeFollowerPreset.settings"></a>

#### settings

```python
@property
def settings() -> SourceEffectEnvelopeFollowerSettings
```

(SourceEffectEnvelopeFollowerSettings):  [Read-Only]

<a id="unreal.SourceEffectEnvelopeFollowerPreset.unregister_envelope_follower_listener"></a>

#### unregister_envelope_follower_listener

```python
def unregister_envelope_follower_listener(
        envelope_follower_listener: EnvelopeFollowerListener) -> None
```

x.unregister_envelope_follower_listener(envelope_follower_listener) -> None
Unregisters an envelope follower listener with the effect.

Args:
    envelope_follower_listener (EnvelopeFollowerListener):

<a id="unreal.SourceEffectEnvelopeFollowerPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SourceEffectEnvelopeFollowerSettings) -> None
```

x.set_settings(settings) -> None
Set Settings

Args:
    settings (SourceEffectEnvelopeFollowerSettings):

<a id="unreal.SourceEffectEnvelopeFollowerPreset.register_envelope_follower_listener"></a>

#### register_envelope_follower_listener

```python
def register_envelope_follower_listener(
        envelope_follower_listener: EnvelopeFollowerListener) -> None
```

x.register_envelope_follower_listener(envelope_follower_listener) -> None
Registers an envelope follower listener with the effect.

Args:
    envelope_follower_listener (EnvelopeFollowerListener):

<a id="unreal.SourceEffectEQPreset"></a>