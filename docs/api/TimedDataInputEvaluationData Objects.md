## TimedDataInputEvaluationData Objects

```python
class TimedDataInputEvaluationData(StructBase)
```

Timed Data Input Evaluation Data

**C++ Source:**

- **Module**: TimeManagement
- **File**: ITimedDataInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_to_newest_sample_seconds`` (float):  [Read-Write] Distance between evaluation time and newest sample in seconds
- ``distance_to_oldest_sample_seconds`` (float):  [Read-Write] Distance between evaluation time and newest sample in seconds

<a id="unreal.TimedDataInputEvaluationData.__init__"></a>

#### __init__

```python
def __init__(distance_to_newest_sample_seconds: float = 0.000000,
             distance_to_oldest_sample_seconds: float = 0.000000) -> None
```

<a id="unreal.TimedDataInputEvaluationData.distance_to_newest_sample_seconds"></a>

#### distance_to_newest_sample_seconds

```python
@property
def distance_to_newest_sample_seconds() -> float
```

(float):  [Read-Write] Distance between evaluation time and newest sample in seconds

<a id="unreal.TimedDataInputEvaluationData.distance_to_newest_sample_seconds"></a>

#### distance_to_newest_sample_seconds

```python
@distance_to_newest_sample_seconds.setter
def distance_to_newest_sample_seconds(value: float) -> None
```

<a id="unreal.TimedDataInputEvaluationData.distance_to_oldest_sample_seconds"></a>

#### distance_to_oldest_sample_seconds

```python
@property
def distance_to_oldest_sample_seconds() -> float
```

(float):  [Read-Write] Distance between evaluation time and newest sample in seconds

<a id="unreal.TimedDataInputEvaluationData.distance_to_oldest_sample_seconds"></a>

#### distance_to_oldest_sample_seconds

```python
@distance_to_oldest_sample_seconds.setter
def distance_to_oldest_sample_seconds(value: float) -> None
```

<a id="unreal.ActorForWorldTransforms"></a>