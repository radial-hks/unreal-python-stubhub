## PoseSearchDatabaseBlendSpaceEx Objects

```python
class PoseSearchDatabaseBlendSpaceEx(PoseSearchDatabaseBlendSpace)
```

Pose Search Database Blend Space Ex

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearchEditor
- **File**: PoseSearchDatabaseEditorReflection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_param_x`` (float):  [Read-Write] BlendParams used to sample this BlendSpace
- ``blend_param_y`` (float):  [Read-Write] BlendParams used to sample this BlendSpace
- ``blend_space`` (BlendSpace):  [Read-Write]
- ``branch_in_id`` (uint32):  [Read-Only] SynchronizeWithExternalDependency is true when this asset has been added via SynchronizeWithExternalDependencies.
  To delete it, remove the PoseSearchBranchIn notify state
- ``disable_reselection`` (bool):  [Read-Write] if bDisableReselection is true, poses from the same asset cannot be reselected. Useful to avoid jumping on frames on the same looping animations
- ``enabled`` (bool):  [Read-Write] This allows users to enable or exclude animations from this database. Useful for debugging.
- ``has_root_motion`` (bool):  [Read-Only] Does this animation have root motion enabled ? If you want to change this you need to change it in the base Anim Sequence.
- ``looping`` (bool):  [Read-Only] Is this animation set as looping? If you want to change this you need to change it in the base Anim Sequence.
  Changing the sampling range will disable looping
- ``mirror_option`` (PoseSearchMirrorOption):  [Read-Write] This allows users to set if this animation is original only (no mirrored data), original and mirrored, or only the mirrored version of this animation.
  It requires the mirror table to be set up in the database Schema.
- ``number_of_horizontal_samples`` (int32):  [Read-Write] Sets the number of horizontal samples in the blend space to pull the animation data coverage from. The larger the samples the more the data, but also the more memory and performance it takes.
- ``number_of_vertical_samples`` (int32):  [Read-Write] Sets the number of vertical samples in the blend space to pull the animation data coverage from.The larger the samples the more the data, but also the more memory and performance it takes.
- ``sampling_range`` (FloatInterval):  [Read-Write] It allows users to set a time range to an individual blend space in the database.
  This is effectively trimming the beginning and end of the animation in the database (not in the original blend space).
  If set to [0, 0] it will be the entire frame range of the original blend space.
- ``use_grid_for_sampling`` (bool):  [Read-Write] When turned on, this will use the set grid samples of the blend space asset for sampling. This will override the Number of Horizontal/Vertical Samples.
- ``use_single_sample`` (bool):  [Read-Write] If true this BlendSpace will output a single segment in the database.

<a id="unreal.PoseSearchDatabaseBlendSpaceEx.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PoseSearchDatabaseAnimCompositeEx"></a>