## QuartzPulseOverrideStep Objects

```python
class QuartzPulseOverrideStep(StructBase)
```

Allows the user to specify non-uniform beat durations in odd meters

**C++ Source:**

- **Module**: Engine
- **File**: QuartzQuantizationUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``number_of_pulses`` (int32):  [Read-Write] The number of pulses for this beat duration
- ``pulse_duration`` (QuartzCommandQuantization):  [Read-Write] This Beat duration

<a id="unreal.QuartzPulseOverrideStep.__init__"></a>

#### __init__

```python
def __init__(
    number_of_pulses: int = 0,
    pulse_duration: QuartzCommandQuantization = QuartzCommandQuantization.BAR
) -> None
```

<a id="unreal.QuartzPulseOverrideStep.number_of_pulses"></a>

#### number_of_pulses

```python
@property
def number_of_pulses() -> int
```

(int32):  [Read-Write] The number of pulses for this beat duration

<a id="unreal.QuartzPulseOverrideStep.number_of_pulses"></a>

#### number_of_pulses

```python
@number_of_pulses.setter
def number_of_pulses(value: int) -> None
```

<a id="unreal.QuartzPulseOverrideStep.pulse_duration"></a>

#### pulse_duration

```python
@property
def pulse_duration() -> QuartzCommandQuantization
```

(QuartzCommandQuantization):  [Read-Write] This Beat duration

<a id="unreal.QuartzPulseOverrideStep.pulse_duration"></a>

#### pulse_duration

```python
@pulse_duration.setter
def pulse_duration(value: QuartzCommandQuantization) -> None
```

<a id="unreal.QuartzTimeSignature"></a>