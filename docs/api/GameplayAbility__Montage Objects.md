## GameplayAbility\_Montage Objects

```python
class GameplayAbility_Montage(GameplayAbility)
```

A gameplay ability that plays a single montage and applies a GameplayEffect

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbility_Montage.h

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
- ``gameplay_effect_classes_while_animating`` (Array[type(Class)]):  [Read-Write] GameplayEffects to apply and then remove while the animation is playing
- ``gameplay_effects_while_animating`` (Array[GameplayEffect]):  [Read-Only] Deprecated. Use GameplayEffectClassesWhileAnimating instead.
- ``instancing_policy`` (GameplayAbilityInstancingPolicy):  [Read-Write] How the ability is instanced when executed. This limits what an ability can do in its implementation.
- ``mark_pending_kill_on_ability_end`` (bool):  [Read-Write]
  deprecated: This is unsafe. Do not use.
- ``montage_to_play`` (AnimMontage):  [Read-Write]
- ``net_execution_policy`` (GameplayAbilityNetExecutionPolicy):  [Read-Write] How does an ability execute on the network. Does a client "ask and predict", "ask and wait", "don't ask (just do it)".
- ``net_security_policy`` (GameplayAbilityNetSecurityPolicy):  [Read-Write] What protections does this ability have? Should the client be allowed to request changes to the execution of the ability?
- ``play_rate`` (float):  [Read-Write]
- ``replicate_input_directly`` (bool):  [Read-Write] If true, this ability will always replicate input press/release events to the server.
- ``replication_policy`` (GameplayAbilityReplicationPolicy):  [Read-Write] How an ability replicates state/events to everyone on the network. Replication is not required for NetExecutionPolicy.
- ``retrigger_instanced_ability`` (bool):  [Read-Write] if true, and trying to activate an already active instanced ability, end it and re-trigger it.
- ``section_name`` (Name):  [Read-Write]
- ``server_respects_remote_ability_cancellation`` (bool):  [Read-Write] If this is set, the server-side version of the ability can be canceled by the client-side version. The client-side version can always be canceled by the server.
- ``source_blocked_tags`` (GameplayTagContainer):  [Read-Write] This ability is blocked if the source actor/component has any of these tags
- ``source_required_tags`` (GameplayTagContainer):  [Read-Write] This ability can only be activated if the source actor/component has all of these tags
- ``target_blocked_tags`` (GameplayTagContainer):  [Read-Write] This ability is blocked if the target actor/component has any of these tags
- ``target_required_tags`` (GameplayTagContainer):  [Read-Write] This ability can only be activated if the target actor/component has all of these tags

<a id="unreal.AbilityTask_ApplyRootMotion_Base"></a>