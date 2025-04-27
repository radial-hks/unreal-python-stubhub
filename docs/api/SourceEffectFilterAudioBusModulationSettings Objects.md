## SourceEffectFilterAudioBusModulationSettings Objects

```python
class SourceEffectFilterAudioBusModulationSettings(StructBase)
```

Source Effect Filter Audio Bus Modulation Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_bus`` (AudioBus):  [Read-Write] Audio bus to use to modulate the filter
- ``envelope_follower_attack_time_msec`` (int32):  [Read-Write] The amplitude envelope follower attack time (in milliseconds) on the audio bus.
- ``envelope_follower_release_time_msec`` (int32):  [Read-Write] The amplitude envelope follower release time (in milliseconds) on the audio bus.
- ``envelope_gain_multiplier`` (float):  [Read-Write] An amount to scale the envelope follower output to map to the modulation values.
- ``filter_param`` (SourceEffectFilterParam):  [Read-Write] Which parameter to modulate.
- ``max_frequency_modulation`` (float):  [Read-Write] The frequency modulation value (in semitones from the filter frequency) to use when the envelope is loudest
- ``max_resonance_modulation`` (float):  [Read-Write] The resonance modulation value to use when the envelope is loudest
- ``min_frequency_modulation`` (float):  [Read-Write] The frequency modulation value (in semitones from the filter frequency) to use when the envelope is quietest
- ``min_resonance_modulation`` (float):  [Read-Write] The resonance modulation value to use when the envelope is quietest

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.__init__"></a>

#### __init__

```python
def __init__(audio_bus: AudioBus = None,
             envelope_follower_attack_time_msec: int = 0,
             envelope_follower_release_time_msec: int = 0,
             envelope_gain_multiplier: float = 0.000000,
             min_frequency_modulation: float = 0.000000,
             max_frequency_modulation: float = 0.000000,
             min_resonance_modulation: float = 0.000000,
             max_resonance_modulation: float = 0.000000) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.audio_bus"></a>

#### audio_bus

```python
@property
def audio_bus() -> AudioBus
```

(AudioBus):  [Read-Write] Audio bus to use to modulate the filter

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.audio_bus"></a>

#### audio_bus

```python
@audio_bus.setter
def audio_bus(value: AudioBus) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.envelope_follower_attack_time_msec"></a>

#### envelope_follower_attack_time_msec

```python
@property
def envelope_follower_attack_time_msec() -> int
```

(int32):  [Read-Write] The amplitude envelope follower attack time (in milliseconds) on the audio bus.

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.envelope_follower_attack_time_msec"></a>

#### envelope_follower_attack_time_msec

```python
@envelope_follower_attack_time_msec.setter
def envelope_follower_attack_time_msec(value: int) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.envelope_follower_release_time_msec"></a>

#### envelope_follower_release_time_msec

```python
@property
def envelope_follower_release_time_msec() -> int
```

(int32):  [Read-Write] The amplitude envelope follower release time (in milliseconds) on the audio bus.

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.envelope_follower_release_time_msec"></a>

#### envelope_follower_release_time_msec

```python
@envelope_follower_release_time_msec.setter
def envelope_follower_release_time_msec(value: int) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.envelope_gain_multiplier"></a>

#### envelope_gain_multiplier

```python
@property
def envelope_gain_multiplier() -> float
```

(float):  [Read-Write] An amount to scale the envelope follower output to map to the modulation values.

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.envelope_gain_multiplier"></a>

#### envelope_gain_multiplier

```python
@envelope_gain_multiplier.setter
def envelope_gain_multiplier(value: float) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.min_frequency_modulation"></a>

#### min_frequency_modulation

```python
@property
def min_frequency_modulation() -> float
```

(float):  [Read-Write] The frequency modulation value (in semitones from the filter frequency) to use when the envelope is quietest

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.min_frequency_modulation"></a>

#### min_frequency_modulation

```python
@min_frequency_modulation.setter
def min_frequency_modulation(value: float) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.max_frequency_modulation"></a>

#### max_frequency_modulation

```python
@property
def max_frequency_modulation() -> float
```

(float):  [Read-Write] The frequency modulation value (in semitones from the filter frequency) to use when the envelope is loudest

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.max_frequency_modulation"></a>

#### max_frequency_modulation

```python
@max_frequency_modulation.setter
def max_frequency_modulation(value: float) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.min_resonance_modulation"></a>

#### min_resonance_modulation

```python
@property
def min_resonance_modulation() -> float
```

(float):  [Read-Write] The resonance modulation value to use when the envelope is quietest

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.min_resonance_modulation"></a>

#### min_resonance_modulation

```python
@min_resonance_modulation.setter
def min_resonance_modulation(value: float) -> None
```

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.max_resonance_modulation"></a>

#### max_resonance_modulation

```python
@property
def max_resonance_modulation() -> float
```

(float):  [Read-Write] The resonance modulation value to use when the envelope is loudest

<a id="unreal.SourceEffectFilterAudioBusModulationSettings.max_resonance_modulation"></a>

#### max_resonance_modulation

```python
@max_resonance_modulation.setter
def max_resonance_modulation(value: float) -> None
```

<a id="unreal.SourceEffectFilterSettings"></a>