## RigUnit_ItemToName Objects

```python
class RigUnit_ItemToName(RigUnit_ItemBase)
```

Casts the provided item key to its name

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Item.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Name):  [Read-Write]
- ``value`` (RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_ItemToName.__init__"></a>

#### __init__

```python
def __init__(value: RigElementKey = [RigElementType.NONE, "None"],
             result: Name = "None") -> None
```

<a id="unreal.RigUnit_ItemToName.value"></a>

#### value

```python
@property
def value() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_ItemToName.value"></a>

#### value

```python
@value.setter
def value(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ItemToName.result"></a>

#### result

```python
@property
def result() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigUnit_HierarchyAddPhysicsSolver"></a>