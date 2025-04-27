## CopyBonesModifier Objects

```python
class CopyBonesModifier(AnimationModifier)
```

Animation Modifier to copy the transform of 'SourceBone(s)' to 'TargetBone(s)'

**C++ Source:**

- **Plugin**: AnimationModifierLibrary
- **Module**: AnimationModifierLibrary
- **File**: CopyBonesModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_pairs`` (Array[BoneReferencePair]):  [Read-Write] Source and Target bone pairs
- ``bone_pose_space`` (AnimPoseSpaces):  [Read-Write] Space to convert SourceBone transforms into before copying them to TargetBone
- ``reapply_post_owner_change`` (bool):  [Read-Write] If this is set to true then the animation modifier will call it's reapply function after any change made to the owning asset.

<a id="unreal.CopyBonesModifier.bone_pairs"></a>

#### bone_pairs

```python
@property
def bone_pairs() -> Array[BoneReferencePair]
```

(Array[BoneReferencePair]):  [Read-Only] Source and Target bone pairs

<a id="unreal.CopyBonesModifier.bone_pose_space"></a>

#### bone_pose_space

```python
@property
def bone_pose_space() -> AnimPoseSpaces
```

(AnimPoseSpaces):  [Read-Only] Space to convert SourceBone transforms into before copying them to TargetBone

<a id="unreal.EncodeRootBoneModifier"></a>