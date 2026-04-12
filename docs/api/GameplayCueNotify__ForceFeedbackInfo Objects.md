## GameplayCueNotify\_ForceFeedbackInfo Objects

```python
class GameplayCueNotify_ForceFeedbackInfo(StructBase)
```

FGameplayCueNotify_ForceFeedbackInfo

    Properties that specify how to play a force feedback effect.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``force_feedback_effect`` (ForceFeedbackEffect):  [Read-Write] Force feedback effect to play.
- ``force_feedback_tag`` (Name):  [Read-Write] Tag used to identify the force feedback effect so it can later be canceled.
  Warning: If this is "None" it will stop ALL force feedback effects if it is canceled.
- ``is_looping`` (bool):  [Read-Write] If enabled, the force feedback will be set to loop.
- ``override_placement_info`` (bool):  [Read-Write] If enabled, use the placement info override and not the default one.
- ``override_spawn_condition`` (bool):  [Read-Write] If enabled, use the spawn condition override and not the default one.
- ``placement_info_override`` (GameplayCueNotify_PlacementInfo):  [Read-Write] Defines how the force feedback will be placed.
- ``play_in_world`` (bool):  [Read-Write] If enabled, the force feedback will be played in the world and affect all players.
- ``spawn_condition_override`` (GameplayCueNotify_SpawnCondition):  [Read-Write] Condition to check before playing the force feedback.
- ``world_attenuation`` (ForceFeedbackAttenuation):  [Read-Write] How the force feedback is attenuated over distance when played in world.
- ``world_intensity`` (float):  [Read-Write] Multiplier applied to the force feedback when played in world.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.__init__"></a>

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
             force_feedback_effect: ForceFeedbackEffect = None,
             force_feedback_tag: Name = "None",
             is_looping: bool = False,
             override_spawn_condition: bool = False,
             override_placement_info: bool = False,
             play_in_world: bool = False,
             world_intensity: float = 0.000000,
             world_attenuation: ForceFeedbackAttenuation = None) -> None
```

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.spawn_condition_override"></a>

#### spawn\_condition\_override

```python
@property
def spawn_condition_override() -> GameplayCueNotify_SpawnCondition
```

(GameplayCueNotify_SpawnCondition):  [Read-Only] Condition to check before playing the force feedback.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.placement_info_override"></a>

#### placement\_info\_override

```python
@property
def placement_info_override() -> GameplayCueNotify_PlacementInfo
```

(GameplayCueNotify_PlacementInfo):  [Read-Only] Defines how the force feedback will be placed.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.force_feedback_effect"></a>

#### force\_feedback\_effect

```python
@property
def force_feedback_effect() -> ForceFeedbackEffect
```

(ForceFeedbackEffect):  [Read-Only] Force feedback effect to play.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.force_feedback_tag"></a>

#### force\_feedback\_tag

```python
@property
def force_feedback_tag() -> Name
```

(Name):  [Read-Only] Tag used to identify the force feedback effect so it can later be canceled.
Warning: If this is "None" it will stop ALL force feedback effects if it is canceled.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.is_looping"></a>

#### is\_looping

```python
@property
def is_looping() -> bool
```

(bool):  [Read-Only] If enabled, the force feedback will be set to loop.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.override_spawn_condition"></a>

#### override\_spawn\_condition

```python
@property
def override_spawn_condition() -> bool
```

(bool):  [Read-Only] If enabled, use the spawn condition override and not the default one.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.override_placement_info"></a>

#### override\_placement\_info

```python
@property
def override_placement_info() -> bool
```

(bool):  [Read-Only] If enabled, use the placement info override and not the default one.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.play_in_world"></a>

#### play\_in\_world

```python
@property
def play_in_world() -> bool
```

(bool):  [Read-Only] If enabled, the force feedback will be played in the world and affect all players.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.world_intensity"></a>

#### world\_intensity

```python
@property
def world_intensity() -> float
```

(float):  [Read-Only] Multiplier applied to the force feedback when played in world.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo.world_attenuation"></a>

#### world\_attenuation

```python
@property
def world_attenuation() -> ForceFeedbackAttenuation
```

(ForceFeedbackAttenuation):  [Read-Only] How the force feedback is attenuated over distance when played in world.

<a id="unreal.GameplayCueNotify_InputDevicePropertyInfo"></a>