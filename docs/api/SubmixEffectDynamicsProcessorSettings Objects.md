## SubmixEffectDynamicsProcessorSettings Objects

```python
class SubmixEffectDynamicsProcessorSettings(StructBase)
```

Submix dynamics processor settings

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerSubmixEffectDynamicsProcessor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``analog_mode`` (bool):  [Read-Write] Toggles treating the attack and release envelopes as analog-style vs digital-style (Analog will respond a bit more naturally/slower)
- ``attack_time_msec`` (float):  [Read-Write] The amount of time to ramp into any dynamics processing effect
- ``bypass`` (bool):  [Read-Write] Whether or not to bypass effect
- ``dynamics_processor_type`` (SubmixEffectDynamicsProcessorType):  [Read-Write] Type of processor to apply
- ``external_audio_bus`` (AudioBus):  [Read-Write] If set, uses output of provided audio bus as modulator of input signal for dynamics processor (Uses input signal as default modulator)
- ``external_submix`` (SoundSubmix):  [Read-Write] If set, uses output of provided submix as modulator of input signal for dynamics processor (Uses input signal as default modulator)
- ``input_gain_db`` (float):  [Read-Write] The input gain of the dynamics processor
- ``key_audition`` (bool):  [Read-Write] Audition the key modulation signal, bypassing enveloping and processing the input signal.
- ``key_gain_db`` (float):  [Read-Write] Gain to apply to key signal if key source not set to default (input).
- ``key_highshelf`` (SubmixEffectDynamicProcessorFilterSettings):  [Read-Write] High Shelf filter settings for key signal (external signal if supplied or input signal if not)
- ``key_lowshelf`` (SubmixEffectDynamicProcessorFilterSettings):  [Read-Write] Low Shelf filter settings for key signal (external signal if supplied or input signal if not)
- ``key_source`` (SubmixEffectDynamicsKeySource):  [Read-Write]
- ``knee_bandwidth_db`` (float):  [Read-Write] The knee bandwidth of the processor to use
- ``link_mode`` (SubmixEffectDynamicsChannelLinkMode):  [Read-Write] Mode of peak detection if key signal is multi-channel
- ``look_ahead_msec`` (float):  [Read-Write] The amount of time to look ahead of the current audio (Allows for transients to be included in dynamics processing)
- ``output_gain_db`` (float):  [Read-Write] The output gain of the dynamics processor
- ``peak_mode`` (SubmixEffectDynamicsPeakMode):  [Read-Write] Mode of peak detection used on input key signal
- ``ratio`` (float):  [Read-Write] The dynamics processor ratio used for compression/expansion
- ``release_time_msec`` (float):  [Read-Write] The amount of time to release the dynamics processing effect
- ``threshold_db`` (float):  [Read-Write] The threshold at which to perform a dynamics processing operation

<a id="unreal.SubmixEffectDynamicsProcessorSettings.__init__"></a>

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
    input_gain_db: float = 0.000000,
    threshold_db: float = 0.000000,
    ratio: float = 0.000000,
    knee_bandwidth_db: float = 0.000000,
    look_ahead_msec: float = 0.000000,
    attack_time_msec: float = 0.000000,
    release_time_msec: float = 0.000000,
    key_source: SubmixEffectDynamicsKeySource = SubmixEffectDynamicsKeySource.
    DEFAULT,
    external_audio_bus: AudioBus = None,
    external_submix: SoundSubmix = None,
    analog_mode: bool = False,
    bypass: bool = False,
    key_audition: bool = False,
    key_gain_db: float = 0.000000,
    output_gain_db: float = 0.000000,
    key_highshelf: SubmixEffectDynamicProcessorFilterSettings = [
        False, 20.000000, 0.000000
    ],
    key_lowshelf: SubmixEffectDynamicProcessorFilterSettings = [
        False, 20.000000, 0.000000
    ]
) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.dynamics_processor_type"></a>

