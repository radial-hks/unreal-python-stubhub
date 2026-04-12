## AbilitySystemComponent Objects

```python
class AbilitySystemComponent(GameplayTasksComponent)
```

The core ActorComponent for interfacing with the GameplayAbilities System

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilitySystemComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``activatable_abilities`` (GameplayAbilitySpecContainer):  [Read-Write] The abilities we can activate.
          -This will include CDOs for non instanced abilities and per-execution instanced abilities.
          -Actor-instanced abilities will be the actual instance (not CDO)

  This array is not vital for things to work. It is a convenience thing for 'giving abilities to the actor'. But abilities could also work on things
  without an AbilitySystemComponent. For example an ability could be written to execute on a StaticMeshActor. As long as the ability doesn't require
  instancing or anything else that the AbilitySystemComponent would provide, then it doesn't need the component to function.
- ``affected_anim_instance_tag`` (Name):  [Read-Write] The linked Anim Instance that this component will play montages in. Use NAME_None for the main anim instance.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``default_starting_data`` (Array[AttributeDefaults]):  [Read-Write]
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_claimed_resources_change`` (OnClaimedResourcesChangeSignature):  [Read-Write]
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.AbilitySystemComponent.affected_anim_instance_tag"></a>

#### affected\_anim\_instance\_tag

```python
@property
def affected_anim_instance_tag() -> Name
```

(Name):  [Read-Write] The linked Anim Instance that this component will play montages in. Use NAME_None for the main anim instance.

<a id="unreal.AbilitySystemComponent.affected_anim_instance_tag"></a>

#### affected\_anim\_instance\_tag

```python
@affected_anim_instance_tag.setter
def affected_anim_instance_tag(value: Name) -> None
```

<a id="unreal.AbilitySystemComponent.activatable_abilities"></a>

#### activatable\_abilities

```python
@property
def activatable_abilities() -> GameplayAbilitySpecContainer
```

(GameplayAbilitySpecContainer):  [Read-Only] The abilities we can activate.
        -This will include CDOs for non instanced abilities and per-execution instanced abilities.
        -Actor-instanced abilities will be the actual instance (not CDO)

This array is not vital for things to work. It is a convenience thing for 'giving abilities to the actor'. But abilities could also work on things
without an AbilitySystemComponent. For example an ability could be written to execute on a StaticMeshActor. As long as the ability doesn't require
instancing or anything else that the AbilitySystemComponent would provide, then it doesn't need the component to function.

<a id="unreal.AbilitySystemComponent.update_active_gameplay_effect_set_by_caller_magnitudes"></a>

#### update\_active\_gameplay\_effect\_set\_by\_caller\_magnitudes

```python
def update_active_gameplay_effect_set_by_caller_magnitudes(
        active_handle: ActiveGameplayEffectHandle,
        new_set_by_caller_values: Map[GameplayTag, float]) -> None
```

x.update_active_gameplay_effect_set_by_caller_magnitudes(active_handle, new_set_by_caller_values) -> None
Dynamically update multiple set-by-caller magnitudes for an active gameplay effect

Args:
    active_handle (ActiveGameplayEffectHandle): 
    new_set_by_caller_values (Map[GameplayTag, float]):

<a id="unreal.AbilitySystemComponent.update_active_gameplay_effect_set_by_caller_magnitude"></a>

#### update\_active\_gameplay\_effect\_set\_by\_caller\_magnitude

```python
def update_active_gameplay_effect_set_by_caller_magnitude(
        active_handle: ActiveGameplayEffectHandle,
        set_by_caller_tag: GameplayTag, new_value: float) -> None
```

x.update_active_gameplay_effect_set_by_caller_magnitude(active_handle, set_by_caller_tag, new_value) -> None
Dynamically update the set-by-caller magnitude for an active gameplay effect

Args:
    active_handle (ActiveGameplayEffectHandle): 
    set_by_caller_tag (GameplayTag): 
    new_value (float):

