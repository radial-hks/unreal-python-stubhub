## PoseSearchQueryTrajectory Objects

```python
class PoseSearchQueryTrajectory(StructBase)
```

Pose Search Query Trajectory

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchTrajectoryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``samples`` (Array[PoseSearchQueryTrajectorySample]):  [Read-Write] This contains zero or more history samples, a current sample, and zero or more future predicted samples.

<a id="unreal.PoseSearchQueryTrajectory.__init__"></a>

#### __init__

```python
def __init__(samples: Array[PoseSearchQueryTrajectorySample] = []) -> None
```

<a id="unreal.PoseSearchQueryTrajectory.samples"></a>

#### samples

```python
@property
def samples() -> Array[PoseSearchQueryTrajectorySample]
```

(Array[PoseSearchQueryTrajectorySample]):  [Read-Write] This contains zero or more history samples, a current sample, and zero or more future predicted samples.

<a id="unreal.PoseSearchQueryTrajectory.samples"></a>

#### samples

```python
@samples.setter
def samples(value: Array[PoseSearchQueryTrajectorySample]) -> None
```

<a id="unreal.AnimNode_MotionMatching"></a>