## PoseSearchDatabaseAnimCompositeEx Objects

```python
class PoseSearchDatabaseAnimCompositeEx(PoseSearchDatabaseAnimComposite)
```

Pose Search Database Anim Composite Ex

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearchEditor
- **File**: PoseSearchDatabaseEditorReflection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_composite`` (AnimComposite):  [Read-Write]
- ``branch_in_id`` (uint32):  [Read-Only] SynchronizeWithExternalDependency is true when this asset has been added via SynchronizeWithExternalDependencies.
  To delete it, remove the PoseSearchBranchIn notify state
- ``disable_reselection`` (bool):  [Read-Write] if bDisableReselection is true, poses from the same asset cannot be reselected. Useful to avoid jumping on frames on the same looping animations
- ``enabled`` (bool):  [Read-Write] This allows users to enable or exclude animations from this database. Useful for debugging.
- ``has_root_motion`` (bool):  [Read-Only] Does this animation have root motion enabled ? If you want to change this you need to change it in the base Anim Sequence.
- ``looping`` (bool):  [Read-Only] Is this animation set as looping? If you want to change this you need to change it in the base Anim Sequence.
  Changing the sampling range will disable looping
- ``mirror_option`` (PoseSearchMirrorOption):  [Read-Write] This allows users to set if this animation is original only (no mirrored data), original and mirrored, or only the mirrored version of this animation.
  It requires the mirror table to be set up in the database Schema.
- ``sampling_range`` (FloatInterval):  [Read-Write] It allows users to set a time range to an individual animation composite in the database.
  This is effectively trimming the beginning and end of the animation in the database (not in the original composite).
  If set to [0, 0] it will be the entire frame range of the original composite.
  Set to readonly if this asset is synchronized via PoseSearchBranchIn notify state.
  To edit its value update the associated PoseSearchBranchIn in AnimComposite

<a id="unreal.PoseSearchDatabaseAnimCompositeEx.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PoseSearchDatabaseAnimMontageEx"></a>