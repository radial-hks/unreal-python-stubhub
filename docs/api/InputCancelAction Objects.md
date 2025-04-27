## InputCancelAction Objects

```python
class InputCancelAction(StructBase)
```

Input Cancel Action

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cancel_action`` (InputAction):  [Read-Write] The action that must be completed (according to Cancellation States) to cancel the combo
- ``cancellation_states`` (uint8):  [Read-Write] Trigger events for this action that will cancel the combo - what events from this action should cancel the combo

<a id="unreal.InputCancelAction.__init__"></a>

#### __init__

```python
def __init__(cancel_action: InputAction = None,
             cancellation_states: int = 0) -> None
```

<a id="unreal.InputCancelAction.cancel_action"></a>

#### cancel_action

```python
@property
def cancel_action() -> InputAction
```

(InputAction):  [Read-Write] The action that must be completed (according to Cancellation States) to cancel the combo

<a id="unreal.InputCancelAction.cancel_action"></a>

#### cancel_action

```python
@cancel_action.setter
def cancel_action(value: InputAction) -> None
```

<a id="unreal.InputCancelAction.cancellation_states"></a>

#### cancellation_states

```python
@property
def cancellation_states() -> int
```

(uint8):  [Read-Write] Trigger events for this action that will cancel the combo - what events from this action should cancel the combo

<a id="unreal.InputCancelAction.cancellation_states"></a>

#### cancellation_states

```python
@cancellation_states.setter
def cancellation_states(value: int) -> None
```

<a id="unreal.DisplayClusterClusterEventBase"></a>