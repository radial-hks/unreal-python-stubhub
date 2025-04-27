## RigVMFunction_StringReplace Objects

```python
class RigVMFunction_StringReplace(RigVMFunction_StringBase)
```

Replace all occurrences of a substring in this string

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write]
- ``new`` (str):  [Read-Write]
- ``old`` (str):  [Read-Write]
- ``result`` (str):  [Read-Write]

<a id="unreal.RigVMFunction_StringReplace.__init__"></a>

#### __init__

```python
def __init__(name: str = "",
             old: str = "",
             new: str = "",
             result: str = "") -> None
```

<a id="unreal.RigVMFunction_StringReplace.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringReplace.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.RigVMFunction_StringReplace.old"></a>

#### old

```python
@property
def old() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringReplace.old"></a>

#### old

```python
@old.setter
def old(value: str) -> None
```

<a id="unreal.RigVMFunction_StringReplace.new"></a>

#### new

```python
@property
def new() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringReplace.new"></a>

#### new

```python
@new.setter
def new(value: str) -> None
```

<a id="unreal.RigVMFunction_StringReplace.result"></a>

#### result

```python
@property
def result() -> str
```

(str):  [Read-Only]

<a id="unreal.RigUnit_StringReplace"></a>