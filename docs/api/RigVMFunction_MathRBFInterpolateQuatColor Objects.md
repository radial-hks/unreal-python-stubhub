## RigVMFunction_MathRBFInterpolateQuatColor Objects

```python
class RigVMFunction_MathRBFInterpolateQuatColor(
        RigVMFunction_MathRBFInterpolateQuatBase)
```

Rig VMFunction Math RBFInterpolate Quat Color

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFQuatDistanceType):  [Read-Only]
- ``input`` (Quat):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``output`` (LinearColor):  [Read-Write]
- ``smoothing_angle`` (float):  [Read-Only]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``targets`` (Array[MathRBFInterpolateQuatColor_Target]):  [Read-Write]
- ``twist_axis`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatColor.__init__"></a>

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

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatColor.targets"></a>

#### targets

```python
@property
def targets() -> Array[MathRBFInterpolateQuatColor_Target]
```

(Array[MathRBFInterpolateQuatColor_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatColor.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[MathRBFInterpolateQuatColor_Target]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatColor.output"></a>

#### output

```python
@property
def output() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.RigUnit_MathRBFInterpolateQuatColor"></a>