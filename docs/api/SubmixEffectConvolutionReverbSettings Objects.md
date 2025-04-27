## SubmixEffectConvolutionReverbSettings Objects

```python
class SubmixEffectConvolutionReverbSettings(StructBase)
```

Submix Effect Convolution Reverb Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectConvolutionReverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_hardware_acceleration`` (bool):  [Read-Write]
  deprecated: Property 'AllowHardwareAcceleration' is deprecated.
- ``bypass`` (bool):  [Read-Write] If true, input audio is directly routed to output audio with applying any effect.
- ``dry_volume_db`` (float):  [Read-Write] Controls how much of the dry signal is mixed into the output, in Decibels
- ``impulse_response`` (AudioImpulseResponse):  [Read-Write]
  deprecated: Property 'ImpulseResponse' is deprecated.
- ``invert_rear_channel_bleed_phase`` (bool):  [Read-Write] If true, rear channel bleed sends will have their phase inverted.
- ``mix_input_channel_format_to_impulse_response_format`` (bool):  [Read-Write] If true, the submix input audio is downmixed to match the IR asset audio channel
         * format. If false, the input audio's channels are matched to the IR assets
         * audio channels.
- ``mix_reverb_output_to_output_channel_format`` (bool):  [Read-Write] If true, the reverberated audio is upmixed or downmixed to match the submix
         * output audio format. If false, the reverberated audio's channels are matched
         * to the submixs output audio channels.
- ``surround_rear_channel_bleed_amount`` (float):  [Read-Write]
  deprecated: Property 'SurroundRearChannelBleedAmount' is deprecated.
- ``surround_rear_channel_bleed_db`` (float):  [Read-Write] Amount of audio to be sent to rear channels in quad/surround configurations
- ``surround_rear_channel_flip`` (bool):  [Read-Write] If true, send Surround Rear Channel Bleed Amount sends front left to back right and vice versa
- ``wet_volume_db`` (float):  [Read-Write] Controls how much of the wet signal is mixed into the output, in Decibels

<a id="unreal.SubmixEffectConvolutionReverbSettings.__init__"></a>

#### __init__

```python
def __init__(wet_volume_db: float = 0.000000,
             dry_volume_db: float = 0.000000,
             bypass: bool = False,
             mix_input_channel_format_to_impulse_response_format: bool = False,
             mix_reverb_output_to_output_channel_format: bool = False,
             surround_rear_channel_bleed_db: float = 0.000000,
             invert_rear_channel_bleed_phase: bool = False,
             surround_rear_channel_flip: bool = False) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.wet_volume_db"></a>

#### wet_volume_db

```python
@property
def wet_volume_db() -> float
```

(float):  [Read-Write] Controls how much of the wet signal is mixed into the output, in Decibels

<a id="unreal.SubmixEffectConvolutionReverbSettings.wet_volume_db"></a>

#### wet_volume_db

```python
@wet_volume_db.setter
def wet_volume_db(value: float) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.dry_volume_db"></a>

#### dry_volume_db

```python
@property
def dry_volume_db() -> float
```

(float):  [Read-Write] Controls how much of the dry signal is mixed into the output, in Decibels

<a id="unreal.SubmixEffectConvolutionReverbSettings.dry_volume_db"></a>

#### dry_volume_db

```python
@dry_volume_db.setter
def dry_volume_db(value: float) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.bypass"></a>

#### bypass

```python
@property
def bypass() -> bool
```

(bool):  [Read-Write] If true, input audio is directly routed to output audio with applying any effect.

<a id="unreal.SubmixEffectConvolutionReverbSettings.bypass"></a>

#### bypass

```python
@bypass.setter
def bypass(value: bool) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.mix_input_channel_format_to_impulse_response_format"></a>

#### mix_input_channel_format_to_impulse_response_format

```python
@property
def mix_input_channel_format_to_impulse_response_format() -> bool
```

(bool):  [Read-Write] If true, the submix input audio is downmixed to match the IR asset audio channel
       * format. If false, the input audio's channels are matched to the IR assets
       * audio channels.

