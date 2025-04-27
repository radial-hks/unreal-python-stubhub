## InputTriggerChordAction Objects

```python
class InputTriggerChordAction(InputTrigger)
```

UInputTriggerChordAction
Applies a chord action that must be triggering for this trigger's action to trigger

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actuation_threshold`` (float):  [Read-Write] Point at which this trigger fires
- ``chord_action`` (InputAction):  [Read-Write] The action that must be triggering for this trigger's action to trigger
- ``last_value`` (InputActionValue):  [Read-Write] Value passed to UpdateState on the previous tick. This will be updated automatically after the trigger is updated.
- ``should_always_tick`` (bool):  [Read-Write] Decides whether this trigger ticks every frame or not.
         * This WILL affect performance and should only be used in specific custom triggers.

<a id="unreal.InputTriggerChordAction.chord_action"></a>

#### chord_action

```python
@property
def chord_action() -> InputAction
```

(InputAction):  [Read-Write] The action that must be triggering for this trigger's action to trigger

<a id="unreal.InputTriggerChordAction.chord_action"></a>

#### chord_action

```python
@chord_action.setter
def chord_action(value: InputAction) -> None
```

<a id="unreal.InputTriggerChordBlocker"></a>