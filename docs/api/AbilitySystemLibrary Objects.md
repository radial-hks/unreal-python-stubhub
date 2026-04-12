## AbilitySystemLibrary Objects

```python
class AbilitySystemLibrary(BlueprintFunctionLibrary)
```

Blueprint library for ability system. Many of these functions are useful to call from native as well

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilitySystemBlueprintLibrary.h

<a id="unreal.AbilitySystemLibrary.target_data_has_origin"></a>

#### target\_data\_has\_origin

```python
@classmethod
def target_data_has_origin(cls, target_data: GameplayAbilityTargetDataHandle,
                           index: int) -> bool
```

X.target_data_has_origin(target_data, index) -> bool
Returns true if the target data has an origin

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.target_data_has_hit_result"></a>

#### target\_data\_has\_hit\_result

```python
@classmethod
def target_data_has_hit_result(cls,
                               hit_result: GameplayAbilityTargetDataHandle,
                               index: int) -> bool
```

X.target_data_has_hit_result(hit_result, index) -> bool
Returns true if the target data has a hit result

Args:
    hit_result (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.target_data_has_end_point"></a>

#### target\_data\_has\_end\_point

```python
@classmethod
def target_data_has_end_point(cls,
                              target_data: GameplayAbilityTargetDataHandle,
                              index: int) -> bool
```

X.target_data_has_end_point(target_data, index) -> bool
Returns true if the target data has an end point

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.target_data_has_actor"></a>

#### target\_data\_has\_actor

```python
@classmethod
def target_data_has_actor(cls, target_data: GameplayAbilityTargetDataHandle,
                          index: int) -> bool
```

X.target_data_has_actor(target_data, index) -> bool
Returns true if the given TargetData has at least 1 actor targeted

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.set_stack_count_to_max"></a>

#### set\_stack\_count\_to\_max

```python
@classmethod
def set_stack_count_to_max(
        cls,
        spec_handle: GameplayEffectSpecHandle) -> GameplayEffectSpecHandle
```

X.set_stack_count_to_max(spec_handle) -> GameplayEffectSpecHandle
Sets the GameplayEffectSpec's StackCount to the max stack count defined in the GameplayEffect definition

Args:
    spec_handle (GameplayEffectSpecHandle): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.set_stack_count"></a>

#### set\_stack\_count

```python
@classmethod
def set_stack_count(cls, spec_handle: GameplayEffectSpecHandle,
                    stack_count: int) -> GameplayEffectSpecHandle
```

X.set_stack_count(spec_handle, stack_count) -> GameplayEffectSpecHandle
Sets the GameplayEffectSpec's StackCount to the specified amount (prior to applying)

Args:
    spec_handle (GameplayEffectSpecHandle): 
    stack_count (int32): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.set_duration"></a>

#### set\_duration

```python
@classmethod
def set_duration(cls, spec_handle: GameplayEffectSpecHandle,
                 duration: float) -> GameplayEffectSpecHandle
```

X.set_duration(spec_handle, duration) -> GameplayEffectSpecHandle
Manually sets the duration on a specific effect

Args:
    spec_handle (GameplayEffectSpecHandle): 
    duration (float): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.send_gameplay_event_to_actor"></a>

#### send\_gameplay\_event\_to\_actor

```python
@classmethod
def send_gameplay_event_to_actor(cls, actor: Actor, event_tag: GameplayTag,
                                 payload: GameplayEventData) -> None
```

X.send_gameplay_event_to_actor(actor, event_tag, payload) -> None
This function can be used to trigger an ability on the actor in question with useful payload data.

Args:
    actor (Actor): 
    event_tag (GameplayTag): 
    payload (GameplayEventData):

<a id="unreal.AbilitySystemLibrary.remove_loose_gameplay_tags"></a>

#### remove\_loose\_gameplay\_tags

```python
@classmethod
def remove_loose_gameplay_tags(cls,
                               actor: Actor,
                               gameplay_tags: GameplayTagContainer,
                               should_replicate: bool = False) -> bool
```

X.remove_loose_gameplay_tags(actor, gameplay_tags, should_replicate=False) -> bool
Manually removes a set of tags from a given actor, with optional replication.

Args:
    actor (Actor): 
    gameplay_tags (GameplayTagContainer): 
    should_replicate (bool): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.not_equal_gameplay_attribute_gameplay_attribute"></a>

#### not\_equal\_gameplay\_attribute\_gameplay\_attribute

```python
@classmethod
def not_equal_gameplay_attribute_gameplay_attribute(
        cls, attribute_a: GameplayAttribute,
        attribute_b: GameplayAttribute) -> bool
```

X.not_equal_gameplay_attribute_gameplay_attribute(attribute_a, attribute_b) -> bool
Simple inequality operator for gameplay attributes

Args:
    attribute_a (GameplayAttribute): 
    attribute_b (GameplayAttribute): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.not_equal_gameplay_ability_spec_handle"></a>

#### not\_equal\_gameplay\_ability\_spec\_handle

```python
@classmethod
def not_equal_gameplay_ability_spec_handle(
        cls, a: GameplayAbilitySpecHandle,
        b: GameplayAbilitySpecHandle) -> bool
```

X.not_equal_gameplay_ability_spec_handle(a, b) -> bool
Inequality operator for two Gameplay Ability Spec Handles

Args:
    a (GameplayAbilitySpecHandle): 
    b (GameplayAbilitySpecHandle): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.not_equal_active_gameplay_effect_handle"></a>

#### not\_equal\_active\_gameplay\_effect\_handle

```python
@classmethod
def not_equal_active_gameplay_effect_handle(
        cls, a: ActiveGameplayEffectHandle,
        b: ActiveGameplayEffectHandle) -> bool
```

X.not_equal_active_gameplay_effect_handle(a, b) -> bool
Inequality operator for two Active Gameplay Effect Handles

Args:
    a (ActiveGameplayEffectHandle): 
    b (ActiveGameplayEffectHandle): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.make_spec_handle_by_class"></a>

#### make\_spec\_handle\_by\_class

```python
@classmethod
def make_spec_handle_by_class(
        cls,
        gameplay_effect: Class,
        instigator: Actor,
        effect_causer: Actor,
        level: float = 1.000000) -> GameplayEffectSpecHandle
```

X.make_spec_handle_by_class(gameplay_effect, instigator, effect_causer, level=1.000000) -> GameplayEffectSpecHandle
Create a spec handle, filling out all fields

Args:
    gameplay_effect (type(Class)): 
    instigator (Actor): 
    effect_causer (Actor): 
    level (float): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.make_spec_handle"></a>

#### make\_spec\_handle

```python
@classmethod
def make_spec_handle(cls,
                     gameplay_effect: GameplayEffect,
                     instigator: Actor,
                     effect_causer: Actor,
                     level: float = 1.000000) -> GameplayEffectSpecHandle
```

X.make_spec_handle(gameplay_effect, instigator, effect_causer, level=1.000000) -> GameplayEffectSpecHandle
Make Spec Handle
deprecated: Function 'MakeSpecHandle' is deprecated.

Args:
    gameplay_effect (GameplayEffect): 
    instigator (Actor): 
    effect_causer (Actor): 
    level (float): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.make_filter_handle"></a>

#### make\_filter\_handle

```python
@classmethod
def make_filter_handle(cls, filter: GameplayTargetDataFilter,
                       filter_actor: Actor) -> GameplayTargetDataFilterHandle
```

X.make_filter_handle(filter, filter_actor) -> GameplayTargetDataFilterHandle
Create a handle for filtering target data, filling out all fields

Args:
    filter (GameplayTargetDataFilter): 
    filter_actor (Actor): 

Returns:
    GameplayTargetDataFilterHandle:

<a id="unreal.AbilitySystemLibrary.is_valid"></a>

#### is\_valid

```python
@classmethod
def is_valid(cls, attribute: GameplayAttribute) -> bool
```

X.is_valid(attribute) -> bool
Returns true if the attribute actually exists

Args:
    attribute (GameplayAttribute): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.is_instigator_locally_controlled_player"></a>

#### is\_instigator\_locally\_controlled\_player

```python
@classmethod
def is_instigator_locally_controlled_player(
        cls, parameters: GameplayCueParameters) -> bool
```

X.is_instigator_locally_controlled_player(parameters) -> bool
Returns true if the ability system component that spawned this cue is locally controlled and a player

Args:
    parameters (GameplayCueParameters): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.is_instigator_locally_controlled"></a>

#### is\_instigator\_locally\_controlled

```python
@classmethod
def is_instigator_locally_controlled(
        cls, parameters: GameplayCueParameters) -> bool
```

X.is_instigator_locally_controlled(parameters) -> bool
Returns true if the ability system component that spawned this cue is locally controlled

Args:
    parameters (GameplayCueParameters): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.is_gameplay_ability_active"></a>

#### is\_gameplay\_ability\_active

```python
@classmethod
def is_gameplay_ability_active(cls, gameplay_ability: GameplayAbility) -> bool
```

X.is_gameplay_ability_active(gameplay_ability) -> bool
Returns true if the passed-in Gameplay Ability instance is active (activated and not yet ended).

Args:
    gameplay_ability (GameplayAbility): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.has_hit_result"></a>

#### has\_hit\_result

```python
@classmethod
def has_hit_result(cls, parameters: GameplayCueParameters) -> bool
```

X.has_hit_result(parameters) -> bool
Checks if the effect context has a hit reslt stored inside

Args:
    parameters (GameplayCueParameters): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.get_target_data_origin"></a>

#### get\_target\_data\_origin

```python
@classmethod
def get_target_data_origin(cls, target_data: GameplayAbilityTargetDataHandle,
                           index: int) -> Transform
```

X.get_target_data_origin(target_data, index) -> Transform
Returns the origin for a given index if it exists

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    Transform:

<a id="unreal.AbilitySystemLibrary.get_target_data_end_point_transform"></a>

#### get\_target\_data\_end\_point\_transform

```python
@classmethod
def get_target_data_end_point_transform(
        cls, target_data: GameplayAbilityTargetDataHandle,
        index: int) -> Transform
```

X.get_target_data_end_point_transform(target_data, index) -> Transform
Returns the end point transform for a given index if it exists

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    Transform:

<a id="unreal.AbilitySystemLibrary.get_target_data_end_point"></a>

#### get\_target\_data\_end\_point

```python
@classmethod
def get_target_data_end_point(cls,
                              target_data: GameplayAbilityTargetDataHandle,
                              index: int) -> Vector
```

X.get_target_data_end_point(target_data, index) -> Vector
Returns the end point for a given index if it exists

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    Vector:

<a id="unreal.AbilitySystemLibrary.get_origin"></a>

#### get\_origin

```python
@classmethod
def get_origin(cls, parameters: GameplayCueParameters) -> Vector
```

X.get_origin(parameters) -> Vector
Gets instigating world location

Args:
    parameters (GameplayCueParameters): 

Returns:
    Vector:

<a id="unreal.AbilitySystemLibrary.get_modified_attribute_magnitude"></a>

#### get\_modified\_attribute\_magnitude

```python
@classmethod
def get_modified_attribute_magnitude(cls,
                                     spec_handle: GameplayEffectSpecHandle,
                                     attribute: GameplayAttribute) -> float
```

X.get_modified_attribute_magnitude(spec_handle, attribute) -> float
Gets the magnitude of change for an attribute on an APPLIED GameplayEffectSpec.

Args:
    spec_handle (GameplayEffectSpecHandle): 
    attribute (GameplayAttribute): 

Returns:
    float:

<a id="unreal.AbilitySystemLibrary.get_instigator_transform"></a>

#### get\_instigator\_transform

```python
@classmethod
def get_instigator_transform(cls,
                             parameters: GameplayCueParameters) -> Transform
```

X.get_instigator_transform(parameters) -> Transform
Gets instigating world location

Args:
    parameters (GameplayCueParameters): 

Returns:
    Transform:

<a id="unreal.AbilitySystemLibrary.get_instigator_actor"></a>

#### get\_instigator\_actor

```python
@classmethod
def get_instigator_actor(cls, parameters: GameplayCueParameters) -> Actor
```

X.get_instigator_actor(parameters) -> Actor
Gets the instigating actor (that holds the ability system component) of the GameplayCue

Args:
    parameters (GameplayCueParameters): 

Returns:
    Actor:

<a id="unreal.AbilitySystemLibrary.get_hit_result_from_target_data"></a>

#### get\_hit\_result\_from\_target\_data

```python
@classmethod
def get_hit_result_from_target_data(
        cls, hit_result: GameplayAbilityTargetDataHandle,
        index: int) -> HitResult
```

X.get_hit_result_from_target_data(hit_result, index) -> HitResult
Returns the hit result for a given index if it exists

Args:
    hit_result (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    HitResult:

<a id="unreal.AbilitySystemLibrary.get_hit_result"></a>

#### get\_hit\_result

```python
@classmethod
def get_hit_result(cls, parameters: GameplayCueParameters) -> HitResult
```

X.get_hit_result(parameters) -> HitResult
Returns a hit result stored in the effect context if valid

Args:
    parameters (GameplayCueParameters): 

Returns:
    HitResult:

<a id="unreal.AbilitySystemLibrary.get_gameplay_effect_ui_data"></a>

#### get\_gameplay\_effect\_ui\_data

```python
@classmethod
def get_gameplay_effect_ui_data(cls, effect_class: Class,
                                data_type: Class) -> GameplayEffectUIData
```

X.get_gameplay_effect_ui_data(effect_class, data_type) -> GameplayEffectUIData
Returns the UI data for a gameplay effect class (if any)

Args:
    effect_class (type(Class)): 
    data_type (type(Class)): 

Returns:
    GameplayEffectUIData:

<a id="unreal.AbilitySystemLibrary.get_gameplay_effect_granted_tags"></a>

#### get\_gameplay\_effect\_granted\_tags

```python
@classmethod
def get_gameplay_effect_granted_tags(
        cls, effect_class: Class) -> GameplayTagContainer
```

X.get_gameplay_effect_granted_tags(effect_class) -> GameplayTagContainer
Returns all tags that the Gameplay Effect grants to the target Actor

Args:
    effect_class (type(Class)): 

Returns:
    GameplayTagContainer:

<a id="unreal.AbilitySystemLibrary.get_gameplay_effect_from_active_effect_handle"></a>

#### get\_gameplay\_effect\_from\_active\_effect\_handle

```python
@classmethod
def get_gameplay_effect_from_active_effect_handle(
        cls, active_handle: ActiveGameplayEffectHandle) -> GameplayEffect
```

X.get_gameplay_effect_from_active_effect_handle(active_handle) -> GameplayEffect
Returns the Gameplay Effect CDO from an active handle.
This reference should be considered read only,
but you can use it to read additional Gameplay Effect info, such as icon, description, etc.

Args:
    active_handle (ActiveGameplayEffectHandle): 

Returns:
    GameplayEffect:

<a id="unreal.AbilitySystemLibrary.get_gameplay_effect_asset_tags"></a>

#### get\_gameplay\_effect\_asset\_tags

```python
@classmethod
def get_gameplay_effect_asset_tags(
        cls, effect_class: Class) -> GameplayTagContainer
```

X.get_gameplay_effect_asset_tags(effect_class) -> GameplayTagContainer
Returns all tags that the Gameplay Effect *has* (that denote the GE Asset itself) and *does not* grant to any Actor.

Args:
    effect_class (type(Class)): 

Returns:
    GameplayTagContainer:

<a id="unreal.AbilitySystemLibrary.get_gameplay_cue_end_location_and_normal"></a>

#### get\_gameplay\_cue\_end\_location\_and\_normal

```python
@classmethod
def get_gameplay_cue_end_location_and_normal(
        cls, target_actor: Actor,
        parameters: GameplayCueParameters) -> Optional[Tuple[Vector, Vector]]
```

X.get_gameplay_cue_end_location_and_normal(target_actor, parameters) -> (location=Vector, normal=Vector) or None
Gets the best end location and normal for this gameplay cue. If there is hit result data, it will return this. Otherwise it will return the target actor's location/rotation. If none of this is available, it will return false.

Args:
    target_actor (Actor): 
    parameters (GameplayCueParameters): 

Returns:
    tuple or None: 

    location (Vector): 

    normal (Vector):

<a id="unreal.AbilitySystemLibrary.get_gameplay_cue_direction"></a>

#### get\_gameplay\_cue\_direction

```python
@classmethod
def get_gameplay_cue_direction(
        cls, target_actor: Actor,
        parameters: GameplayCueParameters) -> Optional[Vector]
```

X.get_gameplay_cue_direction(target_actor, parameters) -> Vector or None
Gets the best normalized effect direction for this gameplay cue. This is useful for effects that require the direction of an enemy attack. Returns true if a valid direction could be calculated.

Args:
    target_actor (Actor): 
    parameters (GameplayCueParameters): 

Returns:
    Vector or None: 

    direction (Vector):

<a id="unreal.AbilitySystemLibrary.get_gameplay_ability_from_spec_handle"></a>

#### get\_gameplay\_ability\_from\_spec\_handle

```python
@classmethod
def get_gameplay_ability_from_spec_handle(
    cls, ability_system: AbilitySystemComponent,
    ability_spec_handle: GameplayAbilitySpecHandle
) -> Tuple[GameplayAbility, bool]
```

X.get_gameplay_ability_from_spec_handle(ability_system, ability_spec_handle) -> (GameplayAbility, is_instance=bool)
Provides the Gameplay Ability object associated with an Ability Spec Handle
This can be either an instanced ability, or in the case of shared abilities, the Class Default Object

Args:
    ability_system (AbilitySystemComponent): 
    ability_spec_handle (GameplayAbilitySpecHandle): 

Returns:
    bool: Pointer to the Gameplay Ability object

    is_instance (bool): Set to true if this is an instanced ability instead of a shared CDO

<a id="unreal.AbilitySystemLibrary.get_float_attribute_from_ability_system_component"></a>

#### get\_float\_attribute\_from\_ability\_system\_component

```python
@classmethod
def get_float_attribute_from_ability_system_component(
        cls, ability_system: AbilitySystemComponent,
        attribute: GameplayAttribute) -> Tuple[float, bool]
```

X.get_float_attribute_from_ability_system_component(ability_system, attribute) -> (float, successfully_found_attribute=bool)
Returns the value of Attribute from the ability system component AbilitySystem.

Args:
    ability_system (AbilitySystemComponent): 
    attribute (GameplayAttribute): 

Returns:
    bool: 

    successfully_found_attribute (bool):

<a id="unreal.AbilitySystemLibrary.get_float_attribute_base_from_ability_system_component"></a>

#### get\_float\_attribute\_base\_from\_ability\_system\_component

```python
@classmethod
def get_float_attribute_base_from_ability_system_component(
        cls, ability_system_component: AbilitySystemComponent,
        attribute: GameplayAttribute) -> Tuple[float, bool]
```

X.get_float_attribute_base_from_ability_system_component(ability_system_component, attribute) -> (float, successfully_found_attribute=bool)
Returns the base value of Attribute from the ability system component AbilitySystemComponent.

Args:
    ability_system_component (AbilitySystemComponent): 
    attribute (GameplayAttribute): 

Returns:
    bool: 

    successfully_found_attribute (bool):

<a id="unreal.AbilitySystemLibrary.get_float_attribute_base"></a>

#### get\_float\_attribute\_base

```python
@classmethod
def get_float_attribute_base(
        cls, actor: Actor, attribute: GameplayAttribute) -> Tuple[float, bool]
```

X.get_float_attribute_base(actor, attribute) -> (float, successfully_found_attribute=bool)
Returns the base value of Attribute from the ability system component belonging to Actor.

Args:
    actor (Actor): 
    attribute (GameplayAttribute): 

Returns:
    bool: 

    successfully_found_attribute (bool):

<a id="unreal.AbilitySystemLibrary.get_float_attribute"></a>

#### get\_float\_attribute

```python
@classmethod
def get_float_attribute(cls, actor: Actor,
                        attribute: GameplayAttribute) -> Tuple[float, bool]
```

X.get_float_attribute(actor, attribute) -> (float, successfully_found_attribute=bool)
Returns the value of Attribute from the ability system component belonging to Actor.

Args:
    actor (Actor): 
    attribute (GameplayAttribute): 

Returns:
    bool: 

    successfully_found_attribute (bool):

<a id="unreal.AbilitySystemLibrary.get_effect_context"></a>

#### get\_effect\_context

```python
@classmethod
def get_effect_context(
        cls,
        spec_handle: GameplayEffectSpecHandle) -> GameplayEffectContextHandle
```

X.get_effect_context(spec_handle) -> GameplayEffectContextHandle
Gets the GameplayEffectSpec's effect context handle

Args:
    spec_handle (GameplayEffectSpecHandle): 

Returns:
    GameplayEffectContextHandle:

<a id="unreal.AbilitySystemLibrary.get_debug_string_from_gameplay_attribute"></a>

#### get\_debug\_string\_from\_gameplay\_attribute

```python
@classmethod
def get_debug_string_from_gameplay_attribute(
        cls, attribute: GameplayAttribute) -> str
```

X.get_debug_string_from_gameplay_attribute(attribute) -> str
Returns FString representation of a gameplay attribute's set class and name, in the form of AttrSetName.AttrName (or just AttrName if not part of a set).

Args:
    attribute (GameplayAttribute): 

Returns:
    str:

<a id="unreal.AbilitySystemLibrary.get_data_count_from_target_data"></a>

#### get\_data\_count\_from\_target\_data

```python
@classmethod
def get_data_count_from_target_data(
        cls, target_data: GameplayAbilityTargetDataHandle) -> int
```

X.get_data_count_from_target_data(target_data) -> int32
Returns number of target data objects, not necessarily number of distinct targets

Args:
    target_data (GameplayAbilityTargetDataHandle): 

Returns:
    int32:

<a id="unreal.AbilitySystemLibrary.get_all_linked_gameplay_effect_spec_handles"></a>

#### get\_all\_linked\_gameplay\_effect\_spec\_handles

```python
@classmethod
def get_all_linked_gameplay_effect_spec_handles(
        cls, spec_handle: GameplayEffectSpecHandle
) -> Array[GameplayEffectSpecHandle]
```

X.get_all_linked_gameplay_effect_spec_handles(spec_handle) -> Array[GameplayEffectSpecHandle]
Get All Linked Gameplay Effect Spec Handles
deprecated: Function 'GetAllLinkedGameplayEffectSpecHandles' is deprecated.

Args:
    spec_handle (GameplayEffectSpecHandle): 

Returns:
    Array[GameplayEffectSpecHandle]:

<a id="unreal.AbilitySystemLibrary.get_all_actors_from_target_data"></a>

#### get\_all\_actors\_from\_target\_data

```python
@classmethod
def get_all_actors_from_target_data(
        cls, target_data: GameplayAbilityTargetDataHandle) -> Array[Actor]
```

X.get_all_actors_from_target_data(target_data) -> Array[Actor]
Returns all actors targeted

Args:
    target_data (GameplayAbilityTargetDataHandle): 

Returns:
    Array[Actor]:

<a id="unreal.AbilitySystemLibrary.get_actors_from_target_data"></a>

#### get\_actors\_from\_target\_data

```python
@classmethod
def get_actors_from_target_data(cls,
                                target_data: GameplayAbilityTargetDataHandle,
                                index: int) -> Array[Actor]
```

X.get_actors_from_target_data(target_data, index) -> Array[Actor]
Returns all actors targeted, for a given index

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    index (int32): 

Returns:
    Array[Actor]:

<a id="unreal.AbilitySystemLibrary.get_actor_count"></a>

#### get\_actor\_count

```python
@classmethod
def get_actor_count(cls, parameters: GameplayCueParameters) -> int
```

X.get_actor_count(parameters) -> int32
Returns number of actors stored in the Effect Context used by this cue

Args:
    parameters (GameplayCueParameters): 

Returns:
    int32:

<a id="unreal.AbilitySystemLibrary.get_actor_by_index"></a>

#### get\_actor\_by\_index

```python
@classmethod
def get_actor_by_index(cls, parameters: GameplayCueParameters,
                       index: int) -> Actor
```

X.get_actor_by_index(parameters, index) -> Actor
Returns actor stored in the Effect Context used by this cue

Args:
    parameters (GameplayCueParameters): 
    index (int32): 

Returns:
    Actor:

<a id="unreal.AbilitySystemLibrary.get_active_gameplay_effect_total_duration"></a>

#### get\_active\_gameplay\_effect\_total\_duration

```python
@classmethod
def get_active_gameplay_effect_total_duration(
        cls, active_handle: ActiveGameplayEffectHandle) -> float
```

X.get_active_gameplay_effect_total_duration(active_handle) -> float
Returns the total duration for a given GameplayEffect

Args:
    active_handle (ActiveGameplayEffectHandle): 

Returns:
    float:

<a id="unreal.AbilitySystemLibrary.get_active_gameplay_effect_start_time"></a>

#### get\_active\_gameplay\_effect\_start\_time

```python
@classmethod
def get_active_gameplay_effect_start_time(
        cls, active_handle: ActiveGameplayEffectHandle) -> float
```

X.get_active_gameplay_effect_start_time(active_handle) -> float
Returns the start time (time which the GE was added) for a given GameplayEffect

Args:
    active_handle (ActiveGameplayEffectHandle): 

Returns:
    float:

<a id="unreal.AbilitySystemLibrary.get_active_gameplay_effect_stack_limit_count"></a>

#### get\_active\_gameplay\_effect\_stack\_limit\_count

```python
@classmethod
def get_active_gameplay_effect_stack_limit_count(
        cls, active_handle: ActiveGameplayEffectHandle) -> int
```

X.get_active_gameplay_effect_stack_limit_count(active_handle) -> int32
Returns stack limit count of an active Gameplay Effect. Will return 0 if the GameplayEffect is no longer valid.

Args:
    active_handle (ActiveGameplayEffectHandle): 

Returns:
    int32:

<a id="unreal.AbilitySystemLibrary.get_active_gameplay_effect_stack_count"></a>

#### get\_active\_gameplay\_effect\_stack\_count

```python
@classmethod
def get_active_gameplay_effect_stack_count(
        cls, active_handle: ActiveGameplayEffectHandle) -> int
```

X.get_active_gameplay_effect_stack_count(active_handle) -> int32
Returns current stack count of an active Gameplay Effect. Will return 0 if the GameplayEffect is no longer valid.

Args:
    active_handle (ActiveGameplayEffectHandle): 

Returns:
    int32:

<a id="unreal.AbilitySystemLibrary.get_active_gameplay_effect_remaining_duration"></a>

#### get\_active\_gameplay\_effect\_remaining\_duration

```python
@classmethod
def get_active_gameplay_effect_remaining_duration(
        cls, world_context_object: Object,
        active_handle: ActiveGameplayEffectHandle) -> float
```

X.get_active_gameplay_effect_remaining_duration(world_context_object, active_handle) -> float
Returns the total duration for a given GameplayEffect, basically ExpectedEndTime - Current Time

Args:
    world_context_object (Object): 
    active_handle (ActiveGameplayEffectHandle): 

Returns:
    float:

<a id="unreal.AbilitySystemLibrary.get_active_gameplay_effect_expected_end_time"></a>

#### get\_active\_gameplay\_effect\_expected\_end\_time

```python
@classmethod
def get_active_gameplay_effect_expected_end_time(
        cls, active_handle: ActiveGameplayEffectHandle) -> float
```

X.get_active_gameplay_effect_expected_end_time(active_handle) -> float
Returns the expected end time (when we think the GE will expire) for a given GameplayEffect (note someone could remove or change it before that happens!)

Args:
    active_handle (ActiveGameplayEffectHandle): 

Returns:
    float:

<a id="unreal.AbilitySystemLibrary.get_active_gameplay_effect_debug_string"></a>

#### get\_active\_gameplay\_effect\_debug\_string

```python
@classmethod
def get_active_gameplay_effect_debug_string(
        cls, active_handle: ActiveGameplayEffectHandle) -> str
```

X.get_active_gameplay_effect_debug_string(active_handle) -> str
Returns a debug string for display

Args:
    active_handle (ActiveGameplayEffectHandle): 

Returns:
    str:

<a id="unreal.AbilitySystemLibrary.get_ability_system_component"></a>

#### get\_ability\_system\_component

```python
@classmethod
def get_ability_system_component(cls, actor: Actor) -> AbilitySystemComponent
```

X.get_ability_system_component(actor) -> AbilitySystemComponent
Tries to find an ability system component on the actor, will use AbilitySystemInterface or fall back to a component search

Args:
    actor (Actor): 

Returns:
    AbilitySystemComponent:

<a id="unreal.AbilitySystemLibrary.forward_gameplay_cue_to_target"></a>

#### forward\_gameplay\_cue\_to\_target

```python
@classmethod
def forward_gameplay_cue_to_target(cls,
                                   target_cue_interface: GameplayCueInterface,
                                   event_type: GameplayCueEvent,
                                   parameters: GameplayCueParameters) -> None
```

X.forward_gameplay_cue_to_target(target_cue_interface, event_type, parameters) -> None
Forwards the gameplay cue to another gameplay cue interface object

Args:
    target_cue_interface (GameplayCueInterface): 
    event_type (GameplayCueEvent): 
    parameters (GameplayCueParameters):

<a id="unreal.AbilitySystemLibrary.filter_target_data"></a>

#### filter\_target\_data

```python
@classmethod
def filter_target_data(
    cls, target_data_handle: GameplayAbilityTargetDataHandle,
    actor_filter_class: GameplayTargetDataFilterHandle
) -> GameplayAbilityTargetDataHandle
```

X.filter_target_data(target_data_handle, actor_filter_class) -> GameplayAbilityTargetDataHandle
Create a new target data handle with filtration performed on the data

Args:
    target_data_handle (GameplayAbilityTargetDataHandle): 
    actor_filter_class (GameplayTargetDataFilterHandle): 

Returns:
    GameplayAbilityTargetDataHandle:

<a id="unreal.AbilitySystemLibrary.evaluate_attribute_value_with_tags_and_base"></a>

#### evaluate\_attribute\_value\_with\_tags\_and\_base

```python
@classmethod
def evaluate_attribute_value_with_tags_and_base(
        cls, ability_system: AbilitySystemComponent,
        attribute: GameplayAttribute, source_tags: GameplayTagContainer,
        target_tags: GameplayTagContainer,
        base_value: float) -> Tuple[float, bool]
```

X.evaluate_attribute_value_with_tags_and_base(ability_system, attribute, source_tags, target_tags, base_value) -> (float, success=bool)
Returns the value of Attribute from the ability system component AbilitySystem after evaluating it with source and target tags using the passed in base value instead of the real base value. bSuccess indicates the success or failure of this operation.

Args:
    ability_system (AbilitySystemComponent): 
    attribute (GameplayAttribute): 
    source_tags (GameplayTagContainer): 
    target_tags (GameplayTagContainer): 
    base_value (float): 

Returns:
    bool: 

    success (bool):

<a id="unreal.AbilitySystemLibrary.evaluate_attribute_value_with_tags"></a>

#### evaluate\_attribute\_value\_with\_tags

```python
@classmethod
def evaluate_attribute_value_with_tags(
        cls, ability_system: AbilitySystemComponent,
        attribute: GameplayAttribute, source_tags: GameplayTagContainer,
        target_tags: GameplayTagContainer) -> Tuple[float, bool]
```

X.evaluate_attribute_value_with_tags(ability_system, attribute, source_tags, target_tags) -> (float, success=bool)
Returns the value of Attribute from the ability system component AbilitySystem after evaluating it with source and target tags. bSuccess indicates the success or failure of this operation.

Args:
    ability_system (AbilitySystemComponent): 
    attribute (GameplayAttribute): 
    source_tags (GameplayTagContainer): 
    target_tags (GameplayTagContainer): 

Returns:
    bool: 

    success (bool):

<a id="unreal.AbilitySystemLibrary.equal_equal_gameplay_attribute_gameplay_attribute"></a>

#### equal\_equal\_gameplay\_attribute\_gameplay\_attribute

```python
@classmethod
def equal_equal_gameplay_attribute_gameplay_attribute(
        cls, attribute_a: GameplayAttribute,
        attribute_b: GameplayAttribute) -> bool
```

X.equal_equal_gameplay_attribute_gameplay_attribute(attribute_a, attribute_b) -> bool
Simple equality operator for gameplay attributes

Args:
    attribute_a (GameplayAttribute): 
    attribute_b (GameplayAttribute): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.equal_equal_gameplay_ability_spec_handle"></a>

#### equal\_equal\_gameplay\_ability\_spec\_handle

```python
@classmethod
def equal_equal_gameplay_ability_spec_handle(
        cls, a: GameplayAbilitySpecHandle,
        b: GameplayAbilitySpecHandle) -> bool
```

X.equal_equal_gameplay_ability_spec_handle(a, b) -> bool
Equality operator for two Gameplay Ability Spec Handles

Args:
    a (GameplayAbilitySpecHandle): 
    b (GameplayAbilitySpecHandle): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.equal_equal_active_gameplay_effect_handle"></a>

#### equal\_equal\_active\_gameplay\_effect\_handle

```python
@classmethod
def equal_equal_active_gameplay_effect_handle(
        cls, a: ActiveGameplayEffectHandle,
        b: ActiveGameplayEffectHandle) -> bool
```

X.equal_equal_active_gameplay_effect_handle(a, b) -> bool
Equality operator for two Active Gameplay Effect Handles

Args:
    a (ActiveGameplayEffectHandle): 
    b (ActiveGameplayEffectHandle): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.effect_context_set_origin"></a>

#### effect\_context\_set\_origin

```python
@classmethod
def effect_context_set_origin(cls, effect_context: GameplayEffectContextHandle,
                              origin: Vector) -> None
```

X.effect_context_set_origin(effect_context, origin) -> None
Sets the location the effect originated from

Args:
    effect_context (GameplayEffectContextHandle): 
    origin (Vector):

<a id="unreal.AbilitySystemLibrary.effect_context_is_valid"></a>

#### effect\_context\_is\_valid

```python
@classmethod
def effect_context_is_valid(
        cls, effect_context: GameplayEffectContextHandle) -> bool
```

X.effect_context_is_valid(effect_context) -> bool
Returns true if this context has ever been initialized

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.effect_context_is_instigator_locally_controlled"></a>

#### effect\_context\_is\_instigator\_locally\_controlled

```python
@classmethod
def effect_context_is_instigator_locally_controlled(
        cls, effect_context: GameplayEffectContextHandle) -> bool
```

X.effect_context_is_instigator_locally_controlled(effect_context) -> bool
Returns true if the ability system component that instigated this is locally controlled

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.effect_context_has_hit_result"></a>

#### effect\_context\_has\_hit\_result

```python
@classmethod
def effect_context_has_hit_result(
        cls, effect_context: GameplayEffectContextHandle) -> bool
```

X.effect_context_has_hit_result(effect_context) -> bool
Returns true if there is a valid hit result inside the effect context

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.effect_context_get_source_object"></a>

#### effect\_context\_get\_source\_object

```python
@classmethod
def effect_context_get_source_object(
        cls, effect_context: GameplayEffectContextHandle) -> Object
```

X.effect_context_get_source_object(effect_context) -> Object
Gets the source object of the effect.

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    Object:

<a id="unreal.AbilitySystemLibrary.effect_context_get_original_instigator_actor"></a>

#### effect\_context\_get\_original\_instigator\_actor

```python
@classmethod
def effect_context_get_original_instigator_actor(
        cls, effect_context: GameplayEffectContextHandle) -> Actor
```

X.effect_context_get_original_instigator_actor(effect_context) -> Actor
Gets the original instigator actor that started the chain of events to cause this effect

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    Actor:

<a id="unreal.AbilitySystemLibrary.effect_context_get_origin"></a>

#### effect\_context\_get\_origin

```python
@classmethod
def effect_context_get_origin(
        cls, effect_context: GameplayEffectContextHandle) -> Vector
```

X.effect_context_get_origin(effect_context) -> Vector
Gets the location the effect originated from

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    Vector:

<a id="unreal.AbilitySystemLibrary.effect_context_get_instigator_actor"></a>

#### effect\_context\_get\_instigator\_actor

```python
@classmethod
def effect_context_get_instigator_actor(
        cls, effect_context: GameplayEffectContextHandle) -> Actor
```

X.effect_context_get_instigator_actor(effect_context) -> Actor
Gets the instigating actor (that holds the ability system component) of the EffectContext

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    Actor:

<a id="unreal.AbilitySystemLibrary.effect_context_get_hit_result"></a>

#### effect\_context\_get\_hit\_result

```python
@classmethod
def effect_context_get_hit_result(
        cls, effect_context: GameplayEffectContextHandle) -> HitResult
```

X.effect_context_get_hit_result(effect_context) -> HitResult
Extracts a hit result from the effect context if it is set

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    HitResult:

<a id="unreal.AbilitySystemLibrary.effect_context_get_effect_causer"></a>

#### effect\_context\_get\_effect\_causer

```python
@classmethod
def effect_context_get_effect_causer(
        cls, effect_context: GameplayEffectContextHandle) -> Actor
```

X.effect_context_get_effect_causer(effect_context) -> Actor
Gets the physical actor that caused the effect, possibly a projectile or weapon

Args:
    effect_context (GameplayEffectContextHandle): 

Returns:
    Actor:

<a id="unreal.AbilitySystemLibrary.effect_context_add_hit_result"></a>

#### effect\_context\_add\_hit\_result

```python
@classmethod
def effect_context_add_hit_result(cls,
                                  effect_context: GameplayEffectContextHandle,
                                  hit_result: HitResult, reset: bool) -> None
```

X.effect_context_add_hit_result(effect_context, hit_result, reset) -> None
Adds a hit result to the effect context

Args:
    effect_context (GameplayEffectContextHandle): 
    hit_result (HitResult): 
    reset (bool):

<a id="unreal.AbilitySystemLibrary.does_target_data_contain_actor"></a>

#### does\_target\_data\_contain\_actor

```python
@classmethod
def does_target_data_contain_actor(
        cls, target_data: GameplayAbilityTargetDataHandle, index: int,
        actor: Actor) -> bool
```

X.does_target_data_contain_actor(target_data, index, actor) -> bool
Returns true if the given TargetData has the actor passed in targeted

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    index (int32): 
    actor (Actor): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.does_gameplay_cue_meet_tag_requirements"></a>

#### does\_gameplay\_cue\_meet\_tag\_requirements

```python
@classmethod
def does_gameplay_cue_meet_tag_requirements(
        cls, parameters: GameplayCueParameters,
        source_tag_reqs: GameplayTagRequirements,
        target_tag_reqs: GameplayTagRequirements) -> bool
```

X.does_gameplay_cue_meet_tag_requirements(parameters, source_tag_reqs, target_tag_reqs) -> bool
Returns true if the aggregated source and target tags from the effect spec meets the tag requirements

Args:
    parameters (GameplayCueParameters): 
    source_tag_reqs (GameplayTagRequirements): 
    target_tag_reqs (GameplayTagRequirements): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.clone_spec_handle"></a>

#### clone\_spec\_handle

```python
@classmethod
def clone_spec_handle(
    cls, new_instigator: Actor, effect_causer: Actor,
    gameplay_effect_spec_handle_clone: GameplayEffectSpecHandle
) -> GameplayEffectSpecHandle
```

X.clone_spec_handle(new_instigator, effect_causer, gameplay_effect_spec_handle_clone) -> GameplayEffectSpecHandle
Create a spec handle, cloning another

Args:
    new_instigator (Actor): 
    effect_causer (Actor): 
    gameplay_effect_spec_handle_clone (GameplayEffectSpecHandle): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.assign_tag_set_by_caller_magnitude"></a>

#### assign\_tag\_set\_by\_caller\_magnitude

```python
@classmethod
def assign_tag_set_by_caller_magnitude(
        cls, spec_handle: GameplayEffectSpecHandle, data_tag: GameplayTag,
        magnitude: float) -> GameplayEffectSpecHandle
```

X.assign_tag_set_by_caller_magnitude(spec_handle, data_tag, magnitude) -> GameplayEffectSpecHandle
Sets a gameplay tag Set By Caller magnitude value

Args:
    spec_handle (GameplayEffectSpecHandle): 
    data_tag (GameplayTag): 
    magnitude (float): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.assign_set_by_caller_magnitude"></a>

#### assign\_set\_by\_caller\_magnitude

```python
@classmethod
def assign_set_by_caller_magnitude(
        cls, spec_handle: GameplayEffectSpecHandle, data_name: Name,
        magnitude: float) -> GameplayEffectSpecHandle
```

X.assign_set_by_caller_magnitude(spec_handle, data_name, magnitude) -> GameplayEffectSpecHandle
Sets a raw name Set By Caller magnitude value, the tag version should normally be used

Args:
    spec_handle (GameplayEffectSpecHandle): 
    data_name (Name): 
    magnitude (float): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.append_target_data_handle"></a>

#### append\_target\_data\_handle

```python
@classmethod
def append_target_data_handle(
    cls, target_handle: GameplayAbilityTargetDataHandle,
    handle_to_add: GameplayAbilityTargetDataHandle
) -> GameplayAbilityTargetDataHandle
```

X.append_target_data_handle(target_handle, handle_to_add) -> GameplayAbilityTargetDataHandle
Copies targets from HandleToAdd to TargetHandle

Args:
    target_handle (GameplayAbilityTargetDataHandle): 
    handle_to_add (GameplayAbilityTargetDataHandle): 

Returns:
    GameplayAbilityTargetDataHandle:

<a id="unreal.AbilitySystemLibrary.add_loose_gameplay_tags"></a>

#### add\_loose\_gameplay\_tags

```python
@classmethod
def add_loose_gameplay_tags(cls,
                            actor: Actor,
                            gameplay_tags: GameplayTagContainer,
                            should_replicate: bool = False) -> bool
```

X.add_loose_gameplay_tags(actor, gameplay_tags, should_replicate=False) -> bool
Manually adds a set of tags to a given actor, and optionally replicates them.

Args:
    actor (Actor): 
    gameplay_tags (GameplayTagContainer): 
    should_replicate (bool): 

Returns:
    bool:

<a id="unreal.AbilitySystemLibrary.add_linked_gameplay_effect_spec"></a>

#### add\_linked\_gameplay\_effect\_spec

```python
@classmethod
def add_linked_gameplay_effect_spec(
    cls, spec_handle: GameplayEffectSpecHandle,
    linked_gameplay_effect_spec: GameplayEffectSpecHandle
) -> GameplayEffectSpecHandle
```

X.add_linked_gameplay_effect_spec(spec_handle, linked_gameplay_effect_spec) -> GameplayEffectSpecHandle
Add Linked Gameplay Effect Spec
deprecated: Function 'AddLinkedGameplayEffectSpec' is deprecated.

Args:
    spec_handle (GameplayEffectSpecHandle): 
    linked_gameplay_effect_spec (GameplayEffectSpecHandle): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.add_linked_gameplay_effect"></a>

#### add\_linked\_gameplay\_effect

```python
@classmethod
def add_linked_gameplay_effect(
        cls, spec_handle: GameplayEffectSpecHandle,
        linked_gameplay_effect: Class) -> GameplayEffectSpecHandle
```

X.add_linked_gameplay_effect(spec_handle, linked_gameplay_effect) -> GameplayEffectSpecHandle
Add Linked Gameplay Effect
deprecated: Function 'AddLinkedGameplayEffect' is deprecated.

Args:
    spec_handle (GameplayEffectSpecHandle): 
    linked_gameplay_effect (type(Class)): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.add_granted_tags"></a>

#### add\_granted\_tags

```python
@classmethod
def add_granted_tags(
        cls, spec_handle: GameplayEffectSpecHandle,
        new_gameplay_tags: GameplayTagContainer) -> GameplayEffectSpecHandle
```

X.add_granted_tags(spec_handle, new_gameplay_tags) -> GameplayEffectSpecHandle
This instance of the effect will now grant NewGameplayTags to the object that this effect is applied to

Args:
    spec_handle (GameplayEffectSpecHandle): 
    new_gameplay_tags (GameplayTagContainer): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.add_granted_tag"></a>

#### add\_granted\_tag

```python
@classmethod
def add_granted_tag(cls, spec_handle: GameplayEffectSpecHandle,
                    new_gameplay_tag: GameplayTag) -> GameplayEffectSpecHandle
```

X.add_granted_tag(spec_handle, new_gameplay_tag) -> GameplayEffectSpecHandle
This instance of the effect will now grant NewGameplayTag to the object that this effect is applied to

Args:
    spec_handle (GameplayEffectSpecHandle): 
    new_gameplay_tag (GameplayTag): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.add_asset_tags"></a>

#### add\_asset\_tags

```python
@classmethod
def add_asset_tags(
        cls, spec_handle: GameplayEffectSpecHandle,
        new_gameplay_tags: GameplayTagContainer) -> GameplayEffectSpecHandle
```

X.add_asset_tags(spec_handle, new_gameplay_tags) -> GameplayEffectSpecHandle
Adds NewGameplayTags to this instance of the effect

Args:
    spec_handle (GameplayEffectSpecHandle): 
    new_gameplay_tags (GameplayTagContainer): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.add_asset_tag"></a>

#### add\_asset\_tag

```python
@classmethod
def add_asset_tag(cls, spec_handle: GameplayEffectSpecHandle,
                  new_gameplay_tag: GameplayTag) -> GameplayEffectSpecHandle
```

X.add_asset_tag(spec_handle, new_gameplay_tag) -> GameplayEffectSpecHandle
Adds NewGameplayTag to this instance of the effect

Args:
    spec_handle (GameplayEffectSpecHandle): 
    new_gameplay_tag (GameplayTag): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemLibrary.ability_target_data_from_locations"></a>

#### ability\_target\_data\_from\_locations

```python
@classmethod
def ability_target_data_from_locations(
    cls, source_location: GameplayAbilityTargetingLocationInfo,
    target_location: GameplayAbilityTargetingLocationInfo
) -> GameplayAbilityTargetDataHandle
```

X.ability_target_data_from_locations(source_location, target_location) -> GameplayAbilityTargetDataHandle
Creates a target data with a source and destination location

Args:
    source_location (GameplayAbilityTargetingLocationInfo): 
    target_location (GameplayAbilityTargetingLocationInfo): 

Returns:
    GameplayAbilityTargetDataHandle:

<a id="unreal.AbilitySystemLibrary.ability_target_data_from_hit_result"></a>

#### ability\_target\_data\_from\_hit\_result

```python
@classmethod
def ability_target_data_from_hit_result(
        cls, hit_result: HitResult) -> GameplayAbilityTargetDataHandle
```

X.ability_target_data_from_hit_result(hit_result) -> GameplayAbilityTargetDataHandle
Creates a target data with a single hit result

Args:
    hit_result (HitResult): 

Returns:
    GameplayAbilityTargetDataHandle:

<a id="unreal.AbilitySystemLibrary.ability_target_data_from_actor_array"></a>

#### ability\_target\_data\_from\_actor\_array

```python
@classmethod
def ability_target_data_from_actor_array(
        cls, actor_array: Array[Actor],
        one_target_per_handle: bool) -> GameplayAbilityTargetDataHandle
```

X.ability_target_data_from_actor_array(actor_array, one_target_per_handle) -> GameplayAbilityTargetDataHandle
Creates actor array target data

Args:
    actor_array (Array[Actor]): 
    one_target_per_handle (bool): 

Returns:
    GameplayAbilityTargetDataHandle:

<a id="unreal.AbilitySystemLibrary.ability_target_data_from_actor"></a>

#### ability\_target\_data\_from\_actor

```python
@classmethod
def ability_target_data_from_actor(
        cls, actor: Actor) -> GameplayAbilityTargetDataHandle
```

X.ability_target_data_from_actor(actor) -> GameplayAbilityTargetDataHandle
Creates single actor target data

Args:
    actor (Actor): 

Returns:
    GameplayAbilityTargetDataHandle:

<a id="unreal.AbilitySystemComponent"></a>