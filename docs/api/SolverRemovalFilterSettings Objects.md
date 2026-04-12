## SolverRemovalFilterSettings Objects

```python
class SolverRemovalFilterSettings(StructBase)
```

Solver Removal Filter Settings

**C++ Source:**

- **Module**: Chaos
- **File**: SolverEventFilters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter_enabled`` (bool):  [Read-Write] Filter is enabled.
- ``min_mass`` (float):  [Read-Write] The minimum mass threshold for the results (compared with min of particle 1 mass and particle 2 mass).
- ``min_volume`` (float):  [Read-Write]

<a id="unreal.SolverRemovalFilterSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(filter_enabled: bool = False,
             min_mass: float = 0.000000,
             min_volume: float = 0.000000) -> None
```

<a id="unreal.SolverRemovalFilterSettings.filter_enabled"></a>

#### filter\_enabled

```python
@property
def filter_enabled() -> bool
```

(bool):  [Read-Write] Filter is enabled.

<a id="unreal.SolverRemovalFilterSettings.filter_enabled"></a>

#### filter\_enabled

```python
@filter_enabled.setter
def filter_enabled(value: bool) -> None
```

<a id="unreal.SolverRemovalFilterSettings.min_mass"></a>

#### min\_mass

```python
@property
def min_mass() -> float
```

(float):  [Read-Write] The minimum mass threshold for the results (compared with min of particle 1 mass and particle 2 mass).

<a id="unreal.SolverRemovalFilterSettings.min_mass"></a>

#### min\_mass

```python
@min_mass.setter
def min_mass(value: float) -> None
```

<a id="unreal.SolverRemovalFilterSettings.min_volume"></a>

#### min\_volume

```python
@property
def min_volume() -> float
```

(float):  [Read-Write]

<a id="unreal.SolverRemovalFilterSettings.min_volume"></a>

#### min\_volume

```python
@min_volume.setter
def min_volume(value: float) -> None
```

<a id="unreal.PhysicalMaterialStrength"></a>