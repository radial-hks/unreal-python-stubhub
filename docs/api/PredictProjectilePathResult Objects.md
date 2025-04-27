## PredictProjectilePathResult Objects

```python
class PredictProjectilePathResult(StructBase)
```

Container for the result of a projectile path trace (using PredictProjectilePath).

**C++ Source:**

- **Module**: Engine
- **File**: GameplayStaticsTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hit_result`` (HitResult):  [Read-Only] Hit along the trace, if tracing with collision was enabled.
- ``last_trace_destination`` (PredictProjectilePathPointData):  [Read-Only] Info on the last point we tried to trace to, which may have been beyond the final hit.
- ``path_data`` (Array[PredictProjectilePathPointData]):  [Read-Only] Info for each point on the path.

<a id="unreal.PredictProjectilePathResult.__init__"></a>

#### __init__

```python
def __init__(
    path_data: Array[PredictProjectilePathPointData] = [],
    last_trace_destination: PredictProjectilePathPointData = [[
        0.000000, 0.000000, 0.000000
    ], [0.000000, 0.000000, 0.000000], 0.000000],
    hit_result: HitResult = [
        False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0,
        0, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.PredictProjectilePathResult.path_data"></a>

#### path_data

```python
@property
def path_data() -> Array[PredictProjectilePathPointData]
```

(Array[PredictProjectilePathPointData]):  [Read-Only] Info for each point on the path.

<a id="unreal.PredictProjectilePathResult.last_trace_destination"></a>

#### last_trace_destination

```python
@property
def last_trace_destination() -> PredictProjectilePathPointData
```

(PredictProjectilePathPointData):  [Read-Only] Info on the last point we tried to trace to, which may have been beyond the final hit.

<a id="unreal.PredictProjectilePathResult.hit_result"></a>

#### hit_result

```python
@property
def hit_result() -> HitResult
```

(HitResult):  [Read-Only] Hit along the trace, if tracing with collision was enabled.

<a id="unreal.MeshApproximationSettings"></a>