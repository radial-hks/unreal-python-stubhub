## MeterResults Objects

```python
class MeterResults(StructBase)
```

The results of the meter analysis.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: Meter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clipping_value`` (float):  [Read-Write] The value (if non-zero) if clipping was detected above the clipping threshold
- ``meter_value`` (float):  [Read-Write] The meter value
- ``num_samples_clipping`` (int32):  [Read-Write] The number of samples in the period which were above the clipping threshold. Will be 0 if no clipping was detected.
- ``peak_value`` (float):  [Read-Write] The peak value
- ``time_seconds`` (float):  [Read-Write] The time in seconds since analysis began of this meter analysis result

<a id="unreal.MeterResults.__init__"></a>

#### __init__

```python
def __init__(time_seconds: float = 0.000000,
             meter_value: float = 0.000000,
             peak_value: float = 0.000000,
             num_samples_clipping: int = 0,
             clipping_value: float = 0.000000) -> None
```

<a id="unreal.MeterResults.time_seconds"></a>

#### time_seconds

```python
@property
def time_seconds() -> float
```

(float):  [Read-Only] The time in seconds since analysis began of this meter analysis result

<a id="unreal.MeterResults.meter_value"></a>

#### meter_value

```python
@property
def meter_value() -> float
```

(float):  [Read-Only] The meter value

<a id="unreal.MeterResults.peak_value"></a>

#### peak_value

```python
@property
def peak_value() -> float
```

(float):  [Read-Only] The peak value

<a id="unreal.MeterResults.num_samples_clipping"></a>

#### num_samples_clipping

```python
@property
def num_samples_clipping() -> int
```

(int32):  [Read-Only] The number of samples in the period which were above the clipping threshold. Will be 0 if no clipping was detected.

<a id="unreal.MeterResults.clipping_value"></a>

#### clipping_value

```python
@property
def clipping_value() -> float
```

(float):  [Read-Only] The value (if non-zero) if clipping was detected above the clipping threshold

<a id="unreal.SynesthesiaSpectrumResults"></a>