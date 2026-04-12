## GameplayCueNotify\_CameraLensEffectInfo Objects

```python
class GameplayCueNotify_CameraLensEffectInfo(StructBase)
```

FGameplayCueNotify_CameraLensEffectInfo

    Properties that specify how to play a camera lens effect.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_lens_effect`` (type(Class)):  [Read-Write] Camera lens effect to play.
- ``override_placement_info`` (bool):  [Read-Write] If enabled, use the placement info override and not the default one.
- ``override_spawn_condition`` (bool):  [Read-Write] If enabled, use the spawn condition override and not the default one.
- ``placement_info_override`` (GameplayCueNotify_PlacementInfo):  [Read-Write] Defines how the camera lens effect will be placed.
- ``play_in_world`` (bool):  [Read-Write] If enabled, the camera lens effect will be played in the world and affect all players.
- ``spawn_condition_override`` (GameplayCueNotify_SpawnCondition):  [Read-Write] Condition to check before playing the camera lens effect.
- ``world_inner_radius`` (float):  [Read-Write] Players inside this radius get the full intensity camera lens effect.
- ``world_outer_radius`` (float):  [Read-Write] Players outside this radius do not get the camera lens effect applied.

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.__init__"></a>

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
             camera_lens_effect: Class = None,
             override_spawn_condition: bool = False,
             override_placement_info: bool = False,
             play_in_world: bool = False,
             world_inner_radius: float = 0.000000,
             world_outer_radius: float = 0.000000) -> None
```

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.spawn_condition_override"></a>

#### spawn\_condition\_override

```python
@property
def spawn_condition_override() -> GameplayCueNotify_SpawnCondition
```

(GameplayCueNotify_SpawnCondition):  [Read-Only] Condition to check before playing the camera lens effect.

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.placement_info_override"></a>

#### placement\_info\_override

```python
@property
def placement_info_override() -> GameplayCueNotify_PlacementInfo
```

(GameplayCueNotify_PlacementInfo):  [Read-Only] Defines how the camera lens effect will be placed.

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.camera_lens_effect"></a>

#### camera\_lens\_effect

```python
@property
def camera_lens_effect() -> Class
```

(type(Class)):  [Read-Only] Camera lens effect to play.

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.override_spawn_condition"></a>

#### override\_spawn\_condition

```python
@property
def override_spawn_condition() -> bool
```

(bool):  [Read-Only] If enabled, use the spawn condition override and not the default one.

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.override_placement_info"></a>

#### override\_placement\_info

```python
@property
def override_placement_info() -> bool
```

(bool):  [Read-Only] If enabled, use the placement info override and not the default one.

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.play_in_world"></a>

#### play\_in\_world

```python
@property
def play_in_world() -> bool
```

(bool):  [Read-Only] If enabled, the camera lens effect will be played in the world and affect all players.

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.world_inner_radius"></a>

#### world\_inner\_radius

```python
@property
def world_inner_radius() -> float
```

(float):  [Read-Only] Players inside this radius get the full intensity camera lens effect.

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo.world_outer_radius"></a>

#### world\_outer\_radius

```python
@property
def world_outer_radius() -> float
```

(float):  [Read-Only] Players outside this radius do not get the camera lens effect applied.

<a id="unreal.GameplayCueNotify_ForceFeedbackInfo"></a>