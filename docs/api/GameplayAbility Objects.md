## GameplayAbility Objects

```python
class GameplayAbility(Object)
```

Abilities define custom gameplay logic that can be activated by players or external game logic

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbility.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ability_tags`` (GameplayTagContainer):  [Read-Write]
- ``ability_triggers`` (Array[AbilityTriggerData]):  [Read-Write] Triggers to determine if this ability should execute in response to an event
- ``activation_blocked_tags`` (GameplayTagContainer):  [Read-Write] This ability is blocked if the activating actor/component has any of these tags
- ``activation_owned_tags`` (GameplayTagContainer):  [Read-Write] Tags to apply to activating owner while this ability is active. These are replicated if ReplicateActivationOwnedTags is enabled in AbilitySystemGlobals.
- ``activation_required_tags`` (GameplayTagContainer):  [Read-Write] This ability can only be activated if the activating actor/component has all of these tags
- ``block_abilities_with_tag`` (GameplayTagContainer):  [Read-Write] Abilities with these tags are blocked while this ability is active
- ``cancel_abilities_with_tag`` (GameplayTagContainer):  [Read-Write] Abilities with these tags are cancelled when this ability is executed
- ``cooldown_gameplay_effect_class`` (type(Class)):  [Read-Write] This GameplayEffect represents the cooldown. It will be applied when the ability is committed and the ability cannot be used again until it is expired.
- ``cost_gameplay_effect_class`` (type(Class)):  [Read-Write] This GameplayEffect represents the cost (mana, stamina, etc) of the ability. It will be applied when the ability is committed.
- ``current_activation_info`` (GameplayAbilityActivationInfo):  [Read-Write] This is information specific to this instance of the ability. E.g, whether it is predicting, authoring, confirmed, etc.
- ``current_event_data`` (GameplayEventData):  [Read-Write] Information specific to this instance of the ability, if it was activated by an event
- ``instancing_policy`` (GameplayAbilityInstancingPolicy):  [Read-Write] How the ability is instanced when executed. This limits what an ability can do in its implementation.
- ``mark_pending_kill_on_ability_end`` (bool):  [Read-Write]
  deprecated: This is unsafe. Do not use.
- ``net_execution_policy`` (GameplayAbilityNetExecutionPolicy):  [Read-Write] How does an ability execute on the network. Does a client "ask and predict", "ask and wait", "don't ask (just do it)".
- ``net_security_policy`` (GameplayAbilityNetSecurityPolicy):  [Read-Write] What protections does this ability have? Should the client be allowed to request changes to the execution of the ability?
- ``replicate_input_directly`` (bool):  [Read-Write] If true, this ability will always replicate input press/release events to the server.
- ``replication_policy`` (GameplayAbilityReplicationPolicy):  [Read-Write] How an ability replicates state/events to everyone on the network. Replication is not required for NetExecutionPolicy.
- ``retrigger_instanced_ability`` (bool):  [Read-Write] if true, and trying to activate an already active instanced ability, end it and re-trigger it.
- ``server_respects_remote_ability_cancellation`` (bool):  [Read-Write] If this is set, the server-side version of the ability can be canceled by the client-side version. The client-side version can always be canceled by the server.
- ``source_blocked_tags`` (GameplayTagContainer):  [Read-Write] This ability is blocked if the source actor/component has any of these tags
- ``source_required_tags`` (GameplayTagContainer):  [Read-Write] This ability can only be activated if the source actor/component has all of these tags
- ``target_blocked_tags`` (GameplayTagContainer):  [Read-Write] This ability is blocked if the target actor/component has any of these tags
- ``target_required_tags`` (GameplayTagContainer):  [Read-Write] This ability can only be activated if the target actor/component has all of these tags

<a id="unreal.GameplayAbility.current_activation_info"></a>

#### current\_activation\_info

```python
@property
def current_activation_info() -> GameplayAbilityActivationInfo
```

(GameplayAbilityActivationInfo):  [Read-Only] This is information specific to this instance of the ability. E.g, whether it is predicting, authoring, confirmed, etc.

<a id="unreal.GameplayAbility.current_event_data"></a>

#### current\_event\_data

```python
@property
def current_event_data() -> GameplayEventData
```

(GameplayEventData):  [Read-Only] Information specific to this instance of the ability, if it was activated by an event

