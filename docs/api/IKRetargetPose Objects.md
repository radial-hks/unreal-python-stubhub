## IKRetargetPose Objects

```python
class IKRetargetPose(StructBase)
```

IKRetarget Pose

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargeter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_rotation_offsets`` (Map[Name, Quat]):  [Read-Write] these are LOCAL-space rotation deltas to be applied to a bone to modify it's retarget pose
- ``root_translation_offset`` (Vector):  [Read-Write] a translational delta in GLOBAL space, applied only to the retarget root bone

<a id="unreal.IKRetargetPose.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.BoneChain"></a>