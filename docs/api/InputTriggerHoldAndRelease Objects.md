## InputTriggerHoldAndRelease Objects

```python
class InputTriggerHoldAndRelease(InputTriggerTimedBase)
```

UInputTriggerHoldAndRelease
      Trigger fires when input is released after having been actuated for at least HoldTimeThreshold seconds.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actuation_threshold`` (float):  [Read-Write] Point at which this trigger fires
- ``affected_by_time_dilation`` (bool):  [Read-Write] Should global time dilation be applied to the held duration?
  Default is set to false.

  If this is set to true, then the owning Player Controller's actor time dilation
  will be used when calculating the HeldDuration.
  see: UInputTriggerTimedBase::CalculateHeldDuration
  see: AWorldSettings::GetEffectiveTimeDilation
- ``held_duration`` (float):  [Read-Write] How long have we been actuating this trigger?
- ``hold_time_threshold`` (float):  [Read-Write] How long does the input have to be held to cause trigger?
- ``last_value`` (InputActionValue):  [Read-Write] Value passed to UpdateState on the previous tick. This will be updated automatically after the trigger is updated.
- ``should_always_tick`` (bool):  [Read-Write] Decides whether this trigger ticks every frame or not.
         * This WILL affect performance and should only be used in specific custom triggers.

<a id="unreal.InputTriggerHoldAndRelease.hold_time_threshold"></a>

#### hold_time_threshold

```python
@property
def hold_time_threshold() -> float
```

(float):  [Read-Write] How long does the input have to be held to cause trigger?

<a id="unreal.InputTriggerHoldAndRelease.hold_time_threshold"></a>

#### hold_time_threshold

```python
@hold_time_threshold.setter
def hold_time_threshold(value: float) -> None
```

<a id="unreal.InputTriggerTap"></a>