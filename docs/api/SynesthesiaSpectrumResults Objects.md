## SynesthesiaSpectrumResults Objects

```python
class SynesthesiaSpectrumResults(StructBase)
```

The results of the spectrum analysis.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: SynesthesiaSpectrumAnalysis.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``spectrum_values`` (Array[float]):  [Read-Write] The spectrum values from the FFT
- ``time_seconds`` (float):  [Read-Write] The time in seconds since analysis began of this SynesthesiaSpectrumAnalysis analysis result

<a id="unreal.SynesthesiaSpectrumResults.__init__"></a>

#### __init__

```python
def __init__(time_seconds: float = 0.000000,
             spectrum_values: Array[float] = []) -> None
```

<a id="unreal.SynesthesiaSpectrumResults.time_seconds"></a>

#### time_seconds

```python
@property
def time_seconds() -> float
```

(float):  [Read-Only] The time in seconds since analysis began of this SynesthesiaSpectrumAnalysis analysis result

<a id="unreal.SynesthesiaSpectrumResults.spectrum_values"></a>

#### spectrum_values

```python
@property
def spectrum_values() -> Array[float]
```

(Array[float]):  [Read-Only] The spectrum values from the FFT

<a id="unreal.CustomMeshTriangle"></a>