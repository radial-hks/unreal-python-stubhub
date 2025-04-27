## SoundClassProperties Objects

```python
class SoundClassProperties(StructBase)
```

Sound Class Properties

**C++ Source:**

- **Module**: Engine
- **File**: SoundClass.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``always_play`` (bool):  [Read-Write] Whether to inflate referencing sound's priority to always play.
- ``apply_ambient_volumes`` (bool):  [Read-Write] Whether the Interior/Exterior volume and LPF modifiers should be applied
- ``apply_effects`` (bool):  [Read-Write] Whether to use 'Master EQ Submix' as set in the 'Audio' category of Project Settings as the default submix for referencing sounds.
- ``attenuation_distance_scale`` (float):  [Read-Write] Scales the distance measurement used by the audio engine when determining distance-based attenuation.
  E.g., a sound 1000 units away with an AttenuationDistanceScale of .5 will be attenuated
  as if it is 500 units away from the listener.
  Allows adjusting attenuation settings dynamically.
- ``center_channel_only`` (bool):  [Read-Write] Whether or not this sound class forces sounds to the center channel
- ``default2d_reverb_send_amount`` (float):  [Read-Write] Send amount to master reverb effect for referencing unattenuated (2D) sounds.
- ``default_submix`` (SoundSubmix):  [Read-Write] Default output submix of referencing sounds. If unset, falls back to the 'Master Submix' as set in the 'Audio' category of Project Settings.
  (Unavailable if legacy 'Output to Master EQ Submix' is set)
- ``is_music`` (bool):  [Read-Write] Whether or not this is music (propagates to child classes only if parent is true)
- ``is_ui_sound`` (bool):  [Read-Write] Whether or not this sound plays when the game is paused in the UI
- ``lfe_bleed`` (float):  [Read-Write] The amount of a sound to bleed to the LFE channel
- ``loading_behavior`` (SoundWaveLoadingBehavior):  [Read-Write] Specifies how and when compressed audio data is loaded for asset if stream caching is enabled.
- ``low_pass_filter_frequency`` (float):  [Read-Write] Lowpass filter cutoff frequency
- ``modulation_settings`` (SoundModulationDefaultSettings):  [Read-Write] Default modulation settings for sounds directly referencing this class
- ``output_target`` (AudioOutputTarget):  [Read-Write] Which output target the sound should be played through
- ``pitch`` (float):  [Read-Write] Pitch multiplier.
- ``radio_filter_volume`` (float):  [Read-Write] Volume of the radio filter effect.
- ``radio_filter_volume_threshold`` (float):  [Read-Write] Volume at which the radio filter kicks in
- ``reverb`` (bool):  [Read-Write] Whether or not sounds referencing this class send to the reverb submix
- ``size_of_first_audio_chunk_in_seconds`` (PerPlatformFloat):  [Read-Write] How much audio to add to First Audio Chunk (in seconds)
- ``voice_center_channel_volume`` (float):  [Read-Write] The amount to send to center channel (does not propagate to child classes)
- ``volume`` (float):  [Read-Write] Volume multiplier.

<a id="unreal.SoundClassProperties.__init__"></a>

#### __init__

```python
def __init__(
        volume: float = 0.000000,
        pitch: float = 0.000000,
        low_pass_filter_frequency: float = 0.000000,
        attenuation_distance_scale: float = 0.000000,
        lfe_bleed: float = 0.000000,
        voice_center_channel_volume: float = 0.000000,
        radio_filter_volume: float = 0.000000,
        radio_filter_volume_threshold: float = 0.000000,
        apply_effects: bool = False,
        always_play: bool = False,
        is_ui_sound: bool = False,
        is_music: bool = False,
        center_channel_only: bool = False,
        apply_ambient_volumes: bool = False,
        reverb: bool = False,
        default2d_reverb_send_amount: float = 0.000000,
        modulation_settings: SoundModulationDefaultSettings = [[
            0.000000, []
        ], [0.000000, []], [20.000000, []], [20000.000000, []]],
        output_target: AudioOutputTarget = AudioOutputTarget.SPEAKER,
        loading_behavior: SoundWaveLoadingBehavior = SoundWaveLoadingBehavior.
    INHERITED,
        default_submix: SoundSubmix = None) -> None
```

<a id="unreal.SoundClassProperties.volume"></a>

#### volume

```python
@property
def volume() -> float
```

(float):  [Read-Only] Volume multiplier.

<a id="unreal.SoundClassProperties.pitch"></a>

#### pitch

```python
@property
def pitch() -> float
```

(float):  [Read-Only] Pitch multiplier.

<a id="unreal.SoundClassProperties.low_pass_filter_frequency"></a>

#### low_pass_filter_frequency

