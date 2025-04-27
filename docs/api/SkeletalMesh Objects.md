## SkeletalMesh Objects

```python
class SkeletalMesh(SkinnedAsset)
```

SkeletalMesh is geometry bound to a hierarchical skeleton of bones which can be animated for the purpose of deforming the mesh.
Skeletal Meshes are built up of two parts; a set of polygons composed to make up the surface of the mesh, and a hierarchical skeleton which can be used to animate the polygons.
The 3D models, rigging, and animations are created in an external modeling and animation application (3DSMax, Maya, Softimage, etc).
see: https://docs.unrealengine.com/latest/INT/Engine/Content/Types/SkeletalMeshes/

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Write]
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``cloth_lod_bias_mode`` (ClothLODBiasMode):  [Read-Write]
- ``default_animating_rig`` (Object):  [Read-Write]
- ``default_mesh_deformer`` (MeshDeformer):  [Read-Write]
- ``disable_below_min_lod_stripping`` (PerPlatformBool):  [Read-Write]
- ``enable_per_poly_collision`` (bool):  [Read-Write]
- ``global_force_mip_levels_to_be_resident`` (bool):  [Read-Write] Global and serialized version of ForceMiplevelsToBeResident.
- ``lod_info`` (Array[SkeletalMeshLODInfo]):  [Read-Write]
- ``lod_settings`` (SkeletalMeshLODSettings):  [Read-Write]
- ``materials`` (Array[SkeletalMaterial]):  [Read-Write]
- ``max_num_optional_lo_ds`` (PerPlatformInt):  [Read-Write]
- ``max_num_streamed_lo_ds`` (PerPlatformInt):  [Read-Write]
- ``mesh_clothing_assets`` (Array[ClothingAssetBase]):  [Read-Write]
- ``min_lod`` (PerPlatformInt):  [Read-Write]
- ``min_quality_level_lod`` (PerQualityLevelInt):  [Read-Write]
- ``morph_targets`` (Array[MorphTarget]):  [Read-Write]
- ``nanite_settings`` (MeshNaniteSettings):  [Read-Write] Settings related to building Nanite data.
- ``negative_bounds_extension`` (Vector):  [Read-Write]
- ``never_stream`` (bool):  [Read-Write]
- ``node_mapping_data`` (Array[NodeMappingContainer]):  [Read-Write]
- ``num_cinematic_mip_levels`` (int32):  [Read-Write] Number of mip-levels to use for cinematic quality.
- ``overlay_material`` (MaterialInterface):  [Read-Write]
- ``overlay_material_max_draw_distance`` (float):  [Read-Write]
- ``override_lod_streaming_settings`` (bool):  [Read-Write]
- ``physics_asset`` (PhysicsAsset):  [Read-Write]
- ``positive_bounds_extension`` (Vector):  [Read-Write]
- ``post_process_anim_blueprint`` (type(Class)):  [Read-Write]
- ``post_process_anim_bplod_threshold`` (int32):  [Read-Write] * Max LOD level that post-process AnimBPs are evaluated.
  * For example if you have the threshold set to 2, it will evaluate until including LOD 2 (based on 0 index). In case the LOD level gets set to 3, it will stop evaluating the post-process AnimBP.
  * Setting it to -1 will always evaluate it and disable LODing.
- ``ray_tracing_min_lod`` (int32):  [Read-Write]
- ``sampling_info`` (SkeletalMeshSamplingInfo):  [Read-Write]
- ``shadow_physics_asset`` (PhysicsAsset):  [Read-Write]
- ``skel_mirror_axis`` (AxisType):  [Read-Write]
- ``skel_mirror_flip_axis`` (AxisType):  [Read-Write]
- ``skel_mirror_table`` (Array[BoneMirrorInfo]):  [Read-Write]
- ``skeleton`` (Skeleton):  [Read-Only]
- ``skin_weight_profiles`` (Array[SkinWeightProfileInfo]):  [Read-Write]
- ``support_lod_streaming`` (PerPlatformBool):  [Read-Write]
- ``support_ray_tracing`` (bool):  [Read-Write]
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only]

<a id="unreal.SkeletalMesh.skeleton"></a>

#### skeleton

```python
@property
def skeleton() -> Skeleton
```

(Skeleton):  [Read-Only]

<a id="unreal.SkeletalMesh.positive_bounds_extension"></a>

#### positive_bounds_extension

