## RigVMFunction_MathDoubleClamp Objects

```python
class RigVMFunction_MathDoubleClamp(RigVMFunction_MathDoubleBase)
```

Clamps the given value within the range provided by minimum and maximum

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathDouble.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maximum`` (double):  [Read-Write]
- ``minimum`` (double):  [Read-Write]
- ``result`` (double):  [Read-Write]
- ``value`` (double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleClamp.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             minimum: float = 0.000000,
             maximum: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathDoubleClamp.value"></a>

#### value

```python
@property
def value() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleClamp.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleClamp.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleClamp.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleClamp.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_MathDoubleClamp.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathDoubleClamp.result"></a>

#### result

```python
@property
def result() -> float
```

(double):  [Read-Only]

<a id="unreal.RigUnit_MathDoubleClamp"></a>