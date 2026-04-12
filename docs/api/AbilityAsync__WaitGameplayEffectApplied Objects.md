## AbilityAsync\_WaitGameplayEffectApplied Objects

```python
class AbilityAsync_WaitGameplayEffectApplied(AbilityAsync)
```

This action listens for specific gameplay effect applications based off specified tags.
Effects themselves are not replicated; rather the tags they grant, the attributes they
change, and the gameplay cues they emit are replicated.
This will only listen for local server or predicted client effects.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityAsync_WaitGameplayEffectApplied.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_applied`` (OnAppliedDelegate):  [Read-Write]

<a id="unreal.AbilityAsync_WaitGameplayEffectApplied.on_applied"></a>

#### on\_applied

```python
@property
def on_applied() -> OnAppliedDelegate
```

(OnAppliedDelegate):  [Read-Write]

<a id="unreal.AbilityAsync_WaitGameplayEffectApplied.on_applied"></a>

#### on\_applied

```python
@on_applied.setter
def on_applied(value: OnAppliedDelegate) -> None
```

<a id="unreal.AbilityAsync_WaitGameplayEvent"></a>