## RigUnit_PointSimulation Objects

```python
class RigUnit_PointSimulation(RigVMFunction_SimBaseMutable)
```

Performs point based simulation
Note: Disabled for now.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_PointSimulation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bezier`` (RigVMFourPointBezier):  [Read-Write] If the simulation has at least four points they will be stored in here.
- ``bone_targets`` (Array[RigUnit_PointSimulation_BoneTarget]):  [Read-Only] The bones to map to the simulated points.
- ``collision_volumes`` (Array[CRSimSoftCollision]):  [Read-Write] The collision volumes to define
- ``debug_settings`` (RigUnit_PointSimulation_DebugSettings):  [Read-Write] Debug draw settings for this simulation
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``forces`` (Array[CRSimPointForce]):  [Read-Write] The forces to apply
- ``integrator_type`` (RigVMSimPointIntegrateType):  [Read-Only] The type of integrator to use
- ``limit_local_position`` (bool):  [Read-Write] If set to true bones are placed within the original distance of
  the previous local transform. This can be used to avoid stretch.
- ``links`` (Array[CRSimLinearSpring]):  [Read-Write] The links to connect the points with
- ``points`` (Array[RigVMSimPoint]):  [Read-Write] The points to simulate
- ``primary_aim_axis`` (Vector):  [Read-Write] The primary axis to use for the aim
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``secondary_aim_axis`` (Vector):  [Read-Write] The secondary axis to use for the aim
- ``simulated_steps_per_second`` (float):  [Read-Only] The frame rate of the simulation
- ``verlet_blend`` (float):  [Read-Write] The amount of blending to apply per second ( only for verlet integrations )

<a id="unreal.RigUnit_PointSimulation.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: RigVMExecuteContext = [],
        points: Array[RigVMSimPoint] = [],
        links: Array[CRSimLinearSpring] = [],
        forces: Array[CRSimPointForce] = [],
        collision_volumes: Array[CRSimSoftCollision] = [],
        simulated_steps_per_second: float = 0.000000,
        integrator_type: RigVMSimPointIntegrateType = RigVMSimPointIntegrateType
    .VERLET,
        verlet_blend: float = 0.000000,
        bone_targets: Array[RigUnit_PointSimulation_BoneTarget] = [],
        limit_local_position: bool = False,
        propagate_to_children: bool = False,
        primary_aim_axis: Vector = [0.000000, 0.000000, 0.000000],
        secondary_aim_axis: Vector = [0.000000, 0.000000, 0.000000],
        debug_settings: RigUnit_PointSimulation_DebugSettings = [
            False, 1.000000, 50.000000, False,
            [0.000000, 0.000000, 1.000000, 1.000000],
            [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
             [1.000000, 1.000000, 1.000000]]
        ],
        bezier: RigVMFourPointBezier = []) -> None
```

<a id="unreal.RigUnit_PointSimulation.points"></a>

#### points

```python
@property
def points() -> Array[RigVMSimPoint]
```

(Array[RigVMSimPoint]):  [Read-Write] The points to simulate

<a id="unreal.RigUnit_PointSimulation.points"></a>

#### points

```python
@points.setter
def points(value: Array[RigVMSimPoint]) -> None
```

<a id="unreal.RigUnit_PointSimulation.links"></a>

#### links

```python
@property
def links() -> Array[CRSimLinearSpring]
```

(Array[CRSimLinearSpring]):  [Read-Write] The links to connect the points with

<a id="unreal.RigUnit_PointSimulation.links"></a>

#### links

```python
@links.setter
def links(value: Array[CRSimLinearSpring]) -> None
```

<a id="unreal.RigUnit_PointSimulation.forces"></a>

#### forces

```python
@property
def forces() -> Array[CRSimPointForce]
```

(Array[CRSimPointForce]):  [Read-Write] The forces to apply

<a id="unreal.RigUnit_PointSimulation.forces"></a>

#### forces

```python
@forces.setter
def forces(value: Array[CRSimPointForce]) -> None
```

<a id="unreal.RigUnit_PointSimulation.collision_volumes"></a>

#### collision_volumes

```python
@property
def collision_volumes() -> Array[CRSimSoftCollision]
```

(Array[CRSimSoftCollision]):  [Read-Write] The collision volumes to define

<a id="unreal.RigUnit_PointSimulation.collision_volumes"></a>

#### collision_volumes

```python
@collision_volumes.setter
def collision_volumes(value: Array[CRSimSoftCollision]) -> None
```

<a id="unreal.RigUnit_PointSimulation.simulated_steps_per_second"></a>

#### simulated_steps_per_second

```python
@property
def simulated_steps_per_second() -> float
```

(float):  [Read-Only] The frame rate of the simulation

<a id="unreal.RigUnit_PointSimulation.integrator_type"></a>

#### integrator_type

```python
@property
def integrator_type() -> RigVMSimPointIntegrateType
```

(RigVMSimPointIntegrateType):  [Read-Only] The type of integrator to use

<a id="unreal.RigUnit_PointSimulation.verlet_blend"></a>

#### verlet_blend

```python
@property
def verlet_blend() -> float
```

(float):  [Read-Write] The amount of blending to apply per second ( only for verlet integrations )

<a id="unreal.RigUnit_PointSimulation.verlet_blend"></a>

#### verlet_blend

```python
@verlet_blend.setter
def verlet_blend(value: float) -> None
```

<a id="unreal.RigUnit_PointSimulation.bone_targets"></a>

#### bone_targets

```python
@property
def bone_targets() -> Array[RigUnit_PointSimulation_BoneTarget]
```

(Array[RigUnit_PointSimulation_BoneTarget]):  [Read-Only] The bones to map to the simulated points.

<a id="unreal.RigUnit_PointSimulation.limit_local_position"></a>

#### limit_local_position

```python
@property
def limit_local_position() -> bool
```

(bool):  [Read-Write] If set to true bones are placed within the original distance of
the previous local transform. This can be used to avoid stretch.

<a id="unreal.RigUnit_PointSimulation.limit_local_position"></a>

#### limit_local_position

```python
@limit_local_position.setter
def limit_local_position(value: bool) -> None
```

<a id="unreal.RigUnit_PointSimulation.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_PointSimulation.primary_aim_axis"></a>

#### primary_aim_axis

```python
@property
def primary_aim_axis() -> Vector
```

(Vector):  [Read-Write] The primary axis to use for the aim

<a id="unreal.RigUnit_PointSimulation.primary_aim_axis"></a>

#### primary_aim_axis

```python
@primary_aim_axis.setter
def primary_aim_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_PointSimulation.secondary_aim_axis"></a>

#### secondary_aim_axis

```python
@property
def secondary_aim_axis() -> Vector
```

(Vector):  [Read-Write] The secondary axis to use for the aim

<a id="unreal.RigUnit_PointSimulation.secondary_aim_axis"></a>

#### secondary_aim_axis

```python
@secondary_aim_axis.setter
def secondary_aim_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_PointSimulation.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> RigUnit_PointSimulation_DebugSettings
```

(RigUnit_PointSimulation_DebugSettings):  [Read-Write] Debug draw settings for this simulation

<a id="unreal.RigUnit_PointSimulation.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: RigUnit_PointSimulation_DebugSettings) -> None
```

<a id="unreal.RigUnit_PointSimulation.bezier"></a>

#### bezier

```python
@property
def bezier() -> RigVMFourPointBezier
```

(RigVMFourPointBezier):  [Read-Only] If the simulation has at least four points they will be stored in here.

<a id="unreal.RigUnit_SpringInterp"></a>