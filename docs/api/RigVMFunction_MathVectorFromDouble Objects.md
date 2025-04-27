## RigVMFunction_MathVectorFromDouble Objects

```python
class RigVMFunction_MathVectorFromDouble(RigVMFunction_MathVectorBase)
```

Makes a vector from a single double

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Vector):  [Read-Write]
- ``value`` (double):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorFromDouble.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorFromDouble.value"></a>

#### value

```python
@property
def value() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorFromDouble.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorFromDouble.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorFromDouble"></a>