```python
@property
def positive_bounds_extension() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkeletalMesh.negative_bounds_extension"></a>

#### negative_bounds_extension

```python
@property
def negative_bounds_extension() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkeletalMesh.materials"></a>

#### materials

```python
@property
def materials() -> Array[SkeletalMaterial]
```

(Array[SkeletalMaterial]):  [Read-Write]

<a id="unreal.SkeletalMesh.materials"></a>

#### materials

```python
@materials.setter
def materials(value: Array[SkeletalMaterial]) -> None
```

<a id="unreal.SkeletalMesh.lod_settings"></a>

#### lod_settings

```python
@property
def lod_settings() -> SkeletalMeshLODSettings
```

(SkeletalMeshLODSettings):  [Read-Write]

<a id="unreal.SkeletalMesh.lod_settings"></a>

#### lod_settings

```python
@lod_settings.setter
def lod_settings(value: SkeletalMeshLODSettings) -> None
```

<a id="unreal.SkeletalMesh.default_animating_rig"></a>

#### default_animating_rig

```python
@property
def default_animating_rig() -> Object
```

(Object):  [Read-Write]

<a id="unreal.SkeletalMesh.default_animating_rig"></a>

#### default_animating_rig

```python
@default_animating_rig.setter
def default_animating_rig(value: Object) -> None
```

<a id="unreal.SkeletalMesh.physics_asset"></a>

#### physics_asset

```python
@property
def physics_asset() -> PhysicsAsset
```

(PhysicsAsset):  [Read-Only]

<a id="unreal.SkeletalMesh.shadow_physics_asset"></a>

#### shadow_physics_asset

```python
@property
def shadow_physics_asset() -> PhysicsAsset
```

(PhysicsAsset):  [Read-Only]

<a id="unreal.SkeletalMesh.node_mapping_data"></a>

#### node_mapping_data

```python
@property
def node_mapping_data() -> Array[NodeMappingContainer]
```

(Array[NodeMappingContainer]):  [Read-Only]

<a id="unreal.SkeletalMesh.morph_targets"></a>

#### morph_targets

```python
@property
def morph_targets() -> Array[MorphTarget]
```

(Array[MorphTarget]):  [Read-Write]

<a id="unreal.SkeletalMesh.morph_targets"></a>

#### morph_targets

```python
@morph_targets.setter
def morph_targets(value: Array[MorphTarget]) -> None
```

<a id="unreal.SkeletalMesh.post_process_anim_blueprint"></a>

#### post_process_anim_blueprint

```python
@property
def post_process_anim_blueprint() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.SkeletalMesh.mesh_clothing_assets"></a>

#### mesh_clothing_assets

```python
@property
def mesh_clothing_assets() -> Array[ClothingAssetBase]
```

(Array[ClothingAssetBase]):  [Read-Write]

<a id="unreal.SkeletalMesh.mesh_clothing_assets"></a>

#### mesh_clothing_assets

```python
@mesh_clothing_assets.setter
def mesh_clothing_assets(value: Array[ClothingAssetBase]) -> None
```

<a id="unreal.SkeletalMesh.default_mesh_deformer"></a>

#### default_mesh_deformer

```python
@property
def default_mesh_deformer() -> MeshDeformer
```

(MeshDeformer):  [Read-Only]

<a id="unreal.SkeletalMesh.overlay_material"></a>

#### overlay_material

```python
@property
def overlay_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only]

<a id="unreal.SkeletalMesh.overlay_material_max_draw_distance"></a>

#### overlay_material_max_draw_distance

```python
@property
def overlay_material_max_draw_distance() -> float
```

(float):  [Read-Only]

<a id="unreal.SkeletalMesh.set_overlay_material_max_draw_distance"></a>

#### set_overlay_material_max_draw_distance

```python
def set_overlay_material_max_draw_distance(max_draw_distance: float) -> None
```

x.set_overlay_material_max_draw_distance(max_draw_distance) -> None
Change the default overlay material max draw distance used by this mesh

Args:
    max_draw_distance (float):

<a id="unreal.SkeletalMesh.set_overlay_material"></a>

#### set_overlay_material

```python
def set_overlay_material(new_overlay_material: MaterialInterface) -> None
```

x.set_overlay_material(new_overlay_material) -> None
Change the default overlay material used by this mesh

Args:
    new_overlay_material (MaterialInterface):

<a id="unreal.SkeletalMesh.set_min_lod_for_quality_levels"></a>

#### set_min_lod_for_quality_levels

