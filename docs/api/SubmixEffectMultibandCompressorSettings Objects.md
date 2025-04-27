## SubmixEffectMultibandCompressorSettings Objects

```python
class SubmixEffectMultibandCompressorSettings(StructBase)
```

A submix dynamics processor

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectMultiBandCompressor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``analog_mode`` (bool):  [Read-Write] Toggles treating the attack and release envelopes as analog-style vs digital-style. Analog will respond a bit more naturally/slower.
- ``bands`` (Array[DynamicsBandSettings]):  [Read-Write] Each band is a full dynamics processor, affecting at a unique frequency range
- ``bypass`` (bool):  [Read-Write] Whether or not to bypass effect
- ``dynamics_processor_type`` (SubmixEffectDynamicsProcessorType):  [Read-Write] Controls how each band will react to audio above its threshold
- ``external_audio_bus`` (AudioBus):  [Read-Write] If set, uses output of provided submix as modulator of input signal for dynamics processor (Uses input signal as default modulator)
- ``external_submix`` (SoundSubmix):  [Read-Write] If set, uses output of provided submix as modulator of input signal for dynamics processor (Uses input signal as default modulator)
- ``four_pole`` (bool):  [Read-Write] Turning off FourPole mode will use cheaper, shallower 2-pole crossovers
- ``key_audition`` (bool):  [Read-Write] Audition the key modulation signal, bypassing enveloping and processing the input signal.
- ``key_gain_db`` (float):  [Read-Write] Gain to apply to key signal if external input is supplied
- ``key_source`` (SubmixEffectDynamicsKeySource):  [Read-Write]
- ``link_mode`` (SubmixEffectDynamicsChannelLinkMode):  [Read-Write] Whether to compress all channels equally, and how to evaluate the overall level
- ``look_ahead_msec`` (float):  [Read-Write] The amount of time to look ahead of the current audio. Allows for transients to be included in dynamics processing.
- ``peak_mode`` (SubmixEffectDynamicsPeakMode):  [Read-Write] Controls how quickly the bands will react to a signal above its threshold

<a id="unreal.SubmixEffectMultibandCompressorSettings.__init__"></a>

#### __init__

```python
def __init__(
        dynamics_processor_type:
    SubmixEffectDynamicsProcessorType = SubmixEffectDynamicsProcessorType.
    COMPRESSOR,
        peak_mode: SubmixEffectDynamicsPeakMode = SubmixEffectDynamicsPeakMode.
    MEAN_SQUARED,
        link_mode:
    SubmixEffectDynamicsChannelLinkMode = SubmixEffectDynamicsChannelLinkMode.
    DISABLED,
        look_ahead_msec: float = 0.000000,
        analog_mode: bool = False,
        four_pole: bool = False,
        bypass: bool = False,
        key_source:
    SubmixEffectDynamicsKeySource = SubmixEffectDynamicsKeySource.DEFAULT,
        external_audio_bus: AudioBus = None,
        external_submix: SoundSubmix = None,
        key_gain_db: float = 0.000000,
        key_audition: bool = False,
        bands: Array[DynamicsBandSettings] = []) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.dynamics_processor_type"></a>

#### dynamics_processor_type

```python
@property
def dynamics_processor_type() -> SubmixEffectDynamicsProcessorType
```

(SubmixEffectDynamicsProcessorType):  [Read-Write] Controls how each band will react to audio above its threshold

<a id="unreal.SubmixEffectMultibandCompressorSettings.dynamics_processor_type"></a>

#### dynamics_processor_type

```python
@dynamics_processor_type.setter
def dynamics_processor_type(value: SubmixEffectDynamicsProcessorType) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.peak_mode"></a>

#### peak_mode

```python
@property
def peak_mode() -> SubmixEffectDynamicsPeakMode
```

(SubmixEffectDynamicsPeakMode):  [Read-Write] Controls how quickly the bands will react to a signal above its threshold

<a id="unreal.SubmixEffectMultibandCompressorSettings.peak_mode"></a>

#### peak_mode

```python
@peak_mode.setter
def peak_mode(value: SubmixEffectDynamicsPeakMode) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.link_mode"></a>

#### link_mode

```python
@property
def link_mode() -> SubmixEffectDynamicsChannelLinkMode
```

(SubmixEffectDynamicsChannelLinkMode):  [Read-Write] Whether to compress all channels equally, and how to evaluate the overall level

<a id="unreal.SubmixEffectMultibandCompressorSettings.link_mode"></a>

#### link_mode

```python
@link_mode.setter
def link_mode(value: SubmixEffectDynamicsChannelLinkMode) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.look_ahead_msec"></a>

#### look_ahead_msec

```python
@property
def look_ahead_msec() -> float
```

(float):  [Read-Write] The amount of time to look ahead of the current audio. Allows for transients to be included in dynamics processing.

<a id="unreal.SubmixEffectMultibandCompressorSettings.look_ahead_msec"></a>

#### look_ahead_msec

```python
@look_ahead_msec.setter
def look_ahead_msec(value: float) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.analog_mode"></a>

#### analog_mode

```python
@property
def analog_mode() -> bool
```

(bool):  [Read-Write] Toggles treating the attack and release envelopes as analog-style vs digital-style. Analog will respond a bit more naturally/slower.

<a id="unreal.SubmixEffectMultibandCompressorSettings.analog_mode"></a>

#### analog_mode

```python
@analog_mode.setter
def analog_mode(value: bool) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.four_pole"></a>

#### four_pole

```python
@property
def four_pole() -> bool
```

(bool):  [Read-Write] Turning off FourPole mode will use cheaper, shallower 2-pole crossovers

<a id="unreal.SubmixEffectMultibandCompressorSettings.four_pole"></a>

#### four_pole

```python
@four_pole.setter
def four_pole(value: bool) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.bypass"></a>

#### bypass

```python
@property
def bypass() -> bool
```

(bool):  [Read-Write] Whether or not to bypass effect

<a id="unreal.SubmixEffectMultibandCompressorSettings.bypass"></a>

#### bypass

```python
@bypass.setter
def bypass(value: bool) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.key_source"></a>

#### key_source

```python
@property
def key_source() -> SubmixEffectDynamicsKeySource
```

(SubmixEffectDynamicsKeySource):  [Read-Write]

<a id="unreal.SubmixEffectMultibandCompressorSettings.key_source"></a>

#### key_source

```python
@key_source.setter
def key_source(value: SubmixEffectDynamicsKeySource) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.external_audio_bus"></a>

#### external_audio_bus

```python
@property
def external_audio_bus() -> AudioBus
```

(AudioBus):  [Read-Write] If set, uses output of provided submix as modulator of input signal for dynamics processor (Uses input signal as default modulator)

<a id="unreal.SubmixEffectMultibandCompressorSettings.external_audio_bus"></a>

#### external_audio_bus

```python
@external_audio_bus.setter
def external_audio_bus(value: AudioBus) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.external_submix"></a>

#### external_submix

```python
@property
def external_submix() -> SoundSubmix
```

(SoundSubmix):  [Read-Write] If set, uses output of provided submix as modulator of input signal for dynamics processor (Uses input signal as default modulator)

<a id="unreal.SubmixEffectMultibandCompressorSettings.external_submix"></a>

#### external_submix

```python
@external_submix.setter
def external_submix(value: SoundSubmix) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.key_gain_db"></a>

#### key_gain_db

```python
@property
def key_gain_db() -> float
```

(float):  [Read-Write] Gain to apply to key signal if external input is supplied

<a id="unreal.SubmixEffectMultibandCompressorSettings.key_gain_db"></a>

#### key_gain_db

```python
@key_gain_db.setter
def key_gain_db(value: float) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.key_audition"></a>

#### key_audition

```python
@property
def key_audition() -> bool
```

(bool):  [Read-Write] Audition the key modulation signal, bypassing enveloping and processing the input signal.

<a id="unreal.SubmixEffectMultibandCompressorSettings.key_audition"></a>

#### key_audition

```python
@key_audition.setter
def key_audition(value: bool) -> None
```

<a id="unreal.SubmixEffectMultibandCompressorSettings.bands"></a>

#### bands

```python
@property
def bands() -> Array[DynamicsBandSettings]
```

(Array[DynamicsBandSettings]):  [Read-Write] Each band is a full dynamics processor, affecting at a unique frequency range

<a id="unreal.SubmixEffectMultibandCompressorSettings.bands"></a>

#### bands

```python
@bands.setter
def bands(value: Array[DynamicsBandSettings]) -> None
```

<a id="unreal.SubmixEffectStereoDelaySettings"></a>