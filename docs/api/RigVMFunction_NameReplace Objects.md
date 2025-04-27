## RigVMFunction_NameReplace Objects

```python
class RigVMFunction_NameReplace(RigVMFunction_NameBase)
```

Replace all occurrences of a substring in this string

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Name.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``new`` (Name):  [Read-Write]
- ``old`` (Name):  [Read-Write]
- ``result`` (Name):  [Read-Write]

<a id="unreal.RigVMFunction_NameReplace.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             old: Name = "None",
             new: Name = "None",
             result: Name = "None") -> None
```

<a id="unreal.RigVMFunction_NameReplace.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_NameReplace.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigVMFunction_NameReplace.old"></a>

#### old

```python
@property
def old() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_NameReplace.old"></a>

#### old

```python
@old.setter
def old(value: Name) -> None
```

<a id="unreal.RigVMFunction_NameReplace.new"></a>

#### new

```python
@property
def new() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_NameReplace.new"></a>

#### new

```python
@new.setter
def new(value: Name) -> None
```

<a id="unreal.RigVMFunction_NameReplace.result"></a>

#### result

```python
@property
def result() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigUnit_NameReplace"></a>