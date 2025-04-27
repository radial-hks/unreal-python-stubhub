## HairSolverSettings Objects

```python
class HairSolverSettings(StructBase)
```

Hair Solver Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_system`` (NiagaraSystem):  [Read-Write] Custom niagara system to be used if custom solver is picked
- ``enable_simulation`` (bool):  [Read-Write] Enable the simulation on that group
- ``force_visible`` (bool):  [Read-Write] Force the Niagara solver component to be visible
- ``gravity_preloading`` (float):  [Read-Write] Optimisation of the rest state configuration to compensate from the gravity
- ``iteration_count`` (int32):  [Read-Write] Number of iterations to solve the constraints with the xpbd solver
- ``niagara_solver`` (GroomNiagaraSolvers):  [Read-Write] Niagara solver to be used for simulation
- ``sub_steps`` (int32):  [Read-Write] Number of sub steps to be done per frame. The actual solver calls are done at 24 fps

<a id="unreal.HairSolverSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairExternalForces"></a>