## GeometryScript_MeshDecomposition Objects

```python
class GeometryScript_MeshDecomposition(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Decomposition Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDecompositionFunctions.h

<a id="unreal.GeometryScript_MeshDecomposition.split_mesh_by_polygroups"></a>

#### split_mesh_by_polygroups

```python
@classmethod
def split_mesh_by_polygroups(
    cls,
    target_mesh: DynamicMesh,
    group_layer: GeometryScriptGroupLayer,
    mesh_pool: DynamicMeshPool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[DynamicMesh], Array[int]]
```

X.split_mesh_by_polygroups(target_mesh, group_layer, mesh_pool, debug=None) -> (DynamicMesh, component_meshes=Array[DynamicMesh], component_polygroups=Array[int32])
Create a new Mesh for each Polygroup of TargetMesh. Note that this may be a *large* number of meshes!
New meshes are drawn from MeshPool if it is provided, otherwise new UDynamicMesh instances are allocated

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    mesh_pool (DynamicMeshPool): New meshes in ComponentMeshes output list are allocated from this pool if it is provided (highly recommended!!)
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    component_meshes (Array[DynamicMesh]): New List of meshes is returned here

    component_polygroups (Array[int32]): Original Polygroup for each Mesh in ComponentMeshes is returned here

<a id="unreal.GeometryScript_MeshDecomposition.split_mesh_by_material_i_ds"></a>

#### split_mesh_by_material_i_ds

```python
@classmethod
def split_mesh_by_material_i_ds(
    cls,
    target_mesh: DynamicMesh,
    mesh_pool: DynamicMeshPool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[DynamicMesh], Array[int]]
```

X.split_mesh_by_material_i_ds(target_mesh, mesh_pool, debug=None) -> (DynamicMesh, component_meshes=Array[DynamicMesh], component_material_i_ds=Array[int32])
Create a new Mesh for each MaterialID of TargetMesh.
New meshes are drawn from MeshPool if it is provided, otherwise new UDynamicMesh instances are allocated

Args:
    target_mesh (DynamicMesh): 
    mesh_pool (DynamicMeshPool): New meshes in ComponentMeshes output list are allocated from this pool if it is provided (highly recommended!!)
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    component_meshes (Array[DynamicMesh]): New List of meshes is returned here

    component_material_i_ds (Array[int32]): MaterialID for each Mesh in ComponentMeshes is returned here

<a id="unreal.GeometryScript_MeshDecomposition.split_mesh_by_components"></a>

#### split_mesh_by_components

```python
@classmethod
def split_mesh_by_components(
    cls,
    target_mesh: DynamicMesh,
    mesh_pool: DynamicMeshPool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[DynamicMesh]]
```

X.split_mesh_by_components(target_mesh, mesh_pool, debug=None) -> (DynamicMesh, component_meshes=Array[DynamicMesh])
Create a new Mesh for each Connected Component of TargetMesh.
New meshes are drawn from MeshPool if it is provided, otherwise new UDynamicMesh instances are allocated

Args:
    target_mesh (DynamicMesh): 
    mesh_pool (DynamicMeshPool): New meshes in ComponentMeshes output list are allocated from this pool if it is provided (highly recommended!!)
    debug (GeometryScriptDebug): 

Returns:
    Array[DynamicMesh]: 

    component_meshes (Array[DynamicMesh]): New List of meshes is returned here

<a id="unreal.GeometryScript_MeshDecomposition.get_sub_mesh_from_mesh"></a>

#### get_sub_mesh_from_mesh

```python
@classmethod
def get_sub_mesh_from_mesh(
    cls,
    target_mesh: DynamicMesh,
    store_to_submesh: DynamicMesh,
    triangle_list: GeometryScriptIndexList,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

X.get_sub_mesh_from_mesh(target_mesh, store_to_submesh, triangle_list, debug=None) -> (DynamicMesh, store_to_submesh=DynamicMesh, store_to_submesh_out=DynamicMesh)
CopyMeshSelectionToMesh should be used instead of this function

Args:
    target_mesh (DynamicMesh): 
    store_to_submesh (DynamicMesh): 
    triangle_list (GeometryScriptIndexList): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    store_to_submesh (DynamicMesh): 

    store_to_submesh_out (DynamicMesh):

<a id="unreal.GeometryScript_MeshDecomposition.copy_mesh_to_mesh"></a>

#### copy_mesh_to_mesh

```python
@classmethod
def copy_mesh_to_mesh(
    cls,
    copy_from_mesh: DynamicMesh,
    copy_to_mesh: DynamicMesh,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

X.copy_mesh_to_mesh(copy_from_mesh, copy_to_mesh, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh)
Set CopyToMesh to be the same mesh as CopyFromMesh

Args:
    copy_from_mesh (DynamicMesh): 
    copy_to_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): 

    copy_to_mesh_out (DynamicMesh):

<a id="unreal.GeometryScript_MeshDecomposition.copy_mesh_selection_to_mesh"></a>

#### copy_mesh_selection_to_mesh

```python
@classmethod
def copy_mesh_selection_to_mesh(
    cls,
    target_mesh: DynamicMesh,
    store_to_submesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    append_to_existing: bool = False,
    preserve_group_i_ds: bool = False,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

X.copy_mesh_selection_to_mesh(target_mesh, store_to_submesh, selection, append_to_existing=False, preserve_group_i_ds=False, debug=None) -> (DynamicMesh, store_to_submesh=DynamicMesh, store_to_submesh_out=DynamicMesh)
Extract the triangles identified by Selection from TargetMesh and copy/add them to StoreToSubmesh

Args:
    target_mesh (DynamicMesh): 
    store_to_submesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    append_to_existing (bool): if false (default), StoreToSubmesh is cleared, otherwise selected triangles are appended
    preserve_group_i_ds (bool): if true, GroupIDs of triangles on TargetMesh are preserved in StoreToSubmesh. Otherwise new GroupIDs are allocated.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    store_to_submesh (DynamicMesh): 

    store_to_submesh_out (DynamicMesh):

<a id="unreal.GeometryScript_MeshDeformers"></a>