## ClothingSimulationInteractor Objects

```python
class ClothingSimulationInteractor(Object)
```

If a clothing simulation is able to be interacted with at runtime then a derived
interactor should be created, and at least the basic API implemented for that
simulation.
Only write to the simulation and context during the call to Sync, as that is
guaranteed to be a safe place to access this data.

**C++ Source:**

- **Module**: ClothingSystemRuntimeInterface
- **File**: ClothingSimulationInteractor.h

<a id="unreal.ClothingSimulationInteractor.set_num_substeps"></a>

#### set_num_substeps

```python
def set_num_substeps(num_substeps: int = 1) -> None
```

x.set_num_substeps(num_substeps=1) -> None
Set the number of substeps or subdivisions.

Args:
    num_substeps (int32):

<a id="unreal.ClothingSimulationInteractor.set_num_iterations"></a>

#### set_num_iterations

```python
def set_num_iterations(num_iterations: int = 1) -> None
```

x.set_num_iterations(num_iterations=1) -> None
Set the number of time dependent solver iterations.

Args:
    num_iterations (int32):

<a id="unreal.ClothingSimulationInteractor.set_max_num_iterations"></a>

#### set_max_num_iterations

```python
def set_max_num_iterations(max_num_iterations: int = 10) -> None
```

x.set_max_num_iterations(max_num_iterations=10) -> None
Set the maximum number of solver iterations.

Args:
    max_num_iterations (int32):

<a id="unreal.ClothingSimulationInteractor.set_anim_drive_spring_stiffness"></a>

#### set_anim_drive_spring_stiffness

```python
def set_anim_drive_spring_stiffness(stiffness: float) -> None
```

x.set_anim_drive_spring_stiffness(stiffness) -> None
Set the stiffness of the spring force for the animation drive.

Args:
    stiffness (float):

<a id="unreal.ClothingSimulationInteractor.physics_asset_updated"></a>

#### physics_asset_updated

```python
def physics_asset_updated() -> None
```

x.physics_asset_updated() -> None
Called to update collision status without restarting the simulation.

<a id="unreal.ClothingSimulationInteractor.get_simulation_time"></a>

#### get_simulation_time

```python
def get_simulation_time() -> float
```

x.get_simulation_time() -> float
Return the instant average simulation time in ms.

Returns:
    float:

<a id="unreal.ClothingSimulationInteractor.get_num_substeps"></a>

#### get_num_substeps

```python
def get_num_substeps() -> int
```

x.get_num_substeps() -> int32
Return the solver number of subdivisions./
This could be different from the number set if the simulation hasn't updated yet.

Returns:
    int32:

<a id="unreal.ClothingSimulationInteractor.get_num_kinematic_particles"></a>

#### get_num_kinematic_particles

```python
def get_num_kinematic_particles() -> int
```

x.get_num_kinematic_particles() -> int32
Return the number of kinematic (animated) particles.

Returns:
    int32:

<a id="unreal.ClothingSimulationInteractor.get_num_iterations"></a>

#### get_num_iterations

```python
def get_num_iterations() -> int
```

x.get_num_iterations() -> int32
Return the solver number of iterations.
This could be different from the number set if the simulation hasn't updated yet.

Returns:
    int32:

<a id="unreal.ClothingSimulationInteractor.get_num_dynamic_particles"></a>

#### get_num_dynamic_particles

```python
def get_num_dynamic_particles() -> int
```

x.get_num_dynamic_particles() -> int32
Return the number of dynamic (simulated) particles.

Returns:
    int32:

<a id="unreal.ClothingSimulationInteractor.get_num_cloths"></a>

#### get_num_cloths

```python
def get_num_cloths() -> int
```

x.get_num_cloths() -> int32
Return the number of cloths run by the simulation.

Returns:
    int32:

<a id="unreal.ClothingSimulationInteractor.get_clothing_interactor"></a>

#### get_clothing_interactor

```python
def get_clothing_interactor(clothing_asset_name: str) -> ClothingInteractor
```

x.get_clothing_interactor(clothing_asset_name) -> ClothingInteractor
Return a cloth interactor for this simulation.

Args:
    clothing_asset_name (str): 

Returns:
    ClothingInteractor:

<a id="unreal.ClothingSimulationInteractor.enable_gravity_override"></a>

#### enable_gravity_override

```python
def enable_gravity_override(vector: Vector) -> None
```

x.enable_gravity_override(vector) -> None
Set a new gravity override and enable the override.

Args:
    vector (Vector):

<a id="unreal.ClothingSimulationInteractor.disable_gravity_override"></a>

#### disable_gravity_override

```python
def disable_gravity_override() -> None
```

x.disable_gravity_override() -> None
Disable any currently set gravity override.

<a id="unreal.ClothingSimulationInteractor.cloth_config_updated"></a>

#### cloth_config_updated

```python
def cloth_config_updated() -> None
```

x.cloth_config_updated() -> None
Called to update the cloth config without restarting the simulation.

<a id="unreal.ToolMenuBase"></a>