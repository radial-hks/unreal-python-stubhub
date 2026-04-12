## AbilityAsync\_WaitGameplayTagQuery Objects

```python
class AbilityAsync_WaitGameplayTagQuery(AbilityAsync)
```

This class defines an async node to wait on a gameplay tag query.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityAsync_WaitGameplayTagQuery.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``triggered`` (AsyncWaitGameplayTagQueryDelegate):  [Read-Write] This delegate will be triggered when the trigger condition has been met.

<a id="unreal.AbilityAsync_WaitGameplayTagQuery.triggered"></a>

#### triggered

```python
@property
def triggered() -> AsyncWaitGameplayTagQueryDelegate
```

(AsyncWaitGameplayTagQueryDelegate):  [Read-Write] This delegate will be triggered when the trigger condition has been met.

<a id="unreal.AbilityAsync_WaitGameplayTagQuery.triggered"></a>

#### triggered

```python
@triggered.setter
def triggered(value: AsyncWaitGameplayTagQueryDelegate) -> None
```

<a id="unreal.GameplayAbility"></a>