## StaticMesh Objects

```python
class StaticMesh(StreamableRenderAsset)
```

A StaticMesh is a piece of geometry that consists of a static set of polygons.
Static Meshes can be translated, rotated, and scaled, but they cannot have their vertices animated in any way. As such, they are more efficient
to render than other types of geometry such as USkeletalMesh, and they are often the basic building block of levels created in the engine.
see: https://docs.unrealengine.com/latest/INT/Engine/Content/Types/StaticMeshes/
see: AStaticMeshActor, UStaticMeshComponent

**C++ Source:**

- **Module**: Engine
- **File**: StaticMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_cpu_access`` (bool):  [Read-Write] If true, will keep geometry data CPU-accessible in cooked builds, rather than uploading to GPU memory and releasing it from CPU memory.
  This is required if you wish to access StaticMesh geometry data on the CPU at runtime in cooked builds (e.g. to convert StaticMesh to ProceduralMeshComponent)
- ``asset_import_data`` (AssetImportData):  [Read-Write] Importing data and options used for this mesh
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``body_setup`` (BodySetup):  [Read-Write]
- ``complex_collision_mesh`` (StaticMesh):  [Read-Write]
- ``customized_collision`` (bool):  [Read-Write] If the user has modified collision in any way or has custom collision imported. Used for determining if to auto generate collision on import
- ``distance_field_self_shadow_bias`` (float):  [Read-Write] Useful for reducing self shadowing from distance field methods when using world position offset to animate the mesh's vertices.
- ``generate_mesh_distance_field`` (bool):  [Read-Write] Whether to generate a distance field for this mesh, which can be used by DistanceField Indirect Shadows.
  This is ignored if the project's 'Generate Mesh Distance Fields' setting is enabled.
- ``global_force_mip_levels_to_be_resident`` (bool):  [Read-Write] Global and serialized version of ForceMiplevelsToBeResident.
- ``has_navigation_data`` (bool):  [Read-Write] If true, mesh will have NavCollision property with additional data for navmesh generation and usage.
            Set to false for distant meshes (always outside navigation bounds) to save memory on collision data.
- ``light_map_coordinate_index`` (int32):  [Read-Write] The light map coordinate index
- ``light_map_resolution`` (int32):  [Read-Write] The light map resolution
- ``lod_for_collision`` (int32):  [Read-Write] Specifies which mesh LOD to use for complex (per-poly) collision.
  Sometimes it can be desirable to use a lower poly representation for collision to reduce memory usage, improve performance and behaviour.
  Collision representation does not change based on distance to camera.
- ``lod_group`` (Name):  [Read-Write] The LOD group to which this mesh belongs.
- ``mesh_paint_texture_coordinate_index`` (int32):  [Read-Write] The default coordinate index to use when texture color painting on this mesh.
- ``mesh_paint_texture_resolution`` (int32):  [Read-Write] The resolution of texture color mesh paint textures on this mesh.
  The final size will be rounded up to a power of 2 and a multiple of the "Mesh Paint Tile Size" project setting.
  A default value of 0 will auto calculate the size using the "Mesh paint texels per vertex" project setting.
- ``nanite_settings`` (MeshNaniteSettings):  [Read-Write] Settings related to building Nanite data.
- ``nav_collision`` (NavCollisionBase):  [Read-Only]
- ``negative_bounds_extension`` (Vector):  [Read-Write]
- ``never_stream`` (bool):  [Read-Write]
- ``num_cinematic_mip_levels`` (int32):  [Read-Write] Number of mip-levels to use for cinematic quality.
- ``positive_bounds_extension`` (Vector):  [Read-Write]
- ``static_materials`` (Array[StaticMaterial]):  [Read-Write]
- ``static_mesh_paint_support`` (StaticMeshPaintSupport):  [Read-Write] Whether to support per instance texture color mesh painting on components using this mesh.
- ``support_gpu_uniformly_distributed_sampling`` (bool):  [Read-Write] If true, a GPU buffer containing required data for uniform mesh surface sampling will be created at load time.
  It is created from the cpu data so bSupportUniformlyDistributedSampling is also required to be true.
