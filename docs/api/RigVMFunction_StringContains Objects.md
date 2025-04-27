## RigVMFunction_StringContains Objects

```python
class RigVMFunction_StringContains(RigVMFunction_StringBase)
```

Returns true or false if a given name exists in another given name

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write]
- ``result`` (bool):  [Read-Write]
- ``search`` (str):  [Read-Write]

<a id="unreal.RigVMFunction_StringContains.__init__"></a>

#### __init__

```python
def __init__(name: str = "", search: str = "", result: bool = False) -> None
```

<a id="unreal.RigVMFunction_StringContains.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringContains.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.RigVMFunction_StringContains.search"></a>

#### search

```python
@property
def search() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringContains.search"></a>

#### search

```python
@search.setter
def search(value: str) -> None
```

<a id="unreal.RigVMFunction_StringContains.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_StringContains"></a>