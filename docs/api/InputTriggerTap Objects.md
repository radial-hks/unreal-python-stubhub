## InputTriggerTap Objects

```python
class InputTriggerTap(InputTriggerTimedBase)
```

UInputTriggerTap
      Input must be actuated then released within TapReleaseTimeThreshold seconds to trigger.

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
- ``last_value`` (InputActionValue):  [Read-Write] Value passed to UpdateState on the previous tick. This will be updated automatically after the trigger is updated.
- ``should_always_tick`` (bool):  [Read-Write] Decides whether this trigger ticks every frame or not.
         * This WILL affect performance and should only be used in specific custom triggers.
- ``tap_release_time_threshold`` (float):  [Read-Write] Release within this time-frame to trigger a tap

<a id="unreal.InputTriggerTap.tap_release_time_threshold"></a>

#### tap_release_time_threshold

```python
@property
def tap_release_time_threshold() -> float
```

(float):  [Read-Write] Release within this time-frame to trigger a tap

<a id="unreal.InputTriggerTap.tap_release_time_threshold"></a>

#### tap_release_time_threshold

```python
@tap_release_time_threshold.setter
def tap_release_time_threshold(value: float) -> None
```

<a id="unreal.InputTriggerPulse"></a>