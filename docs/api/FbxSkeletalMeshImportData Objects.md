## FbxSkeletalMeshImportData Objects

```python
class FbxSkeletalMeshImportData(FbxMeshImportData)
```

Import data and options used when importing a static mesh from fbx
Notes:
- Meta data ImportType i.e.       meta = (ImportType = "SkeletalMesh|GeoOnly")
    - SkeletalMesh : the property will be shown when importing skeletalmesh
    - GeoOnly: The property will be hide if we import skinning only
    - RigOnly: The property will be hide if we import geo only
    - RigAndGeo: The property will be show only if we import both skinning and geometry, it will be hiden otherwise

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxSkeletalMeshImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bake_pivot_in_vertex`` (bool):  [Read-Write] - Experimental - If this option is true the inverse node rotation pivot will be apply to the mesh vertices. The pivot from the DCC will then be the origin of the mesh. Note: "TransformVertexToAbsolute" must be false.
- ``compute_weighted_normals`` (bool):  [Read-Write] Enabling this option will use weighted normals algorithm (area and angle) when computing normals or tangents
- ``convert_scene`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system
- ``convert_scene_unit`` (bool):  [Read-Write] Convert the scene from FBX unit to UE unit (centimeter).
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y
- ``import_content_type`` (FBXImportContentType):  [Read-Write] Filter the content we want to import from the incoming FBX skeletal mesh.
- ``import_mesh_lo_ds`` (bool):  [Read-Write] If enabled, creates LOD models for Unreal meshes from LODs in the import file; If not enabled, only the base mesh from the LOD group is imported
- ``import_meshes_in_bone_hierarchy`` (bool):  [Read-Write] If checked, meshes nested in bone hierarchies will be imported instead of being converted to bones.
- ``import_morph_targets`` (bool):  [Read-Write] If enabled, creates Unreal morph objects for the imported meshes
- ``import_rotation`` (Rotator):  [Read-Write]
- ``import_translation`` (Vector):  [Read-Write]
- ``import_uniform_scale`` (float):  [Read-Write]
- ``import_vertex_attributes`` (bool):  [Read-Write] If enabled, creates a named vertex attribute for each single-channel weight map of the imported mesh.
- ``keep_sections_separate`` (bool):  [Read-Write] If checked, sections with matching materials are kept separate and will not get combined.
- ``morph_threshold_position`` (float):  [Read-Write] Threshold to compare vertex position equality when computing morph target deltas.
- ``normal_generation_method`` (FBXNormalGenerationMethod):  [Read-Write] Use the MikkTSpace tangent space generator for generating normals and tangents on the mesh
- ``normal_import_method`` (FBXNormalImportMethod):  [Read-Write] Enabling this option will read the tangents(tangent,binormal,normal) from FBX file instead of generating them automatically.
- ``preserve_smoothing_groups`` (bool):  [Read-Write] If checked, triangles with non-matching smoothing groups will be physically split.
- ``reorder_material_to_fbx_order`` (bool):  [Read-Write] If checked, The material list will be reorder to the same order has the FBX file.
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.
- ``threshold_position`` (float):  [Read-Write] Threshold to compare vertex position equality.
- ``threshold_tangent_normal`` (float):  [Read-Write] Threshold to compare normal, tangent or bi-normal equality.
- ``threshold_uv`` (float):  [Read-Write] Threshold to compare UV equality.
- ``transform_vertex_to_absolute`` (bool):  [Read-Write] If this option is true the node absolute transform (transform, offset and pivot) will be apply to the mesh vertices.
- ``update_skeleton_reference_pose`` (bool):  [Read-Write] If enabled, update the Skeleton (of the mesh being imported)'s reference pose.
- ``use_t0_as_ref_pose`` (bool):  [Read-Write] Enable this option to use frame 0 as reference pose
- ``vertex_color_import_option`` (VertexColorImportOption):  [Read-Write] Specify how vertex colors should be imported
- ``vertex_override_color`` (Color):  [Read-Write] Specify override color in the case that VertexColorImportOption is set to Override

<a id="unreal.FbxSkeletalMeshImportData.vertex_color_import_option"></a>

#### vertex_color_import_option

```python
@property
def vertex_color_import_option() -> VertexColorImportOption
```

(VertexColorImportOption):  [Read-Write] Specify how vertex colors should be imported

<a id="unreal.FbxSkeletalMeshImportData.vertex_color_import_option"></a>

#### vertex_color_import_option

```python
@vertex_color_import_option.setter
def vertex_color_import_option(value: VertexColorImportOption) -> None
```

<a id="unreal.FbxSkeletalMeshImportData.vertex_override_color"></a>

#### vertex_override_color

```python
@property
def vertex_override_color() -> Color
```

(Color):  [Read-Write] Specify override color in the case that VertexColorImportOption is set to Override

<a id="unreal.FbxSkeletalMeshImportData.vertex_override_color"></a>

#### vertex_override_color

```python
@vertex_override_color.setter
def vertex_override_color(value: Color) -> None
```

<a id="unreal.FbxStaticMeshImportData"></a>