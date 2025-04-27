## RigUnit_MathRBFInterpolateQuatVector Objects

```python
class RigUnit_MathRBFInterpolateQuatVector(
        RigVMFunction_MathRBFInterpolateQuatVector)
```

deprecated: 'RigUnit_MathRBFInterpolateQuatVector' was renamed to 'RigVMFunction_MathRBFInterpolateQuatVector'.

<a id="unreal.RigUnit_MathRBFInterpolateQuatVector.__init__"></a>

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

<a id="unreal.MathRBFInterpolateQuatColor_Target"></a>