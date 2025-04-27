## PoseAsset Objects

```python
class PoseAsset(AnimationAsset)
```

Pose Asset that can be blended by weight of curves

**C++ Source:**

- **Module**: Engine
- **File**: PoseAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additive_pose`` (bool):  [Read-Write] Whether or not Additive Pose or not - these are property that needs post process, so
- ``asset_mapping_table`` (AssetMappingTable):  [Read-Only] Asset mapping table when ParentAsset is set
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``meta_data`` (Array[AnimMetaData]):  [Read-Write] Meta data that can be saved with the asset

  You can query by GetMetaData function
- ``parent_asset`` (AnimationAsset):  [Read-Only] Parent Asset, if set, you won't be able to edit any data in here but just mapping table

  During cooking, this data will be used to bake out to normal asset
- ``preview_pose_asset`` (PoseAsset):  [Read-Write] The default skeletal mesh to use when previewing this asset - this only applies when you open Persona using this asset//
  todo:: note that this doesn't retarget right now
- ``retarget_source`` (Name):  [Read-Write] Base pose to use when retargeting
- ``retarget_source_asset`` (SkeletalMesh):  [Read-Write]
- ``skeleton`` (Skeleton):  [Read-Only] Pointer to the Skeleton this asset can be played on .
- ``source_animation`` (AnimSequence):  [Read-Write]
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.PoseAsset.update_retarget_source_asset_data"></a>

#### update_retarget_source_asset_data

```python
def update_retarget_source_asset_data() -> None
```

x.update_retarget_source_asset_data() -> None
Update the retarget data pose from the source, if it exist, else clears the retarget data pose saved in RetargetSourceAssetReferencePose.
Warning : This function calls LoadSynchronous at the retarget source asset soft object pointer, so it can not be used at PostLoad

<a id="unreal.PoseAsset.update_pose_from_animation"></a>

#### update_pose_from_animation

```python
def update_pose_from_animation(anim_sequence: AnimSequence) -> None
```

x.update_pose_from_animation(anim_sequence) -> None
Contained poses are re-generated from the provided Animation Sequence

Args:
    anim_sequence (AnimSequence):

<a id="unreal.PoseAsset.set_retarget_source_asset"></a>

#### set_retarget_source_asset

```python
def set_retarget_source_asset(retarget_source_asset: SkeletalMesh) -> None
```

x.set_retarget_source_asset(retarget_source_asset) -> None
Assigns the passed skeletal mesh to the retarget source

Args:
    retarget_source_asset (SkeletalMesh):

<a id="unreal.PoseAsset.set_base_pose_name"></a>

#### set_base_pose_name

```python
def set_base_pose_name(new_base_pose_name: Name) -> bool
```

x.set_base_pose_name(new_base_pose_name) -> bool
Set base pose index by name, NAME_None indicates reference pose - returns true if set successfully

Args:
    new_base_pose_name (Name): 

Returns:
    bool:

<a id="unreal.PoseAsset.rename_pose"></a>

#### rename_pose

```python
def rename_pose(original_pose_name: Name, new_pose_name: Name) -> None
```

x.rename_pose(original_pose_name, new_pose_name) -> None
Renames a specific pose

Args:
    original_pose_name (Name): 
    new_pose_name (Name):

<a id="unreal.PoseAsset.get_retarget_source_asset"></a>

#### get_retarget_source_asset

```python
def get_retarget_source_asset() -> SkeletalMesh
```

x.get_retarget_source_asset() -> SkeletalMesh
Returns the retarget source asset soft object pointer.

Returns:
    SkeletalMesh:

<a id="unreal.PoseAsset.get_pose_names"></a>

#### get_pose_names

```python
def get_pose_names() -> Array[Name]
```

x.get_pose_names() -> Array[Name]
Returns the name of all contained poses

Returns:
    Array[Name]: 

    pose_names (Array[Name]):

<a id="unreal.PoseAsset.get_base_pose_name"></a>

#### get_base_pose_name

```python
def get_base_pose_name() -> Name
```

x.get_base_pose_name() -> Name
Returns base pose name, only valid when additive, NAME_None indicates reference pose

Returns:
    Name:

<a id="unreal.PoseAsset.clear_retarget_source_asset"></a>

#### clear_retarget_source_asset

```python
def clear_retarget_source_asset() -> None
```

x.clear_retarget_source_asset() -> None
Resets the retarget source asset

<a id="unreal.PreviewMeshCollection"></a>