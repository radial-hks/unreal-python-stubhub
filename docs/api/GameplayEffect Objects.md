## GameplayEffect Objects

```python
class GameplayEffect(Object)
```

UGameplayEffect
    The GameplayEffect definition. This is the data asset defined in the editor that drives everything.
 This is only blueprintable to allow for templating gameplay effects. Gameplay effects should NOT contain blueprint graphs.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``application_requirements`` (Array[type(Class)]):  [Read-Write]
  deprecated: Property 'ApplicationRequirements' is deprecated.
- ``application_tag_requirements`` (GameplayTagRequirements):  [Read-Write]
  deprecated: Property 'ApplicationTagRequirements' is deprecated.
- ``chance_to_apply_to_target`` (ScalableFloat):  [Read-Write]
  deprecated: Property 'ChanceToApplyToTarget' is deprecated.
- ``clear_stack_on_overflow`` (bool):  [Read-Write] If true, the entire stack of the effect will be cleared once it overflows
- ``conditional_gameplay_effects`` (Array[ConditionalGameplayEffect]):  [Read-Write]
  deprecated: Property 'ConditionalGameplayEffects' is deprecated.
- ``deny_overflow_application`` (bool):  [Read-Write] If true, stacking attempts made while at the stack count will fail, resulting in the duration and context not being refreshed
- ``duration_magnitude`` (GameplayEffectModifierMagnitude):  [Read-Write] Duration in seconds. 0.0 for instantaneous effects; -1.0 for infinite duration.
- ``duration_policy`` (GameplayEffectDurationType):  [Read-Write] Policy for the duration of this effect
- ``editor_status_text`` (Text):  [Read-Only] Allow us to show the Status of the class (valid configurations or invalid configurations) while configuring in the Editor
- ``execute_periodic_effect_on_application`` (bool):  [Read-Write] If true, the effect executes on application and then at every period interval. If false, no execution occurs until the first period elapses. // EditCondition in FGameplayEffectDetails
- ``executions`` (Array[GameplayEffectExecutionDefinition]):  [Read-Write] Array of executions that will affect the target of this effect
- ``gameplay_cues`` (Array[GameplayEffectCue]):  [Read-Write] Cues to trigger non-simulated reactions in response to this GameplayEffect such as sounds, particle effects, etc
- ``ge_components`` (Array[GameplayEffectComponent]):  [Read-Write] These Gameplay Effect Components define how this Gameplay Effect behaves when applied
- ``granted_abilities`` (Array[GameplayAbilitySpecDef]):  [Read-Write]
- ``granted_application_immunity_query`` (GameplayEffectQuery):  [Read-Write]
  deprecated: Property 'GrantedApplicationImmunityQuery' is deprecated.
- ``granted_application_immunity_tags`` (GameplayTagRequirements):  [Read-Write]
  deprecated: Property 'GrantedApplicationImmunityTags' is deprecated.
- ``inheritable_blocked_ability_tags_container`` (InheritedTagContainer):  [Read-Write]
  deprecated: Property 'InheritableBlockedAbilityTagsContainer' is deprecated.
- ``inheritable_gameplay_effect_tags`` (InheritedTagContainer):  [Read-Write]
  deprecated: Property 'InheritableGameplayEffectTags' is deprecated.
- ``inheritable_owned_tags_container`` (InheritedTagContainer):  [Read-Write]
  deprecated: Property 'InheritableOwnedTagsContainer' is deprecated.
- ``modifiers`` (Array[GameplayModifierInfo]):  [Read-Write] Array of modifiers that will affect the target of this effect
- ``ongoing_tag_requirements`` (GameplayTagRequirements):  [Read-Write]
  deprecated: Property 'OngoingTagRequirements' is deprecated.
- ``overflow_effects`` (Array[type(Class)]):  [Read-Write] Effects to apply when a stacking effect "overflows" its stack count through another attempted application. Added whether the overflow application succeeds or not.
- ``period`` (ScalableFloat):  [Read-Write] Period in seconds. 0.0 for non-periodic effects
- ``periodic_inhibition_policy`` (GameplayEffectPeriodInhibitionRemovedPolicy):  [Read-Write] How we should respond when a periodic gameplay effect is no longer inhibited // EditCondition in FGameplayEffectDetails
- ``premature_expiration_effect_classes`` (Array[type(Class)]):  [Read-Write]
  deprecated: Property 'PrematureExpirationEffectClasses' is deprecated.
