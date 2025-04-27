## SubmixEffectMultibandCompressorPreset Objects

```python
class SubmixEffectMultibandCompressorPreset(SoundEffectSubmixPreset)
```

Submix Effect Multiband Compressor Preset

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectMultiBandCompressor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SubmixEffectMultibandCompressorSettings):  [Read-Write]

<a id="unreal.SubmixEffectMultibandCompressorPreset.settings"></a>

#### settings

```python
@property
def settings() -> SubmixEffectMultibandCompressorSettings
```

(SubmixEffectMultibandCompressorSettings):  [Read-Write]

<a id="unreal.SubmixEffectMultibandCompressorPreset.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SubmixEffectMultibandCompressorSettings) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SubmixEffectMultibandCompressorSettings) -> None
```

x.set_settings(settings) -> None
Set Settings

Args:
    settings (SubmixEffectMultibandCompressorSettings):

<a id="unreal.SubmixEffectMultibandCompressorPreset.set_external_submix"></a>

#### set_external_submix

```python
def set_external_submix(submix: SoundSubmix) -> None
```

x.set_external_submix(submix) -> None
Sets the source key input as the provided Submix's output.  If no object is provided, key is set
to effect's input.

Args:
    submix (SoundSubmix):

<a id="unreal.SubmixEffectMultibandCompressorPreset.set_audio_bus"></a>

#### set_audio_bus

```python
def set_audio_bus(audio_bus: AudioBus) -> None
```

x.set_audio_bus(audio_bus) -> None
Sets the source key input as the provided AudioBus' output.  If no object is provided, key is set
to effect's input.

Args:
    audio_bus (AudioBus):

<a id="unreal.SubmixEffectMultibandCompressorPreset.reset_key"></a>

#### reset_key

```python
def reset_key() -> None
```

x.reset_key() -> None
Reset Key

<a id="unreal.SubmixEffectStereoDelayPreset"></a>