<a id="unreal.SubmixEffectConvolutionReverbSettings.mix_input_channel_format_to_impulse_response_format"></a>

#### mix_input_channel_format_to_impulse_response_format

```python
@mix_input_channel_format_to_impulse_response_format.setter
def mix_input_channel_format_to_impulse_response_format(value: bool) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.mix_reverb_output_to_output_channel_format"></a>

#### mix_reverb_output_to_output_channel_format

```python
@property
def mix_reverb_output_to_output_channel_format() -> bool
```

(bool):  [Read-Write] If true, the reverberated audio is upmixed or downmixed to match the submix
       * output audio format. If false, the reverberated audio's channels are matched
       * to the submixs output audio channels.

<a id="unreal.SubmixEffectConvolutionReverbSettings.mix_reverb_output_to_output_channel_format"></a>

#### mix_reverb_output_to_output_channel_format

```python
@mix_reverb_output_to_output_channel_format.setter
def mix_reverb_output_to_output_channel_format(value: bool) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_bleed_db"></a>

#### surround_rear_channel_bleed_db

```python
@property
def surround_rear_channel_bleed_db() -> float
```

(float):  [Read-Write] Amount of audio to be sent to rear channels in quad/surround configurations

<a id="unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_bleed_db"></a>

#### surround_rear_channel_bleed_db

```python
@surround_rear_channel_bleed_db.setter
def surround_rear_channel_bleed_db(value: float) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.invert_rear_channel_bleed_phase"></a>

#### invert_rear_channel_bleed_phase

```python
@property
def invert_rear_channel_bleed_phase() -> bool
```

(bool):  [Read-Write] If true, rear channel bleed sends will have their phase inverted.

<a id="unreal.SubmixEffectConvolutionReverbSettings.invert_rear_channel_bleed_phase"></a>

#### invert_rear_channel_bleed_phase

```python
@invert_rear_channel_bleed_phase.setter
def invert_rear_channel_bleed_phase(value: bool) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_flip"></a>

#### surround_rear_channel_flip

```python
@property
def surround_rear_channel_flip() -> bool
```

(bool):  [Read-Write] If true, send Surround Rear Channel Bleed Amount sends front left to back right and vice versa

<a id="unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_flip"></a>

#### surround_rear_channel_flip

```python
@surround_rear_channel_flip.setter
def surround_rear_channel_flip(value: bool) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_bleed_amount"></a>

#### surround_rear_channel_bleed_amount

```python
@property
def surround_rear_channel_bleed_amount() -> float
```

(float):  [Read-Write]
deprecated: Property 'SurroundRearChannelBleedAmount' is deprecated.

<a id="unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_bleed_amount"></a>

#### surround_rear_channel_bleed_amount

```python
@surround_rear_channel_bleed_amount.setter
def surround_rear_channel_bleed_amount(value: float) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.impulse_response"></a>

#### impulse_response

```python
@property
def impulse_response() -> AudioImpulseResponse
```

(AudioImpulseResponse):  [Read-Write]
deprecated: Property 'ImpulseResponse' is deprecated.

<a id="unreal.SubmixEffectConvolutionReverbSettings.impulse_response"></a>

#### impulse_response

```python
@impulse_response.setter
def impulse_response(value: AudioImpulseResponse) -> None
```

<a id="unreal.SubmixEffectConvolutionReverbSettings.allow_hardware_acceleration"></a>

#### allow_hardware_acceleration

```python
@property
def allow_hardware_acceleration() -> bool
```

(bool):  [Read-Write]
deprecated: Property 'AllowHardwareAcceleration' is deprecated.

<a id="unreal.SubmixEffectConvolutionReverbSettings.allow_hardware_acceleration"></a>

#### allow_hardware_acceleration

```python
@allow_hardware_acceleration.setter
def allow_hardware_acceleration(value: bool) -> None
```

<a id="unreal.SubmixEffectDelaySettings"></a>