## PoseSearchInteractionAsset Objects

```python
class PoseSearchInteractionAsset(MultiAnimAsset)
```

Pose Search Interaction Asset

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchInteractionAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_warp_amount`` (float):  [Read-Write] used to test warping: 0 - no warping applied, 1 - full warping/aligment applied
  test warping actors will be offsetted by Items::DebugWarpOffset transforms from the original
  UMultiAnimAsset::GetOrigin() definition and warped accordingly with CalculateWarpTransforms
  following the rotation and translation weights defined in Items::WarpingWeightRotation and
  Items::WarpingWeightTranslation as relative weights between the Items (they'll be normalized at runtime)
- ``debug_warp_offsets`` (Array[Transform]):  [Read-Write]
- ``enable_debug_warp`` (bool):  [Read-Write]
- ``items`` (Array[PoseSearchInteractionAssetItem]):  [Read-Write]

<a id="unreal.PoseSearchInteractionLibrary"></a>