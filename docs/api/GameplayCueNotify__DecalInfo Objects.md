## GameplayCueNotify\_DecalInfo Objects

```python
class GameplayCueNotify_DecalInfo(StructBase)
```

FGameplayCueNotify_DecalInfo

    Properties that specify how to spawn a decal.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``decal_material`` (MaterialInterface):  [Read-Write] Decal material to spawn.
- ``decal_size`` (Vector):  [Read-Write] Decal size in local space (does not include the component scale).
- ``fade_out_duration`` (float):  [Read-Write] Sets how long it takes for decal actor to fade out.  Will override setting in class.
- ``fade_out_start_delay`` (float):  [Read-Write] Sets when the decal actor will start fading out.  Will override setting in class.
- ``override_fade_out`` (bool):  [Read-Write] If enabled, override default decal actor fade out values.
- ``override_placement_info`` (bool):  [Read-Write] If enabled, use the placement info override and not the default one.
- ``override_spawn_condition`` (bool):  [Read-Write] If enabled, use the spawn condition override and not the default one.
- ``placement_info_override`` (GameplayCueNotify_PlacementInfo):  [Read-Write] Defines how the decal will be placed.
- ``spawn_condition_override`` (GameplayCueNotify_SpawnCondition):  [Read-Write] Condition to check before spawning the decal.

<a id="unreal.GameplayCueNotify_DecalInfo.__init__"></a>

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
             decal_material: MaterialInterface = None,
             decal_size: Vector = [0.000000, 0.000000, 0.000000],
             override_spawn_condition: bool = False,
             override_placement_info: bool = False,
             override_fade_out: bool = False,
             fade_out_start_delay: float = 0.000000,
             fade_out_duration: float = 0.000000) -> None
```

<a id="unreal.GameplayCueNotify_DecalInfo.spawn_condition_override"></a>

#### spawn\_condition\_override

```python
@property
def spawn_condition_override() -> GameplayCueNotify_SpawnCondition
```

(GameplayCueNotify_SpawnCondition):  [Read-Only] Condition to check before spawning the decal.

<a id="unreal.GameplayCueNotify_DecalInfo.placement_info_override"></a>

#### placement\_info\_override

```python
@property
def placement_info_override() -> GameplayCueNotify_PlacementInfo
```

(GameplayCueNotify_PlacementInfo):  [Read-Only] Defines how the decal will be placed.

<a id="unreal.GameplayCueNotify_DecalInfo.decal_material"></a>

#### decal\_material

```python
@property
def decal_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] Decal material to spawn.

<a id="unreal.GameplayCueNotify_DecalInfo.decal_size"></a>

#### decal\_size

```python
@property
def decal_size() -> Vector
```

(Vector):  [Read-Only] Decal size in local space (does not include the component scale).

<a id="unreal.GameplayCueNotify_DecalInfo.override_spawn_condition"></a>

#### override\_spawn\_condition

```python
@property
def override_spawn_condition() -> bool
```

(bool):  [Read-Only] If enabled, use the spawn condition override and not the default one.

<a id="unreal.GameplayCueNotify_DecalInfo.override_placement_info"></a>

#### override\_placement\_info

```python
@property
def override_placement_info() -> bool
```

(bool):  [Read-Only] If enabled, use the placement info override and not the default one.

<a id="unreal.GameplayCueNotify_DecalInfo.override_fade_out"></a>

#### override\_fade\_out

```python
@property
def override_fade_out() -> bool
```

(bool):  [Read-Only] If enabled, override default decal actor fade out values.

<a id="unreal.GameplayCueNotify_DecalInfo.fade_out_start_delay"></a>

#### fade\_out\_start\_delay

```python
@property
def fade_out_start_delay() -> float
```

(float):  [Read-Only] Sets when the decal actor will start fading out.  Will override setting in class.

<a id="unreal.GameplayCueNotify_DecalInfo.fade_out_duration"></a>

#### fade\_out\_duration

```python
@property
def fade_out_duration() -> float
```

(float):  [Read-Only] Sets how long it takes for decal actor to fade out.  Will override setting in class.

<a id="unreal.GameplayCueNotify_BurstEffects"></a>