## Skeleton Objects

```python
class Skeleton(Object)
```

USkeleton : that links between mesh and animation
        - Bone hierarchy for animations
        - Bone/track linkup between mesh and animation
        - Retargetting related

**C++ Source:**

- **Module**: Engine
- **File**: Skeleton.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``bone_tree`` (Array[BoneNode]):  [Read-Only] Skeleton bone tree - each contains name and parent index*
- ``compatible_skeletons`` (Array[Skeleton]):  [Read-Write] The list of compatible skeletons. This skeleton will be able to use animation data originating from skeletons within this array, such as animation sequences.
  This property is not bi-directional.

  This is an array of TSoftObjectPtr in order to prevent all skeletons to be loaded, as we only want to load things on demand.
  As this is EditAnywhere and an array of TSoftObjectPtr, checking validity of pointers is needed.
- ``preview_forward_axis`` (AxisType):  [Read-Write] Preview axis to consider as "forward" for the skeleton. Only used for preview purposes.

<a id="unreal.Skeleton.compatible_skeletons"></a>

#### compatible_skeletons

```python
@property
def compatible_skeletons() -> Array[Skeleton]
```

(Array[Skeleton]):  [Read-Only] The list of compatible skeletons. This skeleton will be able to use animation data originating from skeletons within this array, such as animation sequences.
This property is not bi-directional.

This is an array of TSoftObjectPtr in order to prevent all skeletons to be loaded, as we only want to load things on demand.
As this is EditAnywhere and an array of TSoftObjectPtr, checking validity of pointers is needed.

<a id="unreal.Skeleton.get_blend_profile"></a>

#### get_blend_profile

```python
def get_blend_profile(profile_name: Name) -> BlendProfile
```

x.get_blend_profile(profile_name) -> BlendProfile
Get the specified blend profile by name

Args:
    profile_name (Name): 

Returns:
    BlendProfile:

<a id="unreal.Skeleton.add_compatible_skeleton_soft"></a>

#### add_compatible_skeleton_soft

```python
def add_compatible_skeleton_soft(source_skeleton: Skeleton) -> None
```

x.add_compatible_skeleton_soft(source_skeleton) -> None
Add Compatible Skeleton Soft

Args:
    source_skeleton (Skeleton):

<a id="unreal.Skeleton.add_compatible_skeleton"></a>

#### add_compatible_skeleton

```python
def add_compatible_skeleton(source_skeleton: Skeleton) -> None
```

x.add_compatible_skeleton(source_skeleton) -> None
Add Compatible Skeleton

Args:
    source_skeleton (Skeleton):

<a id="unreal.Skeleton.has_asset_user_data_of_class"></a>

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

<a id="unreal.Skeleton.get_asset_user_data_of_class"></a>

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

<a id="unreal.Skeleton.add_asset_user_data_of_class"></a>

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

<a id="unreal.Skeleton.get_reference_pose"></a>

#### get_reference_pose

```python
def get_reference_pose() -> AnimPose
```

x.get_reference_pose() -> AnimPose
Populates an Anim Pose with the reference poses stored for the provided USkeleton

Returns:
    AnimPose: 

    out_pose (AnimPose): Anim pose to hold the reference pose

<a id="unreal.Skeleton.get_curve_identifiers"></a>

#### get_curve_identifiers

```python
def get_curve_identifiers(
        curve_type: RawCurveTrackTypes) -> Array[AnimationCurveIdentifier]
```

x.get_curve_identifiers(curve_type) -> Array[AnimationCurveIdentifier]
Retrieves all curve identifiers for a specific curve types from the provided Skeleton
deprecated: Curve identifiers are no longer retrievable globally from the skeleton, they are specified per-animation.

Args:
    curve_type (RawCurveTrackTypes): Type of the curve identifers to retrieve

Returns:
    Array[AnimationCurveIdentifier]: Array of FAnimationCurveIdentifier instances each representing a unique curve if the operation was successful, empyty array otherwise

<a id="unreal.Skeleton.get_curve_identifier"></a>

#### get_curve_identifier

```python
def get_curve_identifier(
        name: Name,
        curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
```

x.get_curve_identifier(name, curve_type) -> AnimationCurveIdentifier
Get Curve Identifier
deprecated: Please use SetCurveIdentifier.

Args:
    name (Name): 
    curve_type (RawCurveTrackTypes): 

Returns:
    AnimationCurveIdentifier:

<a id="unreal.Skeleton.find_curve_identifier"></a>

#### find_curve_identifier

```python
def find_curve_identifier(
        name: Name,
        curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
```

x.find_curve_identifier(name, curve_type) -> AnimationCurveIdentifier
Tries to construct a valid FAnimationCurveIdentifier instance. It tries to find the underlying SmartName on the provided Skeleton for the provided curve type.
deprecated: Curve identifiers are no longer retrievable globally from the skeleton, they are specified per-animation.

Args:
    name (Name): Name of the curve to find
    curve_type (RawCurveTrackTypes): Type of the curve to find

Returns:
    AnimationCurveIdentifier: Valid FAnimationCurveIdentifier if the name exists on the skeleton and the operation was successful, invalid otherwise

<a id="unreal.Skeleton.copy_bones_from_skeleton"></a>

#### copy_bones_from_skeleton

```python
def copy_bones_from_skeleton(
        target_mesh: DynamicMesh,
        options: GeometryScriptCopyBonesFromMeshOptions = [
            False, BonesToCopyFromSource.ALL_BONES
        ],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.copy_bones_from_skeleton(target_mesh, options=[False, BonesToCopyFromSource.ALL_BONES], debug=None) -> DynamicMesh
Copy the bone attributes (skeleton) from the SourceSkeleton to the TargetMesh.

Args:
    target_mesh (DynamicMesh): Mesh we are copying the bone attributes to.
    options (GeometryScriptCopyBonesFromMeshOptions): An option object to control how the copying is performed.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.AnimationAsset"></a>