<a id="unreal.AbilitySystemComponent.try_activate_ability_by_class"></a>

#### try\_activate\_ability\_by\_class

```python
def try_activate_ability_by_class(
        ability_to_activate: Class,
        allow_remote_activation: bool = True) -> bool
```

x.try_activate_ability_by_class(ability_to_activate, allow_remote_activation=True) -> bool
Attempts to activate the ability that is passed in. This will check costs and requirements before doing so.
Returns true if it thinks it activated, but it may return false positives due to failure later in activation.
If bAllowRemoteActivation is true, it will remotely activate local/server abilities, if false it will only try to locally activate the ability

Args:
    ability_to_activate (type(Class)): 
    allow_remote_activation (bool): 

Returns:
    bool:

<a id="unreal.AbilitySystemComponent.try_activate_ability"></a>

#### try\_activate\_ability

```python
def try_activate_ability(ability_to_activate: GameplayAbilitySpecHandle,
                         allow_remote_activation: bool = True) -> bool
```

x.try_activate_ability(ability_to_activate, allow_remote_activation=True) -> bool
Attempts to activate the given ability, will check costs and requirements before doing so.
Returns true if it thinks it activated, but it may return false positives due to failure later in activation.
If bAllowRemoteActivation is true, it will remotely activate local/server abilities, if false it will only try to locally activate the ability

Args:
    ability_to_activate (GameplayAbilitySpecHandle): 
    allow_remote_activation (bool): 

Returns:
    bool:

<a id="unreal.AbilitySystemComponent.try_activate_abilities_by_tag"></a>

#### try\_activate\_abilities\_by\_tag

```python
def try_activate_abilities_by_tag(
        gameplay_tag_container: GameplayTagContainer,
        allow_remote_activation: bool = True) -> bool
```

x.try_activate_abilities_by_tag(gameplay_tag_container, allow_remote_activation=True) -> bool
Attempts to activate every gameplay ability that matches the given tag and DoesAbilitySatisfyTagRequirements().
Returns true if anything attempts to activate. Can activate more than one ability and the ability may fail later.
If bAllowRemoteActivation is true, it will remotely activate local/server abilities, if false it will only try to locally activate abilities.

Args:
    gameplay_tag_container (GameplayTagContainer): 
    allow_remote_activation (bool): 

Returns:
    bool:

<a id="unreal.AbilitySystemComponent.try_activate_ability_by_tag"></a>

#### try\_activate\_ability\_by\_tag

```python
def try_activate_ability_by_tag(gameplay_tag_container: GameplayTagContainer,
                                allow_remote_activation: bool = True) -> bool
```

deprecated: 'try_activate_ability_by_tag' was renamed to 'try_activate_abilities_by_tag'.

<a id="unreal.AbilitySystemComponent.target_confirm"></a>

#### target\_confirm

```python
def target_confirm() -> None
```

x.target_confirm() -> None
Any active targeting actors will be told to stop and return current targeting data

<a id="unreal.AbilitySystemComponent.target_cancel"></a>

#### target\_cancel

```python
def target_cancel() -> None
```

x.target_cancel() -> None
Any active targeting actors will be stopped and canceled, not returning any targeting data

<a id="unreal.AbilitySystemComponent.set_user_ability_activation_inhibited"></a>

#### set\_user\_ability\_activation\_inhibited

```python
def set_user_ability_activation_inhibited(new_inhibit: bool) -> None
```

x.set_user_ability_activation_inhibited(new_inhibit) -> None
Disable or Enable a local user from being able to activate abilities. This should only be used for input/UI etc related inhibition. Do not use for game mechanics.

Args:
    new_inhibit (bool):

<a id="unreal.AbilitySystemComponent.set_active_gameplay_effect_level_using_query"></a>

#### set\_active\_gameplay\_effect\_level\_using\_query

```python
def set_active_gameplay_effect_level_using_query(query: GameplayEffectQuery,
                                                 new_level: int) -> None
```

