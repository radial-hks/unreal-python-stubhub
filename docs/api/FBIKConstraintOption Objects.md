## FBIKConstraintOption Objects

```python
class FBIKConstraintOption(StructBase)
```

FBIKConstraint Option

**C++ Source:**

- **Plugin**: FullBodyIK
- **Module**: FullBodyIK
- **File**: FBIKConstraintOption.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_limit`` (FBIKBoneLimit):  [Read-Write] Angular delta limit of this joints local transform. [-Limit, Limit]
- ``angular_stiffness`` (Vector):  [Read-Write] Scale of [0, 1] and applied to angular motion strength, xyz is applied to twist, swing1, swing2
- ``enabled`` (bool):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Only] Bone Name
- ``linear_stiffness`` (Vector):  [Read-Write] Scale of [0, 1] and applied to linear motion strength - linear stiffness works on their local frame
- ``offset_rotation`` (Rotator):  [Read-Write] this is offset rotation applied when constructing the local frame
- ``pole_vector`` (Vector):  [Read-Write] Pole Vector in their local space
- ``pole_vector_option`` (PoleVectorOption):  [Read-Write]
- ``use_angular_limit`` (bool):  [Read-Write]
- ``use_pole_vector`` (bool):  [Read-Write]
- ``use_stiffness`` (bool):  [Read-Write]

<a id="unreal.FBIKConstraintOption.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.FBIKConstraintOption.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Only] Bone Name

<a id="unreal.MotionProcessInput"></a>