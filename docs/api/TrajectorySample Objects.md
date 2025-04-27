## TrajectorySample Objects

```python
class TrajectorySample(StructBase)
```

Trajectory Sample

**C++ Source:**

- **Module**: Engine
- **File**: MotionTrajectoryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulated_seconds`` (float):  [Read-Write] The relative accumulated time that this sample is associated with
  Zero value for instantaneous, negative values for the past, and positive values for the future
- ``linear_velocity`` (Vector):  [Read-Write] Linear velocity relative to the sampled in-motion object
- ``transform`` (Transform):  [Read-Write] Position relative to the sampled in-motion object

<a id="unreal.TrajectorySample.__init__"></a>

#### __init__

```python
def __init__(accumulated_seconds: float = 0.000000,
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             linear_velocity: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.TrajectorySample.accumulated_seconds"></a>

#### accumulated_seconds

```python
@property
def accumulated_seconds() -> float
```

(float):  [Read-Write] The relative accumulated time that this sample is associated with
Zero value for instantaneous, negative values for the past, and positive values for the future

<a id="unreal.TrajectorySample.accumulated_seconds"></a>

#### accumulated_seconds

```python
@accumulated_seconds.setter
def accumulated_seconds(value: float) -> None
```

<a id="unreal.TrajectorySample.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] Position relative to the sampled in-motion object

<a id="unreal.TrajectorySample.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.TrajectorySample.linear_velocity"></a>

#### linear_velocity

```python
@property
def linear_velocity() -> Vector
```

(Vector):  [Read-Write] Linear velocity relative to the sampled in-motion object

<a id="unreal.TrajectorySample.linear_velocity"></a>

#### linear_velocity

```python
@linear_velocity.setter
def linear_velocity(value: Vector) -> None
```

<a id="unreal.TrajectorySampleRange"></a>