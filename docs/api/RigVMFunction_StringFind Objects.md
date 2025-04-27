## RigVMFunction_StringFind Objects

```python
class RigVMFunction_StringFind(RigVMFunction_StringBase)
```

Finds a string within another string

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``found`` (bool):  [Read-Write]
- ``index`` (int32):  [Read-Write]
- ``search`` (str):  [Read-Write]
- ``value`` (str):  [Read-Write]

<a id="unreal.RigVMFunction_StringFind.__init__"></a>

#### __init__

```python
def __init__(value: str = "",
             search: str = "",
             found: bool = False,
             index: int = 0) -> None
```

<a id="unreal.RigVMFunction_StringFind.value"></a>

#### value

```python
@property
def value() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringFind.value"></a>

#### value

```python
@value.setter
def value(value: str) -> None
```

<a id="unreal.RigVMFunction_StringFind.search"></a>

#### search

```python
@property
def search() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringFind.search"></a>

#### search

```python
@search.setter
def search(value: str) -> None
```

<a id="unreal.RigVMFunction_StringFind.found"></a>

#### found

```python
@property
def found() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_StringFind.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_StringFind"></a>