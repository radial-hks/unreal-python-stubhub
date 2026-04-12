## AbilityTask\_StartAbilityState Objects

```python
class AbilityTask_StartAbilityState(AbilityTask)
```

An ability state is simply an ability task that provides a way to handle the ability being interrupted.
You can use ability states to do state-specific cleanup if the ability ends or was interrupted at a certain point during it's execution.

An ability state will always result in either 'OnStateEnded' or 'OnStateInterrupted' being called.

'OnStateEnded' will be called if:
- The ability itself ends via AGameplayAbility::EndAbility
- The ability state is manually ended via AGameplayAbility::EndAbilityState
- Another ability state is started will 'bEndCurrentState' set to true

'OnStateInterrupted' will be called if:
- The ability itself is cancelled via AGameplayAbility::CancelAbility

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_StartAbilityState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_state_ended`` (AbilityStateDelegate):  [Read-Write] Invoked if 'EndAbilityState' is called or if 'EndAbility' is called and this state is active.
- ``on_state_interrupted`` (AbilityStateDelegate):  [Read-Write] Invoked if the ability was interrupted and this state is active.

<a id="unreal.AbilityTask_StartAbilityState.on_state_ended"></a>

#### on\_state\_ended

```python
@property
def on_state_ended() -> AbilityStateDelegate
```

(AbilityStateDelegate):  [Read-Write] Invoked if 'EndAbilityState' is called or if 'EndAbility' is called and this state is active.

<a id="unreal.AbilityTask_StartAbilityState.on_state_ended"></a>

#### on\_state\_ended

```python
@on_state_ended.setter
def on_state_ended(value: AbilityStateDelegate) -> None
```

<a id="unreal.AbilityTask_StartAbilityState.on_state_interrupted"></a>

#### on\_state\_interrupted

```python
@property
def on_state_interrupted() -> AbilityStateDelegate
```

(AbilityStateDelegate):  [Read-Write] Invoked if the ability was interrupted and this state is active.

<a id="unreal.AbilityTask_StartAbilityState.on_state_interrupted"></a>

#### on\_state\_interrupted

```python
@on_state_interrupted.setter
def on_state_interrupted(value: AbilityStateDelegate) -> None
```

<a id="unreal.AbilityTask_VisualizeTargeting"></a>