## SoundCue Objects

```python
class SoundCue(SoundBase)
```

The behavior of audio playback is defined within Sound Cues.

**C++ Source:**

- **Module**: Engine
- **File**: SoundCue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``attenuation_overrides`` (SoundAttenuationSettings):  [Read-Write] Attenuation settings to use if Override Attenuation is set to true
- ``attenuation_settings`` (SoundAttenuation):  [Read-Write] Attenuation settings package for the sound
- ``audio_properties_sheet`` (AudioPropertiesSheetAssetBase):  [Read-Write]
- ``bus_sends`` (Array[SoundSourceBusSendInfo]):  [Read-Write] This sound will send its audio output to this list of buses if there are bus instances playing after source effects are processed.
- ``bypass_volume_scale_for_priority`` (bool):  [Read-Write] Bypass volume weighting priority upon evaluating whether sound should remain active when max channel count is met (See platform Audio Settings).
- ``concurrency_overrides`` (SoundConcurrencySettings):  [Read-Write] If Override Concurrency is true, concurrency settings to use.
- ``concurrency_set`` (Set[SoundConcurrency]):  [Read-Write] Set of concurrency settings to observe (if override is set to false).  Sound must pass all concurrency settings to play.
- ``debug`` (bool):  [Read-Write] When "au.3dVisualize.Attenuation" has been specified, draw this sound's attenuation shape when the sound is audible. For debugging purposes only.
- ``duration`` (float):  [Read-Only] Duration of sound in seconds.
- ``enable_base_submix`` (bool):  [Read-Write] If enabled, sound will route to the Master Submix by default or to the Base Submix if defined. If disabled, sound will route ONLY to the Submix Sends and/or Bus Sends
- ``enable_bus_sends`` (bool):  [Read-Write] Whether or not to enable sending this audio's output to buses.
- ``enable_submix_sends`` (bool):  [Read-Write] Whether or not to enable Submix Sends other than the Base Submix.
- ``exclude_from_random_node_branch_culling`` (bool):  [Read-Write] Ignore per-platform random node culling for memory purposes
- ``first_node`` (SoundNode):  [Read-Write]
- ``max_distance`` (float):  [Read-Only] The MaxDistance property is calculated statically on load or at asset edit time, but is not reliable at runtime.
  the GetMaxDistance function should be used to determine the applied max distance based on runtime behavior.
- ``override_attenuation`` (bool):  [Read-Write] Indicates whether attenuation should use the Attenuation Overrides or the Attenuation Settings asset
- ``override_concurrency`` (bool):  [Read-Write] Whether or not to override the sound concurrency object with local concurrency settings.
- ``pitch_multiplier`` (float):  [Read-Write] Base pitch multiplier
- ``pre_effect_bus_sends`` (Array[SoundSourceBusSendInfo]):  [Read-Write] This sound will send its audio output to this list of buses if there are bus instances playing before source effects are processed.
- ``prime_on_load`` (bool):  [Read-Write] Makes this sound cue automatically load any sound waves it can play into the cache when it is loaded.
- ``priority`` (float):  [Read-Write] Used to determine whether sound can play or remain active if channel limit is met, where higher value is higher priority
  (see platform's Audio Settings 'Max Channels' property). Unless bypassed, value is weighted with the final volume of the
  sound to produce final runtime priority value.
- ``sound_class_object`` (SoundClass):  [Read-Write] Sound class this sound belongs to
- ``sound_submix_object`` (SoundSubmixBase):  [Read-Write] Submix to route sound output to. If unset, falls back to referenced SoundClass submix.
  If SoundClass submix is unset, sends to the 'Master Submix' as set in the 'Audio' category of Project Settings'.
- ``sound_submix_sends`` (Array[SoundSubmixSendInfo]):  [Read-Write] Array of submix sends to which a prescribed amount (see 'Send Level') of this sound is sent.
- ``source_effect_chain`` (SoundEffectSourcePresetChain):  [Read-Write] The source effect chain to use for this sound.
- ``subtitle_priority`` (float):  [Read-Write] The priority of the subtitle.  Defaults to 10000.  Higher values will play instead of lower values.
- ``total_samples`` (float):  [Read-Only] Total number of samples (in the thousands). Useful as a metric to analyze the relative size of a given sound asset in content browser.
- ``virtualization_mode`` (VirtualizationMode):  [Read-Write] Virtualization behavior, determining if a sound may revive and how it continues playing when culled or evicted (limited to looping sounds).
- ``volume_multiplier`` (float):  [Read-Write] Base volume multiplier

<a id="unreal.SoundCue.first_node"></a>

#### first_node

```python
@property
def first_node() -> SoundNode
```

(SoundNode):  [Read-Only]

<a id="unreal.SoundCue.volume_multiplier"></a>

#### volume_multiplier

```python
@property
def volume_multiplier() -> float
```

(float):  [Read-Only] Base volume multiplier

<a id="unreal.SoundCue.pitch_multiplier"></a>

#### pitch_multiplier

```python
@property
def pitch_multiplier() -> float
```

(float):  [Read-Only] Base pitch multiplier

<a id="unreal.SoundMix"></a>