x.set_active_gameplay_effect_level_using_query(query, new_level) -> None
Updates the level of an already applied gameplay effect. The intention is that this is 'seemless' and doesnt behave like removing/reapplying

Args:
    query (GameplayEffectQuery): 
    new_level (int32):

<a id="unreal.AbilitySystemComponent.set_active_gameplay_effect_level"></a>

#### set\_active\_gameplay\_effect\_level

```python
def set_active_gameplay_effect_level(active_handle: ActiveGameplayEffectHandle,
                                     new_level: int) -> None
```

x.set_active_gameplay_effect_level(active_handle, new_level) -> None
Updates the level of an already applied gameplay effect. The intention is that this is 'seemless' and doesnt behave like removing/reapplying

Args:
    active_handle (ActiveGameplayEffectHandle): 
    new_level (int32):

<a id="unreal.AbilitySystemComponent.remove_active_gameplay_effect_by_source_effect"></a>

#### remove\_active\_gameplay\_effect\_by\_source\_effect

```python
def remove_active_gameplay_effect_by_source_effect(
        gameplay_effect: Class,
        instigator_ability_system_component: AbilitySystemComponent,
        stacks_to_remove: int = -1) -> None
```

x.remove_active_gameplay_effect_by_source_effect(gameplay_effect, instigator_ability_system_component, stacks_to_remove=-1) -> None
Remove active gameplay effects whose backing definition are the specified gameplay effect class

Args:
    gameplay_effect (type(Class)): Class of gameplay effect to remove; Does nothing if left null
    instigator_ability_system_component (AbilitySystemComponent): If specified, will only remove gameplay effects applied from this instigator ability system component
    stacks_to_remove (int32): Number of stacks to remove, -1 means remove all

<a id="unreal.AbilitySystemComponent.remove_active_gameplay_effect"></a>

#### remove\_active\_gameplay\_effect

```python
def remove_active_gameplay_effect(handle: ActiveGameplayEffectHandle,
                                  stacks_to_remove: int = -1) -> bool
```

x.remove_active_gameplay_effect(handle, stacks_to_remove=-1) -> bool
Removes GameplayEffect by Handle. StacksToRemove=-1 will remove all stacks.

Args:
    handle (ActiveGameplayEffectHandle): 
    stacks_to_remove (int32): 

Returns:
    bool:

<a id="unreal.AbilitySystemComponent.remove_active_effects_with_tags"></a>

#### remove\_active\_effects\_with\_tags

```python
def remove_active_effects_with_tags(tags: GameplayTagContainer) -> int
```

x.remove_active_effects_with_tags(tags) -> int32
Removes all active effects that contain any of the tags in Tags

Args:
    tags (GameplayTagContainer): 

Returns:
    int32:

<a id="unreal.AbilitySystemComponent.remove_active_effects_with_source_tags"></a>

#### remove\_active\_effects\_with\_source\_tags

```python
def remove_active_effects_with_source_tags(tags: GameplayTagContainer) -> int
```

x.remove_active_effects_with_source_tags(tags) -> int32
Removes all active effects with captured source tags that contain any of the tags in Tags

Args:
    tags (GameplayTagContainer): 

Returns:
    int32:

<a id="unreal.AbilitySystemComponent.remove_active_effects_with_granted_tags"></a>

#### remove\_active\_effects\_with\_granted\_tags

```python
def remove_active_effects_with_granted_tags(tags: GameplayTagContainer) -> int
```

x.remove_active_effects_with_granted_tags(tags) -> int32
Removes all active effects that grant any of the tags in Tags

Args:
    tags (GameplayTagContainer): 

Returns:
    int32:

<a id="unreal.AbilitySystemComponent.remove_active_effects_with_applied_tags"></a>

#### remove\_active\_effects\_with\_applied\_tags

```python
def remove_active_effects_with_applied_tags(tags: GameplayTagContainer) -> int
```