<a id="unreal.GameplayAbility.mark_pending_kill_on_ability_end"></a>

#### mark\_pending\_kill\_on\_ability\_end

```python
@property
def mark_pending_kill_on_ability_end() -> bool
```

(bool):  [Read-Only]
deprecated: This is unsafe. Do not use.

<a id="unreal.GameplayAbility.set_should_block_other_abilities"></a>

#### set\_should\_block\_other\_abilities

```python
def set_should_block_other_abilities(should_block_abilities: bool) -> None
```

x.set_should_block_other_abilities(should_block_abilities) -> None
Sets rather ability block flags are enabled or disabled. Only valid on instanced abilities

Args:
    should_block_abilities (bool):

<a id="unreal.GameplayAbility.set_can_be_canceled"></a>

#### set\_can\_be\_canceled

```python
def set_can_be_canceled(can_be_canceled: bool) -> None
```

x.set_can_be_canceled(can_be_canceled) -> None
Sets whether the ability should ignore cancel requests. Only valid on instanced abilities

Args:
    can_be_canceled (bool):

<a id="unreal.GameplayAbility.send_gameplay_event"></a>

#### send\_gameplay\_event

```python
def send_gameplay_event(event_tag: GameplayTag,
                        payload: GameplayEventData) -> None
```

x.send_gameplay_event(event_tag, payload) -> None
Sends a gameplay event, also creates a prediction window

Args:
    event_tag (GameplayTag): 
    payload (GameplayEventData):

<a id="unreal.GameplayAbility.remove_granted_by_effect"></a>

#### remove\_granted\_by\_effect

```python
def remove_granted_by_effect() -> None
```

x.remove_granted_by_effect() -> None
Removes the GameplayEffect that granted this ability. Can only be called on instanced abilities.

<a id="unreal.GameplayAbility.montage_stop"></a>

#### montage\_stop

```python
def montage_stop(override_blend_out_time: float = -1.000000) -> None
```

x.montage_stop(override_blend_out_time=-1.000000) -> None
Stops the current animation montage.

Args:
    override_blend_out_time (float):

<a id="unreal.GameplayAbility.montage_set_next_section_name"></a>

#### montage\_set\_next\_section\_name

```python
def montage_set_next_section_name(from_section_name: Name,
                                  to_section_name: Name) -> None
```

x.montage_set_next_section_name(from_section_name, to_section_name) -> None
Sets pending section on active montage

Args:
    from_section_name (Name): 
    to_section_name (Name):

<a id="unreal.GameplayAbility.montage_jump_to_section"></a>

#### montage\_jump\_to\_section

```python
def montage_jump_to_section(section_name: Name) -> None
```

x.montage_jump_to_section(section_name) -> None
Immediately jumps the active montage to a section

Args:
    section_name (Name):

<a id="unreal.GameplayAbility.make_target_location_info_from_owner_skeletal_mesh_component"></a>

#### make\_target\_location\_info\_from\_owner\_skeletal\_mesh\_component

```python
def make_target_location_info_from_owner_skeletal_mesh_component(
        socket_name: Name) -> GameplayAbilityTargetingLocationInfo
```

x.make_target_location_info_from_owner_skeletal_mesh_component(socket_name) -> GameplayAbilityTargetingLocationInfo
Creates a target location from a socket on the owner avatar's skeletal mesh

Args:
    socket_name (Name): 

Returns:
    GameplayAbilityTargetingLocationInfo:

<a id="unreal.GameplayAbility.make_target_location_info_from_owner_actor"></a>

#### make\_target\_location\_info\_from\_owner\_actor

```python
def make_target_location_info_from_owner_actor(
) -> GameplayAbilityTargetingLocationInfo
```

x.make_target_location_info_from_owner_actor() -> GameplayAbilityTargetingLocationInfo
Creates a target location from where the owner avatar is

Returns:
    GameplayAbilityTargetingLocationInfo:

<a id="unreal.GameplayAbility.make_outgoing_gameplay_effect_spec"></a>

#### make\_outgoing\_gameplay\_effect\_spec

```python
def make_outgoing_gameplay_effect_spec(
        gameplay_effect_class: Class,
        level: float = 1.000000) -> GameplayEffectSpecHandle
```

