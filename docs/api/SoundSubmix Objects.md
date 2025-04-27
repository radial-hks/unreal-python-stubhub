## SoundSubmix Objects

```python
class SoundSubmix(SoundSubmixWithParentBase)
```

Sound Submix class meant for applying an effect to the downmixed sum of multiple audio sources.

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ambisonics_plugin_settings`` (SoundfieldEncodingSettingsBase):  [Read-Write] Optional settings used by plugins which support ambisonics file playback.
- ``audio_link_settings`` (AudioLinkSettingsAbstract):  [Read-Write] Optional Audio Link Settings Object
- ``auto_disable`` (bool):  [Read-Write] Auto-manage enabling and disabling the submix as a CPU optimization. It will be disabled if the submix and all child submixes are silent. It will re-enable if a sound is sent to the submix or a child submix is audible.
- ``auto_disable_time`` (float):  [Read-Write] The minimum amount of time to wait before automatically disabling a submix if it is silent. Will immediately re-enable if source audio is sent to it.
- ``child_submixes`` (Array[SoundSubmixBase]):  [Read-Only] Child submixes to this sound mix
- ``dry_level_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The dry level of the submix in Decibels. Applied before submix effects and analysis are performed.
- ``envelope_follower_attack_time`` (int32):  [Read-Write] The attack time in milliseconds for the envelope follower. Delegate callbacks can be registered to get the envelope value of sounds played with this submix.
- ``envelope_follower_release_time`` (int32):  [Read-Write] The release time in milliseconds for the envelope follower. Delegate callbacks can be registered to get the envelope value of sounds played with this submix.
- ``is_dynamic`` (bool):  [Read-Write] Is Submix Dynamic. (i.e. allows connect/disconnect at runtime.)  *
- ``mute_when_backgrounded`` (bool):  [Read-Write] Mute this submix when the application is muted or in the background. Used to prevent submix effect tails from continuing when tabbing out of application or if application is muted.
- ``on_submix_recorded_file_done`` (OnSubmixRecordedFileDone):  [Read-Write] Blueprint delegate for when a recorded file is finished exporting.
- ``output_volume_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The output volume of the submix in Decibels. Applied after submix effects and analysis are performed.
- ``parent_submix`` (SoundSubmixBase):  [Read-Only]
- ``send_to_audio_link`` (bool):  [Read-Write] Whether to send this Submix to AudioLink (when AudioLink is Enabled)
- ``submix_effect_chain`` (Array[SoundEffectSubmixPreset]):  [Read-Write]
- ``wet_level_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The wet level of the submixin Decibels. Applied after submix effects and analysis are performed.

<a id="unreal.SoundSubmix.mute_when_backgrounded"></a>

#### mute_when_backgrounded

```python
@property
def mute_when_backgrounded() -> bool
```

(bool):  [Read-Only] Mute this submix when the application is muted or in the background. Used to prevent submix effect tails from continuing when tabbing out of application or if application is muted.

<a id="unreal.SoundSubmix.submix_effect_chain"></a>

#### submix_effect_chain

```python
@property
def submix_effect_chain() -> Array[SoundEffectSubmixPreset]
```

(Array[SoundEffectSubmixPreset]):  [Read-Only]

<a id="unreal.SoundSubmix.ambisonics_plugin_settings"></a>

#### ambisonics_plugin_settings

```python
@property
def ambisonics_plugin_settings() -> SoundfieldEncodingSettingsBase
```

(SoundfieldEncodingSettingsBase):  [Read-Write] Optional settings used by plugins which support ambisonics file playback.

<a id="unreal.SoundSubmix.ambisonics_plugin_settings"></a>

#### ambisonics_plugin_settings

```python
@ambisonics_plugin_settings.setter
def ambisonics_plugin_settings(value: SoundfieldEncodingSettingsBase) -> None
```

<a id="unreal.SoundSubmix.envelope_follower_attack_time"></a>

#### envelope_follower_attack_time

```python
@property
def envelope_follower_attack_time() -> int
```

(int32):  [Read-Write] The attack time in milliseconds for the envelope follower. Delegate callbacks can be registered to get the envelope value of sounds played with this submix.

<a id="unreal.SoundSubmix.envelope_follower_attack_time"></a>

#### envelope_follower_attack_time

```python
@envelope_follower_attack_time.setter
def envelope_follower_attack_time(value: int) -> None
```

<a id="unreal.SoundSubmix.envelope_follower_release_time"></a>

#### envelope_follower_release_time

```python
@property
def envelope_follower_release_time() -> int
```

(int32):  [Read-Write] The release time in milliseconds for the envelope follower. Delegate callbacks can be registered to get the envelope value of sounds played with this submix.

<a id="unreal.SoundSubmix.envelope_follower_release_time"></a>

#### envelope_follower_release_time

```python
@envelope_follower_release_time.setter
def envelope_follower_release_time(value: int) -> None
```

<a id="unreal.SoundSubmix.output_volume_modulation"></a>

#### output_volume_modulation

```python
@property
def output_volume_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The output volume of the submix in Decibels. Applied after submix effects and analysis are performed.

<a id="unreal.SoundSubmix.output_volume_modulation"></a>

#### output_volume_modulation

```python
@output_volume_modulation.setter
def output_volume_modulation(
        value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SoundSubmix.wet_level_modulation"></a>

#### wet_level_modulation

```python
@property
def wet_level_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The wet level of the submixin Decibels. Applied after submix effects and analysis are performed.

<a id="unreal.SoundSubmix.wet_level_modulation"></a>

#### wet_level_modulation

```python
@wet_level_modulation.setter
def wet_level_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SoundSubmix.dry_level_modulation"></a>

#### dry_level_modulation

```python
@property
def dry_level_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The dry level of the submix in Decibels. Applied before submix effects and analysis are performed.

<a id="unreal.SoundSubmix.dry_level_modulation"></a>

#### dry_level_modulation

```python
@dry_level_modulation.setter
def dry_level_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SoundSubmix.send_to_audio_link"></a>

#### send_to_audio_link

```python
@property
def send_to_audio_link() -> bool
```

(bool):  [Read-Write] Whether to send this Submix to AudioLink (when AudioLink is Enabled)

<a id="unreal.SoundSubmix.send_to_audio_link"></a>

#### send_to_audio_link

```python
@send_to_audio_link.setter
def send_to_audio_link(value: bool) -> None
```

<a id="unreal.SoundSubmix.audio_link_settings"></a>

#### audio_link_settings

```python
@property
def audio_link_settings() -> AudioLinkSettingsAbstract
```

(AudioLinkSettingsAbstract):  [Read-Write] Optional Audio Link Settings Object

<a id="unreal.SoundSubmix.audio_link_settings"></a>

#### audio_link_settings

```python
@audio_link_settings.setter
def audio_link_settings(value: AudioLinkSettingsAbstract) -> None
```

<a id="unreal.SoundSubmix.on_submix_recorded_file_done"></a>

#### on_submix_recorded_file_done

```python
@property
def on_submix_recorded_file_done() -> OnSubmixRecordedFileDone
```

(OnSubmixRecordedFileDone):  [Read-Write] Blueprint delegate for when a recorded file is finished exporting.

<a id="unreal.SoundSubmix.on_submix_recorded_file_done"></a>

#### on_submix_recorded_file_done

```python
@on_submix_recorded_file_done.setter
def on_submix_recorded_file_done(value: OnSubmixRecordedFileDone) -> None
```

<a id="unreal.SoundSubmix.stop_spectral_analysis"></a>

#### stop_spectral_analysis

```python
def stop_spectral_analysis(world_context_object: Object) -> None
```

x.stop_spectral_analysis(world_context_object) -> None
Stop spectrum analysis of the audio output.

Args:
    world_context_object (Object):

<a id="unreal.SoundSubmix.stop_recording_output"></a>

#### stop_recording_output

```python
def stop_recording_output(
        world_context_object: Object,
        export_type: AudioRecordingExportType,
        name: str,
        path: str,
        existing_sound_wave_to_overwrite: SoundWave = None) -> None
```

x.stop_recording_output(world_context_object, export_type, name, path, existing_sound_wave_to_overwrite=None) -> None
Finish recording the audio from this submix and export it as a wav file or a USoundWave.

Args:
    world_context_object (Object): 
    export_type (AudioRecordingExportType): 
    name (str): 
    path (str): 
    existing_sound_wave_to_overwrite (SoundWave):

<a id="unreal.SoundSubmix.stop_envelope_following"></a>

#### stop_envelope_following

```python
def stop_envelope_following(world_context_object: Object) -> None
```

x.stop_envelope_following(world_context_object) -> None
Start envelope following the submix output. Register with OnSubmixEnvelope to receive envelope follower data in BP.

Args:
    world_context_object (Object):

<a id="unreal.SoundSubmix.start_spectral_analysis"></a>

#### start_spectral_analysis

```python
def start_spectral_analysis(
    world_context_object: Object,
    fft_size: FFTSize = FFTSize.DEFAULT_SIZE,
    interpolation_method:
    FFTPeakInterpolationMethod = FFTPeakInterpolationMethod.LINEAR,
    window_type: FFTWindowType = FFTWindowType.HANN,
    hop_size: float = 0.000000,
    spectrum_type: AudioSpectrumType = AudioSpectrumType.MAGNITUDE_SPECTRUM
) -> None
```

x.start_spectral_analysis(world_context_object, fft_size=FFTSize.DEFAULT_SIZE, interpolation_method=FFTPeakInterpolationMethod.LINEAR, window_type=FFTWindowType.HANN, hop_size=0.000000, spectrum_type=AudioSpectrumType.MAGNITUDE_SPECTRUM) -> None
Start spectrum analysis of the audio output.

Args:
    world_context_object (Object): 
    fft_size (FFTSize): 
    interpolation_method (FFTPeakInterpolationMethod): 
    window_type (FFTWindowType): 
    hop_size (float): 
    spectrum_type (AudioSpectrumType):

<a id="unreal.SoundSubmix.start_recording_output"></a>

#### start_recording_output

```python
def start_recording_output(world_context_object: Object,
                           expected_duration: float) -> None
```

x.start_recording_output(world_context_object, expected_duration) -> None
Start recording the audio from this submix.

Args:
    world_context_object (Object): 
    expected_duration (float):

<a id="unreal.SoundSubmix.start_envelope_following"></a>

#### start_envelope_following

```python
def start_envelope_following(world_context_object: Object) -> None
```

x.start_envelope_following(world_context_object) -> None
Start envelope following the submix output. Register with OnSubmixEnvelope to receive envelope follower data in BP.

Args:
    world_context_object (Object):

<a id="unreal.SoundSubmix.set_submix_wet_level"></a>

#### set_submix_wet_level

```python
def set_submix_wet_level(world_context_object: Object,
                         wet_level: float) -> None
```

x.set_submix_wet_level(world_context_object, wet_level) -> None
Sets the output volume of the submix in linear gain. This dynamic level acts as a multiplier on the WetLevel property of this submix.

Args:
    world_context_object (Object): 
    wet_level (float):

<a id="unreal.SoundSubmix.set_submix_output_volume"></a>

#### set_submix_output_volume

```python
def set_submix_output_volume(world_context_object: Object,
                             output_volume: float) -> None
```

x.set_submix_output_volume(world_context_object, output_volume) -> None
Sets the output volume of the submix in linear gain. This dynamic volume acts as a multiplier on the OutputVolume property of this submix.

Args:
    world_context_object (Object): 
    output_volume (float):

<a id="unreal.SoundSubmix.set_submix_dry_level"></a>

#### set_submix_dry_level

```python
def set_submix_dry_level(world_context_object: Object,
                         dry_level: float) -> None
```

x.set_submix_dry_level(world_context_object, dry_level) -> None
Sets the output volume of the submix in linear gain. This dynamic level acts as a multiplier on the DryLevel property of this submix.

Args:
    world_context_object (Object): 
    dry_level (float):

<a id="unreal.SoundSubmix.remove_spectral_analysis_delegate"></a>

#### remove_spectral_analysis_delegate

```python
def remove_spectral_analysis_delegate(
        world_context_object: Object,
        on_submix_spectral_analysis_bp: OnSubmixSpectralAnalysisBP) -> None
```

x.remove_spectral_analysis_delegate(world_context_object, on_submix_spectral_analysis_bp) -> None
Remove a spectral analysis delegate.

Args:
    world_context_object (Object): 
    on_submix_spectral_analysis_bp (OnSubmixSpectralAnalysisBP): The event delegate to remove.

<a id="unreal.SoundSubmix.remove_envelope_follower_delegate"></a>

#### remove_envelope_follower_delegate

```python
def remove_envelope_follower_delegate(
        world_context_object: Object,
        on_submix_envelope_bp: OnSubmixEnvelopeBP) -> None
```

x.remove_envelope_follower_delegate(world_context_object, on_submix_envelope_bp) -> None
Remove an envelope follower delegate.

Args:
    world_context_object (Object): 
    on_submix_envelope_bp (OnSubmixEnvelopeBP): The event delegate to remove.

<a id="unreal.SoundSubmix.add_spectral_analysis_delegate"></a>

#### add_spectral_analysis_delegate

```python
def add_spectral_analysis_delegate(
        world_context_object: Object,
        band_settings: Array[SoundSubmixSpectralAnalysisBandSettings],
        on_submix_spectral_analysis_bp: OnSubmixSpectralAnalysisBP,
        update_rate: float = 10.000000,
        decibel_noise_floor: float = -40.000000,
        do_normalize: bool = True,
        do_auto_range: bool = False,
        auto_range_attack_time: float = 0.100000,
        auto_range_release_time: float = 60.000000) -> None
```

x.add_spectral_analysis_delegate(world_context_object, band_settings, on_submix_spectral_analysis_bp, update_rate=10.000000, decibel_noise_floor=-40.000000, do_normalize=True, do_auto_range=False, auto_range_attack_time=0.100000, auto_range_release_time=60.000000) -> None
Adds a spectral analysis delegate to receive notifications when this submix has spectrum analysis enabled.

Args:
    world_context_object (Object): 
    band_settings (Array[SoundSubmixSpectralAnalysisBandSettings]): The frequency bands to analyze and their envelope-following settings.
    on_submix_spectral_analysis_bp (OnSubmixSpectralAnalysisBP): Event to fire when new spectral data is available.
    update_rate (float): How often to retrieve the data from the spectral analyzer and broadcast the event. Max is 30 times per second.
    decibel_noise_floor (float): Decibel Noise Floor to consider as silence when using a Decibel Spectrum Type.
    do_normalize (bool): If true, output band values will be normalized between zero and one.
    do_auto_range (bool): If true, output band values will have their ranges automatically adjusted to the minimum and maximum values in the audio. Output band values will be normalized between zero and one.
    auto_range_attack_time (float): The time (in seconds) it takes for the range to expand to 90% of a larger range.
    auto_range_release_time (float): The time (in seconds) it takes for the range to shrink to 90% of a smaller range.

<a id="unreal.SoundSubmix.add_envelope_follower_delegate"></a>

#### add_envelope_follower_delegate

```python
def add_envelope_follower_delegate(
        world_context_object: Object,
        on_submix_envelope_bp: OnSubmixEnvelopeBP) -> None
```

x.add_envelope_follower_delegate(world_context_object, on_submix_envelope_bp) -> None
Adds an envelope follower delegate to the submix when envelope following is enabled on this submix.

Args:
    world_context_object (Object): 
    on_submix_envelope_bp (OnSubmixEnvelopeBP): Event to fire when new envelope data is available.

<a id="unreal.SoundfieldSubmix"></a>