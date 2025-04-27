## RigVMFunction_MathRBFInterpolateVectorVector Objects

```python
class RigVMFunction_MathRBFInterpolateVectorVector(
        RigVMFunction_MathRBFInterpolateVectorBase)
```

Rig VMFunction Math RBFInterpolate Vector Vector

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFVectorDistanceType):  [Read-Only]
- ``input`` (Vector):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``output`` (Vector):  [Read-Write]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``smoothing_radius`` (float):  [Read-Only]
- ``targets`` (Array[MathRBFInterpolateVectorVector_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorVector.__init__"></a>

#### __init__

```python
def __init__(input: Vector = [0.000000, 0.000000, 0.000000],
             distance_function: RBFVectorDistanceType = RBFVectorDistanceType.
             EUCLIDEAN,
             smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
             smoothing_radius: float = 0.000000,
             normalize_output: bool = False,
             targets: Array[MathRBFInterpolateVectorVector_Target] = [],
             output: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorVector.targets"></a>

#### targets

```python
@property
def targets() -> Array[MathRBFInterpolateVectorVector_Target]
```

(Array[MathRBFInterpolateVectorVector_Target]):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorVector.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[MathRBFInterpolateVectorVector_Target]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorVector.output"></a>

#### output

```python
@property
def output() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathRBFInterpolateVectorVector"></a>