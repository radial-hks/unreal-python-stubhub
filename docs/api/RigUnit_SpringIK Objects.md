## RigUnit_SpringIK Objects

```python
class RigUnit_SpringIK(RigUnit_HighlevelBaseMutable)
```

The Spring IK solver uses a verlet integrator to perform an IK solve.
It support custom constraints including distance, length etc.
Note: This node operates in world space!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SpringIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``damping`` (float):  [Read-Only] The higher the value to more quickly the simulation calms down. Values between 0.0001 and 0.75 are common.
- ``debug_settings`` (RigUnit_SpringIK_DebugSettings):  [Read-Write] The debug setting for the node
- ``effector_ratio`` (float):  [Read-Only] Defines the equilibrium of the effector springs.
  This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose)
- ``effector_strength`` (float):  [Read-Only] Sets the coefficient of the springs towards the effector. Values between 1 and 2048 are common.
- ``end_bone`` (Name):  [Read-Write] The name of the second bone to solve
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``flip_pole_plane`` (bool):  [Read-Write] If set to true the pole plane will be flipped
- ``hierarchy_strength`` (float):  [Read-Only] Sets the coefficient of the springs along the hierarchy. Values between 1 and 2048 are common.
- ``iterations`` (int32):  [Read-Only] Drives how precise the solver operates. Values between 4 and 24 are common.
  This is only used if the simulation is not live (bLiveSimulation setting).
- ``limit_local_position`` (bool):  [Read-Write] If set to true bones are placed within the original distance of
  the previous local transform. This can be used to avoid stretch.
- ``live_simulation`` (bool):  [Read-Write] If set to true simulation will continue for all intermediate bones over time.
- ``pole_vector`` (Vector):  [Read-Write] The polevector to use for the IK solver
  This can be a location or direction.
- ``pole_vector_kind`` (ControlRigVectorKind):  [Read-Write] The kind of pole vector this is representing - can be a direction or a location
- ``pole_vector_space`` (Name):  [Read-Write] The space in which the pole vector is expressed
- ``primary_axis`` (Vector):  [Read-Write] The major axis being aligned - along the bone
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``root_ratio`` (float):  [Read-Only] Defines the equilibrium of the root springs.
  This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose)
- ``root_strength`` (float):  [Read-Only] Sets the coefficient of the springs towards the root. Values between 1 and 2048 are common.
- ``secondary_axis`` (Vector):  [Read-Write] The minor axis being aligned - towards the pole vector
- ``start_bone`` (Name):  [Read-Write] The name of the first bone to solve

