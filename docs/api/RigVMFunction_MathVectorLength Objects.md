## RigVMFunction_MathVectorLength Objects

```python
class RigVMFunction_MathVectorLength(RigVMFunction_MathVectorBase)
```

Returns the length of the vector

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (float):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorLength.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathVectorLength.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorLength.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorLength.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathVectorLength"></a>