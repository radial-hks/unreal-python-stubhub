## AdditiveBasePoseType Objects

```python
class AdditiveBasePoseType(EnumBase)
```

For an additive animation, indicates what the animation is relative to.

**C++ Source:**

- **Module**: Engine
- **File**: AnimEnums.h

<a id="unreal.AdditiveBasePoseType.ABPT_NONE"></a>

#### ABPT_NONE

0: Will be deprecated.

<a id="unreal.AdditiveBasePoseType.ABPT_REF_POSE"></a>

#### ABPT_REF_POSE

1: Use the Skeleton's ref pose as base.

<a id="unreal.AdditiveBasePoseType.ABPT_ANIM_SCALED"></a>

#### ABPT_ANIM_SCALED

2: Use a whole animation as a base pose. BasePoseSeq must be set.

<a id="unreal.AdditiveBasePoseType.ABPT_ANIM_FRAME"></a>

#### ABPT_ANIM_FRAME

3: Use one frame of an animation as a base pose. BasePoseSeq and RefFrameIndex must be set (RefFrameIndex will be clamped).

<a id="unreal.AdditiveBasePoseType.ABPT_LOCAL_ANIM_FRAME"></a>

#### ABPT_LOCAL_ANIM_FRAME

4: Use one frame of this animation. RefFrameIndex must be set (RefFrameIndex will be clamped).

<a id="unreal.AdditiveAnimationType"></a>