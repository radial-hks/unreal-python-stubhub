## RigUnit_MultiFABRIK Objects

```python
class RigUnit_MultiFABRIK(RigUnit_HighlevelBaseMutable)
```

The FABRIK solver can solve multi chains within a root using multi effectors
the Forward and Backward Reaching Inverse Kinematics algorithm.
For now this node supports single effector chains only.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_MultiFABRIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effectors`` (Array[RigUnit_MultiFABRIK_EndEffector]):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``max_iterations`` (int32):  [Read-Write] The maximum number of iterations. Values between 4 and 16 are common.
- ``precision`` (float):  [Read-Only] The precision to use for the fabrik solver
- ``propagate_to_children`` (bool):  [Read-Write] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``root_bone`` (Name):  [Read-Write] The first bone in the chain to solve

<a id="unreal.RigUnit_MultiFABRIK.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             root_bone: Name = "None",
             effectors: Array[RigUnit_MultiFABRIK_EndEffector] = [],
             precision: float = 0.000000,
             propagate_to_children: bool = False,
             max_iterations: int = 0) -> None
```

<a id="unreal.RigUnit_MultiFABRIK.root_bone"></a>

#### root_bone

```python
@property
def root_bone() -> Name
```

(Name):  [Read-Write] The first bone in the chain to solve

<a id="unreal.RigUnit_MultiFABRIK.root_bone"></a>

#### root_bone

```python
@root_bone.setter
def root_bone(value: Name) -> None
```

<a id="unreal.RigUnit_MultiFABRIK.effectors"></a>

#### effectors

```python
@property
def effectors() -> Array[RigUnit_MultiFABRIK_EndEffector]
```

(Array[RigUnit_MultiFABRIK_EndEffector]):  [Read-Write]

<a id="unreal.RigUnit_MultiFABRIK.effectors"></a>

#### effectors

```python
@effectors.setter
def effectors(value: Array[RigUnit_MultiFABRIK_EndEffector]) -> None
```

<a id="unreal.RigUnit_MultiFABRIK.precision"></a>

#### precision

```python
@property
def precision() -> float
```

(float):  [Read-Only] The precision to use for the fabrik solver

<a id="unreal.RigUnit_MultiFABRIK.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Write] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_MultiFABRIK.propagate_to_children"></a>

#### propagate_to_children

```python
@propagate_to_children.setter
def propagate_to_children(value: bool) -> None
```

<a id="unreal.RigUnit_MultiFABRIK.max_iterations"></a>

#### max_iterations

```python
@property
def max_iterations() -> int
```

(int32):  [Read-Write] The maximum number of iterations. Values between 4 and 16 are common.

<a id="unreal.RigUnit_MultiFABRIK.max_iterations"></a>

#### max_iterations

```python
@max_iterations.setter
def max_iterations(value: int) -> None
```

<a id="unreal.RigUnit_SlideChain"></a>