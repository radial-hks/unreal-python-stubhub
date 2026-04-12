## GameplayAbilityTargetingLocationInfo Objects

```python
class GameplayAbilityTargetingLocationInfo(StructBase)
```

Structure that stores a location in one of several different formats

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTargetTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``literal_transform`` (Transform):  [Read-Write] A literal world transform can be used, if one has been calculated outside of the actor using the ability.
- ``location_type`` (GameplayAbilityTargetingLocationType):  [Read-Write] Type of location used - will determine what data is transmitted over the network and what fields are used when calculating position.
- ``source_ability`` (GameplayAbility):  [Read-Write] Ability that will be using the targeting data
- ``source_actor`` (Actor):  [Read-Write] A source actor is needed for Actor-based targeting, but not for Socket-based targeting.
- ``source_component`` (MeshComponent):  [Read-Write] Socket-based targeting requires a skeletal mesh component to check for the named socket.
- ``source_socket_name`` (Name):  [Read-Write] If SourceComponent is valid, this is the name of the socket transform that will be used. If no Socket is provided, SourceComponent's transform will be used.

<a id="unreal.GameplayAbilityTargetingLocationInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    source_actor: Actor = None,
    source_component: MeshComponent = None,
    source_ability: GameplayAbility = None,
    literal_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                    [-0.000000, 0.000000, 0.000000],
                                    [1.000000, 1.000000, 1.000000]],
    source_socket_name: Name = "None",
    location_type:
    GameplayAbilityTargetingLocationType = GameplayAbilityTargetingLocationType
    .LITERAL_TRANSFORM
) -> None
```

<a id="unreal.GameplayAbilityTargetingLocationInfo.source_actor"></a>

#### source\_actor

```python
@property
def source_actor() -> Actor
```

(Actor):  [Read-Write] A source actor is needed for Actor-based targeting, but not for Socket-based targeting.

<a id="unreal.GameplayAbilityTargetingLocationInfo.source_actor"></a>

#### source\_actor

```python
@source_actor.setter
def source_actor(value: Actor) -> None
```

<a id="unreal.GameplayAbilityTargetingLocationInfo.source_component"></a>

#### source\_component

```python
@property
def source_component() -> MeshComponent
```

(MeshComponent):  [Read-Write] Socket-based targeting requires a skeletal mesh component to check for the named socket.

<a id="unreal.GameplayAbilityTargetingLocationInfo.source_component"></a>

#### source\_component

```python
@source_component.setter
def source_component(value: MeshComponent) -> None
```

<a id="unreal.GameplayAbilityTargetingLocationInfo.source_ability"></a>

#### source\_ability

```python
@property
def source_ability() -> GameplayAbility
```

(GameplayAbility):  [Read-Write] Ability that will be using the targeting data

<a id="unreal.GameplayAbilityTargetingLocationInfo.source_ability"></a>

#### source\_ability

```python
@source_ability.setter
def source_ability(value: GameplayAbility) -> None
```

<a id="unreal.GameplayAbilityTargetingLocationInfo.literal_transform"></a>

#### literal\_transform

```python
@property
def literal_transform() -> Transform
```

(Transform):  [Read-Write] A literal world transform can be used, if one has been calculated outside of the actor using the ability.

<a id="unreal.GameplayAbilityTargetingLocationInfo.literal_transform"></a>

#### literal\_transform

```python
@literal_transform.setter
def literal_transform(value: Transform) -> None
```

<a id="unreal.GameplayAbilityTargetingLocationInfo.source_socket_name"></a>

#### source\_socket\_name

```python
@property
def source_socket_name() -> Name
```

(Name):  [Read-Write] If SourceComponent is valid, this is the name of the socket transform that will be used. If no Socket is provided, SourceComponent's transform will be used.

<a id="unreal.GameplayAbilityTargetingLocationInfo.source_socket_name"></a>

#### source\_socket\_name

```python
@source_socket_name.setter
def source_socket_name(value: Name) -> None
```

<a id="unreal.GameplayAbilityTargetingLocationInfo.location_type"></a>

#### location\_type

```python
@property
def location_type() -> GameplayAbilityTargetingLocationType
```

(GameplayAbilityTargetingLocationType):  [Read-Write] Type of location used - will determine what data is transmitted over the network and what fields are used when calculating position.

<a id="unreal.GameplayAbilityTargetingLocationInfo.location_type"></a>

#### location\_type

```python
@location_type.setter
def location_type(value: GameplayAbilityTargetingLocationType) -> None
```

<a id="unreal.GameplayAbilityTargetData"></a>