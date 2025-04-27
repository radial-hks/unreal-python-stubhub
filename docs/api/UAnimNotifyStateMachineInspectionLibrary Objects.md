## UAnimNotifyStateMachineInspectionLibrary Objects

```python
class UAnimNotifyStateMachineInspectionLibrary(BlueprintFunctionLibrary)
```

A library of commonly used functionality for Notifies related to state machines, exposed to blueprint.

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotifyStateMachineInspectionLibrary.h

<a id="unreal.UAnimNotifyStateMachineInspectionLibrary.is_triggered_by_state_machine"></a>

#### is_triggered_by_state_machine

```python
@classmethod
def is_triggered_by_state_machine(cls,
                                  event_reference: AnimNotifyEventReference,
                                  anim_instance: AnimInstance,
                                  state_machine_name: Name) -> bool
```

X.is_triggered_by_state_machine(event_reference, anim_instance, state_machine_name) -> bool
Get whether the notify was triggered from the specified state machine

Args:
    event_reference (AnimNotifyEventReference): The event to inspect
    anim_instance (AnimInstance): 
    state_machine_name (Name): The Name of a state machine to test

Returns:
    bool:

<a id="unreal.UAnimNotifyStateMachineInspectionLibrary.is_triggered_by_state_in_state_machine"></a>

#### is_triggered_by_state_in_state_machine

```python
@classmethod
def is_triggered_by_state_in_state_machine(
        cls, event_reference: AnimNotifyEventReference,
        anim_instance: AnimInstance, state_machine_name: Name,
        state_name: Name) -> bool
```

X.is_triggered_by_state_in_state_machine(event_reference, anim_instance, state_machine_name, state_name) -> bool
Get whether a particular state in a specific state machine triggered the notify

Args:
    event_reference (AnimNotifyEventReference): The event to inspect
    anim_instance (AnimInstance): 
    state_machine_name (Name): The name of a state machine to test
    state_name (Name): The name of a state to test

Returns:
    bool:

<a id="unreal.UAnimNotifyStateMachineInspectionLibrary.is_triggered_by_state"></a>

#### is_triggered_by_state

```python
@classmethod
def is_triggered_by_state(cls, event_reference: AnimNotifyEventReference,
                          anim_instance: AnimInstance,
                          state_name: Name) -> bool
```

X.is_triggered_by_state(event_reference, anim_instance, state_name) -> bool
Get whether a state with the given name in any state machine triggered the notify

Args:
    event_reference (AnimNotifyEventReference): The event to inspect
    anim_instance (AnimInstance): 
    state_name (Name): The name of a state to test

Returns:
    bool:

<a id="unreal.AnimNotifyState_DisableRootMotion"></a>