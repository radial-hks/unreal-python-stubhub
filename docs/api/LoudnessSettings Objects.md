## LoudnessSettings Objects

```python
class LoudnessSettings(AudioSynesthesiaSettings)
```

ULoudnessSettings

Settings for a ULoudness analyzer.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: Loudness.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``analysis_period`` (float):  [Read-Write] Number of seconds between loudness measurements
- ``curve_type`` (LoudnessCurveTypeEnum):  [Read-Write] Type of equal loudness curve used in calculations
- ``expected_max_loudness`` (float):  [Read-Write] dB level to denote silence.  Used when calculating normalized loudness.
- ``maximum_frequency`` (float):  [Read-Write] Maximum analysis frequency for calculating loudness.
- ``minimum_frequency`` (float):  [Read-Write] Minimum analysis frequency for calculating loudness.
- ``noise_floor_db`` (float):  [Read-Write] dB level to denote silence.  Used when calculating normalized loudness.

<a id="unreal.LoudnessSettings.analysis_period"></a>

#### analysis_period

```python
@property
def analysis_period() -> float
```

(float):  [Read-Only] Number of seconds between loudness measurements

<a id="unreal.LoudnessSettings.minimum_frequency"></a>

#### minimum_frequency

```python
@property
def minimum_frequency() -> float
```

(float):  [Read-Only] Minimum analysis frequency for calculating loudness.

<a id="unreal.LoudnessSettings.maximum_frequency"></a>

#### maximum_frequency

```python
@property
def maximum_frequency() -> float
```

(float):  [Read-Only] Maximum analysis frequency for calculating loudness.

<a id="unreal.LoudnessSettings.curve_type"></a>

#### curve_type

```python
@property
def curve_type() -> LoudnessCurveTypeEnum
```

(LoudnessCurveTypeEnum):  [Read-Only] Type of equal loudness curve used in calculations

<a id="unreal.LoudnessSettings.noise_floor_db"></a>

#### noise_floor_db

```python
@property
def noise_floor_db() -> float
```

(float):  [Read-Only] dB level to denote silence.  Used when calculating normalized loudness.

<a id="unreal.LoudnessSettings.expected_max_loudness"></a>

#### expected_max_loudness

```python
@property
def expected_max_loudness() -> float
```

(float):  [Read-Only] dB level to denote silence.  Used when calculating normalized loudness.

<a id="unreal.LoudnessAnalyzer"></a>