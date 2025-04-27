## PoseSearchDatabaseMultiAnimAsset Objects

```python
class PoseSearchDatabaseMultiAnimAsset(PoseSearchDatabaseAnimationAssetBase)
```

Pose Search Database Multi Anim Asset

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchDatabase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``branch_in_id`` (uint32):  [Read-Only] SynchronizeWithExternalDependency is true when this asset has been added via SynchronizeWithExternalDependencies.
  To delete it, remove the PoseSearchBranchIn notify state
- ``disable_reselection`` (bool):  [Read-Write] if bDisableReselection is true, poses from the same asset cannot be reselected. Useful to avoid jumping on frames on the same looping animations
- ``enabled`` (bool):  [Read-Write] This allows users to enable or exclude animations from this database. Useful for debugging.
- ``mirror_option`` (PoseSearchMirrorOption):  [Read-Write] This allows users to set if this animation is original only (no mirrored data), original and mirrored, or only the mirrored version of this animation.
  It requires the mirror table to be set up in the database Schema.
- ``multi_anim_asset`` (MultiAnimAsset):  [Read-Write]
- ``sampling_range`` (FloatInterval):  [Read-Write] It allows users to set a time range to an individual UMultiAnimAsset in the database.
  This is effectively trimming the beginning and end of the animation in the database (not in the original UMultiAnimAsset).
  If set to [0, 0] it will be the entire frame range of the original UMultiAnimAsset.

<a id="unreal.PoseSearchDatabaseMultiAnimAsset.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PoseSearchHistoryCollectorAnimNodeReference"></a>