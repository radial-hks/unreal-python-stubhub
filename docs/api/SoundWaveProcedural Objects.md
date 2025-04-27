## SoundWaveProcedural Objects

```python
class SoundWaveProcedural(SoundWave)
```

Sound Wave Procedural

**C++ Source:**

- **Module**: Engine
- **File**: SoundWaveProcedural.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only]
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``attenuation_settings`` (SoundAttenuation):  [Read-Write] Attenuation settings package for the sound
- ``audio_properties_sheet`` (AudioPropertiesSheetAssetBase):  [Read-Write]
- ``bus_sends`` (Array[SoundSourceBusSendInfo]):  [Read-Write] This sound will send its audio output to this list of buses if there are bus instances playing after source effects are processed.
- ``bypass_volume_scale_for_priority`` (bool):  [Read-Write] Bypass volume weighting priority upon evaluating whether sound should remain active when max channel count is met (See platform Audio Settings).
- ``comment`` (str):  [Read-Write] Provides contextual information for the sound to the translator.
- ``compression_quality`` (int32):  [Read-Write] Platform agnostic compression quality. 1..100 with 1 being best compression and 100 being best quality. ADPCM and PCM sound asset compression types ignore this parameter.
- ``concurrency_overrides`` (SoundConcurrencySettings):  [Read-Write] If Override Concurrency is true, concurrency settings to use.
- ``concurrency_set`` (Set[SoundConcurrency]):  [Read-Write] Set of concurrency settings to observe (if override is set to false).  Sound must pass all concurrency settings to play.
- ``cue_points`` (Array[SoundWaveCuePoint]):  [Read-Only] Cue point data parsed fro the .wav file. Contains "Loop Regions" as cue points as well!
- ``curves`` (CurveTable):  [Read-Write] Curves associated with this sound wave
- ``debug`` (bool):  [Read-Write] When "au.3dVisualize.Attenuation" has been specified, draw this sound's attenuation shape when the sound is audible. For debugging purposes only.
- ``duration`` (float):  [Read-Only] Duration of sound in seconds.
- ``enable_amplitude_envelope_analysis`` (bool):  [Read-Write] Whether or not to enable cook-time amplitude envelope analysis.
- ``enable_baked_fft_analysis`` (bool):  [Read-Write] Whether or not to enable cook-time baked FFT analysis.
- ``enable_base_submix`` (bool):  [Read-Write] If enabled, sound will route to the Master Submix by default or to the Base Submix if defined. If disabled, sound will route ONLY to the Submix Sends and/or Bus Sends
- ``enable_bus_sends`` (bool):  [Read-Write] Whether or not to enable sending this audio's output to buses.
- ``enable_cloud_streaming`` (bool):  [Read-Write] If enabled, this wave may be streamed from the cloud using the Opus format. Loading behavior must NOT be `Force Inline`. Requires a suitable support plugin to be installed.
- ``enable_submix_sends`` (bool):  [Read-Write] Whether or not to enable Submix Sends other than the Base Submix.
- ``envelope_follower_attack_time`` (int32):  [Read-Write] The attack time in milliseconds. Describes how quickly the envelope analyzer responds to increasing amplitudes.
- ``envelope_follower_frame_size`` (int32):  [Read-Write] How many audio frames to average a new envelope value. Larger values use less memory for audio envelope data but will result in lower envelope accuracy.
- ``envelope_follower_release_time`` (int32):  [Read-Write] The release time in milliseconds. Describes how quickly the envelope analyzer responds to decreasing amplitudes.
- ``fft_analysis_attack_time`` (int32):  [Read-Write] Attack time in milliseconds of the spectral envelope follower.
- ``fft_analysis_frame_size`` (int32):  [Read-Write] How many audio frames analyze at a time.
- ``fft_analysis_release_time`` (int32):  [Read-Write] Release time in milliseconds of the spectral envelope follower.
- ``fft_size`` (SoundWaveFFTSize):  [Read-Write] The FFT window size to use for fft analysis.
- ``frequencies_to_analyze`` (Array[float]):  [Read-Write] The frequencies (in hz) to analyze when doing baked FFT analysis.
- ``imported_sample_rate`` (int32):  [Read-Only] Sample rate of the imported sound wave.
- ``initial_chunk_size`` (int32):  [Read-Write] Please use size of First Chunk in Seconds.
  deprecated: Property 'InitialChunkSize' is deprecated.
- ``is_ambisonics`` (bool):  [Read-Write] Whether or not this source is ambisonics file format. If set, sound always uses the
  'Master Ambisonics Submix' as set in the 'Audio' category of Project Settings'
  and ignores submix if provided locally or in the referenced SoundClass.
- ``loading_behavior`` (SoundWaveLoadingBehavior):  [Read-Write] Specifies how and when compressed audio data is loaded for asset if stream caching is enabled.
- ``looping`` (bool):  [Read-Write] If set, when played directly (not through a sound cue) the wave will be played looping.
- ``manual_word_wrap`` (bool):  [Read-Write] If set to true will disable automatic generation of line breaks - use if the subtitles have been split manually.
- ``mature`` (bool):  [Read-Write] If set to true if this sound is considered to contain mature/adult content.
- ``max_distance`` (float):  [Read-Only] The MaxDistance property is calculated statically on load or at asset edit time, but is not reliable at runtime.
  the GetMaxDistance function should be used to determine the applied max distance based on runtime behavior.
