## RigVMFunction_MathRBFInterpolateVectorBase Objects

```python
class RigVMFunction_MathRBFInterpolateVectorBase(
        RigVMFunction_MathRBFInterpolateBase)
```

Rig VMFunction Math RBFInterpolate Vector Base

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRBFInterpolate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_function`` (RBFVectorDistanceType):  [Read-Only]
- ``input`` (Vector):  [Read-Write]
- ``normalize_output`` (bool):  [Read-Only]
- ``smoothing_function`` (RBFKernelType):  [Read-Only]
- ``smoothing_radius`` (float):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorBase.__init__"></a>

#### __init__

```python
def __init__(input: Vector = [0.000000, 0.000000, 0.000000],
             distance_function: RBFVectorDistanceType = RBFVectorDistanceType.
             EUCLIDEAN,
             smoothing_function: RBFKernelType = RBFKernelType.GAUSSIAN,
             smoothing_radius: float = 0.000000,
             normalize_output: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorBase.input"></a>

#### input

```python
@property
def input() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorBase.input"></a>

#### input

```python
@input.setter
def input(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorBase.distance_function"></a>

#### distance_function

```python
@property
def distance_function() -> RBFVectorDistanceType
```

(RBFVectorDistanceType):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorBase.smoothing_function"></a>

#### smoothing_function

```python
@property
def smoothing_function() -> RBFKernelType
```

(RBFKernelType):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorBase.smoothing_radius"></a>

#### smoothing_radius

```python
@property
def smoothing_radius() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateVectorBase.normalize_output"></a>

#### normalize_output

```python
@property
def normalize_output() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathRBFInterpolateVectorBase"></a>