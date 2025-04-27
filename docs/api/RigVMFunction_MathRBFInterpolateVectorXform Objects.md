## RigVMFunction_MathRBFInterpolateVectorXform Objects

```python
class RigVMFunction_MathRBFInterpolateVectorXform(
        RigVMFunction_MathRBFInterpolateVectorBase)
```

Rig VMFunction Math RBFInterpolate Vector Xform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFVectorDistanceType):  [Read-Only]
- ``input`` (Vector):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``output`` (Transform):  [Read-Write]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``smoothing_radius`` (float):  [Read-Only]
- ``targets`` (Array[MathRBFInterpolateVectorXform_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorXform.__init__"></a>

#### __init__

```python
def __init__(
    input: Vector = [0.000000, 0.000000, 0.000000],
    distance_function: RBFVectorDistanceType = RBFVectorDistanceType.EUCLIDEAN,
    smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
    smoothing_radius: float = 0.000000,
    normalize_output: bool = False,
    targets: Array[MathRBFInterpolateVectorXform_Target] = [],
    output: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorXform.targets"></a>

#### targets

```python
@property
def targets() -> Array[MathRBFInterpolateVectorXform_Target]
```

(Array[MathRBFInterpolateVectorXform_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorXform.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[MathRBFInterpolateVectorXform_Target]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorXform.output"></a>

#### output

```python
@property
def output() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathRBFInterpolateVectorXform"></a>