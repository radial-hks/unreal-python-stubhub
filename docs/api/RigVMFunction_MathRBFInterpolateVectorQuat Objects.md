## RigVMFunction_MathRBFInterpolateVectorQuat Objects

```python
class RigVMFunction_MathRBFInterpolateVectorQuat(
        RigVMFunction_MathRBFInterpolateVectorBase)
```

Rig VMFunction Math RBFInterpolate Vector Quat

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFVectorDistanceType):  [Read-Only]
- ``input`` (Vector):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``output`` (Quat):  [Read-Write]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``smoothing_radius`` (float):  [Read-Only]
- ``targets`` (Array[MathRBFInterpolateVectorQuat_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorQuat.__init__"></a>

#### __init__

```python
def __init__(input: Vector = [0.000000, 0.000000, 0.000000],
             distance_function: RBFVectorDistanceType = RBFVectorDistanceType.
             EUCLIDEAN,
             smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
             smoothing_radius: float = 0.000000,
             normalize_output: bool = False,
             targets: Array[MathRBFInterpolateVectorQuat_Target] = [],
             output: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorQuat.targets"></a>

#### targets

```python
@property
def targets() -> Array[MathRBFInterpolateVectorQuat_Target]
```

(Array[MathRBFInterpolateVectorQuat_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorQuat.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[MathRBFInterpolateVectorQuat_Target]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorQuat.output"></a>

#### output

```python
@property
def output() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathRBFInterpolateVectorQuat"></a>