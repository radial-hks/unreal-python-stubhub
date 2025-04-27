## RootMotionGeneratorOp Objects

```python
class RootMotionGeneratorOp(RetargetOpBase)
```

Root Motion Generator Op

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: RootMotionGeneratorOp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_offset`` (Transform):  [Read-Write] A manual offset to apply in global space to the root bone.
- ``maintain_offset_from_pelvis`` (bool):  [Read-Write] Applies only when generating root motion from the Pelvis.
  Maintains the offset between the root and pelvis as recorded in the target retarget pose.
  If false, the root bone is placed directly under the Pelvis bone.
- ``propagate_to_non_retargeted_children`` (bool):  [Read-Write] Will transform all children of the target root that are not themselves part of a retarget chain.
- ``root_height_source`` (RootMotionHeightSource):  [Read-Write] How to set the height of the root bone.
  Copy Height From Source: copies the height of the root bone on the source skeleton's root bone.
  Snap To Ground: sets the root bone height to the ground plane (Z=0).
- ``root_motion_source`` (RootMotionSource):  [Read-Write] Where to copy the root motion from.
  Copy From Source Root: copies the motion from the source root bone, but scales it according to relative height difference.
  Generate From Target Pelvis: uses the retargeted Pelvis motion to generate root motion.
  NOTE: Generating root motion from the Pelvis
- ``rotate_with_pelvis`` (bool):  [Read-Write] Applies only when generating root motion from the Pelvis.
  When true, the applied offset will be rotated by the Pelvis.
  (NOTE: This may cause unwanted rotations, for example if Pelvis Yaw is animated.)
- ``source_root_bone`` (Name):  [Read-Write] The root of the source skeleton.
- ``target_pelvis_bone`` (Name):  [Read-Write] The pelvis of the target skeleton.
- ``target_root_bone`` (Name):  [Read-Write] The root of the target skeleton.

<a id="unreal.IKRigComponent"></a>