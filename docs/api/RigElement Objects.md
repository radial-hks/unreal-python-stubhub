## RigElement Objects

```python
class RigElement(StructBase)
```

Rig Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``index`` (int32):  [Read-Only]
- ``name`` (Name):  [Read-Write]

<a id="unreal.RigElement.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None", index: int = 0) -> None
```

<a id="unreal.RigElement.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigElement.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigBone"></a>