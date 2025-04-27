## RigBoneElement Objects

```python
class RigBoneElement(RigSingleParentElement)
```

Rig Bone Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_type`` (RigBoneType):  [Read-Only]
- ``created_at_instruction_index`` (int32):  [Read-Write]
- ``index`` (int32):  [Read-Only]
- ``key`` (RigElementKey):  [Read-Only]
- ``selected`` (bool):  [Read-Write]
- ``sub_index`` (int32):  [Read-Only]

<a id="unreal.RigBoneElement.__init__"></a>

#### __init__

```python
def __init__(key: RigElementKey = [RigElementType.NONE, "None"],
             index: int = 0,
             sub_index: int = 0,
             created_at_instruction_index: int = 0,
             selected: bool = False,
             bone_type: RigBoneType = RigBoneType.IMPORTED) -> None
```

<a id="unreal.RigBoneElement.bone_type"></a>

#### bone_type

```python
@property
def bone_type() -> RigBoneType
```

(RigBoneType):  [Read-Only]

<a id="unreal.RigNullElement"></a>