## RigVMFunction_MathFloatIsNearlyZero Objects

```python
class RigVMFunction_MathFloatIsNearlyZero(RigVMFunction_MathFloatBase)
```

Returns true if the value is nearly zero

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (bool):  [Read-Write]
- ``tolerance`` (float):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatIsNearlyZero.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             tolerance: float = 0.000000,
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathFloatIsNearlyZero.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatIsNearlyZero.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatIsNearlyZero.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatIsNearlyZero.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatIsNearlyZero.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathFloatIsNearlyZero"></a>