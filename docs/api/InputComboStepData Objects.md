## InputComboStepData Objects

```python
class InputComboStepData(StructBase)
```

Input Combo Step Data

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``combo_step_action`` (InputAction):  [Read-Write] The action that must be completed (according to Combo Step Completion States) to progress the combo
- ``combo_step_completion_states`` (uint8):  [Read-Write] Trigger events that will complete this step - what events from this action should progress the combo
- ``time_to_press_key`` (float):  [Read-Write] Time to press the key before combo is cancelled - starts once the previous step in the combo is completed
  Note: This can be safely ignored for the first action in the combo

<a id="unreal.InputComboStepData.__init__"></a>

#### __init__

```python
def __init__(combo_step_action: InputAction = None,
             combo_step_completion_states: int = 0,
             time_to_press_key: float = 0.000000) -> None
```

<a id="unreal.InputComboStepData.combo_step_action"></a>

#### combo_step_action

```python
@property
def combo_step_action() -> InputAction
```

(InputAction):  [Read-Write] The action that must be completed (according to Combo Step Completion States) to progress the combo

<a id="unreal.InputComboStepData.combo_step_action"></a>

#### combo_step_action

```python
@combo_step_action.setter
def combo_step_action(value: InputAction) -> None
```

<a id="unreal.InputComboStepData.combo_step_completion_states"></a>

#### combo_step_completion_states

```python
@property
def combo_step_completion_states() -> int
```

(uint8):  [Read-Write] Trigger events that will complete this step - what events from this action should progress the combo

<a id="unreal.InputComboStepData.combo_step_completion_states"></a>

#### combo_step_completion_states

```python
@combo_step_completion_states.setter
def combo_step_completion_states(value: int) -> None
```

<a id="unreal.InputComboStepData.time_to_press_key"></a>

#### time_to_press_key

```python
@property
def time_to_press_key() -> float
```

(float):  [Read-Write] Time to press the key before combo is cancelled - starts once the previous step in the combo is completed
Note: This can be safely ignored for the first action in the combo

<a id="unreal.InputComboStepData.time_to_press_key"></a>

#### time_to_press_key

```python
@time_to_press_key.setter
def time_to_press_key(value: float) -> None
```

<a id="unreal.InputCancelAction"></a>