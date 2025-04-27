## SolverBreakingFilterSettings Objects

```python
class SolverBreakingFilterSettings(StructBase)
```

Solver Breaking Filter Settings

**C++ Source:**

- **Module**: Chaos
- **File**: SolverEventFilters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter_enabled`` (bool):  [Read-Write] Filter is enabled.
- ``min_mass`` (float):  [Read-Write] The minimum mass threshold for the results (compared with min of particle 1 mass and particle 2 mass).
- ``min_speed`` (float):  [Read-Write] The min velocity threshold for the results (compared with min of particle 1 speed and particle 2 speed).
- ``min_volume`` (float):  [Read-Write]

<a id="unreal.SolverBreakingFilterSettings.__init__"></a>

#### __init__

```python
def __init__(filter_enabled: bool = False,
             min_mass: float = 0.000000,
             min_speed: float = 0.000000,
             min_volume: float = 0.000000) -> None
```

<a id="unreal.SolverBreakingFilterSettings.filter_enabled"></a>

#### filter_enabled

```python
@property
def filter_enabled() -> bool
```

(bool):  [Read-Write] Filter is enabled.

<a id="unreal.SolverBreakingFilterSettings.filter_enabled"></a>

#### filter_enabled

```python
@filter_enabled.setter
def filter_enabled(value: bool) -> None
```

<a id="unreal.SolverBreakingFilterSettings.min_mass"></a>

#### min_mass

```python
@property
def min_mass() -> float
```

(float):  [Read-Write] The minimum mass threshold for the results (compared with min of particle 1 mass and particle 2 mass).

<a id="unreal.SolverBreakingFilterSettings.min_mass"></a>

#### min_mass

```python
@min_mass.setter
def min_mass(value: float) -> None
```

<a id="unreal.SolverBreakingFilterSettings.min_speed"></a>

#### min_speed

```python
@property
def min_speed() -> float
```

(float):  [Read-Write] The min velocity threshold for the results (compared with min of particle 1 speed and particle 2 speed).

<a id="unreal.SolverBreakingFilterSettings.min_speed"></a>

#### min_speed

```python
@min_speed.setter
def min_speed(value: float) -> None
```

<a id="unreal.SolverBreakingFilterSettings.min_volume"></a>

#### min_volume

```python
@property
def min_volume() -> float
```

(float):  [Read-Write]

<a id="unreal.SolverBreakingFilterSettings.min_volume"></a>

#### min_volume

```python
@min_volume.setter
def min_volume(value: float) -> None
```

<a id="unreal.SolverCollisionFilterSettings"></a>