x.remove_active_effects_with_applied_tags(tags) -> int32
Removes all active effects that apply any of the tags in Tags

Args:
    tags (GameplayTagContainer): 

Returns:
    int32:

<a id="unreal.AbilitySystemComponent.release_input_id"></a>

#### release\_input\_id

```python
def release_input_id(input_id: int) -> None
```

x.release_input_id(input_id) -> None
Sends a local player Input Released event with the provided Input ID, notifying any bound abilities

Args:
    input_id (int32): The Input ID to match

<a id="unreal.AbilitySystemComponent.press_input_id"></a>

#### press\_input\_id

```python
def press_input_id(input_id: int) -> None
```

x.press_input_id(input_id) -> None
* Sends a local player Input Pressed event with the provided Input ID, notifying any bound abilities
*
*

Args:
    input_id (int32): The Input ID to match

<a id="unreal.AbilitySystemComponent.make_outgoing_spec"></a>

#### make\_outgoing\_spec

```python
def make_outgoing_spec(
        gameplay_effect_class: Class, level: float,
        context: GameplayEffectContextHandle) -> GameplayEffectSpecHandle
```

x.make_outgoing_spec(gameplay_effect_class, level, context) -> GameplayEffectSpecHandle
Get an outgoing GameplayEffectSpec that is ready to be applied to other things.

Args:
    gameplay_effect_class (type(Class)): 
    level (float): 
    context (GameplayEffectContextHandle): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.AbilitySystemComponent.make_effect_context"></a>

#### make\_effect\_context

```python
def make_effect_context() -> GameplayEffectContextHandle
```

x.make_effect_context() -> GameplayEffectContextHandle
Create an EffectContext for the owner of this AbilitySystemComponent

Returns:
    GameplayEffectContextHandle:

<a id="unreal.AbilitySystemComponent.get_effect_context"></a>

#### get\_effect\_context

```python
def get_effect_context() -> GameplayEffectContextHandle
```

deprecated: 'get_effect_context' was renamed to 'make_effect_context'.

<a id="unreal.AbilitySystemComponent.init_stats"></a>

#### init\_stats

```python
def init_stats(attributes: Class, data_table: DataTable) -> None
```

x.init_stats(attributes, data_table) -> None
K2 Init Stats

Args:
    attributes (type(Class)): 
    data_table (DataTable):

<a id="unreal.AbilitySystemComponent.give_ability_and_activate_once"></a>

#### give\_ability\_and\_activate\_once

```python
def give_ability_and_activate_once(
        ability_class: Class,
        level: int = 0,
        input_id: int = -1) -> GameplayAbilitySpecHandle
```

x.give_ability_and_activate_once(ability_class, level=0, input_id=-1) -> GameplayAbilitySpecHandle
Grants a Gameplay Ability, activates it once, and removes it.
This will be ignored if the actor is not authoritative.

Args:
    ability_class (type(Class)): Type of ability to grant
    level (int32): Level to grant the ability at
    input_id (int32): Input ID value to bind ability activation to.

Returns:
    GameplayAbilitySpecHandle:

<a id="unreal.AbilitySystemComponent.give_ability"></a>

#### give\_ability

```python
def give_ability(ability_class: Class,
                 level: int = 0,
                 input_id: int = -1) -> GameplayAbilitySpecHandle
```

x.give_ability(ability_class, level=0, input_id=-1) -> GameplayAbilitySpecHandle
Grants a Gameplay Ability and returns its handle.
This will be ignored if the actor is not authoritative.

Args:
    ability_class (type(Class)): Type of ability to grant
    level (int32): Level to grant the ability at
    input_id (int32): Input ID value to bind ability activation to.

Returns:
    GameplayAbilitySpecHandle:

<a id="unreal.AbilitySystemComponent.is_gameplay_cue_active"></a>

#### is\_gameplay\_cue\_active

