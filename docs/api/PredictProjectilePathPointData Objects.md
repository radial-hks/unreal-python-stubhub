## PredictProjectilePathPointData Objects

```python
class PredictProjectilePathPointData(StructBase)
```

Data about a single point in a projectile path trace.

**C++ Source:**

- **Module**: Engine
- **File**: GameplayStaticsTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Only] Location of this point
- ``time`` (float):  [Read-Only] Elapsed time at this point from the start of the trace.
- ``velocity`` (Vector):  [Read-Only] Velocity at this point

<a id="unreal.PredictProjectilePathPointData.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             velocity: Vector = [0.000000, 0.000000, 0.000000],
             time: float = 0.000000) -> None
```

<a id="unreal.PredictProjectilePathPointData.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only] Location of this point

<a id="unreal.PredictProjectilePathPointData.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Only] Velocity at this point

<a id="unreal.PredictProjectilePathPointData.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Only] Elapsed time at this point from the start of the trace.

<a id="unreal.PredictProjectilePathResult"></a>