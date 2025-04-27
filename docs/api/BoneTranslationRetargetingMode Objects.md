## BoneTranslationRetargetingMode Objects

```python
class BoneTranslationRetargetingMode(EnumBase)
```

Bone translation retargeting mode.

**C++ Source:**

- **Module**: Engine
- **File**: Skeleton.h

<a id="unreal.BoneTranslationRetargetingMode.ANIMATION"></a>

#### ANIMATION

0: Use translation from animation data.

<a id="unreal.BoneTranslationRetargetingMode.SKELETON"></a>

#### SKELETON

1: Use fixed translation from Skeleton.

<a id="unreal.BoneTranslationRetargetingMode.ANIMATION_SCALED"></a>

#### ANIMATION_SCALED

2: Use Translation from animation, but scale length by Skeleton's proportions.

<a id="unreal.BoneTranslationRetargetingMode.ANIMATION_RELATIVE"></a>

#### ANIMATION_RELATIVE

3: Use Translation from animation, but also play the difference from retargeting pose as an additive.

<a id="unreal.BoneTranslationRetargetingMode.ORIENT_AND_SCALE"></a>

#### ORIENT_AND_SCALE

4: Apply delta orientation and scale from ref pose

<a id="unreal.SoundWaveCloudStreamingPlatformEnableType"></a>