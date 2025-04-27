## HairSimulationSolver Objects

```python
class HairSimulationSolver(StructBase)
```

Hair Simulation Solver

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_simulation`` (bool):  [Read-Write] Enable the simulation of the groom groups/LODs if both this boolean and the one in the groom asset are true

<a id="unreal.HairSimulationSolver.__init__"></a>

#### __init__

```python
def __init__(enable_simulation: bool = False) -> None
```

<a id="unreal.HairSimulationSolver.enable_simulation"></a>

#### enable_simulation

```python
@property
def enable_simulation() -> bool
```

(bool):  [Read-Write] Enable the simulation of the groom groups/LODs if both this boolean and the one in the groom asset are true

<a id="unreal.HairSimulationSolver.enable_simulation"></a>

#### enable_simulation

```python
@enable_simulation.setter
def enable_simulation(value: bool) -> None
```

<a id="unreal.HairSimulationForces"></a>