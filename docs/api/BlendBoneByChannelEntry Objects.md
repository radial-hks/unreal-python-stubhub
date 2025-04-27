## BlendBoneByChannelEntry Objects

```python
class BlendBoneByChannelEntry(StructBase)
```

Blend Bone by Channel Entry

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendBoneByChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_rotation`` (bool):  [Read-Write] Copy Rotation from Source to Target
- ``blend_scale`` (bool):  [Read-Write] Copy Scale from Source to Target
- ``blend_translation`` (bool):  [Read-Write] Copy Translation from Source to Target
- ``source_bone`` (BoneReference):  [Read-Write] Bone to take Transform from
- ``target_bone`` (BoneReference):  [Read-Write] Bone to apply Transform to

<a id="unreal.BlendBoneByChannelEntry.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_BlendBoneByChannel"></a>