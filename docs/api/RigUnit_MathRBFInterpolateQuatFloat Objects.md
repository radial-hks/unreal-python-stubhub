## RigUnit_MathRBFInterpolateQuatFloat Objects

```python
class RigUnit_MathRBFInterpolateQuatFloat(
        RigVMFunction_MathRBFInterpolateQuatFloat)
```

deprecated: 'RigUnit_MathRBFInterpolateQuatFloat' was renamed to 'RigVMFunction_MathRBFInterpolateQuatFloat'.

<a id="unreal.RigUnit_MathRBFInterpolateQuatFloat.__init__"></a>

#### __init__

```python
def __init__(
        input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        distance_function: RBFQuatDistanceType = RBFQuatDistanceType.EUCLIDEAN,
        smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
        smoothing_angle: float = 0.000000,
        normalize_output: bool = False,
        twist_axis: Vector = [0.000000, 0.000000, 0.000000],
        targets: Array[MathRBFInterpolateQuatFloat_Target] = [],
        output: float = 0.000000) -> None
```

<a id="unreal.MathRBFInterpolateQuatVector_Target"></a>