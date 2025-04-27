## RigVMFunction_StringTruncate Objects

```python
class RigVMFunction_StringTruncate(RigVMFunction_StringBase)
```

Returns the left or right most characters from the string chopping the given number of characters from the start or the end

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chopped`` (str):  [Read-Write] the part of the name that has been chopped off
- ``count`` (int32):  [Read-Write] Number of characters to remove from left or right
- ``from_end`` (bool):  [Read-Write] if set to true the characters will be removed from the end
- ``name`` (str):  [Read-Write]
- ``remainder`` (str):  [Read-Write] the part of the string without the chopped characters

<a id="unreal.RigVMFunction_StringTruncate.__init__"></a>

#### __init__

```python
def __init__(name: str = "",
             count: int = 0,
             from_end: bool = False,
             remainder: str = "",
             chopped: str = "") -> None
```

<a id="unreal.RigVMFunction_StringTruncate.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringTruncate.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.RigVMFunction_StringTruncate.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Write] Number of characters to remove from left or right

<a id="unreal.RigVMFunction_StringTruncate.count"></a>

#### count

```python
@count.setter
def count(value: int) -> None
```

<a id="unreal.RigVMFunction_StringTruncate.from_end"></a>

#### from_end

```python
@property
def from_end() -> bool
```

(bool):  [Read-Write] if set to true the characters will be removed from the end

<a id="unreal.RigVMFunction_StringTruncate.from_end"></a>

#### from_end

```python
@from_end.setter
def from_end(value: bool) -> None
```

<a id="unreal.RigVMFunction_StringTruncate.remainder"></a>

#### remainder

```python
@property
def remainder() -> str
```

(str):  [Read-Only] the part of the string without the chopped characters

<a id="unreal.RigVMFunction_StringTruncate.chopped"></a>

#### chopped

```python
@property
def chopped() -> str
```

(str):  [Read-Only] the part of the name that has been chopped off

<a id="unreal.RigUnit_StringTruncate"></a>