```python
def is_gameplay_cue_active(gameplay_cue_tag: GameplayTag) -> bool
```

x.is_gameplay_cue_active(gameplay_cue_tag) -> bool
Allows polling to see if a GameplayCue is active. We expect most GameplayCue handling to be event based, but some cases we may need to check if a GameplayCue is active (Animation Blueprint for example)

Args:
    gameplay_cue_tag (GameplayTag): 

Returns:
    bool:

<a id="unreal.AbilitySystemComponent.input_confirm"></a>

#### input\_confirm

```python
def input_confirm() -> None
```

x.input_confirm() -> None
Sends a local player Input Confirm event, notifying abilities

<a id="unreal.AbilitySystemComponent.input_cancel"></a>

#### input\_cancel

```python
def input_cancel() -> None
```

x.input_cancel() -> None
Sends a local player Input Cancel event, notifying abilities

<a id="unreal.AbilitySystemComponent.get_user_ability_activation_inhibited"></a>

#### get\_user\_ability\_activation\_inhibited

```python
def get_user_ability_activation_inhibited() -> bool
```

x.get_user_ability_activation_inhibited() -> bool
This is meant to be used to inhibit activating an ability from an input perspective. (E.g., the menu is pulled up, another game mechanism is consuming all input, etc)
This should only be called on locally owned players.
This should not be used to game mechanics like silences or disables. Those should be done through gameplay effects.

Returns:
    bool:

<a id="unreal.AbilitySystemComponent.get_gameplay_tag_count"></a>

#### get\_gameplay\_tag\_count

```python
def get_gameplay_tag_count(gameplay_tag: GameplayTag) -> int
```

x.get_gameplay_tag_count(gameplay_tag) -> int32
Returns the current count of the given gameplay tag.
This includes both loose tags, and tags granted by gameplay effects and abilities.
This function can be called on the client, but it may not display the most current count on the server.

Args:
    gameplay_tag (GameplayTag): The gameplay tag to query

Returns:
    int32:

<a id="unreal.AbilitySystemComponent.get_gameplay_effect_magnitude"></a>

#### get\_gameplay\_effect\_magnitude

```python
def get_gameplay_effect_magnitude(handle: ActiveGameplayEffectHandle,
                                  attribute: GameplayAttribute) -> float
```

