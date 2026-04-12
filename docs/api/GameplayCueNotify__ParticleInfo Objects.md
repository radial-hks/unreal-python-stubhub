## GameplayCueNotify\_ParticleInfo Objects

```python
class GameplayCueNotify_ParticleInfo(StructBase)
```

FGameplayCueNotify_ParticleInfo

    Properties that specify how to play a particle effect.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cast_shadow`` (bool):  [Read-Write] If enabled, this particle system will cast a shadow.
- ``niagara_system`` (NiagaraSystem):  [Read-Write] Niagara FX system to spawn.
- ``override_placement_info`` (bool):  [Read-Write] If enabled, use the placement info override and not the default one.
- ``override_spawn_condition`` (bool):  [Read-Write] If enabled, use the spawn condition override and not the default one.
- ``placement_info_override`` (GameplayCueNotify_PlacementInfo):  [Read-Write] Defines how the particle system will be placed.
- ``spawn_condition_override`` (GameplayCueNotify_SpawnCondition):  [Read-Write] Condition to check before spawning the particle system.

<a id="unreal.GameplayCueNotify_ParticleInfo.__init__"></a>

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
             niagara_system: NiagaraSystem = None,
             override_spawn_condition: bool = False,
             override_placement_info: bool = False,
             cast_shadow: bool = False) -> None
```

<a id="unreal.GameplayCueNotify_ParticleInfo.spawn_condition_override"></a>

#### spawn\_condition\_override

```python
@property
def spawn_condition_override() -> GameplayCueNotify_SpawnCondition
```

(GameplayCueNotify_SpawnCondition):  [Read-Only] Condition to check before spawning the particle system.

<a id="unreal.GameplayCueNotify_ParticleInfo.placement_info_override"></a>

#### placement\_info\_override

```python
@property
def placement_info_override() -> GameplayCueNotify_PlacementInfo
```

(GameplayCueNotify_PlacementInfo):  [Read-Only] Defines how the particle system will be placed.

<a id="unreal.GameplayCueNotify_ParticleInfo.niagara_system"></a>

#### niagara\_system

```python
@property
def niagara_system() -> NiagaraSystem
```

(NiagaraSystem):  [Read-Only] Niagara FX system to spawn.

<a id="unreal.GameplayCueNotify_ParticleInfo.override_spawn_condition"></a>

#### override\_spawn\_condition

```python
@property
def override_spawn_condition() -> bool
```

(bool):  [Read-Only] If enabled, use the spawn condition override and not the default one.

<a id="unreal.GameplayCueNotify_ParticleInfo.override_placement_info"></a>

#### override\_placement\_info

```python
@property
def override_placement_info() -> bool
```

(bool):  [Read-Only] If enabled, use the placement info override and not the default one.

<a id="unreal.GameplayCueNotify_ParticleInfo.cast_shadow"></a>

#### cast\_shadow

```python
@property
def cast_shadow() -> bool
```

(bool):  [Read-Only] If enabled, this particle system will cast a shadow.

<a id="unreal.GameplayCueNotify_SoundParameterInterfaceInfo"></a>