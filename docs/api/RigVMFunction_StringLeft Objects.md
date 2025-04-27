## RigVMFunction_StringLeft Objects

```python
class RigVMFunction_StringLeft(RigVMFunction_StringBase)
```

Returns the left most characters of a string

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``count`` (int32):  [Read-Write]
- ``result`` (str):  [Read-Write]
- ``value`` (str):  [Read-Write]

<a id="unreal.RigVMFunction_StringLeft.__init__"></a>

#### __init__

```python
def __init__(value: str = "", count: int = 0, result: str = "") -> None
```

<a id="unreal.RigVMFunction_StringLeft.value"></a>

#### value

```python
@property
def value() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringLeft.value"></a>

#### value

```python
@value.setter
def value(value: str) -> None
```

<a id="unreal.RigVMFunction_StringLeft.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_StringLeft.count"></a>

#### count

```python
@count.setter
def count(value: int) -> None
```

<a id="unreal.RigVMFunction_StringLeft.result"></a>

#### result

```python
@property
def result() -> str
```

(str):  [Read-Only]

<a id="unreal.RigUnit_StringLeft"></a>