- ``support_physical_material_masks`` (bool):  [Read-Write] If true, complex collision data will store UVs and face remap table for use when performing
  PhysicalMaterialMask lookups in cooked builds. Note the increased memory cost for this
  functionality.
- ``support_ray_tracing`` (bool):  [Read-Write] If true, a ray tracing acceleration structure will be built for this mesh and it may be used in ray tracing effects
- ``support_uniformly_distributed_sampling`` (bool):  [Read-Write] Mesh supports uniformly distributed sampling in constant time.
  Memory cost is 8 bytes per triangle.
  Example usage is uniform spawning of particles.
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``use_legacy_tangent_scaling`` (bool):  [Read-Write]

<a id="unreal.StaticMesh.static_materials"></a>

#### static_materials

```python
@property
def static_materials() -> Array[StaticMaterial]
```

(Array[StaticMaterial]):  [Read-Write]

<a id="unreal.StaticMesh.static_materials"></a>

#### static_materials

```python
@static_materials.setter
def static_materials(value: Array[StaticMaterial]) -> None
```

<a id="unreal.StaticMesh.static_mesh_paint_support"></a>

#### static_mesh_paint_support

```python
@property
def static_mesh_paint_support() -> StaticMeshPaintSupport
```

(StaticMeshPaintSupport):  [Read-Write] Whether to support per instance texture color mesh painting on components using this mesh.

<a id="unreal.StaticMesh.static_mesh_paint_support"></a>

#### static_mesh_paint_support

```python
@static_mesh_paint_support.setter
def static_mesh_paint_support(value: StaticMeshPaintSupport) -> None
```

<a id="unreal.StaticMesh.lod_for_collision"></a>

#### lod_for_collision

```python
@property
def lod_for_collision() -> int
```

(int32):  [Read-Write] Specifies which mesh LOD to use for complex (per-poly) collision.
Sometimes it can be desirable to use a lower poly representation for collision to reduce memory usage, improve performance and behaviour.
Collision representation does not change based on distance to camera.

<a id="unreal.StaticMesh.lod_for_collision"></a>

#### lod_for_collision

```python
@lod_for_collision.setter
def lod_for_collision(value: int) -> None
```

<a id="unreal.StaticMesh.set_num_source_models"></a>

#### set_num_source_models

```python
def set_num_source_models(num: int) -> None
```

x.set_num_source_models(num) -> None
Set Num Source Models

Args:
    num (int32):

<a id="unreal.StaticMesh.set_min_lod_for_quality_levels"></a>

#### set_min_lod_for_quality_levels

```python
def set_min_lod_for_quality_levels(quality_level_minimum_lo_ds: Map[
    PerQualityLevels, int],
                                   default: int = -1) -> None
```

x.set_min_lod_for_quality_levels(quality_level_minimum_lo_ds, default=-1) -> None
Allow to override min lod quality levels on a staticMesh and it Default value (-1 value for Default dont override its value).

Args:
    quality_level_minimum_lo_ds (Map[PerQualityLevels, int32]): 
    default (int32):

<a id="unreal.StaticMesh.set_minimum_lod_for_platforms"></a>

#### set_minimum_lod_for_platforms

```python
def set_minimum_lod_for_platforms(
        platform_minimum_lo_ds: Map[Name, int]) -> None
```

x.set_minimum_lod_for_platforms(platform_minimum_lo_ds) -> None
Set Minimum LODFor Platforms

Args:
    platform_minimum_lo_ds (Map[Name, int32]):

<a id="unreal.StaticMesh.set_minimum_lod_for_platform"></a>

#### set_minimum_lod_for_platform

```python
def set_minimum_lod_for_platform(platform_name: Name, min_lod: int) -> None
```

x.set_minimum_lod_for_platform(platform_name, min_lod) -> None
Set Minimum LODFor Platform

Args:
    platform_name (Name): 
    min_lod (int32):

<a id="unreal.StaticMesh.set_material"></a>

