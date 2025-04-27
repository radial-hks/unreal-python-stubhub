## RigVMFunction_MathColorFromFloat Objects

```python
class RigVMFunction_MathColorFromFloat(RigVMFunction_MathColorBase)
```

Makes a vector from a single float

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathColor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (LinearColor):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorFromFloat.__init__"></a>

#### __init__

```python
def __init__(
        value: float = 0.000000,
        result: LinearColor = [0.000000, 0.000000, 0.000000,
                               0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathColorFromFloat.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathColorFromFloat.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathColorFromFloat.result"></a>

#### result

```python
@property
def result() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.RigUnit_MathColorFromFloat"></a>