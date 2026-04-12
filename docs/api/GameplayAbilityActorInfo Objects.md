## GameplayAbilityActorInfo Objects

```python
class GameplayAbilityActorInfo(StructBase)
```

FGameplayAbilityActorInfo

Cached data associated with an Actor using an Ability.
        -Initialized from an AActor* in InitFromActor
        -Abilities use this to know what to actor upon. E.g., instead of being coupled to a specific actor class.
        -These are generally passed around as pointers to support polymorphism.
        -Projects can override UAbilitySystemGlobals::AllocAbilityActorInfo to override the default struct type that is created.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ability_system_component`` (AbilitySystemComponent):  [Read-Write] Ability System component associated with the owner actor, shouldn't be null
- ``affected_anim_instance_tag`` (Name):  [Read-Write] The linked Anim Instance that this component will play montages in. Use NAME_None for the main anim instance.
- ``anim_instance`` (AnimInstance):  [Read-Write] Anim instance of the avatar actor. Often null
- ``avatar_actor`` (Actor):  [Read-Write] The physical representation of the owner, used for targeting and animation. This will often be null!
- ``movement_component`` (MovementComponent):  [Read-Write] Movement component of the avatar actor. Often null
- ``owner_actor`` (Actor):  [Read-Write] The actor that owns the abilities, shouldn't be null
- ``player_controller`` (PlayerController):  [Read-Write] PlayerController associated with the owning actor. This will often be null!
- ``skeletal_mesh_component`` (SkeletalMeshComponent):  [Read-Write] Skeletal mesh of the avatar actor. Often null

<a id="unreal.GameplayAbilityActorInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(owner_actor: Actor = None,
             avatar_actor: Actor = None,
             player_controller: PlayerController = None,
             ability_system_component: AbilitySystemComponent = None,
             skeletal_mesh_component: SkeletalMeshComponent = None,
             anim_instance: AnimInstance = None,
             movement_component: MovementComponent = None,
             affected_anim_instance_tag: Name = "None") -> None
```

<a id="unreal.GameplayAbilityActorInfo.owner_actor"></a>

#### owner\_actor

```python
@property
def owner_actor() -> Actor
```

(Actor):  [Read-Only] The actor that owns the abilities, shouldn't be null

<a id="unreal.GameplayAbilityActorInfo.avatar_actor"></a>

#### avatar\_actor

```python
@property
def avatar_actor() -> Actor
```

(Actor):  [Read-Only] The physical representation of the owner, used for targeting and animation. This will often be null!

<a id="unreal.GameplayAbilityActorInfo.player_controller"></a>

#### player\_controller

```python
@property
def player_controller() -> PlayerController
```

(PlayerController):  [Read-Only] PlayerController associated with the owning actor. This will often be null!

<a id="unreal.GameplayAbilityActorInfo.ability_system_component"></a>

#### ability\_system\_component

```python
@property
def ability_system_component() -> AbilitySystemComponent
```

(AbilitySystemComponent):  [Read-Only] Ability System component associated with the owner actor, shouldn't be null

<a id="unreal.GameplayAbilityActorInfo.skeletal_mesh_component"></a>

#### skeletal\_mesh\_component

```python
@property
def skeletal_mesh_component() -> SkeletalMeshComponent
```

(SkeletalMeshComponent):  [Read-Only] Skeletal mesh of the avatar actor. Often null

<a id="unreal.GameplayAbilityActorInfo.anim_instance"></a>

#### anim\_instance

```python
@property
def anim_instance() -> AnimInstance
```

(AnimInstance):  [Read-Only] Anim instance of the avatar actor. Often null

<a id="unreal.GameplayAbilityActorInfo.movement_component"></a>

#### movement\_component

```python
@property
def movement_component() -> MovementComponent
```

(MovementComponent):  [Read-Only] Movement component of the avatar actor. Often null

<a id="unreal.GameplayAbilityActorInfo.affected_anim_instance_tag"></a>

#### affected\_anim\_instance\_tag

```python
@property
def affected_anim_instance_tag() -> Name
```

(Name):  [Read-Only] The linked Anim Instance that this component will play montages in. Use NAME_None for the main anim instance.

<a id="unreal.AbilityEndedData"></a>