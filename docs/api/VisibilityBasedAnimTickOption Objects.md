## VisibilityBasedAnimTickOption Objects

```python
class VisibilityBasedAnimTickOption(EnumBase)
```

Skinned Mesh Animation Tick option based on rendered or not. This dictates "TickPose and RefreshBoneTransforms"

**C++ Source:**

- **Module**: Engine
- **File**: SkinnedMeshComponent.h

<a id="unreal.VisibilityBasedAnimTickOption.ALWAYS_TICK_POSE_AND_REFRESH_BONES"></a>

#### ALWAYS\_TICK\_POSE\_AND\_REFRESH\_BONES

0: Always Tick and Refresh BoneTransforms whether rendered or not.

<a id="unreal.VisibilityBasedAnimTickOption.ALWAYS_TICK_POSE"></a>

#### ALWAYS\_TICK\_POSE

1: Always Tick, but Refresh BoneTransforms only when rendered.

<a id="unreal.VisibilityBasedAnimTickOption.ONLY_TICK_MONTAGES_AND_REFRESH_BONES_WHEN_PLAYING_MONTAGES"></a>

#### ONLY\_TICK\_MONTAGES\_AND\_REFRESH\_BONES\_WHEN\_PLAYING\_MONTAGES

2: When rendered Tick Pose and Refresh Bone Transforms,
otherwise, just update montages alongside BoneTransforms.
(AnimBP graph will not be updated).

<a id="unreal.VisibilityBasedAnimTickOption.ONLY_TICK_MONTAGES_WHEN_NOT_RENDERED"></a>

#### ONLY\_TICK\_MONTAGES\_WHEN\_NOT\_RENDERED

3: When rendered Tick Pose and Refresh Bone Transforms,
otherwise, just update montages and skip everything else.
(AnimBP graph will not be updated).

<a id="unreal.VisibilityBasedAnimTickOption.ONLY_TICK_POSE_WHEN_RENDERED"></a>

#### ONLY\_TICK\_POSE\_WHEN\_RENDERED

4: Tick only when rendered, and it will only RefreshBoneTransforms when rendered.

<a id="unreal.MeshComponentUpdateFlag"></a>