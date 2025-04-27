## RigUnit_CCDIK Objects

```python
class RigUnit_CCDIK(RigUnit_HighlevelBaseMutable)
```

The CCID solver can solve N-Bone chains using
the Cyclic Coordinate Descent Inverse Kinematics algorithm.
For now this node supports single effector chains only.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_CCDIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_rotation_limit`` (float):  [Read-Only] The general rotation limit to be applied to bones
- ``effector_bone`` (Name):  [Read-Write] The last bone in the chain to solve - the effector
- ``effector_transform`` (Transform):  [Read-Write] The transform of the effector in global space
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``max_iterations`` (int32):  [Read-Write] The maximum number of iterations. Values between 4 and 16 are common.
- ``precision`` (float):  [Read-Only] The precision to use for the fabrik solver
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``rotation_limits`` (Array[RigUnit_CCDIK_RotationLimit]):  [Read-Only] Defines the limits of rotation per bone.
- ``start_bone`` (Name):  [Read-Write] The first bone in the chain to solve
- ``start_from_tail`` (bool):  [Read-Only] If set to true the direction of the solvers is flipped.
- ``weight`` (float):  [Read-Write] The weight of the solver - how much the IK should be applied.

<a id="unreal.RigUnit_CCDIK.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             start_bone: Name = "None",
             effector_bone: Name = "None",
             effector_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                              [-0.000000, 0.000000, 0.000000],
                                              [1.000000, 1.000000, 1.000000]],
             precision: float = 0.000000,
             weight: float = 0.000000,
             max_iterations: int = 0,
             start_from_tail: bool = False,
             base_rotation_limit: float = 0.000000,
             rotation_limits: Array[RigUnit_CCDIK_RotationLimit] = [],
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_CCDIK.start_bone"></a>

#### start_bone

```python
@property
def start_bone() -> Name
```

(Name):  [Read-Write] The first bone in the chain to solve

<a id="unreal.RigUnit_CCDIK.start_bone"></a>

#### start_bone

```python
@start_bone.setter
def start_bone(value: Name) -> None
```

<a id="unreal.RigUnit_CCDIK.effector_bone"></a>

#### effector_bone

```python
@property
def effector_bone() -> Name
```

(Name):  [Read-Write] The last bone in the chain to solve - the effector

<a id="unreal.RigUnit_CCDIK.effector_bone"></a>

#### effector_bone

```python
@effector_bone.setter
def effector_bone(value: Name) -> None
```

<a id="unreal.RigUnit_CCDIK.effector_transform"></a>

#### effector_transform

```python
@property
def effector_transform() -> Transform
```

(Transform):  [Read-Write] The transform of the effector in global space

<a id="unreal.RigUnit_CCDIK.effector_transform"></a>

#### effector_transform

```python
@effector_transform.setter
def effector_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_CCDIK.precision"></a>

#### precision

```python
@property
def precision() -> float
```

(float):  [Read-Only] The precision to use for the fabrik solver

<a id="unreal.RigUnit_CCDIK.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the solver - how much the IK should be applied.

<a id="unreal.RigUnit_CCDIK.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_CCDIK.max_iterations"></a>

#### max_iterations

```python
@property
def max_iterations() -> int
```

(int32):  [Read-Write] The maximum number of iterations. Values between 4 and 16 are common.

<a id="unreal.RigUnit_CCDIK.max_iterations"></a>

#### max_iterations

```python
@max_iterations.setter
def max_iterations(value: int) -> None
```

<a id="unreal.RigUnit_CCDIK.start_from_tail"></a>

#### start_from_tail

```python
@property
def start_from_tail() -> bool
```

(bool):  [Read-Only] If set to true the direction of the solvers is flipped.

<a id="unreal.RigUnit_CCDIK.base_rotation_limit"></a>

#### base_rotation_limit

```python
@property
def base_rotation_limit() -> float
```

(float):  [Read-Only] The general rotation limit to be applied to bones

<a id="unreal.RigUnit_CCDIK.rotation_limits"></a>

#### rotation_limits

```python
@property
def rotation_limits() -> Array[RigUnit_CCDIK_RotationLimit]
```

(Array[RigUnit_CCDIK_RotationLimit]):  [Read-Only] Defines the limits of rotation per bone.

<a id="unreal.RigUnit_CCDIK.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_CCDIKPerItem"></a>