#### set_material

```python
def set_material(material_index: int, new_material: MaterialInterface) -> None
```

x.set_material(material_index, new_material) -> None
Sets a Material given a Material Index

Args:
    material_index (int32): 
    new_material (MaterialInterface):

<a id="unreal.StaticMesh.remove_socket"></a>

#### remove_socket

```python
def remove_socket(socket: StaticMeshSocket) -> None
```

x.remove_socket(socket) -> None
Remove a socket object in this StaticMesh by providing it's pointer. Use FindSocket() if needed.

Args:
    socket (StaticMeshSocket):

<a id="unreal.StaticMesh.is_lod_screen_size_auto_computed"></a>

#### is_lod_screen_size_auto_computed

```python
def is_lod_screen_size_auto_computed() -> bool
```

x.is_lod_screen_size_auto_computed() -> bool
Is LODScreen Size Auto Computed

Returns:
    bool:

<a id="unreal.StaticMesh.get_static_mesh_description"></a>

#### get_static_mesh_description

```python
def get_static_mesh_description(lod_index: int) -> StaticMeshDescription
```

x.get_static_mesh_description(lod_index) -> StaticMeshDescription
Return a new StaticMeshDescription referencing the MeshDescription of the given LOD

Args:
    lod_index (int32): 

Returns:
    StaticMeshDescription:

<a id="unreal.StaticMesh.get_sockets_by_tag"></a>

#### get_sockets_by_tag

```python
def get_sockets_by_tag(socket_tag: str) -> Array[StaticMeshSocket]
```

x.get_sockets_by_tag(socket_tag) -> Array[StaticMeshSocket]
Returns a list of sockets with the provided tag.

Args:
    socket_tag (str): 

Returns:
    Array[StaticMeshSocket]:

<a id="unreal.StaticMesh.get_num_triangles"></a>

#### get_num_triangles

```python
def get_num_triangles(lod_index: int) -> int
```

x.get_num_triangles(lod_index) -> int32
Returns the number of triangles in the render data for the specified LOD.

Args:
    lod_index (int32): 

Returns:
    int32:

<a id="unreal.StaticMesh.get_num_sections"></a>

#### get_num_sections

```python
def get_num_sections(lod: int) -> int
```

x.get_num_sections(lod) -> int32
Returns number of Sections that this StaticMesh has, in the supplied LOD (LOD 0 is the highest)

Args:
    lod (int32): 

Returns:
    int32:

<a id="unreal.StaticMesh.get_num_lods"></a>

#### get_num_lods

```python
def get_num_lods() -> int
```

x.get_num_lods() -> int32
Returns the number of LODs used by the mesh.

Returns:
    int32:

<a id="unreal.StaticMesh.get_min_lod_for_quality_levels"></a>

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

<a id="unreal.StaticMesh.get_minimum_lod_for_quality_levels"></a>

#### get_minimum_lod_for_quality_levels

```python
def get_minimum_lod_for_quality_levels() -> Map[Name, int]
```

x.get_minimum_lod_for_quality_levels() -> Map[Name, int32]
Get Minimum LODFor Quality Levels

Returns:
    Map[Name, int32]: 

    quality_level_minimum_lo_ds (Map[Name, int32]):

<a id="unreal.StaticMesh.get_minimum_lod_for_quality_level"></a>

#### get_minimum_lod_for_quality_level

```python
def get_minimum_lod_for_quality_level(quality_level: Name) -> int
```

x.get_minimum_lod_for_quality_level(quality_level) -> int32
Get Minimum LODFor Quality Level

Args:
    quality_level (Name): 

Returns:
    int32:

<a id="unreal.StaticMesh.get_minimum_lod_for_platforms"></a>

#### get_minimum_lod_for_platforms

```python
def get_minimum_lod_for_platforms() -> Map[Name, int]
```

x.get_minimum_lod_for_platforms() -> Map[Name, int32]
Get Minimum LODFor Platforms

Returns:
    Map[Name, int32]: 

    platform_minimum_lo_ds (Map[Name, int32]):

