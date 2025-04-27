## RigVMFunction_MathFloatToInt Objects

```python
class RigVMFunction_MathFloatToInt(RigVMFunction_MathFloatBase)
```

Returns the float cast to an int (this uses floor)

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (int32):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatToInt.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000, result: int = 0) -> None
```

<a id="unreal.RigVMFunction_MathFloatToInt.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatToInt.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatToInt.result"></a>

#### result

```python
@property
def result() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_MathFloatToInt"></a>