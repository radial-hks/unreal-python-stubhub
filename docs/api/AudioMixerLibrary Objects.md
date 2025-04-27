## AudioMixerLibrary Objects

```python
class AudioMixerLibrary(BlueprintFunctionLibrary)
```

Audio Mixer Blueprint Library

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerBlueprintLibrary.h

<a id="unreal.AudioMixerLibrary.unregister_audio_bus_from_submix"></a>

#### unregister_audio_bus_from_submix

```python
@classmethod
def unregister_audio_bus_from_submix(cls, world_context_object: Object,
                                     sound_submix: SoundSubmix,
                                     audio_bus: AudioBus) -> None
```

X.unregister_audio_bus_from_submix(world_context_object, sound_submix, audio_bus) -> None
Unregisters an audio bus that could have been registered to a submix.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    audio_bus (AudioBus):

<a id="unreal.AudioMixerLibrary.trim_audio_cache"></a>

#### trim_audio_cache

```python
@classmethod
def trim_audio_cache(cls, megabytes_to_free: float) -> float
```

X.trim_audio_cache(megabytes_to_free) -> float
Trim memory used by the audio cache. Returns the number of megabytes freed.

Args:
    megabytes_to_free (float): 

Returns:
    float:

<a id="unreal.AudioMixerLibrary.swap_audio_output_device"></a>

#### swap_audio_output_device

```python
@classmethod
def swap_audio_output_device(
        cls, world_context_object: Object, new_device_id: str,
        on_completed_device_swap: OnCompletedDeviceSwap) -> None
```

X.swap_audio_output_device(world_context_object, new_device_id, on_completed_device_swap) -> None
Hotswaps to the requested audio output device

Args:
    world_context_object (Object): 
    new_device_id (str): the device Id to swap to
    on_completed_device_swap (OnCompletedDeviceSwap): the event to fire when the audio endpoint devices have been retrieved

<a id="unreal.AudioMixerLibrary.stop_recording_output"></a>

#### stop_recording_output

```python
@classmethod
def stop_recording_output(
        cls,
        world_context_object: Object,
        export_type: AudioRecordingExportType,
        name: str,
        path: str,
        submix_to_record: SoundSubmix = None,
        existing_sound_wave_to_overwrite: SoundWave = None) -> SoundWave
```

X.stop_recording_output(world_context_object, export_type, name, path, submix_to_record=None, existing_sound_wave_to_overwrite=None) -> SoundWave
Stop recording audio. Path can be absolute, or relative (to the /Saved/BouncedWavFiles folder). By leaving the Submix To Record field blank, you can record the master output of the game.

Args:
    world_context_object (Object): 
    export_type (AudioRecordingExportType): 
    name (str): 
    path (str): 
    submix_to_record (SoundSubmix): 
    existing_sound_wave_to_overwrite (SoundWave): 

Returns:
    SoundWave:

<a id="unreal.AudioMixerLibrary.stop_audio_bus"></a>

#### stop_audio_bus

```python
@classmethod
def stop_audio_bus(cls, world_context_object: Object,
                   audio_bus: AudioBus) -> None
```

X.stop_audio_bus(world_context_object, audio_bus) -> None
Stops the given audio bus.

Args:
    world_context_object (Object): 
    audio_bus (AudioBus):

<a id="unreal.AudioMixerLibrary.stop_analyzing_output"></a>

#### stop_analyzing_output

```python
@classmethod
def stop_analyzing_output(
        cls,
        world_context_object: Object,
        submix_to_stop_analyzing: SoundSubmix = None) -> None
```

X.stop_analyzing_output(world_context_object, submix_to_stop_analyzing=None) -> None
Stop spectrum analysis.

Args:
    world_context_object (Object): 
    submix_to_stop_analyzing (SoundSubmix):

<a id="unreal.AudioMixerLibrary.start_recording_output"></a>

#### start_recording_output

```python
@classmethod
def start_recording_output(cls,
                           world_context_object: Object,
                           expected_duration: float,
                           submix_to_record: SoundSubmix = None) -> None
```

X.start_recording_output(world_context_object, expected_duration, submix_to_record=None) -> None
Start recording audio. By leaving the Submix To Record field blank, you can record the master output of the game.

Args:
    world_context_object (Object): 
    expected_duration (float): 
    submix_to_record (SoundSubmix):