- ``removal_tag_requirements`` (GameplayTagRequirements):  [Read-Write]
  deprecated: Property 'RemovalTagRequirements' is deprecated.
- ``remove_gameplay_effect_query`` (GameplayEffectQuery):  [Read-Write]
  deprecated: Property 'RemoveGameplayEffectQuery' is deprecated.
- ``remove_gameplay_effects_with_tags`` (InheritedTagContainer):  [Read-Write]
  deprecated: Property 'RemoveGameplayEffectsWithTags' is deprecated.
- ``require_modifier_success_to_trigger_cues`` (bool):  [Read-Write] If true, cues will only trigger when GE modifiers succeed being applied (whether through modifiers or executions)
- ``routine_expiration_effect_classes`` (Array[type(Class)]):  [Read-Write]
  deprecated: Property 'RoutineExpirationEffectClasses' is deprecated.
- ``stack_duration_refresh_policy`` (GameplayEffectStackingDurationPolicy):  [Read-Write] Policy for how the effect duration should be refreshed while stacking
- ``stack_expiration_policy`` (GameplayEffectStackingExpirationPolicy):  [Read-Write] Policy for how to handle duration expiring on this gameplay effect
- ``stack_limit_count`` (int32):  [Read-Write] Stack limit for StackingType
- ``stack_period_reset_policy`` (GameplayEffectStackingPeriodPolicy):  [Read-Write] Policy for how the effect period should be reset (or not) while stacking
- ``stacking_type`` (GameplayEffectStackingType):  [Read-Write] How this GameplayEffect stacks with other instances of this same GameplayEffect
- ``suppress_stacking_cues`` (bool):  [Read-Write] If true, GameplayCues will only be triggered for the first instance in a stacking GameplayEffect.
- ``ui_data`` (GameplayEffectUIData):  [Read-Write]
  deprecated: Property 'UIData' is deprecated.

<a id="unreal.GameplayEffect.period"></a>

#### period

```python
@property
def period() -> ScalableFloat
```

(ScalableFloat):  [Read-Only] Period in seconds. 0.0 for non-periodic effects

<a id="unreal.GameplayEffect.execute_periodic_effect_on_application"></a>

#### execute\_periodic\_effect\_on\_application

```python
@property
def execute_periodic_effect_on_application() -> bool
```

(bool):  [Read-Only] If true, the effect executes on application and then at every period interval. If false, no execution occurs until the first period elapses. // EditCondition in FGameplayEffectDetails

<a id="unreal.GameplayEffect.periodic_inhibition_policy"></a>

#### periodic\_inhibition\_policy

```python
@property
def periodic_inhibition_policy(
) -> GameplayEffectPeriodInhibitionRemovedPolicy
```

(GameplayEffectPeriodInhibitionRemovedPolicy):  [Read-Only] How we should respond when a periodic gameplay effect is no longer inhibited // EditCondition in FGameplayEffectDetails

<a id="unreal.GameplayEffect.modifiers"></a>

#### modifiers

```python
@property
def modifiers() -> Array[GameplayModifierInfo]
```

(Array[GameplayModifierInfo]):  [Read-Only] Array of modifiers that will affect the target of this effect

<a id="unreal.GameplayEffect.executions"></a>

#### executions

```python
@property
def executions() -> Array[GameplayEffectExecutionDefinition]
```

(Array[GameplayEffectExecutionDefinition]):  [Read-Only] Array of executions that will affect the target of this effect

<a id="unreal.GameplayEffect.chance_to_apply_to_target"></a>

#### chance\_to\_apply\_to\_target

```python
@property
def chance_to_apply_to_target() -> ScalableFloat
```

(ScalableFloat):  [Read-Write]
deprecated: Property 'ChanceToApplyToTarget' is deprecated.

<a id="unreal.GameplayEffect.chance_to_apply_to_target"></a>

#### chance\_to\_apply\_to\_target

```python
@chance_to_apply_to_target.setter
def chance_to_apply_to_target(value: ScalableFloat) -> None
```

<a id="unreal.GameplayEffect.application_requirements"></a>

#### application\_requirements

```python
@property
def application_requirements() -> Array[Class]
```

(Array[type(Class)]):  [Read-Write]
deprecated: Property 'ApplicationRequirements' is deprecated.

<a id="unreal.GameplayEffect.application_requirements"></a>

#### application\_requirements

```python
@application_requirements.setter
def application_requirements(value: Array[Class]) -> None
```

<a id="unreal.GameplayEffect.conditional_gameplay_effects"></a>

