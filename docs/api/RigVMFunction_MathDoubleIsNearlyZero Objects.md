## RigVMFunction_MathDoubleIsNearlyZero Objects

```python
class RigVMFunction_MathDoubleIsNearlyZero(RigVMFunction_MathDoubleBase)
```

Returns true if the value is nearly zero

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathDouble.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (bool):  [Read-Write]
- ``tolerance`` (double):  [Read-Write]
- ``value`` (double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleIsNearlyZero.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             tolerance: float = 0.000000,
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathDoubleIsNearlyZero.value"></a>

#### value

```python
@property
def value() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleIsNearlyZero.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleIsNearlyZero.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleIsNearlyZero.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleIsNearlyZero.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathDoubleIsNearlyZero"></a>