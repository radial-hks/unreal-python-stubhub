## MotionTrajectorySettings Objects

```python
class MotionTrajectorySettings(StructBase)
```

Specifies the chosen domain parameters for trajectory sample retention and creation

**C++ Source:**

- **Plugin**: MotionTrajectory
- **Module**: MotionTrajectory
- **File**: MotionTrajectory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``seconds`` (float):  [Read-Write] Sample time horizon

<a id="unreal.MotionTrajectorySettings.__init__"></a>

#### __init__

```python
def __init__(seconds: float = 0.000000) -> None
```

<a id="unreal.MotionTrajectorySettings.seconds"></a>

#### seconds

```python
@property
def seconds() -> float
```

(float):  [Read-Write] Sample time horizon

<a id="unreal.MotionTrajectorySettings.seconds"></a>

#### seconds

```python
@seconds.setter
def seconds(value: float) -> None
```

<a id="unreal.TrajectorySamplingData"></a>