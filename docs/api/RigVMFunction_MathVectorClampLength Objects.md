## RigVMFunction_MathVectorClampLength Objects

```python
class RigVMFunction_MathVectorClampLength(RigVMFunction_MathVectorBase)
```

Clamps the length of a given vector between a minimum and maximum

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maximum_length`` (float):  [Read-Write]
- ``minimum_length`` (float):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorClampLength.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             minimum_length: float = 0.000000,
             maximum_length: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorClampLength.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorClampLength.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorClampLength.minimum_length"></a>

#### minimum_length

```python
@property
def minimum_length() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorClampLength.minimum_length"></a>

#### minimum_length

```python
@minimum_length.setter
def minimum_length(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorClampLength.maximum_length"></a>

#### maximum_length

```python
@property
def maximum_length() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorClampLength.maximum_length"></a>

#### maximum_length

```python
@maximum_length.setter
def maximum_length(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorClampLength.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorClampLength"></a>