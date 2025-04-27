## GeometryScript_MeshEdits Objects

```python
class GeometryScript_MeshEdits(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Basic Edit Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBasicEditFunctions.h

<a id="unreal.GeometryScript_MeshEdits.set_vertex_position"></a>

#### set_vertex_position

```python
@classmethod
def set_vertex_position(
        cls,
        target_mesh: DynamicMesh,
        vertex_id: int,
        new_position: Vector,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.set_vertex_position(target_mesh, vertex_id, new_position, defer_change_notifications=False) -> (DynamicMesh, is_valid_vertex=bool)
Set Vertex Position

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): 
    new_position (Vector): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_vertex (bool):

<a id="unreal.GeometryScript_MeshEdits.set_all_mesh_vertex_positions"></a>

#### set_all_mesh_vertex_positions

```python
@classmethod
def set_all_mesh_vertex_positions(
        cls,
        target_mesh: DynamicMesh,
        position_list: GeometryScriptVectorList,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_all_mesh_vertex_positions(target_mesh, position_list, debug=None) -> DynamicMesh
Set all vertex positions in the TargetMesh to the specified Positions.

Args:
    target_mesh (DynamicMesh): 
    position_list (GeometryScriptVectorList): new vertex Positions. Size must be less than or equal to the MaxVertexID of TargetMesh  (ie gaps are supported).
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshEdits.discard_mesh_attributes"></a>

#### discard_mesh_attributes

```python
@classmethod
def discard_mesh_attributes(
        cls,
        target_mesh: DynamicMesh,
        defer_change_notifications: bool = False) -> DynamicMesh
