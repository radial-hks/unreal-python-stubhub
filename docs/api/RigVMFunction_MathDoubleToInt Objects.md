## RigVMFunction_MathDoubleToInt Objects

```python
class RigVMFunction_MathDoubleToInt(RigVMFunction_MathDoubleBase)
```

Returns the double cast to an int (this uses floor)

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathDouble.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (int32):  [Read-Write]
- ``value`` (double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleToInt.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000, result: int = 0) -> None
```

<a id="unreal.RigVMFunction_MathDoubleToInt.value"></a>

#### value

```python
@property
def value() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleToInt.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleToInt.result"></a>

#### result

```python
@property
def result() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_MathDoubleToInt"></a>