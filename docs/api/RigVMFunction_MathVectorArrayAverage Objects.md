## RigVMFunction_MathVectorArrayAverage Objects

```python
class RigVMFunction_MathVectorArrayAverage(RigVMFunction_MathVectorBase)
```

Returns the average of the given array

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``array`` (Array[Vector]):  [Read-Write]
- ``average`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorArrayAverage.__init__"></a>

#### __init__

```python
def __init__(array: Array[Vector] = [],
             average: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorArrayAverage.array"></a>

#### array

```python
@property
def array() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorArrayAverage.array"></a>

#### array

```python
@array.setter
def array(value: Array[Vector]) -> None
```

<a id="unreal.RigVMFunction_MathVectorArrayAverage.average"></a>

#### average

```python
@property
def average() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_NoiseFloat"></a>