## InterchangeGenericMeshPipeline Objects

```python
class InterchangeGenericMeshPipeline(InterchangePipelineBase)
```

Hide drop down will make sure the class is not showing in the class picker

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericMeshPipeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_compute_lod_screen_sizes`` (bool):  [Read-Write] If enabled, LOD Screen Sizes would be auto-computed.
- ``bone_influence_limit`` (int32):  [Read-Write] The maximum number of bone influences to allow each vertex in this mesh to use.
  If set higher than the limit determined by the project settings, it has no effect.
  If set to 0, the value is taken from the DefaultBoneInfluenceLimit project setting.
- ``build_nanite`` (bool):  [Read-Write] If enabled, imported meshes will be rendered by Nanite at runtime. Make sure your meshes and materials meet the requirements for Nanite.
- ``build_reversed_index_buffer`` (bool):  [Read-Write] If enabled, builds a reversed index buffer for each static mesh.
- ``build_scale3d`` (Vector):  [Read-Write] The local scale applied when building the mesh.
- ``collision`` (bool):  [Read-Write] If enabled, custom collision will be imported. If enabled and there is no custom collision, a generic collision will be automatically generated.
  If disabled, no collision will be created or imported.
- ``combine_skeletal_meshes`` (bool):  [Read-Write]
- ``combine_static_meshes`` (bool):  [Read-Write] If enabled, all translated static mesh nodes will be imported as a single static mesh.
- ``create_physics_asset`` (bool):  [Read-Write] If enabled, create new PhysicsAsset if one doesn't exist.
- ``distance_field_replacement_mesh`` (StaticMesh):  [Read-Write] If set, replaces the distance field for all imported meshes with the distance field of the specified Static Mesh.
- ``distance_field_resolution_scale`` (float):  [Read-Write] Scale to apply to the mesh when allocating the distance field volume texture.
  The default scale is 1, which assumes that the mesh will be placed unscaled in the world.
- ``dst_lightmap_index`` (int32):  [Read-Write] Specifies the index of the UV channel that will store generated lightmap UVs.
- ``fallback_collision_type`` (InterchangeMeshCollision):  [Read-Write] Type used to generate a collision when no custom collisions are present in the file.
- ``generate_distance_field_as_if_two_sided`` (bool):  [Read-Write] Determines whether to generate the distance field treating every triangle hit as a front face.
  When enabled, prevents the distance field from being discarded due to the mesh being open, but also lowers distance field ambient occlusion quality.
- ``generate_lightmap_u_vs`` (bool):  [Read-Write] If enabled, generates lightmap UVs for each static mesh.
- ``import_collision`` (bool):  [Read-Write]
  deprecated: Use Collision instead.
- ``import_collision_according_to_mesh_name`` (bool):  [Read-Write] If enabled, meshes with certain prefixes will be imported as collision primitives for the mesh with the corresponding unprefixed name.

  Supported prefixes are:
  UBX_ Box collision
  UCP_ Capsule collision
  USP_ Sphere collision
  UCX_ Convex collision
- ``import_morph_targets`` (bool):  [Read-Write] If enabled, imports all morph target shapes found in the source.
- ``import_skeletal_meshes`` (bool):  [Read-Write] If enabled, imports all skeletal mesh assets found in the sources.
- ``import_static_meshes`` (bool):  [Read-Write] If enabled, imports all static mesh assets found in the sources.
- ``import_vertex_attributes`` (bool):  [Read-Write] If enabled, creates named vertex attributes for secondary vertex color data.
- ``lod_group`` (Name):  [Read-Write] The LOD group that will be assigned to this mesh.
- ``lod_screen_sizes`` (Array[float]):  [Read-Write] This setting is only used if the Auto Compute LOD Screen Sizes setting is disabled.
- ``max_lumen_mesh_cards`` (int32):  [Read-Write] The maximum number of Lumen mesh cards to generate for this mesh.
  More cards means that the surface will have better coverage, but will result in increased runtime overhead.
  Set this to 0 to disable mesh card generation for this mesh.
  The default is 12.
