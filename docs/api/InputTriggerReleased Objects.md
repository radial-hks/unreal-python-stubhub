## InputTriggerReleased Objects

```python
class InputTriggerReleased(InputTrigger)
```

UInputTriggerReleased
      Trigger returns Ongoing whilst input exceeds the actuation threshold.
      Trigger fires once only when input drops back below actuation threshold.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actuation_threshold`` (float):  [Read-Write] Point at which this trigger fires
- ``last_value`` (InputActionValue):  [Read-Write] Value passed to UpdateState on the previous tick. This will be updated automatically after the trigger is updated.
- ``should_always_tick`` (bool):  [Read-Write] Decides whether this trigger ticks every frame or not.
         * This WILL affect performance and should only be used in specific custom triggers.

<a id="unreal.InputTriggerHold"></a>