<a id="unreal.AudioMixerLibrary.start_audio_bus"></a>

#### start_audio_bus

```python
@classmethod
def start_audio_bus(cls, world_context_object: Object,
                    audio_bus: AudioBus) -> None
```

X.start_audio_bus(world_context_object, audio_bus) -> None
Starts the given audio bus.

Args:
    world_context_object (Object): 
    audio_bus (AudioBus):

<a id="unreal.AudioMixerLibrary.start_analyzing_output"></a>

#### start_analyzing_output

```python
@classmethod
def start_analyzing_output(
    cls,
    world_context_object: Object,
    submix_to_analyze: SoundSubmix = None,
    fft_size: FFTSize = FFTSize.DEFAULT_SIZE,
    interpolation_method:
    FFTPeakInterpolationMethod = FFTPeakInterpolationMethod.LINEAR,
    window_type: FFTWindowType = FFTWindowType.HANN,
    hop_size: float = 0.000000,
    spectrum_type: AudioSpectrumType = AudioSpectrumType.MAGNITUDE_SPECTRUM
) -> None
```

X.start_analyzing_output(world_context_object, submix_to_analyze=None, fft_size=FFTSize.DEFAULT_SIZE, interpolation_method=FFTPeakInterpolationMethod.LINEAR, window_type=FFTWindowType.HANN, hop_size=0.000000, spectrum_type=AudioSpectrumType.MAGNITUDE_SPECTRUM) -> None
Start spectrum analysis of the audio output. By leaving the Submix To Analyze blank, you can analyze the master output of the game.

Args:
    world_context_object (Object): 
    submix_to_analyze (SoundSubmix): 
    fft_size (FFTSize): 
    interpolation_method (FFTPeakInterpolationMethod): 
    window_type (FFTWindowType): 
    hop_size (float): 
    spectrum_type (AudioSpectrumType):

<a id="unreal.AudioMixerLibrary.set_submix_effect_chain_override"></a>

#### set_submix_effect_chain_override

```python
@classmethod
def set_submix_effect_chain_override(
        cls, world_context_object: Object, sound_submix: SoundSubmix,
        submix_effect_preset_chain: Array[SoundEffectSubmixPreset],
        fade_time_sec: float) -> None
```

X.set_submix_effect_chain_override(world_context_object, sound_submix, submix_effect_preset_chain, fade_time_sec) -> None
Sets a submix effect chain override on the given submix. The effect chain will cross fade from the base effect chain or current override to the new override.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    submix_effect_preset_chain (Array[SoundEffectSubmixPreset]): 
    fade_time_sec (float):

<a id="unreal.AudioMixerLibrary.set_bypass_source_effect_chain_entry"></a>

#### set_bypass_source_effect_chain_entry

```python
@classmethod
def set_bypass_source_effect_chain_entry(
        cls, world_context_object: Object,
        preset_chain: SoundEffectSourcePresetChain, entry_index: int,
        bypassed: bool) -> None
```

X.set_bypass_source_effect_chain_entry(world_context_object, preset_chain, entry_index, bypassed) -> None
Set whether or not to bypass the effect at the source effect chain index.

Args:
    world_context_object (Object): 
    preset_chain (SoundEffectSourcePresetChain): 
    entry_index (int32): 
    bypassed (bool):

<a id="unreal.AudioMixerLibrary.resume_recording_output"></a>

#### resume_recording_output

```python
@classmethod
def resume_recording_output(cls,
                            world_context_object: Object,
                            submix_to_pause: SoundSubmix = None) -> None
```

X.resume_recording_output(world_context_object, submix_to_pause=None) -> None
Resume recording audio after pausing. By leaving the Submix To Pause field blank, you can record the master output of the game.

Args:
    world_context_object (Object): 
    submix_to_pause (SoundSubmix):

<a id="unreal.AudioMixerLibrary.replace_submix_effect"></a>

#### replace_submix_effect

```python
@classmethod
def replace_submix_effect(
        cls, world_context_object: Object, sound_submix: SoundSubmix,
        submix_chain_index: int,
        submix_effect_preset: SoundEffectSubmixPreset) -> None
```

X.replace_submix_effect(world_context_object, sound_submix, submix_chain_index, submix_effect_preset) -> None
Replaces the submix effect at the given submix chain index, adds the effect if there is none at that index.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    submix_chain_index (int32): 
    submix_effect_preset (SoundEffectSubmixPreset):

