## GeometryScriptCreateNewSkeletalMeshAssetOptions Objects

```python
class GeometryScriptCreateNewSkeletalMeshAssetOptions(StructBase)
```

Geometry Script Create New Skeletal Mesh Asset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingEditor
- **File**: CreateNewAssetUtilityFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_recompute_normals`` (bool):  [Read-Write]
- ``enable_recompute_tangents`` (bool):  [Read-Write]
- ``materials`` (Map[Name, MaterialInterface]):  [Read-Write]
- ``use_mesh_bone_proportions`` (bool):  [Read-Write] If true, will use the skeleton proportions (if availabale) stored in the dynamic mesh.
- ``use_original_vertex_order`` (bool):  [Read-Write] Use the original vertex order found in the source data. This is useful if the inbound mesh was originally non-manifold, and needs to keep
  the non-manifold structure when re-created.

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.__init__"></a>

#### __init__

```python
def __init__(enable_recompute_normals: bool = False,
             enable_recompute_tangents: bool = False,
             materials: Map[Name, MaterialInterface] = {},
             use_mesh_bone_proportions: bool = False,
             use_original_vertex_order: bool = False) -> None
```

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.enable_recompute_normals"></a>

#### enable_recompute_normals

```python
@property
def enable_recompute_normals() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.enable_recompute_normals"></a>

#### enable_recompute_normals

```python
@enable_recompute_normals.setter
def enable_recompute_normals(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.enable_recompute_tangents"></a>

#### enable_recompute_tangents

```python
@property
def enable_recompute_tangents() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.enable_recompute_tangents"></a>

#### enable_recompute_tangents

```python
@enable_recompute_tangents.setter
def enable_recompute_tangents(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.materials"></a>

#### materials

```python
@property
def materials() -> Map[Name, MaterialInterface]
```

(Map[Name, MaterialInterface]):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.materials"></a>

#### materials

```python
@materials.setter
def materials(value: Map[Name, MaterialInterface]) -> None
```

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.use_mesh_bone_proportions"></a>

#### use_mesh_bone_proportions

```python
@property
def use_mesh_bone_proportions() -> bool
```

(bool):  [Read-Write] If true, will use the skeleton proportions (if availabale) stored in the dynamic mesh.

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.use_mesh_bone_proportions"></a>

#### use_mesh_bone_proportions

```python
@use_mesh_bone_proportions.setter
def use_mesh_bone_proportions(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.use_original_vertex_order"></a>

#### use_original_vertex_order

```python
@property
def use_original_vertex_order() -> bool
```

(bool):  [Read-Write] Use the original vertex order found in the source data. This is useful if the inbound mesh was originally non-manifold, and needs to keep
the non-manifold structure when re-created.

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.use_original_vertex_order"></a>

#### use_original_vertex_order

```python
@use_original_vertex_order.setter
def use_original_vertex_order(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewTexture2DAssetOptions"></a>