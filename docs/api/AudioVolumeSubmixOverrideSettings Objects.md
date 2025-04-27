## AudioVolumeSubmixOverrideSettings Objects

```python
class AudioVolumeSubmixOverrideSettings(StructBase)
```

Audio Volume Submix Override Settings

**C++ Source:**

- **Module**: Engine
- **File**: AudioVolume.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``crossfade_time`` (float):  [Read-Write] The amount of time to crossfade to the override for the submix chain
- ``submix`` (SoundSubmix):  [Read-Write] The submix to override the effect chain of
- ``submix_effect_chain`` (Array[SoundEffectSubmixPreset]):  [Read-Write] The submix effect chain to override

<a id="unreal.AudioVolumeSubmixOverrideSettings.__init__"></a>

#### __init__

```python
def __init__(submix: SoundSubmix = None,
             submix_effect_chain: Array[SoundEffectSubmixPreset] = [],
             crossfade_time: float = 0.000000) -> None
```

<a id="unreal.AudioVolumeSubmixOverrideSettings.submix"></a>

#### submix

```python
@property
def submix() -> SoundSubmix
```

(SoundSubmix):  [Read-Write] The submix to override the effect chain of

<a id="unreal.AudioVolumeSubmixOverrideSettings.submix"></a>

#### submix

```python
@submix.setter
def submix(value: SoundSubmix) -> None
```

<a id="unreal.AudioVolumeSubmixOverrideSettings.submix_effect_chain"></a>

#### submix_effect_chain

```python
@property
def submix_effect_chain() -> Array[SoundEffectSubmixPreset]
```

(Array[SoundEffectSubmixPreset]):  [Read-Only] The submix effect chain to override

<a id="unreal.AudioVolumeSubmixOverrideSettings.crossfade_time"></a>

#### crossfade_time

```python
@property
def crossfade_time() -> float
```

(float):  [Read-Only] The amount of time to crossfade to the override for the submix chain

<a id="unreal.InteriorSettings"></a>