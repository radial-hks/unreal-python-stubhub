## RigVMFunction_MathRBFInterpolateVectorColor Objects

```python
class RigVMFunction_MathRBFInterpolateVectorColor(
        RigVMFunction_MathRBFInterpolateVectorBase)
```

Rig VMFunction Math RBFInterpolate Vector Color

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFVectorDistanceType):  [Read-Only]
- ``input`` (Vector):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``output`` (LinearColor):  [Read-Write]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``smoothing_radius`` (float):  [Read-Only]
- ``targets`` (Array[MathRBFInterpolateVectorColor_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorColor.__init__"></a>

#### __init__

```python
def __init__(
        input: Vector = [0.000000, 0.000000, 0.000000],
        distance_function: RBFVectorDistanceType = RBFVectorDistanceType.
    EUCLIDEAN,
        smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
        smoothing_radius: float = 0.000000,
        normalize_output: bool = False,
        targets: Array[MathRBFInterpolateVectorColor_Target] = [],
        output: LinearColor = [0.000000, 0.000000, 0.000000,
                               0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorColor.targets"></a>

#### targets

```python
@property
def targets() -> Array[MathRBFInterpolateVectorColor_Target]
```

(Array[MathRBFInterpolateVectorColor_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorColor.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[MathRBFInterpolateVectorColor_Target]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorColor.output"></a>

#### output

```python
@property
def output() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.RigUnit_MathRBFInterpolateVectorColor"></a>