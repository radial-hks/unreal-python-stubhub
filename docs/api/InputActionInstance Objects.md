## InputActionInstance Objects

```python
class InputActionInstance(StructBase)
```

Run time queryable action instance
Generated from UInputAction templates above

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputAction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``elapsed_processed_time`` (float):  [Read-Write] Total trigger processing/evaluation time (How long this action has been in event Started, Ongoing, or Triggered
- ``elapsed_triggered_time`` (float):  [Read-Write] Triggered time (How long this action has been in event Triggered only)
- ``last_triggered_world_time`` (float):  [Read-Write] The last time that this evaluated to a Triggered State
- ``modifiers`` (Array[InputModifier]):  [Read-Write]
- ``source_action`` (InputAction):  [Read-Write] The source action that this instance is created from
- ``trigger_event`` (TriggerEvent):  [Read-Write] Trigger state
- ``triggers`` (Array[InputTrigger]):  [Read-Write]

<a id="unreal.InputActionInstance.__init__"></a>

#### __init__

```python
def __init__(source_action: InputAction = None,
             trigger_event: TriggerEvent = 0,
             last_triggered_world_time: float = 0.000000,
             triggers: Array[InputTrigger] = [],
             modifiers: Array[InputModifier] = [],
             elapsed_processed_time: float = 0.000000,
             elapsed_triggered_time: float = 0.000000) -> None
```

<a id="unreal.InputActionInstance.source_action"></a>

#### source_action

```python
@property
def source_action() -> InputAction
```

(InputAction):  [Read-Only] The source action that this instance is created from

<a id="unreal.InputActionInstance.trigger_event"></a>

#### trigger_event

```python
@property
def trigger_event() -> TriggerEvent
```

(TriggerEvent):  [Read-Only] Trigger state

<a id="unreal.InputActionInstance.last_triggered_world_time"></a>

#### last_triggered_world_time

```python
@property
def last_triggered_world_time() -> float
```

(float):  [Read-Only] The last time that this evaluated to a Triggered State

<a id="unreal.InputActionInstance.triggers"></a>

#### triggers

```python
@property
def triggers() -> Array[InputTrigger]
```

(Array[InputTrigger]):  [Read-Only]

<a id="unreal.InputActionInstance.modifiers"></a>

#### modifiers

```python
@property
def modifiers() -> Array[InputModifier]
```

(Array[InputModifier]):  [Read-Only]

<a id="unreal.InputActionInstance.elapsed_processed_time"></a>

#### elapsed_processed_time

```python
@property
def elapsed_processed_time() -> float
```

(float):  [Read-Only] Total trigger processing/evaluation time (How long this action has been in event Started, Ongoing, or Triggered

<a id="unreal.InputActionInstance.elapsed_triggered_time"></a>

#### elapsed_triggered_time

```python
@property
def elapsed_triggered_time() -> float
```

(float):  [Read-Only] Triggered time (How long this action has been in event Triggered only)

<a id="unreal.InputComboStepData"></a>