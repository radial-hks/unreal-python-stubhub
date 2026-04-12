## GameplayCueNotify\_Burst Objects

```python
class GameplayCueNotify_Burst(GameplayCueNotify_Static)
```

UGameplayCueNotify_Burst

    This is a non-instanced gameplay cue notify for effects that are one-offs.
    Since it is not instanced, it cannot do latent actions such as delays and time lines.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotify_Burst.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``burst_effects`` (GameplayCueNotify_BurstEffects):  [Read-Write] List of effects to spawn on burst.
- ``default_placement_info`` (GameplayCueNotify_PlacementInfo):  [Read-Write] Default placement rules.  Applies for all spawns unless overridden.
- ``default_spawn_condition`` (GameplayCueNotify_SpawnCondition):  [Read-Write] Default condition to check before spawning anything.  Applies for all spawns unless overridden.
- ``gameplay_cue_tag`` (GameplayTag):  [Read-Write] Tag this notify is activated by
- ``is_override`` (bool):  [Read-Write] Does this Cue override other cues, or is it called in addition to them? E.g., If this is Damage.Physical.Slash, we wont call Damage.Physical afer we run this cue.

<a id="unreal.GameplayCueNotify_Burst.default_spawn_condition"></a>

#### default\_spawn\_condition

```python
@property
def default_spawn_condition() -> GameplayCueNotify_SpawnCondition
```

(GameplayCueNotify_SpawnCondition):  [Read-Only] Default condition to check before spawning anything.  Applies for all spawns unless overridden.

<a id="unreal.GameplayCueNotify_Burst.default_placement_info"></a>

#### default\_placement\_info

```python
@property
def default_placement_info() -> GameplayCueNotify_PlacementInfo
```

(GameplayCueNotify_PlacementInfo):  [Read-Only] Default placement rules.  Applies for all spawns unless overridden.

<a id="unreal.GameplayCueNotify_Burst.burst_effects"></a>

#### burst\_effects

```python
@property
def burst_effects() -> GameplayCueNotify_BurstEffects
```

(GameplayCueNotify_BurstEffects):  [Read-Only] List of effects to spawn on burst.

<a id="unreal.GameplayCueNotify_Burst.on_burst"></a>

#### on\_burst

```python
def on_burst(target: Actor, parameters: GameplayCueParameters,
             spawn_results: GameplayCueNotify_SpawnResult) -> None
```

x.on_burst(target, parameters, spawn_results) -> None
On Burst

Args:
    target (Actor): 
    parameters (GameplayCueParameters): 
    spawn_results (GameplayCueNotify_SpawnResult):

<a id="unreal.GameplayCueNotify_BurstLatent"></a>