<a id="unreal.AudioMixerLibrary.replace_sound_effect_submix"></a>

#### replace_sound_effect_submix

```python
@classmethod
def replace_sound_effect_submix(
        cls, world_context_object: Object, sound_submix: SoundSubmix,
        submix_chain_index: int,
        submix_effect_preset: SoundEffectSubmixPreset) -> None
```

X.replace_sound_effect_submix(world_context_object, sound_submix, submix_chain_index, submix_effect_preset) -> None
Replace Sound Effect Submix
deprecated: Function 'ReplaceSoundEffectSubmix' is deprecated.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    submix_chain_index (int32): 
    submix_effect_preset (SoundEffectSubmixPreset):

<a id="unreal.AudioMixerLibrary.remove_submix_effect_preset_at_index"></a>

#### remove_submix_effect_preset_at_index

```python
@classmethod
def remove_submix_effect_preset_at_index(cls, world_context_object: Object,
                                         sound_submix: SoundSubmix,
                                         submix_chain_index: int) -> None
```

X.remove_submix_effect_preset_at_index(world_context_object, sound_submix, submix_chain_index) -> None
Remove Submix Effect Preset at Index
deprecated: Function 'RemoveSubmixEffectPresetAtIndex' is deprecated.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    submix_chain_index (int32):

<a id="unreal.AudioMixerLibrary.remove_submix_effect_preset"></a>

#### remove_submix_effect_preset

```python
@classmethod
def remove_submix_effect_preset(
        cls, world_context_object: Object, sound_submix: SoundSubmix,
        submix_effect_preset: SoundEffectSubmixPreset) -> None
```

X.remove_submix_effect_preset(world_context_object, sound_submix, submix_effect_preset) -> None
Remove Submix Effect Preset
deprecated: Function 'RemoveSubmixEffectPreset' is deprecated.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    submix_effect_preset (SoundEffectSubmixPreset):

<a id="unreal.AudioMixerLibrary.remove_submix_effect_at_index"></a>

#### remove_submix_effect_at_index

```python
@classmethod
def remove_submix_effect_at_index(cls, world_context_object: Object,
                                  sound_submix: SoundSubmix,
                                  submix_chain_index: int) -> None
```

X.remove_submix_effect_at_index(world_context_object, sound_submix, submix_chain_index) -> None
Removes the submix effect at the given submix chain index, if there is a submix effect at that index.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    submix_chain_index (int32):

<a id="unreal.AudioMixerLibrary.remove_submix_effect"></a>

#### remove_submix_effect

```python
@classmethod
def remove_submix_effect(
        cls, world_context_object: Object, sound_submix: SoundSubmix,
        submix_effect_preset: SoundEffectSubmixPreset) -> None
```

X.remove_submix_effect(world_context_object, sound_submix, submix_effect_preset) -> None
Removes all instances of a submix effect preset from the given submix.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    submix_effect_preset (SoundEffectSubmixPreset):

<a id="unreal.AudioMixerLibrary.remove_source_effect_from_preset_chain"></a>

#### remove_source_effect_from_preset_chain

```python
@classmethod
def remove_source_effect_from_preset_chain(
        cls, world_context_object: Object,
        preset_chain: SoundEffectSourcePresetChain, entry_index: int) -> None
```

X.remove_source_effect_from_preset_chain(world_context_object, preset_chain, entry_index) -> None
Removes source effect entry from preset chain. Only affects the instance of preset chain.

Args:
    world_context_object (Object): 
    preset_chain (SoundEffectSourcePresetChain): 
    entry_index (int32):

<a id="unreal.AudioMixerLibrary.remove_master_submix_effect"></a>

#### remove_master_submix_effect

```python
@classmethod
def remove_master_submix_effect(
        cls, world_context_object: Object,
        submix_effect_preset: SoundEffectSubmixPreset) -> None
```

X.remove_master_submix_effect(world_context_object, submix_effect_preset) -> None
Removes a submix effect preset from the master submix.

Args:
    world_context_object (Object): 
    submix_effect_preset (SoundEffectSubmixPreset):

<a id="unreal.AudioMixerLibrary.register_audio_bus_to_submix"></a>

#### register_audio_bus_to_submix