x.make_outgoing_gameplay_effect_spec(gameplay_effect_class, level=1.000000) -> GameplayEffectSpecHandle
Convenience method for abilities to get outgoing gameplay effect specs (for example, to pass on to projectiles to apply to whoever they hit)

Args:
    gameplay_effect_class (type(Class)): 
    level (float): 

Returns:
    GameplayEffectSpecHandle:

<a id="unreal.GameplayAbility.should_ability_respond_to_event"></a>

#### should\_ability\_respond\_to\_event

```python
def should_ability_respond_to_event(actor_info: GameplayAbilityActorInfo,
                                    payload: GameplayEventData) -> bool
```

x.should_ability_respond_to_event(actor_info, payload) -> bool
Returns true if this ability can be activated right now. Has no side effects

Args:
    actor_info (GameplayAbilityActorInfo): 
    payload (GameplayEventData): 

Returns:
    bool:

<a id="unreal.GameplayAbility.remove_gameplay_cue"></a>

#### remove\_gameplay\_cue

```python
def remove_gameplay_cue(gameplay_cue_tag: GameplayTag) -> None
```

x.remove_gameplay_cue(gameplay_cue_tag) -> None
Removes a persistent gameplay cue from the ability owner

Args:
    gameplay_cue_tag (GameplayTag):

<a id="unreal.GameplayAbility.on_end_ability"></a>

#### on\_end\_ability

```python
def on_end_ability(was_cancelled: bool) -> None
```

x.on_end_ability(was_cancelled) -> None
Blueprint event, will be called if an ability ends normally or abnormally

Args:
    was_cancelled (bool):

<a id="unreal.GameplayAbility.k2_has_authority"></a>

#### k2\_has\_authority

```python
def k2_has_authority() -> bool
```

x.k2_has_authority() -> bool
K2 Has Authority

Returns:
    bool:

<a id="unreal.GameplayAbility.execute_gameplay_cue_with_params"></a>

#### execute\_gameplay\_cue\_with\_params

```python
def execute_gameplay_cue_with_params(
        gameplay_cue_tag: GameplayTag,
        gameplay_cue_parameters: GameplayCueParameters) -> None
```

x.execute_gameplay_cue_with_params(gameplay_cue_tag, gameplay_cue_parameters) -> None
Invoke a gameplay cue on the ability owner, with extra parameters

Args:
    gameplay_cue_tag (GameplayTag): 
    gameplay_cue_parameters (GameplayCueParameters):

<a id="unreal.GameplayAbility.execute_gameplay_cue"></a>

#### execute\_gameplay\_cue

```python
def execute_gameplay_cue(gameplay_cue_tag: GameplayTag,
                         context: GameplayEffectContextHandle) -> None
```

x.execute_gameplay_cue(gameplay_cue_tag, context) -> None
Invoke a gameplay cue on the ability owner

Args:
    gameplay_cue_tag (GameplayTag): 
    context (GameplayEffectContextHandle):

<a id="unreal.GameplayAbility.end_ability_locally"></a>

#### end\_ability\_locally

```python
def end_ability_locally() -> None
```

x.end_ability_locally() -> None
Call from blueprints to end the ability naturally. This will only end predicted abilities locally, allowing it end naturally on the client or server

<a id="unreal.GameplayAbility.end_ability"></a>

#### end\_ability

```python
def end_ability() -> None
```

x.end_ability() -> None
Call from blueprints to forcibly end the ability without canceling it. This will replicate the end ability to the client or server which can interrupt tasks

<a id="unreal.GameplayAbility.commit_execute"></a>

#### commit\_execute

```python
def commit_execute() -> None
```

x.commit_execute() -> None
BP event called from CommitAbility

<a id="unreal.GameplayAbility.commit_ability_cost"></a>

#### commit\_ability\_cost

```python
def commit_ability_cost(broadcast_commit_event: bool = False) -> bool
```

x.commit_ability_cost(broadcast_commit_event=False) -> bool
Attempts to commit the ability's cost only. If BroadcastCommitEvent is true, it will broadcast the commit event that tasks like WaitAbilityCommit are listening for.

Args:
    broadcast_commit_event (bool): 

Returns:
    bool:

<a id="unreal.GameplayAbility.commit_ability_cooldown"></a>

#### commit\_ability\_cooldown