- ``merge_morph_targets_with_same_name`` (bool):  [Read-Write] If enabled, all morph target shapes with the same name will be merge together. Turn it to false if you want to control those morph with different values.
- ``min_lightmap_resolution`` (int32):  [Read-Write] When generating lightmaps, determines the amount of padding used to pack UVs. Set this value to the lowest-resolution lightmap you expect to use with the imported meshes.
- ``morph_threshold_position`` (float):  [Read-Write] Threshold to compare vertex position equality when computing morph target deltas.
- ``one_convex_hull_per_ucx`` (bool):  [Read-Write] If enabled, each UCX collision mesh will be imported as a single convex hull. If disabled, a UCX mesh will be decomposed into its separate pieces and a convex hull generated for each.
- ``physics_asset`` (PhysicsAsset):  [Read-Write] If set, use the specified PhysicsAsset. If not set and the Create Physics Asset setting is not enabled, the importer will not generate or set any physics asset.
- ``skeletal_mesh_import_content_type`` (InterchangeSkeletalMeshContentType):  [Read-Write] Determines what types of information are imported for skeletal meshes.
- ``src_lightmap_index`` (int32):  [Read-Write] Specifies the index of the UV channel that will be used as the source when generating lightmaps.
- ``support_face_remap`` (bool):  [Read-Write] If enabled, imported static meshes are set up for use with physical material masks.
- ``threshold_position`` (float):  [Read-Write] Threshold value that is used to decide whether two vertex positions are equal.
- ``threshold_tangent_normal`` (float):  [Read-Write] Threshold value that is used to decide whether two normals, tangents, or bi-normals are equal.
- ``threshold_uv`` (float):  [Read-Write] Threshold value that is used to decide whether two UVs are equal.
- ``update_skeleton_reference_pose`` (bool):  [Read-Write] Enable this option to update the reference pose of the Skeleton (of the mesh). The reference pose of the mesh is always updated.
- ``use_high_precision_skin_weights`` (bool):  [Read-Write] If enabled, imported skin weights use 16 bits instead of 8 bits.

<a id="unreal.InterchangeGenericMeshPipeline.import_static_meshes"></a>

#### import_static_meshes

```python
@property
def import_static_meshes() -> bool
```

(bool):  [Read-Write] If enabled, imports all static mesh assets found in the sources.

<a id="unreal.InterchangeGenericMeshPipeline.import_static_meshes"></a>

#### import_static_meshes