```python
@classmethod
def register_audio_bus_to_submix(cls, world_context_object: Object,
                                 sound_submix: SoundSubmix,
                                 audio_bus: AudioBus) -> None
```

X.register_audio_bus_to_submix(world_context_object, sound_submix, audio_bus) -> None
Registers an audio bus to a submix so the submix output can be routed to the audiobus.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    audio_bus (AudioBus):

<a id="unreal.AudioMixerLibrary.prime_sound_for_playback"></a>

#### prime_sound_for_playback

```python
@classmethod
def prime_sound_for_playback(cls, sound_wave: SoundWave,
                             on_load_completion: OnSoundLoadComplete) -> None
```

X.prime_sound_for_playback(sound_wave, on_load_completion) -> None
Begin loading a sound into the cache so that it can be played immediately.

Args:
    sound_wave (SoundWave): 
    on_load_completion (OnSoundLoadComplete):

<a id="unreal.AudioMixerLibrary.prime_sound_cue_for_playback"></a>

#### prime_sound_cue_for_playback

```python
@classmethod
def prime_sound_cue_for_playback(cls, sound_cue: SoundCue) -> None
```

X.prime_sound_cue_for_playback(sound_cue) -> None
Begin loading any sounds referenced by a sound cue into the cache so that it can be played immediately.

Args:
    sound_cue (SoundCue):

<a id="unreal.AudioMixerLibrary.pause_recording_output"></a>

#### pause_recording_output

```python
@classmethod
def pause_recording_output(cls,
                           world_context_object: Object,
                           submix_to_pause: SoundSubmix = None) -> None
```

X.pause_recording_output(world_context_object, submix_to_pause=None) -> None
Pause recording audio, without finalizing the recording to disk. By leaving the Submix To Record field blank, you can record the master output of the game.

Args:
    world_context_object (Object): 
    submix_to_pause (SoundSubmix):

<a id="unreal.AudioMixerLibrary.make_preset_spectral_analysis_band_settings"></a>

#### make_preset_spectral_analysis_band_settings

```python
@classmethod
def make_preset_spectral_analysis_band_settings(
    cls,
    band_preset_type: AudioSpectrumBandPresetType,
    num_bands: int = 10,
    attack_time_msec: int = 10,
    release_time_msec: int = 10
) -> Array[SoundSubmixSpectralAnalysisBandSettings]
```

X.make_preset_spectral_analysis_band_settings(band_preset_type, num_bands=10, attack_time_msec=10, release_time_msec=10) -> Array[SoundSubmixSpectralAnalysisBandSettings]
Make an array of bands which span the frequency range of a given EAudioSpectrumBandPresetType.

Args:
    band_preset_type (AudioSpectrumBandPresetType): The type audio content which the bands encompass.
    num_bands (int32): The number of bands used to represent the spectrum.
    attack_time_msec (int32): The attack time (in milliseconds) to apply to each band's envelope tracker.
    release_time_msec (int32): The release time (in milliseconds) to apply to each band's envelope tracker.

Returns:
    Array[SoundSubmixSpectralAnalysisBandSettings]:

<a id="unreal.AudioMixerLibrary.make_musical_spectral_analysis_band_settings"></a>

#### make_musical_spectral_analysis_band_settings

```python
@classmethod
def make_musical_spectral_analysis_band_settings(
    cls,
    num_semitones: int = 60,
    starting_musical_note: MusicalNoteName = MusicalNoteName.C,
    starting_octave: int = 2,
    attack_time_msec: int = 10,
    release_time_msec: int = 10
) -> Array[SoundSubmixSpectralAnalysisBandSettings]
```

X.make_musical_spectral_analysis_band_settings(num_semitones=60, starting_musical_note=MusicalNoteName.C, starting_octave=2, attack_time_msec=10, release_time_msec=10) -> Array[SoundSubmixSpectralAnalysisBandSettings]
Make an array of musically spaced bands with ascending frequency.

Args:
    num_semitones (int32): The number of semitones to represent.
    starting_musical_note (MusicalNoteName): 
    starting_octave (int32): The octave of the first note in the array.
    attack_time_msec (int32): The attack time (in milliseconds) to apply to each band's envelope tracker.
    release_time_msec (int32): The release time (in milliseconds) to apply to each band's envelope tracker.

