## InputTriggerCombo Objects

```python
class InputTriggerCombo(InputTrigger)
```

UInputTriggerCombo
All actions in the combo array must be completed (based on combo completion event specified - triggered, completed, etc.) to trigger the action this trigger is on.
Actions must also be completed in the order specified by the combo actions array (starting at index 0).
Note: This will only trigger for one frame before resetting the combo trigger's progress

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actuation_threshold`` (float):  [Read-Write] Point at which this trigger fires
- ``combo_actions`` (Array[InputComboStepData]):  [Read-Write] List of input actions that need to be completed (according to Combo Step Completion States) to trigger this action.
  Input actions must be triggered in order (starting at index 0) to count towards the triggering of the combo.
- ``current_combo_step_index`` (int32):  [Read-Write] Keeps track of what action we're currently at in the combo
- ``current_time_between_combo_steps`` (float):  [Read-Write] Time elapsed between last combo InputAction trigger and current time
- ``input_cancel_actions`` (Array[InputCancelAction]):  [Read-Write] Actions that will cancel the combo if they are completed (according to Cancellation States)
- ``last_value`` (InputActionValue):  [Read-Write] Value passed to UpdateState on the previous tick. This will be updated automatically after the trigger is updated.
- ``should_always_tick`` (bool):  [Read-Write] Decides whether this trigger ticks every frame or not.
         * This WILL affect performance and should only be used in specific custom triggers.

<a id="unreal.InputTriggerCombo.current_combo_step_index"></a>

#### current_combo_step_index

```python
@property
def current_combo_step_index() -> int
```

(int32):  [Read-Only] Keeps track of what action we're currently at in the combo

<a id="unreal.InputTriggerCombo.current_time_between_combo_steps"></a>

#### current_time_between_combo_steps

```python
@property
def current_time_between_combo_steps() -> float
```

(float):  [Read-Only] Time elapsed between last combo InputAction trigger and current time

<a id="unreal.InputTriggerCombo.combo_actions"></a>

#### combo_actions

```python
@property
def combo_actions() -> Array[InputComboStepData]
```

(Array[InputComboStepData]):  [Read-Write] List of input actions that need to be completed (according to Combo Step Completion States) to trigger this action.
Input actions must be triggered in order (starting at index 0) to count towards the triggering of the combo.

<a id="unreal.InputTriggerCombo.combo_actions"></a>

#### combo_actions

```python
@combo_actions.setter
def combo_actions(value: Array[InputComboStepData]) -> None
```

<a id="unreal.InputTriggerCombo.input_cancel_actions"></a>

#### input_cancel_actions

```python
@property
def input_cancel_actions() -> Array[InputCancelAction]
```

(Array[InputCancelAction]):  [Read-Write] Actions that will cancel the combo if they are completed (according to Cancellation States)

<a id="unreal.InputTriggerCombo.input_cancel_actions"></a>

#### input_cancel_actions

```python
@input_cancel_actions.setter
def input_cancel_actions(value: Array[InputCancelAction]) -> None
```

<a id="unreal.PlayerMappableInputConfig"></a>