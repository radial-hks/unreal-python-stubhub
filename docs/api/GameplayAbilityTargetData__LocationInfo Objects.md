## GameplayAbilityTargetData\_LocationInfo Objects

```python
class GameplayAbilityTargetData_LocationInfo(GameplayAbilityTargetData)
```

Target data with just a source and target location in space

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTargetTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``source_location`` (GameplayAbilityTargetingLocationInfo):  [Read-Write] Generic location data for source
- ``target_location`` (GameplayAbilityTargetingLocationInfo):  [Read-Write] Generic location data for target

<a id="unreal.GameplayAbilityTargetData_LocationInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    source_location: GameplayAbilityTargetingLocationInfo = [
        None, None, None,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], "None",
        GameplayAbilityTargetingLocationType.LITERAL_TRANSFORM
    ],
    target_location: GameplayAbilityTargetingLocationInfo = [
        None, None, None,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], "None",
        GameplayAbilityTargetingLocationType.LITERAL_TRANSFORM
    ]
) -> None
```

<a id="unreal.GameplayAbilityTargetData_LocationInfo.source_location"></a>

#### source\_location

```python
@property
def source_location() -> GameplayAbilityTargetingLocationInfo
```

(GameplayAbilityTargetingLocationInfo):  [Read-Write] Generic location data for source

<a id="unreal.GameplayAbilityTargetData_LocationInfo.source_location"></a>

#### source\_location

```python
@source_location.setter
def source_location(value: GameplayAbilityTargetingLocationInfo) -> None
```

<a id="unreal.GameplayAbilityTargetData_LocationInfo.target_location"></a>

#### target\_location

```python
@property
def target_location() -> GameplayAbilityTargetingLocationInfo
```

(GameplayAbilityTargetingLocationInfo):  [Read-Write] Generic location data for target

<a id="unreal.GameplayAbilityTargetData_LocationInfo.target_location"></a>

#### target\_location

```python
@target_location.setter
def target_location(value: GameplayAbilityTargetingLocationInfo) -> None
```

<a id="unreal.GameplayAbilityTargetData_ActorArray"></a>