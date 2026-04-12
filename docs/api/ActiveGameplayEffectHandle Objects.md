## ActiveGameplayEffectHandle Objects

```python
class ActiveGameplayEffectHandle(StructBase)
```

This handle is required for things outside of FActiveGameplayEffectsContainer to refer to a specific active GameplayEffect
    For example if a skill needs to create an active effect and then destroy that specific effect that it created, it has to do so
    through a handle. a pointer or index into the active list is not sufficient. These are not synchronized between clients and server.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: ActiveGameplayEffectHandle.h

<a id="unreal.ActiveGameplayEffectHandle.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.ActiveGameplayEffectHandle.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``ActiveGameplayEffectHandle`` Equality operator for two Active Gameplay Effect Handles

<a id="unreal.ActiveGameplayEffectHandle.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``ActiveGameplayEffectHandle`` Inequality operator for two Active Gameplay Effect Handles

<a id="unreal.GameplayEffectSpecHandle"></a>