## PropertyAnimatorSoundWave Objects

```python
class PropertyAnimatorSoundWave(PropertyAnimatorNumericBase)
```

Applies a sampled sound wave movement with various options on supported float properties

**C++ Source:**

- **Plugin**: PropertyAnimator
- **Module**: PropertyAnimator
- **File**: PropertyAnimatorSoundWave.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_time_source`` (PropertyAnimatorCoreTimeSourceBase):  [Read-Only] Active time source with its options, determined by its name
- ``animator_display_name`` (Name):  [Read-Only] Display name as title property for component array, hide it but must be visible to editor for array title property
- ``animator_enabled`` (bool):  [Read-Write] Enable control of properties linked to this Animator
- ``cycle_duration`` (float):  [Read-Write] Duration of one cycle for the effect = period of the effect
- ``cycle_gap_duration`` (float):  [Read-Write] Time gap between each cycle
- ``cycle_mode`` (PropertyAnimatorCycleMode):  [Read-Write] Cycle mode for the effect
- ``linked_properties`` (Array[PropertyAnimatorCoreContext]):  [Read-Write] Context for properties linked to this Animator
- ``loop`` (bool):  [Read-Write] Whether we keep looping after the duration has been reached or before 0
- ``magnitude`` (float):  [Read-Write] Magnitude for the effect on all properties
- ``override_time_source`` (bool):  [Read-Write] Use the global time source or override it on this animator
- ``random_time_offset`` (bool):  [Read-Write] Use random time offset to add variation in animation
- ``sampled_sound_wave`` (SoundWave):  [Read-Write] The sound wave to analyse
  Cannot be switched at runtime, only in editor due to analyzer
  Analyzed audio will work at runtime since it is cached
- ``seed`` (int32):  [Read-Write] Seed to generate per property time offset
- ``time_source_name`` (Name):  [Read-Write] The time source to use
- ``time_sources_instances`` (Map[Name, PropertyAnimatorCoreTimeSourceBase]):  [Read-Write]
  deprecated: Use TimeSources instead

<a id="unreal.PropertyAnimatorSoundWave.sampled_sound_wave"></a>

#### sampled_sound_wave

```python
@property
def sampled_sound_wave() -> SoundWave
```

(SoundWave):  [Read-Only] The sound wave to analyse
Cannot be switched at runtime, only in editor due to analyzer
Analyzed audio will work at runtime since it is cached

<a id="unreal.PropertyAnimatorSoundWave.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Write] Whether we keep looping after the duration has been reached or before 0

<a id="unreal.PropertyAnimatorSoundWave.loop"></a>

#### loop

```python
@loop.setter
def loop(value: bool) -> None
```

<a id="unreal.PropertyAnimatorVectorContext"></a>