<a id="unreal.RigUnit_SpringIK.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    start_bone: Name = "None",
    end_bone: Name = "None",
    hierarchy_strength: float = 0.000000,
    effector_strength: float = 0.000000,
    effector_ratio: float = 0.000000,
    root_strength: float = 0.000000,
    root_ratio: float = 0.000000,
    damping: float = 0.000000,
    pole_vector: Vector = [0.000000, 0.000000, 0.000000],
    flip_pole_plane: bool = False,
    pole_vector_kind: ControlRigVectorKind = ControlRigVectorKind.DIRECTION,
    pole_vector_space: Name = "None",
    primary_axis: Vector = [0.000000, 0.000000, 0.000000],
    secondary_axis: Vector = [0.000000, 0.000000, 0.000000],
    live_simulation: bool = False,
    iterations: int = 0,
    limit_local_position: bool = False,
    propagate_to_children: bool = False,
    debug_settings: RigUnit_SpringIK_DebugSettings = [
        False, 1.000000, [0.000000, 0.000000, 1.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ]
) -> None
```

<a id="unreal.RigUnit_SpringIK.start_bone"></a>

#### start_bone

```python
@property
def start_bone() -> Name
```

(Name):  [Read-Write] The name of the first bone to solve

<a id="unreal.RigUnit_SpringIK.start_bone"></a>

#### start_bone

```python
@start_bone.setter
def start_bone(value: Name) -> None
```

<a id="unreal.RigUnit_SpringIK.end_bone"></a>

#### end_bone

```python
@property
def end_bone() -> Name
```

(Name):  [Read-Write] The name of the second bone to solve

<a id="unreal.RigUnit_SpringIK.end_bone"></a>

#### end_bone

```python
@end_bone.setter
def end_bone(value: Name) -> None
```

<a id="unreal.RigUnit_SpringIK.hierarchy_strength"></a>

#### hierarchy_strength

```python
@property
def hierarchy_strength() -> float
```

(float):  [Read-Only] Sets the coefficient of the springs along the hierarchy. Values between 1 and 2048 are common.

<a id="unreal.RigUnit_SpringIK.effector_strength"></a>

#### effector_strength

```python
@property
def effector_strength() -> float
```

(float):  [Read-Only] Sets the coefficient of the springs towards the effector. Values between 1 and 2048 are common.

<a id="unreal.RigUnit_SpringIK.effector_ratio"></a>

#### effector_ratio

```python
@property
def effector_ratio() -> float
```

(float):  [Read-Only] Defines the equilibrium of the effector springs.
This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose)

<a id="unreal.RigUnit_SpringIK.root_strength"></a>

#### root_strength

```python
@property
def root_strength() -> float
```

(float):  [Read-Only] Sets the coefficient of the springs towards the root. Values between 1 and 2048 are common.

<a id="unreal.RigUnit_SpringIK.root_ratio"></a>

#### root_ratio

```python
@property
def root_ratio() -> float
```

(float):  [Read-Only] Defines the equilibrium of the root springs.
This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose)

<a id="unreal.RigUnit_SpringIK.damping"></a>

#### damping

```python
@property
def damping() -> float
```

(float):  [Read-Only] The higher the value to more quickly the simulation calms down. Values between 0.0001 and 0.75 are common.

<a id="unreal.RigUnit_SpringIK.pole_vector"></a>

#### pole_vector

```python
@property
def pole_vector() -> Vector
```

(Vector):  [Read-Write] The polevector to use for the IK solver
This can be a location or direction.

<a id="unreal.RigUnit_SpringIK.pole_vector"></a>

#### pole_vector

```python
@pole_vector.setter
def pole_vector(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringIK.flip_pole_plane"></a>

#### flip_pole_plane

```python
@property
def flip_pole_plane() -> bool
```

(bool):  [Read-Write] If set to true the pole plane will be flipped

<a id="unreal.RigUnit_SpringIK.flip_pole_plane"></a>

#### flip_pole_plane

```python
@flip_pole_plane.setter
def flip_pole_plane(value: bool) -> None
```

<a id="unreal.RigUnit_SpringIK.pole_vector_kind"></a>

#### pole_vector_kind

```python
@property
def pole_vector_kind() -> ControlRigVectorKind
```

(ControlRigVectorKind):  [Read-Write] The kind of pole vector this is representing - can be a direction or a location

<a id="unreal.RigUnit_SpringIK.pole_vector_kind"></a>

#### pole_vector_kind

```python
@pole_vector_kind.setter
def pole_vector_kind(value: ControlRigVectorKind) -> None
```

<a id="unreal.RigUnit_SpringIK.pole_vector_space"></a>

#### pole_vector_space

```python
@property
def pole_vector_space() -> Name
```

(Name):  [Read-Write] The space in which the pole vector is expressed

<a id="unreal.RigUnit_SpringIK.pole_vector_space"></a>

#### pole_vector_space

```python
@pole_vector_space.setter
def pole_vector_space(value: Name) -> None
```

<a id="unreal.RigUnit_SpringIK.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> Vector
```

(Vector):  [Read-Write] The major axis being aligned - along the bone

<a id="unreal.RigUnit_SpringIK.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringIK.secondary_axis"></a>

#### secondary_axis

```python
@property
def secondary_axis() -> Vector
```

(Vector):  [Read-Write] The minor axis being aligned - towards the pole vector

<a id="unreal.RigUnit_SpringIK.secondary_axis"></a>

#### secondary_axis

```python
@secondary_axis.setter
def secondary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringIK.live_simulation"></a>

#### live_simulation

```python
@property
def live_simulation() -> bool
```

(bool):  [Read-Write] If set to true simulation will continue for all intermediate bones over time.

<a id="unreal.RigUnit_SpringIK.live_simulation"></a>

#### live_simulation

```python
@live_simulation.setter
def live_simulation(value: bool) -> None
```

<a id="unreal.RigUnit_SpringIK.iterations"></a>

#### iterations

```python
@property
def iterations() -> int
```

(int32):  [Read-Only] Drives how precise the solver operates. Values between 4 and 24 are common.
This is only used if the simulation is not live (bLiveSimulation setting).

<a id="unreal.RigUnit_SpringIK.limit_local_position"></a>

#### limit_local_position

```python
@property
def limit_local_position() -> bool
```

(bool):  [Read-Write] If set to true bones are placed within the original distance of
the previous local transform. This can be used to avoid stretch.

<a id="unreal.RigUnit_SpringIK.limit_local_position"></a>

#### limit_local_position

```python
@limit_local_position.setter
def limit_local_position(value: bool) -> None
```

<a id="unreal.RigUnit_SpringIK.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_SpringIK.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> RigUnit_SpringIK_DebugSettings
```

(RigUnit_SpringIK_DebugSettings):  [Read-Write] The debug setting for the node

<a id="unreal.RigUnit_SpringIK.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: RigUnit_SpringIK_DebugSettings) -> None
```

<a id="unreal.ConstraintTarget"></a>