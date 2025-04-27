## InputTriggerTimedBase Objects

```python
class InputTriggerTimedBase(InputTrigger)
```

Base class for building triggers that have firing conditions governed by elapsed time.
This class transitions state to Ongoing once input is actuated, and will track Ongoing input time until input is released.
Inheriting classes should provide the logic for Triggered transitions.

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

<a id="unreal.InputTriggerTimedBase.held_duration"></a>

#### held_duration

```python
@property
def held_duration() -> float
```

(float):  [Read-Write] How long have we been actuating this trigger?

<a id="unreal.InputTriggerTimedBase.held_duration"></a>

#### held_duration

```python
@held_duration.setter
def held_duration(value: float) -> None
```

<a id="unreal.InputTriggerTimedBase.affected_by_time_dilation"></a>

#### affected_by_time_dilation

```python
@property
def affected_by_time_dilation() -> bool
```

(bool):  [Read-Write] Should global time dilation be applied to the held duration?
Default is set to false.

If this is set to true, then the owning Player Controller's actor time dilation
will be used when calculating the HeldDuration.
see: UInputTriggerTimedBase::CalculateHeldDuration
see: AWorldSettings::GetEffectiveTimeDilation

<a id="unreal.InputTriggerTimedBase.affected_by_time_dilation"></a>

#### affected_by_time_dilation

```python
@affected_by_time_dilation.setter
def affected_by_time_dilation(value: bool) -> None
```

<a id="unreal.InputTriggerDown"></a>