- ``modulation_settings`` (SoundModulationDefaultRoutingSettings):  [Read-Write] Modulation Settings
- ``num_channels`` (int32):  [Read-Only] Number of channels of multichannel data; 1 or 2 for regular mono and stereo files
- ``override_concurrency`` (bool):  [Read-Write] Whether or not to override the sound concurrency object with local concurrency settings.
- ``override_sound_to_use_for_analysis`` (SoundWave):  [Read-Write] Specify a sound to use for the baked analysis. Will default to this USoundWave if not set.
- ``pitch`` (float):  [Read-Write] Playback pitch for sound.
- ``platform_settings`` (Map[Guid, SoundWaveCloudStreamingPlatformSettings]):  [Read-Write] Optionally disables cloud streaming per platform
- ``pre_effect_bus_sends`` (Array[SoundSourceBusSendInfo]):  [Read-Write] This sound will send its audio output to this list of buses if there are bus instances playing before source effects are processed.
- ``priority`` (float):  [Read-Write] Used to determine whether sound can play or remain active if channel limit is met, where higher value is higher priority
  (see platform's Audio Settings 'Max Channels' property). Unless bypassed, value is weighted with the final volume of the
  sound to produce final runtime priority value.
- ``sample_rate`` (int32):  [Read-Only] Cooked sample rate of the asset. Can be modified by sample rate override.
- ``sample_rate_quality`` (SoundwaveSampleRateSettings):  [Read-Write] Determines the max sample rate to use if the platform enables "Resampling For Device" in project settings.
       For example, if the platform enables Resampling For Device and specifies 32000 for High, then setting High here will
       force the sound wave to be _at most_ 32000. Does nothing if Resampling For Device is disabled.
- ``seekable_streaming`` (bool):  [Read-Write] Deprecated compression type properties
  deprecated: 5.0 - Property is deprecated. bSeekableStreaming now means ADPCM codec in SoundAssetCompressionType.
- ``single_line`` (bool):  [Read-Write] If set to true the subtitles display as a sequence of single lines as opposed to multiline.
- ``size_of_first_audio_chunk_in_seconds`` (PerPlatformFloat):  [Read-Write] How much audio to add to First Audio Chunk (in seconds)
- ``sound_asset_compression_type`` (SoundAssetCompressionType):  [Read-Write] The compression type to use for the sound wave asset.
- ``sound_class_object`` (SoundClass):  [Read-Write] Sound class this sound belongs to
- ``sound_group`` (SoundGroup):  [Read-Write]
- ``sound_submix_object`` (SoundSubmixBase):  [Read-Write] Submix to route sound output to. If unset, falls back to referenced SoundClass submix.
  If SoundClass submix is unset, sends to the 'Master Submix' as set in the 'Audio' category of Project Settings'.
- ``sound_submix_sends`` (Array[SoundSubmixSendInfo]):  [Read-Write] Array of submix sends to which a prescribed amount (see 'Send Level') of this sound is sent.
- ``source_effect_chain`` (SoundEffectSourcePresetChain):  [Read-Write] The source effect chain to use for this sound.
- ``spoken_text`` (str):  [Read-Write] A localized version of the text that is actually spoken phonetically in the audio.
  deprecated: Use Subtitles instead.
- ``streaming_priority`` (int32):  [Read-Write]
  deprecated: 5.0 - Property is deprecated. Streaming priority has no effect with stream caching enabled.
- ``subtitle_priority`` (float):  [Read-Write] The priority of the subtitle.
- ``subtitles`` (Array[SubtitleCue]):  [Read-Write] Subtitle cues.
- ``timecode_info`` (SoundWaveTimecodeInfo):  [Read-Only] Information about the time-code from import, if available.
- ``total_samples`` (float):  [Read-Only] Total number of samples (in the thousands). Useful as a metric to analyze the relative size of a given sound asset in content browser.
- ``transformations`` (Array[WaveformTransformationBase]):  [Read-Write] Waveform edits to be applied to this SoundWave on cook (editing transformations will trigger a cook)
- ``treat_file_as_looping_for_analysis`` (bool):  [Read-Write] Whether or not we should treat the sound wave used for analysis (this or the override) as looping while performing analysis.
  A looping sound may include the end of the file for inclusion in analysis for envelope and FFT analysis.
- ``use_bink_audio`` (bool):  [Read-Write]
  deprecated: 5.0 - Property is deprecated. bUseBinkAudio now means Bink codec in SoundAssetCompressionType.
- ``virtualization_mode`` (VirtualizationMode):  [Read-Write] Virtualization behavior, determining if a sound may revive and how it continues playing when culled or evicted (limited to looping sounds).
- ``volume`` (float):  [Read-Write] Playback volume of sound 0 to 1 - Default is 1.0.

<a id="unreal.SynthSound"></a>