x.get_gameplay_effect_magnitude(handle, attribute) -> float
Raw accessor to ask the magnitude of a gameplay effect, not necessarily always correct. How should outside code (UI, etc) ask things like 'how much is this gameplay effect modifying my damage by'
(most likely we want to catch this on the backend - when damage is applied we can get a full dump/history of how the number got to where it is. But still we may need polling methods like below (how much would my damage be)

Args:
    handle (ActiveGameplayEffectHandle): 
    attribute (GameplayAttribute): 

Returns:
    float:

<a id="unreal.AbilitySystemComponent.get_gameplay_effect_count_if_loaded"></a>

#### get\_gameplay\_effect\_count\_if\_loaded

```python
def get_gameplay_effect_count_if_loaded(
        soft_source_gameplay_effect: Class,
        optional_instigator_filter_component: AbilitySystemComponent,
        enforce_on_going_check: bool = True) -> int
```

x.get_gameplay_effect_count_if_loaded(soft_source_gameplay_effect, optional_instigator_filter_component, enforce_on_going_check=True) -> int32
Get the count of the specified source effect on the ability system component. For non-stacking effects, this is the sum of all active instances.
For stacking effects, this is the sum of all valid stack counts. If an instigator is specified, only effects from that instigator are counted.

Args:
    soft_source_gameplay_effect (Class): Effect to get the count of. If this is not currently loaded, the count is 0
    optional_instigator_filter_component (AbilitySystemComponent): If specified, only count effects applied by this ability system component
    enforce_on_going_check (bool): 

Returns:
    int32: Count of the specified source effect

<a id="unreal.AbilitySystemComponent.get_gameplay_effect_count"></a>

#### get\_gameplay\_effect\_count

```python
def get_gameplay_effect_count(
        source_gameplay_effect: Class,
        optional_instigator_filter_component: AbilitySystemComponent,
        enforce_on_going_check: bool = True) -> int
```

x.get_gameplay_effect_count(source_gameplay_effect, optional_instigator_filter_component, enforce_on_going_check=True) -> int32
Get the count of the specified source effect on the ability system component. For non-stacking effects, this is the sum of all active instances.
For stacking effects, this is the sum of all valid stack counts. If an instigator is specified, only effects from that instigator are counted.

Args:
    source_gameplay_effect (type(Class)): Effect to get the count of
    optional_instigator_filter_component (AbilitySystemComponent): If specified, only count effects applied by this ability system component
    enforce_on_going_check (bool): 

Returns:
    int32: Count of the specified source effect

<a id="unreal.AbilitySystemComponent.get_gameplay_attribute_value"></a>

#### get\_gameplay\_attribute\_value

```python
def get_gameplay_attribute_value(
        attribute: GameplayAttribute) -> Tuple[float, bool]
```

x.get_gameplay_attribute_value(attribute) -> (float, found=bool)
Returns the current value of the given gameplay attribute, or zero if the attribute is not found.
NOTE: This doesn't take predicted gameplay effect modifiers into consideration, so the value may not be accurate on clients at all times.

Args:
    attribute (GameplayAttribute): The gameplay attribute to query

Returns:
    bool: 

    found (bool): Set to true if the attribute exists in this component

<a id="unreal.AbilitySystemComponent.get_attribute_set"></a>

#### get\_attribute\_set

```python
def get_attribute_set(attribute_set_class: Class) -> AttributeSet
```

x.get_attribute_set(attribute_set_class) -> AttributeSet
Returns a reference to the Attribute Set instance, if one exists in this component

Args:
    attribute_set_class (type(Class)): The type of attribute set to look for

Returns:
    AttributeSet:

<a id="unreal.AbilitySystemComponent.get_all_attributes"></a>

#### get\_all\_attributes

```python
def get_all_attributes() -> Array[GameplayAttribute]
```

x.get_all_attributes() -> Array[GameplayAttribute]
Returns a list of all attributes for this abilty system component

Returns:
    Array[GameplayAttribute]: 

    out_attributes (Array[GameplayAttribute]):

<a id="unreal.AbilitySystemComponent.get_all_abilities"></a>

#### get\_all\_abilities

```python
def get_all_abilities() -> Array[GameplayAbilitySpecHandle]
```

x.get_all_abilities() -> Array[GameplayAbilitySpecHandle]
Returns an array with all granted ability handles
NOTE: currently this doesn't include abilities that are mid-activation

Returns:
    Array[GameplayAbilitySpecHandle]: 

    out_ability_handles (Array[GameplayAbilitySpecHandle]): This array will be filled with the granted Ability Spec Handles

<a id="unreal.AbilitySystemComponent.get_active_effects_with_all_tags"></a>

#### get\_active\_effects\_with\_all\_tags

```python
def get_active_effects_with_all_tags(
        tags: GameplayTagContainer) -> Array[ActiveGameplayEffectHandle]
```

x.get_active_effects_with_all_tags(tags) -> Array[ActiveGameplayEffectHandle]
Returns list of active effects that have all of the passed in tags

Args:
    tags (GameplayTagContainer): 

Returns:
    Array[ActiveGameplayEffectHandle]:

<a id="unreal.AbilitySystemComponent.get_active_effects"></a>

#### get\_active\_effects

```python
def get_active_effects(
        query: GameplayEffectQuery) -> Array[ActiveGameplayEffectHandle]
```

x.get_active_effects(query) -> Array[ActiveGameplayEffectHandle]
Returns list of active effects, for a query

Args:
    query (GameplayEffectQuery): 

Returns:
    Array[ActiveGameplayEffectHandle]:

<a id="unreal.AbilitySystemComponent.find_all_abilities_with_tags"></a>

#### find\_all\_abilities\_with\_tags

```python
def find_all_abilities_with_tags(
        tags: GameplayTagContainer,
        exact_match: bool = True) -> Array[GameplayAbilitySpecHandle]
```

x.find_all_abilities_with_tags(tags, exact_match=True) -> Array[GameplayAbilitySpecHandle]
Returns an array with all abilities that match the provided tags

Args:
    tags (GameplayTagContainer): Gameplay Tags to match
    exact_match (bool): If true, tags must be matched exactly. Otherwise, abilities matching any of the tags will be returned

Returns:
    Array[GameplayAbilitySpecHandle]: 

    out_ability_handles (Array[GameplayAbilitySpecHandle]): This array will be filled with matching Ability Spec Handles

<a id="unreal.AbilitySystemComponent.find_all_abilities_with_input_id"></a>

#### find\_all\_abilities\_with\_input\_id

```python
def find_all_abilities_with_input_id(
        input_id: int = 0) -> Array[GameplayAbilitySpecHandle]
```

x.find_all_abilities_with_input_id(input_id=0) -> Array[GameplayAbilitySpecHandle]
Returns an array with all abilities bound to an Input ID value

Args:
    input_id (int32): The Input ID to match

Returns:
    Array[GameplayAbilitySpecHandle]: 

    out_ability_handles (Array[GameplayAbilitySpecHandle]): This array will be filled with matching Ability Spec Handles

<a id="unreal.AbilitySystemComponent.find_all_abilities_matching_query"></a>

#### find\_all\_abilities\_matching\_query

```python
def find_all_abilities_matching_query(
        query: GameplayTagQuery) -> Array[GameplayAbilitySpecHandle]
```

x.find_all_abilities_matching_query(query) -> Array[GameplayAbilitySpecHandle]
Returns an array with all abilities that match the provided Gameplay Tag Query

Args:
    query (GameplayTagQuery): Gameplay Tag Query to match

Returns:
    Array[GameplayAbilitySpecHandle]: 

    out_ability_handles (Array[GameplayAbilitySpecHandle]): This array will be filled with matching Ability Spec Handles

<a id="unreal.AbilitySystemComponent.clear_all_abilities_with_input_id"></a>

#### clear\_all\_abilities\_with\_input\_id

```python
def clear_all_abilities_with_input_id(input_id: int = 0) -> None
```

x.clear_all_abilities_with_input_id(input_id=0) -> None
Clears all abilities bound to a given Input ID
This will be ignored if the actor is not authoritative

Args:
    input_id (int32): The numeric Input ID of the abilities to remove

<a id="unreal.AbilitySystemComponent.clear_all_abilities"></a>

#### clear\_all\_abilities

```python
def clear_all_abilities() -> None
```

x.clear_all_abilities() -> None
Wipes all 'given' abilities. This will be ignored if the actor is not authoritative.

<a id="unreal.AbilitySystemComponent.clear_ability"></a>

#### clear\_ability

```python
def clear_ability(handle: GameplayAbilitySpecHandle) -> None
```

x.clear_ability(handle) -> None
Removes the specified ability.
This will be ignored if the actor is not authoritative.

Args:
    handle (GameplayAbilitySpecHandle): Ability Spec Handle of the ability we want to remove

<a id="unreal.AbilitySystemComponent.apply_gameplay_effect_to_target"></a>

#### apply\_gameplay\_effect\_to\_target

```python
def apply_gameplay_effect_to_target(
        gameplay_effect_class: Class, target: AbilitySystemComponent,
        level: float,
        context: GameplayEffectContextHandle) -> ActiveGameplayEffectHandle
```

x.apply_gameplay_effect_to_target(gameplay_effect_class, target, level, context) -> ActiveGameplayEffectHandle
Apply a gameplay effect to passed in target

Args:
    gameplay_effect_class (type(Class)): 
    target (AbilitySystemComponent): 
    level (float): 
    context (GameplayEffectContextHandle): 

Returns:
    ActiveGameplayEffectHandle:

<a id="unreal.AbilitySystemComponent.apply_gameplay_effect_to_self"></a>

#### apply\_gameplay\_effect\_to\_self

```python
def apply_gameplay_effect_to_self(
        gameplay_effect_class: Class, level: float,
        effect_context: GameplayEffectContextHandle
) -> ActiveGameplayEffectHandle
```

x.apply_gameplay_effect_to_self(gameplay_effect_class, level, effect_context) -> ActiveGameplayEffectHandle
Apply a gameplay effect to self

Args:
    gameplay_effect_class (type(Class)): 
    level (float): 
    effect_context (GameplayEffectContextHandle): 

Returns:
    ActiveGameplayEffectHandle:

<a id="unreal.AbilitySystemComponent.apply_gameplay_effect_spec_to_target"></a>

#### apply\_gameplay\_effect\_spec\_to\_target

```python
def apply_gameplay_effect_spec_to_target(
        spec_handle: GameplayEffectSpecHandle,
        target: AbilitySystemComponent) -> ActiveGameplayEffectHandle
```

x.apply_gameplay_effect_spec_to_target(spec_handle, target) -> ActiveGameplayEffectHandle
Applies a previously created gameplay effect spec to a target

Args:
    spec_handle (GameplayEffectSpecHandle): 
    target (AbilitySystemComponent): 

Returns:
    ActiveGameplayEffectHandle:

<a id="unreal.AbilitySystemComponent.apply_gameplay_effect_spec_to_self"></a>

#### apply\_gameplay\_effect\_spec\_to\_self

```python
def apply_gameplay_effect_spec_to_self(
        spec_handle: GameplayEffectSpecHandle) -> ActiveGameplayEffectHandle
```

x.apply_gameplay_effect_spec_to_self(spec_handle) -> ActiveGameplayEffectHandle
Applies a previously created gameplay effect spec to this component

Args:
    spec_handle (GameplayEffectSpecHandle): 

Returns:
    ActiveGameplayEffectHandle:

<a id="unreal.AbilitySystemComponent.has_matching_gameplay_tag"></a>

#### has\_matching\_gameplay\_tag

```python
def has_matching_gameplay_tag(tag_to_check: GameplayTag) -> bool
```

x.has_matching_gameplay_tag(tag_to_check) -> bool
Check if the asset has a gameplay tag that matches against the specified tag (expands to include parents of asset tags)

Args:
    tag_to_check (GameplayTag): Tag to check for a match

Returns:
    bool: True if the asset has a gameplay tag that matches, false if not

<a id="unreal.AbilitySystemComponent.has_any_matching_gameplay_tags"></a>

#### has\_any\_matching\_gameplay\_tags

```python
def has_any_matching_gameplay_tags(
        tag_container: GameplayTagContainer) -> bool
```

x.has_any_matching_gameplay_tags(tag_container) -> bool
Check if the asset has gameplay tags that matches against any of the specified tags (expands to include parents of asset tags)

Args:
    tag_container (GameplayTagContainer): Tag container to check for a match

Returns:
    bool: True if the asset has matches any of the gameplay tags, will be false if container is empty

<a id="unreal.AbilitySystemComponent.has_all_matching_gameplay_tags"></a>

#### has\_all\_matching\_gameplay\_tags

```python
def has_all_matching_gameplay_tags(
        tag_container: GameplayTagContainer) -> bool
```

x.has_all_matching_gameplay_tags(tag_container) -> bool
Check if the asset has gameplay tags that matches against all of the specified tags (expands to include parents of asset tags)

Args:
    tag_container (GameplayTagContainer): Tag container to check for a match

Returns:
    bool: True if the asset has matches all of the gameplay tags, will be true if container is empty

<a id="unreal.AttributeSet"></a>