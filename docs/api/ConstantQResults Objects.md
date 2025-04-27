## ConstantQResults Objects

```python
class ConstantQResults(StructBase)
```

The results of the ConstantQ analysis.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: ConstantQ.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``spectrum_values`` (Array[float]):  [Read-Write] The spectrum values from the FFT
- ``time_seconds`` (float):  [Read-Write] The time in seconds since analysis began of this ConstantQ analysis result

<a id="unreal.ConstantQResults.__init__"></a>

#### __init__

```python
def __init__(time_seconds: float = 0.000000,
             spectrum_values: Array[float] = []) -> None
```

<a id="unreal.ConstantQResults.time_seconds"></a>

#### time_seconds

```python
@property
def time_seconds() -> float
```

(float):  [Read-Only] The time in seconds since analysis began of this ConstantQ analysis result

<a id="unreal.ConstantQResults.spectrum_values"></a>

#### spectrum_values

```python
@property
def spectrum_values() -> Array[float]
```

(Array[float]):  [Read-Only] The spectrum values from the FFT

<a id="unreal.LoudnessResults"></a>