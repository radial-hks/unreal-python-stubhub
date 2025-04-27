## RigVMFunction_MathIntClamp Objects

```python
class RigVMFunction_MathIntClamp(RigVMFunction_MathIntBase)
```

Clamps the given value within the range provided by minimum and maximum

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathInt.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maximum`` (int32):  [Read-Write]
- ``minimum`` (int32):  [Read-Write]
- ``result`` (int32):  [Read-Write]
- ``value`` (int32):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntClamp.__init__"></a>

#### __init__

```python
def __init__(value: int = 0,
             minimum: int = 0,
             maximum: int = 0,
             result: int = 0) -> None
```

<a id="unreal.RigVMFunction_MathIntClamp.value"></a>

#### value

```python
@property
def value() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntClamp.value"></a>

#### value

```python
@value.setter
def value(value: int) -> None
```

<a id="unreal.RigVMFunction_MathIntClamp.minimum"></a>

#### minimum

```python
@property
def minimum() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntClamp.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: int) -> None
```

<a id="unreal.RigVMFunction_MathIntClamp.maximum"></a>

#### maximum

```python
@property
def maximum() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntClamp.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: int) -> None
```

<a id="unreal.RigVMFunction_MathIntClamp.result"></a>

#### result

```python
@property
def result() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_MathIntClamp"></a>