#### conditional\_gameplay\_effects

```python
@property
def conditional_gameplay_effects() -> Array[ConditionalGameplayEffect]
```

(Array[ConditionalGameplayEffect]):  [Read-Only]
deprecated: Property 'ConditionalGameplayEffects' is deprecated.

<a id="unreal.GameplayEffect.overflow_effects"></a>

#### overflow\_effects

```python
@property
def overflow_effects() -> Array[Class]
```

(Array[type(Class)]):  [Read-Only] Effects to apply when a stacking effect "overflows" its stack count through another attempted application. Added whether the overflow application succeeds or not.

<a id="unreal.GameplayEffect.deny_overflow_application"></a>

#### deny\_overflow\_application

```python
@property
def deny_overflow_application() -> bool
```

(bool):  [Read-Only] If true, stacking attempts made while at the stack count will fail, resulting in the duration and context not being refreshed

<a id="unreal.GameplayEffect.clear_stack_on_overflow"></a>

#### clear\_stack\_on\_overflow

```python
@property
def clear_stack_on_overflow() -> bool
```

(bool):  [Read-Only] If true, the entire stack of the effect will be cleared once it overflows

<a id="unreal.GameplayEffect.premature_expiration_effect_classes"></a>

#### premature\_expiration\_effect\_classes

```python
@property
def premature_expiration_effect_classes() -> Array[Class]
```

(Array[type(Class)]):  [Read-Only]
deprecated: Property 'PrematureExpirationEffectClasses' is deprecated.

<a id="unreal.GameplayEffect.routine_expiration_effect_classes"></a>

#### routine\_expiration\_effect\_classes

```python
@property
def routine_expiration_effect_classes() -> Array[Class]
```

(Array[type(Class)]):  [Read-Only]
deprecated: Property 'RoutineExpirationEffectClasses' is deprecated.

<a id="unreal.GameplayEffect.require_modifier_success_to_trigger_cues"></a>

#### require\_modifier\_success\_to\_trigger\_cues

```python
@property
def require_modifier_success_to_trigger_cues() -> bool
```

(bool):  [Read-Only] If true, cues will only trigger when GE modifiers succeed being applied (whether through modifiers or executions)

<a id="unreal.GameplayEffect.gameplay_cues"></a>

#### gameplay\_cues

```python
@property
def gameplay_cues() -> Array[GameplayEffectCue]
```

(Array[GameplayEffectCue]):  [Read-Only] Cues to trigger non-simulated reactions in response to this GameplayEffect such as sounds, particle effects, etc

<a id="unreal.GameplayEffect.ui_data"></a>

#### ui\_data

```python
@property
def ui_data() -> GameplayEffectUIData
```

(GameplayEffectUIData):  [Read-Only]
deprecated: Property 'UIData' is deprecated.

<a id="unreal.GameplayEffect.inheritable_gameplay_effect_tags"></a>

#### inheritable\_gameplay\_effect\_tags

```python
@property
def inheritable_gameplay_effect_tags() -> InheritedTagContainer
```

(InheritedTagContainer):  [Read-Only]
deprecated: Property 'InheritableGameplayEffectTags' is deprecated.

<a id="unreal.GameplayEffect.inheritable_owned_tags_container"></a>

#### inheritable\_owned\_tags\_container

```python
@property
def inheritable_owned_tags_container() -> InheritedTagContainer
```

(InheritedTagContainer):  [Read-Only]
deprecated: Property 'InheritableOwnedTagsContainer' is deprecated.

<a id="unreal.GameplayEffect.inheritable_blocked_ability_tags_container"></a>

#### inheritable\_blocked\_ability\_tags\_container

```python
@property
def inheritable_blocked_ability_tags_container() -> InheritedTagContainer
```

(InheritedTagContainer):  [Read-Only]
deprecated: Property 'InheritableBlockedAbilityTagsContainer' is deprecated.

<a id="unreal.GameplayEffect.ongoing_tag_requirements"></a>

#### ongoing\_tag\_requirements

```python
@property
def ongoing_tag_requirements() -> GameplayTagRequirements
```

(GameplayTagRequirements):  [Read-Only]
deprecated: Property 'OngoingTagRequirements' is deprecated.

<a id="unreal.GameplayEffect.application_tag_requirements"></a>

#### application\_tag\_requirements

```python
@property
def application_tag_requirements() -> GameplayTagRequirements
```

(GameplayTagRequirements):  [Read-Only]
deprecated: Property 'ApplicationTagRequirements' is deprecated.

