## RigUnit_MathRBFInterpolateQuatColor Objects

```python
class RigUnit_MathRBFInterpolateQuatColor(
        RigVMFunction_MathRBFInterpolateQuatColor)
```

deprecated: 'RigUnit_MathRBFInterpolateQuatColor' was renamed to 'RigVMFunction_MathRBFInterpolateQuatColor'.

<a id="unreal.RigUnit_MathRBFInterpolateQuatColor.__init__"></a>

#### __init__

```python
def __init__(
        input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        distance_function: RBFQuatDistanceType = RBFQuatDistanceType.EUCLIDEAN,
        smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
        smoothing_angle: float = 0.000000,
        normalize_output: bool = False,
        twist_axis: Vector = [0.000000, 0.000000, 0.000000],
        targets: Array[MathRBFInterpolateQuatColor_Target] = [],
        output: LinearColor = [0.000000, 0.000000, 0.000000,
                               0.000000]) -> None
```

<a id="unreal.MathRBFInterpolateQuatQuat_Target"></a>