## RigVMFunction_StringMiddle Objects

```python
class RigVMFunction_StringMiddle(RigVMFunction_StringBase)
```

Returns the middle section of a string

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``count`` (int32):  [Read-Write] if count is set to -1 all character from Start will be returned
- ``result`` (str):  [Read-Write]
- ``start`` (int32):  [Read-Write] the index of the first character
- ``value`` (str):  [Read-Write]

<a id="unreal.RigVMFunction_StringMiddle.__init__"></a>

#### __init__

```python
def __init__(value: str = "",
             start: int = 0,
             count: int = 0,
             result: str = "") -> None
```

<a id="unreal.RigVMFunction_StringMiddle.value"></a>

#### value

```python
@property
def value() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringMiddle.value"></a>

#### value

```python
@value.setter
def value(value: str) -> None
```

<a id="unreal.RigVMFunction_StringMiddle.start"></a>

#### start

```python
@property
def start() -> int
```

(int32):  [Read-Write] the index of the first character

<a id="unreal.RigVMFunction_StringMiddle.start"></a>

#### start

```python
@start.setter
def start(value: int) -> None
```

<a id="unreal.RigVMFunction_StringMiddle.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Write] if count is set to -1 all character from Start will be returned

<a id="unreal.RigVMFunction_StringMiddle.count"></a>

#### count

```python
@count.setter
def count(value: int) -> None
```

<a id="unreal.RigVMFunction_StringMiddle.result"></a>

#### result

```python
@property
def result() -> str
```

(str):  [Read-Only]

<a id="unreal.RigUnit_StringMiddle"></a>