```python
@property
def low_pass_filter_frequency() -> float
```

(float):  [Read-Only] Lowpass filter cutoff frequency

<a id="unreal.SoundClassProperties.attenuation_distance_scale"></a>

#### attenuation_distance_scale

```python
@property
def attenuation_distance_scale() -> float
```

(float):  [Read-Only] Scales the distance measurement used by the audio engine when determining distance-based attenuation.
E.g., a sound 1000 units away with an AttenuationDistanceScale of .5 will be attenuated
as if it is 500 units away from the listener.
Allows adjusting attenuation settings dynamically.

<a id="unreal.SoundClassProperties.lfe_bleed"></a>

#### lfe_bleed

```python
@property
def lfe_bleed() -> float
```

(float):  [Read-Only] The amount of a sound to bleed to the LFE channel

<a id="unreal.SoundClassProperties.voice_center_channel_volume"></a>

#### voice_center_channel_volume

```python
@property
def voice_center_channel_volume() -> float
```

(float):  [Read-Only] The amount to send to center channel (does not propagate to child classes)

<a id="unreal.SoundClassProperties.radio_filter_volume"></a>

#### radio_filter_volume

```python
@property
def radio_filter_volume() -> float
```

(float):  [Read-Only] Volume of the radio filter effect.

<a id="unreal.SoundClassProperties.radio_filter_volume_threshold"></a>

#### radio_filter_volume_threshold

```python
@property
def radio_filter_volume_threshold() -> float
```

(float):  [Read-Only] Volume at which the radio filter kicks in

<a id="unreal.SoundClassProperties.apply_effects"></a>

#### apply_effects

```python
@property
def apply_effects() -> bool
```

(bool):  [Read-Only] Whether to use 'Master EQ Submix' as set in the 'Audio' category of Project Settings as the default submix for referencing sounds.

<a id="unreal.SoundClassProperties.always_play"></a>

#### always_play

```python
@property
def always_play() -> bool
```

(bool):  [Read-Only] Whether to inflate referencing sound's priority to always play.

<a id="unreal.SoundClassProperties.is_ui_sound"></a>

#### is_ui_sound

```python
@property
def is_ui_sound() -> bool
```

(bool):  [Read-Only] Whether or not this sound plays when the game is paused in the UI

<a id="unreal.SoundClassProperties.is_music"></a>

#### is_music

```python
@property
def is_music() -> bool
```

(bool):  [Read-Only] Whether or not this is music (propagates to child classes only if parent is true)

<a id="unreal.SoundClassProperties.center_channel_only"></a>

#### center_channel_only

```python
@property
def center_channel_only() -> bool
```

(bool):  [Read-Only] Whether or not this sound class forces sounds to the center channel

<a id="unreal.SoundClassProperties.apply_ambient_volumes"></a>

#### apply_ambient_volumes

```python
@property
def apply_ambient_volumes() -> bool
```

(bool):  [Read-Only] Whether the Interior/Exterior volume and LPF modifiers should be applied

<a id="unreal.SoundClassProperties.reverb"></a>

#### reverb

```python
@property
def reverb() -> bool
```

(bool):  [Read-Only] Whether or not sounds referencing this class send to the reverb submix

<a id="unreal.SoundClassProperties.default2d_reverb_send_amount"></a>

#### default2d_reverb_send_amount

```python
@property
def default2d_reverb_send_amount() -> float
```

(float):  [Read-Only] Send amount to master reverb effect for referencing unattenuated (2D) sounds.

<a id="unreal.SoundClassProperties.modulation_settings"></a>

#### modulation_settings

```python
@property
def modulation_settings() -> SoundModulationDefaultSettings
```

(SoundModulationDefaultSettings):  [Read-Only] Default modulation settings for sounds directly referencing this class

<a id="unreal.SoundClassProperties.output_target"></a>

#### output_target

```python
@property
def output_target() -> AudioOutputTarget
```

(AudioOutputTarget):  [Read-Only] Which output target the sound should be played through

<a id="unreal.SoundClassProperties.loading_behavior"></a>

#### loading_behavior

```python
@property
def loading_behavior() -> SoundWaveLoadingBehavior
```

(SoundWaveLoadingBehavior):  [Read-Only] Specifies how and when compressed audio data is loaded for asset if stream caching is enabled.

<a id="unreal.SoundClassProperties.default_submix"></a>

#### default_submix

```python
@property
def default_submix() -> SoundSubmix
```

(SoundSubmix):  [Read-Only] Default output submix of referencing sounds. If unset, falls back to the 'Master Submix' as set in the 'Audio' category of Project Settings.
(Unavailable if legacy 'Output to Master EQ Submix' is set)

<a id="unreal.SoundModulationDefaultSettings"></a>