```python
def commit_ability_cooldown(broadcast_commit_event: bool = False,
                            force_cooldown: bool = False) -> bool
```

x.commit_ability_cooldown(broadcast_commit_event=False, force_cooldown=False) -> bool
Attempts to commit the ability's cooldown only. If BroadcastCommitEvent is true, it will broadcast the commit event that tasks like WaitAbilityCommit are listening for.

Args:
    broadcast_commit_event (bool): 
    force_cooldown (bool): 

Returns:
    bool:

<a id="unreal.GameplayAbility.commit_ability"></a>

#### commit\_ability

```python
def commit_ability() -> bool
```

x.commit_ability() -> bool
Attempts to commit the ability (spend resources, etc). This our last chance to fail. Child classes that override ActivateAbility must call this themselves!

Returns:
    bool:

<a id="unreal.GameplayAbility.check_ability_cost"></a>

#### check\_ability\_cost

```python
def check_ability_cost() -> bool
```

x.check_ability_cost() -> bool
Checks the ability's cost, but does not apply it.

Returns:
    bool:

<a id="unreal.GameplayAbility.check_ability_cooldown"></a>

#### check\_ability\_cooldown

```python
def check_ability_cooldown() -> bool
```

x.check_ability_cooldown() -> bool
Checks the ability's cooldown, but does not apply it.

Returns:
    bool:

<a id="unreal.GameplayAbility.cancel_ability"></a>

#### cancel\_ability

```python
def cancel_ability() -> None
```

x.cancel_ability() -> None
Call from Blueprint to cancel the ability naturally

<a id="unreal.GameplayAbility.can_activate_ability"></a>

#### can\_activate\_ability

```python
def can_activate_ability(
        actor_info: GameplayAbilityActorInfo,
        handle: GameplayAbilitySpecHandle) -> Optional[GameplayTagContainer]
```

x.can_activate_ability(actor_info, handle) -> GameplayTagContainer or None
Returns true if this ability can be activated right now. Has no side effects

Args:
    actor_info (GameplayAbilityActorInfo): 
    handle (GameplayAbilitySpecHandle): 

Returns:
    GameplayTagContainer or None: 

    relevant_tags (GameplayTagContainer):

<a id="unreal.GameplayAbility.apply_gameplay_effect_spec_to_target"></a>

#### apply\_gameplay\_effect\_spec\_to\_target

```python
def apply_gameplay_effect_spec_to_target(
    effect_spec_handle: GameplayEffectSpecHandle,
    target_data: GameplayAbilityTargetDataHandle
) -> Array[ActiveGameplayEffectHandle]
```

x.apply_gameplay_effect_spec_to_target(effect_spec_handle, target_data) -> Array[ActiveGameplayEffectHandle]
Apply a previously created gameplay effect spec to a target

Args:
    effect_spec_handle (GameplayEffectSpecHandle): 
    target_data (GameplayAbilityTargetDataHandle): 

Returns:
    Array[ActiveGameplayEffectHandle]:

<a id="unreal.GameplayAbility.apply_gameplay_effect_spec_to_owner"></a>

#### apply\_gameplay\_effect\_spec\_to\_owner

```python
def apply_gameplay_effect_spec_to_owner(
    effect_spec_handle: GameplayEffectSpecHandle
) -> ActiveGameplayEffectHandle
```

x.apply_gameplay_effect_spec_to_owner(effect_spec_handle) -> ActiveGameplayEffectHandle
Apply a previously created gameplay effect spec to the owner of this ability

Args:
    effect_spec_handle (GameplayEffectSpecHandle): 

Returns:
    ActiveGameplayEffectHandle:

<a id="unreal.GameplayAbility.add_gameplay_cue_with_params"></a>

#### add\_gameplay\_cue\_with\_params

```python
def add_gameplay_cue_with_params(gameplay_cue_tag: GameplayTag,
                                 gameplay_cue_parameter: GameplayCueParameters,
                                 remove_on_ability_end: bool = True) -> None
```

x.add_gameplay_cue_with_params(gameplay_cue_tag, gameplay_cue_parameter, remove_on_ability_end=True) -> None
Adds a persistent gameplay cue to the ability owner. Optionally will remove if ability ends

