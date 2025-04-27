## FbxStaticMeshImportData Objects

```python
class FbxStaticMeshImportData(FbxMeshImportData)
```

Fbx Static Mesh Import Data

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxStaticMeshImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_generate_collision`` (bool):  [Read-Write] If checked, collision will automatically be generated (ignored if custom collision is imported or used).
- ``bake_pivot_in_vertex`` (bool):  [Read-Write] - Experimental - If this option is true the inverse node rotation pivot will be apply to the mesh vertices. The pivot from the DCC will then be the origin of the mesh. Note: "TransformVertexToAbsolute" must be false.
- ``build_nanite`` (bool):  [Read-Write] If enabled, allows to render objects with Nanite
- ``build_reversed_index_buffer`` (bool):  [Read-Write]
- ``combine_meshes`` (bool):  [Read-Write] If enabled, combines all meshes into a single mesh
- ``compute_weighted_normals`` (bool):  [Read-Write] Enabling this option will use weighted normals algorithm (area and angle) when computing normals or tangents
- ``convert_scene`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system
- ``convert_scene_unit`` (bool):  [Read-Write] Convert the scene from FBX unit to UE unit (centimeter).
- ``distance_field_resolution_scale`` (float):  [Read-Write] Scale to apply to the mesh when allocating the distance field volume texture.
  The default scale is 1, which is assuming that the mesh will be placed unscaled in the world.
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y
- ``generate_lightmap_u_vs`` (bool):  [Read-Write]
- ``import_mesh_lo_ds`` (bool):  [Read-Write] If enabled, creates LOD models for Unreal meshes from LODs in the import file; If not enabled, only the base mesh from the LOD group is imported
- ``import_rotation`` (Rotator):  [Read-Write]
- ``import_translation`` (Vector):  [Read-Write]
- ``import_uniform_scale`` (float):  [Read-Write]
- ``normal_generation_method`` (FBXNormalGenerationMethod):  [Read-Write] Use the MikkTSpace tangent space generator for generating normals and tangents on the mesh
- ``normal_import_method`` (FBXNormalImportMethod):  [Read-Write] Enabling this option will read the tangents(tangent,binormal,normal) from FBX file instead of generating them automatically.
- ``one_convex_hull_per_ucx`` (bool):  [Read-Write] If checked, one convex hull per UCX_ prefixed collision mesh will be generated instead of decomposing into multiple hulls
- ``remove_degenerates`` (bool):  [Read-Write] Disabling this option will keep degenerate triangles found.  In general you should leave this option on.
- ``reorder_material_to_fbx_order`` (bool):  [Read-Write] If checked, The material list will be reorder to the same order has the FBX file.
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.
- ``static_mesh_lod_group`` (Name):  [Read-Write] The LODGroup to associate with this mesh when it is imported
- ``transform_vertex_to_absolute`` (bool):  [Read-Write] If this option is true the node absolute transform (transform, offset and pivot) will be apply to the mesh vertices.
- ``vertex_color_import_option`` (VertexColorImportOption):  [Read-Write] Specify how vertex colors should be imported
- ``vertex_override_color`` (Color):  [Read-Write] Specify override color in the case that VertexColorImportOption is set to Override

<a id="unreal.FbxStaticMeshImportData.static_mesh_lod_group"></a>

#### static_mesh_lod_group

```python
@property
def static_mesh_lod_group() -> Name
```

(Name):  [Read-Write] The LODGroup to associate with this mesh when it is imported

<a id="unreal.FbxStaticMeshImportData.static_mesh_lod_group"></a>

#### static_mesh_lod_group

```python
@static_mesh_lod_group.setter
def static_mesh_lod_group(value: Name) -> None
```

<a id="unreal.FbxStaticMeshImportData.vertex_color_import_option"></a>

#### vertex_color_import_option

```python
@property
def vertex_color_import_option() -> VertexColorImportOption
```

(VertexColorImportOption):  [Read-Write] Specify how vertex colors should be imported

<a id="unreal.FbxStaticMeshImportData.vertex_color_import_option"></a>

#### vertex_color_import_option

```python
@vertex_color_import_option.setter
def vertex_color_import_option(value: VertexColorImportOption) -> None
```

<a id="unreal.FbxStaticMeshImportData.vertex_override_color"></a>

#### vertex_override_color

```python
@property
def vertex_override_color() -> Color
```

(Color):  [Read-Write] Specify override color in the case that VertexColorImportOption is set to Override

<a id="unreal.FbxStaticMeshImportData.vertex_override_color"></a>

#### vertex_override_color

```python
@vertex_override_color.setter
def vertex_override_color(value: Color) -> None
```

<a id="unreal.FbxStaticMeshImportData.remove_degenerates"></a>

#### remove_degenerates

```python
@property
def remove_degenerates() -> bool
```

(bool):  [Read-Write] Disabling this option will keep degenerate triangles found.  In general you should leave this option on.

<a id="unreal.FbxStaticMeshImportData.remove_degenerates"></a>

#### remove_degenerates

```python
@remove_degenerates.setter
def remove_degenerates(value: bool) -> None
```

<a id="unreal.FbxStaticMeshImportData.build_reversed_index_buffer"></a>

#### build_reversed_index_buffer

```python
@property
def build_reversed_index_buffer() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FbxStaticMeshImportData.build_reversed_index_buffer"></a>

