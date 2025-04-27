## PoseSearchInteractionAssetItem Objects

```python
class PoseSearchInteractionAssetItem(StructBase)
```

Pose Search Interaction Asset Item

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchInteractionAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation`` (AnimationAsset):  [Read-Write] associated aniamtion for this FPoseSearchInteractionAssetItem
- ``origin`` (Transform):  [Read-Write] offset from the origin
- ``role`` (Name):  [Read-Write] associated role for this FPoseSearchInteractionAssetItem
- ``warping_weight_rotation`` (float):  [Read-Write] relative weight to the other FPoseSearchInteractionAssetItem::WarpingWeightRotation(s) defining which character will be rotated while warping
  0 - the associated character to this item will move fully to compensate the warping errors
  > 0 && all the other FPoseSearchInteractionAssetItem::WarpingWeightTranslation as zero, and the associated character will not move
- ``warping_weight_translation`` (float):  [Read-Write] relative weight to the other FPoseSearchInteractionAssetItem::WarpingWeightTranslation(s) defining which character will be translated while warping
  0 - the associated character to this item will move fully to compensate the warping errors
  > 0 && all the other FPoseSearchInteractionAssetItem::WarpingWeightTranslation as zero, and the associated character will not move

<a id="unreal.PoseSearchInteractionAssetItem.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PoseSearchRoledSkeleton"></a>