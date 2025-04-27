## AnimationAsset Objects

```python
class AnimationAsset(Object)
```

Animation Asset

**C++ Source:**

- **Module**: Engine
- **File**: AnimationAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_mapping_table`` (AssetMappingTable):  [Read-Only] Asset mapping table when ParentAsset is set
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``meta_data`` (Array[AnimMetaData]):  [Read-Write] Meta data that can be saved with the asset

  You can query by GetMetaData function
- ``parent_asset`` (AnimationAsset):  [Read-Only] Parent Asset, if set, you won't be able to edit any data in here but just mapping table

  During cooking, this data will be used to bake out to normal asset
- ``preview_pose_asset`` (PoseAsset):  [Read-Write] The default skeletal mesh to use when previewing this asset - this only applies when you open Persona using this asset//
  todo:: note that this doesn't retarget right now
- ``skeleton`` (Skeleton):  [Read-Only] Pointer to the Skeleton this asset can be played on .
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.AnimationAsset.set_preview_skeletal_mesh"></a>

#### set_preview_skeletal_mesh

```python
def set_preview_skeletal_mesh(preview_mesh: SkeletalMesh) -> None
```

x.set_preview_skeletal_mesh(preview_mesh) -> None
Sets or updates the preview skeletal mesh

Args:
    preview_mesh (SkeletalMesh):

<a id="unreal.AnimationAsset.get_play_length"></a>

#### get_play_length

```python
def get_play_length() -> float
```

x.get_play_length() -> float
Get Play Length

Returns:
    float:

<a id="unreal.AnimationAsset.find_meta_data_by_class"></a>

#### find_meta_data_by_class

```python
def find_meta_data_by_class(meta_data_class: Class) -> AnimMetaData
```

x.find_meta_data_by_class(meta_data_class) -> AnimMetaData
Returns the first metadata of the specified class

Args:
    meta_data_class (type(Class)): 

Returns:
    AnimMetaData:

<a id="unreal.AnimationAsset.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.AnimationAsset.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.AnimationAsset.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.AnimationAsset.get_skeleton"></a>

#### get_skeleton

```python
def get_skeleton() -> Skeleton
```

x.get_skeleton() -> Skeleton


Returns:
    Skeleton: The target USkeleton for the provided UAnimationAsset

<a id="unreal.AnimationAsset.create_attribute_identifier"></a>

#### create_attribute_identifier

```python
def create_attribute_identifier(
        attribute_name: Name,
        bone_name: Name,
        attribute_type: ScriptStruct,
        validate_exists_on_asset: bool = False
) -> AnimationAttributeIdentifier
```

x.create_attribute_identifier(attribute_name, bone_name, attribute_type, validate_exists_on_asset=False) -> AnimationAttributeIdentifier
Constructs a valid FAnimationAttributeIdentifier instance. Ensuring that the underlying BoneName exists on the Skeleton for the provided AnimationAsset.

Args:
    attribute_name (Name): Name of the attribute
    bone_name (Name): Name of the bone this attribute should be attributed to
    attribute_type (ScriptStruct): Type of the underlying data (to-be) stored by this attribute
    validate_exists_on_asset (bool): Whether or not the attribute should exist on the AnimationAsset. False by default.

Returns:
    AnimationAttributeIdentifier: Valid FAnimationCurveIdentifier if the operation was successful

<a id="unreal.AnimSequenceBase"></a>