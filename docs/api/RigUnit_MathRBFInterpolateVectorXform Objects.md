## RigUnit_MathRBFInterpolateVectorXform Objects

```python
class RigUnit_MathRBFInterpolateVectorXform(
        RigVMFunction_MathRBFInterpolateVectorXform)
```

deprecated: 'RigUnit_MathRBFInterpolateVectorXform' was renamed to 'RigVMFunction_MathRBFInterpolateVectorXform'.

<a id="unreal.RigUnit_MathRBFInterpolateVectorXform.__init__"></a>

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

<a id="unreal.RigVMFunction_MathTransformMutableBase"></a>