```python
def set_min_lod_for_quality_levels(quality_level_minimum_lo_ds: Map[
    PerQualityLevels, int],
                                   default: int = -1) -> None
```

x.set_min_lod_for_quality_levels(quality_level_minimum_lo_ds, default=-1) -> None
Allow to override min lod quality levels on a skeletalMesh and it Default value (-1 value for Default dont override its value).

Args:
    quality_level_minimum_lo_ds (Map[PerQualityLevels, int32]): 
    default (int32):

<a id="unreal.SkeletalMesh.num_sockets"></a>

#### num_sockets

```python
def num_sockets() -> int
```

x.num_sockets() -> int32
Returns the number of sockets available. Both on this mesh and it's skeleton.

Returns:
    int32:

<a id="unreal.SkeletalMesh.get_all_morph_target_names"></a>

#### get_all_morph_target_names

```python
def get_all_morph_target_names() -> Array[str]
```

x.get_all_morph_target_names() -> Array[str]
Returns the list of all morph targets of this skeletal mesh

Returns:
    Array[str]: The list of morph targets

<a id="unreal.SkeletalMesh.is_section_using_cloth"></a>

#### is_section_using_cloth

```python
def is_section_using_cloth(section_index: int,
                           check_corresponding_sections: bool = True) -> bool
```

x.is_section_using_cloth(section_index, check_corresponding_sections=True) -> bool
Checks whether the provided section is using APEX cloth. if bCheckCorrespondingSections is true
disabled sections will defer to correspond sections to see if they use cloth (non-cloth sections
are disabled and another section added when cloth is enabled, using this flag allows for a check
on the original section to succeed)

Args:
    section_index (int32): Index to check
    check_corresponding_sections (bool): Whether to check corresponding sections for disabled sections

Returns:
    bool:

<a id="unreal.SkeletalMesh.get_socket_by_index"></a>

#### get_socket_by_index

```python
def get_socket_by_index(index: int) -> SkeletalMeshSocket
```

x.get_socket_by_index(index) -> SkeletalMeshSocket
Returns a socket by index. Max index is NumSockets(). The meshes sockets are accessed first, then the skeletons.

Args:
    index (int32): 

Returns:
    SkeletalMeshSocket:

<a id="unreal.SkeletalMesh.get_overlay_material_max_draw_distance"></a>

#### get_overlay_material_max_draw_distance

```python
def get_overlay_material_max_draw_distance() -> float
```

x.get_overlay_material_max_draw_distance() -> float
Get the default overlay material max draw distance used by this mesh

Returns:
    float:

<a id="unreal.SkeletalMesh.get_overlay_material"></a>

#### get_overlay_material

```python
def get_overlay_material() -> MaterialInterface
```

x.get_overlay_material() -> MaterialInterface
Get the default overlay material used by this mesh

Returns:
    MaterialInterface:

<a id="unreal.SkeletalMesh.get_node_mapping_container"></a>

#### get_node_mapping_container

```python
def get_node_mapping_container(
        source_asset: Blueprint) -> NodeMappingContainer
```

x.get_node_mapping_container(source_asset) -> NodeMappingContainer
Get Node Mapping Container

Args:
    source_asset (Blueprint): 

Returns:
    NodeMappingContainer:

<a id="unreal.SkeletalMesh.get_min_lod_for_quality_levels"></a>

#### get_min_lod_for_quality_levels

```python
def get_min_lod_for_quality_levels() -> Tuple[Map[PerQualityLevels, int], int]
```

x.get_min_lod_for_quality_levels() -> (quality_level_minimum_lo_ds=Map[PerQualityLevels, int32], default=int32)
Get Min LODFor Quality Levels

Returns:
    tuple: 

    quality_level_minimum_lo_ds (Map[PerQualityLevels, int32]): 

    default (int32):

<a id="unreal.SkeletalMesh.get_imported_bounds"></a>

#### get_imported_bounds

```python
def get_imported_bounds() -> BoxSphereBounds
```

x.get_imported_bounds() -> BoxSphereBounds
Get the original imported bounds of the skel mesh

Returns:
    BoxSphereBounds:

<a id="unreal.SkeletalMesh.has_vertex_colors"></a>

#### has_vertex_colors

```python
def has_vertex_colors() -> bool
```

x.has_vertex_colors() -> bool
Return whether the mesh has vertex colors. USkinnedAsset interface.

Returns:
    bool:

<a id="unreal.SkeletalMesh.get_default_mesh_deformer"></a>

#### get_default_mesh_deformer

