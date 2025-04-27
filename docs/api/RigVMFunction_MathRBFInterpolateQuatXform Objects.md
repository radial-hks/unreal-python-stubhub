## RigVMFunction_MathRBFInterpolateQuatXform Objects

```python
class RigVMFunction_MathRBFInterpolateQuatXform(
        RigVMFunction_MathRBFInterpolateQuatBase)
```

Rig VMFunction Math RBFInterpolate Quat Xform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFQuatDistanceType):  [Read-Only]
- ``input`` (Quat):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``output`` (Transform):  [Read-Write]
- ``smoothing_angle`` (float):  [Read-Only]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``targets`` (Array[MathRBFInterpolateQuatXform_Target]):  [Read-Write]
- ``twist_axis`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatXform.__init__"></a>

#### __init__

```python
def __init__(
    input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
    distance_function: RBFQuatDistanceType = RBFQuatDistanceType.EUCLIDEAN,
    smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
    smoothing_angle: float = 0.000000,
    normalize_output: bool = False,
    twist_axis: Vector = [0.000000, 0.000000, 0.000000],
    targets: Array[MathRBFInterpolateQuatXform_Target] = [],
    output: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatXform.targets"></a>

#### targets

```python
@property
def targets() -> Array[MathRBFInterpolateQuatXform_Target]
```

(Array[MathRBFInterpolateQuatXform_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatXform.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[MathRBFInterpolateQuatXform_Target]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatXform.output"></a>

#### output

```python
@property
def output() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathRBFInterpolateQuatXform"></a>