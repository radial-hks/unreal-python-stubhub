## RigUnit_MathRBFInterpolateQuatQuat Objects

```python
class RigUnit_MathRBFInterpolateQuatQuat(
        RigVMFunction_MathRBFInterpolateQuatQuat)
```

deprecated: 'RigUnit_MathRBFInterpolateQuatQuat' was renamed to 'RigVMFunction_MathRBFInterpolateQuatQuat'.

<a id="unreal.RigUnit_MathRBFInterpolateQuatQuat.__init__"></a>

#### __init__

```python
def __init__(
        input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        distance_function: RBFQuatDistanceType = RBFQuatDistanceType.EUCLIDEAN,
        smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
        smoothing_angle: float = 0.000000,
        normalize_output: bool = False,
        twist_axis: Vector = [0.000000, 0.000000, 0.000000],
        targets: Array[MathRBFInterpolateQuatQuat_Target] = [],
        output: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.MathRBFInterpolateQuatXform_Target"></a>