<a id="unreal.GameplayEffect.removal_tag_requirements"></a>

#### removal\_tag\_requirements

```python
@property
def removal_tag_requirements() -> GameplayTagRequirements
```

(GameplayTagRequirements):  [Read-Only]
deprecated: Property 'RemovalTagRequirements' is deprecated.

<a id="unreal.GameplayEffect.remove_gameplay_effects_with_tags"></a>

#### remove\_gameplay\_effects\_with\_tags

```python
@property
def remove_gameplay_effects_with_tags() -> InheritedTagContainer
```

(InheritedTagContainer):  [Read-Only]
deprecated: Property 'RemoveGameplayEffectsWithTags' is deprecated.

<a id="unreal.GameplayEffect.inheritable_clear_tags_container"></a>

#### inheritable\_clear\_tags\_container

```python
@property
def inheritable_clear_tags_container() -> InheritedTagContainer
```

deprecated: 'inheritable_clear_tags_container' was renamed to 'remove_gameplay_effects_with_tags'.

<a id="unreal.GameplayEffect.granted_application_immunity_tags"></a>

#### granted\_application\_immunity\_tags

```python
@property
def granted_application_immunity_tags() -> GameplayTagRequirements
```

(GameplayTagRequirements):  [Read-Only]
deprecated: Property 'GrantedApplicationImmunityTags' is deprecated.

<a id="unreal.GameplayEffect.granted_application_immunity_query"></a>

#### granted\_application\_immunity\_query

```python
@property
def granted_application_immunity_query() -> GameplayEffectQuery
```

(GameplayEffectQuery):  [Read-Only]
deprecated: Property 'GrantedApplicationImmunityQuery' is deprecated.

<a id="unreal.GameplayEffect.remove_gameplay_effect_query"></a>

#### remove\_gameplay\_effect\_query

```python
@property
def remove_gameplay_effect_query() -> GameplayEffectQuery
```

(GameplayEffectQuery):  [Read-Only]
deprecated: Property 'RemoveGameplayEffectQuery' is deprecated.

<a id="unreal.GameplayEffect.stacking_type"></a>

#### stacking\_type

```python
@property
def stacking_type() -> GameplayEffectStackingType
```

(GameplayEffectStackingType):  [Read-Only] How this GameplayEffect stacks with other instances of this same GameplayEffect

<a id="unreal.GameplayEffect.stack_limit_count"></a>

#### stack\_limit\_count

```python
@property
def stack_limit_count() -> int
```

(int32):  [Read-Only] Stack limit for StackingType

<a id="unreal.GameplayEffect.stack_duration_refresh_policy"></a>

#### stack\_duration\_refresh\_policy

```python
@property
def stack_duration_refresh_policy() -> GameplayEffectStackingDurationPolicy
```

(GameplayEffectStackingDurationPolicy):  [Read-Only] Policy for how the effect duration should be refreshed while stacking

<a id="unreal.GameplayEffect.stack_period_reset_policy"></a>

#### stack\_period\_reset\_policy

```python
@property
def stack_period_reset_policy() -> GameplayEffectStackingPeriodPolicy
```

(GameplayEffectStackingPeriodPolicy):  [Read-Only] Policy for how the effect period should be reset (or not) while stacking

<a id="unreal.GameplayEffect.stack_expiration_policy"></a>

#### stack\_expiration\_policy

```python
@property
def stack_expiration_policy() -> GameplayEffectStackingExpirationPolicy
```

(GameplayEffectStackingExpirationPolicy):  [Read-Only] Policy for how to handle duration expiring on this gameplay effect

<a id="unreal.GameplayEffect.granted_abilities"></a>

#### granted\_abilities

```python
@property
def granted_abilities() -> Array[GameplayAbilitySpecDef]
```

(Array[GameplayAbilitySpecDef]):  [Read-Only]

<a id="unreal.GameplayEffect.ge_components"></a>

#### ge\_components

```python
@property
def ge_components() -> Array[GameplayEffectComponent]
```

(Array[GameplayEffectComponent]):  [Read-Only] These Gameplay Effect Components define how this Gameplay Effect behaves when applied

<a id="unreal.GameplayEffect.has_matching_gameplay_tag"></a>

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

<a id="unreal.GameplayEffect.has_any_matching_gameplay_tags"></a>

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

<a id="unreal.GameplayEffect.has_all_matching_gameplay_tags"></a>

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

<a id="unreal.AbilityAsync"></a>