```python
def get_default_mesh_deformer() -> MeshDeformer
```

x.get_default_mesh_deformer() -> MeshDeformer
Get the default mesh deformer used by this mesh. A mesh deformer is used to deform the skeletal mesh at runtime

Returns:
    MeshDeformer:

<a id="unreal.SkeletalMesh.get_bounds"></a>

#### get_bounds

```python
def get_bounds() -> BoxSphereBounds
```

x.get_bounds() -> BoxSphereBounds
Get the extended bounds of this mesh (imported bounds plus bounds extension). USkinnedAsset interface.

Returns:
    BoxSphereBounds:

<a id="unreal.SkeletalMesh.find_socket_and_index"></a>

#### find_socket_and_index

```python
def find_socket_and_index(socket_name: Name) -> Tuple[SkeletalMeshSocket, int]
```

x.find_socket_and_index(socket_name) -> (SkeletalMeshSocket, out_index=int32)
Find a socket object in this SkeletalMesh by name.
Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.
Also returns the index for the socket allowing for future fast access via GetSocketByIndex()

Args:
    socket_name (Name): 

Returns:
    int32: 

    out_index (int32):

<a id="unreal.SkeletalMesh.add_socket"></a>

#### add_socket

```python
def add_socket(socket: SkeletalMeshSocket,
               add_to_skeleton: bool = False) -> None
```

x.add_socket(socket, add_to_skeleton=False) -> None
Add a skeletal socket object to this SkeletalMesh, and optionally promotes it to USkeleton socket.

Args:
    socket (SkeletalMeshSocket): 
    add_to_skeleton (bool):

<a id="unreal.SkeletalMesh.has_asset_user_data_of_class"></a>

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

<a id="unreal.SkeletalMesh.get_asset_user_data_of_class"></a>

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

<a id="unreal.SkeletalMesh.add_asset_user_data_of_class"></a>

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

<a id="unreal.SkeletalMesh.rename_socket"></a>

#### rename_socket

```python
def rename_socket(old_name: Name, new_name: Name) -> bool
```

x.rename_socket(old_name, new_name) -> bool
Rename a socket within a skeleton

Args:
    old_name (Name): The old name of the socket
    new_name (Name): The new name of the socket

Returns:
    bool: true if the renaming succeeded.

<a id="unreal.SkeletalMesh.regenerate_lod"></a>

#### regenerate_lod

```python
def regenerate_lod(new_lod_count: int = 0,
                   regenerate_even_if_imported: bool = False,
                   generate_base_lod: bool = False) -> bool
```

x.regenerate_lod(new_lod_count=0, regenerate_even_if_imported=False, generate_base_lod=False) -> bool
Regenerate LODs of the mesh

Args:
    new_lod_count (int32): Set valid value (>0) if you want to change LOD count. Otherwise, it will use the current LOD and regenerate
    regenerate_even_if_imported (bool): If this is true, it only regenerate even if this LOD was imported before If false, it will regenerate for only previously auto generated ones
    generate_base_lod (bool): If this is true and there is some reduction data, the base LOD will be reduce according to the settings

Returns:
    bool: true if succeed. If mesh reduction is not available this will return false.

<a id="unreal.SkeletalMesh.strip_lod_geometry"></a>

#### strip_lod_geometry

```python
def strip_lod_geometry(lod_index: int, texture_mask: Texture2D,
                       threshold: float) -> bool
```

x.strip_lod_geometry(lod_index, texture_mask, threshold) -> bool
This function will strip all triangle in the specified LOD that don't have any UV area pointing on a black pixel in the TextureMask.
We use the UVChannel 0 to find the pixels in the texture.

Args:
    lod_index (int32): 
    texture_mask (Texture2D): 
    threshold (float): 

Returns:
    bool:

<a id="unreal.SkeletalMesh.remove_lo_ds"></a>

#### remove_lo_ds

```python
def remove_lo_ds(to_remove_lo_ds: Array[int]) -> bool
```

x.remove_lo_ds(to_remove_lo_ds) -> bool
Remove all the specified LODs. This function will remove all the valid LODs in the list.
Valid LOD is any LOD greater then 0 that exist in the skeletalmesh. We cannot remove the base LOD 0.

Args:
    to_remove_lo_ds (Array[int32]): The LODs we need to remove

Returns:
    bool: true if the successfully remove all the LODs. False otherwise, but evedn if it return false it will have removed all valid LODs.

<a id="unreal.SkeletalMeshLODSettings"></a>