#### dynamics_processor_type

```python
@property
def dynamics_processor_type() -> SubmixEffectDynamicsProcessorType
```

(SubmixEffectDynamicsProcessorType):  [Read-Write] Type of processor to apply

<a id="unreal.SubmixEffectDynamicsProcessorSettings.dynamics_processor_type"></a>

#### dynamics_processor_type

```python
@dynamics_processor_type.setter
def dynamics_processor_type(value: SubmixEffectDynamicsProcessorType) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.peak_mode"></a>

#### peak_mode

```python
@property
def peak_mode() -> SubmixEffectDynamicsPeakMode
```

(SubmixEffectDynamicsPeakMode):  [Read-Write] Mode of peak detection used on input key signal

<a id="unreal.SubmixEffectDynamicsProcessorSettings.peak_mode"></a>

#### peak_mode

```python
@peak_mode.setter
def peak_mode(value: SubmixEffectDynamicsPeakMode) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.link_mode"></a>

#### link_mode

```python
@property
def link_mode() -> SubmixEffectDynamicsChannelLinkMode
```

(SubmixEffectDynamicsChannelLinkMode):  [Read-Write] Mode of peak detection if key signal is multi-channel

<a id="unreal.SubmixEffectDynamicsProcessorSettings.link_mode"></a>

#### link_mode

