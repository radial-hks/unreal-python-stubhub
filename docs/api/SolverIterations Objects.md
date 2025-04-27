## SolverIterations Objects

```python
class SolverIterations(StructBase)
```

Solver settings for use by the Legacy RigidBody AnimNode (RBAN) solver.
These settings are no longer used by default and will eventually be deprecated and then removed.
note: These settings have no effect when the Physics Asset is used in a world simulation (ragdoll).

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_iterations`` (int32):  [Read-Write] The recommended number of collision sub-iterations. Increasing this can help with collision jitter.
- ``collision_push_out_iterations`` (int32):  [Read-Write] The recommended number of joint sub-push-out iterations. Increasing this can help with collision penetration problems.
- ``joint_iterations`` (int32):  [Read-Write] The recommended number of joint sub-iterations. Increasing this can help with chains of long-thin bodies.
- ``joint_push_out_iterations`` (int32):  [Read-Write] The recommended number of joint sub-push-out iterations.
- ``solver_iterations`` (int32):  [Read-Write] The recommended number of solver iterations. Increase this if collision and joints are fighting, or joint chains are stretching.
- ``solver_push_out_iterations`` (int32):  [Read-Write] Increase this if bodies remain penetrating

<a id="unreal.SolverIterations.__init__"></a>

#### __init__

```python
def __init__(solver_iterations: int = 0,
             joint_iterations: int = 0,
             collision_iterations: int = 0,
             solver_push_out_iterations: int = 0,
             joint_push_out_iterations: int = 0,
             collision_push_out_iterations: int = 0) -> None
```

<a id="unreal.SolverIterations.solver_iterations"></a>

#### solver_iterations

```python
@property
def solver_iterations() -> int
```

(int32):  [Read-Write] The recommended number of solver iterations. Increase this if collision and joints are fighting, or joint chains are stretching.

<a id="unreal.SolverIterations.solver_iterations"></a>

#### solver_iterations

```python
@solver_iterations.setter
def solver_iterations(value: int) -> None
```

<a id="unreal.SolverIterations.joint_iterations"></a>

#### joint_iterations

```python
@property
def joint_iterations() -> int
```

(int32):  [Read-Write] The recommended number of joint sub-iterations. Increasing this can help with chains of long-thin bodies.

<a id="unreal.SolverIterations.joint_iterations"></a>

#### joint_iterations

```python
@joint_iterations.setter
def joint_iterations(value: int) -> None
```

<a id="unreal.SolverIterations.collision_iterations"></a>

#### collision_iterations

```python
@property
def collision_iterations() -> int
```

(int32):  [Read-Write] The recommended number of collision sub-iterations. Increasing this can help with collision jitter.

<a id="unreal.SolverIterations.collision_iterations"></a>

#### collision_iterations

```python
@collision_iterations.setter
def collision_iterations(value: int) -> None
```

<a id="unreal.SolverIterations.solver_push_out_iterations"></a>

#### solver_push_out_iterations

```python
@property
def solver_push_out_iterations() -> int
```

(int32):  [Read-Write] Increase this if bodies remain penetrating

<a id="unreal.SolverIterations.solver_push_out_iterations"></a>

#### solver_push_out_iterations

```python
@solver_push_out_iterations.setter
def solver_push_out_iterations(value: int) -> None
```

<a id="unreal.SolverIterations.joint_push_out_iterations"></a>

#### joint_push_out_iterations

```python
@property
def joint_push_out_iterations() -> int
```

(int32):  [Read-Write] The recommended number of joint sub-push-out iterations.

<a id="unreal.SolverIterations.joint_push_out_iterations"></a>

#### joint_push_out_iterations

```python
@joint_push_out_iterations.setter
def joint_push_out_iterations(value: int) -> None
```

<a id="unreal.SolverIterations.collision_push_out_iterations"></a>

#### collision_push_out_iterations

```python
@property
def collision_push_out_iterations() -> int
```

(int32):  [Read-Write] The recommended number of joint sub-push-out iterations. Increasing this can help with collision penetration problems.

<a id="unreal.SolverIterations.collision_push_out_iterations"></a>

#### collision_push_out_iterations

```python
@collision_push_out_iterations.setter
def collision_push_out_iterations(value: int) -> None
```

<a id="unreal.NeuralProfileStruct"></a>