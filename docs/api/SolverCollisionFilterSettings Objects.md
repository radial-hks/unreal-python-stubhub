## SolverCollisionFilterSettings Objects

```python
class SolverCollisionFilterSettings(StructBase)
```

Solver Collision Filter Settings

**C++ Source:**

- **Module**: Chaos
- **File**: SolverEventFilters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter_enabled`` (bool):  [Read-Write] Filter is enabled.
- ``min_impulse`` (float):  [Read-Write] The minimum impulse threshold for the results.
- ``min_mass`` (float):  [Read-Write] The minimum mass threshold for the results (compared with min of particle 1 mass and particle 2 mass).
- ``min_speed`` (float):  [Read-Write] The min velocity threshold for the results (compared with min of particle 1 speed and particle 2 speed).

<a id="unreal.SolverCollisionFilterSettings.__init__"></a>

#### __init__

```python
def __init__(filter_enabled: bool = False,
             min_mass: float = 0.000000,
             min_speed: float = 0.000000,
             min_impulse: float = 0.000000) -> None
```

<a id="unreal.SolverCollisionFilterSettings.filter_enabled"></a>

#### filter_enabled

```python
@property
def filter_enabled() -> bool
```

(bool):  [Read-Write] Filter is enabled.

<a id="unreal.SolverCollisionFilterSettings.filter_enabled"></a>

#### filter_enabled

```python
@filter_enabled.setter
def filter_enabled(value: bool) -> None
```

<a id="unreal.SolverCollisionFilterSettings.min_mass"></a>

#### min_mass

```python
@property
def min_mass() -> float
```

(float):  [Read-Write] The minimum mass threshold for the results (compared with min of particle 1 mass and particle 2 mass).

<a id="unreal.SolverCollisionFilterSettings.min_mass"></a>

#### min_mass

```python
@min_mass.setter
def min_mass(value: float) -> None
```

<a id="unreal.SolverCollisionFilterSettings.min_speed"></a>

#### min_speed

```python
@property
def min_speed() -> float
```

(float):  [Read-Write] The min velocity threshold for the results (compared with min of particle 1 speed and particle 2 speed).

<a id="unreal.SolverCollisionFilterSettings.min_speed"></a>

#### min_speed

```python
@min_speed.setter
def min_speed(value: float) -> None
```

<a id="unreal.SolverCollisionFilterSettings.min_impulse"></a>

#### min_impulse

```python
@property
def min_impulse() -> float
```

(float):  [Read-Write] The minimum impulse threshold for the results.

<a id="unreal.SolverCollisionFilterSettings.min_impulse"></a>

#### min_impulse

```python
@min_impulse.setter
def min_impulse(value: float) -> None
```

<a id="unreal.SolverRemovalFilterSettings"></a>