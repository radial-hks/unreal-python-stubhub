## RigElementKey Objects

```python
class RigElementKey(StructBase)
```

Rig Element Key

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``type`` (RigElementType):  [Read-Write]

<a id="unreal.RigElementKey.__init__"></a>

#### __init__

```python
def __init__(type: RigElementType = RigElementType.NONE,
             name: Name = "None") -> None
```

<a id="unreal.RigElementKey.type"></a>

#### type

```python
@property
def type() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigElementKey.type"></a>

#### type

```python
@type.setter
def type(value: RigElementType) -> None
```

<a id="unreal.RigElementKey.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigElementKey.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigVMExtendedExecuteContext"></a>