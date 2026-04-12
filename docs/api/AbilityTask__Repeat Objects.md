## AbilityTask\_Repeat Objects

```python
class AbilityTask_Repeat(AbilityTask)
```

Repeat a task a certain number of times at a given interval.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_Repeat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_finished`` (RepeatedActionDelegate):  [Read-Write]
- ``on_perform_action`` (RepeatedActionDelegate):  [Read-Write]

<a id="unreal.AbilityTask_Repeat.on_perform_action"></a>

#### on\_perform\_action

```python
@property
def on_perform_action() -> RepeatedActionDelegate
```

(RepeatedActionDelegate):  [Read-Write]

<a id="unreal.AbilityTask_Repeat.on_perform_action"></a>

#### on\_perform\_action

```python
@on_perform_action.setter
def on_perform_action(value: RepeatedActionDelegate) -> None
```

<a id="unreal.AbilityTask_Repeat.on_finished"></a>

#### on\_finished

```python
@property
def on_finished() -> RepeatedActionDelegate
```

(RepeatedActionDelegate):  [Read-Write]

<a id="unreal.AbilityTask_Repeat.on_finished"></a>

#### on\_finished

```python
@on_finished.setter
def on_finished(value: RepeatedActionDelegate) -> None
```

<a id="unreal.AbilityTask_SpawnActor"></a>