Args:
    gameplay_cue_tag (GameplayTag): 
    gameplay_cue_parameter (GameplayCueParameters): 
    remove_on_ability_end (bool):

<a id="unreal.GameplayAbility.add_gameplay_cue"></a>

#### add\_gameplay\_cue

```python
def add_gameplay_cue(gameplay_cue_tag: GameplayTag,
                     context: GameplayEffectContextHandle,
                     remove_on_ability_end: bool = True) -> None
```

x.add_gameplay_cue(gameplay_cue_tag, context, remove_on_ability_end=True) -> None
Adds a persistent gameplay cue to the ability owner. Optionally will remove if ability ends

Args:
    gameplay_cue_tag (GameplayTag): 
    context (GameplayEffectContextHandle): 
    remove_on_ability_end (bool):

<a id="unreal.GameplayAbility.activate_ability_from_event"></a>

#### activate\_ability\_from\_event

```python
def activate_ability_from_event(event_data: GameplayEventData) -> None
```

x.activate_ability_from_event(event_data) -> None
K2 Activate Ability from Event

Args:
    event_data (GameplayEventData):

<a id="unreal.GameplayAbility.activate_ability"></a>

#### activate\_ability

```python
def activate_ability() -> None
```

x.activate_ability() -> None
The main function that defines what an ability does.
 -Child classes will want to override this
 -This function graph should call CommitAbility
 -This function graph should call EndAbility

 Latent/async actions are ok in this graph. Note that Commit and EndAbility calling requirements speak to the K2_ActivateAbility graph.
 In C++, the call to K2_ActivateAbility() may return without CommitAbility or EndAbility having been called. But it is expected that this
 will only occur when latent/async actions are pending. When K2_ActivateAbility logically finishes, then we will expect Commit/End to have been called.

<a id="unreal.GameplayAbility.is_locally_controlled"></a>

#### is\_locally\_controlled

```python
def is_locally_controlled() -> bool
```

x.is_locally_controlled() -> bool
True if the owning actor is locally controlled, true in single player

Returns:
    bool:

<a id="unreal.GameplayAbility.invalidate_client_prediction_key"></a>

#### invalidate\_client\_prediction\_key

```python
def invalidate_client_prediction_key() -> None
```

x.invalidate_client_prediction_key() -> None
Invalidates the current prediction key. This should be used in cases where there is a valid prediction window, but the server is doing logic that only it can do, and afterwards performs an action that the client could predict (had the client been able to run the server-only code prior).
This returns instantly and has no other side effects other than clearing the current prediction key.

<a id="unreal.GameplayAbility.get_source_object_bp"></a>

#### get\_source\_object\_bp

```python
def get_source_object_bp(handle: GameplayAbilitySpecHandle,
                         actor_info: GameplayAbilityActorInfo) -> Object
```

x.get_source_object_bp(handle, actor_info) -> Object
Retrieves the SourceObject associated with this ability. Callable on non instanced

Args:
    handle (GameplayAbilitySpecHandle): 
    actor_info (GameplayAbilityActorInfo): 

Returns:
    Object:

<a id="unreal.GameplayAbility.get_owning_component_from_actor_info"></a>

#### get\_owning\_component\_from\_actor\_info

```python
def get_owning_component_from_actor_info() -> SkeletalMeshComponent
```

x.get_owning_component_from_actor_info() -> SkeletalMeshComponent
Convenience method for abilities to get skeletal mesh component - useful for aiming abilities

Returns:
    SkeletalMeshComponent:

<a id="unreal.GameplayAbility.get_owning_actor_from_actor_info"></a>

#### get\_owning\_actor\_from\_actor\_info

```python
def get_owning_actor_from_actor_info() -> Actor
```

x.get_owning_actor_from_actor_info() -> Actor
Returns the actor that owns this ability, which may not have a physical location

Returns:
    Actor:

<a id="unreal.GameplayAbility.get_granted_by_effect_context"></a>

#### get\_granted\_by\_effect\_context

```python
def get_granted_by_effect_context() -> GameplayEffectContextHandle
```

x.get_granted_by_effect_context() -> GameplayEffectContextHandle
Retrieves the EffectContext of the GameplayEffect that granted this ability. Can only be called on instanced abilities.

Returns:
    GameplayEffectContextHandle:

<a id="unreal.GameplayAbility.get_current_source_object"></a>

