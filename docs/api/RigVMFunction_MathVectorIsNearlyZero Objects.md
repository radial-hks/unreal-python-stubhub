## RigVMFunction_MathVectorIsNearlyZero Objects

```python
class RigVMFunction_MathVectorIsNearlyZero(RigVMFunction_MathVectorBase)
```

Returns true if the value is nearly zero

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (bool):  [Read-Write]
- ``tolerance`` (float):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorIsNearlyZero.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             tolerance: float = 0.000000,
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathVectorIsNearlyZero.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorIsNearlyZero.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorIsNearlyZero.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorIsNearlyZero.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorIsNearlyZero.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathVectorIsNearlyZero"></a>