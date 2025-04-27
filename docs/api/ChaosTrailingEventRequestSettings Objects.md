## ChaosTrailingEventRequestSettings Objects

```python
class ChaosTrailingEventRequestSettings(StructBase)
```

Chaos Trailing Event Request Settings

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: ChaosTrailingEventFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_distance`` (float):  [Read-Write] The maximum distance threshold for the results (if location is set on destruction event listener).
- ``max_number_of_results`` (int32):  [Read-Write] The maximum number of results to return.
- ``min_angular_speed`` (float):  [Read-Write] The minimum angular speed threshold for the results.
- ``min_mass`` (float):  [Read-Write] The minimum mass treshold for the results.
- ``min_speed`` (float):  [Read-Write] The minimum speed threshold for the results.
- ``sort_method`` (ChaosTrailingSortMethod):  [Read-Write] The method used to sort the breaking events.

<a id="unreal.ChaosTrailingEventRequestSettings.__init__"></a>

#### __init__

```python
def __init__(
    max_number_of_results: int = 0,
    min_mass: float = 0.000000,
    min_speed: float = 0.000000,
    min_angular_speed: float = 0.000000,
    max_distance: float = 0.000000,
    sort_method: ChaosTrailingSortMethod = ChaosTrailingSortMethod.SORT_NONE
) -> None
```

<a id="unreal.ChaosTrailingEventRequestSettings.max_number_of_results"></a>

#### max_number_of_results

```python
@property
def max_number_of_results() -> int
```

(int32):  [Read-Write] The maximum number of results to return.

<a id="unreal.ChaosTrailingEventRequestSettings.max_number_of_results"></a>

#### max_number_of_results

```python
@max_number_of_results.setter
def max_number_of_results(value: int) -> None
```

<a id="unreal.ChaosTrailingEventRequestSettings.min_mass"></a>

#### min_mass

```python
@property
def min_mass() -> float
```

(float):  [Read-Write] The minimum mass treshold for the results.

<a id="unreal.ChaosTrailingEventRequestSettings.min_mass"></a>

#### min_mass

```python
@min_mass.setter
def min_mass(value: float) -> None
```

<a id="unreal.ChaosTrailingEventRequestSettings.min_speed"></a>

#### min_speed

```python
@property
def min_speed() -> float
```

(float):  [Read-Write] The minimum speed threshold for the results.

<a id="unreal.ChaosTrailingEventRequestSettings.min_speed"></a>

#### min_speed

```python
@min_speed.setter
def min_speed(value: float) -> None
```

<a id="unreal.ChaosTrailingEventRequestSettings.min_angular_speed"></a>

#### min_angular_speed

```python
@property
def min_angular_speed() -> float
```

(float):  [Read-Write] The minimum angular speed threshold for the results.

<a id="unreal.ChaosTrailingEventRequestSettings.min_angular_speed"></a>

#### min_angular_speed

```python
@min_angular_speed.setter
def min_angular_speed(value: float) -> None
```

<a id="unreal.ChaosTrailingEventRequestSettings.max_distance"></a>

#### max_distance

```python
@property
def max_distance() -> float
```

(float):  [Read-Write] The maximum distance threshold for the results (if location is set on destruction event listener).

<a id="unreal.ChaosTrailingEventRequestSettings.max_distance"></a>

#### max_distance

```python
@max_distance.setter
def max_distance(value: float) -> None
```

<a id="unreal.ChaosTrailingEventRequestSettings.sort_method"></a>

#### sort_method

```python
@property
def sort_method() -> ChaosTrailingSortMethod
```

(ChaosTrailingSortMethod):  [Read-Write] The method used to sort the breaking events.

<a id="unreal.ChaosTrailingEventRequestSettings.sort_method"></a>

#### sort_method

```python
@sort_method.setter
def sort_method(value: ChaosTrailingSortMethod) -> None
```

<a id="unreal.GeometryCollectionSource"></a>