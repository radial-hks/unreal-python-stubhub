## RigUnit_FABRIK Objects

```python
class RigUnit_FABRIK(RigUnit_HighlevelBaseMutable)
```

The FABRIK solver can solve N-Bone chains using
the Forward and Backward Reaching Inverse Kinematics algorithm.
For now this node supports single effector chains only.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_FABRIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effector_bone`` (Name):  [Read-Write] The last bone in the chain to solve - the effector
- ``effector_transform`` (Transform):  [Read-Write] The transform of the effector in global space
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``max_iterations`` (int32):  [Read-Write] The maximum number of iterations. Values between 4 and 16 are common.
- ``precision`` (float):  [Read-Only] The precision to use for the fabrik solver
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``set_effector_transform`` (bool):  [Read-Write] The option to set the effector transform
- ``start_bone`` (Name):  [Read-Write] The first bone in the chain to solve
- ``weight`` (float):  [Read-Write] The weight of the solver - how much the IK should be applied.

<a id="unreal.RigUnit_FABRIK.__init__"></a>

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
             propagate_to_children: bool = False,
             max_iterations: int = 0,
             set_effector_transform: bool = False) -> None
```

<a id="unreal.RigUnit_FABRIK.start_bone"></a>

#### start_bone

```python
@property
def start_bone() -> Name
```

(Name):  [Read-Write] The first bone in the chain to solve

<a id="unreal.RigUnit_FABRIK.start_bone"></a>

#### start_bone

```python
@start_bone.setter
def start_bone(value: Name) -> None
```

<a id="unreal.RigUnit_FABRIK.effector_bone"></a>

#### effector_bone

```python
@property
def effector_bone() -> Name
```

(Name):  [Read-Write] The last bone in the chain to solve - the effector

<a id="unreal.RigUnit_FABRIK.effector_bone"></a>

#### effector_bone

```python
@effector_bone.setter
def effector_bone(value: Name) -> None
```

<a id="unreal.RigUnit_FABRIK.effector_transform"></a>

#### effector_transform

```python
@property
def effector_transform() -> Transform
```

(Transform):  [Read-Write] The transform of the effector in global space

<a id="unreal.RigUnit_FABRIK.effector_transform"></a>

#### effector_transform

```python
@effector_transform.setter
def effector_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_FABRIK.precision"></a>

#### precision

```python
@property
def precision() -> float
```

(float):  [Read-Only] The precision to use for the fabrik solver

<a id="unreal.RigUnit_FABRIK.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the solver - how much the IK should be applied.

<a id="unreal.RigUnit_FABRIK.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_FABRIK.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_FABRIK.max_iterations"></a>

#### max_iterations

```python
@property
def max_iterations() -> int
```

(int32):  [Read-Write] The maximum number of iterations. Values between 4 and 16 are common.

<a id="unreal.RigUnit_FABRIK.max_iterations"></a>

#### max_iterations

```python
@max_iterations.setter
def max_iterations(value: int) -> None
```

<a id="unreal.RigUnit_FABRIK.set_effector_transform"></a>

#### set_effector_transform

```python
@property
def set_effector_transform() -> bool
```

(bool):  [Read-Write] The option to set the effector transform

<a id="unreal.RigUnit_FABRIK.set_effector_transform"></a>

#### set_effector_transform

```python
@set_effector_transform.setter
def set_effector_transform(value: bool) -> None
```

<a id="unreal.RigUnit_FABRIKPerItem"></a>