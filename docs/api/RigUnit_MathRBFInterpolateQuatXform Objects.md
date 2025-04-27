## RigUnit_MathRBFInterpolateQuatXform Objects

```python
class RigUnit_MathRBFInterpolateQuatXform(
        RigVMFunction_MathRBFInterpolateQuatXform)
```

deprecated: 'RigUnit_MathRBFInterpolateQuatXform' was renamed to 'RigVMFunction_MathRBFInterpolateQuatXform'.

<a id="unreal.RigUnit_MathRBFInterpolateQuatXform.__init__"></a>

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

<a id="unreal.MathRBFInterpolateVectorFloat_Target"></a>