```python
@link_mode.setter
def link_mode(value: SubmixEffectDynamicsChannelLinkMode) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.input_gain_db"></a>

#### input_gain_db

```python
@property
def input_gain_db() -> float
```

(float):  [Read-Write] The input gain of the dynamics processor

<a id="unreal.SubmixEffectDynamicsProcessorSettings.input_gain_db"></a>

#### input_gain_db

```python
@input_gain_db.setter
def input_gain_db(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.threshold_db"></a>

#### threshold_db

```python
@property
def threshold_db() -> float
```

(float):  [Read-Write] The threshold at which to perform a dynamics processing operation

<a id="unreal.SubmixEffectDynamicsProcessorSettings.threshold_db"></a>

#### threshold_db

```python
@threshold_db.setter
def threshold_db(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write] The dynamics processor ratio used for compression/expansion

<a id="unreal.SubmixEffectDynamicsProcessorSettings.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.knee_bandwidth_db"></a>

#### knee_bandwidth_db

```python
@property
def knee_bandwidth_db() -> float
```

(float):  [Read-Write] The knee bandwidth of the processor to use

<a id="unreal.SubmixEffectDynamicsProcessorSettings.knee_bandwidth_db"></a>

#### knee_bandwidth_db

```python
@knee_bandwidth_db.setter
def knee_bandwidth_db(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.look_ahead_msec"></a>

#### look_ahead_msec

```python
@property
def look_ahead_msec() -> float
```

(float):  [Read-Write] The amount of time to look ahead of the current audio (Allows for transients to be included in dynamics processing)

<a id="unreal.SubmixEffectDynamicsProcessorSettings.look_ahead_msec"></a>

#### look_ahead_msec

```python
@look_ahead_msec.setter
def look_ahead_msec(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.attack_time_msec"></a>

#### attack_time_msec

```python
@property
def attack_time_msec() -> float
```

(float):  [Read-Write] The amount of time to ramp into any dynamics processing effect

<a id="unreal.SubmixEffectDynamicsProcessorSettings.attack_time_msec"></a>

#### attack_time_msec

```python
@attack_time_msec.setter
def attack_time_msec(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.release_time_msec"></a>

#### release_time_msec

```python
@property
def release_time_msec() -> float
```

(float):  [Read-Write] The amount of time to release the dynamics processing effect

<a id="unreal.SubmixEffectDynamicsProcessorSettings.release_time_msec"></a>

#### release_time_msec

```python
@release_time_msec.setter
def release_time_msec(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_source"></a>

#### key_source

```python
@property
def key_source() -> SubmixEffectDynamicsKeySource
```

(SubmixEffectDynamicsKeySource):  [Read-Write]

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_source"></a>

#### key_source

```python
@key_source.setter
def key_source(value: SubmixEffectDynamicsKeySource) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.external_audio_bus"></a>

#### external_audio_bus

```python
@property
def external_audio_bus() -> AudioBus
```

(AudioBus):  [Read-Write] If set, uses output of provided audio bus as modulator of input signal for dynamics processor (Uses input signal as default modulator)

<a id="unreal.SubmixEffectDynamicsProcessorSettings.external_audio_bus"></a>

#### external_audio_bus

```python
@external_audio_bus.setter
def external_audio_bus(value: AudioBus) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.external_submix"></a>

#### external_submix

```python
@property
def external_submix() -> SoundSubmix
```

(SoundSubmix):  [Read-Write] If set, uses output of provided submix as modulator of input signal for dynamics processor (Uses input signal as default modulator)

<a id="unreal.SubmixEffectDynamicsProcessorSettings.external_submix"></a>

#### external_submix

```python
@external_submix.setter
def external_submix(value: SoundSubmix) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.analog_mode"></a>

#### analog_mode

```python
@property
def analog_mode() -> bool
```

(bool):  [Read-Write] Toggles treating the attack and release envelopes as analog-style vs digital-style (Analog will respond a bit more naturally/slower)

<a id="unreal.SubmixEffectDynamicsProcessorSettings.analog_mode"></a>

#### analog_mode

```python
@analog_mode.setter
def analog_mode(value: bool) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.bypass"></a>

#### bypass

```python
@property
def bypass() -> bool
```

(bool):  [Read-Write] Whether or not to bypass effect

<a id="unreal.SubmixEffectDynamicsProcessorSettings.bypass"></a>

#### bypass

```python
@bypass.setter
def bypass(value: bool) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_audition"></a>

#### key_audition

```python
@property
def key_audition() -> bool
```

(bool):  [Read-Write] Audition the key modulation signal, bypassing enveloping and processing the input signal.

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_audition"></a>

#### key_audition

```python
@key_audition.setter
def key_audition(value: bool) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_gain_db"></a>

#### key_gain_db

```python
@property
def key_gain_db() -> float
```

(float):  [Read-Write] Gain to apply to key signal if key source not set to default (input).

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_gain_db"></a>

#### key_gain_db

```python
@key_gain_db.setter
def key_gain_db(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.output_gain_db"></a>

#### output_gain_db

```python
@property
def output_gain_db() -> float
```

(float):  [Read-Write] The output gain of the dynamics processor

<a id="unreal.SubmixEffectDynamicsProcessorSettings.output_gain_db"></a>

#### output_gain_db

```python
@output_gain_db.setter
def output_gain_db(value: float) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_highshelf"></a>

#### key_highshelf

```python
@property
def key_highshelf() -> SubmixEffectDynamicProcessorFilterSettings
```

(SubmixEffectDynamicProcessorFilterSettings):  [Read-Write] High Shelf filter settings for key signal (external signal if supplied or input signal if not)

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_highshelf"></a>

#### key_highshelf

```python
@key_highshelf.setter
def key_highshelf(value: SubmixEffectDynamicProcessorFilterSettings) -> None
```

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_lowshelf"></a>

#### key_lowshelf

```python
@property
def key_lowshelf() -> SubmixEffectDynamicProcessorFilterSettings
```

(SubmixEffectDynamicProcessorFilterSettings):  [Read-Write] Low Shelf filter settings for key signal (external signal if supplied or input signal if not)

<a id="unreal.SubmixEffectDynamicsProcessorSettings.key_lowshelf"></a>

#### key_lowshelf

```python
@key_lowshelf.setter
def key_lowshelf(value: SubmixEffectDynamicProcessorFilterSettings) -> None
```

<a id="unreal.SubmixEffectEQBand"></a>