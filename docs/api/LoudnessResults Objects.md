## LoudnessResults Objects

```python
class LoudnessResults(StructBase)
```

The results of the loudness analyis.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: Loudness.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``loudness`` (float):  [Read-Write] The raw loudness value in dB
- ``normalized_loudness`` (float):  [Read-Write] The normalized loudness
- ``perceptual_energy`` (float):  [Read-Write] The normalized loudness
- ``time_seconds`` (float):  [Read-Write] The time in seconds since analysis began

<a id="unreal.LoudnessResults.__init__"></a>

#### __init__

```python
def __init__(loudness: float = 0.000000,
             normalized_loudness: float = 0.000000,
             perceptual_energy: float = 0.000000,
             time_seconds: float = 0.000000) -> None
```

<a id="unreal.LoudnessResults.loudness"></a>

#### loudness

```python
@property
def loudness() -> float
```

(float):  [Read-Only] The raw loudness value in dB

<a id="unreal.LoudnessResults.normalized_loudness"></a>

#### normalized_loudness

```python
@property
def normalized_loudness() -> float
```

(float):  [Read-Only] The normalized loudness

<a id="unreal.LoudnessResults.perceptual_energy"></a>

#### perceptual_energy

```python
@property
def perceptual_energy() -> float
```

(float):  [Read-Only] The normalized loudness

<a id="unreal.LoudnessResults.time_seconds"></a>

#### time_seconds

```python
@property
def time_seconds() -> float
```

(float):  [Read-Only] The time in seconds since analysis began

<a id="unreal.MeterResults"></a>