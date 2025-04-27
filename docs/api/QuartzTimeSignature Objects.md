## QuartzTimeSignature Objects

```python
class QuartzTimeSignature(StructBase)
```

Quartz Time Signature

**C++ Source:**

- **Module**: Engine
- **File**: QuartzQuantizationUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``beat_type`` (QuartzTimeSignatureQuantization):  [Read-Write] denominator
- ``num_beats`` (int32):  [Read-Write] numerator
- ``optional_pulse_override`` (Array[QuartzPulseOverrideStep]):  [Read-Write] beat override

<a id="unreal.QuartzTimeSignature.__init__"></a>

#### __init__

```python
def __init__(
        num_beats: int = 0,
        beat_type:
    QuartzTimeSignatureQuantization = QuartzTimeSignatureQuantization.
    HALF_NOTE,
        optional_pulse_override: Array[QuartzPulseOverrideStep] = []) -> None
```

<a id="unreal.QuartzTimeSignature.num_beats"></a>

#### num_beats

```python
@property
def num_beats() -> int
```

(int32):  [Read-Write] numerator

<a id="unreal.QuartzTimeSignature.num_beats"></a>

#### num_beats

```python
@num_beats.setter
def num_beats(value: int) -> None
```

<a id="unreal.QuartzTimeSignature.beat_type"></a>

#### beat_type

```python
@property
def beat_type() -> QuartzTimeSignatureQuantization
```

(QuartzTimeSignatureQuantization):  [Read-Write] denominator

<a id="unreal.QuartzTimeSignature.beat_type"></a>

#### beat_type

```python
@beat_type.setter
def beat_type(value: QuartzTimeSignatureQuantization) -> None
```

<a id="unreal.QuartzTimeSignature.optional_pulse_override"></a>

#### optional_pulse_override

```python
@property
def optional_pulse_override() -> Array[QuartzPulseOverrideStep]
```

(Array[QuartzPulseOverrideStep]):  [Read-Write] beat override

<a id="unreal.QuartzTimeSignature.optional_pulse_override"></a>

#### optional_pulse_override

```python
@optional_pulse_override.setter
def optional_pulse_override(value: Array[QuartzPulseOverrideStep]) -> None
```

<a id="unreal.QuartzTransportTimeStamp"></a>