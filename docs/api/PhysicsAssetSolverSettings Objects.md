## PhysicsAssetSolverSettings Objects

```python
class PhysicsAssetSolverSettings(StructBase)
```

Solver iterations settings for use by RigidBody AnimNode (RBAN) in the Anim Graph. Each RBAN node runs its own solver with these settings.
note: These settings have no effect when the Physics Asset is used in a world simulation (i.e., as a ragdoll on a SkeletalMeshComponent).

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cull_distance`` (float):  [Read-Write] RBAN: The distance at which collisions are ignored. In general you need this to be a bit larger than the typical relative body
  movement in your simulation, but small enough so that we don't have to speculatively create too many unused collisions.
- ``fixed_time_step`` (float):  [Read-Write] RBAN: The recommended fixed timestep for the RBAN solver. Set to 0 to run with variable timestep (default).
  NOTE: If this value is non-zero and less than the current frame time, the simulation will step multiple times
  which increases the cost.
- ``max_depenetration_velocity`` (float):  [Read-Write] RBAN: When bodies are penetrating, this is the maximum velocity delta that can be applied in one frame.
- ``position_iterations`` (int32):  [Read-Write] RBAN: The number of position iterations to run. The position solve is responsible for depenetration.
  Increasing this will improve simulation stability, but increase the cost.
- ``projection_iterations`` (int32):  [Read-Write] RBAN: The number of projection iterations to run. The projection phase is a final pass over the constraints, applying
  a semi-physical correction to any joint errors remaining after the position and velocity solves. It can be
  very helpful to stabilize joint chains, but can cause issues with collision response. The projection magnitude
  can be controlled per-constraint in the constraint settings (assuming ProjectionIteration is not zero).
  This should be left as 1 in almost all cases.
- ``use_linear_joint_solver`` (bool):  [Read-Write] RBAN: Whether to use the linear or non-linear solver for RBAN Joints. The linear solver is significantly cheaper than
  the non-linear solver when you are running multiple iterations, but is more likely to suffer from jitter.
  In general you should try to use the linear solver and increase the PositionIterations to improve stability if
  possible, only using the non-linear solver as a last resort.
- ``use_manifolds`` (bool):  [Read-Write] RBAN: It enables the use of multi-point contact manifolds, which are created only once at the start of each tick.
  When disabled, a single-point contact is generated in each solver iteration which is more expensive.
- ``velocity_iterations`` (int32):  [Read-Write] RBAN: The number of velocity iterations to run. The velocity solve is responsible for restitution (bounce) and friction.
  This should usually be 1, but could be 0 if you don't care about friction and restitution.

<a id="unreal.PhysicsAssetSolverSettings.__init__"></a>

#### __init__

```python
def __init__(position_iterations: int = 0,
             velocity_iterations: int = 0,
             projection_iterations: int = 0,
             cull_distance: float = 0.000000,
             max_depenetration_velocity: float = 0.000000,
             fixed_time_step: float = 0.000000,
             use_linear_joint_solver: bool = False,
             use_manifolds: bool = False) -> None
```

<a id="unreal.PhysicsAssetSolverSettings.position_iterations"></a>

#### position_iterations

```python
@property
def position_iterations() -> int
```

(int32):  [Read-Write] RBAN: The number of position iterations to run. The position solve is responsible for depenetration.
Increasing this will improve simulation stability, but increase the cost.

<a id="unreal.PhysicsAssetSolverSettings.position_iterations"></a>

#### position_iterations

```python
@position_iterations.setter
def position_iterations(value: int) -> None
```

<a id="unreal.PhysicsAssetSolverSettings.velocity_iterations"></a>

#### velocity_iterations

```python
@property
def velocity_iterations() -> int
```

(int32):  [Read-Write] RBAN: The number of velocity iterations to run. The velocity solve is responsible for restitution (bounce) and friction.
This should usually be 1, but could be 0 if you don't care about friction and restitution.

