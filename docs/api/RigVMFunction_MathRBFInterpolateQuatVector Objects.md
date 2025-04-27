## RigVMFunction_MathRBFInterpolateQuatVector Objects

```python
class RigVMFunction_MathRBFInterpolateQuatVector(
        RigVMFunction_MathRBFInterpolateQuatBase)
```

Rig VMFunction Math RBFInterpolate Quat Vector

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFQuatDistanceType):  [Read-Only]
- ``input`` (Quat):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``output`` (Vector):  [Read-Write]
- ``smoothing_angle`` (float):  [Read-Only]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``targets`` (Array[MathRBFInterpolateQuatVector_Target]):  [Read-Write]
- ``twist_axis`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatVector.__init__"></a>

#### __init__

```python
def __init__(
        input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        distance_function: RBFQuatDistanceType = RBFQuatDistanceType.EUCLIDEAN,
        smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
        smoothing_angle: float = 0.000000,
        normalize_output: bool = False,
        twist_axis: Vector = [0.000000, 0.000000, 0.000000],
        targets: Array[MathRBFInterpolateQuatVector_Target] = [],
        output: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatVector.targets"></a>

#### targets

```python
@property
def targets() -> Array[MathRBFInterpolateQuatVector_Target]
```

(Array[MathRBFInterpolateQuatVector_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatVector.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[MathRBFInterpolateQuatVector_Target]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatVector.output"></a>

#### output

```python
@property
def output() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathRBFInterpolateQuatVector"></a>