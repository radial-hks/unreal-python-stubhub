## PinBoneOp Objects

```python
class PinBoneOp(RetargetOpBase)
```

Pin Bone Op

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: PinBoneOp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bones_to_pin`` (Array[PinBoneData]):  [Read-Write]
- ``global_offset`` (Transform):  [Read-Write] A manual offset to apply in global space
- ``local_offset`` (Transform):  [Read-Write] A manual offset to apply in local space
- ``maintain_offset`` (bool):  [Read-Write] Maintain the original offset between the source and target bone
- ``pin_to`` (RetargetSourceOrTarget):  [Read-Write] The bone, on the target skeleton to pin to.
- ``pin_type`` (PinBoneType):  [Read-Write] Apply this pin to the full transform, or just translation or rotation only.

<a id="unreal.RootMotionGeneratorOp"></a>