Returns:
    Array[SoundSubmixSpectralAnalysisBandSettings]:

<a id="unreal.AudioMixerLibrary.make_full_spectrum_spectral_analysis_band_settings"></a>

#### make_full_spectrum_spectral_analysis_band_settings

```python
@classmethod
def make_full_spectrum_spectral_analysis_band_settings(
    cls,
    num_bands: int = 30,
    minimum_frequency: float = 40.000000,
    maximum_frequency: float = 16000.000000,
    attack_time_msec: int = 10,
    release_time_msec: int = 10
) -> Array[SoundSubmixSpectralAnalysisBandSettings]
```

X.make_full_spectrum_spectral_analysis_band_settings(num_bands=30, minimum_frequency=40.000000, maximum_frequency=16000.000000, attack_time_msec=10, release_time_msec=10) -> Array[SoundSubmixSpectralAnalysisBandSettings]
Make an array of logarithmically spaced bands.

Args:
    num_bands (int32): The number of bands to used to represent the spectrum.
    minimum_frequency (float): The center frequency of the first band.
    maximum_frequency (float): The center frequency of the last band.
    attack_time_msec (int32): The attack time (in milliseconds) to apply to each band's envelope tracker.
    release_time_msec (int32): The release time (in milliseconds) to apply to each band's envelope tracker.

Returns:
    Array[SoundSubmixSpectralAnalysisBandSettings]:

<a id="unreal.AudioMixerLibrary.is_audio_bus_active"></a>

#### is_audio_bus_active

```python
@classmethod
def is_audio_bus_active(cls, world_context_object: Object,
                        audio_bus: AudioBus) -> bool
```

X.is_audio_bus_active(world_context_object, audio_bus) -> bool
Queries if the given audio bus is active (and audio can be mixed to it).

Args:
    world_context_object (Object): 
    audio_bus (AudioBus): 

Returns:
    bool:

<a id="unreal.AudioMixerLibrary.get_phase_for_frequencies"></a>

#### get_phase_for_frequencies

```python
@classmethod
def get_phase_for_frequencies(
        cls,
        world_context_object: Object,
        frequencies: Array[float],
        submix_to_analyze: SoundSubmix = None) -> Array[float]
```

X.get_phase_for_frequencies(world_context_object, frequencies, submix_to_analyze=None) -> Array[float]
Retrieve the phases for the given frequencies.

Args:
    world_context_object (Object): 
    frequencies (Array[float]): 
    submix_to_analyze (SoundSubmix): 

Returns:
    Array[float]: 

    phases (Array[float]):

<a id="unreal.AudioMixerLibrary.get_number_of_entries_in_source_effect_chain"></a>

#### get_number_of_entries_in_source_effect_chain

```python
@classmethod
def get_number_of_entries_in_source_effect_chain(
        cls, world_context_object: Object,
        preset_chain: SoundEffectSourcePresetChain) -> int
```

X.get_number_of_entries_in_source_effect_chain(world_context_object, preset_chain) -> int32
Returns the number of effect chain entries in the given source effect chain.

Args:
    world_context_object (Object): 
    preset_chain (SoundEffectSourcePresetChain): 

Returns:
    int32:

<a id="unreal.AudioMixerLibrary.get_magnitude_for_frequencies"></a>

#### get_magnitude_for_frequencies

```python
@classmethod
def get_magnitude_for_frequencies(
        cls,
        world_context_object: Object,
        frequencies: Array[float],
        submix_to_analyze: SoundSubmix = None) -> Array[float]
```

X.get_magnitude_for_frequencies(world_context_object, frequencies, submix_to_analyze=None) -> Array[float]
Retrieve the magnitudes for the given frequencies.

Args:
    world_context_object (Object): 
    frequencies (Array[float]): 
    submix_to_analyze (SoundSubmix): 

Returns:
    Array[float]: 

    magnitudes (Array[float]):

<a id="unreal.AudioMixerLibrary.get_current_audio_output_device_name"></a>

#### get_current_audio_output_device_name

```python
@classmethod
def get_current_audio_output_device_name(
        cls, world_context_object: Object,
        on_obtain_current_device_event: OnMainAudioOutputDeviceObtained
) -> None
```

X.get_current_audio_output_device_name(world_context_object, on_obtain_current_device_event) -> None
Gets information about the currently used audio output device

