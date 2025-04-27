## RigVMFunction_StringLength Objects

```python
class RigVMFunction_StringLength(RigVMFunction_StringBase)
```

Returns the length of a string

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``length`` (int32):  [Read-Write]
- ``value`` (str):  [Read-Write]

<a id="unreal.RigVMFunction_StringLength.__init__"></a>

#### __init__

```python
def __init__(value: str = "", length: int = 0) -> None
```

<a id="unreal.RigVMFunction_StringLength.value"></a>

#### value

```python
@property
def value() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringLength.value"></a>

#### value

```python
@value.setter
def value(value: str) -> None
```

<a id="unreal.RigVMFunction_StringLength.length"></a>

#### length

```python
@property
def length() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_StringLength"></a>