```python
@import_static_meshes.setter
def import_static_meshes(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.combine_static_meshes"></a>

#### combine_static_meshes

```python
@property
def combine_static_meshes() -> bool
```

(bool):  [Read-Write] If enabled, all translated static mesh nodes will be imported as a single static mesh.

<a id="unreal.InterchangeGenericMeshPipeline.combine_static_meshes"></a>

#### combine_static_meshes

```python
@combine_static_meshes.setter
def combine_static_meshes(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.lod_group"></a>

#### lod_group

```python
@property
def lod_group() -> Name
```

(Name):  [Read-Write] The LOD group that will be assigned to this mesh.

<a id="unreal.InterchangeGenericMeshPipeline.lod_group"></a>

#### lod_group

```python
@lod_group.setter
def lod_group(value: Name) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.auto_compute_lod_screen_sizes"></a>

#### auto_compute_lod_screen_sizes

```python
@property
def auto_compute_lod_screen_sizes() -> bool
```

(bool):  [Read-Write] If enabled, LOD Screen Sizes would be auto-computed.

<a id="unreal.InterchangeGenericMeshPipeline.auto_compute_lod_screen_sizes"></a>

#### auto_compute_lod_screen_sizes

```python
@auto_compute_lod_screen_sizes.setter
def auto_compute_lod_screen_sizes(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.lod_screen_sizes"></a>

#### lod_screen_sizes

```python
@property
def lod_screen_sizes() -> Array[float]
```

(Array[float]):  [Read-Write] This setting is only used if the Auto Compute LOD Screen Sizes setting is disabled.

<a id="unreal.InterchangeGenericMeshPipeline.lod_screen_sizes"></a>

#### lod_screen_sizes

```python
@lod_screen_sizes.setter
def lod_screen_sizes(value: Array[float]) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.import_collision"></a>

#### import_collision

```python
@property
def import_collision() -> bool
```

(bool):  [Read-Write]
deprecated: Use Collision instead.

<a id="unreal.InterchangeGenericMeshPipeline.import_collision"></a>

#### import_collision

```python
@import_collision.setter
def import_collision(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.collision"></a>

#### collision

```python
@property
def collision() -> bool
```

(bool):  [Read-Write] If enabled, custom collision will be imported. If enabled and there is no custom collision, a generic collision will be automatically generated.
If disabled, no collision will be created or imported.

<a id="unreal.InterchangeGenericMeshPipeline.collision"></a>

#### collision

```python
@collision.setter
def collision(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.import_collision_according_to_mesh_name"></a>

#### import_collision_according_to_mesh_name

```python
@property
def import_collision_according_to_mesh_name() -> bool
```

(bool):  [Read-Write] If enabled, meshes with certain prefixes will be imported as collision primitives for the mesh with the corresponding unprefixed name.

Supported prefixes are:
UBX_ Box collision
UCP_ Capsule collision
USP_ Sphere collision
UCX_ Convex collision

<a id="unreal.InterchangeGenericMeshPipeline.import_collision_according_to_mesh_name"></a>

#### import_collision_according_to_mesh_name

```python
@import_collision_according_to_mesh_name.setter
def import_collision_according_to_mesh_name(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.one_convex_hull_per_ucx"></a>

#### one_convex_hull_per_ucx

```python
@property
def one_convex_hull_per_ucx() -> bool
```

(bool):  [Read-Write] If enabled, each UCX collision mesh will be imported as a single convex hull. If disabled, a UCX mesh will be decomposed into its separate pieces and a convex hull generated for each.

<a id="unreal.InterchangeGenericMeshPipeline.one_convex_hull_per_ucx"></a>

#### one_convex_hull_per_ucx

```python
@one_convex_hull_per_ucx.setter
def one_convex_hull_per_ucx(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.fallback_collision_type"></a>

#### fallback_collision_type

```python
@property
def fallback_collision_type() -> InterchangeMeshCollision
```

(InterchangeMeshCollision):  [Read-Write] Type used to generate a collision when no custom collisions are present in the file.

<a id="unreal.InterchangeGenericMeshPipeline.fallback_collision_type"></a>

#### fallback_collision_type

```python
@fallback_collision_type.setter
def fallback_collision_type(value: InterchangeMeshCollision) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.build_nanite"></a>

#### build_nanite

```python
@property
def build_nanite() -> bool
```

(bool):  [Read-Write] If enabled, imported meshes will be rendered by Nanite at runtime. Make sure your meshes and materials meet the requirements for Nanite.

<a id="unreal.InterchangeGenericMeshPipeline.build_nanite"></a>

#### build_nanite

```python
@build_nanite.setter
def build_nanite(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.build_reversed_index_buffer"></a>

#### build_reversed_index_buffer

```python
@property
def build_reversed_index_buffer() -> bool
```

(bool):  [Read-Write] If enabled, builds a reversed index buffer for each static mesh.

<a id="unreal.InterchangeGenericMeshPipeline.build_reversed_index_buffer"></a>

#### build_reversed_index_buffer

```python
@build_reversed_index_buffer.setter
def build_reversed_index_buffer(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@property
def generate_lightmap_u_vs() -> bool
```

(bool):  [Read-Write] If enabled, generates lightmap UVs for each static mesh.

<a id="unreal.InterchangeGenericMeshPipeline.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@generate_lightmap_u_vs.setter
def generate_lightmap_u_vs(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.generate_distance_field_as_if_two_sided"></a>

#### generate_distance_field_as_if_two_sided

```python
@property
def generate_distance_field_as_if_two_sided() -> bool
```

(bool):  [Read-Write] Determines whether to generate the distance field treating every triangle hit as a front face.
When enabled, prevents the distance field from being discarded due to the mesh being open, but also lowers distance field ambient occlusion quality.

<a id="unreal.InterchangeGenericMeshPipeline.generate_distance_field_as_if_two_sided"></a>

#### generate_distance_field_as_if_two_sided

```python
@generate_distance_field_as_if_two_sided.setter
def generate_distance_field_as_if_two_sided(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.support_face_remap"></a>

#### support_face_remap

```python
@property
def support_face_remap() -> bool
```

(bool):  [Read-Write] If enabled, imported static meshes are set up for use with physical material masks.

<a id="unreal.InterchangeGenericMeshPipeline.support_face_remap"></a>

#### support_face_remap

```python
@support_face_remap.setter
def support_face_remap(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.min_lightmap_resolution"></a>

#### min_lightmap_resolution

```python
@property
def min_lightmap_resolution() -> int
```

(int32):  [Read-Write] When generating lightmaps, determines the amount of padding used to pack UVs. Set this value to the lowest-resolution lightmap you expect to use with the imported meshes.

<a id="unreal.InterchangeGenericMeshPipeline.min_lightmap_resolution"></a>

#### min_lightmap_resolution

```python
@min_lightmap_resolution.setter
def min_lightmap_resolution(value: int) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.src_lightmap_index"></a>

#### src_lightmap_index

```python
@property
def src_lightmap_index() -> int
```

(int32):  [Read-Write] Specifies the index of the UV channel that will be used as the source when generating lightmaps.

<a id="unreal.InterchangeGenericMeshPipeline.src_lightmap_index"></a>

#### src_lightmap_index

```python
@src_lightmap_index.setter
def src_lightmap_index(value: int) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.dst_lightmap_index"></a>

#### dst_lightmap_index

```python
@property
def dst_lightmap_index() -> int
```

(int32):  [Read-Write] Specifies the index of the UV channel that will store generated lightmap UVs.

<a id="unreal.InterchangeGenericMeshPipeline.dst_lightmap_index"></a>

#### dst_lightmap_index

```python
@dst_lightmap_index.setter
def dst_lightmap_index(value: int) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.build_scale3d"></a>

#### build_scale3d

```python
@property
def build_scale3d() -> Vector
```

(Vector):  [Read-Write] The local scale applied when building the mesh.

<a id="unreal.InterchangeGenericMeshPipeline.build_scale3d"></a>

#### build_scale3d

```python
@build_scale3d.setter
def build_scale3d(value: Vector) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.distance_field_resolution_scale"></a>

#### distance_field_resolution_scale

```python
@property
def distance_field_resolution_scale() -> float
```

(float):  [Read-Write] Scale to apply to the mesh when allocating the distance field volume texture.
The default scale is 1, which assumes that the mesh will be placed unscaled in the world.

<a id="unreal.InterchangeGenericMeshPipeline.distance_field_resolution_scale"></a>

#### distance_field_resolution_scale

```python
@distance_field_resolution_scale.setter
def distance_field_resolution_scale(value: float) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.distance_field_replacement_mesh"></a>

#### distance_field_replacement_mesh

```python
@property
def distance_field_replacement_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write] If set, replaces the distance field for all imported meshes with the distance field of the specified Static Mesh.

<a id="unreal.InterchangeGenericMeshPipeline.distance_field_replacement_mesh"></a>

#### distance_field_replacement_mesh

```python
@distance_field_replacement_mesh.setter
def distance_field_replacement_mesh(value: StaticMesh) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.max_lumen_mesh_cards"></a>

#### max_lumen_mesh_cards

```python
@property
def max_lumen_mesh_cards() -> int
```

(int32):  [Read-Write] The maximum number of Lumen mesh cards to generate for this mesh.
More cards means that the surface will have better coverage, but will result in increased runtime overhead.
Set this to 0 to disable mesh card generation for this mesh.
The default is 12.

<a id="unreal.InterchangeGenericMeshPipeline.max_lumen_mesh_cards"></a>

#### max_lumen_mesh_cards

```python
@max_lumen_mesh_cards.setter
def max_lumen_mesh_cards(value: int) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.import_skeletal_meshes"></a>

#### import_skeletal_meshes

```python
@property
def import_skeletal_meshes() -> bool
```

(bool):  [Read-Write] If enabled, imports all skeletal mesh assets found in the sources.

<a id="unreal.InterchangeGenericMeshPipeline.import_skeletal_meshes"></a>

#### import_skeletal_meshes

```python
@import_skeletal_meshes.setter
def import_skeletal_meshes(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.skeletal_mesh_import_content_type"></a>

#### skeletal_mesh_import_content_type

```python
@property
def skeletal_mesh_import_content_type() -> InterchangeSkeletalMeshContentType
```

(InterchangeSkeletalMeshContentType):  [Read-Write] Determines what types of information are imported for skeletal meshes.

<a id="unreal.InterchangeGenericMeshPipeline.skeletal_mesh_import_content_type"></a>

#### skeletal_mesh_import_content_type

```python
@skeletal_mesh_import_content_type.setter
def skeletal_mesh_import_content_type(
        value: InterchangeSkeletalMeshContentType) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.combine_skeletal_meshes"></a>

#### combine_skeletal_meshes

```python
@property
def combine_skeletal_meshes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.InterchangeGenericMeshPipeline.combine_skeletal_meshes"></a>

#### combine_skeletal_meshes

```python
@combine_skeletal_meshes.setter
def combine_skeletal_meshes(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.import_morph_targets"></a>

#### import_morph_targets

```python
@property
def import_morph_targets() -> bool
```

(bool):  [Read-Write] If enabled, imports all morph target shapes found in the source.

<a id="unreal.InterchangeGenericMeshPipeline.import_morph_targets"></a>

#### import_morph_targets

```python
@import_morph_targets.setter
def import_morph_targets(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.merge_morph_targets_with_same_name"></a>

#### merge_morph_targets_with_same_name

```python
@property
def merge_morph_targets_with_same_name() -> bool
```

(bool):  [Read-Write] If enabled, all morph target shapes with the same name will be merge together. Turn it to false if you want to control those morph with different values.

<a id="unreal.InterchangeGenericMeshPipeline.merge_morph_targets_with_same_name"></a>

#### merge_morph_targets_with_same_name

```python
@merge_morph_targets_with_same_name.setter
def merge_morph_targets_with_same_name(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.import_vertex_attributes"></a>

#### import_vertex_attributes

```python
@property
def import_vertex_attributes() -> bool
```

(bool):  [Read-Write] If enabled, creates named vertex attributes for secondary vertex color data.

<a id="unreal.InterchangeGenericMeshPipeline.import_vertex_attributes"></a>

#### import_vertex_attributes

```python
@import_vertex_attributes.setter
def import_vertex_attributes(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.update_skeleton_reference_pose"></a>

#### update_skeleton_reference_pose

```python
@property
def update_skeleton_reference_pose() -> bool
```

(bool):  [Read-Write] Enable this option to update the reference pose of the Skeleton (of the mesh). The reference pose of the mesh is always updated.

<a id="unreal.InterchangeGenericMeshPipeline.update_skeleton_reference_pose"></a>

#### update_skeleton_reference_pose

```python
@update_skeleton_reference_pose.setter
def update_skeleton_reference_pose(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.create_physics_asset"></a>

#### create_physics_asset

```python
@property
def create_physics_asset() -> bool
```

(bool):  [Read-Write] If enabled, create new PhysicsAsset if one doesn't exist.

<a id="unreal.InterchangeGenericMeshPipeline.create_physics_asset"></a>

#### create_physics_asset

```python
@create_physics_asset.setter
def create_physics_asset(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.physics_asset"></a>

#### physics_asset

```python
@property
def physics_asset() -> PhysicsAsset
```

(PhysicsAsset):  [Read-Write] If set, use the specified PhysicsAsset. If not set and the Create Physics Asset setting is not enabled, the importer will not generate or set any physics asset.

<a id="unreal.InterchangeGenericMeshPipeline.physics_asset"></a>

#### physics_asset

```python
@physics_asset.setter
def physics_asset(value: PhysicsAsset) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.use_high_precision_skin_weights"></a>

#### use_high_precision_skin_weights

```python
@property
def use_high_precision_skin_weights() -> bool
```

(bool):  [Read-Write] If enabled, imported skin weights use 16 bits instead of 8 bits.

<a id="unreal.InterchangeGenericMeshPipeline.use_high_precision_skin_weights"></a>

#### use_high_precision_skin_weights

```python
@use_high_precision_skin_weights.setter
def use_high_precision_skin_weights(value: bool) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.threshold_position"></a>

#### threshold_position

```python
@property
def threshold_position() -> float
```

(float):  [Read-Write] Threshold value that is used to decide whether two vertex positions are equal.

<a id="unreal.InterchangeGenericMeshPipeline.threshold_position"></a>

#### threshold_position

```python
@threshold_position.setter
def threshold_position(value: float) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.threshold_tangent_normal"></a>

#### threshold_tangent_normal

```python
@property
def threshold_tangent_normal() -> float
```

(float):  [Read-Write] Threshold value that is used to decide whether two normals, tangents, or bi-normals are equal.

<a id="unreal.InterchangeGenericMeshPipeline.threshold_tangent_normal"></a>

#### threshold_tangent_normal

```python
@threshold_tangent_normal.setter
def threshold_tangent_normal(value: float) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.threshold_uv"></a>

#### threshold_uv

```python
@property
def threshold_uv() -> float
```

(float):  [Read-Write] Threshold value that is used to decide whether two UVs are equal.

<a id="unreal.InterchangeGenericMeshPipeline.threshold_uv"></a>

#### threshold_uv

```python
@threshold_uv.setter
def threshold_uv(value: float) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.morph_threshold_position"></a>

#### morph_threshold_position

```python
@property
def morph_threshold_position() -> float
```

(float):  [Read-Write] Threshold to compare vertex position equality when computing morph target deltas.

<a id="unreal.InterchangeGenericMeshPipeline.morph_threshold_position"></a>

#### morph_threshold_position

```python
@morph_threshold_position.setter
def morph_threshold_position(value: float) -> None
```

<a id="unreal.InterchangeGenericMeshPipeline.bone_influence_limit"></a>

#### bone_influence_limit

```python
@property
def bone_influence_limit() -> int
```

(int32):  [Read-Write] The maximum number of bone influences to allow each vertex in this mesh to use.
If set higher than the limit determined by the project settings, it has no effect.
If set to 0, the value is taken from the DefaultBoneInfluenceLimit project setting.

<a id="unreal.InterchangeGenericMeshPipeline.bone_influence_limit"></a>

#### bone_influence_limit

```python
@bone_influence_limit.setter
def bone_influence_limit(value: int) -> None
```

<a id="unreal.InterchangeGenericLevelPipeline"></a>