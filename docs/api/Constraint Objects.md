## Constraint Objects

```python
class Constraint(StructBase)
```

Constraint Set up

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_Constraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``offset_option`` (ConstraintOffsetOption):  [Read-Write] Maintain offset based on refpose or not.

  None - no offset
  Offset_RefPose - offset is created based on reference pose

  In the future, we'd like to support custom offset, not just based on ref pose
- ``per_axis`` (FilterOptionPerAxis):  [Read-Write] Per axis filter options - applied in their local space not in world space
- ``target_bone`` (BoneReference):  [Read-Write] Target Bone this is constraint to
- ``transform_type`` (TransformConstraintType):  [Read-Write] What transform type is constraint to - Translation, Rotation, Scale OR Parent. Parent overrides all component

<a id="unreal.Constraint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimLegIKDefinition"></a>