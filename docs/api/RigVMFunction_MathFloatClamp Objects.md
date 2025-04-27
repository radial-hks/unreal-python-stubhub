## RigVMFunction_MathFloatClamp Objects

```python
class RigVMFunction_MathFloatClamp(RigVMFunction_MathFloatBase)
```

Clamps the given value within the range provided by minimum and maximum

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maximum`` (float):  [Read-Write]
- ``minimum`` (float):  [Read-Write]
- ``result`` (float):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatClamp.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             minimum: float = 0.000000,
             maximum: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathFloatClamp.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatClamp.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatClamp.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatClamp.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatClamp.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatClamp.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatClamp.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathFloatClamp"></a>