## QuartzQuantizationBoundary Objects

```python
class QuartzQuantizationBoundary(StructBase)
```

struct used to specify the quantization boundary of an event

**C++ Source:**

- **Module**: Engine
- **File**: QuartzQuantizationUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cancel_command_if_clock_is_not_running`` (bool):  [Read-Write] If this is true, this command will be canceled if the Clock is stopped or otherwise not running
- ``counting_reference_point`` (QuarztQuantizationReference):  [Read-Write]
- ``fire_on_clock_start`` (bool):  [Read-Write] If this is true and the Clock hasn't started yet, the event will fire immediately when the Clock starts
- ``multiplier`` (float):  [Read-Write] how many "Resolutions" to wait before the onset we care about
- ``quantization`` (QuartzCommandQuantization):  [Read-Write] resolution we are interested in
- ``reset_clock_on_queued`` (bool):  [Read-Write] If this is true, queueing the sound will also call a Reset Clock command
- ``resume_clock_on_queued`` (bool):  [Read-Write] If this is true, queueing the sound will also call a Resume Clock command

<a id="unreal.QuartzQuantizationBoundary.__init__"></a>

#### __init__

```python
def __init__(
        quantization: QuartzCommandQuantization = QuartzCommandQuantization.
    BAR,
        multiplier: float = 0.000000,
        counting_reference_point:
    QuarztQuantizationReference = QuarztQuantizationReference.BAR_RELATIVE,
        fire_on_clock_start: bool = False,
        cancel_command_if_clock_is_not_running: bool = False,
        reset_clock_on_queued: bool = False,
        resume_clock_on_queued: bool = False) -> None
```

<a id="unreal.QuartzQuantizationBoundary.quantization"></a>

#### quantization

```python
@property
def quantization() -> QuartzCommandQuantization
```

(QuartzCommandQuantization):  [Read-Write] resolution we are interested in

<a id="unreal.QuartzQuantizationBoundary.quantization"></a>

#### quantization

```python
@quantization.setter
def quantization(value: QuartzCommandQuantization) -> None
```

<a id="unreal.QuartzQuantizationBoundary.multiplier"></a>

#### multiplier

```python
@property
def multiplier() -> float
```

(float):  [Read-Write] how many "Resolutions" to wait before the onset we care about

<a id="unreal.QuartzQuantizationBoundary.multiplier"></a>

#### multiplier

```python
@multiplier.setter
def multiplier(value: float) -> None
```

<a id="unreal.QuartzQuantizationBoundary.counting_reference_point"></a>

#### counting_reference_point

```python
@property
def counting_reference_point() -> QuarztQuantizationReference
```

(QuarztQuantizationReference):  [Read-Write]

<a id="unreal.QuartzQuantizationBoundary.counting_reference_point"></a>

#### counting_reference_point

```python
@counting_reference_point.setter
def counting_reference_point(value: QuarztQuantizationReference) -> None
```

<a id="unreal.QuartzQuantizationBoundary.fire_on_clock_start"></a>

#### fire_on_clock_start

```python
@property
def fire_on_clock_start() -> bool
```

(bool):  [Read-Write] If this is true and the Clock hasn't started yet, the event will fire immediately when the Clock starts

<a id="unreal.QuartzQuantizationBoundary.fire_on_clock_start"></a>

#### fire_on_clock_start

```python
@fire_on_clock_start.setter
def fire_on_clock_start(value: bool) -> None
```

<a id="unreal.QuartzQuantizationBoundary.cancel_command_if_clock_is_not_running"></a>

#### cancel_command_if_clock_is_not_running

```python
@property
def cancel_command_if_clock_is_not_running() -> bool
```

(bool):  [Read-Write] If this is true, this command will be canceled if the Clock is stopped or otherwise not running

<a id="unreal.QuartzQuantizationBoundary.cancel_command_if_clock_is_not_running"></a>

#### cancel_command_if_clock_is_not_running

```python
@cancel_command_if_clock_is_not_running.setter
def cancel_command_if_clock_is_not_running(value: bool) -> None
```

<a id="unreal.QuartzQuantizationBoundary.reset_clock_on_queued"></a>

#### reset_clock_on_queued

```python
@property
def reset_clock_on_queued() -> bool
```

(bool):  [Read-Write] If this is true, queueing the sound will also call a Reset Clock command

<a id="unreal.QuartzQuantizationBoundary.reset_clock_on_queued"></a>

#### reset_clock_on_queued

```python
@reset_clock_on_queued.setter
def reset_clock_on_queued(value: bool) -> None
```

<a id="unreal.QuartzQuantizationBoundary.resume_clock_on_queued"></a>

#### resume_clock_on_queued

```python
@property
def resume_clock_on_queued() -> bool
```

(bool):  [Read-Write] If this is true, queueing the sound will also call a Resume Clock command

<a id="unreal.QuartzQuantizationBoundary.resume_clock_on_queued"></a>

#### resume_clock_on_queued

```python
@resume_clock_on_queued.setter
def resume_clock_on_queued(value: bool) -> None
```

<a id="unreal.MovementProperties"></a>