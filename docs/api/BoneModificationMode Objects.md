## BoneModificationMode Objects

```python
class BoneModificationMode(EnumBase)
```

EBone Modification Mode

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_ModifyBone.h

<a id="unreal.BoneModificationMode.BMM_IGNORE"></a>

#### BMM_IGNORE

0: The modifier ignores this channel (keeps the existing bone translation, rotation, or scale).

<a id="unreal.BoneModificationMode.BMM_REPLACE"></a>

#### BMM_REPLACE

1: The modifier replaces the existing translation, rotation, or scale.

<a id="unreal.BoneModificationMode.BMM_ADDITIVE"></a>

#### BMM_ADDITIVE

2: The modifier adds to the existing translation, rotation, or scale.

<a id="unreal.PoseDriverSource"></a>