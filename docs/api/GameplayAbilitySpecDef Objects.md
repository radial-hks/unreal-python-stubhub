## GameplayAbilitySpecDef Objects

```python
class GameplayAbilitySpecDef(StructBase)
```

This is data that can be used to create an FGameplayAbilitySpec. Has some data that is only relevant when granted by a GameplayEffect

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilitySpec.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ability`` (type(Class)):  [Read-Write] What ability to grant
- ``input_id`` (int32):  [Read-Write] Input ID to bind this ability to
- ``level_scalable_float`` (ScalableFloat):  [Read-Write] What level to grant this ability at
- ``removal_policy`` (GameplayEffectGrantedAbilityRemovePolicy):  [Read-Write] What will remove this ability later

<a id="unreal.GameplayAbilitySpecDef.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.ScalableFloat"></a>