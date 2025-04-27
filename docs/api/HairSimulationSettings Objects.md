## HairSimulationSettings Objects

```python
class HairSimulationSettings(StructBase)
```

Hair Simulation Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``external_forces`` (HairSimulationForces):  [Read-Write] External Forces for the hair physics
- ``material_constraints`` (HairSimulationConstraints):  [Read-Write] Material Constraints for the hair physics
- ``override_settings`` (bool):  [Read-Write] Boolean to control if we are going to override the groom asset physics settings
- ``simulation_setup`` (HairSimulationSetup):  [Read-Write] Solver Settings for the hair physics
- ``solver_settings`` (HairSimulationSolver):  [Read-Write] Solver Settings for the hair physics

<a id="unreal.HairSimulationSettings.__init__"></a>

#### __init__

```python
def __init__(
    override_settings: bool = False,
    simulation_setup: HairSimulationSetup = [
        False, False, True, 1.000000, 1.000000, "root", 50.000000
    ],
    solver_settings: HairSimulationSolver = [False],
    external_forces: HairSimulationForces = [[0.000000, 0.000000, -981.000000],
                                             0.100000,
                                             [0.000000, 0.000000, 0.000000]],
    material_constraints: HairSimulationConstraints = [
        0.001000, 0.010000, 0.001000, 1.000000, 0.100000, 0.100000, 1.000000,
        0.001000
    ]
) -> None
```

<a id="unreal.HairSimulationSettings.override_settings"></a>

#### override_settings

```python
@property
def override_settings() -> bool
```

(bool):  [Read-Write] Boolean to control if we are going to override the groom asset physics settings

<a id="unreal.HairSimulationSettings.override_settings"></a>

#### override_settings

```python
@override_settings.setter
def override_settings(value: bool) -> None
```

<a id="unreal.HairSimulationSettings.simulation_setup"></a>

#### simulation_setup

```python
@property
def simulation_setup() -> HairSimulationSetup
```

(HairSimulationSetup):  [Read-Write] Solver Settings for the hair physics

<a id="unreal.HairSimulationSettings.simulation_setup"></a>

#### simulation_setup

```python
@simulation_setup.setter
def simulation_setup(value: HairSimulationSetup) -> None
```

<a id="unreal.HairSimulationSettings.solver_settings"></a>

#### solver_settings

```python
@property
def solver_settings() -> HairSimulationSolver
```

(HairSimulationSolver):  [Read-Write] Solver Settings for the hair physics

<a id="unreal.HairSimulationSettings.solver_settings"></a>

#### solver_settings

```python
@solver_settings.setter
def solver_settings(value: HairSimulationSolver) -> None
```

<a id="unreal.HairSimulationSettings.external_forces"></a>

#### external_forces

```python
@property
def external_forces() -> HairSimulationForces
```

(HairSimulationForces):  [Read-Write] External Forces for the hair physics

<a id="unreal.HairSimulationSettings.external_forces"></a>

#### external_forces

```python
@external_forces.setter
def external_forces(value: HairSimulationForces) -> None
```

<a id="unreal.HairSimulationSettings.material_constraints"></a>

#### material_constraints

```python
@property
def material_constraints() -> HairSimulationConstraints
```

(HairSimulationConstraints):  [Read-Write] Material Constraints for the hair physics

<a id="unreal.HairSimulationSettings.material_constraints"></a>

#### material_constraints

```python
@material_constraints.setter
def material_constraints(value: HairSimulationConstraints) -> None
```

<a id="unreal.HairGeometrySettings"></a>