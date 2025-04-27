## SoundBase Objects

```python
class SoundBase(Object)
```

The base class for a playable sound object

**C++ Source:**

- **Module**: Engine
- **File**: SoundBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
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
- ``max_distance`` (float):  [Read-Only] The MaxDistance property is calculated statically on load or at asset edit time, but is not reliable at runtime.
  the GetMaxDistance function should be used to determine the applied max distance based on runtime behavior.
- ``override_concurrency`` (bool):  [Read-Write] Whether or not to override the sound concurrency object with local concurrency settings.
- ``pre_effect_bus_sends`` (Array[SoundSourceBusSendInfo]):  [Read-Write] This sound will send its audio output to this list of buses if there are bus instances playing before source effects are processed.
- ``priority`` (float):  [Read-Write] Used to determine whether sound can play or remain active if channel limit is met, where higher value is higher priority
  (see platform's Audio Settings 'Max Channels' property). Unless bypassed, value is weighted with the final volume of the
  sound to produce final runtime priority value.
- ``sound_class_object`` (SoundClass):  [Read-Write] Sound class this sound belongs to
- ``sound_submix_object`` (SoundSubmixBase):  [Read-Write] Submix to route sound output to. If unset, falls back to referenced SoundClass submix.
  If SoundClass submix is unset, sends to the 'Master Submix' as set in the 'Audio' category of Project Settings'.
- ``sound_submix_sends`` (Array[SoundSubmixSendInfo]):  [Read-Write] Array of submix sends to which a prescribed amount (see 'Send Level') of this sound is sent.
- ``source_effect_chain`` (SoundEffectSourcePresetChain):  [Read-Write] The source effect chain to use for this sound.
- ``total_samples`` (float):  [Read-Only] Total number of samples (in the thousands). Useful as a metric to analyze the relative size of a given sound asset in content browser.
- ``virtualization_mode`` (VirtualizationMode):  [Read-Write] Virtualization behavior, determining if a sound may revive and how it continues playing when culled or evicted (limited to looping sounds).

<a id="unreal.SoundBase.sound_class_object"></a>

#### sound_class_object

```python
@property
def sound_class_object() -> SoundClass
```

(SoundClass):  [Read-Only] Sound class this sound belongs to

<a id="unreal.SoundBase.override_concurrency"></a>

#### override_concurrency

```python
@property
def override_concurrency() -> bool
```

(bool):  [Read-Write] Whether or not to override the sound concurrency object with local concurrency settings.

<a id="unreal.SoundBase.override_concurrency"></a>

#### override_concurrency

```python
@override_concurrency.setter
def override_concurrency(value: bool) -> None
```

<a id="unreal.SoundBase.enable_bus_sends"></a>

#### enable_bus_sends

```python
@property
def enable_bus_sends() -> bool
```

(bool):  [Read-Write] Whether or not to enable sending this audio's output to buses.

<a id="unreal.SoundBase.enable_bus_sends"></a>

#### enable_bus_sends

```python
@enable_bus_sends.setter
def enable_bus_sends(value: bool) -> None
```

<a id="unreal.SoundBase.bypass_volume_scale_for_priority"></a>

#### bypass_volume_scale_for_priority

```python
@property
def bypass_volume_scale_for_priority() -> bool
```

(bool):  [Read-Write] Bypass volume weighting priority upon evaluating whether sound should remain active when max channel count is met (See platform Audio Settings).

<a id="unreal.SoundBase.bypass_volume_scale_for_priority"></a>

#### bypass_volume_scale_for_priority

```python
@bypass_volume_scale_for_priority.setter
def bypass_volume_scale_for_priority(value: bool) -> None
```

<a id="unreal.SoundBase.virtualization_mode"></a>

#### virtualization_mode

```python
@property
def virtualization_mode() -> VirtualizationMode
```

(VirtualizationMode):  [Read-Write] Virtualization behavior, determining if a sound may revive and how it continues playing when culled or evicted (limited to looping sounds).

<a id="unreal.SoundBase.virtualization_mode"></a>

#### virtualization_mode

```python
@virtualization_mode.setter
def virtualization_mode(value: VirtualizationMode) -> None
```

<a id="unreal.SoundBase.concurrency_set"></a>

#### concurrency_set

```python
@property
def concurrency_set() -> Set[SoundConcurrency]
```

(Set[SoundConcurrency]):  [Read-Write] Set of concurrency settings to observe (if override is set to false).  Sound must pass all concurrency settings to play.

<a id="unreal.SoundBase.concurrency_set"></a>

#### concurrency_set

```python
@concurrency_set.setter
def concurrency_set(value: Set[SoundConcurrency]) -> None
```

<a id="unreal.SoundBase.concurrency_overrides"></a>

#### concurrency_overrides

```python
@property
def concurrency_overrides() -> SoundConcurrencySettings
```

(SoundConcurrencySettings):  [Read-Write] If Override Concurrency is true, concurrency settings to use.

<a id="unreal.SoundBase.concurrency_overrides"></a>

#### concurrency_overrides

```python
@concurrency_overrides.setter
def concurrency_overrides(value: SoundConcurrencySettings) -> None
```

<a id="unreal.SoundBase.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Only] Duration of sound in seconds.

<a id="unreal.SoundBase.max_distance"></a>

#### max_distance

```python
@property
def max_distance() -> float
```

(float):  [Read-Only] The MaxDistance property is calculated statically on load or at asset edit time, but is not reliable at runtime.
the GetMaxDistance function should be used to determine the applied max distance based on runtime behavior.

<a id="unreal.SoundBase.total_samples"></a>

#### total_samples

```python
@property
def total_samples() -> float
```

(float):  [Read-Only] Total number of samples (in the thousands). Useful as a metric to analyze the relative size of a given sound asset in content browser.

<a id="unreal.SoundBase.priority"></a>

#### priority

```python
@property
def priority() -> float
```

(float):  [Read-Write] Used to determine whether sound can play or remain active if channel limit is met, where higher value is higher priority
(see platform's Audio Settings 'Max Channels' property). Unless bypassed, value is weighted with the final volume of the
sound to produce final runtime priority value.

<a id="unreal.SoundBase.priority"></a>

#### priority

```python
@priority.setter
def priority(value: float) -> None
```

<a id="unreal.SoundBase.sound_submix_object"></a>

#### sound_submix_object

```python
@property
def sound_submix_object() -> SoundSubmixBase
```

(SoundSubmixBase):  [Read-Write] Submix to route sound output to. If unset, falls back to referenced SoundClass submix.
If SoundClass submix is unset, sends to the 'Master Submix' as set in the 'Audio' category of Project Settings'.

<a id="unreal.SoundBase.sound_submix_object"></a>

#### sound_submix_object

```python
@sound_submix_object.setter
def sound_submix_object(value: SoundSubmixBase) -> None
```

<a id="unreal.SoundBase.sound_submix_sends"></a>

#### sound_submix_sends

```python
@property
def sound_submix_sends() -> Array[SoundSubmixSendInfo]
```

(Array[SoundSubmixSendInfo]):  [Read-Write] Array of submix sends to which a prescribed amount (see 'Send Level') of this sound is sent.

<a id="unreal.SoundBase.sound_submix_sends"></a>

#### sound_submix_sends

```python
@sound_submix_sends.setter
def sound_submix_sends(value: Array[SoundSubmixSendInfo]) -> None
```

<a id="unreal.SoundBase.source_effect_chain"></a>

#### source_effect_chain

```python
@property
def source_effect_chain() -> SoundEffectSourcePresetChain
```

(SoundEffectSourcePresetChain):  [Read-Write] The source effect chain to use for this sound.

<a id="unreal.SoundBase.source_effect_chain"></a>

#### source_effect_chain

```python
@source_effect_chain.setter
def source_effect_chain(value: SoundEffectSourcePresetChain) -> None
```

<a id="unreal.SoundBase.bus_sends"></a>

#### bus_sends

```python
@property
def bus_sends() -> Array[SoundSourceBusSendInfo]
```

(Array[SoundSourceBusSendInfo]):  [Read-Write] This sound will send its audio output to this list of buses if there are bus instances playing after source effects are processed.

<a id="unreal.SoundBase.bus_sends"></a>

#### bus_sends

```python
@bus_sends.setter
def bus_sends(value: Array[SoundSourceBusSendInfo]) -> None
```

<a id="unreal.SoundBase.pre_effect_bus_sends"></a>

#### pre_effect_bus_sends

```python
@property
def pre_effect_bus_sends() -> Array[SoundSourceBusSendInfo]
```

(Array[SoundSourceBusSendInfo]):  [Read-Write] This sound will send its audio output to this list of buses if there are bus instances playing before source effects are processed.

<a id="unreal.SoundBase.pre_effect_bus_sends"></a>

#### pre_effect_bus_sends

```python
@pre_effect_bus_sends.setter
def pre_effect_bus_sends(value: Array[SoundSourceBusSendInfo]) -> None
```

<a id="unreal.SoundBase.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.SoundBase.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.SoundBase.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.SoundWave"></a>