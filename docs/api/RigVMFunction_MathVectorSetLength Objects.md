## RigVMFunction_MathVectorSetLength Objects

```python
class RigVMFunction_MathVectorSetLength(RigVMFunction_MathVectorBase)
```

Sets the length of a given vector

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``length`` (float):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorSetLength.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             length: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorSetLength.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorSetLength.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorSetLength.length"></a>

#### length

```python
@property
def length() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorSetLength.length"></a>

#### length

```python
@length.setter
def length(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorSetLength.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorSetLength"></a>