#### get\_current\_source\_object

```python
def get_current_source_object() -> Object
```

x.get_current_source_object() -> Object
Retrieves the SourceObject associated with this ability. Can only be called on instanced abilities.

Returns:
    Object:

<a id="unreal.GameplayAbility.get_current_montage"></a>

#### get\_current\_montage

```python
def get_current_montage() -> AnimMontage
```

x.get_current_montage() -> AnimMontage
Returns the currently playing montage for this ability, if any

Returns:
    AnimMontage:

<a id="unreal.GameplayAbility.get_cooldown_time_remaining"></a>

#### get\_cooldown\_time\_remaining

```python
def get_cooldown_time_remaining() -> float
```

x.get_cooldown_time_remaining() -> float
Returns the time in seconds remaining on the currently active cooldown.

Returns:
    float:

<a id="unreal.GameplayAbility.get_context_from_owner"></a>

#### get\_context\_from\_owner

```python
def get_context_from_owner(
    optional_target_data: GameplayAbilityTargetDataHandle
) -> GameplayEffectContextHandle
```

x.get_context_from_owner(optional_target_data) -> GameplayEffectContextHandle
Generates a GameplayEffectContextHandle from our owner and an optional TargetData.

Args:
    optional_target_data (GameplayAbilityTargetDataHandle): 

Returns:
    GameplayEffectContextHandle:

<a id="unreal.GameplayAbility.get_avatar_actor_from_actor_info"></a>

#### get\_avatar\_actor\_from\_actor\_info

```python
def get_avatar_actor_from_actor_info() -> Actor
```

x.get_avatar_actor_from_actor_info() -> Actor
Returns the physical actor that is executing this ability. May be null

Returns:
    Actor:

<a id="unreal.GameplayAbility.get_actor_info"></a>

#### get\_actor\_info

```python
def get_actor_info() -> GameplayAbilityActorInfo
```

x.get_actor_info() -> GameplayAbilityActorInfo
Returns the actor info associated with this ability, has cached pointers to useful objects

Returns:
    GameplayAbilityActorInfo:

<a id="unreal.GameplayAbility.get_ability_system_component_from_actor_info"></a>

#### get\_ability\_system\_component\_from\_actor\_info

```python
def get_ability_system_component_from_actor_info() -> AbilitySystemComponent
```

x.get_ability_system_component_from_actor_info() -> AbilitySystemComponent
Returns the AbilitySystemComponent that is activating this ability

Returns:
    AbilitySystemComponent:

<a id="unreal.GameplayAbility.get_ability_level_bp"></a>

#### get\_ability\_level\_bp

```python
def get_ability_level_bp(handle: GameplayAbilitySpecHandle,
                         actor_info: GameplayAbilityActorInfo) -> int
```

x.get_ability_level_bp(handle, actor_info) -> int32
Returns current ability level for non instanced abilities. You must call this version in these contexts!

Args:
    handle (GameplayAbilitySpecHandle): 
    actor_info (GameplayAbilityActorInfo): 

Returns:
    int32:

<a id="unreal.GameplayAbility.get_ability_level"></a>

#### get\_ability\_level

```python
def get_ability_level() -> int
```

x.get_ability_level() -> int32
Returns current level of the Ability

Returns:
    int32:

<a id="unreal.GameplayAbility.end_task_by_instance_name"></a>

#### end\_task\_by\_instance\_name

```python
def end_task_by_instance_name(instance_name: Name) -> None
```

x.end_task_by_instance_name(instance_name) -> None
Add any task with this instance name to a list to be ended (not canceled) next frame.  See also CancelTaskByInstanceName.

Args:
    instance_name (Name):

<a id="unreal.GameplayAbility.end_ability_state"></a>

#### end\_ability\_state

```python
def end_ability_state(optional_state_name_to_end: Name) -> None
```

x.end_ability_state(optional_state_name_to_end) -> None
Ends any active ability state task with the given name. If name is 'None' all active states will be ended (in an arbitrary order).

Args:
    optional_state_name_to_end (Name):

<a id="unreal.GameplayAbility.confirm_task_by_instance_name"></a>

#### confirm\_task\_by\_instance\_name

```python
def confirm_task_by_instance_name(instance_name: Name, end_task: bool) -> None
```

