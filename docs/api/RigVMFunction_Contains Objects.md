## RigVMFunction_Contains Objects

```python
class RigVMFunction_Contains(RigVMFunction_NameBase)
```

Returns true or false if a given name exists in another given name

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Name.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``result`` (bool):  [Read-Write]
- ``search`` (Name):  [Read-Write]

<a id="unreal.RigVMFunction_Contains.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             search: Name = "None",
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_Contains.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_Contains.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigVMFunction_Contains.search"></a>

#### search

```python
@property
def search() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_Contains.search"></a>

#### search

```python
@search.setter
def search(value: Name) -> None
```

<a id="unreal.RigVMFunction_Contains.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_Contains"></a>