## RigVMFunction_StringPadInteger Objects

```python
class RigVMFunction_StringPadInteger(RigVMFunction_StringBase)
```

Converts an integer number to a string with padding

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``digits`` (int32):  [Read-Write]
- ``result`` (str):  [Read-Write]
- ``value`` (int32):  [Read-Write]

<a id="unreal.RigVMFunction_StringPadInteger.__init__"></a>

#### __init__

```python
def __init__(value: int = 0, digits: int = 0, result: str = "") -> None
```

<a id="unreal.RigVMFunction_StringPadInteger.value"></a>

#### value

```python
@property
def value() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_StringPadInteger.value"></a>

#### value

```python
@value.setter
def value(value: int) -> None
```

<a id="unreal.RigVMFunction_StringPadInteger.digits"></a>

#### digits

```python
@property
def digits() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_StringPadInteger.digits"></a>

#### digits

```python
@digits.setter
def digits(value: int) -> None
```

<a id="unreal.RigVMFunction_StringPadInteger.result"></a>

#### result

```python
@property
def result() -> str
```

(str):  [Read-Only]

<a id="unreal.RigUnit_StringPadInteger"></a>