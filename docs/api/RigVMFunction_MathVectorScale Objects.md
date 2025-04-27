## RigVMFunction_MathVectorScale Objects

```python
class RigVMFunction_MathVectorScale(RigVMFunction_MathVectorBase)
```

Returns the product of the the vector and the float value

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``factor`` (float):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorScale.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             factor: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorScale.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorScale.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorScale.factor"></a>

#### factor

```python
@property
def factor() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorScale.factor"></a>

#### factor

```python
@factor.setter
def factor(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorScale.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorScale"></a>