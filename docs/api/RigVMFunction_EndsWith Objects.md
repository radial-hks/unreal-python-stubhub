## RigVMFunction_EndsWith Objects

```python
class RigVMFunction_EndsWith(RigVMFunction_NameBase)
```

Tests whether this string ends with given string

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Name.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ending`` (Name):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``result`` (bool):  [Read-Write]

<a id="unreal.RigVMFunction_EndsWith.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             ending: Name = "None",
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_EndsWith.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_EndsWith.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigVMFunction_EndsWith.ending"></a>

#### ending

```python
@property
def ending() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_EndsWith.ending"></a>

#### ending

```python
@ending.setter
def ending(value: Name) -> None
```

<a id="unreal.RigVMFunction_EndsWith.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_EndsWith"></a>