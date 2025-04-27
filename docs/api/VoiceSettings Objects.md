## VoiceSettings Objects

```python
class VoiceSettings(StructBase)
```

Voice Settings

**C++ Source:**

- **Module**: Engine
- **File**: VoiceConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attenuation_settings`` (SoundAttenuation):  [Read-Write] Optional attenuation settings to attach to this player's voice.
  This should only be used when ComponentToAttachTo is set.
- ``component_to_attach_to`` (SceneComponent):  [Read-Write] Optionally attach the voice source to a Scene Component to give the appearance
  that the voice is coming from that scene component.
  If this is not set, the voice will not be spatialized.
- ``source_effect_chain`` (SoundEffectSourcePresetChain):  [Read-Write] Optional audio effects to apply to this player's voice.

<a id="unreal.VoiceSettings.__init__"></a>

#### __init__

```python
def __init__(component_to_attach_to: SceneComponent = None,
             attenuation_settings: SoundAttenuation = None,
             source_effect_chain: SoundEffectSourcePresetChain = None) -> None
```

<a id="unreal.VoiceSettings.component_to_attach_to"></a>

#### component_to_attach_to

```python
@property
def component_to_attach_to() -> SceneComponent
```

(SceneComponent):  [Read-Write] Optionally attach the voice source to a Scene Component to give the appearance
that the voice is coming from that scene component.
If this is not set, the voice will not be spatialized.

<a id="unreal.VoiceSettings.component_to_attach_to"></a>

#### component_to_attach_to

```python
@component_to_attach_to.setter
def component_to_attach_to(value: SceneComponent) -> None
```

<a id="unreal.VoiceSettings.attenuation_settings"></a>

#### attenuation_settings

```python
@property
def attenuation_settings() -> SoundAttenuation
```

(SoundAttenuation):  [Read-Write] Optional attenuation settings to attach to this player's voice.
This should only be used when ComponentToAttachTo is set.

<a id="unreal.VoiceSettings.attenuation_settings"></a>

#### attenuation_settings

```python
@attenuation_settings.setter
def attenuation_settings(value: SoundAttenuation) -> None
```

<a id="unreal.VoiceSettings.source_effect_chain"></a>

#### source_effect_chain

```python
@property
def source_effect_chain() -> SoundEffectSourcePresetChain
```

(SoundEffectSourcePresetChain):  [Read-Write] Optional audio effects to apply to this player's voice.

<a id="unreal.VoiceSettings.source_effect_chain"></a>

#### source_effect_chain

```python
@source_effect_chain.setter
def source_effect_chain(value: SoundEffectSourcePresetChain) -> None
```

<a id="unreal.ActorDesc"></a>