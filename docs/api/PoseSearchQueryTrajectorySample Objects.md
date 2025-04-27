## PoseSearchQueryTrajectorySample Objects

```python
class PoseSearchQueryTrajectorySample(StructBase)
```

Pose Search Query Trajectory Sample

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchTrajectoryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulated_seconds`` (float):  [Read-Write]
- ``facing`` (Quat):  [Read-Write]
- ``position`` (Vector):  [Read-Write]

<a id="unreal.PoseSearchQueryTrajectorySample.__init__"></a>

#### __init__

```python
def __init__(facing: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             position: Vector = [0.000000, 0.000000, 0.000000],
             accumulated_seconds: float = 0.000000) -> None
```

<a id="unreal.PoseSearchQueryTrajectorySample.facing"></a>

#### facing

```python
@property
def facing() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.PoseSearchQueryTrajectorySample.facing"></a>

#### facing

```python
@facing.setter
def facing(value: Quat) -> None
```

<a id="unreal.PoseSearchQueryTrajectorySample.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PoseSearchQueryTrajectorySample.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.PoseSearchQueryTrajectorySample.accumulated_seconds"></a>

#### accumulated_seconds

```python
@property
def accumulated_seconds() -> float
```

(float):  [Read-Write]

<a id="unreal.PoseSearchQueryTrajectorySample.accumulated_seconds"></a>

#### accumulated_seconds

```python
@accumulated_seconds.setter
def accumulated_seconds(value: float) -> None
```

<a id="unreal.PoseSearchQueryTrajectory"></a>