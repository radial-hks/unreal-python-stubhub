## GameplayAbilityTargetData\_ActorArray Objects

```python
class GameplayAbilityTargetData_ActorArray(GameplayAbilityTargetData)
```

Target data with a source location and a list of targeted actors, makes sense for AOE attacks

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTargetTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``source_location`` (GameplayAbilityTargetingLocationInfo):  [Read-Write] We could be selecting this group of actors from any type of location, so use a generic location type
- ``target_actor_array`` (Array[Actor]):  [Read-Write] Rather than targeting a single point, this type of targeting selects multiple actors.

<a id="unreal.GameplayAbilityTargetData_ActorArray.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    source_location: GameplayAbilityTargetingLocationInfo = [
        None, None, None,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], "None",
        GameplayAbilityTargetingLocationType.LITERAL_TRANSFORM
    ]
) -> None
```

<a id="unreal.GameplayAbilityTargetData_ActorArray.source_location"></a>

#### source\_location

```python
@property
def source_location() -> GameplayAbilityTargetingLocationInfo
```

(GameplayAbilityTargetingLocationInfo):  [Read-Write] We could be selecting this group of actors from any type of location, so use a generic location type

<a id="unreal.GameplayAbilityTargetData_ActorArray.source_location"></a>

#### source\_location

```python
@source_location.setter
def source_location(value: GameplayAbilityTargetingLocationInfo) -> None
```

<a id="unreal.GameplayAbilityTargetData_SingleTargetHit"></a>