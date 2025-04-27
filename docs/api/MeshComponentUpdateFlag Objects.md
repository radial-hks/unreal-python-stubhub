## MeshComponentUpdateFlag Objects

```python
class MeshComponentUpdateFlag(EnumBase)
```

deprecated: 'MeshComponentUpdateFlag' was renamed to 'VisibilityBasedAnimTickOption'.

<a id="unreal.MeshComponentUpdateFlag.ALWAYS_TICK_POSE_AND_REFRESH_BONES"></a>

#### ALWAYS_TICK_POSE_AND_REFRESH_BONES

0: Always Tick and Refresh BoneTransforms whether rendered or not.

<a id="unreal.MeshComponentUpdateFlag.ALWAYS_TICK_POSE"></a>

#### ALWAYS_TICK_POSE

1: Always Tick, but Refresh BoneTransforms only when rendered.

<a id="unreal.MeshComponentUpdateFlag.ONLY_TICK_MONTAGES_AND_REFRESH_BONES_WHEN_PLAYING_MONTAGES"></a>

#### ONLY_TICK_MONTAGES_AND_REFRESH_BONES_WHEN_PLAYING_MONTAGES

2: When rendered Tick Pose and Refresh Bone Transforms,
otherwise, just update montages alongside BoneTransforms.
(AnimBP graph will not be updated).

<a id="unreal.MeshComponentUpdateFlag.ONLY_TICK_MONTAGES_WHEN_NOT_RENDERED"></a>

#### ONLY_TICK_MONTAGES_WHEN_NOT_RENDERED

3: When rendered Tick Pose and Refresh Bone Transforms,
otherwise, just update montages and skip everything else.
(AnimBP graph will not be updated).

<a id="unreal.MeshComponentUpdateFlag.ONLY_TICK_POSE_WHEN_RENDERED"></a>

#### ONLY_TICK_POSE_WHEN_RENDERED

4: Tick only when rendered, and it will only RefreshBoneTransforms when rendered.

<a id="unreal.SkinWeightProfileLayer"></a>