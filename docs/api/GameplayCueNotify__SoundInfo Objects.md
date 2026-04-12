## GameplayCueNotify\_SoundInfo Objects

```python
class GameplayCueNotify_SoundInfo(StructBase)
```

FGameplayCueNotify_SoundInfo

    Properties that specify how to play a sound effect.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``looping_fade_out_duration`` (float):  [Read-Write] How long it should take to fade out.  Only used on looping gameplay cues.
- ``looping_fade_volume_level`` (float):  [Read-Write] The volume level you want the sound to fade out to over the 'Looping Fade Out Duration' before stopping.
  This value is irrelevant if the 'Looping Fade Out Duration' is zero.
  NOTE: If the fade out duration is positive and this value is not lower than the volume the sound is playing at, the sound will never stop!
- ``override_placement_info`` (bool):  [Read-Write] If enabled, use the placement info override and not the default one.
- ``override_spawn_condition`` (bool):  [Read-Write] If enabled, use the spawn condition override and not the default one.
- ``placement_info_override`` (GameplayCueNotify_PlacementInfo):  [Read-Write] Defines how the sound will be placed.
- ``sound`` (SoundBase):  [Read-Write] Sound to play.
- ``sound_cue`` (SoundBase):  [Read-Write]
  deprecated: 5.0 - SoundCue is deprecated. Instead use the Sound property. The type is USoundBase not USoundCue.
- ``sound_parameter_interface_info`` (GameplayCueNotify_SoundParameterInterfaceInfo):  [Read-Write] Defines how to interface with the sound.
- ``spawn_condition_override`` (GameplayCueNotify_SpawnCondition):  [Read-Write] Condition to check before playing the sound.
- ``use_sound_parameter_interface`` (bool):  [Read-Write] If enabled, use the placement info override and not the default one.

<a id="unreal.GameplayCueNotify_SoundInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(spawn_condition_override: GameplayCueNotify_SpawnCondition = [
    GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR,
    GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []
],
             placement_info_override: GameplayCueNotify_PlacementInfo = [
                 "None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH,
                 AttachmentRule.KEEP_WORLD, False, True,
                 [0.000000, 0.000000,
                  0.000000], [1.000000, 1.000000, 1.000000]
             ],
             sound: SoundBase = None,
             looping_fade_out_duration: float = 0.000000,
             looping_fade_volume_level: float = 0.000000,
             sound_parameter_interface_info:
             GameplayCueNotify_SoundParameterInterfaceInfo = ["OnStop"],
             override_spawn_condition: bool = False,
             override_placement_info: bool = False,
             use_sound_parameter_interface: bool = False) -> None
```

<a id="unreal.GameplayCueNotify_SoundInfo.spawn_condition_override"></a>

#### spawn\_condition\_override

```python
@property
def spawn_condition_override() -> GameplayCueNotify_SpawnCondition
```

(GameplayCueNotify_SpawnCondition):  [Read-Only] Condition to check before playing the sound.

<a id="unreal.GameplayCueNotify_SoundInfo.placement_info_override"></a>

#### placement\_info\_override

```python
@property
def placement_info_override() -> GameplayCueNotify_PlacementInfo
```

(GameplayCueNotify_PlacementInfo):  [Read-Only] Defines how the sound will be placed.

<a id="unreal.GameplayCueNotify_SoundInfo.sound"></a>

#### sound

```python
@property
def sound() -> SoundBase
```

(SoundBase):  [Read-Only] Sound to play.

<a id="unreal.GameplayCueNotify_SoundInfo.sound_cue"></a>

#### sound\_cue

```python
@property
def sound_cue() -> SoundBase
```

(SoundBase):  [Read-Write]
deprecated: 5.0 - SoundCue is deprecated. Instead use the Sound property. The type is USoundBase not USoundCue.

<a id="unreal.GameplayCueNotify_SoundInfo.sound_cue"></a>

#### sound\_cue

```python
@sound_cue.setter
def sound_cue(value: SoundBase) -> None
```

<a id="unreal.GameplayCueNotify_SoundInfo.looping_fade_out_duration"></a>

#### looping\_fade\_out\_duration

```python
@property
def looping_fade_out_duration() -> float
```

(float):  [Read-Only] How long it should take to fade out.  Only used on looping gameplay cues.

<a id="unreal.GameplayCueNotify_SoundInfo.looping_fade_volume_level"></a>

#### looping\_fade\_volume\_level

```python
@property
def looping_fade_volume_level() -> float
```

(float):  [Read-Only] The volume level you want the sound to fade out to over the 'Looping Fade Out Duration' before stopping.
This value is irrelevant if the 'Looping Fade Out Duration' is zero.
NOTE: If the fade out duration is positive and this value is not lower than the volume the sound is playing at, the sound will never stop!

<a id="unreal.GameplayCueNotify_SoundInfo.sound_parameter_interface_info"></a>

#### sound\_parameter\_interface\_info

```python
@property
def sound_parameter_interface_info(
) -> GameplayCueNotify_SoundParameterInterfaceInfo
```

(GameplayCueNotify_SoundParameterInterfaceInfo):  [Read-Only] Defines how to interface with the sound.

<a id="unreal.GameplayCueNotify_SoundInfo.override_spawn_condition"></a>

#### override\_spawn\_condition

```python
@property
def override_spawn_condition() -> bool
```

(bool):  [Read-Only] If enabled, use the spawn condition override and not the default one.

<a id="unreal.GameplayCueNotify_SoundInfo.override_placement_info"></a>

#### override\_placement\_info

```python
@property
def override_placement_info() -> bool
```

(bool):  [Read-Only] If enabled, use the placement info override and not the default one.

<a id="unreal.GameplayCueNotify_SoundInfo.use_sound_parameter_interface"></a>

#### use\_sound\_parameter\_interface

```python
@property
def use_sound_parameter_interface() -> bool
```

(bool):  [Read-Only] If enabled, use the placement info override and not the default one.

<a id="unreal.GameplayCueNotify_CameraShakeInfo"></a>