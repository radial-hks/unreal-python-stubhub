## FindFloorResult Objects

```python
class FindFloorResult(StructBase)
```

Data about the floor for walking movement, used by CharacterMovementComponent.

**C++ Source:**

- **Module**: Engine
- **File**: CharacterMovementComponentAsync.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blocking_hit`` (bool):  [Read-Only] True if there was a blocking hit in the floor test that was NOT in initial penetration.
  The HitResult can give more info about other circumstances.
- ``floor_dist`` (float):  [Read-Only] The distance to the floor, computed from the swept capsule trace.
- ``hit_result`` (HitResult):  [Read-Only] Hit result of the test that found a floor. Includes more specific data about the point of impact and surface normal at that point.
- ``line_dist`` (float):  [Read-Only] The distance to the floor, computed from the trace. Only valid if bLineTrace is true.
- ``line_trace`` (bool):  [Read-Only] True if the hit found a valid walkable floor using a line trace (rather than a sweep test, which happens when the sweep test fails to yield a walkable surface).
- ``walkable_floor`` (bool):  [Read-Only] True if the hit found a valid walkable floor.

<a id="unreal.FindFloorResult.__init__"></a>

#### __init__

```python
def __init__(
    blocking_hit: bool = False,
    walkable_floor: bool = False,
    line_trace: bool = False,
    floor_dist: float = 0.000000,
    line_dist: float = 0.000000,
    hit_result: HitResult = [
        False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0,
        0, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.FindFloorResult.blocking_hit"></a>

#### blocking_hit

```python
@property
def blocking_hit() -> bool
```

(bool):  [Read-Only] True if there was a blocking hit in the floor test that was NOT in initial penetration.
The HitResult can give more info about other circumstances.

<a id="unreal.FindFloorResult.walkable_floor"></a>

#### walkable_floor

```python
@property
def walkable_floor() -> bool
```

(bool):  [Read-Only] True if the hit found a valid walkable floor.

<a id="unreal.FindFloorResult.line_trace"></a>

#### line_trace

```python
@property
def line_trace() -> bool
```

(bool):  [Read-Only] True if the hit found a valid walkable floor using a line trace (rather than a sweep test, which happens when the sweep test fails to yield a walkable surface).

<a id="unreal.FindFloorResult.floor_dist"></a>

#### floor_dist

```python
@property
def floor_dist() -> float
```

(float):  [Read-Only] The distance to the floor, computed from the swept capsule trace.

<a id="unreal.FindFloorResult.line_dist"></a>

#### line_dist

```python
@property
def line_dist() -> float
```

(float):  [Read-Only] The distance to the floor, computed from the trace. Only valid if bLineTrace is true.

<a id="unreal.FindFloorResult.hit_result"></a>

#### hit_result

```python
@property
def hit_result() -> HitResult
```

(HitResult):  [Read-Only] Hit result of the test that found a floor. Includes more specific data about the point of impact and surface normal at that point.

<a id="unreal.AudioComponentParam"></a>