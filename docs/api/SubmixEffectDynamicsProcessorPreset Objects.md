## SubmixEffectDynamicsProcessorPreset Objects

```python
class SubmixEffectDynamicsProcessorPreset(SoundEffectSubmixPreset)
```

Submix Effect Dynamics Processor Preset

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerSubmixEffectDynamicsProcessor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SubmixEffectDynamicsProcessorSettings):  [Read-Write]

<a id="unreal.SubmixEffectDynamicsProcessorPreset.settings"></a>

#### settings

```python
@property
def settings() -> SubmixEffectDynamicsProcessorSettings
```

(SubmixEffectDynamicsProcessorSettings):  [Read-Write]

<a id="unreal.SubmixEffectDynamicsProcessorPreset.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SubmixEffectDynamicsProcessorSettings) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SubmixEffectDynamicsProcessorSettings) -> None
```

x.set_settings(settings) -> None
Set Settings

Args:
    settings (SubmixEffectDynamicsProcessorSettings):

<a id="unreal.SubmixEffectDynamicsProcessorPreset.set_external_submix"></a>

#### set_external_submix

```python
def set_external_submix(submix: SoundSubmix) -> None
```

x.set_external_submix(submix) -> None
Sets the source key input as the provided Submix's output.  If no object is provided, key is set
to effect's input.

Args:
    submix (SoundSubmix):

<a id="unreal.SubmixEffectDynamicsProcessorPreset.set_audio_bus"></a>

#### set_audio_bus

```python
def set_audio_bus(audio_bus: AudioBus) -> None
```

x.set_audio_bus(audio_bus) -> None
Sets the source key input as the provided AudioBus' output.  If no object is provided, key is set
to effect's input.

Args:
    audio_bus (AudioBus):

<a id="unreal.SubmixEffectDynamicsProcessorPreset.reset_key"></a>

#### reset_key

```python
def reset_key() -> None
```

x.reset_key() -> None
Reset Key

<a id="unreal.SubmixEffectSubmixEQPreset"></a>