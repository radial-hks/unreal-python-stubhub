## RigVMFunction_NameTruncate Objects

```python
class RigVMFunction_NameTruncate(RigVMFunction_NameBase)
```

Returns the left or right most characters from the string chopping the given number of characters from the start or the end

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Name.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chopped`` (Name):  [Read-Write] the part of the name that has been chopped off
- ``count`` (int32):  [Read-Write] Number of characters to remove from left or right
- ``from_end`` (bool):  [Read-Write] if set to true the characters will be removed from the end
- ``name`` (Name):  [Read-Write]
- ``remainder`` (Name):  [Read-Write] the part of the string without the chopped characters

<a id="unreal.RigVMFunction_NameTruncate.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             count: int = 0,
             from_end: bool = False,
             remainder: Name = "None",
             chopped: Name = "None") -> None
```

<a id="unreal.RigVMFunction_NameTruncate.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_NameTruncate.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigVMFunction_NameTruncate.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Write] Number of characters to remove from left or right

<a id="unreal.RigVMFunction_NameTruncate.count"></a>

#### count

```python
@count.setter
def count(value: int) -> None
```

<a id="unreal.RigVMFunction_NameTruncate.from_end"></a>

#### from_end

```python
@property
def from_end() -> bool
```

(bool):  [Read-Write] if set to true the characters will be removed from the end

<a id="unreal.RigVMFunction_NameTruncate.from_end"></a>

#### from_end

```python
@from_end.setter
def from_end(value: bool) -> None
```

<a id="unreal.RigVMFunction_NameTruncate.remainder"></a>

#### remainder

```python
@property
def remainder() -> Name
```

(Name):  [Read-Only] the part of the string without the chopped characters

<a id="unreal.RigVMFunction_NameTruncate.chopped"></a>

#### chopped

```python
@property
def chopped() -> Name
```

(Name):  [Read-Only] the part of the name that has been chopped off

<a id="unreal.RigUnit_NameTruncate"></a>