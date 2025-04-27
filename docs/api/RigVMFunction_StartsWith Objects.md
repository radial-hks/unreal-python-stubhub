## RigVMFunction_StartsWith Objects

```python
class RigVMFunction_StartsWith(RigVMFunction_NameBase)
```

Tests whether this string starts with given string

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Name.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``result`` (bool):  [Read-Write]
- ``start`` (Name):  [Read-Write]

<a id="unreal.RigVMFunction_StartsWith.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             start: Name = "None",
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_StartsWith.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_StartsWith.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigVMFunction_StartsWith.start"></a>

#### start

```python
@property
def start() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_StartsWith.start"></a>

#### start

```python
@start.setter
def start(value: Name) -> None
```

<a id="unreal.RigVMFunction_StartsWith.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_StartsWith"></a>