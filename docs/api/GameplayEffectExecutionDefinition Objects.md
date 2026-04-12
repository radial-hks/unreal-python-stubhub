## GameplayEffectExecutionDefinition Objects

```python
class GameplayEffectExecutionDefinition(StructBase)
```

Struct representing the definition of a custom execution for a gameplay effect.
Custom executions run special logic from an outside class each time the gameplay effect executes.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``calculation_class`` (type(Class)):  [Read-Write] Custom execution calculation class to run when the gameplay effect executes
- ``calculation_modifiers`` (Array[GameplayEffectExecutionScopedModifierInfo]):  [Read-Write] Modifiers that are applied "in place" during the execution calculation
- ``conditional_gameplay_effects`` (Array[ConditionalGameplayEffect]):  [Read-Write] Other Gameplay Effects that will be applied to the target of this execution if the execution is successful. Note if no execution class is selected, these will always apply.
- ``passed_in_tags`` (GameplayTagContainer):  [Read-Write] These tags are passed into the execution as is, and may be used to do conditional logic

<a id="unreal.GameplayEffectExecutionDefinition.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.GameplayModifierInfo"></a>