```

X.discard_mesh_attributes(target_mesh, defer_change_notifications=False) -> DynamicMesh
Discard Mesh Attributes

Args:
    target_mesh (DynamicMesh): 
    defer_change_notifications (bool): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshEdits.delete_vertices_from_mesh"></a>

#### delete_vertices_from_mesh

```python
@classmethod
def delete_vertices_from_mesh(
        cls,
        target_mesh: DynamicMesh,
        vertex_list: GeometryScriptIndexList,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

X.delete_vertices_from_mesh(target_mesh, vertex_list, defer_change_notifications=False) -> (DynamicMesh, num_deleted=int32)
Removes a list of vertices from the mesh.
On return, NumDeleted will contain the actual number of vertices removed.

Args:
    target_mesh (DynamicMesh): 
    vertex_list (GeometryScriptIndexList): 
    defer_change_notifications (bool): 

Returns:
    int32: 

    num_deleted (int32):

<a id="unreal.GeometryScript_MeshEdits.delete_vertex_from_mesh"></a>

#### delete_vertex_from_mesh

```python
@classmethod
def delete_vertex_from_mesh(
        cls,
        target_mesh: DynamicMesh,
        vertex_id: int,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.delete_vertex_from_mesh(target_mesh, vertex_id, defer_change_notifications=False) -> (DynamicMesh, was_vertex_deleted=bool)
Removes a vertex from the mesh as indicated by the VertexID.
Should the delete fail, e.g. if the specified vertex was not a mesh element, the flag bWasVertexDeleted will be set to false.

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    was_vertex_deleted (bool):

<a id="unreal.GeometryScript_MeshEdits.delete_triangles_from_mesh"></a>

#### delete_triangles_from_mesh

```python
@classmethod
def delete_triangles_from_mesh(
        cls,
        target_mesh: DynamicMesh,
        triangle_list: GeometryScriptIndexList,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

X.delete_triangles_from_mesh(target_mesh, triangle_list, defer_change_notifications=False) -> (DynamicMesh, num_deleted=int32)
Removes a list of triangles from the mesh.
On return, NumDeleted will contain the actual number of triangles removed.

Args:
    target_mesh (DynamicMesh): 
    triangle_list (GeometryScriptIndexList): 
    defer_change_notifications (bool): 

Returns:
    int32: 

    num_deleted (int32):

<a id="unreal.GeometryScript_MeshEdits.delete_triangle_from_mesh"></a>

#### delete_triangle_from_mesh

```python
@classmethod
def delete_triangle_from_mesh(
        cls,
        target_mesh: DynamicMesh,
        triangle_id: int,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.delete_triangle_from_mesh(target_mesh, triangle_id, defer_change_notifications=False) -> (DynamicMesh, was_triangle_deleted=bool)
Removes a triangle from the mesh as indicated by the Triangle ID.
Should the delete fail, e.g. if the specified triangle was not a mesh element, the flag bWasTriangleDelete will be set to false.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    was_triangle_deleted (bool):

<a id="unreal.GeometryScript_MeshEdits.delete_selected_triangles_from_mesh"></a>

#### delete_selected_triangles_from_mesh

```python
@classmethod
def delete_selected_triangles_from_mesh(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

X.delete_selected_triangles_from_mesh(target_mesh, selection, defer_change_notifications=False) -> (DynamicMesh, num_deleted=int32)
Removes specified triangles, identified by mesh selection, from the mesh.
On return, NumDeleted will contain the actual number of triangles removed.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    defer_change_notifications (bool): 

Returns:
    int32: 

    num_deleted (int32):

<a id="unreal.GeometryScript_MeshEdits.append_mesh_with_materials"></a>

#### append_mesh_with_materials

```python
@classmethod
def append_mesh_with_materials(
    cls,
    target_mesh: DynamicMesh,
    target_mesh_material_list: Array[MaterialInterface],
    append_mesh: DynamicMesh,
    append_mesh_material_list: Array[MaterialInterface],
    append_transform: Transform,
    defer_change_notifications: bool = False,
    append_options: GeometryScriptAppendMeshOptions = [
        GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING
    ],
    compact_appended_materials: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[MaterialInterface]]
```

X.append_mesh_with_materials(target_mesh, target_mesh_material_list, append_mesh, append_mesh_material_list, append_transform, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials=True, debug=None) -> (DynamicMesh, result_mesh_material_list=Array[MaterialInterface])
Apply Append Transform to Append Mesh and then add its geometry to the Target Mesh.
Also combines materials lists of the Target and Append meshes, and updates the output mesh materials to reference the combined list.

Args:
    target_mesh (DynamicMesh): 
    target_mesh_material_list (Array[MaterialInterface]): 
    append_mesh (DynamicMesh): 
    append_mesh_material_list (Array[MaterialInterface]): 
    append_transform (Transform): 
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another.
    compact_appended_materials (bool): 
    debug (GeometryScriptDebug): 

Returns:
    Array[MaterialInterface]: 

    result_mesh_material_list (Array[MaterialInterface]):

<a id="unreal.GeometryScript_MeshEdits.append_mesh_transformed_with_materials"></a>

#### append_mesh_transformed_with_materials

```python
@classmethod
def append_mesh_transformed_with_materials(
    cls,
    target_mesh: DynamicMesh,
    target_mesh_material_list: Array[MaterialInterface],
    append_mesh: DynamicMesh,
    append_mesh_material_list: Array[MaterialInterface],
    append_transforms: Array[Transform],
    constant_transform: Transform,
    constant_transform_is_relative: bool = True,
    defer_change_notifications: bool = False,
    append_options: GeometryScriptAppendMeshOptions = [
        GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING
    ],
    compact_appended_materials: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[MaterialInterface]]
```

X.append_mesh_transformed_with_materials(target_mesh, target_mesh_material_list, append_mesh, append_mesh_material_list, append_transforms, constant_transform, constant_transform_is_relative=True, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials=True, debug=None) -> (DynamicMesh, result_mesh_material_list=Array[MaterialInterface])
For each transform in AppendTransforms, apply the transform to AppendMesh and then add its geometry to the TargetMesh.
Also combines materials lists of the Target and Append meshes, and updates the output mesh materials to reference the combined list.

Args:
    target_mesh (DynamicMesh): 
    target_mesh_material_list (Array[MaterialInterface]): 
    append_mesh (DynamicMesh): 
    append_mesh_material_list (Array[MaterialInterface]): 
    append_transforms (Array[Transform]): 
    constant_transform (Transform): the Constant transform will be applied after each Append transform
    constant_transform_is_relative (bool): if true, the Constant transform is applied "in the frame" of the Append Transform, otherwise it is applied as a second transform in local coordinates (ie rotate around the AppendTransform X axis, vs around the local X axis)
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another
    compact_appended_materials (bool): 
    debug (GeometryScriptDebug): 

Returns:
    Array[MaterialInterface]: 

    result_mesh_material_list (Array[MaterialInterface]):

<a id="unreal.GeometryScript_MeshEdits.append_mesh_transformed"></a>

#### append_mesh_transformed

```python
@classmethod
def append_mesh_transformed(
        cls,
        target_mesh: DynamicMesh,
        append_mesh: DynamicMesh,
        append_transforms: Array[Transform],
        constant_transform: Transform,
        constant_transform_is_relative: bool = True,
        defer_change_notifications: bool = False,
        append_options: GeometryScriptAppendMeshOptions = [
            GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING
        ],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_mesh_transformed(target_mesh, append_mesh, append_transforms, constant_transform, constant_transform_is_relative=True, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug=None) -> DynamicMesh
For each transform in AppendTransforms, apply the transform to AppendMesh and then add its geometry to the TargetMesh.

Args:
    target_mesh (DynamicMesh): 
    append_mesh (DynamicMesh): 
    append_transforms (Array[Transform]): 
    constant_transform (Transform): the Constant transform will be applied after each Append transform
    constant_transform_is_relative (bool): if true, the Constant transform is applied "in the frame" of the Append Transform, otherwise it is applied as a second transform in local coordinates (ie rotate around the AppendTransform X axis, vs around the local X axis)
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshEdits.append_mesh_repeated_with_materials"></a>

#### append_mesh_repeated_with_materials

```python
@classmethod
def append_mesh_repeated_with_materials(
    cls,
    target_mesh: DynamicMesh,
    target_mesh_material_list: Array[MaterialInterface],
    append_mesh: DynamicMesh,
    append_mesh_material_list: Array[MaterialInterface],
    append_transform: Transform,
    repeat_count: int = 1,
    apply_transform_to_first_instance: bool = True,
    defer_change_notifications: bool = False,
    append_options: GeometryScriptAppendMeshOptions = [
        GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING
    ],
    compact_appended_materials: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[MaterialInterface]]
```

X.append_mesh_repeated_with_materials(target_mesh, target_mesh_material_list, append_mesh, append_mesh_material_list, append_transform, repeat_count=1, apply_transform_to_first_instance=True, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials=True, debug=None) -> (DynamicMesh, result_mesh_material_list=Array[MaterialInterface])
Repeatedly apply AppendTransform to the AppendMesh, each time adding the geometry to TargetMesh.
Also combines materials lists of the Target and Append meshes, and updates the output mesh materials to reference the combined list.

Args:
    target_mesh (DynamicMesh): 
    target_mesh_material_list (Array[MaterialInterface]): 
    append_mesh (DynamicMesh): 
    append_mesh_material_list (Array[MaterialInterface]): 
    append_transform (Transform): 
    repeat_count (int32): number of times to repeat the transform-append cycle
    apply_transform_to_first_instance (bool): if true, the AppendTransform is applied before the first mesh append, otherwise it is applied after
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another
    compact_appended_materials (bool): 
    debug (GeometryScriptDebug): 

Returns:
    Array[MaterialInterface]: 

    result_mesh_material_list (Array[MaterialInterface]):

<a id="unreal.GeometryScript_MeshEdits.append_mesh_repeated"></a>

#### append_mesh_repeated

```python
@classmethod
def append_mesh_repeated(
        cls,
        target_mesh: DynamicMesh,
        append_mesh: DynamicMesh,
        append_transform: Transform,
        repeat_count: int = 1,
        apply_transform_to_first_instance: bool = True,
        defer_change_notifications: bool = False,
        append_options: GeometryScriptAppendMeshOptions = [
            GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING
        ],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_mesh_repeated(target_mesh, append_mesh, append_transform, repeat_count=1, apply_transform_to_first_instance=True, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug=None) -> DynamicMesh
Repeatedly apply AppendTransform to the AppendMesh, each time adding the geometry to TargetMesh.

Args:
    target_mesh (DynamicMesh): 
    append_mesh (DynamicMesh): 
    append_transform (Transform): 
    repeat_count (int32): number of times to repeat the transform-append cycle
    apply_transform_to_first_instance (bool): if true, the AppendTransform is applied before the first mesh append, otherwise it is applied after
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshEdits.append_mesh"></a>

#### append_mesh

```python
@classmethod
def append_mesh(cls,
                target_mesh: DynamicMesh,
                append_mesh: DynamicMesh,
                append_transform: Transform,
                defer_change_notifications: bool = False,
                append_options: GeometryScriptAppendMeshOptions = [
                    GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING
                ],
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_mesh(target_mesh, append_mesh, append_transform, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug=None) -> DynamicMesh
Apply Append Transform to Append Mesh and then add its geometry to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    append_mesh (DynamicMesh): 
    append_transform (Transform): 
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshEdits.append_buffers_to_mesh"></a>

#### append_buffers_to_mesh

```python
@classmethod
def append_buffers_to_mesh(
    cls,
    target_mesh: DynamicMesh,
    buffers: GeometryScriptSimpleMeshBuffers,
    material_id: int = 0,
    defer_change_notifications: bool = False,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

X.append_buffers_to_mesh(target_mesh, buffers, material_id=0, defer_change_notifications=False, debug=None) -> (DynamicMesh, new_triangle_indices_list=GeometryScriptIndexList)
Adds a set of vertices/triangles to the mesh, with Normals, UVs, and Colors; returning the new triangles indices

Args:
    target_mesh (DynamicMesh): 
    buffers (GeometryScriptSimpleMeshBuffers): 
    material_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    new_triangle_indices_list (GeometryScriptIndexList):

<a id="unreal.GeometryScript_MeshEdits.add_vertices_to_mesh"></a>

#### add_vertices_to_mesh

```python
@classmethod
def add_vertices_to_mesh(
    cls,
    target_mesh: DynamicMesh,
    new_positions_list: GeometryScriptVectorList,
    defer_change_notifications: bool = False
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

X.add_vertices_to_mesh(target_mesh, new_positions_list, defer_change_notifications=False) -> (DynamicMesh, new_indices_list=GeometryScriptIndexList)
Adds a list of vertices to the mesh, and populates the NewIndicesList with the corresponding new Vertex IDs.

Args:
    target_mesh (DynamicMesh): 
    new_positions_list (GeometryScriptVectorList): 
    defer_change_notifications (bool): 

Returns:
    GeometryScriptIndexList: 

    new_indices_list (GeometryScriptIndexList):

<a id="unreal.GeometryScript_MeshEdits.add_vertex_to_mesh"></a>

#### add_vertex_to_mesh

```python
@classmethod
def add_vertex_to_mesh(
        cls,
        target_mesh: DynamicMesh,
        new_position: Vector,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

X.add_vertex_to_mesh(target_mesh, new_position, defer_change_notifications=False) -> (DynamicMesh, new_vertex_index=int32)
Adds a new vertex to the mesh and returns a new Vertex ID (NewVertexIndex).

Args:
    target_mesh (DynamicMesh): 
    new_position (Vector): 
    defer_change_notifications (bool): 

Returns:
    int32: 

    new_vertex_index (int32):

<a id="unreal.GeometryScript_MeshEdits.add_triangle_to_mesh"></a>

#### add_triangle_to_mesh

```python
@classmethod
def add_triangle_to_mesh(
        cls,
        target_mesh: DynamicMesh,
        new_triangle: IntVector,
        new_triangle_group_id: int = 0,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
```

X.add_triangle_to_mesh(target_mesh, new_triangle, new_triangle_group_id=0, defer_change_notifications=False, debug=None) -> (DynamicMesh, new_triangle_index=int32)
Adds a triangle (Vertex ID triplet) to the mesh and updates New Triangle Index with the resulting Triangle ID.

Args:
    target_mesh (DynamicMesh): 
    new_triangle (IntVector): 
    new_triangle_group_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    int32: 

    new_triangle_index (int32):

<a id="unreal.GeometryScript_MeshEdits.add_triangles_to_mesh"></a>

#### add_triangles_to_mesh

```python
@classmethod
def add_triangles_to_mesh(
    cls,
    target_mesh: DynamicMesh,
    new_triangles_list: GeometryScriptTriangleList,
    new_triangle_group_id: int = 0,
    defer_change_notifications: bool = False,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

X.add_triangles_to_mesh(target_mesh, new_triangles_list, new_triangle_group_id=0, defer_change_notifications=False, debug=None) -> (DynamicMesh, new_indices_list=GeometryScriptIndexList)
Adds a list of triangles to the mesh and populates the New Indices List with the corresponding new Triangle IDs.

Args:
    target_mesh (DynamicMesh): 
    new_triangles_list (GeometryScriptTriangleList): 
    new_triangle_group_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    new_indices_list (GeometryScriptIndexList):

<a id="unreal.GeometryScript_BoneWeights"></a>