<a id="unreal.StaticMesh.get_minimum_lod_for_platform"></a>

#### get_minimum_lod_for_platform

```python
def get_minimum_lod_for_platform(platform_name: Name) -> int
```

x.get_minimum_lod_for_platform(platform_name) -> int32
Get Minimum LODFor Platform

Args:
    platform_name (Name): 

Returns:
    int32:

<a id="unreal.StaticMesh.get_material_index"></a>

#### get_material_index

```python
def get_material_index(material_slot_name: Name) -> int
```

x.get_material_index(material_slot_name) -> int32
Gets a Material index given a slot name

Args:
    material_slot_name (Name): 

Returns:
    int32: Requested material

<a id="unreal.StaticMesh.get_material"></a>

#### get_material

```python
def get_material(material_index: int) -> MaterialInterface
```

x.get_material(material_index) -> MaterialInterface
Gets a Material given a Material Index and an LOD number

Args:
    material_index (int32): 

Returns:
    MaterialInterface: Requested material

<a id="unreal.StaticMesh.get_bounds"></a>

#### get_bounds

```python
def get_bounds() -> BoxSphereBounds
```

x.get_bounds() -> BoxSphereBounds
Returns the number of bounds of the mesh.

Returns:
    BoxSphereBounds: The bounding box represented as box origin with extents and also a sphere that encapsulates that box

<a id="unreal.StaticMesh.get_bounding_box"></a>

#### get_bounding_box

```python
def get_bounding_box() -> Box
```

x.get_bounding_box() -> Box
Returns the bounding box, in local space including bounds extension(s), of the StaticMesh asset

Returns:
    Box:

<a id="unreal.StaticMesh.find_socket"></a>

#### find_socket

```python
def find_socket(socket_name: Name) -> StaticMeshSocket
```

x.find_socket(socket_name) -> StaticMeshSocket
Find a socket object in this StaticMesh by name.
Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.

Args:
    socket_name (Name): 

Returns:
    StaticMeshSocket:

<a id="unreal.StaticMesh.create_static_mesh_description"></a>

#### create_static_mesh_description

```python
@classmethod
def create_static_mesh_description(cls,
                                   outer: Object = None
                                   ) -> StaticMeshDescription
```

X.create_static_mesh_description(outer=None) -> StaticMeshDescription
Create an empty StaticMeshDescription object, to describe a static mesh at runtime

Args:
    outer (Object): 

Returns:
    StaticMeshDescription:

<a id="unreal.StaticMesh.build_from_static_mesh_descriptions"></a>

#### build_from_static_mesh_descriptions

```python
def build_from_static_mesh_descriptions(
        static_mesh_descriptions: Array[StaticMeshDescription],
        build_simple_collision: bool = False,
        fast_build: bool = True) -> None
```

x.build_from_static_mesh_descriptions(static_mesh_descriptions, build_simple_collision=False, fast_build=True) -> None
Builds static mesh LODs from the array of StaticMeshDescriptions passed in

Args:
    static_mesh_descriptions (Array[StaticMeshDescription]): 
    build_simple_collision (bool): 
    fast_build (bool):

<a id="unreal.StaticMesh.add_socket"></a>

#### add_socket

```python
def add_socket(socket: StaticMeshSocket) -> None
```

x.add_socket(socket) -> None
Add a socket object in this StaticMesh.

Args:
    socket (StaticMeshSocket):

<a id="unreal.StaticMesh.add_material"></a>

#### add_material

```python
def add_material(material: MaterialInterface) -> Name
```

x.add_material(material) -> Name
Adds a new material and return its slot name

Args:
    material (MaterialInterface): 

Returns:
    Name:

<a id="unreal.StaticMesh.has_asset_user_data_of_class"></a>

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

<a id="unreal.StaticMesh.get_asset_user_data_of_class"></a>

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

<a id="unreal.StaticMesh.add_asset_user_data_of_class"></a>

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

<a id="unreal.ActorTextureStreamingBuildDataComponent"></a>