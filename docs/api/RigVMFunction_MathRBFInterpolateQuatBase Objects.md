## RigVMFunction_MathRBFInterpolateQuatBase Objects

```python
class RigVMFunction_MathRBFInterpolateQuatBase(
        RigVMFunction_MathRBFInterpolateBase)
```

Rig VMFunction Math RBFInterpolate Quat Base

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFQuatDistanceType):  [Read-Only]
- ``input`` (Quat):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``smoothing_angle`` (float):  [Read-Only]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``twist_axis`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.__init__"></a>

#### __init__

```python
def __init__(
        input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        distance_function: RBFQuatDistanceType = RBFQuatDistanceType.EUCLIDEAN,
        smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
        smoothing_angle: float = 0.000000,
        normalize_output: bool = False,
        twist_axis: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.input"></a>

#### input

```python
@property
def input() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.input"></a>

#### input

```python
@input.setter
def input(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.distance_function"></a>

#### distance_function

```python
@property
def distance_function() -> RBFQuatDistanceType
```

(RBFQuatDistanceType):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.smoothing_function"></a>

#### smoothing_function

```python
@property
def smoothing_function() -> RBFKernelType
```

(RBFKernelType):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.smoothing_angle"></a>

#### smoothing_angle

```python
@property
def smoothing_angle() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.normalize_output"></a>

#### normalize_output

```python
@property
def normalize_output() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.twist_axis"></a>

#### twist_axis

```python
@property
def twist_axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateQuatBase.twist_axis"></a>

#### twist_axis

```python
@twist_axis.setter
def twist_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_MathRBFInterpolateQuatBase"></a>