Args:
    world_context_object (Object): 
    on_obtain_current_device_event (OnMainAudioOutputDeviceObtained): the event to fire when the audio endpoint devices have been retrieved

<a id="unreal.AudioMixerLibrary.get_available_audio_output_devices"></a>

#### get_available_audio_output_devices

```python
@classmethod
def get_available_audio_output_devices(
        cls, world_context_object: Object,
        on_obtain_devices_event: OnAudioOutputDevicesObtained) -> None
```

X.get_available_audio_output_devices(world_context_object, on_obtain_devices_event) -> None
Gets information about all audio output devices available in the system

Args:
    world_context_object (Object): 
    on_obtain_devices_event (OnAudioOutputDevicesObtained): the event to fire when the audio endpoint devices have been retrieved

<a id="unreal.AudioMixerLibrary.conv_audio_output_device_info_to_string"></a>

#### conv_audio_output_device_info_to_string

```python
@classmethod
def conv_audio_output_device_info_to_string(
        cls, info: AudioOutputDeviceInfo) -> str
```

X.conv_audio_output_device_info_to_string(info) -> str
Returns the device info in a human readable format

Args:
    info (AudioOutputDeviceInfo): The audio device data to print

Returns:
    str: The data in a string format

<a id="unreal.AudioMixerLibrary.clear_submix_effects"></a>

#### clear_submix_effects

```python
@classmethod
def clear_submix_effects(cls, world_context_object: Object,
                         sound_submix: SoundSubmix) -> None
```

X.clear_submix_effects(world_context_object, sound_submix) -> None
Clears all submix effects on the given submix.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix):

<a id="unreal.AudioMixerLibrary.clear_submix_effect_chain_override"></a>

#### clear_submix_effect_chain_override

```python
@classmethod
def clear_submix_effect_chain_override(cls, world_context_object: Object,
                                       sound_submix: SoundSubmix,
                                       fade_time_sec: float) -> None
```

X.clear_submix_effect_chain_override(world_context_object, sound_submix, fade_time_sec) -> None
Clears all submix effect overrides on the given submix and returns it to the default effect chain.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    fade_time_sec (float):

<a id="unreal.AudioMixerLibrary.clear_master_submix_effects"></a>

#### clear_master_submix_effects

```python
@classmethod
def clear_master_submix_effects(cls, world_context_object: Object) -> None
```

X.clear_master_submix_effects(world_context_object) -> None
Clears all master submix effects.

Args:
    world_context_object (Object):

<a id="unreal.AudioMixerLibrary.add_submix_effect"></a>

#### add_submix_effect

```python
@classmethod
def add_submix_effect(cls, world_context_object: Object,
                      sound_submix: SoundSubmix,
                      submix_effect_preset: SoundEffectSubmixPreset) -> int
```

X.add_submix_effect(world_context_object, sound_submix, submix_effect_preset) -> int32
Adds a submix effect preset to the given submix at the end of its submix effect chain. Returns the number of submix effects.

Args:
    world_context_object (Object): 
    sound_submix (SoundSubmix): 
    submix_effect_preset (SoundEffectSubmixPreset): 

Returns:
    int32:

<a id="unreal.AudioMixerLibrary.add_source_effect_to_preset_chain"></a>

#### add_source_effect_to_preset_chain

```python
@classmethod
def add_source_effect_to_preset_chain(
        cls, world_context_object: Object,
        preset_chain: SoundEffectSourcePresetChain,
        entry: SourceEffectChainEntry) -> None
```

X.add_source_effect_to_preset_chain(world_context_object, preset_chain, entry) -> None
Adds source effect entry to preset chain. Only effects the instance of the preset chain

Args:
    world_context_object (Object): 
    preset_chain (SoundEffectSourcePresetChain): 
    entry (SourceEffectChainEntry):

<a id="unreal.AudioMixerLibrary.add_master_submix_effect"></a>

#### add_master_submix_effect

```python
@classmethod
def add_master_submix_effect(
        cls, world_context_object: Object,
        submix_effect_preset: SoundEffectSubmixPreset) -> None
```

X.add_master_submix_effect(world_context_object, submix_effect_preset) -> None
Adds a submix effect preset to the master submix.

Args:
    world_context_object (Object): 
    submix_effect_preset (SoundEffectSubmixPreset):

<a id="unreal.SoundBase"></a>