<a id="unreal.PhysicsAssetSolverSettings.velocity_iterations"></a>

#### velocity_iterations

```python
@velocity_iterations.setter
def velocity_iterations(value: int) -> None
```

<a id="unreal.PhysicsAssetSolverSettings.projection_iterations"></a>

#### projection_iterations

```python
@property
def projection_iterations() -> int
```

(int32):  [Read-Write] RBAN: The number of projection iterations to run. The projection phase is a final pass over the constraints, applying
a semi-physical correction to any joint errors remaining after the position and velocity solves. It can be
very helpful to stabilize joint chains, but can cause issues with collision response. The projection magnitude
can be controlled per-constraint in the constraint settings (assuming ProjectionIteration is not zero).
This should be left as 1 in almost all cases.

<a id="unreal.PhysicsAssetSolverSettings.projection_iterations"></a>

#### projection_iterations

```python
@projection_iterations.setter
def projection_iterations(value: int) -> None
```

<a id="unreal.PhysicsAssetSolverSettings.cull_distance"></a>

#### cull_distance

```python
@property
def cull_distance() -> float
```

(float):  [Read-Write] RBAN: The distance at which collisions are ignored. In general you need this to be a bit larger than the typical relative body
movement in your simulation, but small enough so that we don't have to speculatively create too many unused collisions.

<a id="unreal.PhysicsAssetSolverSettings.cull_distance"></a>

#### cull_distance

```python
@cull_distance.setter
def cull_distance(value: float) -> None
```

<a id="unreal.PhysicsAssetSolverSettings.max_depenetration_velocity"></a>

#### max_depenetration_velocity

```python
@property
def max_depenetration_velocity() -> float
```

(float):  [Read-Write] RBAN: When bodies are penetrating, this is the maximum velocity delta that can be applied in one frame.

<a id="unreal.PhysicsAssetSolverSettings.max_depenetration_velocity"></a>

#### max_depenetration_velocity

```python
@max_depenetration_velocity.setter
def max_depenetration_velocity(value: float) -> None
```

<a id="unreal.PhysicsAssetSolverSettings.fixed_time_step"></a>

#### fixed_time_step

```python
@property
def fixed_time_step() -> float
```

(float):  [Read-Write] RBAN: The recommended fixed timestep for the RBAN solver. Set to 0 to run with variable timestep (default).
NOTE: If this value is non-zero and less than the current frame time, the simulation will step multiple times
which increases the cost.

<a id="unreal.PhysicsAssetSolverSettings.fixed_time_step"></a>

#### fixed_time_step

```python
@fixed_time_step.setter
def fixed_time_step(value: float) -> None
```

<a id="unreal.PhysicsAssetSolverSettings.use_linear_joint_solver"></a>

#### use_linear_joint_solver

```python
@property
def use_linear_joint_solver() -> bool
```

(bool):  [Read-Write] RBAN: Whether to use the linear or non-linear solver for RBAN Joints. The linear solver is significantly cheaper than
the non-linear solver when you are running multiple iterations, but is more likely to suffer from jitter.
In general you should try to use the linear solver and increase the PositionIterations to improve stability if
possible, only using the non-linear solver as a last resort.

<a id="unreal.PhysicsAssetSolverSettings.use_linear_joint_solver"></a>

#### use_linear_joint_solver

```python
@use_linear_joint_solver.setter
def use_linear_joint_solver(value: bool) -> None
```

<a id="unreal.PhysicsAssetSolverSettings.use_manifolds"></a>

#### use_manifolds

```python
@property
def use_manifolds() -> bool
```

(bool):  [Read-Write] RBAN: It enables the use of multi-point contact manifolds, which are created only once at the start of each tick.
When disabled, a single-point contact is generated in each solver iteration which is more expensive.

<a id="unreal.PhysicsAssetSolverSettings.use_manifolds"></a>

#### use_manifolds

```python
@use_manifolds.setter
def use_manifolds(value: bool) -> None
```

<a id="unreal.SolverIterations"></a>