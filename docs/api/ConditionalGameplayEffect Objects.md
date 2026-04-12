## ConditionalGameplayEffect Objects

```python
class ConditionalGameplayEffect(StructBase)
```

Struct for gameplay effects that apply only if another gameplay effect (or execution) was successfully applied.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effect_class`` (type(Class)):  [Read-Write] gameplay effect that will be applied to the target
- ``required_source_tags`` (GameplayTagContainer):  [Read-Write] Tags that the source must have for this GE to apply.  If this is blank, then there are no requirements to apply the EffectClass.

<a id="unreal.ConditionalGameplayEffect.__init__"></a>

#### \_\_init\_\_

```python
def __init__(effect_class: Class = None,
             required_source_tags: GameplayTagContainer = [[]]) -> None
```

<a id="unreal.ConditionalGameplayEffect.effect_class"></a>

#### effect\_class

```python
@property
def effect_class() -> Class
```

(type(Class)):  [Read-Only] gameplay effect that will be applied to the target

<a id="unreal.ConditionalGameplayEffect.required_source_tags"></a>

#### required\_source\_tags

```python
@property
def required_source_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Only] Tags that the source must have for this GE to apply.  If this is blank, then there are no requirements to apply the EffectClass.

<a id="unreal.GameplayEffectExecutionDefinition"></a>