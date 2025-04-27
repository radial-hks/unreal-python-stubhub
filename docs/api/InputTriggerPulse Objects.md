## InputTriggerPulse Objects

```python
class InputTriggerPulse(InputTriggerTimedBase)
```

UInputTriggerPulse
      Trigger that fires at an Interval, in seconds, while input is actuated.
      Note:   Completed only fires when the repeat limit is reached or when input is released immediately after being triggered.
                      Otherwise, Canceled is fired when input is released.

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
- ``interval`` (float):  [Read-Write] How long between each trigger fire while input is held, in seconds?
- ``last_value`` (InputActionValue):  [Read-Write] Value passed to UpdateState on the previous tick. This will be updated automatically after the trigger is updated.
- ``should_always_tick`` (bool):  [Read-Write] Decides whether this trigger ticks every frame or not.
         * This WILL affect performance and should only be used in specific custom triggers.
- ``trigger_limit`` (int32):  [Read-Write] How many times can the trigger fire while input is held? (0 = no limit)
- ``trigger_on_start`` (bool):  [Read-Write] Whether to trigger when the input first exceeds the actuation threshold or wait for the first interval?

<a id="unreal.InputTriggerPulse.trigger_on_start"></a>

#### trigger_on_start

```python
@property
def trigger_on_start() -> bool
```

(bool):  [Read-Write] Whether to trigger when the input first exceeds the actuation threshold or wait for the first interval?

<a id="unreal.InputTriggerPulse.trigger_on_start"></a>

#### trigger_on_start

```python
@trigger_on_start.setter
def trigger_on_start(value: bool) -> None
```

<a id="unreal.InputTriggerPulse.interval"></a>

#### interval

```python
@property
def interval() -> float
```

(float):  [Read-Write] How long between each trigger fire while input is held, in seconds?

<a id="unreal.InputTriggerPulse.interval"></a>

#### interval

```python
@interval.setter
def interval(value: float) -> None
```

<a id="unreal.InputTriggerPulse.trigger_limit"></a>

#### trigger_limit

```python
@property
def trigger_limit() -> int
```

(int32):  [Read-Write] How many times can the trigger fire while input is held? (0 = no limit)

<a id="unreal.InputTriggerPulse.trigger_limit"></a>

#### trigger_limit

```python
@trigger_limit.setter
def trigger_limit(value: int) -> None
```

<a id="unreal.InputTriggerChordAction"></a>