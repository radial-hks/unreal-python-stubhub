## FbxMeshImportData Objects

```python
class FbxMeshImportData(FbxAssetImportData)
```

Import data and options used when importing any mesh from FBX

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxMeshImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bake_pivot_in_vertex`` (bool):  [Read-Write] - Experimental - If this option is true the inverse node rotation pivot will be apply to the mesh vertices. The pivot from the DCC will then be the origin of the mesh. Note: "TransformVertexToAbsolute" must be false.
- ``compute_weighted_normals`` (bool):  [Read-Write] Enabling this option will use weighted normals algorithm (area and angle) when computing normals or tangents
- ``convert_scene`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system
- ``convert_scene_unit`` (bool):  [Read-Write] Convert the scene from FBX unit to UE unit (centimeter).
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y
- ``import_mesh_lo_ds`` (bool):  [Read-Write] If enabled, creates LOD models for Unreal meshes from LODs in the import file; If not enabled, only the base mesh from the LOD group is imported
- ``import_rotation`` (Rotator):  [Read-Write]
- ``import_translation`` (Vector):  [Read-Write]
- ``import_uniform_scale`` (float):  [Read-Write]
- ``normal_generation_method`` (FBXNormalGenerationMethod):  [Read-Write] Use the MikkTSpace tangent space generator for generating normals and tangents on the mesh
- ``normal_import_method`` (FBXNormalImportMethod):  [Read-Write] Enabling this option will read the tangents(tangent,binormal,normal) from FBX file instead of generating them automatically.
- ``reorder_material_to_fbx_order`` (bool):  [Read-Write] If checked, The material list will be reorder to the same order has the FBX file.
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.
- ``transform_vertex_to_absolute`` (bool):  [Read-Write] If this option is true the node absolute transform (transform, offset and pivot) will be apply to the mesh vertices.

<a id="unreal.FbxMeshImportData.transform_vertex_to_absolute"></a>

#### transform_vertex_to_absolute

```python
@property
def transform_vertex_to_absolute() -> bool
```

(bool):  [Read-Write] If this option is true the node absolute transform (transform, offset and pivot) will be apply to the mesh vertices.

<a id="unreal.FbxMeshImportData.transform_vertex_to_absolute"></a>

#### transform_vertex_to_absolute

```python
@transform_vertex_to_absolute.setter
def transform_vertex_to_absolute(value: bool) -> None
```

<a id="unreal.FbxMeshImportData.bake_pivot_in_vertex"></a>

#### bake_pivot_in_vertex

```python
@property
def bake_pivot_in_vertex() -> bool
```

(bool):  [Read-Write] - Experimental - If this option is true the inverse node rotation pivot will be apply to the mesh vertices. The pivot from the DCC will then be the origin of the mesh. Note: "TransformVertexToAbsolute" must be false.

<a id="unreal.FbxMeshImportData.bake_pivot_in_vertex"></a>

#### bake_pivot_in_vertex

```python
@bake_pivot_in_vertex.setter
def bake_pivot_in_vertex(value: bool) -> None
```

<a id="unreal.FbxMeshImportData.import_mesh_lo_ds"></a>

#### import_mesh_lo_ds

```python
@property
def import_mesh_lo_ds() -> bool
```

(bool):  [Read-Write] If enabled, creates LOD models for Unreal meshes from LODs in the import file; If not enabled, only the base mesh from the LOD group is imported

<a id="unreal.FbxMeshImportData.import_mesh_lo_ds"></a>

#### import_mesh_lo_ds

```python
@import_mesh_lo_ds.setter
def import_mesh_lo_ds(value: bool) -> None
```

<a id="unreal.FbxMeshImportData.normal_import_method"></a>

#### normal_import_method

```python
@property
def normal_import_method() -> FBXNormalImportMethod
```

(FBXNormalImportMethod):  [Read-Write] Enabling this option will read the tangents(tangent,binormal,normal) from FBX file instead of generating them automatically.

<a id="unreal.FbxMeshImportData.normal_import_method"></a>

#### normal_import_method

```python
@normal_import_method.setter
def normal_import_method(value: FBXNormalImportMethod) -> None
```

<a id="unreal.FbxMeshImportData.normal_generation_method"></a>

#### normal_generation_method

```python
@property
def normal_generation_method() -> FBXNormalGenerationMethod
```

(FBXNormalGenerationMethod):  [Read-Write] Use the MikkTSpace tangent space generator for generating normals and tangents on the mesh

<a id="unreal.FbxMeshImportData.normal_generation_method"></a>

#### normal_generation_method

```python
@normal_generation_method.setter
def normal_generation_method(value: FBXNormalGenerationMethod) -> None
```

<a id="unreal.FbxMeshImportData.compute_weighted_normals"></a>

#### compute_weighted_normals

```python
@property
def compute_weighted_normals() -> bool
```

(bool):  [Read-Write] Enabling this option will use weighted normals algorithm (area and angle) when computing normals or tangents

<a id="unreal.FbxMeshImportData.compute_weighted_normals"></a>

#### compute_weighted_normals

```python
@compute_weighted_normals.setter
def compute_weighted_normals(value: bool) -> None
```

<a id="unreal.FbxMeshImportData.reorder_material_to_fbx_order"></a>

#### reorder_material_to_fbx_order

```python
@property
def reorder_material_to_fbx_order() -> bool
```

(bool):  [Read-Write] If checked, The material list will be reorder to the same order has the FBX file.

<a id="unreal.FbxMeshImportData.reorder_material_to_fbx_order"></a>

#### reorder_material_to_fbx_order

```python
@reorder_material_to_fbx_order.setter
def reorder_material_to_fbx_order(value: bool) -> None
```

<a id="unreal.SceneImportFactory"></a>