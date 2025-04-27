## SubmixEffectReverbPreset Objects

```python
class SubmixEffectReverbPreset(SoundEffectSubmixPreset)
```

Submix Effect Reverb Preset

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerSubmixEffectReverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SubmixEffectReverbSettings):  [Read-Write]

<a id="unreal.SubmixEffectReverbPreset.settings"></a>

#### settings

```python
@property
def settings() -> SubmixEffectReverbSettings
```

(SubmixEffectReverbSettings):  [Read-Write]

<a id="unreal.SubmixEffectReverbPreset.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SubmixEffectReverbSettings) -> None
```

<a id="unreal.SubmixEffectReverbPreset.set_settings_with_reverb_effect"></a>

#### set_settings_with_reverb_effect

```python
def set_settings_with_reverb_effect(reverb_effect: ReverbEffect,
                                    wet_level: float,
                                    dry_level: float = 0.000000) -> None
```

x.set_settings_with_reverb_effect(reverb_effect, wet_level, dry_level=0.000000) -> None
Set Settings with Reverb Effect

Args:
    reverb_effect (ReverbEffect): 
    wet_level (float): 
    dry_level (float):

<a id="unreal.SubmixEffectReverbPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SubmixEffectReverbSettings) -> None
```

x.set_settings(settings) -> None
Set Settings

Args:
    settings (SubmixEffectReverbSettings):

<a id="unreal.SubmixEffectReverbFastPreset"></a>