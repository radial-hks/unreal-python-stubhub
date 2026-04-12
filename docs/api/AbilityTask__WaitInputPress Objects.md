## AbilityTask\_WaitInputPress Objects

```python
class AbilityTask_WaitInputPress(AbilityTask)
```

Waits until the input is pressed from activating an ability. This should be true immediately upon starting the ability, since the key was pressed to activate it.
We expect server to execute this task in parallel and keep its own time. We do not keep track of

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_WaitInputPress.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_press`` (InputPressDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitInputPress.on_press"></a>

#### on\_press

```python
@property
def on_press() -> InputPressDelegate
```

(InputPressDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitInputPress.on_press"></a>

#### on\_press

```python
@on_press.setter
def on_press(value: InputPressDelegate) -> None
```

<a id="unreal.AbilityTask_WaitInputRelease"></a>