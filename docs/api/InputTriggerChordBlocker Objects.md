## InputTriggerChordBlocker Objects

```python
class InputTriggerChordBlocker(InputTriggerChordAction)
```

UInputTriggerChordBlocker
      Automatically instantiated  to block mappings that are masked by a UInputTriggerChordAction chord from firing whilst the chording key is active.
      NOTE: Do not attempt to add these manually.

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

<a id="unreal.InputTriggerCombo"></a>