x.confirm_task_by_instance_name(instance_name, end_task) -> None
Finds all currently active tasks named InstanceName and confirms them. What this means depends on the individual task. By default, this does nothing other than ending if bEndTask is true.

Args:
    instance_name (Name): 
    end_task (bool):

<a id="unreal.GameplayAbility.cancel_task_by_instance_name"></a>

#### cancel\_task\_by\_instance\_name

```python
def cancel_task_by_instance_name(instance_name: Name) -> None
```

x.cancel_task_by_instance_name(instance_name) -> None
Add any task with this instance name to a list to be canceled (not ended) next frame.  See also EndTaskByInstanceName.

Args:
    instance_name (Name):

<a id="unreal.GameplayAbility.remove_gameplay_effect_from_owner_with_handle"></a>

#### remove\_gameplay\_effect\_from\_owner\_with\_handle

```python
def remove_gameplay_effect_from_owner_with_handle(
        handle: ActiveGameplayEffectHandle,
        stacks_to_remove: int = -1) -> None
```

x.remove_gameplay_effect_from_owner_with_handle(handle, stacks_to_remove=-1) -> None
Removes GameplayEffect from owner that match the given handle

Args:
    handle (ActiveGameplayEffectHandle): 
    stacks_to_remove (int32):

<a id="unreal.GameplayAbility.remove_gameplay_effect_from_owner_with_granted_tags"></a>

#### remove\_gameplay\_effect\_from\_owner\_with\_granted\_tags

```python
def remove_gameplay_effect_from_owner_with_granted_tags(
        with_granted_tags: GameplayTagContainer,
        stacks_to_remove: int = -1) -> None
```

x.remove_gameplay_effect_from_owner_with_granted_tags(with_granted_tags, stacks_to_remove=-1) -> None
Removes GameplayEffects from owner which grant the given tags

Args:
    with_granted_tags (GameplayTagContainer): 
    stacks_to_remove (int32):

<a id="unreal.GameplayAbility.remove_gameplay_effect_from_owner_with_asset_tags"></a>

#### remove\_gameplay\_effect\_from\_owner\_with\_asset\_tags

```python
def remove_gameplay_effect_from_owner_with_asset_tags(
        with_asset_tags: GameplayTagContainer,
        stacks_to_remove: int = -1) -> None
```

x.remove_gameplay_effect_from_owner_with_asset_tags(with_asset_tags, stacks_to_remove=-1) -> None
Removes GameplayEffects from owner which match the given asset level tags

Args:
    with_asset_tags (GameplayTagContainer): 
    stacks_to_remove (int32):

<a id="unreal.GameplayAbility.apply_gameplay_effect_to_target"></a>

#### apply\_gameplay\_effect\_to\_target

```python
def apply_gameplay_effect_to_target(
        target_data: GameplayAbilityTargetDataHandle,
        gameplay_effect_class: Class,
        gameplay_effect_level: int = 1,
        stacks: int = 1) -> Array[ActiveGameplayEffectHandle]
```

x.apply_gameplay_effect_to_target(target_data, gameplay_effect_class, gameplay_effect_level=1, stacks=1) -> Array[ActiveGameplayEffectHandle]
Apply a gameplay effect to a Target

Args:
    target_data (GameplayAbilityTargetDataHandle): 
    gameplay_effect_class (type(Class)): 
    gameplay_effect_level (int32): 
    stacks (int32): 

Returns:
    Array[ActiveGameplayEffectHandle]:

<a id="unreal.GameplayAbility.apply_gameplay_effect_to_owner"></a>

#### apply\_gameplay\_effect\_to\_owner

```python
def apply_gameplay_effect_to_owner(
        gameplay_effect_class: Class,
        gameplay_effect_level: int = 1,
        stacks: int = 1) -> ActiveGameplayEffectHandle
```

x.apply_gameplay_effect_to_owner(gameplay_effect_class, gameplay_effect_level=1, stacks=1) -> ActiveGameplayEffectHandle
Apply a gameplay effect to the owner of this ability

Args:
    gameplay_effect_class (type(Class)): 
    gameplay_effect_level (int32): 
    stacks (int32): 

Returns:
    ActiveGameplayEffectHandle:

<a id="unreal.GameplayAbilityTargetActor"></a>