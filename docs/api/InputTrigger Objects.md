## InputTrigger Objects

```python
class InputTrigger(Object)
```

Base class for building triggers.
Transitions to Triggered state once the input meets or exceeds the actuation threshold.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actuation_threshold`` (float):  [Read-Write] Point at which this trigger fires
- ``last_value`` (InputActionValue):  [Read-Write] Value passed to UpdateState on the previous tick. This will be updated automatically after the trigger is updated.
- ``should_always_tick`` (bool):  [Read-Write] Decides whether this trigger ticks every frame or not.
         * This WILL affect performance and should only be used in specific custom triggers.

<a id="unreal.InputTrigger.actuation_threshold"></a>

#### actuation_threshold

```python
@property
def actuation_threshold() -> float
```

(float):  [Read-Write] Point at which this trigger fires

<a id="unreal.InputTrigger.actuation_threshold"></a>

#### actuation_threshold

```python
@actuation_threshold.setter
def actuation_threshold(value: float) -> None
```

<a id="unreal.InputTrigger.should_always_tick"></a>

#### should_always_tick

```python
@property
def should_always_tick() -> bool
```

(bool):  [Read-Only] Decides whether this trigger ticks every frame or not.
       * This WILL affect performance and should only be used in specific custom triggers.

<a id="unreal.InputTrigger.last_value"></a>

#### last_value

```python
@property
def last_value() -> InputActionValue
```

(InputActionValue):  [Read-Only] Value passed to UpdateState on the previous tick. This will be updated automatically after the trigger is updated.

<a id="unreal.InputTrigger.update_state"></a>

#### update_state

```python
def update_state(player_input: EnhancedPlayerInput,
                 modified_value: InputActionValue,
                 delta_time: float) -> TriggerState
```

x.update_state(player_input, modified_value, delta_time) -> TriggerState
This function checks if the requisite conditions have been met for the trigger to fire.
 Returns Trigger State None              - No trigger conditions have been met. Trigger is inactive.
                 Trigger State Ongoing   - Some trigger conditions have been met. Trigger is processing but not yet active.
                 Trigger State Triggered - All trigger conditions have been met to fire. Trigger is active.

Args:
    player_input (EnhancedPlayerInput): 
    modified_value (InputActionValue): 
    delta_time (float): 

Returns:
    TriggerState:

<a id="unreal.InputTrigger.is_actuated"></a>

#### is_actuated

```python
def is_actuated(for_value: InputActionValue) -> bool
```

x.is_actuated(for_value) -> bool
* Is the value passed in sufficiently large to be of interest to the trigger.
* This is a helper function that implements the most obvious (>=) interpretation of the actuation threshold.

Args:
    for_value (InputActionValue): 

Returns:
    bool:

<a id="unreal.InputTrigger.get_trigger_type"></a>

#### get_trigger_type

```python
def get_trigger_type() -> TriggerType
```

x.get_trigger_type() -> TriggerType
Changes the way this trigger affects an action with multiple triggers:
        All implicit triggers must be triggering to trigger the action.
        If there are any explicit triggers at least one must be triggering to trigger the action.

Returns:
    TriggerType:

<a id="unreal.InputTriggerTimedBase"></a>