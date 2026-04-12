## GameplayEffectExecutionScopedModifierInfo Objects

```python
class GameplayEffectExecutionScopedModifierInfo(StructBase)
```

Struct representing modifier info used exclusively for "scoped" executions that happen instantaneously. These are
folded into a calculation only for the extent of the calculation and never permanently added to an aggregator.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aggregator_type`` (GameplayEffectScopedModifierAggregatorType):  [Read-Only] Type of aggregator backing the scoped mod
- ``captured_attribute`` (GameplayEffectAttributeCaptureDefinition):  [Read-Only] Backing attribute that the scoped modifier is for
- ``evaluation_channel_settings`` (GameplayModEvaluationChannelSettings):  [Read-Write] Evaluation channel settings of the scoped modifier
- ``modifier_magnitude`` (GameplayEffectModifierMagnitude):  [Read-Write] Magnitude of the scoped modifier
- ``modifier_op`` (GameplayModOp):  [Read-Write] Modifier operation to perform
- ``source_tags`` (GameplayTagRequirements):  [Read-Write] Source tag requirements for the modifier to apply
- ``target_tags`` (GameplayTagRequirements):  [Read-Write] Target tag requirements for the modifier to apply
- ``transient_aggregator_identifier`` (GameplayTag):  [Read-Only] Identifier for aggregator if acting as a transient "temporary variable" aggregator

<a id="unreal.GameplayEffectExecutionScopedModifierInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.ConditionalGameplayEffect"></a>