## TrajectorySamplingData Objects

```python
class TrajectorySamplingData(StructBase)
```

Trajectory Sampling Data

**C++ Source:**

- **Plugin**: MotionTrajectory
- **Module**: MotionTrajectory
- **File**: MotionTrajectoryLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``history_length_seconds`` (float):  [Read-Write] This should generally match the longest history required by a Motion Matching Database in the project.
  Motion Matching will use extrapolation to generate samples if the history doesn't contain enough samples.
- ``history_samples_per_second`` (int32):  [Read-Write] Higher values will cost more storage and processing time, but give higher accuracy.
- ``prediction_length_seconds`` (float):  [Read-Write] This should match the longest trajectory prediction required by a Motion Matching Database in the project.
  Motion Matching will use extrapolation to generate samples if the prediction doesn't contain enough samples.
- ``prediction_samples_per_second`` (int32):  [Read-Write] Higher values will cost more storage and processing time, but give higher accuracy.

<a id="unreal.TrajectorySamplingData.__init__"></a>

#### __init__

```python
def __init__(history_length_seconds: float = 0.000000,
             history_samples_per_second: int = 0,
             prediction_length_seconds: float = 0.000000,
             prediction_samples_per_second: int = 0) -> None
```

<a id="unreal.TrajectorySamplingData.history_length_seconds"></a>

#### history_length_seconds

```python
@property
def history_length_seconds() -> float
```

(float):  [Read-Only] This should generally match the longest history required by a Motion Matching Database in the project.
Motion Matching will use extrapolation to generate samples if the history doesn't contain enough samples.

<a id="unreal.TrajectorySamplingData.history_samples_per_second"></a>

#### history_samples_per_second

```python
@property
def history_samples_per_second() -> int
```

(int32):  [Read-Only] Higher values will cost more storage and processing time, but give higher accuracy.

<a id="unreal.TrajectorySamplingData.prediction_length_seconds"></a>

#### prediction_length_seconds

```python
@property
def prediction_length_seconds() -> float
```

(float):  [Read-Only] This should match the longest trajectory prediction required by a Motion Matching Database in the project.
Motion Matching will use extrapolation to generate samples if the prediction doesn't contain enough samples.

<a id="unreal.TrajectorySamplingData.prediction_samples_per_second"></a>

#### prediction_samples_per_second

```python
@property
def prediction_samples_per_second() -> int
```

(int32):  [Read-Only] Higher values will cost more storage and processing time, but give higher accuracy.

<a id="unreal.CharacterTrajectoryData"></a>