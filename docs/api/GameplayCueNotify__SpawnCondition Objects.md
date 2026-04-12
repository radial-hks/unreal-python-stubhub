## GameplayCueNotify\_SpawnCondition Objects

```python
class GameplayCueNotify_SpawnCondition(StructBase)
```

FGameplayCueNotify_SpawnCondition

    Conditions used to determine if the gameplay cue notify should spawn.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allowed_surface_types`` (Array[PhysicalSurface]):  [Read-Write] The gameplay cue effects will only spawn if the surface type is in this list.
  An empty list means everything is allowed.
- ``chance_to_play`` (float):  [Read-Write] Random chance to play the effects.  (1.0 = always play,  0.0 = never play)
- ``locally_controlled_policy`` (GameplayCueNotify_LocallyControlledPolicy):  [Read-Write] Locally controlled policy used to determine if the gameplay cue effects should spawn.
- ``locally_controlled_source`` (GameplayCueNotify_LocallyControlledSource):  [Read-Write] Source actor to use when determining if it is locally controlled.
- ``rejected_surface_types`` (Array[PhysicalSurface]):  [Read-Write] The gameplay cue effects will only spawn if the surface type is NOT in this list.
  An empty list means nothing will be rejected.

<a id="unreal.GameplayCueNotify_SpawnCondition.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        locally_controlled_source:
    GameplayCueNotify_LocallyControlledSource = GameplayCueNotify_LocallyControlledSource
    .INSTIGATOR_ACTOR,
        locally_controlled_policy:
    GameplayCueNotify_LocallyControlledPolicy = GameplayCueNotify_LocallyControlledPolicy
    .ALWAYS,
        chance_to_play: float = 0.000000,
        allowed_surface_types: Array[PhysicalSurface] = [],
        rejected_surface_types: Array[PhysicalSurface] = []) -> None
```

<a id="unreal.GameplayCueNotify_SpawnCondition.locally_controlled_source"></a>

#### locally\_controlled\_source

```python
@property
def locally_controlled_source() -> GameplayCueNotify_LocallyControlledSource
```

(GameplayCueNotify_LocallyControlledSource):  [Read-Only] Source actor to use when determining if it is locally controlled.

<a id="unreal.GameplayCueNotify_SpawnCondition.locally_controlled_policy"></a>

#### locally\_controlled\_policy

```python
@property
def locally_controlled_policy() -> GameplayCueNotify_LocallyControlledPolicy
```

(GameplayCueNotify_LocallyControlledPolicy):  [Read-Only] Locally controlled policy used to determine if the gameplay cue effects should spawn.

<a id="unreal.GameplayCueNotify_SpawnCondition.chance_to_play"></a>

#### chance\_to\_play

```python
@property
def chance_to_play() -> float
```

(float):  [Read-Only] Random chance to play the effects.  (1.0 = always play,  0.0 = never play)

<a id="unreal.GameplayCueNotify_SpawnCondition.allowed_surface_types"></a>

#### allowed\_surface\_types

```python
@property
def allowed_surface_types() -> Array[PhysicalSurface]
```

(Array[PhysicalSurface]):  [Read-Only] The gameplay cue effects will only spawn if the surface type is in this list.
An empty list means everything is allowed.

<a id="unreal.GameplayCueNotify_SpawnCondition.rejected_surface_types"></a>

#### rejected\_surface\_types

```python
@property
def rejected_surface_types() -> Array[PhysicalSurface]
```

(Array[PhysicalSurface]):  [Read-Only] The gameplay cue effects will only spawn if the surface type is NOT in this list.
An empty list means nothing will be rejected.

<a id="unreal.GameplayCueNotify_PlacementInfo"></a>