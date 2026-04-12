## GameplayCueNotify\_CameraShakeInfo Objects

```python
class GameplayCueNotify_CameraShakeInfo(StructBase)
```

FGameplayCueNotify_CameraShakeInfo

    Properties that specify how to play a camera shake.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_shake`` (type(Class)):  [Read-Write] Camera shake to play.
- ``override_placement_info`` (bool):  [Read-Write] If enabled, use the placement info override and not the default one.
- ``override_spawn_condition`` (bool):  [Read-Write] If enabled, use the spawn condition override and not the default one.
- ``placement_info_override`` (GameplayCueNotify_PlacementInfo):  [Read-Write] Defines how the camera shake will be placed.
- ``play_in_world`` (bool):  [Read-Write] If enabled, the camera shake will be played in the world and affect all players.
- ``play_space`` (GameplayCueNotify_EffectPlaySpace):  [Read-Write] What coordinate space to play the camera shake relative to.
- ``shake_scale`` (float):  [Read-Write] Scale applied to the camera shake.
- ``spawn_condition_override`` (GameplayCueNotify_SpawnCondition):  [Read-Write] Condition to check before playing the camera shake.
- ``world_falloff_exponent`` (float):  [Read-Write] Exponent that describes the shake intensity falloff curve between the inner and outer radii.  (1.0 is linear)
- ``world_inner_radius`` (float):  [Read-Write] Players inside this radius get the full intensity camera shake.
- ``world_outer_radius`` (float):  [Read-Write] Players outside this radius do not get the camera shake applied.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        spawn_condition_override: GameplayCueNotify_SpawnCondition = [
            GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR,
            GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []
        ],
        placement_info_override: GameplayCueNotify_PlacementInfo = [
            "None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH,
            AttachmentRule.KEEP_WORLD, False, True,
            [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]
        ],
        camera_shake: Class = None,
        shake_scale: float = 0.000000,
        play_space:
    GameplayCueNotify_EffectPlaySpace = GameplayCueNotify_EffectPlaySpace.
    WORLD_SPACE,
        override_spawn_condition: bool = False,
        override_placement_info: bool = False,
        play_in_world: bool = False,
        world_inner_radius: float = 0.000000,
        world_outer_radius: float = 0.000000,
        world_falloff_exponent: float = 0.000000) -> None
```

<a id="unreal.GameplayCueNotify_CameraShakeInfo.spawn_condition_override"></a>

#### spawn\_condition\_override

```python
@property
def spawn_condition_override() -> GameplayCueNotify_SpawnCondition
```

(GameplayCueNotify_SpawnCondition):  [Read-Only] Condition to check before playing the camera shake.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.placement_info_override"></a>

#### placement\_info\_override

```python
@property
def placement_info_override() -> GameplayCueNotify_PlacementInfo
```

(GameplayCueNotify_PlacementInfo):  [Read-Only] Defines how the camera shake will be placed.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.camera_shake"></a>

#### camera\_shake

```python
@property
def camera_shake() -> Class
```

(type(Class)):  [Read-Only] Camera shake to play.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.shake_scale"></a>

#### shake\_scale

```python
@property
def shake_scale() -> float
```

(float):  [Read-Only] Scale applied to the camera shake.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.play_space"></a>

#### play\_space

```python
@property
def play_space() -> GameplayCueNotify_EffectPlaySpace
```

(GameplayCueNotify_EffectPlaySpace):  [Read-Only] What coordinate space to play the camera shake relative to.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.override_spawn_condition"></a>

#### override\_spawn\_condition

```python
@property
def override_spawn_condition() -> bool
```

(bool):  [Read-Only] If enabled, use the spawn condition override and not the default one.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.override_placement_info"></a>

#### override\_placement\_info

```python
@property
def override_placement_info() -> bool
```

(bool):  [Read-Only] If enabled, use the placement info override and not the default one.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.play_in_world"></a>

#### play\_in\_world

```python
@property
def play_in_world() -> bool
```

(bool):  [Read-Only] If enabled, the camera shake will be played in the world and affect all players.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.world_inner_radius"></a>

#### world\_inner\_radius

```python
@property
def world_inner_radius() -> float
```

(float):  [Read-Only] Players inside this radius get the full intensity camera shake.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.world_outer_radius"></a>

#### world\_outer\_radius

```python
@property
def world_outer_radius() -> float
```

(float):  [Read-Only] Players outside this radius do not get the camera shake applied.

<a id="unreal.GameplayCueNotify_CameraShakeInfo.world_falloff_exponent"></a>

#### world\_falloff\_exponent

```python
@property
def world_falloff_exponent() -> float
```

(float):  [Read-Only] Exponent that describes the shake intensity falloff curve between the inner and outer radii.  (1.0 is linear)

<a id="unreal.GameplayCueNotify_CameraLensEffectInfo"></a>