#### build_reversed_index_buffer

```python
@build_reversed_index_buffer.setter
def build_reversed_index_buffer(value: bool) -> None
```

<a id="unreal.FbxStaticMeshImportData.build_nanite"></a>

#### build_nanite

```python
@property
def build_nanite() -> bool
```

(bool):  [Read-Write] If enabled, allows to render objects with Nanite

<a id="unreal.FbxStaticMeshImportData.build_nanite"></a>

#### build_nanite

```python
@build_nanite.setter
def build_nanite(value: bool) -> None
```

<a id="unreal.FbxStaticMeshImportData.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@property
def generate_lightmap_u_vs() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FbxStaticMeshImportData.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@generate_lightmap_u_vs.setter
def generate_lightmap_u_vs(value: bool) -> None
```

<a id="unreal.FbxStaticMeshImportData.one_convex_hull_per_ucx"></a>

#### one_convex_hull_per_ucx

```python
@property
def one_convex_hull_per_ucx() -> bool
```

(bool):  [Read-Write] If checked, one convex hull per UCX_ prefixed collision mesh will be generated instead of decomposing into multiple hulls

<a id="unreal.FbxStaticMeshImportData.one_convex_hull_per_ucx"></a>

#### one_convex_hull_per_ucx

```python
@one_convex_hull_per_ucx.setter
def one_convex_hull_per_ucx(value: bool) -> None
```

<a id="unreal.FbxStaticMeshImportData.auto_generate_collision"></a>

#### auto_generate_collision

```python
@property
def auto_generate_collision() -> bool
```

(bool):  [Read-Write] If checked, collision will automatically be generated (ignored if custom collision is imported or used).

<a id="unreal.FbxStaticMeshImportData.auto_generate_collision"></a>

#### auto_generate_collision

```python
@auto_generate_collision.setter
def auto_generate_collision(value: bool) -> None
```

<a id="unreal.FbxStaticMeshImportData.combine_meshes"></a>

#### combine_meshes

```python
@property
def combine_meshes() -> bool
```

(bool):  [Read-Write] If enabled, combines all meshes into a single mesh

<a id="unreal.FbxStaticMeshImportData.combine_meshes"></a>

#### combine_meshes

```python
@combine_meshes.setter
def combine_meshes(value: bool) -> None
```

<a id="unreal.FbxStaticMeshImportData.distance_field_resolution_scale"></a>

#### distance_field_resolution_scale

```python
@property
def distance_field_resolution_scale() -> float
```

(float):  [Read-Write] Scale to apply to the mesh when allocating the distance field volume texture.
The default scale is 1, which is assuming that the mesh will be placed unscaled in the world.

<a id="unreal.FbxStaticMeshImportData.distance_field_resolution_scale"></a>

#### distance_field_resolution_scale

```python
@distance_field_resolution_scale.setter
def distance_field_resolution_scale(value: float) -> None
```

<a id="unreal.FbxTextureImportData"></a>