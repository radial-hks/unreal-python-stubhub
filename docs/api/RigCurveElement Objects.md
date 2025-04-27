## RigCurveElement Objects

```python
class RigCurveElement(RigBaseElement)
```

Rig Curve Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``created_at_instruction_index`` (int32):  [Read-Write]
- ``index`` (int32):  [Read-Only]
- ``key`` (RigElementKey):  [Read-Only]
- ``selected`` (bool):  [Read-Write]
- ``sub_index`` (int32):  [Read-Only]

<a id="unreal.RigCurveElement.__init__"></a>

#### __init__

```python
def __init__(key: RigElementKey = [RigElementType.NONE, "None"],
             index: int = 0,
             sub_index: int = 0,
             created_at_instruction_index: int = 0,
             selected: bool = False) -> None
```

<a id="unreal.RigPhysicsSolverDescription"></a>