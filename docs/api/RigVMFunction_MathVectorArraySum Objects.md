## RigVMFunction_MathVectorArraySum Objects

```python
class RigVMFunction_MathVectorArraySum(RigVMFunction_MathVectorBase)
```

Returns the sum of the given array

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``array`` (Array[Vector]):  [Read-Write]
- ``sum`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorArraySum.__init__"></a>

#### __init__

```python
def __init__(array: Array[Vector] = [],
             sum: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorArraySum.array"></a>

#### array

```python
@property
def array() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorArraySum.array"></a>

#### array

```python
@array.setter
def array(value: Array[Vector]) -> None
```

<a id="unreal.RigVMFunction_MathVectorArraySum.sum"></a>

#### sum

```python
@property
def sum() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathVectorArrayAverage"></a>