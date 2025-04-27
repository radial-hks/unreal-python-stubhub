## ChaosCollisionEventRequestSettings Objects

```python
class ChaosCollisionEventRequestSettings(StructBase)
```

Settings used to define collision event requests

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: ChaosCollisionEventFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_distance`` (float):  [Read-Write] The maximum distance threshold for the results.
- ``max_number_results`` (int32):  [Read-Write] The maximum number of results to return.
- ``min_impulse`` (float):  [Read-Write] The minimum impulse threshold for the results.
- ``min_mass`` (float):  [Read-Write] The minimum mass threshold for the results (compared with min of particle 1 mass and particle 2 mass).
- ``min_speed`` (float):  [Read-Write] The min speed threshold for the results (compared with min of particle 1 speed and particle 2 speed).
- ``sort_method`` (ChaosCollisionSortMethod):  [Read-Write] The method used to sort the collision events.

<a id="unreal.ChaosCollisionEventRequestSettings.__init__"></a>

#### __init__

```python
def __init__(
    max_number_results: int = 0,
    min_mass: float = 0.000000,
    min_speed: float = 0.000000,
    min_impulse: float = 0.000000,
    max_distance: float = 0.000000,
    sort_method: ChaosCollisionSortMethod = ChaosCollisionSortMethod.SORT_NONE
) -> None
```

<a id="unreal.ChaosCollisionEventRequestSettings.max_number_results"></a>

#### max_number_results

```python
@property
def max_number_results() -> int
```

(int32):  [Read-Write] The maximum number of results to return.

<a id="unreal.ChaosCollisionEventRequestSettings.max_number_results"></a>

#### max_number_results

```python
@max_number_results.setter
def max_number_results(value: int) -> None
```

<a id="unreal.ChaosCollisionEventRequestSettings.min_mass"></a>

#### min_mass

```python
@property
def min_mass() -> float
```

(float):  [Read-Write] The minimum mass threshold for the results (compared with min of particle 1 mass and particle 2 mass).

<a id="unreal.ChaosCollisionEventRequestSettings.min_mass"></a>

#### min_mass

```python
@min_mass.setter
def min_mass(value: float) -> None
```

<a id="unreal.ChaosCollisionEventRequestSettings.min_speed"></a>

#### min_speed

```python
@property
def min_speed() -> float
```

(float):  [Read-Write] The min speed threshold for the results (compared with min of particle 1 speed and particle 2 speed).

<a id="unreal.ChaosCollisionEventRequestSettings.min_speed"></a>

#### min_speed

```python
@min_speed.setter
def min_speed(value: float) -> None
```

<a id="unreal.ChaosCollisionEventRequestSettings.min_impulse"></a>

#### min_impulse

```python
@property
def min_impulse() -> float
```

(float):  [Read-Write] The minimum impulse threshold for the results.

<a id="unreal.ChaosCollisionEventRequestSettings.min_impulse"></a>

#### min_impulse

```python
@min_impulse.setter
def min_impulse(value: float) -> None
```

<a id="unreal.ChaosCollisionEventRequestSettings.max_distance"></a>

#### max_distance

```python
@property
def max_distance() -> float
```

(float):  [Read-Write] The maximum distance threshold for the results.

<a id="unreal.ChaosCollisionEventRequestSettings.max_distance"></a>

#### max_distance

```python
@max_distance.setter
def max_distance(value: float) -> None
```

<a id="unreal.ChaosCollisionEventRequestSettings.sort_method"></a>

#### sort_method

```python
@property
def sort_method() -> ChaosCollisionSortMethod
```

(ChaosCollisionSortMethod):  [Read-Write] The method used to sort the collision events.

<a id="unreal.ChaosCollisionEventRequestSettings.sort_method"></a>

#### sort_method

```python
@sort_method.setter
def sort_method(value: ChaosCollisionSortMethod) -> None
```

<a id="unreal.ChaosRemovalEventRequestSettings"></a>