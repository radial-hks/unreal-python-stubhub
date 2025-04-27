## DynamicMesh Objects

```python
class DynamicMesh(Object)
```

UDynamicMesh is a UObject container for a FDynamicMesh3.

**C++ Source:**

- **Module**: GeometryFramework
- **File**: UDynamicMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_mesh_generator`` (bool):  [Read-Write] Controls whether the active Generator (if configured) will be applied when rebuilding the mesh
- ``mesh_modified_bp_event`` (OnDynamicMeshModifiedBP):  [Read-Write] Blueprintable event called when mesh is modified, in the same cases as OnMeshChanged

<a id="unreal.DynamicMesh.mesh_modified_bp_event"></a>

#### mesh_modified_bp_event

```python
@property
def mesh_modified_bp_event() -> OnDynamicMeshModifiedBP
```

(OnDynamicMeshModifiedBP):  [Read-Write] Blueprintable event called when mesh is modified, in the same cases as OnMeshChanged

<a id="unreal.DynamicMesh.mesh_modified_bp_event"></a>

#### mesh_modified_bp_event

```python
@mesh_modified_bp_event.setter
def mesh_modified_bp_event(value: OnDynamicMeshModifiedBP) -> None
```

<a id="unreal.DynamicMesh.reset_to_cube"></a>

#### reset_to_cube

```python
def reset_to_cube() -> DynamicMesh
```

x.reset_to_cube() -> DynamicMesh
Clear the internal mesh to a 100x100x100 cube with base at the origin.
This this instead of Reset() if an initially-empty mesh is undesirable (eg for a Component)

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.reset"></a>

#### reset

```python
def reset() -> DynamicMesh
```

x.reset() -> DynamicMesh
Clear the internal mesh to an empty mesh.
This *does not* allocate a new mesh, so any existing mesh pointers/refs are still valid

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.is_empty"></a>

#### is_empty

```python
def is_empty() -> bool
```

x.is_empty() -> bool


Returns:
    bool: true if the mesh has no triangles

<a id="unreal.DynamicMesh.get_triangle_count"></a>

#### get_triangle_count

```python
def get_triangle_count() -> int
```

x.get_triangle_count() -> int32


Returns:
    int32: number of triangles in the mesh

<a id="unreal.DynamicMesh.compute_mesh_swept_hull"></a>

#### compute_mesh_swept_hull

```python
def compute_mesh_swept_hull(
    copy_to_mesh: DynamicMesh,
    projection_frame: Transform,
    options: GeometryScriptSweptHullOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

x.compute_mesh_swept_hull(copy_to_mesh, projection_frame, options, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh)
Compute the Swept Hull of a given Target Mesh for a given 3D Plane defined by ProjectionFrame, and put the result in Hull Mesh
The Swept Hull is a linear sweep of the 2D convex hull of the mesh vertices projected onto the plane (the sweep precisely contains the mesh extents along the plane normal)

Args:
    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the swept hull geometry.
    projection_frame (Transform): 
    options (GeometryScriptSweptHullOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the swept hull geometry.

    copy_to_mesh_out (DynamicMesh): The resulting swept hull.

<a id="unreal.DynamicMesh.compute_mesh_convex_hull"></a>

#### compute_mesh_convex_hull

```python
def compute_mesh_convex_hull(
    copy_to_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    options: GeometryScriptConvexHullOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

x.compute_mesh_convex_hull(copy_to_mesh, selection, options, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh)
Compute the Convex Hull of a given Target Mesh, or part of the mesh if an optional Selection is provided, and put the result in Hull Mesh

Args:
    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the convex hull geometry.
    selection (GeometryScriptMeshSelection): Selection of mesh faces/vertices to contain in the convex hull. If not provided, entire mesh is used.
    options (GeometryScriptConvexHullOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the convex hull geometry.

    copy_to_mesh_out (DynamicMesh): The resulting convex hull.

<a id="unreal.DynamicMesh.compute_mesh_convex_decomposition"></a>

#### compute_mesh_convex_decomposition

```python
def compute_mesh_convex_decomposition(
    copy_to_mesh: DynamicMesh,
    options: GeometryScriptConvexDecompositionOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

x.compute_mesh_convex_decomposition(copy_to_mesh, options, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh)
Compute a Convex Hull Decomposition of the given TargetMesh. Assuming more than one hull is requested,
multiple hulls will be returned that attempt to approximate the mesh. If simplification settings are enabled,
there is no guarantee that the entire mesh is contained in the hulls.
warning: this function can be quite expensive, and the results are expected to change in the future as the Convex Decomposition algorithm is improved

Args:
    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the convex hulls as a single, combined mesh. Note: SplitMeshByComponents can separate this result into its convex parts.
    options (GeometryScriptConvexDecompositionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the convex hulls as a single, combined mesh. Note: SplitMeshByComponents can separate this result into its convex parts.

    copy_to_mesh_out (DynamicMesh): A combined mesh of the convex hulls. Note: SplitMeshByComponents can separate this result into its convex parts.

<a id="unreal.DynamicMesh.set_vertex_position"></a>

#### set_vertex_position

```python
def set_vertex_position(
        vertex_id: int,
        new_position: Vector,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.set_vertex_position(vertex_id, new_position, defer_change_notifications=False) -> (DynamicMesh, is_valid_vertex=bool)
Set Vertex Position

Args:
    vertex_id (int32): 
    new_position (Vector): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_vertex (bool):

<a id="unreal.DynamicMesh.set_all_mesh_vertex_positions"></a>

#### set_all_mesh_vertex_positions

```python
def set_all_mesh_vertex_positions(
        position_list: GeometryScriptVectorList,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_all_mesh_vertex_positions(position_list, debug=None) -> DynamicMesh
Set all vertex positions in the TargetMesh to the specified Positions.

Args:
    position_list (GeometryScriptVectorList): new vertex Positions. Size must be less than or equal to the MaxVertexID of TargetMesh  (ie gaps are supported).
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.discard_mesh_attributes"></a>

#### discard_mesh_attributes

```python
def discard_mesh_attributes(
        defer_change_notifications: bool = False) -> DynamicMesh
```

x.discard_mesh_attributes(defer_change_notifications=False) -> DynamicMesh
Discard Mesh Attributes

Args:
    defer_change_notifications (bool): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.delete_vertices_from_mesh"></a>

#### delete_vertices_from_mesh

```python
def delete_vertices_from_mesh(
        vertex_list: GeometryScriptIndexList,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

x.delete_vertices_from_mesh(vertex_list, defer_change_notifications=False) -> (DynamicMesh, num_deleted=int32)
Removes a list of vertices from the mesh.
On return, NumDeleted will contain the actual number of vertices removed.

Args:
    vertex_list (GeometryScriptIndexList): 
    defer_change_notifications (bool): 

Returns:
    int32: 

    num_deleted (int32):

<a id="unreal.DynamicMesh.delete_vertex_from_mesh"></a>

#### delete_vertex_from_mesh

```python
def delete_vertex_from_mesh(
        vertex_id: int,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.delete_vertex_from_mesh(vertex_id, defer_change_notifications=False) -> (DynamicMesh, was_vertex_deleted=bool)
Removes a vertex from the mesh as indicated by the VertexID.
Should the delete fail, e.g. if the specified vertex was not a mesh element, the flag bWasVertexDeleted will be set to false.

Args:
    vertex_id (int32): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    was_vertex_deleted (bool):

<a id="unreal.DynamicMesh.delete_triangles_from_mesh"></a>

#### delete_triangles_from_mesh

```python
def delete_triangles_from_mesh(
        triangle_list: GeometryScriptIndexList,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

x.delete_triangles_from_mesh(triangle_list, defer_change_notifications=False) -> (DynamicMesh, num_deleted=int32)
Removes a list of triangles from the mesh.
On return, NumDeleted will contain the actual number of triangles removed.

Args:
    triangle_list (GeometryScriptIndexList): 
    defer_change_notifications (bool): 

Returns:
    int32: 

    num_deleted (int32):

<a id="unreal.DynamicMesh.delete_triangle_from_mesh"></a>

#### delete_triangle_from_mesh

```python
def delete_triangle_from_mesh(
        triangle_id: int,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.delete_triangle_from_mesh(triangle_id, defer_change_notifications=False) -> (DynamicMesh, was_triangle_deleted=bool)
Removes a triangle from the mesh as indicated by the Triangle ID.
Should the delete fail, e.g. if the specified triangle was not a mesh element, the flag bWasTriangleDelete will be set to false.

Args:
    triangle_id (int32): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    was_triangle_deleted (bool):

<a id="unreal.DynamicMesh.delete_selected_triangles_from_mesh"></a>

#### delete_selected_triangles_from_mesh

```python
def delete_selected_triangles_from_mesh(
        selection: GeometryScriptMeshSelection,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

x.delete_selected_triangles_from_mesh(selection, defer_change_notifications=False) -> (DynamicMesh, num_deleted=int32)
Removes specified triangles, identified by mesh selection, from the mesh.
On return, NumDeleted will contain the actual number of triangles removed.

Args:
    selection (GeometryScriptMeshSelection): 
    defer_change_notifications (bool): 

Returns:
    int32: 

    num_deleted (int32):

<a id="unreal.DynamicMesh.append_mesh_with_materials"></a>

#### append_mesh_with_materials

```python
def append_mesh_with_materials(
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

x.append_mesh_with_materials(target_mesh_material_list, append_mesh, append_mesh_material_list, append_transform, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials=True, debug=None) -> (DynamicMesh, result_mesh_material_list=Array[MaterialInterface])
Apply Append Transform to Append Mesh and then add its geometry to the Target Mesh.
Also combines materials lists of the Target and Append meshes, and updates the output mesh materials to reference the combined list.

Args:
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

<a id="unreal.DynamicMesh.append_mesh_transformed_with_materials"></a>

#### append_mesh_transformed_with_materials

```python
def append_mesh_transformed_with_materials(
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

x.append_mesh_transformed_with_materials(target_mesh_material_list, append_mesh, append_mesh_material_list, append_transforms, constant_transform, constant_transform_is_relative=True, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials=True, debug=None) -> (DynamicMesh, result_mesh_material_list=Array[MaterialInterface])
For each transform in AppendTransforms, apply the transform to AppendMesh and then add its geometry to the TargetMesh.
Also combines materials lists of the Target and Append meshes, and updates the output mesh materials to reference the combined list.

Args:
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

<a id="unreal.DynamicMesh.append_mesh_transformed"></a>

#### append_mesh_transformed

```python
def append_mesh_transformed(
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

x.append_mesh_transformed(append_mesh, append_transforms, constant_transform, constant_transform_is_relative=True, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug=None) -> DynamicMesh
For each transform in AppendTransforms, apply the transform to AppendMesh and then add its geometry to the TargetMesh.

Args:
    append_mesh (DynamicMesh): 
    append_transforms (Array[Transform]): 
    constant_transform (Transform): the Constant transform will be applied after each Append transform
    constant_transform_is_relative (bool): if true, the Constant transform is applied "in the frame" of the Append Transform, otherwise it is applied as a second transform in local coordinates (ie rotate around the AppendTransform X axis, vs around the local X axis)
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_mesh_repeated_with_materials"></a>

#### append_mesh_repeated_with_materials

```python
def append_mesh_repeated_with_materials(
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

x.append_mesh_repeated_with_materials(target_mesh_material_list, append_mesh, append_mesh_material_list, append_transform, repeat_count=1, apply_transform_to_first_instance=True, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials=True, debug=None) -> (DynamicMesh, result_mesh_material_list=Array[MaterialInterface])
Repeatedly apply AppendTransform to the AppendMesh, each time adding the geometry to TargetMesh.
Also combines materials lists of the Target and Append meshes, and updates the output mesh materials to reference the combined list.

Args:
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

<a id="unreal.DynamicMesh.append_mesh_repeated"></a>

#### append_mesh_repeated

```python
def append_mesh_repeated(
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

x.append_mesh_repeated(append_mesh, append_transform, repeat_count=1, apply_transform_to_first_instance=True, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug=None) -> DynamicMesh
Repeatedly apply AppendTransform to the AppendMesh, each time adding the geometry to TargetMesh.

Args:
    append_mesh (DynamicMesh): 
    append_transform (Transform): 
    repeat_count (int32): number of times to repeat the transform-append cycle
    apply_transform_to_first_instance (bool): if true, the AppendTransform is applied before the first mesh append, otherwise it is applied after
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_mesh"></a>

#### append_mesh

```python
def append_mesh(append_mesh: DynamicMesh,
                append_transform: Transform,
                defer_change_notifications: bool = False,
                append_options: GeometryScriptAppendMeshOptions = [
                    GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING
                ],
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_mesh(append_mesh, append_transform, defer_change_notifications=False, append_options=[GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug=None) -> DynamicMesh
Apply Append Transform to Append Mesh and then add its geometry to the Target Mesh.

Args:
    append_mesh (DynamicMesh): 
    append_transform (Transform): 
    defer_change_notifications (bool): 
    append_options (GeometryScriptAppendMeshOptions): Control how details like mesh attributes are handled when one mesh is appended to another.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_buffers_to_mesh"></a>

#### append_buffers_to_mesh

```python
def append_buffers_to_mesh(
    buffers: GeometryScriptSimpleMeshBuffers,
    material_id: int = 0,
    defer_change_notifications: bool = False,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

x.append_buffers_to_mesh(buffers, material_id=0, defer_change_notifications=False, debug=None) -> (DynamicMesh, new_triangle_indices_list=GeometryScriptIndexList)
Adds a set of vertices/triangles to the mesh, with Normals, UVs, and Colors; returning the new triangles indices

Args:
    buffers (GeometryScriptSimpleMeshBuffers): 
    material_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    new_triangle_indices_list (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.add_vertices_to_mesh"></a>

#### add_vertices_to_mesh

```python
def add_vertices_to_mesh(
    new_positions_list: GeometryScriptVectorList,
    defer_change_notifications: bool = False
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

x.add_vertices_to_mesh(new_positions_list, defer_change_notifications=False) -> (DynamicMesh, new_indices_list=GeometryScriptIndexList)
Adds a list of vertices to the mesh, and populates the NewIndicesList with the corresponding new Vertex IDs.

Args:
    new_positions_list (GeometryScriptVectorList): 
    defer_change_notifications (bool): 

Returns:
    GeometryScriptIndexList: 

    new_indices_list (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.add_vertex_to_mesh"></a>

#### add_vertex_to_mesh

```python
def add_vertex_to_mesh(
        new_position: Vector,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

x.add_vertex_to_mesh(new_position, defer_change_notifications=False) -> (DynamicMesh, new_vertex_index=int32)
Adds a new vertex to the mesh and returns a new Vertex ID (NewVertexIndex).

Args:
    new_position (Vector): 
    defer_change_notifications (bool): 

Returns:
    int32: 

    new_vertex_index (int32):

<a id="unreal.DynamicMesh.add_triangle_to_mesh"></a>

#### add_triangle_to_mesh

```python
def add_triangle_to_mesh(
        new_triangle: IntVector,
        new_triangle_group_id: int = 0,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
```

x.add_triangle_to_mesh(new_triangle, new_triangle_group_id=0, defer_change_notifications=False, debug=None) -> (DynamicMesh, new_triangle_index=int32)
Adds a triangle (Vertex ID triplet) to the mesh and updates New Triangle Index with the resulting Triangle ID.

Args:
    new_triangle (IntVector): 
    new_triangle_group_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    int32: 

    new_triangle_index (int32):

<a id="unreal.DynamicMesh.add_triangles_to_mesh"></a>

#### add_triangles_to_mesh

```python
def add_triangles_to_mesh(
    new_triangles_list: GeometryScriptTriangleList,
    new_triangle_group_id: int = 0,
    defer_change_notifications: bool = False,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

x.add_triangles_to_mesh(new_triangles_list, new_triangle_group_id=0, defer_change_notifications=False, debug=None) -> (DynamicMesh, new_indices_list=GeometryScriptIndexList)
Adds a list of triangles to the mesh and populates the New Indices List with the corresponding new Triangle IDs.

Args:
    new_triangles_list (GeometryScriptTriangleList): 
    new_triangle_group_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    new_indices_list (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.transfer_bone_weights_from_mesh"></a>

#### transfer_bone_weights_from_mesh

```python
def transfer_bone_weights_from_mesh(
        target_mesh: DynamicMesh,
        options: GeometryScriptTransferBoneWeightsOptions = [
            TransferBoneWeightsMethod.CLOSEST_POINT_ON_SURFACE,
            OutputTargetMeshBones.SOURCE_BONES, ["Default"], ["Default"],
            -1.000000, -1.000000, True, 0, 0.000000, "None"
        ],
        selection: GeometryScriptMeshSelection = [],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.transfer_bone_weights_from_mesh(target_mesh, options=[TransferBoneWeightsMethod.CLOSEST_POINT_ON_SURFACE, OutputTargetMeshBones.SOURCE_BONES, ["Default"], ["Default"], -1.000000, -1.000000, True, 0, 0.000000, "None"], selection=[], debug=None) -> DynamicMesh
Transfer the bone weights from the SourceMesh to the TargetMesh. Assumes that the meshes are aligned. Otherwise,
use the TransformMesh geometry script function to align them.

Args:
    target_mesh (DynamicMesh): The mesh we are transferring the weights to.
    options (GeometryScriptTransferBoneWeightsOptions): The options to set for the transfer weight algorithm.
    selection (GeometryScriptMeshSelection): Optional subset of target mesh vertices to transfer weights to. If left empty, skin weights will be transferred to all target mesh vertices.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_vertex_bone_weights"></a>

#### set_vertex_bone_weights

```python
def set_vertex_bone_weights(
        vertex_id: int,
        bone_weights: Array[GeometryScriptBoneWeight],
        profile: GeometryScriptBoneWeightProfile = ["Default"],
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

x.set_vertex_bone_weights(vertex_id, bone_weights, profile=["Default"], debug=None) -> (DynamicMesh, is_valid_vertex_id=bool)
Set the Bone/Skin Weights at a given vertex of TargetMesh

Args:
    vertex_id (int32): vertex to update
    bone_weights (Array[GeometryScriptBoneWeight]): input array of bone index/weight pairs for the Vertex
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    is_valid_vertex_id (bool): will be returned as true if the vertex ID is valid

<a id="unreal.DynamicMesh.set_all_vertex_bone_weights"></a>

#### set_all_vertex_bone_weights

```python
def set_all_vertex_bone_weights(
        bone_weights: Array[GeometryScriptBoneWeight],
        profile: GeometryScriptBoneWeightProfile = ["Default"],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_all_vertex_bone_weights(bone_weights, profile=["Default"], debug=None) -> DynamicMesh
Set all vertices of the TargetMesh to the given Bone/Skin Weights

Args:
    bone_weights (Array[GeometryScriptBoneWeight]): input array of bone index/weight pairs for the Vertex
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.prune_bone_weights"></a>

#### prune_bone_weights

```python
def prune_bone_weights(bones_to_prune: Array[Name],
                       options: GeometryScriptPruneBoneWeightsOptions,
                       profile: GeometryScriptBoneWeightProfile = ["Default"],
                       debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.prune_bone_weights(bones_to_prune, options, profile=["Default"], debug=None) -> DynamicMesh
Prunes the given bones from any bone weight assignment on the given profile.
The bone weights are re-assigned based on the type of re-assignment specified in the options,
although in the case where the bone(s) being pruned are the sole bone weight on a vertex, then
the parent bone will be assigned as the sole bone weight for that vertex.
Bones are pruned iteratively from leaf to root, to ensure that weighs are progressively re-assigned
in case multiple bones along the same branch are being pruned.

Args:
    bones_to_prune (Array[Name]): The list of bones to remove.
    options (GeometryScriptPruneBoneWeightsOptions): The options to set for the pruning algorithm.
    profile (GeometryScriptBoneWeightProfile): The skin weight profile to prune the bones from.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.mesh_has_bone_weights"></a>

#### mesh_has_bone_weights

```python
def mesh_has_bone_weights(
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, bool]
```

x.mesh_has_bone_weights(profile=["Default"]) -> (DynamicMesh, has_bone_weights=bool)
Check whether the TargetMesh has a per-vertex Bone/Skin Weight Attribute set

Args:
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    bool: 

    has_bone_weights (bool): will be returned true if the requested bone weight profile exists

<a id="unreal.DynamicMesh.mesh_create_bone_weights"></a>

#### mesh_create_bone_weights

```python
def mesh_create_bone_weights(
    replace_existing_profile: bool = False,
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, bool]
```

x.mesh_create_bone_weights(replace_existing_profile=False, profile=["Default"]) -> (DynamicMesh, profile_existed=bool)
Create a new BoneWeights attribute on the TargetMesh, if it does not already exist. If it does exist,
and bReplaceExistingProfile is passed as true, the attribute will be removed and re-added, to reset it.

Args:
    replace_existing_profile (bool): if true, if the Profile already exists, it is reset
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    bool: 

    profile_existed (bool): will be returned true if the requested bone weight profile already existed

<a id="unreal.DynamicMesh.mesh_copy_bone_weights"></a>

#### mesh_copy_bone_weights

```python
def mesh_copy_bone_weights(
    target_profile: GeometryScriptBoneWeightProfile,
    source_profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, bool]
```

x.mesh_copy_bone_weights(target_profile, source_profile=["Default"]) -> (DynamicMesh, profile_existed=bool)
Copies all bone weights from a source profile onto a target profile, on the same mesh, replacing all
weights that existed on the target profile. If either the source or the target profile didn't exist,
then bProfileExisted will be set to false and no weights are copied.

Args:
    target_profile (GeometryScriptBoneWeightProfile): The skin weight profile to copy to.
    source_profile (GeometryScriptBoneWeightProfile): The skin weight profile to copy from.

Returns:
    bool: 

    profile_existed (bool): will be returned true if both of the requested bone weight profiles exist

<a id="unreal.DynamicMesh.get_vertex_bone_weights"></a>

#### get_vertex_bone_weights

```python
def get_vertex_bone_weights(
    vertex_id: int,
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, Array[GeometryScriptBoneWeight], bool]
```

x.get_vertex_bone_weights(vertex_id, profile=["Default"]) -> (DynamicMesh, bone_weights=Array[GeometryScriptBoneWeight], has_valid_bone_weights=bool)
Return an array of Bone/Skin Weights at a given vertex of TargetMesh

Args:
    vertex_id (int32): requested vertex
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    tuple: 

    bone_weights (Array[GeometryScriptBoneWeight]): output array of bone index/weight pairs for the given Vertex

    has_valid_bone_weights (bool): will be returned as true if the vertex has bone weights in the given profile, ie BoneWeights is valid

<a id="unreal.DynamicMesh.get_root_bone_name"></a>

#### get_root_bone_name

```python
def get_root_bone_name(
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Name]
```

x.get_root_bone_name(debug=None) -> (DynamicMesh, bone_name=Name)
Get the name of the root bone.

Args:
    debug (GeometryScriptDebug): 

Returns:
    Name: 

    bone_name (Name): The name of the root bone.

<a id="unreal.DynamicMesh.get_max_bone_weight_index"></a>

#### get_max_bone_weight_index

```python
def get_max_bone_weight_index(
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, bool, int]
```

x.get_max_bone_weight_index(profile=["Default"]) -> (DynamicMesh, has_bone_weights=bool, max_bone_index=int32)
Determine the largest bone weight index that exists on the Mesh

Args:
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    tuple: 

    has_bone_weights (bool): will be returned true if the requested bone weight profile exists

    max_bone_index (int32): maximum bone index will be returned here, or -1 if no bone indices exist

<a id="unreal.DynamicMesh.get_largest_vertex_bone_weight"></a>

#### get_largest_vertex_bone_weight

```python
def get_largest_vertex_bone_weight(
    vertex_id: int,
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, GeometryScriptBoneWeight, bool]
```

x.get_largest_vertex_bone_weight(vertex_id, profile=["Default"]) -> (DynamicMesh, bone_weight=GeometryScriptBoneWeight, has_valid_bone_weights=bool)
Return the Bone/Skin Weight with the maximum weight at a given vertex of TargetMesh

Args:
    vertex_id (int32): requested vertex
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    tuple: 

    bone_weight (GeometryScriptBoneWeight): the bone index and weight that was found to have the maximum weight

    has_valid_bone_weights (bool): will be returned as true if the vertex has bone weights in the given profile and a largest weight was found

<a id="unreal.DynamicMesh.get_bone_info"></a>

#### get_bone_info

```python
def get_bone_info(
    bone_name: Name,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, bool, GeometryScriptBoneInfo]
```

x.get_bone_info(bone_name, debug=None) -> (DynamicMesh, is_valid_bone_name=bool, bone_info=GeometryScriptBoneInfo)
Get the bone information.

Args:
    bone_name (Name): The name of bone.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_valid_bone_name (bool): Set to true if the TargetMesh contains a bone with the given name, false otherwise.

    bone_info (GeometryScriptBoneInfo): The information about the bone.

<a id="unreal.DynamicMesh.get_bone_index"></a>

#### get_bone_index

```python
def get_bone_index(
        bone_name: Name,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool, int]
```

x.get_bone_index(bone_name, debug=None) -> (DynamicMesh, is_valid_bone_name=bool, bone_index=int32)
Get Bone Index

Args:
    bone_name (Name): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_valid_bone_name (bool): 

    bone_index (int32):

<a id="unreal.DynamicMesh.get_bone_children"></a>

#### get_bone_children

```python
def get_bone_children(
    bone_name: Name,
    recursive: bool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, bool, Array[GeometryScriptBoneInfo]]
```

x.get_bone_children(bone_name, recursive, debug=None) -> (DynamicMesh, is_valid_bone_name=bool, children_info=Array[GeometryScriptBoneInfo])
Get the information about the children of the bone.

Args:
    bone_name (Name): The name of bone.
    recursive (bool): If set to true, grandchildren will also be added recursively
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_valid_bone_name (bool): Set to true if the TargetMesh contains a bone with the given name, false otherwise.

    children_info (Array[GeometryScriptBoneInfo]): The informattion of the children.

<a id="unreal.DynamicMesh.get_all_bones_info"></a>

#### get_all_bones_info

```python
def get_all_bones_info(
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[GeometryScriptBoneInfo]]
```

x.get_all_bones_info(debug=None) -> (DynamicMesh, bones_info=Array[GeometryScriptBoneInfo])
Get an array of bones representing the skeleton. Each entry contains information about the bone.

Args:
    debug (GeometryScriptDebug): 

Returns:
    Array[GeometryScriptBoneInfo]: 

    bones_info (Array[GeometryScriptBoneInfo]): Skeleton information.

<a id="unreal.DynamicMesh.discard_bones_from_mesh"></a>

#### discard_bones_from_mesh

```python
def discard_bones_from_mesh(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.discard_bones_from_mesh(debug=None) -> DynamicMesh
Discard the bone attributes (skeleton) from the TargetMesh.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.copy_bones_from_mesh"></a>

#### copy_bones_from_mesh

```python
def copy_bones_from_mesh(target_mesh: DynamicMesh,
                         options: GeometryScriptCopyBonesFromMeshOptions = [
                             False, BonesToCopyFromSource.ALL_BONES
                         ],
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.copy_bones_from_mesh(target_mesh, options=[False, BonesToCopyFromSource.ALL_BONES], debug=None) -> DynamicMesh
Copy the bone attributes (skeleton) from the SourceMesh to the TargetMesh.

Args:
    target_mesh (DynamicMesh): Mesh we are copying the bone attributes to.
    options (GeometryScriptCopyBonesFromMeshOptions): An option object to control how the copying is performed.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.compute_smooth_bone_weights"></a>

#### compute_smooth_bone_weights

```python
def compute_smooth_bone_weights(
        skeleton: Skeleton,
        options: GeometryScriptSmoothBoneWeightsOptions,
        profile: GeometryScriptBoneWeightProfile = ["Default"],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.compute_smooth_bone_weights(skeleton, options, profile=["Default"], debug=None) -> DynamicMesh
Computes a smooth skin binding for the given mesh to the skeleton provided.

Args:
    skeleton (Skeleton): The skeleton to compute binding for the skin weights.
    options (GeometryScriptSmoothBoneWeightsOptions): The options to set for the binding algorithm.
    profile (GeometryScriptBoneWeightProfile): The skin weight profile to update with the smooth binding.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_self_union"></a>

#### apply_mesh_self_union

```python
def apply_mesh_self_union(options: GeometryScriptMeshSelfUnionOptions,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_self_union(options, debug=None) -> DynamicMesh
Mesh-Boolean-Union an object with itself to repair self-intersections, remove floating geometry, etc.

Args:
    options (GeometryScriptMeshSelfUnionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_plane_slice"></a>

#### apply_mesh_plane_slice

```python
def apply_mesh_plane_slice(cut_frame: Transform,
                           options: GeometryScriptMeshPlaneSliceOptions,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_plane_slice(cut_frame, options, debug=None) -> DynamicMesh
Slices a mesh into two halves, with optional hole filling.

Args:
    cut_frame (Transform): defines the plane used to slice the TargetMesh.
    options (GeometryScriptMeshPlaneSliceOptions): selects additional clean-up operations performed after the cut.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_plane_cut"></a>

#### apply_mesh_plane_cut

```python
def apply_mesh_plane_cut(cut_frame: Transform,
                         options: GeometryScriptMeshPlaneCutOptions,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_plane_cut(cut_frame, options, debug=None) -> DynamicMesh
Applies a plane cut to a mesh, optionally filling any holes created.

Args:
    cut_frame (Transform): defines the plane used to cut the TargetMesh
    options (GeometryScriptMeshPlaneCutOptions): selects additional clean-up operations performed after the cut.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_mirror"></a>

#### apply_mesh_mirror

```python
def apply_mesh_mirror(mirror_frame: Transform,
                      options: GeometryScriptMeshMirrorOptions,
                      debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_mirror(mirror_frame, options, debug=None) -> DynamicMesh
Mirrors a mesh across a plane, with optional cutting and welding of triangles.

Args:
    mirror_frame (Transform): defines the plane used to mirror the TargetMesh.
    options (GeometryScriptMeshMirrorOptions): selects  additional clean-up operations performed after the mirror.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_boolean"></a>

#### apply_mesh_boolean

```python
def apply_mesh_boolean(target_transform: Transform,
                       tool_mesh: DynamicMesh,
                       tool_transform: Transform,
                       operation: GeometryScriptBooleanOperation,
                       options: GeometryScriptMeshBooleanOptions,
                       debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_boolean(target_transform, tool_mesh, tool_transform, operation, options, debug=None) -> DynamicMesh
Applies a Boolean operation (such as, Union, Intersect, and Subtract) to the Target Dynamic Mesh based on a Tool Dynamic Mesh.

Args:
    target_transform (Transform): used to position the TargetMesh
    tool_mesh (DynamicMesh): Dynamic Mesh that acts as the cutting tool
    tool_transform (Transform): used to position the ToolMesh
    operation (GeometryScriptBooleanOperation): selects the specific boolean operation
    options (GeometryScriptMeshBooleanOptions): selects additional options that are applied to the result
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.measure_distances_between_meshes"></a>

#### measure_distances_between_meshes

```python
def measure_distances_between_meshes(
    other_mesh: DynamicMesh,
    options: GeometryScriptMeasureMeshDistanceOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, float, float, float, float]
```

x.measure_distances_between_meshes(other_mesh, options, debug=None) -> (DynamicMesh, max_distance=double, min_distance=double, average_distance=double, root_mean_sqr_deviation=double)
Measures the min/max and average closest-point distances between two meshes.

Args:
    other_mesh (DynamicMesh): 
    options (GeometryScriptMeasureMeshDistanceOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    max_distance (double): 

    min_distance (double): 

    average_distance (double): 

    root_mean_sqr_deviation (double):

<a id="unreal.DynamicMesh.is_same_mesh_as"></a>

#### is_same_mesh_as

```python
def is_same_mesh_as(
    other_mesh: DynamicMesh,
    options: GeometryScriptIsSameMeshOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, bool, GeometryScriptMeshDifferenceInfo]
```

x.is_same_mesh_as(other_mesh, options, debug=None) -> (DynamicMesh, is_same_mesh=bool, difference_info=GeometryScriptMeshDifferenceInfo)
Returns true if the two input meshes are equivalent under the comparisons defined by the input options. If false, DifferenceInfo provides info on the first difference found.

Args:
    other_mesh (DynamicMesh): 
    options (GeometryScriptIsSameMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_same_mesh (bool): 

    difference_info (GeometryScriptMeshDifferenceInfo): If the meshes are different, provides info on the first difference found.

<a id="unreal.DynamicMesh.is_intersecting_mesh"></a>

#### is_intersecting_mesh

```python
def is_intersecting_mesh(
        target_transform: Transform,
        other_mesh: DynamicMesh,
        other_transform: Transform,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

x.is_intersecting_mesh(target_transform, other_mesh, other_transform, debug=None) -> (DynamicMesh, is_intersecting=bool)
Returns true if the two input meshes (with optional transforms) are geometrically intersecting.

Args:
    target_transform (Transform): 
    other_mesh (DynamicMesh): 
    other_transform (Transform): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    is_intersecting (bool):

<a id="unreal.DynamicMesh.split_mesh_by_polygroups"></a>

#### split_mesh_by_polygroups

```python
def split_mesh_by_polygroups(
    group_layer: GeometryScriptGroupLayer,
    mesh_pool: DynamicMeshPool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[DynamicMesh], Array[int]]
```

x.split_mesh_by_polygroups(group_layer, mesh_pool, debug=None) -> (DynamicMesh, component_meshes=Array[DynamicMesh], component_polygroups=Array[int32])
Create a new Mesh for each Polygroup of TargetMesh. Note that this may be a *large* number of meshes!
New meshes are drawn from MeshPool if it is provided, otherwise new UDynamicMesh instances are allocated

Args:
    group_layer (GeometryScriptGroupLayer): 
    mesh_pool (DynamicMeshPool): New meshes in ComponentMeshes output list are allocated from this pool if it is provided (highly recommended!!)
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    component_meshes (Array[DynamicMesh]): New List of meshes is returned here

    component_polygroups (Array[int32]): Original Polygroup for each Mesh in ComponentMeshes is returned here

<a id="unreal.DynamicMesh.split_mesh_by_material_i_ds"></a>

#### split_mesh_by_material_i_ds

```python
def split_mesh_by_material_i_ds(
    mesh_pool: DynamicMeshPool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[DynamicMesh], Array[int]]
```

x.split_mesh_by_material_i_ds(mesh_pool, debug=None) -> (DynamicMesh, component_meshes=Array[DynamicMesh], component_material_i_ds=Array[int32])
Create a new Mesh for each MaterialID of TargetMesh.
New meshes are drawn from MeshPool if it is provided, otherwise new UDynamicMesh instances are allocated

Args:
    mesh_pool (DynamicMeshPool): New meshes in ComponentMeshes output list are allocated from this pool if it is provided (highly recommended!!)
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    component_meshes (Array[DynamicMesh]): New List of meshes is returned here

    component_material_i_ds (Array[int32]): MaterialID for each Mesh in ComponentMeshes is returned here

<a id="unreal.DynamicMesh.split_mesh_by_components"></a>

#### split_mesh_by_components

```python
def split_mesh_by_components(
    mesh_pool: DynamicMeshPool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[DynamicMesh]]
```

x.split_mesh_by_components(mesh_pool, debug=None) -> (DynamicMesh, component_meshes=Array[DynamicMesh])
Create a new Mesh for each Connected Component of TargetMesh.
New meshes are drawn from MeshPool if it is provided, otherwise new UDynamicMesh instances are allocated

Args:
    mesh_pool (DynamicMeshPool): New meshes in ComponentMeshes output list are allocated from this pool if it is provided (highly recommended!!)
    debug (GeometryScriptDebug): 

Returns:
    Array[DynamicMesh]: 

    component_meshes (Array[DynamicMesh]): New List of meshes is returned here

<a id="unreal.DynamicMesh.get_sub_mesh_from_mesh"></a>

#### get_sub_mesh_from_mesh

```python
def get_sub_mesh_from_mesh(
    store_to_submesh: DynamicMesh,
    triangle_list: GeometryScriptIndexList,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

x.get_sub_mesh_from_mesh(store_to_submesh, triangle_list, debug=None) -> (DynamicMesh, store_to_submesh=DynamicMesh, store_to_submesh_out=DynamicMesh)
CopyMeshSelectionToMesh should be used instead of this function

Args:
    store_to_submesh (DynamicMesh): 
    triangle_list (GeometryScriptIndexList): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    store_to_submesh (DynamicMesh): 

    store_to_submesh_out (DynamicMesh):

<a id="unreal.DynamicMesh.copy_mesh_to_mesh"></a>

#### copy_mesh_to_mesh

```python
def copy_mesh_to_mesh(
    copy_to_mesh: DynamicMesh,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

x.copy_mesh_to_mesh(copy_to_mesh, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh)
Set CopyToMesh to be the same mesh as CopyFromMesh

Args:
    copy_to_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): 

    copy_to_mesh_out (DynamicMesh):

<a id="unreal.DynamicMesh.copy_mesh_selection_to_mesh"></a>

#### copy_mesh_selection_to_mesh

```python
def copy_mesh_selection_to_mesh(
    store_to_submesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    append_to_existing: bool = False,
    preserve_group_i_ds: bool = False,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

x.copy_mesh_selection_to_mesh(store_to_submesh, selection, append_to_existing=False, preserve_group_i_ds=False, debug=None) -> (DynamicMesh, store_to_submesh=DynamicMesh, store_to_submesh_out=DynamicMesh)
Extract the triangles identified by Selection from TargetMesh and copy/add them to StoreToSubmesh

Args:
    store_to_submesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    append_to_existing (bool): if false (default), StoreToSubmesh is cleared, otherwise selected triangles are appended
    preserve_group_i_ds (bool): if true, GroupIDs of triangles on TargetMesh are preserved in StoreToSubmesh. Otherwise new GroupIDs are allocated.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    store_to_submesh (DynamicMesh): 

    store_to_submesh_out (DynamicMesh):

<a id="unreal.DynamicMesh.apply_twist_warp_to_mesh"></a>

#### apply_twist_warp_to_mesh

```python
def apply_twist_warp_to_mesh(options: GeometryScriptTwistWarpOptions,
                             twist_orientation: Transform,
                             twist_angle: float = 45.000000,
                             twist_extent: float = 50.000000,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_twist_warp_to_mesh(options, twist_orientation, twist_angle=45.000000, twist_extent=50.000000, debug=None) -> DynamicMesh
Applies a twist warp around an axis defined by the Twist Orientation transform.
The extents of the affected region can be controlled by the Options.

Args:
    options (GeometryScriptTwistWarpOptions): 
    twist_orientation (Transform): 
    twist_angle (float): 
    twist_extent (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_perlin_noise_to_mesh"></a>

#### apply_perlin_noise_to_mesh

```python
def apply_perlin_noise_to_mesh(
        selection: GeometryScriptMeshSelection,
        options: GeometryScriptPerlinNoiseOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_perlin_noise_to_mesh(selection, options, debug=None) -> DynamicMesh
Applies 3D Perlin noise displacement to the Target Mesh.

Args:
    selection (GeometryScriptMeshSelection): if non-empty, only the vertices identified by the selection will be displaced, otherwise the Options' EmptyBehavior will be followed.
    options (GeometryScriptPerlinNoiseOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_math_warp_to_mesh"></a>

#### apply_math_warp_to_mesh

```python
def apply_math_warp_to_mesh(warp_orientation: Transform,
                            warp_type: GeometryScriptMathWarpType,
                            options: GeometryScriptMathWarpOptions,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_math_warp_to_mesh(warp_orientation, warp_type, options, debug=None) -> DynamicMesh
Applies various simple math-function-based warps around an axis defined by the Warp Orientation transform,
currently a 1D or 2D sine-wave with arbitrary orientation may be selected by WarpType.

Args:
    warp_orientation (Transform): 
    warp_type (GeometryScriptMathWarpType): 
    options (GeometryScriptMathWarpOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_iterative_smoothing_to_mesh"></a>

#### apply_iterative_smoothing_to_mesh

```python
def apply_iterative_smoothing_to_mesh(
        selection: GeometryScriptMeshSelection,
        options: GeometryScriptIterativeMeshSmoothingOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_iterative_smoothing_to_mesh(selection, options, debug=None) -> DynamicMesh
Applies a number of iterations of mesh smoothing to a Dynamic Mesh.

Args:
    selection (GeometryScriptMeshSelection): if non-empty, only the vertices identified by the selection will be subject to smoothing,  otherwise the Options' EmptyBehavior will be followed.
    options (GeometryScriptIterativeMeshSmoothingOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_flare_warp_to_mesh"></a>

#### apply_flare_warp_to_mesh

```python
def apply_flare_warp_to_mesh(options: GeometryScriptFlareWarpOptions,
                             flare_orientation: Transform,
                             flare_percent_x: float = 0.000000,
                             flare_percent_y: float = 0.000000,
                             flare_extent: float = 50.000000,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_flare_warp_to_mesh(options, flare_orientation, flare_percent_x=0.000000, flare_percent_y=0.000000, flare_extent=50.000000, debug=None) -> DynamicMesh
Applies a Flare/Bulge warp around an axis defined by the Flare Orientation transform.
The amount of flare in the perpendicular directions can be controlled by FlarePercentX and FlarePercentY
and the extents of the affected region can be controlled by the Options.

Args:
    options (GeometryScriptFlareWarpOptions): 
    flare_orientation (Transform): 
    flare_percent_x (float): 
    flare_percent_y (float): 
    flare_extent (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_displace_from_texture_map"></a>

#### apply_displace_from_texture_map

```python
def apply_displace_from_texture_map(
        texture: Texture2D,
        selection: GeometryScriptMeshSelection,
        options: GeometryScriptDisplaceFromTextureOptions,
        uv_layer: int = 0,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_displace_from_texture_map(texture, selection, options, uv_layer=0, debug=None) -> DynamicMesh
Applies a displacement to a Dynamic Mesh based on a Texture2D and a UV Channel.

Args:
    texture (Texture2D): 
    selection (GeometryScriptMeshSelection): if non-empty, only the vertices identified by the selection will be subject to displacement,  otherwise the Options' EmptyBehavior will be followed.
    options (GeometryScriptDisplaceFromTextureOptions): 
    uv_layer (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_displace_from_per_vertex_vectors"></a>

#### apply_displace_from_per_vertex_vectors

```python
def apply_displace_from_per_vertex_vectors(
        selection: GeometryScriptMeshSelection,
        vector_list: GeometryScriptVectorList,
        magnitude: float = 5.000000,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_displace_from_per_vertex_vectors(selection, vector_list, magnitude=5.000000, debug=None) -> DynamicMesh
Add the vectors in VectorList, scaled by Magnitude, to the vertex positions in Target Mesh.
VectorList Length must be >= the MaxVertexID of the Target Mesh.

Args:
    selection (GeometryScriptMeshSelection): if non-empty, only the vertices identified by the selection will be displaced. The VectorList must still be the same size as the whole mesh, this is just a filter on which vertices are updated.
    vector_list (GeometryScriptVectorList): 
    magnitude (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_bend_warp_to_mesh"></a>

#### apply_bend_warp_to_mesh

```python
def apply_bend_warp_to_mesh(options: GeometryScriptBendWarpOptions,
                            bend_orientation: Transform,
                            bend_angle: float = 45.000000,
                            bend_extent: float = 50.000000,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_bend_warp_to_mesh(options, bend_orientation, bend_angle=45.000000, bend_extent=50.000000, debug=None) -> DynamicMesh
Applies a Bend Warp around an axis defined by the Bend Orientation transform.
The extents of the affected region can be controlled by the Options.

Args:
    options (GeometryScriptBendWarpOptions): 
    bend_orientation (Transform): 
    bend_angle (float): 
    bend_extent (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.get_shortest_vertex_path"></a>

#### get_shortest_vertex_path

```python
def get_shortest_vertex_path(
    start_vertex_id: int,
    end_vertex_id: int,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

x.get_shortest_vertex_path(start_vertex_id, end_vertex_id, debug=None) -> (DynamicMesh, vertex_id_list=GeometryScriptIndexList, found_errors=bool)
Computes a vertex list that represents the shortest path constrained to travel along mesh triangle edges between the prescribed start and end vertex.
This can fail if the Start and End points are within separate connected components of the mesh.

Args:
    start_vertex_id (int32): indicates ID of mesh vertex that defines the starting point of the path.
    end_vertex_id (int32): indicates ID of the mesh vertex that defined the end point of the path.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    vertex_id_list (GeometryScriptIndexList): 

    found_errors (bool): will be false on success.

<a id="unreal.DynamicMesh.get_shortest_surface_path"></a>

#### get_shortest_surface_path

```python
def get_shortest_surface_path(
    start_triangle_id: int,
    start_bary_coords: Vector,
    end_triangle_id: int,
    end_bary_coords: Vector,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptPolyPath, bool]
```

x.get_shortest_surface_path(start_triangle_id, start_bary_coords, end_triangle_id, end_bary_coords, debug=None) -> (DynamicMesh, shortest_path=GeometryScriptPolyPath, found_errors=bool)
Computes a PolyPath that represents the shortest mesh surface path between two prescribed points on the provided mesh.
This can fail if the Start and End points are within separate connected components of the mesh.

Args:
    start_triangle_id (int32): the ID of mesh Triangle that contains the start point of the path.
    start_bary_coords (Vector): indicates the location of start point within the start triangle, in terms of barycentric coordinates.
    end_triangle_id (int32): the ID of mesh Triangle that contains the end point of the path.
    end_bary_coords (Vector): indicates the location of the end point within the end triangle, in terms of barycentric coordinates.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    shortest_path (GeometryScriptPolyPath): 

    found_errors (bool):

<a id="unreal.DynamicMesh.create_surface_path"></a>

#### create_surface_path

```python
def create_surface_path(
    direction: Vector,
    start_triangle_id: int,
    start_bary_coords: Vector,
    max_path_length: float,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptPolyPath, bool]
```

x.create_surface_path(direction, start_triangle_id, start_bary_coords, max_path_length, debug=None) -> (DynamicMesh, surface_path=GeometryScriptPolyPath, found_errors=bool)
Computes a PolyPath that represents a "straight" surface path starting at the prescribed point on the mesh, and continuing
in the indicated direction until reaching the requested path length or encountering a mesh boundary, whichever comes first.

Args:
    direction (Vector): is a three-dimensional vector that is projected onto the mesh surface to determine the path direction.
    start_triangle_id (int32): the ID of mesh Triangle that contains the start point of the path.
    start_bary_coords (Vector): indicates the location of start point within the start triangle, in terms of barycentric coordinates.
    max_path_length (float): sets the maximal length of the path, but the actual path may be shorter as it automatically terminates when encountering a mesh boundary edge.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    surface_path (GeometryScriptPolyPath): holds on return a PolyPath that forms a "straight" path along the mesh surface from the start position.

    found_errors (bool):

<a id="unreal.DynamicMesh.set_triangle_material_id"></a>

#### set_triangle_material_id

```python
def set_triangle_material_id(
        triangle_id: int,
        material_id: int,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.set_triangle_material_id(triangle_id, material_id, defer_change_notifications=False) -> (DynamicMesh, is_valid_triangle=bool)
Assigns the specified triangle the given Material ID.
If the Target Mesh does not have Material IDs enabled, or if the Triangle ID is not an element of the Target Mesh then bIsValidTriangle will be set to false.

Args:
    triangle_id (int32): 
    material_id (int32): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.DynamicMesh.set_polygroup_material_id"></a>

#### set_polygroup_material_id

```python
def set_polygroup_material_id(
        group_layer: GeometryScriptGroupLayer,
        polygroup_id: int,
        material_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

x.set_polygroup_material_id(group_layer, polygroup_id, material_id, defer_change_notifications=False, debug=None) -> (DynamicMesh, is_valid_polygroup_id=bool)
Set a new MaterialID on all the triangles of TargetMesh with the given PolyGroup.

Args:
    group_layer (GeometryScriptGroupLayer): PolyGroup Layer to use as basis for PolyGroups
    polygroup_id (int32): PolyGroup ID that specifies Triangles to set to new MaterialID
    material_id (int32): explicit new MaterialID to set
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    is_valid_polygroup_id (bool):

<a id="unreal.DynamicMesh.set_material_id_on_triangles"></a>

#### set_material_id_on_triangles

```python
def set_material_id_on_triangles(
        triangle_id_list: GeometryScriptIndexList,
        material_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_material_id_on_triangles(triangle_id_list, material_id, defer_change_notifications=False, debug=None) -> DynamicMesh
Assigns the Material ID to all the triangles specified by the Triangle ID List.

Args:
    triangle_id_list (GeometryScriptIndexList): the triangles in the target mesh that will be updated with the new Material ID
    material_id (int32): the ID to be assigned to each triangle in the input list.
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_material_id_for_mesh_selection"></a>

#### set_material_id_for_mesh_selection

```python
def set_material_id_for_mesh_selection(
        selection: GeometryScriptMeshSelection,
        material_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_material_id_for_mesh_selection(selection, material_id, defer_change_notifications=False, debug=None) -> DynamicMesh
Set a new MaterialID on all the triangles of the given Selection.

Args:
    selection (GeometryScriptMeshSelection): 
    material_id (int32): new Material ID to set
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_all_triangle_material_i_ds"></a>

#### set_all_triangle_material_i_ds

```python
def set_all_triangle_material_i_ds(
        triangle_material_id_list: GeometryScriptIndexList,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_all_triangle_material_i_ds(triangle_material_id_list, defer_change_notifications=False, debug=None) -> DynamicMesh
Sets the Material ID of all triangles in a mesh to the values in an input Index List.

Args:
    triangle_material_id_list (GeometryScriptIndexList): 
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.remap_to_new_material_i_ds_by_material"></a>

#### remap_to_new_material_i_ds_by_material

```python
def remap_to_new_material_i_ds_by_material(
        from_material_list: Array[MaterialInterface],
        to_material_list: Array[MaterialInterface],
        missing_material_id: int = -1,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.remap_to_new_material_i_ds_by_material(from_material_list, to_material_list, missing_material_id=-1, debug=None) -> DynamicMesh
Remap the Material IDs of the TargetMesh to a new set of Material IDs based on a 'From'/Current Material List, and a New Material List.
For each triangle, the current Material is determined as FromMaterialList[MaterialID], and then the first index of this Material is found
in the ToMaterialList, and this index is used as the new MaterialID

If a Material cannot be found in ToMaterialList, a warning will be printed and the MaterialID left unmodified,
unless MissingMaterialID is set to a value >= 0, in which case MissingMaterialID will be assigned

Args:
    from_material_list (Array[MaterialInterface]): 
    to_material_list (Array[MaterialInterface]): 
    missing_material_id (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.remap_material_i_ds"></a>

#### remap_material_i_ds

```python
def remap_material_i_ds(from_material_id: int,
                        to_material_id: int,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.remap_material_i_ds(from_material_id, to_material_id, debug=None) -> DynamicMesh
For all triangles with a Material ID matching the given value (From Material ID), update the Material ID to the new value (To Material ID).

Args:
    from_material_id (int32): 
    to_material_id (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.remap_and_combine_materials"></a>

#### remap_and_combine_materials

```python
def remap_and_combine_materials(
    target_mesh_materials: Array[MaterialInterface],
    required_materials: Array[MaterialInterface],
    remap_invalid_material_id: int = -1,
    compact_duplicate_materials: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[MaterialInterface]]
```

x.remap_and_combine_materials(target_mesh_materials, required_materials, remap_invalid_material_id=-1, compact_duplicate_materials=True, debug=None) -> (DynamicMesh, combined_materials=Array[MaterialInterface])
Remap material IDs to be consistent with a Required Materials list.
The Target Mesh material IDs will be remapped to reference the Combined Materials list,
which will always start with the Required Materials.

If a Material cannot be found in CurrentMeshMaterials, a warning will be printed and the MaterialID left unmodified,
unless RemapInvalidMaterialID is set to a value >= 0, in which case RemapInvalidMaterialID will be assigned

Args:
    target_mesh_materials (Array[MaterialInterface]): Initial materials used by the TargetMesh
    required_materials (Array[MaterialInterface]): Materials that must be used, unchanged, in the output
    remap_invalid_material_id (int32): If >= 0, automatically remap invalid input material IDs to this value
    compact_duplicate_materials (bool): If true, materials from TargetMeshMaterials will only be added if they are not already in RequiredMaterials. If false, all TargetMeshMaterials are appended.
    debug (GeometryScriptDebug): 

Returns:
    Array[MaterialInterface]: 

    combined_materials (Array[MaterialInterface]): Final materials used by the TargetMesh after remapping. Always starts with the RequiredMaterials.

<a id="unreal.DynamicMesh.get_triangles_by_material_id"></a>

#### get_triangles_by_material_id

```python
def get_triangles_by_material_id(
    material_id: int,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

x.get_triangles_by_material_id(material_id, debug=None) -> (DynamicMesh, triangle_id_list=GeometryScriptIndexList)
Populates Triangle ID List with the Triangle IDs of triangles that share the specified Material ID in the Target Mesh.

Args:
    material_id (int32): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    triangle_id_list (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.get_triangle_material_id"></a>

#### get_triangle_material_id

```python
def get_triangle_material_id(triangle_id: int) -> Tuple[int, bool]
```

x.get_triangle_material_id(triangle_id) -> (int32, is_valid_triangle=bool)
Returns the current Material ID for a Triangle.
If the mesh does not have Material IDs enabled or if the Triangle ID is not an element of the mesh, the value 0 will be returned and bIsValidTriangle will be false.

Args:
    triangle_id (int32): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.DynamicMesh.get_max_material_id"></a>

#### get_max_material_id

```python
def get_max_material_id() -> Tuple[int, bool]
```

x.get_max_material_id() -> (int32, has_material_i_ds=bool)
Get Max Material ID

Returns:
    bool: 

    has_material_i_ds (bool):

<a id="unreal.DynamicMesh.get_material_i_ds_of_triangles"></a>

#### get_material_i_ds_of_triangles

```python
def get_material_i_ds_of_triangles(
    triangle_id_list: GeometryScriptIndexList,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

x.get_material_i_ds_of_triangles(triangle_id_list, debug=None) -> (DynamicMesh, material_id_list=GeometryScriptIndexList)
This populates the MaterialIDList with Material IDs for each triangle in the TriangleIDList.
If a triangle is not present in the Target Mesh the number -1 will be used for the corresponding Material ID.
If Material IDs are not enabled on the TargetMesh no Material IDs will be added to the result list.

Args:
    triangle_id_list (GeometryScriptIndexList): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    material_id_list (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.get_all_triangle_material_i_ds"></a>

#### get_all_triangle_material_i_ds

```python
def get_all_triangle_material_i_ds(
) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

x.get_all_triangle_material_i_ds() -> (DynamicMesh, material_id_list=GeometryScriptIndexList, has_material_i_ds=bool)
Returns an Index List of all triangle Material IDs, constructed with one entry for each consecutive Triangle ID.
If Material IDs are not enabled on the mesh, bHasMaterialsIDs will be set to false on return and nothing will be added to the Material ID List.
warning: if the mesh is not Triangle-Compact (eg GetHasTriangleIDGaps == false) then the returned list will also have the same gaps where the number -1 will be recorded for any missing Triangle IDs.

Returns:
    tuple: 

    material_id_list (GeometryScriptIndexList): 

    has_material_i_ds (bool):

<a id="unreal.DynamicMesh.enable_material_i_ds"></a>

#### enable_material_i_ds

```python
def enable_material_i_ds(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.enable_material_i_ds(debug=None) -> DynamicMesh
Enables per-triangle Material IDs on a mesh and initializes the values to 0.
If Target Mesh already has Material IDs, this function will do nothing.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.delete_triangles_by_material_id"></a>

#### delete_triangles_by_material_id

```python
def delete_triangles_by_material_id(
        material_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
```

x.delete_triangles_by_material_id(material_id, defer_change_notifications=False, debug=None) -> (DynamicMesh, num_deleted=int32)
Delete all triangles in TargetMesh with the given MaterialID

Args:
    material_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    int32: 

    num_deleted (int32): number of deleted triangles is returned here

<a id="unreal.DynamicMesh.compact_material_i_ds"></a>

#### compact_material_i_ds

```python
def compact_material_i_ds(
    source_material_list: Array[MaterialInterface],
    remove_duplicate_materials: bool = False,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[MaterialInterface]]
```

x.compact_material_i_ds(source_material_list, remove_duplicate_materials=False, debug=None) -> (DynamicMesh, compacted_material_list=Array[MaterialInterface])
Compact the MaterialIDs of the TargetMesh, ie remove any un-used MaterialIDs and remap the remaining
N in-use MaterialIDs to the range [0,N-1]. Optionally compute a Compacted list of Materials.

Args:
    source_material_list (Array[MaterialInterface]): Input Material list, assumption is that SourceMaterialList.Num() == number of MaterialIDs on mesh at input
    remove_duplicate_materials (bool): Whether to also remove duplicate materials from the compacted list
    debug (GeometryScriptDebug): 

Returns:
    Array[MaterialInterface]: 

    compacted_material_list (Array[MaterialInterface]): new Compacted Material list, one-to-one with new compacted MaterialIDs

<a id="unreal.DynamicMesh.clear_material_i_ds"></a>

#### clear_material_i_ds

```python
def clear_material_i_ds(clear_value: int = 0,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.clear_material_i_ds(clear_value=0, debug=None) -> DynamicMesh
Resets all Material IDs on a mesh to the given ClearValue, or 0 if no ClearValue is provided.
If Material IDs are not already enabled on the Target Mesh, this function will first enable them and then set the value.

Args:
    clear_value (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_shell"></a>

#### apply_mesh_shell

```python
def apply_mesh_shell(options: GeometryScriptMeshOffsetOptions,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_shell(options, debug=None) -> DynamicMesh
Create a thickened shell from TargetMesh by offsetting the vertex positions along averaged vertex normals, inwards or outwards.
Similar to ApplyMeshOffset but also includes the initial mesh (possibly flipped, if the offset is positive)

Args:
    options (GeometryScriptMeshOffsetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_polygroup_bevel"></a>

#### apply_mesh_polygroup_bevel

```python
def apply_mesh_polygroup_bevel(
        options: GeometryScriptMeshBevelOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_polygroup_bevel(options, debug=None) -> DynamicMesh
Apply a Mesh Bevel operation to all PolyGroup Edges.

Args:
    options (GeometryScriptMeshBevelOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_offset_faces"></a>

#### apply_mesh_offset_faces

```python
def apply_mesh_offset_faces(options: GeometryScriptMeshOffsetFacesOptions,
                            selection: GeometryScriptMeshSelection,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_offset_faces(options, selection, debug=None) -> DynamicMesh
Apply an Offset to the faces of TargetMesh identified by the Selection, or all faces if the Selection is empty.
The Offset direction at each vertex can be derived from the averaged vertex normals or per-triangle normals.

Args:
    options (GeometryScriptMeshOffsetFacesOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_offset"></a>

#### apply_mesh_offset

```python
def apply_mesh_offset(options: GeometryScriptMeshOffsetOptions,
                      debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_offset(options, debug=None) -> DynamicMesh
Offset the vertices of TargetMesh from their initial positions based on averaged vertex normals.
This function is intended for high-res meshes, for polymodeling-style offsets, ApplyMeshOffsetFaces will produce better results.

Args:
    options (GeometryScriptMeshOffsetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_linear_extrude_faces"></a>

#### apply_mesh_linear_extrude_faces

```python
def apply_mesh_linear_extrude_faces(
        options: GeometryScriptMeshLinearExtrudeOptions,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_linear_extrude_faces(options, selection, debug=None) -> DynamicMesh
Apply Linear Extrusion (ie extrusion in a single direction) to the triangles of TargetMesh identified by the Selection.
The input Selection will still identify the same geometric elements after the Extrusion

Args:
    options (GeometryScriptMeshLinearExtrudeOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_inset_outset_faces"></a>

#### apply_mesh_inset_outset_faces

```python
def apply_mesh_inset_outset_faces(
        options: GeometryScriptMeshInsetOutsetFacesOptions,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_inset_outset_faces(options, selection, debug=None) -> DynamicMesh
Apply an Inset or Outset to the faces of TargetMesh identified by the Selection, or all faces if the Selection is empty.

Args:
    options (GeometryScriptMeshInsetOutsetFacesOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_extrude_compatibility_5p0"></a>

#### apply_mesh_extrude_compatibility_5p0

```python
def apply_mesh_extrude_compatibility_5p0(
        options: GeometryScriptMeshExtrudeOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_extrude_compatibility_5p0(options, debug=None) -> DynamicMesh
Backwards-Compatibility implementations
---------------------------------------------
These are versions/variants of the above functions that were released
in previous UE 5.x versions, that have since been updated.
To avoid breaking user scripts, these previous versions are currently kept and
called via redirectors registered in GeometryScriptingCoreModule.cpp.

These functions may be deprecated in future UE releases.

Args:
    options (GeometryScriptMeshExtrudeOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_extrude"></a>

#### apply_mesh_extrude

```python
def apply_mesh_extrude(options: GeometryScriptMeshExtrudeOptions,
                       debug: GeometryScriptDebug = None) -> DynamicMesh
```

deprecated: 'apply_mesh_extrude' was renamed to 'apply_mesh_extrude_compatibility_5p0'.

<a id="unreal.DynamicMesh.apply_mesh_duplicate_faces"></a>

#### apply_mesh_duplicate_faces

```python
def apply_mesh_duplicate_faces(
    selection: GeometryScriptMeshSelection,
    group_options: GeometryScriptMeshEditPolygroupOptions = [
        GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0
    ],
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.apply_mesh_duplicate_faces(selection, group_options=[GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0], debug=None) -> (DynamicMesh, new_triangles=GeometryScriptMeshSelection)
Duplicate the triangles of TargetMesh identified by the Selection

Args:
    selection (GeometryScriptMeshSelection): 
    group_options (GeometryScriptMeshEditPolygroupOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptMeshSelection: 

    new_triangles (GeometryScriptMeshSelection): a Mesh Selection of the duplicate triangles is returned here (with type Triangles)

<a id="unreal.DynamicMesh.apply_mesh_disconnect_faces_along_edges"></a>

#### apply_mesh_disconnect_faces_along_edges

```python
def apply_mesh_disconnect_faces_along_edges(
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_disconnect_faces_along_edges(selection, debug=None) -> DynamicMesh
Disconnect triangles of TargetMesh along the edges of the Selection.
The input Selection will still identify the same geometric elements after Disconnecting.

Args:
    selection (GeometryScriptMeshSelection): Which edges to operate on. Non-edge selections will be interpreted as edge selections -- i.e., all selected triangles' edges, or all selected vertices' one-ring edges.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_disconnect_faces"></a>

#### apply_mesh_disconnect_faces

```python
def apply_mesh_disconnect_faces(
        selection: GeometryScriptMeshSelection,
        allow_bowties_in_output: bool = True,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_disconnect_faces(selection, allow_bowties_in_output=True, debug=None) -> DynamicMesh
Disconnect the triangles of TargetMesh identified by the Selection.
The input Selection will still identify the same geometric elements after Disconnecting.

Args:
    selection (GeometryScriptMeshSelection): 
    allow_bowties_in_output (bool): if false, any bowtie vertices created by the operation will be automatically split
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_bevel_selection"></a>

#### apply_mesh_bevel_selection

```python
def apply_mesh_bevel_selection(
        selection: GeometryScriptMeshSelection,
        bevel_mode: GeometryScriptMeshBevelSelectionMode,
        bevel_options: GeometryScriptMeshBevelSelectionOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_bevel_selection(selection, bevel_mode, bevel_options, debug=None) -> DynamicMesh
Apply a Mesh Bevel operation to parts of TargetMesh using the BevelOptions settings, with additional options to handle region selections

Args:
    selection (GeometryScriptMeshSelection): specifies which mesh edges to Bevel
    bevel_mode (GeometryScriptMeshBevelSelectionMode): specifies whether Selection should be optionally converted to a Triangle Region or set of PolyGroup Edges
    bevel_options (GeometryScriptMeshBevelSelectionOptions): settings for the Bevel Operation
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_bevel_edge_selection"></a>

#### apply_mesh_bevel_edge_selection

```python
def apply_mesh_bevel_edge_selection(
        selection: GeometryScriptMeshSelection,
        bevel_options: GeometryScriptMeshBevelSelectionOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_bevel_edge_selection(selection, bevel_options, debug=None) -> DynamicMesh
Apply a Mesh Bevel operation to parts of TargetMesh using the BevelOptions settings.

Args:
    selection (GeometryScriptMeshSelection): specifies which mesh edges to Bevel
    bevel_options (GeometryScriptMeshBevelSelectionOptions): settings for the Bevel Operation
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.update_vertex_normal"></a>

#### update_vertex_normal

```python
def update_vertex_normal(
        vertex_id: int,
        update_normal: bool = True,
        new_normal: Vector = ...,
        update_tangents: bool = ...,
        new_tangent_x: Vector = ...,
        new_tangent_y: Vector = ...,
        merge_split_values: bool = ...,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.update_vertex_normal(vertex_id, update_normal=True, new_normal, update_tangents, new_tangent_x, new_tangent_y, merge_split_values, defer_change_notifications=False) -> (DynamicMesh, is_valid_vertex=bool)
Update the Normals and/or Tangents at VertexID of TargetMesh. Note that the specified vertex may have "split normals"
or "split tangents", ie in the case of hard/crease normals, UV seams, and so on. In these situations, by default
each of the unique normals/tangents at the vertex will be updated, but they will not be "merged", ie they will remain split.
However if bMergeSplitValues=true, then the vertex will be "un-split", ie after the function call the vertex will have
a single unique shared normal and/or tangents.

Note that this function requires that some normals/tangents already exist on the TargetMesh. If this is not the case,
functions like SetPerVertexNormals and ComputeTangents can be used to initialize the normals/tangents first.

Args:
    vertex_id (int32): 
    update_normal (bool): if true (default) then the normals overlay is updated
    new_normal (Vector): the new normal vector. This vector will not be normalized, it must be normalized by the calling code.
    update_tangents (bool): if true then the tangents overlay will be updated. If the tangents overlay does not exist, this function returns an error.
    new_tangent_x (Vector): the new tangent vector. This vector will not be normalized, it must be normalized by the calling code.
    new_tangent_y (Vector): the new bitangent/binormal vector. This vector will not be normalized, it must be normalized by the calling code.
    merge_split_values (bool): if true, any split normals/tangents at the vertex will be cleared, and a unique normal/tangent element will be set in the connected triangles
    defer_change_notifications (bool): if true, no mesh change notification will be sent. Set to true if changing many normals in a loop.

Returns:
    bool: 

    is_valid_vertex (bool): will be set to true on return if the VertexID was valid, ie had valid normals and tangents

<a id="unreal.DynamicMesh.set_split_normals_along_selected_edges"></a>

#### set_split_normals_along_selected_edges

```python
def set_split_normals_along_selected_edges(
        selection: GeometryScriptMeshSelection,
        split: bool = True,
        recalculate_normals: bool = True,
        calculate_options: GeometryScriptCalculateNormalsOptions = [
            True, True
        ],
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_split_normals_along_selected_edges(selection, split=True, recalculate_normals=True, calculate_options=[True, True], defer_change_notifications=False, debug=None) -> DynamicMesh
Set or remove split normals (aka sharp normals) for all edges in the Selection

Args:
    selection (GeometryScriptMeshSelection): Which edges to operate on
    split (bool): Whether to split normals along the selected edges; if false, they will be merged instead
    recalculate_normals (bool): Whether to recalculate normals along edges where they were split/merged
    calculate_options (GeometryScriptCalculateNormalsOptions): Options for computing the normals, if bRecalculateNormals is true
    defer_change_notifications (bool): If true, no mesh change notification will be sent. Set to true if performing many changes in a loop.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_per_vertex_normals"></a>

#### set_per_vertex_normals

```python
def set_per_vertex_normals(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_per_vertex_normals(debug=None) -> DynamicMesh
Recompute the normals of TargetMesh by averaging the triangle/face normals around each vertex, using combined area and angle weighting.
Each vertex will have a single normal, ie there will be no hard edges.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_per_face_normals"></a>

#### set_per_face_normals

```python
def set_per_face_normals(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_per_face_normals(debug=None) -> DynamicMesh
Recompute the normals of TargetMesh by setting the normals of each triangle vertex to the triangle/face normal.
Each vertex will have a unique normal in each triangle, ie there will be hard edges / split normals at every mesh edge

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_mesh_triangle_normals"></a>

#### set_mesh_triangle_normals

```python
def set_mesh_triangle_normals(
        triangle_id: int,
        normals: GeometryScriptTriangle,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.set_mesh_triangle_normals(triangle_id, normals, defer_change_notifications=False) -> (DynamicMesh, is_valid_triangle=bool)
Set the triangle-vertex normals for the given TriangleID on the TargetMesh. This will
create unique triangle-vertex normals, ie it will create hard edges / split normals in
the normal overlay for each edge of the triangle.

Args:
    triangle_id (int32): 
    normals (GeometryScriptTriangle): 
    defer_change_notifications (bool): if true, no mesh change notification will be sent. Set to true if changing many normals in a loop.

Returns:
    bool: 

    is_valid_triangle (bool): will be returned as false if TriangleID does not refer to a valid triangle

<a id="unreal.DynamicMesh.set_mesh_per_vertex_tangents"></a>

#### set_mesh_per_vertex_tangents

```python
def set_mesh_per_vertex_tangents(
        tangent_x_list: GeometryScriptVectorList,
        tangent_y_list: GeometryScriptVectorList,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_mesh_per_vertex_tangents(tangent_x_list, tangent_y_list, debug=None) -> DynamicMesh
Set all tangents in the TargetMesh Tangents Overlays to the specified per-vertex tangents
note: If setting Tangents for use with a DynamicMeshComponent, it is also necessary to set the Tangents Type on the Component to "Externally Provided"

Args:
    tangent_x_list (GeometryScriptVectorList): per-vertex tangent vectors. Size must be equal to the MaxVertexID of TargetMesh  (ie non-compact TargetMesh is supported)
    tangent_y_list (GeometryScriptVectorList): per-vertex bitangent/binormal vectors. Size must be equal to TangentXList
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_mesh_per_vertex_normals"></a>

#### set_mesh_per_vertex_normals

```python
def set_mesh_per_vertex_normals(
        vertex_normal_list: GeometryScriptVectorList,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_mesh_per_vertex_normals(vertex_normal_list, debug=None) -> DynamicMesh
Set all normals in the TargetMesh Normals Overlay to the specified per-vertex normals

Args:
    vertex_normal_list (GeometryScriptVectorList): per-vertex normals. Size must be equal to the MaxVertexID of TargetMesh  (ie non-compact TargetMesh is supported)
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.recompute_normals_for_mesh_selection"></a>

#### recompute_normals_for_mesh_selection

```python
def recompute_normals_for_mesh_selection(
        selection: GeometryScriptMeshSelection,
        calculate_options: GeometryScriptCalculateNormalsOptions,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.recompute_normals_for_mesh_selection(selection, calculate_options, defer_change_notifications=False, debug=None) -> DynamicMesh
Recompute the normals of TargetMesh on all the triangles/vertices of the given Selection using the given CalculateOptions.
This method will preserve any existing hard edges, ie each shared triangle-vertex normal is recomputed by averaging
the face normals of triangles that reference that shared triangle-vertex normal

Args:
    selection (GeometryScriptMeshSelection): 
    calculate_options (GeometryScriptCalculateNormalsOptions): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.recompute_normals"></a>

#### recompute_normals

```python
def recompute_normals(calculate_options: GeometryScriptCalculateNormalsOptions,
                      defer_change_notifications: bool = False,
                      debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.recompute_normals(calculate_options, defer_change_notifications=False, debug=None) -> DynamicMesh
Recompute the normals of TargetMesh using the given CalculateOptions. This method will preserve any existing hard
edges, ie each shared triangle-vertex normal is recomputed by averaging the face normals of triangles that reference
that shared triangle-vertex normal

Args:
    calculate_options (GeometryScriptCalculateNormalsOptions): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.get_mesh_per_vertex_tangents"></a>

#### get_mesh_per_vertex_tangents

```python
def get_mesh_per_vertex_tangents(
    average_split_vertex_values: bool = True
) -> Tuple[DynamicMesh, GeometryScriptVectorList, GeometryScriptVectorList,
           bool, bool]
```

x.get_mesh_per_vertex_tangents(average_split_vertex_values=True) -> (DynamicMesh, tangent_x_list=GeometryScriptVectorList, tangent_y_list=GeometryScriptVectorList, is_valid_tangent_set=bool, has_vertex_id_gaps=bool)
Get a list of single tangent vectors for each mesh vertex in the TargetMesh, derived from the Tangents Overlays.
The Tangents Overlay may store multiple tangents for a single vertex (ie split tangents)
In such cases the tangents can either be averaged, or the last tangent seen will be used, depending on the bAverageSplitVertexValues parameter.

Args:
    average_split_vertex_values (bool): control how multiple tangents at the same vertex should be interpreted

Returns:
    tuple: 

    tangent_x_list (GeometryScriptVectorList): output Tangent "X" vectors list will be stored here. Size will be equal to the MaxVertexID of TargetMesh  (not the VertexCount!)

    tangent_y_list (GeometryScriptVectorList): output Tangent "Y" vectors (Binormal/Bitangent) list will be stored here. Size will be equal to TangentXList

    is_valid_tangent_set (bool): will be set to true if the Tangent Overlay was valid

    has_vertex_id_gaps (bool): will be set to true if some vertex indices in TargetMesh were invalid, ie MaxVertexID > VertexCount

<a id="unreal.DynamicMesh.get_mesh_per_vertex_normals"></a>

#### get_mesh_per_vertex_normals

```python
def get_mesh_per_vertex_normals(
    average_split_vertex_values: bool = True
) -> Tuple[DynamicMesh, GeometryScriptVectorList, bool, bool]
```

x.get_mesh_per_vertex_normals(average_split_vertex_values=True) -> (DynamicMesh, normal_list=GeometryScriptVectorList, is_valid_normal_set=bool, has_vertex_id_gaps=bool)
Get a list of single normal vectors for each mesh vertex in the TargetMesh, derived from the Normals Overlay.
The Normals Overlay may store multiple normals for a single vertex (ie split normals)
In such cases the normals can either be averaged, or the last normal seen will be used, depending on the bAverageSplitVertexValues parameter.

Args:
    average_split_vertex_values (bool): control how multiple normals at the same vertex should be interpreted

Returns:
    tuple: 

    normal_list (GeometryScriptVectorList): output normal list will be stored here. Size will be equal to the MaxVertexID of TargetMesh  (not the VertexCount!)

    is_valid_normal_set (bool): will be set to true if the Normal Overlay was valid

    has_vertex_id_gaps (bool): will be set to true if some vertex indices in TargetMesh were invalid, ie MaxVertexID > VertexCount

<a id="unreal.DynamicMesh.get_mesh_has_tangents"></a>

#### get_mesh_has_tangents

```python
def get_mesh_has_tangents(
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

x.get_mesh_has_tangents(debug=None) -> (DynamicMesh, has_tangents=bool)
Check if the TargetMesh has a Tangents Attribute Layer enabled

Args:
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    has_tangents (bool):

<a id="unreal.DynamicMesh.flip_normals"></a>

#### flip_normals

```python
def flip_normals(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.flip_normals(debug=None) -> DynamicMesh
Flip/Invert the normal vectors of TargetMesh by multiplying them by -1, as well as reversing the mesh triangle orientations, ie triangle (a,b,c) becomes (b,a,c)

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.discard_tangents"></a>

#### discard_tangents

```python
def discard_tangents(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.discard_tangents(debug=None) -> DynamicMesh
Remove any existing Tangents Attribute Layer from the TargetMesh

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.compute_tangents"></a>

#### compute_tangents

```python
def compute_tangents(options: GeometryScriptTangentsOptions,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.compute_tangents(options, debug=None) -> DynamicMesh
Recompute Tangents for the TargetMesh, using the method and settings specified by FGeometryScriptTangentsOptions
note: If recomputing Tangents for use with a DynamicMeshComponent, it is also necessary to set the Tangents Type on the Component to "Externally Provided"

Args:
    options (GeometryScriptTangentsOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.compute_split_normals"></a>

#### compute_split_normals

```python
def compute_split_normals(
        split_options: GeometryScriptSplitNormalsOptions,
        calculate_options: GeometryScriptCalculateNormalsOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.compute_split_normals(split_options, calculate_options, debug=None) -> DynamicMesh
Recompute hard edges / split-normals for TargetMesh based on the provided SplitOptions, and then
recompute the new shared triangle-vertex normals using the given CalculateOptions.
The normal recomputation is identical to calling RecomputeNormals.

Args:
    split_options (GeometryScriptSplitNormalsOptions): 
    calculate_options (GeometryScriptCalculateNormalsOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.auto_repair_normals"></a>

#### auto_repair_normals

```python
def auto_repair_normals(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.auto_repair_normals(debug=None) -> DynamicMesh
Attempt to repair inconsistent normals in TargetMesh. Currently this is done in two passes. In the first pass, triangles with
reversed orientation from their neighours are incrementally flipped until each connected component has a consistent orientation,
if this is possible (note that this is not always globally possible, eg for a mobius-strip topology there is no consistent orientation).
In the second pass, the "global" orientation is detected by casting rays from outside the mesh. This may produce incorrect results for
meshes that are not closed.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_polygroup_for_mesh_selection"></a>

#### set_polygroup_for_mesh_selection

```python
def set_polygroup_for_mesh_selection(
        group_layer: GeometryScriptGroupLayer,
        selection: GeometryScriptMeshSelection,
        set_polygroup_id: int = 0,
        generate_new_polygroup: bool = False,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

x.set_polygroup_for_mesh_selection(group_layer, selection, set_polygroup_id=0, generate_new_polygroup=False, defer_change_notifications=False) -> (DynamicMesh, set_polygroup_id_out=int32)
Set a new PolyGroup on all the triangles of the given Selection, for the given GroupLayer.

Args:
    group_layer (GeometryScriptGroupLayer): 
    selection (GeometryScriptMeshSelection): 
    set_polygroup_id (int32): explicit new PolyGroupID to set
    generate_new_polygroup (bool): if true, SetPolyGroupID is ignored and a new unique PolyGroupID is generated
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification

Returns:
    int32: 

    set_polygroup_id_out (int32): the PolyGroupID that was set on the triangles is returned here (whether explicit or auto-generated)

<a id="unreal.DynamicMesh.set_num_extended_polygroup_layers"></a>

#### set_num_extended_polygroup_layers

```python
def set_num_extended_polygroup_layers(num_layers: int,
                                      debug: GeometryScriptDebug = None
                                      ) -> DynamicMesh
```

x.set_num_extended_polygroup_layers(num_layers, debug=None) -> DynamicMesh
Sets the number of extended PolyGroup Layers on a Mesh.

Args:
    num_layers (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.get_triangles_in_polygroup"></a>

#### get_triangles_in_polygroup

```python
def get_triangles_in_polygroup(
    group_layer: GeometryScriptGroupLayer, polygroup_id: int,
    triangle_i_ds_out: GeometryScriptIndexList
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

x.get_triangles_in_polygroup(group_layer, polygroup_id, triangle_i_ds_out) -> (DynamicMesh, triangle_i_ds_out=GeometryScriptIndexList)
Create list of all triangles with the given PolyGroup ID in the given GroupLayer (not necessarily a single connected-component)

Args:
    group_layer (GeometryScriptGroupLayer): 
    polygroup_id (int32): 
    triangle_i_ds_out (GeometryScriptIndexList): 

Returns:
    GeometryScriptIndexList: 

    triangle_i_ds_out (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.get_triangle_polygroup_id"></a>

#### get_triangle_polygroup_id

```python
def get_triangle_polygroup_id(group_layer: GeometryScriptGroupLayer,
                              triangle_id: int) -> Tuple[int, bool]
```

x.get_triangle_polygroup_id(group_layer, triangle_id) -> (int32, is_valid_triangle=bool)
Gets the PolyGroup ID associated with the specified Triangle ID and stored in the Group Layer.
If the Group Layer or the Triangle does not exist, the value 0 will be returned and bIsValidTriangle set to false.

Args:
    group_layer (GeometryScriptGroupLayer): indicates the layer on the Target Mesh to query.
    triangle_id (int32): identifies a triangle in the Target Mesh.

Returns:
    bool: 

    is_valid_triangle (bool): will be populated on return with false if either the Group Layer or the Triangle does not exist.

<a id="unreal.DynamicMesh.get_polygroup_i_ds_in_mesh"></a>

#### get_polygroup_i_ds_in_mesh

```python
def get_polygroup_i_ds_in_mesh(
    group_layer: GeometryScriptGroupLayer,
    polygroup_i_ds_out: GeometryScriptIndexList
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

x.get_polygroup_i_ds_in_mesh(group_layer, polygroup_i_ds_out) -> (DynamicMesh, polygroup_i_ds_out=GeometryScriptIndexList)
Create list of all unique PolyGroup IDs that exist in the PolyGroup Layer in the Mesh

Args:
    group_layer (GeometryScriptGroupLayer): 
    polygroup_i_ds_out (GeometryScriptIndexList): 

Returns:
    GeometryScriptIndexList: 

    polygroup_i_ds_out (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.get_all_triangle_polygroup_i_ds"></a>

#### get_all_triangle_polygroup_i_ds

```python
def get_all_triangle_polygroup_i_ds(
    group_layer: GeometryScriptGroupLayer,
    polygroup_i_ds_out: GeometryScriptIndexList
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

x.get_all_triangle_polygroup_i_ds(group_layer, polygroup_i_ds_out) -> (DynamicMesh, polygroup_i_ds_out=GeometryScriptIndexList)
Create list of per-triangle PolyGroup IDs for the PolyGroup in the Mesh
warning: if the mesh is not Triangle-Compact (eg GetHasTriangleIDGaps == false) then the returned list will also have the same gaps

Args:
    group_layer (GeometryScriptGroupLayer): 
    polygroup_i_ds_out (GeometryScriptIndexList): 

Returns:
    GeometryScriptIndexList: 

    polygroup_i_ds_out (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.enable_polygroups"></a>

#### enable_polygroups

```python
def enable_polygroups(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.enable_polygroups(debug=None) -> DynamicMesh
Enables the standard PolyGroup Layer on the Target Mesh.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.delete_triangles_in_polygroup"></a>

#### delete_triangles_in_polygroup

```python
def delete_triangles_in_polygroup(
        group_layer: GeometryScriptGroupLayer,
        polygroup_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
```

x.delete_triangles_in_polygroup(group_layer, polygroup_id, defer_change_notifications=False, debug=None) -> (DynamicMesh, num_deleted=int32)
Deletes all triangles from the Target Mesh that have a particular PolyGroup ID, in the specific Group Layer.

Args:
    group_layer (GeometryScriptGroupLayer): specifies the PolyGroup Layer to query.
    polygroup_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    int32: 

    num_deleted (int32): on return will contain the number of triangles deleted from the Target Mesh.

<a id="unreal.DynamicMesh.copy_polygroups_layer"></a>

#### copy_polygroups_layer

```python
def copy_polygroups_layer(from_group_layer: GeometryScriptGroupLayer,
                          to_group_layer: GeometryScriptGroupLayer,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.copy_polygroups_layer(from_group_layer, to_group_layer, debug=None) -> DynamicMesh
Copies the triangle PolyGroup assignments from one layer on the Target Mesh to another.
Note, this will have no effect if PolyGroups have not been enabled on the mesh, or if one of the requested Group Layers does not exist.

Args:
    from_group_layer (GeometryScriptGroupLayer): 
    to_group_layer (GeometryScriptGroupLayer): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.convert_uv_islands_to_polygroups"></a>

#### convert_uv_islands_to_polygroups

```python
def convert_uv_islands_to_polygroups(
        group_layer: GeometryScriptGroupLayer,
        uv_layer: int = 0,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.convert_uv_islands_to_polygroups(group_layer, uv_layer=0, debug=None) -> DynamicMesh
Creates and assigns a new PolyGroup for each disconnected UV island of a Mesh.
Note, this will have no effect if either the requested UV Layer or Group Layer does not exist.

Args:
    group_layer (GeometryScriptGroupLayer): indicates PolyGroup Layer that will be populated with unique values for each UV island.
    uv_layer (int32): specifies the UV Layer used to construct the PolyGroups.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.convert_components_to_polygroups"></a>

#### convert_components_to_polygroups

```python
def convert_components_to_polygroups(
        group_layer: GeometryScriptGroupLayer,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.convert_components_to_polygroups(group_layer, debug=None) -> DynamicMesh
Creates and assigns a new PolyGroup for each disconnected component of a Mesh. Regions of a mesh are disconnected they do not have a triangle in common.
Note, this will have no effect if the Group Layer does not exist.

Args:
    group_layer (GeometryScriptGroupLayer): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.compute_polygroups_from_polygon_detection"></a>

#### compute_polygroups_from_polygon_detection

```python
def compute_polygroups_from_polygon_detection(
        group_layer: GeometryScriptGroupLayer,
        respect_uv_seams: bool = True,
        respect_hard_normals: bool = False,
        quad_adjacency_weight: float = 1.000000,
        quad_metric_clamp: float = 1.000000,
        max_search_rounds: int = 1,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.compute_polygroups_from_polygon_detection(group_layer, respect_uv_seams=True, respect_hard_normals=False, quad_adjacency_weight=1.000000, quad_metric_clamp=1.000000, max_search_rounds=1, debug=None) -> DynamicMesh
Sets PolyGroups by identifying adjacent triangles that form reasonable quads. Note any triangles that do not neatly pair to form quads will receive their own PolyGroup.

Args:
    group_layer (GeometryScriptGroupLayer): 
    respect_uv_seams (bool): 
    respect_hard_normals (bool): 
    quad_adjacency_weight (double): 
    quad_metric_clamp (double): 
    max_search_rounds (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.compute_polygroups_from_angle_threshold"></a>

#### compute_polygroups_from_angle_threshold

```python
def compute_polygroups_from_angle_threshold(
        group_layer: GeometryScriptGroupLayer,
        crease_angle: float = 15.000000,
        min_group_size: int = 2,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.compute_polygroups_from_angle_threshold(group_layer, crease_angle=15.000000, min_group_size=2, debug=None) -> DynamicMesh
Sets PolyGroups by partitioning the mesh based on an edge crease/opening-angle.
Note, this will have no effect if the Group Layer does not exist.

Args:
    group_layer (GeometryScriptGroupLayer): indicates the PolyGroup Layer that will be populated.
    crease_angle (float): measured in degrees and used when comparing adjacent faces.
    min_group_size (int32): the minimum number of triangles in each PolyGroup.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.clear_polygroups"></a>

#### clear_polygroups

```python
def clear_polygroups(group_layer: GeometryScriptGroupLayer,
                     clear_value: int = 0,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.clear_polygroups(group_layer, clear_value=0, debug=None) -> DynamicMesh
Resets the triangle PolyGroup assignments within a PolyGroup Layer to the given Clear Value (or 0 if no Clear Value is specified).
Note, this will have no effect if PolyGroups have not been enabled on the mesh, or if the requested Group Layer does not exist.

Args:
    group_layer (GeometryScriptGroupLayer): 
    clear_value (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_voronoi_diagram2d"></a>

#### append_voronoi_diagram2d

```python
def append_voronoi_diagram2d(primitive_options: GeometryScriptPrimitiveOptions,
                             transform: Transform,
                             voronoi_sites: Array[Vector2D],
                             voronoi_options: GeometryScriptVoronoiOptions,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_voronoi_diagram2d(primitive_options, transform, voronoi_sites, voronoi_options, debug=None) -> DynamicMesh
Generates triangulated Voronoi Cells from the provided Voronoi Sites, identifying each with PolyGroups, and appends to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    voronoi_sites (Array[Vector2D]): 
    voronoi_options (GeometryScriptVoronoiOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_triangulated_polygon3d"></a>

#### append_triangulated_polygon3d

```python
def append_triangulated_polygon3d(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices3d: Array[Vector],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_triangulated_polygon3d(primitive_options, transform, polygon_vertices3d, debug=None) -> DynamicMesh
Appends a Triangulated Polygon (with vertices specified in 3D) to the Target Mesh.
Uses Ear Clipping-based triangulation. Output vertices will always be 1:1 with input vertices.
Polygon endpoint is not repeated.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices3d (Array[Vector]): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_triangulated_polygon"></a>

#### append_triangulated_polygon

```python
def append_triangulated_polygon(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices: Array[Vector2D],
        allow_self_intersections: bool = True,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_triangulated_polygon(primitive_options, transform, polygon_vertices, allow_self_intersections=True, debug=None) -> DynamicMesh
Appends a Triangulated Polygon to the Target Mesh.
Polygon should be oriented counter-clockwise to produce a correctly-oriented shape, otherwise it will be inside-out
Polygon endpoint is not repeated.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): 
    allow_self_intersections (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_torus"></a>

#### append_torus

```python
def append_torus(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        revolve_options: GeometryScriptRevolveOptions,
        major_radius: float = 50.000000,
        minor_radius: float = 25.000000,
        major_steps: int = 16,
        minor_steps: int = 8,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_torus(primitive_options, transform, revolve_options, major_radius=50.000000, minor_radius=25.000000, major_steps=16, minor_steps=8, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D torus (donut) or partial torus to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    revolve_options (GeometryScriptRevolveOptions): 
    major_radius (float): 
    minor_radius (float): 
    major_steps (int32): 
    minor_steps (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_sweep_polyline"></a>

#### append_sweep_polyline

```python
def append_sweep_polyline(primitive_options: GeometryScriptPrimitiveOptions,
                          transform: Transform,
                          polyline_vertices: Array[Vector2D],
                          sweep_path: Array[Transform],
                          polyline_tex_param_u: Array[float],
                          sweep_path_tex_param_v: Array[float],
                          loop: bool = False,
                          start_scale: float = 1.000000,
                          end_scale: float = 1.000000,
                          rotation_angle_deg: float = 0.000000,
                          miter_limit: float = 1.000000,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_sweep_polyline(primitive_options, transform, polyline_vertices, sweep_path, polyline_tex_param_u, sweep_path_tex_param_v, loop=False, start_scale=1.000000, end_scale=1.000000, rotation_angle_deg=0.000000, miter_limit=1.000000, debug=None) -> DynamicMesh
Sweep the given 2D PolylineVertices along the SweepPath specified as a set of FTransforms
If the 2D vertices are (U,V), then in the coordinate space of the FTransform, X points "along" the path,
Y points "right" (U) and Z points "up" (V).

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polyline_vertices (Array[Vector2D]): vertices of the open 2D path that will be swept along the SweepPath
    sweep_path (Array[Transform]): defines the 3D sweep path curve as a 3D poly-path, with rotation and scaling at each polypath vertex taken from the Transform
    polyline_tex_param_u (Array[float]): defines U coordinate value for each element in PolylineVertices. Must be same length as PolylineVertices (ignored if length=0).
    sweep_path_tex_param_v (Array[float]): defines V coordinate value for each element in SweepPath. Must be same length as SweepPath if bLoop=false, length+1 if bLoop=true, and ignored if length=0.
    loop (bool): if true, SweepPath is considered to be a Loop and a section connecting the end and start of the path is added (bCapped is ignored)
    start_scale (float): uniform scaling applied to the 2D polygon at the start of the path. Interpolated via arc length to EndScale at the end of the path.
    end_scale (float): uniform scaling applied to the 2D polygon at the end of the path
    rotation_angle_deg (float): Rotation applied to the 2D Polygon. Positive rotation rotates clockwise, ie Up/+Z/+V towards Right/+Y/+U. This Rotation is applied before any rotation in the SweepPath Transforms.
    miter_limit (float): If > 1, maximum scaling to apply at sharp turns in the curve path to keep the apparent swept profile from shrinking, and sweep path frames will be aligned to the path direction
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_sweep_polygon"></a>

#### append_sweep_polygon

```python
def append_sweep_polygon(primitive_options: GeometryScriptPrimitiveOptions,
                         transform: Transform,
                         polygon_vertices: Array[Vector2D],
                         sweep_path: Array[Transform],
                         loop: bool = False,
                         capped: bool = True,
                         start_scale: float = 1.000000,
                         end_scale: float = 1.000000,
                         rotation_angle_deg: float = 0.000000,
                         miter_limit: float = 1.000000,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_sweep_polygon(primitive_options, transform, polygon_vertices, sweep_path, loop=False, capped=True, start_scale=1.000000, end_scale=1.000000, rotation_angle_deg=0.000000, miter_limit=1.000000, debug=None) -> DynamicMesh
Sweep the given 2D PolygonVertices along the SweepPath specified as a set of FTransforms
If the 2D vertices are (U,V), then in the coordinate space of the FTransform, X points "along" the path,
Y points "right" (U) and Z points "up" (V).

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): vertices of the closed 2D polyon that will be swept along the SweepPath
    sweep_path (Array[Transform]): defines the 3D sweep path curve as a 3D poly-path, with rotation and scaling at each polypath vertex taken from the Transform
    loop (bool): if true, SweepPath is considered to be a Loop and a section connecting the end and start of the path is added (bCapped is ignored)
    capped (bool): if true the open ends of the swept generalized cylinder are triangulated
    start_scale (float): uniform scaling applied to the 2D polygon at the start of the path. Interpolated via arc length to EndScale at the end of the path.
    end_scale (float): uniform scaling applied to the 2D polygon at the end of the path
    rotation_angle_deg (float): Rotation applied to the 2D Polygon. Positive rotation rotates clockwise, ie Up/+Z/+V towards Right/+Y/+U. This Rotation is applied before any rotation in the SweepPath Transforms.
    miter_limit (float): If > 1, maximum scaling to apply at sharp turns in the curve path to keep the apparent swept profile from shrinking, and sweep path frames will be aligned to the path direction
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_spiral_revolve_polygon"></a>

#### append_spiral_revolve_polygon

```python
def append_spiral_revolve_polygon(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices: Array[Vector2D],
        revolve_options: GeometryScriptRevolveOptions,
        radius: float = 100.000000,
        steps: int = 18,
        rise_per_revolution: float = 50.000000,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_spiral_revolve_polygon(primitive_options, transform, polygon_vertices, revolve_options, radius=100.000000, steps=18, rise_per_revolution=50.000000, debug=None) -> DynamicMesh
Revolves a 2D polygon on a helical path, like one used to create a vertical spiral, appending the result to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): 
    revolve_options (GeometryScriptRevolveOptions): 
    radius (float): 
    steps (int32): 
    rise_per_revolution (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_sphere_lat_long_with_collision"></a>

#### append_sphere_lat_long_with_collision

```python
def append_sphere_lat_long_with_collision(
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    radius: float = 50.000000,
    steps_phi: int = 10,
    steps_theta: int = 16,
    origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode
    .CENTER,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

x.append_sphere_lat_long_with_collision(primitive_options, transform, radius=50.000000, steps_phi=10, steps_theta=16, origin=GeometryScriptPrimitiveOriginMode.CENTER, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D Sphere triangulated using latitude/longitude topology to the Target Mesh.
Also creates matching simple collision. Note: If transform has non-uniform scale, collision shape will be a uniform-scale approximation
matching the behavior of the physics system -- specifically, it will scale the sphere radius by the smallest axis scale.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    steps_phi (int32): 
    steps_theta (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.DynamicMesh.append_sphere_lat_long"></a>

#### append_sphere_lat_long

```python
def append_sphere_lat_long(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        radius: float = 50.000000,
        steps_phi: int = 10,
        steps_theta: int = 16,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.
    CENTER,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_sphere_lat_long(primitive_options, transform, radius=50.000000, steps_phi=10, steps_theta=16, origin=GeometryScriptPrimitiveOriginMode.CENTER, debug=None) -> DynamicMesh
Appends a 3D Sphere triangulated using latitude/longitude topology to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    steps_phi (int32): 
    steps_theta (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_sphere_box_with_collision"></a>

#### append_sphere_box_with_collision

```python
def append_sphere_box_with_collision(
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    radius: float = 50.000000,
    steps_x: int = 6,
    steps_y: int = 6,
    steps_z: int = 6,
    origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode
    .CENTER,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

x.append_sphere_box_with_collision(primitive_options, transform, radius=50.000000, steps_x=6, steps_y=6, steps_z=6, origin=GeometryScriptPrimitiveOriginMode.CENTER, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D sphere triangulated using box topology to the Target Mesh.
Also creates matching simple collision. Note: If transform has non-uniform scale, collision shape will be a uniform-scale approximation
matching the behavior of the physics system -- specifically, it will scale the sphere radius by the smallest axis scale.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.DynamicMesh.append_sphere_box"></a>

#### append_sphere_box

```python
def append_sphere_box(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        radius: float = 50.000000,
        steps_x: int = 6,
        steps_y: int = 6,
        steps_z: int = 6,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.
    CENTER,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_sphere_box(primitive_options, transform, radius=50.000000, steps_x=6, steps_y=6, steps_z=6, origin=GeometryScriptPrimitiveOriginMode.CENTER, debug=None) -> DynamicMesh
Appends a 3D sphere triangulated using box topology to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_simple_swept_polygon"></a>

#### append_simple_swept_polygon

```python
def append_simple_swept_polygon(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices: Array[Vector2D],
        sweep_path: Array[Vector],
        loop: bool = False,
        capped: bool = True,
        start_scale: float = 1.000000,
        end_scale: float = 1.000000,
        rotation_angle_deg: float = 0.000000,
        miter_limit: float = 1.000000,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_simple_swept_polygon(primitive_options, transform, polygon_vertices, sweep_path, loop=False, capped=True, start_scale=1.000000, end_scale=1.000000, rotation_angle_deg=0.000000, miter_limit=1.000000, debug=None) -> DynamicMesh
Sweeps a 2D polygon along an arbitrary 3D path, appending the result to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): vertices of the closed 2D polyon that will be swept along the SweepPath
    sweep_path (Array[Vector]): defines the 3D sweep path curve
    loop (bool): if true, SweepPath is considered to be a Loop and a section connecting the end and start of the path is added (bCapped is ignored)
    capped (bool): if true the open ends of the swept generalized cylinder are triangulated
    start_scale (float): uniform scaling applied to the 2D polygon at the start of the path. Interpolated via arc length to EndScale at the end of the path.
    end_scale (float): uniform scaling applied to the 2D polygon at the end of the path
    rotation_angle_deg (float): Rotation applied to the 2D Polygon. Positive rotation rotates clockwise, ie Up/+Z/+V towards Right/+Y/+U
    miter_limit (float): If > 1, maximum scaling to apply at sharp turns in the curve path to keep the apparent swept profile from shrinking
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_simple_extrude_polygon"></a>

#### append_simple_extrude_polygon

```python
def append_simple_extrude_polygon(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices: Array[Vector2D],
        height: float = 100.000000,
        height_steps: int = 0,
        capped: bool = True,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_simple_extrude_polygon(primitive_options, transform, polygon_vertices, height=100.000000, height_steps=0, capped=True, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Polygon should be oriented counter-clockwise to produce a correctly-oriented shape, otherwise it will be inside-out
Polygon endpoint is not repeated.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): 
    height (float): 
    height_steps (int32): 
    capped (bool): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_round_rectangle_xy"></a>

#### append_round_rectangle_xy

```python
def append_round_rectangle_xy(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        dimension_x: float = 100.000000,
        dimension_y: float = 100.000000,
        corner_radius: float = 5.000000,
        steps_width: int = 0,
        steps_height: int = 0,
        steps_round: int = 4,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_round_rectangle_xy(primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, corner_radius=5.000000, steps_width=0, steps_height=0, steps_round=4, debug=None) -> DynamicMesh
Appends a planar Rectangle with Rounded Corners (RoundRect) to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    corner_radius (float): 
    steps_width (int32): 
    steps_height (int32): 
    steps_round (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_round_rectangle_compatibility_5_0"></a>

#### append_round_rectangle_compatibility_5_0

```python
def append_round_rectangle_compatibility_5_0(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        dimension_x: float = 100.000000,
        dimension_y: float = 100.000000,
        corner_radius: float = 5.000000,
        steps_width: int = 0,
        steps_height: int = 0,
        steps_round: int = 4,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_round_rectangle_compatibility_5_0(primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, corner_radius=5.000000, steps_width=0, steps_height=0, steps_round=4, debug=None) -> DynamicMesh
5.0 Preview 1 Compatibility version of AppendRoundRectangleXY.
Incorrectly divides the input DimensionX and DimensionY by 2.
warning: It is strongly recommended that callers of this function update to the current AppendRoundRectangleXY function!

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    corner_radius (float): 
    steps_width (int32): 
    steps_height (int32): 
    steps_round (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_round_rectangle"></a>

#### append_round_rectangle

```python
def append_round_rectangle(primitive_options: GeometryScriptPrimitiveOptions,
                           transform: Transform,
                           dimension_x: float = 100.000000,
                           dimension_y: float = 100.000000,
                           corner_radius: float = 5.000000,
                           steps_width: int = 0,
                           steps_height: int = 0,
                           steps_round: int = 4,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

deprecated: 'append_round_rectangle' was renamed to 'append_round_rectangle_compatibility_5_0'.

<a id="unreal.DynamicMesh.append_revolve_polygon"></a>

#### append_revolve_polygon

```python
def append_revolve_polygon(primitive_options: GeometryScriptPrimitiveOptions,
                           transform: Transform,
                           polygon_vertices: Array[Vector2D],
                           revolve_options: GeometryScriptRevolveOptions,
                           radius: float = 100.000000,
                           steps: int = 8,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_revolve_polygon(primitive_options, transform, polygon_vertices, revolve_options, radius=100.000000, steps=8, debug=None) -> DynamicMesh
In the coordinate system of the revolve polygon, +X is towards the "outside" of the revolve donut, and +Y is "up" (ie +Z in local space)
Polygon should be oriented counter-clockwise to produce a correctly-oriented shape, otherwise it will be inside-out
Polygon endpoint is not repeated.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): 
    revolve_options (GeometryScriptRevolveOptions): 
    radius (float): 
    steps (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_revolve_path"></a>

#### append_revolve_path

```python
def append_revolve_path(primitive_options: GeometryScriptPrimitiveOptions,
                        transform: Transform,
                        path_vertices: Array[Vector2D],
                        revolve_options: GeometryScriptRevolveOptions,
                        steps: int = 8,
                        capped: bool = True,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_revolve_path(primitive_options, transform, path_vertices, revolve_options, steps=8, capped=True, debug=None) -> DynamicMesh
Revolves an open 2D path, with optional top and bottom end caps, appending the result to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    path_vertices (Array[Vector2D]): 
    revolve_options (GeometryScriptRevolveOptions): 
    steps (int32): 
    capped (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_rectangle_xy"></a>

#### append_rectangle_xy

```python
def append_rectangle_xy(primitive_options: GeometryScriptPrimitiveOptions,
                        transform: Transform,
                        dimension_x: float = 100.000000,
                        dimension_y: float = 100.000000,
                        steps_width: int = 0,
                        steps_height: int = 0,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_rectangle_xy(primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, steps_width=0, steps_height=0, debug=None) -> DynamicMesh
Appends a planar Rectangle to a Dynamic Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    steps_width (int32): 
    steps_height (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_rectangle_compatibility_5_0"></a>

#### append_rectangle_compatibility_5_0

```python
def append_rectangle_compatibility_5_0(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        dimension_x: float = 100.000000,
        dimension_y: float = 100.000000,
        steps_width: int = 0,
        steps_height: int = 0,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_rectangle_compatibility_5_0(primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, steps_width=0, steps_height=0, debug=None) -> DynamicMesh
5.0 Preview 1 Compatibility version of AppendRectangleXY. Incorrectly interprets the input dimensions.
Incorrectly divides the input DimensionX and DimensionY by 2.
warning: It is strongly recommended that callers of this function update to the current AppendRectangleXY function!

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    steps_width (int32): 
    steps_height (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_rectangle"></a>

#### append_rectangle

```python
def append_rectangle(primitive_options: GeometryScriptPrimitiveOptions,
                     transform: Transform,
                     dimension_x: float = 100.000000,
                     dimension_y: float = 100.000000,
                     steps_width: int = 0,
                     steps_height: int = 0,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

deprecated: 'append_rectangle' was renamed to 'append_rectangle_compatibility_5_0'.

<a id="unreal.DynamicMesh.append_linear_stairs"></a>

#### append_linear_stairs

```python
def append_linear_stairs(primitive_options: GeometryScriptPrimitiveOptions,
                         transform: Transform,
                         step_width: float = 100.000000,
                         step_height: float = 20.000000,
                         step_depth: float = 30.000000,
                         num_steps: int = 8,
                         floating: bool = False,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_linear_stairs(primitive_options, transform, step_width=100.000000, step_height=20.000000, step_depth=30.000000, num_steps=8, floating=False, debug=None) -> DynamicMesh
Appends a linear staircase to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    step_width (float): 
    step_height (float): 
    step_depth (float): 
    num_steps (int32): 
    floating (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_disc"></a>

#### append_disc

```python
def append_disc(primitive_options: GeometryScriptPrimitiveOptions,
                transform: Transform,
                radius: float = 50.000000,
                angle_steps: int = 16,
                spoke_steps: int = 0,
                start_angle: float = 0.000000,
                end_angle: float = 360.000000,
                hole_radius: float = 0.000000,
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_disc(primitive_options, transform, radius=50.000000, angle_steps=16, spoke_steps=0, start_angle=0.000000, end_angle=360.000000, hole_radius=0.000000, debug=None) -> DynamicMesh
Appends a planar disc to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    angle_steps (int32): 
    spoke_steps (int32): 
    start_angle (float): 
    end_angle (float): 
    hole_radius (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_delaunay_triangulation2d"></a>

#### append_delaunay_triangulation2d

```python
def append_delaunay_triangulation2d(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        vertex_positions: Array[Vector2D],
        constrained_edges: Array[IntPoint],
        triangulation_options:
    GeometryScriptConstrainedDelaunayTriangulationOptions,
        debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[int], bool]
```

x.append_delaunay_triangulation2d(primitive_options, transform, vertex_positions, constrained_edges, triangulation_options, debug=None) -> (DynamicMesh, positions_to_vertex_i_ds=Array[int32], has_duplicate_vertices=bool)
Generates a Delaunay Triangulation of the provided vertices, and appends it to the Target Mesh.
If optional Constrained Edges are provided, will generate a Constrained Delaunay Triangulation which connects the specified vertices with edges.
On success, all vertices are always appended to the output mesh, though duplicate vertices will not be used in any triangles and may optionally be removed.
Use PositionsToVertexIDs to map indices in the input VertexPositions array to vertex IDs in the Dynamic Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    vertex_positions (Array[Vector2D]): 
    constrained_edges (Array[IntPoint]): 
    triangulation_options (GeometryScriptConstrainedDelaunayTriangulationOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    positions_to_vertex_i_ds (Array[int32]): 

    has_duplicate_vertices (bool):

<a id="unreal.DynamicMesh.append_cylinder"></a>

#### append_cylinder

```python
def append_cylinder(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        radius: float = 50.000000,
        height: float = 100.000000,
        radial_steps: int = 12,
        height_steps: int = 0,
        capped: bool = True,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_cylinder(primitive_options, transform, radius=50.000000, height=100.000000, radial_steps=12, height_steps=0, capped=True, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D Cylinder (with optional end caps) to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    height (float): 
    radial_steps (int32): 
    height_steps (int32): 
    capped (bool): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_curved_stairs"></a>

#### append_curved_stairs

```python
def append_curved_stairs(primitive_options: GeometryScriptPrimitiveOptions,
                         transform: Transform,
                         step_width: float = 100.000000,
                         step_height: float = 20.000000,
                         inner_radius: float = 150.000000,
                         curve_angle: float = 90.000000,
                         num_steps: int = 8,
                         floating: bool = False,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_curved_stairs(primitive_options, transform, step_width=100.000000, step_height=20.000000, inner_radius=150.000000, curve_angle=90.000000, num_steps=8, floating=False, debug=None) -> DynamicMesh
Appends a rising circular staircase to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    step_width (float): 
    step_height (float): 
    inner_radius (float): 
    curve_angle (float): 
    num_steps (int32): 
    floating (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_cone"></a>

#### append_cone

```python
def append_cone(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        base_radius: float = 50.000000,
        top_radius: float = 5.000000,
        height: float = 100.000000,
        radial_steps: int = 12,
        height_steps: int = 4,
        capped: bool = True,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_cone(primitive_options, transform, base_radius=50.000000, top_radius=5.000000, height=100.000000, radial_steps=12, height_steps=4, capped=True, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D cone to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    base_radius (float): 
    top_radius (float): 
    height (float): 
    radial_steps (int32): 
    height_steps (int32): 
    capped (bool): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_capsule_with_collision"></a>

#### append_capsule_with_collision

```python
def append_capsule_with_collision(
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    radius: float = 30.000000,
    line_length: float = 75.000000,
    hemisphere_steps: int = 5,
    circle_steps: int = 8,
    segment_steps: int = 0,
    origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

x.append_capsule_with_collision(primitive_options, transform, radius=30.000000, line_length=75.000000, hemisphere_steps=5, circle_steps=8, segment_steps=0, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D Capsule to the Target Mesh.
Also creates matching simple collision. Note: If transform has non-uniform scale, collision shape will be a uniform-scale approximation
matching the behavior of the physics system -- specifically, it will scale the radius by the larger of the X, Y axis scales, and the length by the Z axis scale

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    line_length (float): 
    hemisphere_steps (int32): 
    circle_steps (int32): 
    segment_steps (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.DynamicMesh.append_capsule"></a>

#### append_capsule

```python
def append_capsule(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        radius: float = 30.000000,
        line_length: float = 75.000000,
        hemisphere_steps: int = 5,
        circle_steps: int = 8,
        segment_steps: int = 0,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_capsule(primitive_options, transform, radius=30.000000, line_length=75.000000, hemisphere_steps=5, circle_steps=8, segment_steps=0, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D Capsule to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    line_length (float): 
    hemisphere_steps (int32): 
    circle_steps (int32): 
    segment_steps (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_box_with_collision"></a>

#### append_box_with_collision

```python
def append_box_with_collision(
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    dimension_x: float = 100.000000,
    dimension_y: float = 100.000000,
    dimension_z: float = 100.000000,
    steps_x: int = 0,
    steps_y: int = 0,
    steps_z: int = 0,
    origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

x.append_box_with_collision(primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, dimension_z=100.000000, steps_x=0, steps_y=0, steps_z=0, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D box to the Target Mesh
Also creates matching simple collision

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    dimension_z (float): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.DynamicMesh.append_box"></a>

#### append_box

```python
def append_box(
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        dimension_x: float = 100.000000,
        dimension_y: float = 100.000000,
        dimension_z: float = 100.000000,
        steps_x: int = 0,
        steps_y: int = 0,
        steps_z: int = 0,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_box(primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, dimension_z=100.000000, steps_x=0, steps_y=0, steps_z=0, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D box to the Target Mesh.

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    dimension_z (float): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.append_bounding_box_with_collision"></a>

#### append_bounding_box_with_collision

```python
def append_bounding_box_with_collision(
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    box: Box,
    steps_x: int = 0,
    steps_y: int = 0,
    steps_z: int = 0,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

x.append_bounding_box_with_collision(primitive_options, transform, box, steps_x=0, steps_y=0, steps_z=0, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D box to the Target Mesh with dimensions and origin taken from the input Box
Also creates matching simple collision

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    box (Box): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.DynamicMesh.append_bounding_box"></a>

#### append_bounding_box

```python
def append_bounding_box(primitive_options: GeometryScriptPrimitiveOptions,
                        transform: Transform,
                        box: Box,
                        steps_x: int = 0,
                        steps_y: int = 0,
                        steps_z: int = 0,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.append_bounding_box(primitive_options, transform, box, steps_x=0, steps_y=0, steps_z=0, debug=None) -> DynamicMesh
Appends a 3D box to the Target Mesh with dimensions and origin taken from the input Box

Args:
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    box (Box): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.is_valid_vertex_id"></a>

#### is_valid_vertex_id

```python
def is_valid_vertex_id(vertex_id: int) -> bool
```

x.is_valid_vertex_id(vertex_id) -> bool
Returns true if Vertex ID refers to a valid vertex in the Target Mesh.

Args:
    vertex_id (int32): 

Returns:
    bool:

<a id="unreal.DynamicMesh.is_valid_triangle_id"></a>

#### is_valid_triangle_id

```python
def is_valid_triangle_id(triangle_id: int) -> bool
```

x.is_valid_triangle_id(triangle_id) -> bool
Returns true if Triangle ID refers to a valid Triangle in the Target Mesh.

Args:
    triangle_id (int32): 

Returns:
    bool:

<a id="unreal.DynamicMesh.get_vertex_position"></a>

#### get_vertex_position

```python
def get_vertex_position(vertex_id: int) -> Tuple[Vector, bool]
```

x.get_vertex_position(vertex_id) -> (Vector, is_valid_vertex=bool)
Gets the 3D position of a mesh vertex in the mesh local space, by Vertex ID.

Args:
    vertex_id (int32): 

Returns:
    bool: 

    is_valid_vertex (bool):

<a id="unreal.DynamicMesh.get_vertex_count"></a>

#### get_vertex_count

```python
def get_vertex_count() -> int
```

x.get_vertex_count() -> int32
Gets the number of vertices in the mesh. Note this may be less than the number of Vertex IDs used as some vertices may have been deleted.

Returns:
    int32:

<a id="unreal.DynamicMesh.get_vertex_connected_vertices"></a>

#### get_vertex_connected_vertices

```python
def get_vertex_connected_vertices(
        vertex_id: int) -> Tuple[DynamicMesh, Array[int]]
```

x.get_vertex_connected_vertices(vertex_id) -> (DynamicMesh, vertices=Array[int32])
Return array of Vertex IDs connected via a mesh edge to the given VertexID, ie the vertex one-ring

Args:
    vertex_id (int32): 

Returns:
    Array[int32]: 

    vertices (Array[int32]):

<a id="unreal.DynamicMesh.get_vertex_connected_triangles"></a>

#### get_vertex_connected_triangles

```python
def get_vertex_connected_triangles(
        vertex_id: int) -> Tuple[DynamicMesh, Array[int]]
```

x.get_vertex_connected_triangles(vertex_id) -> (DynamicMesh, triangles=Array[int32])
Return array of Triangle IDs connected to the given VertexID, ie the triangle one-ring

Args:
    vertex_id (int32): 

Returns:
    Array[int32]: 

    triangles (Array[int32]):

<a id="unreal.DynamicMesh.get_uv_set_bounding_box"></a>

#### get_uv_set_bounding_box

```python
def get_uv_set_bounding_box(uv_set_index: int) -> Tuple[Box2D, bool, bool]
```

x.get_uv_set_bounding_box(uv_set_index) -> (Box2D, is_valid_uv_set=bool, uv_set_is_empty=bool)
Gets the 2D bounding box of all UVs in the UV Channel.  If the UV Channel does not exist, or if the UV Channel is empty, the resulting box will be invalid.

Args:
    uv_set_index (int32): 

Returns:
    tuple: 

    is_valid_uv_set (bool): 

    uv_set_is_empty (bool):

<a id="unreal.DynamicMesh.get_triangle_vertex_colors"></a>

#### get_triangle_vertex_colors

```python
def get_triangle_vertex_colors(
    triangle_id: int
) -> Tuple[DynamicMesh, LinearColor, LinearColor, LinearColor, bool]
```

x.get_triangle_vertex_colors(triangle_id) -> (DynamicMesh, color1=LinearColor, color2=LinearColor, color3=LinearColor, tri_has_valid_vertex_colors=bool)
For the specified TriangleID of the TargetMesh, get the Vertex Colors at each vertex of the Triangle.
These Colors will be taken from the Vertex Color Attribute, ie they will potentially be split-colors.

Args:
    triangle_id (int32): 

Returns:
    tuple: 

    color1 (LinearColor): 

    color2 (LinearColor): 

    color3 (LinearColor): 

    tri_has_valid_vertex_colors (bool): will be returned true if TriangleID exists in TargetMesh and has Vertex Colors set

<a id="unreal.DynamicMesh.get_triangle_u_vs"></a>

#### get_triangle_u_vs

```python
def get_triangle_u_vs(
        uv_set_index: int,
        triangle_id: int) -> Tuple[Vector2D, Vector2D, Vector2D, bool]
```

x.get_triangle_u_vs(uv_set_index, triangle_id) -> (uv1=Vector2D, uv2=Vector2D, uv3=Vector2D, have_valid_u_vs=bool)
Returns the UV values associated with the three vertices of the triangle in the specified UV Channel.
If the Triangle does not exist in the mesh or if no UVs are set in the specified UV Channel for the triangle, the resulting values will be (0,0) and bHaveValidUVs will be set to false.

Args:
    uv_set_index (int32): 
    triangle_id (int32): 

Returns:
    tuple: 

    uv1 (Vector2D): 

    uv2 (Vector2D): 

    uv3 (Vector2D): 

    have_valid_u_vs (bool):

<a id="unreal.DynamicMesh.get_triangle_positions"></a>

#### get_triangle_positions

```python
def get_triangle_positions(
        triangle_id: int) -> Tuple[bool, Vector, Vector, Vector]
```

x.get_triangle_positions(triangle_id) -> (is_valid_triangle=bool, vertex1=Vector, vertex2=Vector, vertex3=Vector)
* Returns the 3D positions (in the mesh local space) of the three vertices of the requested triangle.
* If the Triangle ID is not an element of the Target Mesh, all three vertices will be returned as (0, 0, 0) and bIsValidTriangle will be set to false.

Args:
    triangle_id (int32): 

Returns:
    tuple: 

    is_valid_triangle (bool): 

    vertex1 (Vector): 

    vertex2 (Vector): 

    vertex3 (Vector):

<a id="unreal.DynamicMesh.get_triangle_normal_tangents"></a>

#### get_triangle_normal_tangents

```python
def get_triangle_normal_tangents(
    triangle_id: int
) -> Tuple[DynamicMesh, bool, GeometryScriptTriangle, GeometryScriptTriangle,
           GeometryScriptTriangle]
```

x.get_triangle_normal_tangents(triangle_id) -> (DynamicMesh, tri_has_valid_elements=bool, normals=GeometryScriptTriangle, tangents=GeometryScriptTriangle, bi_tangents=GeometryScriptTriangle)
For the specified Triangle ID of the TargetMesh, get the Normal and Tangent vectors at each vertex of the Triangle.
These Normals/Tangents will be taken from the Normal and Tangents Overlays, i.e. they will potentially be split-normals.

Args:
    triangle_id (int32): 

Returns:
    tuple: 

    tri_has_valid_elements (bool): will be returned true if TriangleID exists in TargetMesh and has Normals and Tangents set.

    normals (GeometryScriptTriangle): 

    tangents (GeometryScriptTriangle): 

    bi_tangents (GeometryScriptTriangle):

<a id="unreal.DynamicMesh.get_triangle_normals"></a>

#### get_triangle_normals

```python
def get_triangle_normals(
        triangle_id: int) -> Tuple[DynamicMesh, Vector, Vector, Vector, bool]
```

x.get_triangle_normals(triangle_id) -> (DynamicMesh, normal1=Vector, normal2=Vector, normal3=Vector, tri_has_valid_normals=bool)
For the specified TriangleID of the Target Mesh, get the Normal vectors at each vertex of the Triangle.
These Normals will be taken from the Normal Overlay, i.e. they will potentially be split-normals.

Args:
    triangle_id (int32): 

Returns:
    tuple: 

    normal1 (Vector): 

    normal2 (Vector): 

    normal3 (Vector): 

    tri_has_valid_normals (bool): will be returned true if TriangleID exists in TargetMesh and has Normals set.

<a id="unreal.DynamicMesh.get_triangle_indices"></a>

#### get_triangle_indices

```python
def get_triangle_indices(triangle_id: int) -> Tuple[IntVector, bool]
```

x.get_triangle_indices(triangle_id) -> (IntVector, is_valid_triangle=bool)
Returns the Vertex ID triplet for the specified Triangle.

Args:
    triangle_id (int32): indicates the triangle to query on the Target Mesh.

Returns:
    bool: 

    is_valid_triangle (bool): will be false on return if the Triangle ID does not exist in the Target Mesh, in that case the returned vertex triplet will be (-1, -1, -1).

<a id="unreal.DynamicMesh.get_triangle_face_normal"></a>

#### get_triangle_face_normal

```python
def get_triangle_face_normal(triangle_id: int) -> Tuple[Vector, bool]
```

x.get_triangle_face_normal(triangle_id) -> (Vector, is_valid_triangle=bool)
Get Triangle Face Normal

Args:
    triangle_id (int32): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.DynamicMesh.get_num_vertex_i_ds"></a>

#### get_num_vertex_i_ds

```python
def get_num_vertex_i_ds() -> int
```

x.get_num_vertex_i_ds() -> int32
Gets the number of Vertex IDs in the mesh, which may be larger than the Vertex Count, if the mesh is not dense (e.g.  after deleting vertices).

Returns:
    int32:

<a id="unreal.DynamicMesh.get_num_uv_sets"></a>

#### get_num_uv_sets

```python
def get_num_uv_sets() -> int
```

x.get_num_uv_sets() -> int32
Gets the number of UV Channels on the Target Mesh.

Returns:
    int32:

<a id="unreal.DynamicMesh.get_num_uv_islands"></a>

#### get_num_uv_islands

```python
def get_num_uv_islands(uv_channel: int) -> Tuple[int, bool]
```

x.get_num_uv_islands(uv_channel) -> (int32, is_valid_uv_channel=bool)
Returns the number of UV islands in a given UV channel.

Args:
    uv_channel (int32): The UV channel to query

Returns:
    bool: The number of UV islands

    is_valid_uv_channel (bool): True, if the mesh has UVs for the given UVSetIndex.

<a id="unreal.DynamicMesh.get_num_triangle_i_ds"></a>

#### get_num_triangle_i_ds

```python
def get_num_triangle_i_ds() -> int
```

x.get_num_triangle_i_ds() -> int32
Gets the number of Triangle IDs in the mesh. This may be larger than the Triangle Count if the mesh is not dense, even after deleting triangles.

Returns:
    int32:

<a id="unreal.DynamicMesh.get_num_open_border_loops"></a>

#### get_num_open_border_loops

```python
def get_num_open_border_loops() -> Tuple[int, bool]
```

x.get_num_open_border_loops() -> (int32, ambiguous_topology_found=bool)
Returns the number of open border loops, such as "holes" in the mesh.

Returns:
    bool: 

    ambiguous_topology_found (bool):

<a id="unreal.DynamicMesh.get_num_open_border_edges"></a>

#### get_num_open_border_edges

```python
def get_num_open_border_edges() -> int
```

x.get_num_open_border_edges() -> int32
Returns the number of topological boundary edges in the mesh, i.e counts edges that only have one adjacent triangle.

Returns:
    int32:

<a id="unreal.DynamicMesh.get_num_extended_polygroup_layers"></a>

#### get_num_extended_polygroup_layers

```python
def get_num_extended_polygroup_layers() -> int
```

x.get_num_extended_polygroup_layers() -> int32
Returns the count of extended PolyGroup Layers.

Returns:
    int32:

<a id="unreal.DynamicMesh.get_num_connected_components"></a>

#### get_num_connected_components

```python
def get_num_connected_components() -> int
```

x.get_num_connected_components() -> int32
Returns the number of separate connected components in the mesh, such as "triangle patches" internally connected by shared edges.

Returns:
    int32:

<a id="unreal.DynamicMesh.get_mesh_volume_area_center"></a>

#### get_mesh_volume_area_center

```python
def get_mesh_volume_area_center() -> Tuple[float, float, Vector]
```

x.get_mesh_volume_area_center() -> (surface_area=float, volume=float, center_of_mass=Vector)
Computes the volume, area and center-of-mass of the mesh.

Returns:
    tuple: 

    surface_area (float): 

    volume (float): 

    center_of_mass (Vector):

<a id="unreal.DynamicMesh.get_mesh_volume_area"></a>

#### get_mesh_volume_area

```python
def get_mesh_volume_area() -> Tuple[float, float]
```

x.get_mesh_volume_area() -> (surface_area=float, volume=float)
Computes the volume and area of the mesh.

Returns:
    tuple: 

    surface_area (float): 

    volume (float):

<a id="unreal.DynamicMesh.get_mesh_uv_area"></a>

#### get_mesh_uv_area

```python
def get_mesh_uv_area(uv_channel: int) -> Tuple[float, bool]
```

x.get_mesh_uv_area(uv_channel) -> (double, is_valid_uv_channel=bool)
Gets the area of triangles in UV space for the given UV Channel.

Args:
    uv_channel (int32): The UV channel to query

Returns:
    bool: The number of UV islands

    is_valid_uv_channel (bool): True, if the mesh has UVs for the given UVSetIndex.

<a id="unreal.DynamicMesh.get_mesh_info_string"></a>

#### get_mesh_info_string

```python
def get_mesh_info_string() -> str
```

x.get_mesh_info_string() -> str
Returns information about the Target Mesh, such as the vertex and triangle count as well as some attribute information.

Returns:
    str:

<a id="unreal.DynamicMesh.get_mesh_has_attribute_set"></a>

#### get_mesh_has_attribute_set

```python
def get_mesh_has_attribute_set() -> bool
```

x.get_mesh_has_attribute_set() -> bool
Returns true if the Target Mesh has attributes enabled.

Returns:
    bool:

<a id="unreal.DynamicMesh.get_mesh_bounding_box"></a>

#### get_mesh_bounding_box

```python
def get_mesh_bounding_box() -> Box
```

x.get_mesh_bounding_box() -> Box
Computes the bounding box of the mesh vertices in the local space of the mesh.

Returns:
    Box:

<a id="unreal.DynamicMesh.get_is_dense_mesh"></a>

#### get_is_dense_mesh

```python
def get_is_dense_mesh() -> bool
```

x.get_is_dense_mesh() -> bool
Returns true if the mesh is dense. For example, no gaps in Vertex IDs or Triangle IDs.
Note if a mesh is not dense, the Compact Mesh node can be used to removed the gaps.

Returns:
    bool:

<a id="unreal.DynamicMesh.get_is_closed_mesh"></a>

#### get_is_closed_mesh

```python
def get_is_closed_mesh() -> bool
```

x.get_is_closed_mesh() -> bool
Returns true if the mesh is closed, such as no topological boundary edges.

Returns:
    bool:

<a id="unreal.DynamicMesh.get_interpolated_triangle_vertex_color"></a>

#### get_interpolated_triangle_vertex_color

```python
def get_interpolated_triangle_vertex_color(
        triangle_id: int, barycentric_coords: Vector,
        default_color: LinearColor) -> Tuple[DynamicMesh, bool, LinearColor]
```

x.get_interpolated_triangle_vertex_color(triangle_id, barycentric_coords, default_color) -> (DynamicMesh, tri_has_valid_vertex_colors=bool, interpolated_color=LinearColor)
Compute the interpolated Vertex Color (A*Color1 + B*Color2 + C*Color3), where (A,B,C)=BarycentricCoords and the Colors are taken
from the specified TriangleID in the Vertex Color layer of the TargetMesh.

Args:
    triangle_id (int32): 
    barycentric_coords (Vector): 
    default_color (LinearColor): 

Returns:
    tuple: 

    tri_has_valid_vertex_colors (bool): will be returned true if TriangleID exists in TargetMesh and has Colors set, and otherwise will be returned false

    interpolated_color (LinearColor):

<a id="unreal.DynamicMesh.get_interpolated_triangle_uv"></a>

#### get_interpolated_triangle_uv

```python
def get_interpolated_triangle_uv(
        uv_set_index: int, triangle_id: int,
        barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector2D]
```

x.get_interpolated_triangle_uv(uv_set_index, triangle_id, barycentric_coords) -> (DynamicMesh, tri_has_valid_u_vs=bool, interpolated_uv=Vector2D)
Compute the interpolated UV (A*UV1+ B*UV2+ C*UV3), where (A,B,C)=BarycentricCoords and the UV positions are taken
from the specified TriangleID in the specified UVSet of the TargetMesh.

Args:
    uv_set_index (int32): 
    triangle_id (int32): 
    barycentric_coords (Vector): 

Returns:
    tuple: 

    tri_has_valid_u_vs (bool): 

    interpolated_uv (Vector2D):

<a id="unreal.DynamicMesh.get_interpolated_triangle_position"></a>

#### get_interpolated_triangle_position

```python
def get_interpolated_triangle_position(
        triangle_id: int,
        barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector]
```

x.get_interpolated_triangle_position(triangle_id, barycentric_coords) -> (DynamicMesh, is_valid_triangle=bool, interpolated_position=Vector)
Compute the interpolated Position (A*Vertex1 + B*Vertex2 + C*Vertex3), where (A,B,C)=BarycentricCoords and the Vertex positions are taken
from the specified TriangleID of the TargetMesh.

Args:
    triangle_id (int32): 
    barycentric_coords (Vector): 

Returns:
    tuple: 

    is_valid_triangle (bool): will be returned true if TriangleID exists in TargetMesh, and otherwise will be returned false

    interpolated_position (Vector):

<a id="unreal.DynamicMesh.get_interpolated_triangle_normal_tangents"></a>

#### get_interpolated_triangle_normal_tangents

```python
def get_interpolated_triangle_normal_tangents(
    triangle_id: int, barycentric_coords: Vector
) -> Tuple[DynamicMesh, bool, Vector, Vector, Vector]
```

x.get_interpolated_triangle_normal_tangents(triangle_id, barycentric_coords) -> (DynamicMesh, tri_has_valid_elements=bool, interpolated_normal=Vector, interpolated_tangent=Vector, interpolated_bi_tangent=Vector)
Compute the interpolated Normal and Tangents for the specified specified TriangleID in the Normal and Tangent attributes of the TargetMesh.

Args:
    triangle_id (int32): 
    barycentric_coords (Vector): 

Returns:
    tuple: 

    tri_has_valid_elements (bool): will be returned true if TriangleID exists in TargetMesh and has Normals and Tangents set, and otherwise will be returned false

    interpolated_normal (Vector): 

    interpolated_tangent (Vector): 

    interpolated_bi_tangent (Vector):

<a id="unreal.DynamicMesh.get_interpolated_triangle_normal"></a>

#### get_interpolated_triangle_normal

```python
def get_interpolated_triangle_normal(
        triangle_id: int,
        barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector]
```

x.get_interpolated_triangle_normal(triangle_id, barycentric_coords) -> (DynamicMesh, tri_has_valid_normals=bool, interpolated_normal=Vector)
Compute the interpolated Normal (A*Normal1 + B*Normal2 + C*Normal3), where (A,B,C)=BarycentricCoords and the Normals are taken
from the specified TriangleID in the Normal layer of the TargetMesh.

Args:
    triangle_id (int32): 
    barycentric_coords (Vector): 

Returns:
    tuple: 

    tri_has_valid_normals (bool): will be returned true if TriangleID exists in TargetMesh and has Normals set, and otherwise will be returned false.

    interpolated_normal (Vector):

<a id="unreal.DynamicMesh.get_has_vertex_id_gaps"></a>

#### get_has_vertex_id_gaps

```python
def get_has_vertex_id_gaps() -> bool
```

x.get_has_vertex_id_gaps() -> bool
Returns true if there are gaps in the Vertex ID list. For example, Get Number of Vertex IDs is greater than Get Vertex Count.

Returns:
    bool:

<a id="unreal.DynamicMesh.get_has_vertex_colors"></a>

#### get_has_vertex_colors

```python
def get_has_vertex_colors() -> bool
```

x.get_has_vertex_colors() -> bool


Returns:
    bool: true if the TargetMesh has the Vertex Colors attribute enabled

<a id="unreal.DynamicMesh.get_has_triangle_normals"></a>

#### get_has_triangle_normals

```python
def get_has_triangle_normals() -> bool
```

x.get_has_triangle_normals() -> bool


Returns:
    bool: true if the TargetMesh has the Normals Attribute enabled (which allows for storing split normals)

<a id="unreal.DynamicMesh.get_has_triangle_id_gaps"></a>

#### get_has_triangle_id_gaps

```python
def get_has_triangle_id_gaps() -> bool
```

x.get_has_triangle_id_gaps() -> bool
Returns true if there are gaps in the Triangle ID list, such that Get Num Triangle IDs is greater than Get Triangle Count.

Returns:
    bool:

<a id="unreal.DynamicMesh.get_has_polygroups"></a>

#### get_has_polygroups

```python
def get_has_polygroups() -> bool
```

x.get_has_polygroups() -> bool
Returns true if the mesh has a standard PolyGroup Layer.

Returns:
    bool:

<a id="unreal.DynamicMesh.get_has_material_i_ds"></a>

#### get_has_material_i_ds

```python
def get_has_material_i_ds() -> bool
```

x.get_has_material_i_ds() -> bool
Returns true if the mesh has Material IDs available/enabled.

Returns:
    bool:

<a id="unreal.DynamicMesh.get_all_vertex_positions_at_edges"></a>

#### get_all_vertex_positions_at_edges

```python
def get_all_vertex_positions_at_edges(
    edge_i_ds: GeometryScriptIndexList
) -> Tuple[DynamicMesh, GeometryScriptVectorList, GeometryScriptVectorList]
```

x.get_all_vertex_positions_at_edges(edge_i_ds) -> (DynamicMesh, start=GeometryScriptVectorList, end=GeometryScriptVectorList)
Returns the vertex positions for each edge in the given index list.

Args:
    edge_i_ds (GeometryScriptIndexList): The edge IDs to query

Returns:
    tuple: The target mesh that was queried

    start (GeometryScriptVectorList): The output list of start vertex positions

    end (GeometryScriptVectorList): The output list of end vertex positions

<a id="unreal.DynamicMesh.get_all_vertex_positions"></a>

#### get_all_vertex_positions

```python
def get_all_vertex_positions(
        skip_gaps: bool) -> Tuple[DynamicMesh, GeometryScriptVectorList, bool]
```

x.get_all_vertex_positions(skip_gaps) -> (DynamicMesh, position_list=GeometryScriptVectorList, has_vertex_id_gaps=bool)
Returns a Vector List of all the mesh vertex 3D positions (possibly large!).

Args:
    skip_gaps (bool): if false there will be a one-to-one correspondence between Vertex ID and entries in the Position List where a zero vector (0,0,0) will correspond to Vertex IDs not found in the Target Mesh.

Returns:
    tuple: 

    position_list (GeometryScriptVectorList): 

    has_vertex_id_gaps (bool): will be false if the mesh had no gaps in Vertex IDs or if bSkipGaps was set to true.

<a id="unreal.DynamicMesh.get_all_vertex_i_ds"></a>

#### get_all_vertex_i_ds

```python
def get_all_vertex_i_ds() -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

x.get_all_vertex_i_ds() -> (DynamicMesh, vertex_id_list=GeometryScriptIndexList, has_vertex_id_gaps=bool)
Returns an IndexList of all Vertex IDs in mesh.

Returns:
    tuple: 

    vertex_id_list (GeometryScriptIndexList): 

    has_vertex_id_gaps (bool):

<a id="unreal.DynamicMesh.get_all_uv_seam_edges"></a>

#### get_all_uv_seam_edges

```python
def get_all_uv_seam_edges(
        uv_set_index: int
) -> Tuple[DynamicMesh, bool, GeometryScriptIndexList]
```

x.get_all_uv_seam_edges(uv_set_index) -> (DynamicMesh, have_valid_u_vs=bool, element_i_ds=GeometryScriptIndexList)
Returns all edge element IDs that are UV seam edges for a given UV channel.

Args:
    uv_set_index (int32): The UV channel to query

Returns:
    tuple: The target mesh that was queried.

    have_valid_u_vs (bool): True, if the mesh has UVs for the given UVSetIndex.

    element_i_ds (GeometryScriptIndexList): The returned edge element IDs

<a id="unreal.DynamicMesh.get_all_triangle_indices"></a>

#### get_all_triangle_indices

```python
def get_all_triangle_indices(
        skip_gaps: bool
) -> Tuple[DynamicMesh, GeometryScriptTriangleList, bool]
```

x.get_all_triangle_indices(skip_gaps) -> (DynamicMesh, triangle_list=GeometryScriptTriangleList, has_triangle_id_gaps=bool)
* Returns a TriangleList of all Triangle Vertex ID triplets in a mesh.
*

Args:
    skip_gaps (bool): if false there will be a one-to-one correspondence between Triangle ID and entries in the triangle list and invalid triplets of (-1,-1,-1) will correspond to Triangle IDs not found in the Target Mesh. *

Returns:
    tuple: 

    triangle_list (GeometryScriptTriangleList): 

    has_triangle_id_gaps (bool): will be false on return if the mesh had no gaps in Triangle IDs or if bSkipGaps was set to true.

<a id="unreal.DynamicMesh.get_all_triangle_i_ds"></a>

#### get_all_triangle_i_ds

```python
def get_all_triangle_i_ds(
) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

x.get_all_triangle_i_ds() -> (DynamicMesh, triangle_id_list=GeometryScriptIndexList, has_triangle_id_gaps=bool)
Returns an Index List of all Triangle IDs in a mesh.

Returns:
    tuple: 

    triangle_id_list (GeometryScriptIndexList): 

    has_triangle_id_gaps (bool): will be true on return if there are breaks in the sequential numeration of Triangle IDs, as would happen after deleting triangles.

<a id="unreal.DynamicMesh.get_all_split_u_vs_at_vertex"></a>

#### get_all_split_u_vs_at_vertex

```python
def get_all_split_u_vs_at_vertex(
        uv_set_index: int, vertex_id: int
) -> Tuple[DynamicMesh, Array[int], Array[Vector2D], bool]
```

x.get_all_split_u_vs_at_vertex(uv_set_index, vertex_id) -> (DynamicMesh, element_i_ds=Array[int32], element_u_vs=Array[Vector2D], have_valid_u_vs=bool)
Returns the unique UV element IDs and values associated with the mesh vertex, in the specified UV Channel.
If the Vertex or UV channel does not exist, the arrays will be empty and bHaveValidUVs will be set to false.

Args:
    uv_set_index (int32): 
    vertex_id (int32): 

Returns:
    tuple: 

    element_i_ds (Array[int32]): 

    element_u_vs (Array[Vector2D]): 

    have_valid_u_vs (bool):

<a id="unreal.DynamicMesh.compute_triangle_barycentric_coords"></a>

#### compute_triangle_barycentric_coords

```python
def compute_triangle_barycentric_coords(
        triangle_id: int, point: Vector
) -> Tuple[DynamicMesh, bool, Vector, Vector, Vector, Vector]
```

x.compute_triangle_barycentric_coords(triangle_id, point) -> (DynamicMesh, is_valid_triangle=bool, vertex1=Vector, vertex2=Vector, vertex3=Vector, barycentric_coords=Vector)
Compute the barycentric coordinates (A,B,C) of the Point relative to the specified TriangleID of the TargetMesh.
The properties of barycentric coordinates are such that A,B,C are all positive, A+B+C=1.0, and A*Vertex1 + B*Vertex2 + C*Vertex3 = Point.
So, the barycentric coordinates can be used to smoothly interpolate/blend any other per-triangle-vertex quantities.
The Point must lie in the plane of the Triangle, otherwise the coordinates are somewhat meaningless (but clamped to 0-1 range to avoid catastrophic errors)
The Positions of the Triangle Vertices are also returned for convenience (similar to GetTrianglePositions)

Args:
    triangle_id (int32): 
    point (Vector): 

Returns:
    tuple: 

    is_valid_triangle (bool): will be returned true if TriangleID exists in TargetMesh, and otherwise will be returned false

    vertex1 (Vector): 

    vertex2 (Vector): 

    vertex3 (Vector): 

    barycentric_coords (Vector):

<a id="unreal.DynamicMesh.apply_uniform_remesh"></a>

#### apply_uniform_remesh

```python
def apply_uniform_remesh(remesh_options: GeometryScriptRemeshOptions,
                         uniform_options: GeometryScriptUniformRemeshOptions,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_uniform_remesh(remesh_options, uniform_options, debug=None) -> DynamicMesh
Apply Uniform Remeshing to the TargetMesh.
warning: this function can be quite expensive. The results may be non-deterministic, and are expected to change in future versions.

Args:
    remesh_options (GeometryScriptRemeshOptions): 
    uniform_options (GeometryScriptUniformRemeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.weld_mesh_edges"></a>

#### weld_mesh_edges

```python
def weld_mesh_edges(weld_options: GeometryScriptWeldEdgesOptions,
                    debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.weld_mesh_edges(weld_options, debug=None) -> DynamicMesh
Welds any open boundary edges of the mesh together if possible in order to remove "cracks."

Args:
    weld_options (GeometryScriptWeldEdgesOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.split_mesh_bowties"></a>

#### split_mesh_bowties

```python
def split_mesh_bowties(mesh_bowties: bool = True,
                       attribute_bowties: bool = True,
                       debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.split_mesh_bowties(mesh_bowties=True, attribute_bowties=True, debug=None) -> DynamicMesh
Splits Bowties in the mesh and/or the attributes.  A Bowtie is formed when a single vertex is connected to more than two boundary edges,
and splitting duplicates the shared vertex so each triangle will have a unique copy.

Args:
    mesh_bowties (bool): 
    attribute_bowties (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.snap_mesh_open_boundaries"></a>

#### snap_mesh_open_boundaries

```python
def snap_mesh_open_boundaries(
        snap_options: GeometryScriptSnapBoundariesOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.snap_mesh_open_boundaries(snap_options, debug=None) -> DynamicMesh
Snap vertices on open edges to the closest compatible open boundary, if found within the tolerance distance
Unlike ResolveMeshTJunctions, does not introduce new vertices to the mesh

Args:
    snap_options (GeometryScriptSnapBoundariesOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.resolve_mesh_t_junctions"></a>

#### resolve_mesh_t_junctions

```python
def resolve_mesh_t_junctions(
        resolve_options: GeometryScriptResolveTJunctionOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.resolve_mesh_t_junctions(resolve_options, debug=None) -> DynamicMesh
Attempts to resolve T-Junctions in the mesh by addition of vertices and welding.

Args:
    resolve_options (GeometryScriptResolveTJunctionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.repair_mesh_degenerate_geometry"></a>

#### repair_mesh_degenerate_geometry

```python
def repair_mesh_degenerate_geometry(
        options: GeometryScriptDegenerateTriangleOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.repair_mesh_degenerate_geometry(options, debug=None) -> DynamicMesh
Removes triangles that have area or edge length below specified amounts depending on the Options requested.

Args:
    options (GeometryScriptDegenerateTriangleOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.remove_unused_vertices"></a>

#### remove_unused_vertices

```python
def remove_unused_vertices(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.remove_unused_vertices(debug=None) -> DynamicMesh
Remove vertices that are not used by any triangles. Note: Does not update the IDs of any remaining vertices; use CompactMesh to do so.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.remove_small_components"></a>

#### remove_small_components

```python
def remove_small_components(options: GeometryScriptRemoveSmallComponentOptions,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.remove_small_components(options, debug=None) -> DynamicMesh
* Removes connected components of the mesh that have a volume, area, or triangle count below a threshold as specified by the Options.

Args:
    options (GeometryScriptRemoveSmallComponentOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.remove_hidden_triangles"></a>

#### remove_hidden_triangles

```python
def remove_hidden_triangles(
        options: GeometryScriptRemoveHiddenTrianglesOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.remove_hidden_triangles(options, debug=None) -> DynamicMesh
Removes any triangles in the mesh that are not visible from the exterior view, under various definitions of "visible" and "outside"
as specified by the Options.

Args:
    options (GeometryScriptRemoveHiddenTrianglesOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.fill_all_mesh_holes"></a>

#### fill_all_mesh_holes

```python
def fill_all_mesh_holes(
        fill_options: GeometryScriptFillHolesOptions,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int, int]
```

x.fill_all_mesh_holes(fill_options, debug=None) -> (DynamicMesh, num_filled_holes=int32, num_failed_hole_fills=int32)
Tries to fill all open boundary loops (such as holes in the geometry surface) of a mesh.

Args:
    fill_options (GeometryScriptFillHolesOptions): specifies the method used to fill the holes.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    num_filled_holes (int32): reports the number of holes filled by the function.

    num_failed_hole_fills (int32):

<a id="unreal.DynamicMesh.compact_mesh"></a>

#### compact_mesh

```python
def compact_mesh(debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.compact_mesh(debug=None) -> DynamicMesh
Compacts the mesh's vertices and triangles to remove any "holes" in the Vertex ID or Triangle ID lists.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.compute_vertex_weighted_point_sampling"></a>

#### compute_vertex_weighted_point_sampling

```python
def compute_vertex_weighted_point_sampling(
    options: GeometryScriptMeshPointSamplingOptions,
    non_uniform_options: GeometryScriptNonUniformPointSamplingOptions,
    vertex_weights: GeometryScriptScalarList,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[Transform], Array[float],
           GeometryScriptIndexList]
```

x.compute_vertex_weighted_point_sampling(options, non_uniform_options, vertex_weights, debug=None) -> (DynamicMesh, samples=Array[Transform], sample_radii=Array[double], triangle_i_ds=GeometryScriptIndexList)
Compute a set of sample points lying on the surface of TargetMesh based on the provided sampling Options and NonUniformOptions.
The sample points have radii in the range [Options.SamplingRadius, NonUniformOptions.MaxSamplingRadius], and
are non-overlapping, ie the distance between two points is always larger than the sum of their respective radii.

Args:
    options (GeometryScriptMeshPointSamplingOptions): 
    non_uniform_options (GeometryScriptNonUniformPointSamplingOptions): 
    vertex_weights (GeometryScriptScalarList): defines a per-vertex weight in range [0,1], these are interpolated to create a scalar field over the mesh triangles which is used to weight the sampling radii
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    samples (Array[Transform]): 

    sample_radii (Array[double]): 

    triangle_i_ds (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.compute_point_sampling"></a>

#### compute_point_sampling

```python
def compute_point_sampling(
    options: GeometryScriptMeshPointSamplingOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[Transform], GeometryScriptIndexList]
```

x.compute_point_sampling(options, debug=None) -> (DynamicMesh, samples=Array[Transform], triangle_i_ds=GeometryScriptIndexList)
Compute a set of sample points lying on the surface of TargetMesh based on the provided sampling Options.
Samples are approximately uniformly distributed, and non-overlapping relative to the provided Options.SamplingRadius,
ie the distance between any pair of samples if >= 2*SamplingRadius.

Args:
    options (GeometryScriptMeshPointSamplingOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    samples (Array[Transform]): output list of sample points. Transform Location is sample position, Rotation orients Z with the triangle normal

    triangle_i_ds (GeometryScriptIndexList): TriangleID that contains each sample point. Length is the same as Samples array.

<a id="unreal.DynamicMesh.compute_non_uniform_point_sampling"></a>

#### compute_non_uniform_point_sampling

```python
def compute_non_uniform_point_sampling(
    options: GeometryScriptMeshPointSamplingOptions,
    non_uniform_options: GeometryScriptNonUniformPointSamplingOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[Transform], Array[float],
           GeometryScriptIndexList]
```

x.compute_non_uniform_point_sampling(options, non_uniform_options, debug=None) -> (DynamicMesh, samples=Array[Transform], sample_radii=Array[double], triangle_i_ds=GeometryScriptIndexList)
Compute a set of sample points lying on the surface of TargetMesh based on the provided sampling Options and NonUniformOptions.
The sample points have radii in the range [Options.SamplingRadius, NonUniformOptions.MaxSamplingRadius], and
are non-overlapping, ie the distance between two points is always larger than the sum of their respective radii.

Args:
    options (GeometryScriptMeshPointSamplingOptions): 
    non_uniform_options (GeometryScriptNonUniformPointSamplingOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    samples (Array[Transform]): 

    sample_radii (Array[double]): 

    triangle_i_ds (GeometryScriptIndexList):

<a id="unreal.DynamicMesh.select_selection_boundary_edges"></a>

#### select_selection_boundary_edges

```python
def select_selection_boundary_edges(
    selection: GeometryScriptMeshSelection,
    exclude_mesh_boundary_edges: bool = False
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_selection_boundary_edges(selection, exclude_mesh_boundary_edges=False) -> (DynamicMesh, boundary_selection=GeometryScriptMeshSelection)
Create a new BoundarySelection, for the TargetMesh, of the edges on the boundary of another Selection

Args:
    selection (GeometryScriptMeshSelection): 
    exclude_mesh_boundary_edges (bool): If true, do not include Selection boundary edges if they are also mesh boundary edges

Returns:
    GeometryScriptMeshSelection: 

    boundary_selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_sharp_edges"></a>

#### select_mesh_sharp_edges

```python
def select_mesh_sharp_edges(
    min_angle_deg: float = 20.000000
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_sharp_edges(min_angle_deg=20.000000) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Selection, for the TargetMesh, of all 'sharp' edges where the edge's adjacent triangle normals differ by at least MinAngleDeg

Args:
    min_angle_deg (double): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_elements_with_plane"></a>

#### select_mesh_elements_with_plane

```python
def select_mesh_elements_with_plane(
    plane_origin: Vector = [0.000000, 0.000000, 0.000000],
    plane_normal: Vector = [0.000000, 0.000000, 1.000000],
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_elements_with_plane(plane_origin=[0.000000, 0.000000, 0.000000], plane_normal=[0.000000, 0.000000, 1.000000], selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements on the "positive" side of a Plane

Args:
    plane_origin (Vector): center point of the Plane
    plane_normal (Vector): normal vector for the Plane
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements on the other (negative) side of the Plane
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_elements_in_sphere"></a>

#### select_mesh_elements_in_sphere

```python
def select_mesh_elements_in_sphere(
    sphere_origin: Vector = [0.000000, 0.000000, 0.000000],
    sphere_radius: float = 100.000000,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_elements_in_sphere(sphere_origin=[0.000000, 0.000000, 0.000000], sphere_radius=100.000000, selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements contained in the Sphere.

Args:
    sphere_origin (Vector): center point of the Sphere
    sphere_radius (double): radius of the Sphere
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements not in the Sphere
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_elements_inside_mesh"></a>

#### select_mesh_elements_inside_mesh

```python
def select_mesh_elements_inside_mesh(
    selection_mesh: DynamicMesh,
    selection_mesh_transform: Transform,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    shell_distance: float = 0.000000,
    winding_threshold: float = 0.500000,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_elements_inside_mesh(selection_mesh, selection_mesh_transform, selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, shell_distance=0.000000, winding_threshold=0.500000, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements inside a second SelectionMesh
For Triangle and PolyGroup selections the triangle facet normal is used, for Vertex selections the per-vertex averaged normal is used.

Args:
    selection_mesh (DynamicMesh): 
    selection_mesh_transform (Transform): Transform applied to SelectionMesh for inside/outside testing
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements not within the given deviation
    shell_distance (double): If > 0, points within this distance from SelectionMesh will also be considered "inside"
    winding_threshold (double): Threshold used for Fast Mesh Winding Number inside/outside test (range is [0,1], with 1 being "inside")
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_elements_in_box"></a>

#### select_mesh_elements_in_box

```python
def select_mesh_elements_in_box(
    box: Box,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_elements_in_box(box, selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements contained in the Box.

Args:
    box (Box): 
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements not in the Box
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_elements_by_polygroup"></a>

#### select_mesh_elements_by_polygroup

```python
def select_mesh_elements_by_polygroup(
    group_layer: GeometryScriptGroupLayer,
    polygroup_id: int,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_elements_by_polygroup(group_layer, polygroup_id, selection_type=GeometryScriptMeshSelectionType.TRIANGLES) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Selection of the SelectionType that contains all mesh elements referencing triangles with the given PolyGroup ID in the given GroupLayer

Args:
    group_layer (GeometryScriptGroupLayer): 
    polygroup_id (int32): 
    selection_type (GeometryScriptMeshSelectionType): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_elements_by_normal_angle"></a>

#### select_mesh_elements_by_normal_angle

```python
def select_mesh_elements_by_normal_angle(
    normal: Vector = [0.000000, 0.000000, 1.000000],
    max_angle_deg: float = 1.000000,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_elements_by_normal_angle(normal=[0.000000, 0.000000, 1.000000], max_angle_deg=1.000000, selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements that have a normal
vector that is within an angular deviation threshold from the given Normal.
For Triangle and PolyGroup selections the triangle facet normal is used, for Vertex selections the per-vertex averaged normal is used.

Args:
    normal (Vector): normal/direction vector to measure against
    max_angle_deg (double): maximum angular deviation from Normal, in degrees
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements not within the given deviation
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_elements_by_material_id"></a>

#### select_mesh_elements_by_material_id

```python
def select_mesh_elements_by_material_id(
    material_id: int,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_elements_by_material_id(material_id, selection_type=GeometryScriptMeshSelectionType.TRIANGLES) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Selection of the SelectionType that contains all mesh elements referencing triangles with the given Material ID

Args:
    material_id (int32): 
    selection_type (GeometryScriptMeshSelectionType): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.select_mesh_boundary_edges"></a>

#### select_mesh_boundary_edges

```python
def select_mesh_boundary_edges(
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_boundary_edges() -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Selection, for the TargetMesh, of all mesh boundary edges

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.invert_mesh_selection"></a>

#### invert_mesh_selection

```python
def invert_mesh_selection(
    selection: GeometryScriptMeshSelection,
    only_to_connected: bool = False
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.invert_mesh_selection(selection, only_to_connected=False) -> (DynamicMesh, new_selection=GeometryScriptMeshSelection)
Invert the Selection on the TargetMesh, ie select what is not currently selected

Args:
    selection (GeometryScriptMeshSelection): 
    only_to_connected (bool): if true, the inverse is limited to mesh areas geometrically connected to the Selection, instead of the entire mesh

Returns:
    GeometryScriptMeshSelection: 

    new_selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.get_mesh_unique_selection_info"></a>

#### get_mesh_unique_selection_info

```python
def get_mesh_unique_selection_info(
    selection: GeometryScriptMeshSelection
) -> Tuple[GeometryScriptMeshSelectionType, int]
```

x.get_mesh_unique_selection_info(selection) -> (selection_type=GeometryScriptMeshSelectionType, num_selected=int32)
Query information about a Mesh Selection, and get a count of unique selected elements

Args:
    selection (GeometryScriptMeshSelection): 

Returns:
    tuple: 

    selection_type (GeometryScriptMeshSelectionType): 

    num_selected (int32):

<a id="unreal.DynamicMesh.expand_mesh_selection_to_connected"></a>

#### expand_mesh_selection_to_connected

```python
def expand_mesh_selection_to_connected(
    selection: GeometryScriptMeshSelection,
    connection_type:
    GeometryScriptTopologyConnectionType = GeometryScriptTopologyConnectionType
    .GEOMETRIC
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.expand_mesh_selection_to_connected(selection, connection_type=GeometryScriptTopologyConnectionType.GEOMETRIC) -> (DynamicMesh, new_selection=GeometryScriptMeshSelection)
Expand the Selection on the TargetMesh to connected regions and return the NewSelection

Args:
    selection (GeometryScriptMeshSelection): 
    connection_type (GeometryScriptTopologyConnectionType): defines what "connected" means, ie purely geometric connection, or some additional constraint like same MaterialIDs/etc

Returns:
    GeometryScriptMeshSelection: 

    new_selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.expand_contract_mesh_selection"></a>

#### expand_contract_mesh_selection

```python
def expand_contract_mesh_selection(
    selection: GeometryScriptMeshSelection,
    iterations: int = 1,
    contract: bool = False,
    only_expand_to_face_neighbours: bool = False
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.expand_contract_mesh_selection(selection, iterations=1, contract=False, only_expand_to_face_neighbours=False) -> (DynamicMesh, new_selection=GeometryScriptMeshSelection)
Grow or Shrink the Selection on the TargetMesh to connected neighbours.
For Vertex selections, Expand includes vertices in one-ring of selected vertices, and Contract removes any vertices with a one-ring neighbour that is not selected
For Triangle selections, Add/Remove Triangles connected to selected Triangles
For PolyGroup selections, Add/Remove PolyGroups connected to selected PolyGroups

Args:
    selection (GeometryScriptMeshSelection): 
    iterations (int32): number of times to Expand/Contract the Selection. Valid range is [0,100] where 0 is a no-op.
    contract (bool): if true selection contracts instead of growing
    only_expand_to_face_neighbours (bool): if true, only adjacent Triangles/PolyGroups directly connected by an edge are added, vs connected to any selected vertex

Returns:
    GeometryScriptMeshSelection: 

    new_selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.create_select_all_mesh_selection"></a>

#### create_select_all_mesh_selection

```python
def create_select_all_mesh_selection(
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.create_select_all_mesh_selection(selection_type=GeometryScriptMeshSelectionType.TRIANGLES) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Selection of the given SelectionType that contains all the mesh elements of TargetMesh

Args:
    selection_type (GeometryScriptMeshSelectionType): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.convert_mesh_selection_to_index_list"></a>

#### convert_mesh_selection_to_index_list

```python
def convert_mesh_selection_to_index_list(
    selection: GeometryScriptMeshSelection,
    convert_to_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY
) -> Tuple[DynamicMesh, GeometryScriptIndexList, GeometryScriptIndexType]
```

x.convert_mesh_selection_to_index_list(selection, convert_to_type=GeometryScriptIndexType.ANY) -> (DynamicMesh, index_list=GeometryScriptIndexList, result_list_type=GeometryScriptIndexType)
Convert a Mesh Selection to an Index List

Args:
    selection (GeometryScriptMeshSelection): 
    convert_to_type (GeometryScriptIndexType): optional parameter specifying the type of Index List to convert to. If Set to Any, no conversion will be performed.

Returns:
    tuple: 

    index_list (GeometryScriptIndexList): 

    result_list_type (GeometryScriptIndexType):

<a id="unreal.DynamicMesh.convert_mesh_selection_to_index_array"></a>

#### convert_mesh_selection_to_index_array

```python
def convert_mesh_selection_to_index_array(
    selection: GeometryScriptMeshSelection
) -> Tuple[DynamicMesh, Array[int], GeometryScriptMeshSelectionType]
```

x.convert_mesh_selection_to_index_array(selection) -> (DynamicMesh, index_array=Array[int32], selection_type=GeometryScriptMeshSelectionType)
Convert a Mesh Selection to an Index Array

Args:
    selection (GeometryScriptMeshSelection): 

Returns:
    tuple: 

    index_array (Array[int32]): 

    selection_type (GeometryScriptMeshSelectionType):

<a id="unreal.DynamicMesh.convert_mesh_selection"></a>

#### convert_mesh_selection

```python
def convert_mesh_selection(
    from_selection: GeometryScriptMeshSelection,
    new_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType
    .TRIANGLES,
    allow_partial_inclusion: bool = True
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.convert_mesh_selection(from_selection, new_type=GeometryScriptMeshSelectionType.TRIANGLES, allow_partial_inclusion=True) -> (DynamicMesh, to_selection=GeometryScriptMeshSelection)
Convert a Mesh Selection to a different Type (eg Vertices to Triangles, etc)
By default, Vertices map to Triangle one-rings, and Triangles to all contained vertices.
If bAllowPartialInclusion is disabled, then more restrictive conversions are performed, as follows:
  For To-Vertices, only include vertices where all one-ring triangles or edges are included in FromSelection.
  For To-Edges, only include edges where all adjacent triangles or vertices are included in FromSelection
  For To-Triangles, only include triangles where all tri vertices or edges are included in FromSelection.
  For To-PolyGroups, only include groups where all group triangles are touched by FromSelection
(Note: The To-PolyGroups rule allows vertex and edge selections that miss some vertices or edges, as long as they touch all the polygroup triangles.)

Args:
    from_selection (GeometryScriptMeshSelection): 
    new_type (GeometryScriptMeshSelectionType): 
    allow_partial_inclusion (bool): if false, perform more limited selection conversion as described above

Returns:
    GeometryScriptMeshSelection: 

    to_selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.convert_index_set_to_mesh_selection"></a>

#### convert_index_set_to_mesh_selection

```python
def convert_index_set_to_mesh_selection(
    index_set: Set[int], selection_type: GeometryScriptMeshSelectionType
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.convert_index_set_to_mesh_selection(index_set, selection_type) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Mesh Selection from the IndexSet.

Args:
    index_set (Set[int32]): 
    selection_type (GeometryScriptMeshSelectionType): type of indices specified in the selection

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.convert_index_list_to_mesh_selection"></a>

#### convert_index_list_to_mesh_selection

```python
def convert_index_list_to_mesh_selection(
    index_list: GeometryScriptIndexList,
    selection_type: GeometryScriptMeshSelectionType
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.convert_index_list_to_mesh_selection(index_list, selection_type) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Mesh Selection from the Index List. For cases where the IndexList Type does not match
the SelectionType, ConvertMeshSelection with bAllowPartialInclusion=true is used to convert.

Args:
    index_list (GeometryScriptIndexList): 
    selection_type (GeometryScriptMeshSelectionType): type of indices desired in the Output selection

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.convert_index_array_to_mesh_selection"></a>

#### convert_index_array_to_mesh_selection

```python
def convert_index_array_to_mesh_selection(
    index_array: Array[int], selection_type: GeometryScriptMeshSelectionType
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.convert_index_array_to_mesh_selection(index_array, selection_type) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Mesh Selection from the IndexArray.

Args:
    index_array (Array[int32]): 
    selection_type (GeometryScriptMeshSelectionType): type of indices specified in the selection

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.get_mesh_selection_bounding_box"></a>

#### get_mesh_selection_bounding_box

```python
def get_mesh_selection_bounding_box(
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Box, bool]
```

x.get_mesh_selection_bounding_box(selection, debug=None) -> (DynamicMesh, selection_bounds=Box, is_empty=bool)
Get the 3D Bounding Box of a Mesh Selection, ie bounding box of vertices contained in the Selection

Args:
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    selection_bounds (Box): 

    is_empty (bool): will return as true if the selection was empty (the box will be initialized to 0 in this case)

<a id="unreal.DynamicMesh.get_mesh_selection_boundary_loops"></a>

#### get_mesh_selection_boundary_loops

```python
def get_mesh_selection_boundary_loops(
    selection: GeometryScriptMeshSelection,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[GeometryScriptIndexList],
           Array[GeometryScriptPolyPath], int, bool]
```

x.get_mesh_selection_boundary_loops(selection, debug=None) -> (DynamicMesh, index_loops=Array[GeometryScriptIndexList], path_loops=Array[GeometryScriptPolyPath], num_loops=int32, found_errors=bool)
Compute the set of Vertex Loops bordering a Mesh Selection. Both the 3D polylines and lists of vertex indices are returned for each Loop.
Note that for a Vertex selection this will function return the border loops around the set of vertex triangle one-rings.

Args:
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    index_loops (Array[GeometryScriptIndexList]): for each discovered Loop, the IndexList of mesh vertex indices around the loop is returned here

    path_loops (Array[GeometryScriptPolyPath]): for each discovered Loop, the PolyPath of mesh vertex positions around the loop is returned here. The ordering for each loop is the same as IndexLoops.

    num_loops (int32): number of loops found is returned here

    found_errors (bool): true is returned here if topological errors were found during loop computation. In this case the Loop set may be incomplete.

<a id="unreal.DynamicMesh.apply_simplify_to_vertex_count"></a>

#### apply_simplify_to_vertex_count

```python
def apply_simplify_to_vertex_count(
        vertex_count: int,
        options: GeometryScriptSimplifyMeshOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_simplify_to_vertex_count(vertex_count, options, debug=None) -> DynamicMesh
Simplifies the mesh until a target vertex count is reached. Behavior can be additionally controlled with the Options.

Args:
    vertex_count (int32): 
    options (GeometryScriptSimplifyMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_simplify_to_triangle_count"></a>

#### apply_simplify_to_triangle_count

```python
def apply_simplify_to_triangle_count(
        triangle_count: int,
        options: GeometryScriptSimplifyMeshOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_simplify_to_triangle_count(triangle_count, options, debug=None) -> DynamicMesh
Simplifies the mesh until a target triangle count is reached. Behavior can be additionally controlled with the Options.

Args:
    triangle_count (int32): 
    options (GeometryScriptSimplifyMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_simplify_to_tolerance"></a>

#### apply_simplify_to_tolerance

```python
def apply_simplify_to_tolerance(
        tolerance: float,
        options: GeometryScriptSimplifyMeshOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_simplify_to_tolerance(tolerance, options, debug=None) -> DynamicMesh
Simplifies the mesh to a target geometric tolerance. Stops when any further simplification would result in a deviation from the input mesh larger than the tolerance.
Behavior can be additionally controlled with the Options.

Args:
    tolerance (float): 
    options (GeometryScriptSimplifyMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_simplify_to_polygroup_topology"></a>

#### apply_simplify_to_polygroup_topology

```python
def apply_simplify_to_polygroup_topology(
        options: GeometryScriptPolygroupSimplifyOptions,
        group_layer: GeometryScriptGroupLayer,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_simplify_to_polygroup_topology(options, group_layer, debug=None) -> DynamicMesh
Simplifies the mesh down to the PolyGroup Topology. For example, the high-level faces of the mesh PolyGroups.
Another example would be on a default Box-Sphere where simplifying to PolyGroup topology produces a box.

Args:
    options (GeometryScriptPolygroupSimplifyOptions): 
    group_layer (GeometryScriptGroupLayer): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_simplify_to_planar"></a>

#### apply_simplify_to_planar

```python
def apply_simplify_to_planar(options: GeometryScriptPlanarSimplifyOptions,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_simplify_to_planar(options, debug=None) -> DynamicMesh
Simplifies planar areas of the mesh that have more triangles than necessary. Note that it does not change the 3D shape of the mesh.
Planar regions are identified by comparison of face normals using a Angle Threshold in the Options.

Args:
    options (GeometryScriptPlanarSimplifyOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.select_mesh_elements_in_box_with_bvh"></a>

#### select_mesh_elements_in_box_with_bvh

```python
def select_mesh_elements_in_box_with_bvh(
    query_bvh: GeometryScriptDynamicMeshBVH,
    query_box: Box,
    options: GeometryScriptSpatialQueryOptions,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.VERTICES,
    min_num_triangle_points: int = 3,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

x.select_mesh_elements_in_box_with_bvh(query_bvh, query_box, options, selection_type=GeometryScriptMeshSelectionType.VERTICES, min_num_triangle_points=3, debug=None) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create Mesh Selection of mesh elements in TargetMesh contained by QueryBox, using QueryBVH to accellerate the computation.
Triangles and Edges are selected if Min Element Vertices (clamped to a 1-3 or 1-2 range, for triangles or edges respectively) or more are inside the box.
PolyGroups are selected if any of their triangles are inside the box

Note that this method cannot select mesh elements that cut through the query box without having any vertices in the query box.

Args:
    query_bvh (GeometryScriptDynamicMeshBVH): is an acceleration structure previously built with TargetMesh.
    query_box (Box): 
    options (GeometryScriptSpatialQueryOptions): control the fast winding number threshold
    selection_type (GeometryScriptMeshSelectionType): 
    min_num_triangle_points (int32): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.DynamicMesh.rebuild_bvh_for_mesh"></a>

#### rebuild_bvh_for_mesh

```python
def rebuild_bvh_for_mesh(
    update_bvh: GeometryScriptDynamicMeshBVH,
    only_if_invalid: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptDynamicMeshBVH]
```

x.rebuild_bvh_for_mesh(update_bvh, only_if_invalid=True, debug=None) -> (DynamicMesh, update_bvh=GeometryScriptDynamicMeshBVH)
Rebuilds the Bounding Volume Hierarchy (BVH) for the mesh in-place, which can reduce memory allocations, compared to building a new BVH.

Args:
    update_bvh (GeometryScriptDynamicMeshBVH): 
    only_if_invalid (bool): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptDynamicMeshBVH: 

    update_bvh (GeometryScriptDynamicMeshBVH):

<a id="unreal.DynamicMesh.is_point_inside_mesh"></a>

#### is_point_inside_mesh

```python
def is_point_inside_mesh(
    query_bvh: GeometryScriptDynamicMeshBVH,
    query_point: Vector,
    options: GeometryScriptSpatialQueryOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, bool, GeometryScriptContainmentOutcomePins]
```

x.is_point_inside_mesh(query_bvh, query_point, options, debug=None) -> (DynamicMesh, is_inside=bool, outcome=GeometryScriptContainmentOutcomePins)
Tests if a point is inside the mesh using the Fast Winding Number query and data stored in the BVH.

Args:
    query_bvh (GeometryScriptDynamicMeshBVH): is an acceleration structure previously built with this mesh.
    query_point (Vector): the point in the mesh's 3D local space.
    options (GeometryScriptSpatialQueryOptions): control the fast winding number threshold
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_inside (bool): 

    outcome (GeometryScriptContainmentOutcomePins):

<a id="unreal.DynamicMesh.is_bvh_valid_for_mesh"></a>

#### is_bvh_valid_for_mesh

```python
def is_bvh_valid_for_mesh(
        test_bvh: GeometryScriptDynamicMeshBVH,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

x.is_bvh_valid_for_mesh(test_bvh, debug=None) -> (DynamicMesh, is_valid=bool)
Checks if the provided Bounding Volume Hierarchy (BVH) can still be used with the Mesh — it generally returns false if the mesh has been changed.

Args:
    test_bvh (GeometryScriptDynamicMeshBVH): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.DynamicMesh.find_nearest_ray_intersection_with_mesh"></a>

#### find_nearest_ray_intersection_with_mesh

```python
def find_nearest_ray_intersection_with_mesh(
    query_bvh: GeometryScriptDynamicMeshBVH,
    ray_origin: Vector,
    ray_direction: Vector,
    options: GeometryScriptSpatialQueryOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptRayHitResult,
           GeometryScriptSearchOutcomePins]
```

x.find_nearest_ray_intersection_with_mesh(query_bvh, ray_origin, ray_direction, options, debug=None) -> (DynamicMesh, hit_result=GeometryScriptRayHitResult, outcome=GeometryScriptSearchOutcomePins)
Finds the nearest intersection of a 3D ray with the mesh by using the Query BVH.
Note, depending on the Ray Origin and Ray Direction, there is the possibility that the ray might not intersect with the Target Mesh.
Should the ray miss, the HitResult.bHit will be false and the Outcome  will be Not Found.

Args:
    query_bvh (GeometryScriptDynamicMeshBVH): 
    ray_origin (Vector): 
    ray_direction (Vector): 
    options (GeometryScriptSpatialQueryOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    hit_result (GeometryScriptRayHitResult): 

    outcome (GeometryScriptSearchOutcomePins):

<a id="unreal.DynamicMesh.find_nearest_point_on_mesh"></a>

#### find_nearest_point_on_mesh

```python
def find_nearest_point_on_mesh(
    query_bvh: GeometryScriptDynamicMeshBVH,
    query_point: Vector,
    options: GeometryScriptSpatialQueryOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptTrianglePoint,
           GeometryScriptSearchOutcomePins]
```

x.find_nearest_point_on_mesh(query_bvh, query_point, options, debug=None) -> (DynamicMesh, nearest_result=GeometryScriptTrianglePoint, outcome=GeometryScriptSearchOutcomePins)
Finds the nearest point (Nearest Result) on the Target Mesh to a given 3D point (Query Point) by using the Query BVH.

Args:
    query_bvh (GeometryScriptDynamicMeshBVH): a BVH associated with the Target Mesh
    query_point (Vector): a 3D location relative to the local space of the mesh
    options (GeometryScriptSpatialQueryOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    nearest_result (GeometryScriptTrianglePoint): on return, holds the nearest point on the mesh to the QueryPoint

    outcome (GeometryScriptSearchOutcomePins): will be either Found or Not Found depending on the success of the query. Note NearestResult.bValid will be false if the query failed.

<a id="unreal.DynamicMesh.build_bvh_for_mesh"></a>

#### build_bvh_for_mesh

```python
def build_bvh_for_mesh(
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptDynamicMeshBVH]
```

x.build_bvh_for_mesh(debug=None) -> (DynamicMesh, output_bvh=GeometryScriptDynamicMeshBVH)
Builds a Bounding Volume Hierarchy (BVH) object for a mesh that can be used with multiple spatial queries.

Args:
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptDynamicMeshBVH: 

    output_bvh (GeometryScriptDynamicMeshBVH):

<a id="unreal.DynamicMesh.apply_uniform_tessellation"></a>

#### apply_uniform_tessellation

```python
def apply_uniform_tessellation(
        tessellation_level: int = 3,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_uniform_tessellation(tessellation_level=3, debug=None) -> DynamicMesh
Apply Uniform Tessellation to the Target Mesh as controlled by the Tessellation Level and the Options.

Args:
    tessellation_level (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_selective_tessellation"></a>

#### apply_selective_tessellation

```python
def apply_selective_tessellation(
        selection: GeometryScriptMeshSelection,
        options: GeometryScriptSelectiveTessellateOptions,
        tessellation_level: int = 1,
        pattern_type:
    SelectiveTessellatePatternType = SelectiveTessellatePatternType.
    CONCENTRIC_RINGS,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_selective_tessellation(selection, options, tessellation_level=1, pattern_type=SelectiveTessellatePatternType.CONCENTRIC_RINGS, debug=None) -> DynamicMesh
Selectively Tessellate a Selection of the Target Mesh or possibly the entire mesh as controlled by
the Options.

Args:
    selection (GeometryScriptMeshSelection): selects the triangles of the mesh to be tessellated.
    options (GeometryScriptSelectiveTessellateOptions): controls the behavior of the tessellation if the Selection is empty.
    tessellation_level (int32): determines the amount of tessellation
    pattern_type (SelectiveTessellatePatternType): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_pn_tessellation"></a>

#### apply_pn_tessellation

```python
def apply_pn_tessellation(options: GeometryScriptPNTessellateOptions,
                          tessellation_level: int = 3,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_pn_tessellation(options, tessellation_level=3, debug=None) -> DynamicMesh
Apply PN Tessellation to the Target Mesh as controlled by the Tessellation Level and the Options.

Args:
    options (GeometryScriptPNTessellateOptions): 
    tessellation_level (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.translate_pivot_to_location"></a>

#### translate_pivot_to_location

```python
def translate_pivot_to_location(
        pivot_location: Vector,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.translate_pivot_to_location(pivot_location, debug=None) -> DynamicMesh
Set the Pivot Location for the Mesh. Since the Pivot of a Mesh object is always the point at (0,0,0),
this function simply translates the mesh by -PivotLocation.

Args:
    pivot_location (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.translate_mesh_selection"></a>

#### translate_mesh_selection

```python
def translate_mesh_selection(selection: GeometryScriptMeshSelection,
                             translation: Vector,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.translate_mesh_selection(selection, translation, debug=None) -> DynamicMesh
Applies the given Translation to the vertices identified by the Selection of the mesh.

Args:
    selection (GeometryScriptMeshSelection): 
    translation (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.translate_mesh"></a>

#### translate_mesh

```python
def translate_mesh(translation: Vector,
                   debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.translate_mesh(translation, debug=None) -> DynamicMesh
Applies the provided Translation to the vertices of a Mesh.

Args:
    translation (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.transform_mesh_selection"></a>

#### transform_mesh_selection

```python
def transform_mesh_selection(selection: GeometryScriptMeshSelection,
                             transform: Transform,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.transform_mesh_selection(selection, transform, debug=None) -> DynamicMesh
Applies the given Transform to the vertices identified by the Selection of the mesh.

Args:
    selection (GeometryScriptMeshSelection): 
    transform (Transform): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.transform_mesh"></a>

#### transform_mesh

```python
def transform_mesh(transform: Transform,
                   fix_orientation_for_negative_scale: bool = True,
                   debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.transform_mesh(transform, fix_orientation_for_negative_scale=True, debug=None) -> DynamicMesh
Applies the provided Transform to the vertices of a Mesh.

Args:
    transform (Transform): 
    fix_orientation_for_negative_scale (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.scale_mesh_selection"></a>

#### scale_mesh_selection

```python
def scale_mesh_selection(selection: GeometryScriptMeshSelection,
                         scale: Vector = [1.000000, 1.000000, 1.000000],
                         scale_origin: Vector = [0.000000, 0.000000, 0.000000],
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.scale_mesh_selection(selection, scale=[1.000000, 1.000000, 1.000000], scale_origin=[0.000000, 0.000000, 0.000000], debug=None) -> DynamicMesh
Applies the given Scale transform relative to the Scale Origin to the selection part of the mesh.

Args:
    selection (GeometryScriptMeshSelection): 
    scale (Vector): 
    scale_origin (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.scale_mesh"></a>

#### scale_mesh

```python
def scale_mesh(scale: Vector = [1.000000, 1.000000, 1.000000],
               scale_origin: Vector = [0.000000, 0.000000, 0.000000],
               fix_orientation_for_negative_scale: bool = True,
               debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.scale_mesh(scale=[1.000000, 1.000000, 1.000000], scale_origin=[0.000000, 0.000000, 0.000000], fix_orientation_for_negative_scale=True, debug=None) -> DynamicMesh
Applies the provided Scale transformation relative to the Scale Origin to the vertices of a Mesh.

Args:
    scale (Vector): 
    scale_origin (Vector): 
    fix_orientation_for_negative_scale (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.rotate_mesh_selection"></a>

#### rotate_mesh_selection

```python
def rotate_mesh_selection(selection: GeometryScriptMeshSelection,
                          rotation: Rotator,
                          rotation_origin: Vector = [
                              0.000000, 0.000000, 0.000000
                          ],
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.rotate_mesh_selection(selection, rotation, rotation_origin=[0.000000, 0.000000, 0.000000], debug=None) -> DynamicMesh
Rotates the selected part of the mesh relative to the specified Rotation Origin.

Args:
    selection (GeometryScriptMeshSelection): 
    rotation (Rotator): 
    rotation_origin (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.rotate_mesh"></a>

#### rotate_mesh

```python
def rotate_mesh(rotation: Rotator,
                rotation_origin: Vector = [0.000000, 0.000000, 0.000000],
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.rotate_mesh(rotation, rotation_origin=[0.000000, 0.000000, 0.000000], debug=None) -> DynamicMesh
Rotates the mesh relative to the specified Rotation Origin.

Args:
    rotation (Rotator): 
    rotation_origin (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.translate_mesh_u_vs"></a>

#### translate_mesh_u_vs

```python
def translate_mesh_u_vs(uv_set_index: int,
                        translation: Vector2D,
                        selection: GeometryScriptMeshSelection,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.translate_mesh_u_vs(uv_set_index, translation, selection, debug=None) -> DynamicMesh
Update all selected UV values in the specified UV Channel by adding the Translation value to each.
If the provided Selection is empty, the Translation is applied to the entire UV Channel.

Args:
    uv_set_index (int32): 
    translation (Vector2D): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_uv_seams_along_selected_edges"></a>

#### set_uv_seams_along_selected_edges

```python
def set_uv_seams_along_selected_edges(
        uv_channel: int,
        selection: GeometryScriptMeshSelection,
        insert_seams: bool = True,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_uv_seams_along_selected_edges(uv_channel, selection, insert_seams=True, defer_change_notifications=False, debug=None) -> DynamicMesh
Convert Selection to an Edge selection, and set or remove UV seams along all of the selected edges

Args:
    uv_channel (int32): The UV Channel to update
    selection (GeometryScriptMeshSelection): Which edges to operate on
    insert_seams (bool): Whether to insert new seams. If false, removes existing seams instead.
    defer_change_notifications (bool): If true, no mesh change notification will be sent. Set to true if performing many changes in a loop.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_num_uv_sets"></a>

#### set_num_uv_sets

```python
def set_num_uv_sets(num_uv_sets: int,
                    debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_num_uv_sets(num_uv_sets, debug=None) -> DynamicMesh
Set the number of UV Channels on the Target Mesh. If not already enabled, this will enable the mesh attributes.

Args:
    num_uv_sets (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_mesh_u_vs_from_planar_projection"></a>

#### set_mesh_u_vs_from_planar_projection

```python
def set_mesh_u_vs_from_planar_projection(
        uv_set_index: int,
        plane_transform: Transform,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_mesh_u_vs_from_planar_projection(uv_set_index, plane_transform, selection, debug=None) -> DynamicMesh
Scale of PlaneTransform defines world-space dimension that maps to 1 UV dimension

Args:
    uv_set_index (int32): 
    plane_transform (Transform): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_mesh_u_vs_from_cylinder_projection"></a>

#### set_mesh_u_vs_from_cylinder_projection

```python
def set_mesh_u_vs_from_cylinder_projection(
        uv_set_index: int,
        cylinder_transform: Transform,
        selection: GeometryScriptMeshSelection,
        split_angle: float = 45.000000,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_mesh_u_vs_from_cylinder_projection(uv_set_index, cylinder_transform, selection, split_angle=45.000000, debug=None) -> DynamicMesh
Using Cylinder Projection, update the UVs in the UV Channel for an entire mesh or a subset defined by a non-empty Selection.

Args:
    uv_set_index (int32): 
    cylinder_transform (Transform): 
    selection (GeometryScriptMeshSelection): 
    split_angle (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_mesh_u_vs_from_box_projection"></a>

#### set_mesh_u_vs_from_box_projection

```python
def set_mesh_u_vs_from_box_projection(
        uv_set_index: int,
        box_transform: Transform,
        selection: GeometryScriptMeshSelection,
        min_island_tri_count: int = 2,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_mesh_u_vs_from_box_projection(uv_set_index, box_transform, selection, min_island_tri_count=2, debug=None) -> DynamicMesh
Using Box Projection, update the UVs in the UV Channel for an entire mesh or a subset defined by a non-empty Selection.

Args:
    uv_set_index (int32): 
    box_transform (Transform): 
    selection (GeometryScriptMeshSelection): 
    min_island_tri_count (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_mesh_uv_element_position"></a>

#### set_mesh_uv_element_position

```python
def set_mesh_uv_element_position(
        uv_set_index: int,
        element_id: int,
        new_uv_position: Vector2D,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.set_mesh_uv_element_position(uv_set_index, element_id, new_uv_position, defer_change_notifications=False) -> (DynamicMesh, is_valid_element_id=bool)
Sets the UV position of a specific ElementID in the given UV Set/Channel
If the UV Set or Element ID does not exist, bIsValidElementID will be returned as false.

Args:
    uv_set_index (int32): 
    element_id (int32): 
    new_uv_position (Vector2D): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_element_id (bool):

<a id="unreal.DynamicMesh.set_mesh_triangle_u_vs"></a>

#### set_mesh_triangle_u_vs

```python
def set_mesh_triangle_u_vs(
        uv_set_index: int,
        triangle_id: int,
        u_vs: GeometryScriptUVTriangle,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.set_mesh_triangle_u_vs(uv_set_index, triangle_id, u_vs, defer_change_notifications=False) -> (DynamicMesh, is_valid_triangle=bool)
Sets the UVs of a mesh triangle in the given UV Channel.
This function will create new UV elements for each vertex of the triangle, meaning that
the triangle will become an isolated UV island.

Args:
    uv_set_index (int32): 
    triangle_id (int32): 
    u_vs (GeometryScriptUVTriangle): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.DynamicMesh.set_mesh_triangle_uv_element_i_ds"></a>

#### set_mesh_triangle_uv_element_i_ds

```python
def set_mesh_triangle_uv_element_i_ds(
        uv_set_index: int,
        triangle_id: int,
        triangle_uv_elements: IntVector,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

x.set_mesh_triangle_uv_element_i_ds(uv_set_index, triangle_id, triangle_uv_elements, defer_change_notifications=False) -> (DynamicMesh, is_valid_triangle=bool)
Sets the UV Element IDs for a given Triangle in the specified UV Channel, ie the "UV Triangle" indices.
This function does not create new UVs, the provided UV Elements must already.
The UV Triangle can only be set if the resulting topology would be valid, ie the Elements cannot be shared
between different base Mesh Vertices, so they must either be unused by any other triangles, or already associated
with the same mesh vertex in other UV triangles.
If any conditions are not met, bIsValidTriangle will be returned as false.

Args:
    uv_set_index (int32): 
    triangle_id (int32): 
    triangle_uv_elements (IntVector): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.DynamicMesh.scale_mesh_u_vs"></a>

#### scale_mesh_u_vs

```python
def scale_mesh_u_vs(uv_set_index: int,
                    scale: Vector2D,
                    scale_origin: Vector2D,
                    selection: GeometryScriptMeshSelection,
                    debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.scale_mesh_u_vs(uv_set_index, scale, scale_origin, selection, debug=None) -> DynamicMesh
Update all selected UV values in the specified UV Channel by Scale, mathematically the new value is given by (UV - ScaleOrigin) * Scale + ScaleOrigin
If the provided Selection is empty, the update is applied to the entire UV Channel.

Args:
    uv_set_index (int32): 
    scale (Vector2D): 
    scale_origin (Vector2D): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.rotate_mesh_u_vs"></a>

#### rotate_mesh_u_vs

```python
def rotate_mesh_u_vs(uv_set_index: int,
                     rotation_angle: float,
                     rotation_origin: Vector2D,
                     selection: GeometryScriptMeshSelection,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.rotate_mesh_u_vs(uv_set_index, rotation_angle, rotation_origin, selection, debug=None) -> DynamicMesh
Update all the selected UV values in the specified UV Channel by a rotation of Rotation Angle (in degrees) relative to the Rotation Origin.
If the provided Selection is empty, the update is applied to the entire UV Channel.

Args:
    uv_set_index (int32): 
    rotation_angle (float): 
    rotation_origin (Vector2D): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.repack_mesh_u_vs"></a>

#### repack_mesh_u_vs

```python
def repack_mesh_u_vs(uv_set_index: int,
                     repack_options: GeometryScriptRepackUVsOptions,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.repack_mesh_u_vs(uv_set_index, repack_options, debug=None) -> DynamicMesh
Packs the existing UV islands in the specified UV Channel into standard UV space based on the Repack Options.

Args:
    uv_set_index (int32): 
    repack_options (GeometryScriptRepackUVsOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.recompute_mesh_u_vs"></a>

#### recompute_mesh_u_vs

```python
def recompute_mesh_u_vs(uv_set_index: int,
                        options: GeometryScriptRecomputeUVsOptions,
                        selection: GeometryScriptMeshSelection,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.recompute_mesh_u_vs(uv_set_index, options, selection, debug=None) -> DynamicMesh
Recomputes UVs in the UV Channel for a Mesh based on different types of well-defined UV islands, such as existing UV islands, PolyGroups,
or a subset of the mesh based on a non-empty Selection.

Args:
    uv_set_index (int32): 
    options (GeometryScriptRecomputeUVsOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.layout_mesh_u_vs"></a>

#### layout_mesh_u_vs

```python
def layout_mesh_u_vs(uv_set_index: int,
                     layout_options: GeometryScriptLayoutUVsOptions,
                     selection: GeometryScriptMeshSelection,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.layout_mesh_u_vs(uv_set_index, layout_options, selection, debug=None) -> DynamicMesh
Packs the existing UV islands in the specified UV Channel into standard UV space based on the Repack Options.

Args:
    uv_set_index (int32): 
    layout_options (GeometryScriptLayoutUVsOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.get_mesh_uv_size_info"></a>

#### get_mesh_uv_size_info

```python
def get_mesh_uv_size_info(
    uv_set_index: int,
    selection: GeometryScriptMeshSelection,
    only_include_valid_uv_tris: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, float, float, Box, Box2D, bool, bool]
```

x.get_mesh_uv_size_info(uv_set_index, selection, only_include_valid_uv_tris=True, debug=None) -> (DynamicMesh, mesh_area=double, uv_area=double, mesh_bounds=Box, uv_bounds=Box2D, is_valid_uv_set=bool, found_unset_u_vs=bool)
Compute information about dimensions and areas for a UV Set of a Mesh, with an optional Mesh Selection

Args:
    uv_set_index (int32): index of UV Channel to query
    selection (GeometryScriptMeshSelection): subset of triangles to process, whole mesh is used if selection is not provided
    only_include_valid_uv_tris (bool): if true, only triangles with valid UVs are included in 3D Mesh Area/Bounds
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    mesh_area (double): output 3D area of queried triangles

    uv_area (double): output 2D UV-space area of queried triangles

    mesh_bounds (Box): output 3D bounding box of queried triangles

    uv_bounds (Box2D): output 2D UV-space bounding box of queried triangles

    is_valid_uv_set (bool): output flag set to false if UV Channel does not exist on the target mesh. In this case Areas and Bounds are not initialized.

    found_unset_u_vs (bool): output flag set to true if any of the queried triangles do not have valid UVs set

<a id="unreal.DynamicMesh.get_mesh_uv_element_position"></a>

#### get_mesh_uv_element_position

```python
def get_mesh_uv_element_position(
        uv_set_index: int,
        element_id: int) -> Tuple[DynamicMesh, Vector2D, bool]
```

x.get_mesh_uv_element_position(uv_set_index, element_id) -> (DynamicMesh, uv_position=Vector2D, is_valid_element_id=bool)
Returns the UV Position for a given UV Element ID in the specified UV Channel.
If the UV Set or Element ID does not exist, bIsValidElementID will be returned as false.

Args:
    uv_set_index (int32): 
    element_id (int32): 

Returns:
    tuple: 

    uv_position (Vector2D): 

    is_valid_element_id (bool):

<a id="unreal.DynamicMesh.get_mesh_triangle_uv_element_i_ds"></a>

#### get_mesh_triangle_uv_element_i_ds

```python
def get_mesh_triangle_uv_element_i_ds(
        uv_set_index: int,
        triangle_id: int) -> Tuple[DynamicMesh, IntVector, bool]
```

x.get_mesh_triangle_uv_element_i_ds(uv_set_index, triangle_id) -> (DynamicMesh, triangle_uv_elements=IntVector, have_valid_u_vs=bool)
Returns the UV Element IDs associated with the three vertices of the triangle in the specified UV Channel.
If the Triangle does not exist in the mesh or if no UVs are set in the specified UV Channel for the triangle, bHaveValidUVs will be returned as false.

Args:
    uv_set_index (int32): 
    triangle_id (int32): 

Returns:
    tuple: 

    triangle_uv_elements (IntVector): 

    have_valid_u_vs (bool):

<a id="unreal.DynamicMesh.get_mesh_per_vertex_u_vs"></a>

#### get_mesh_per_vertex_u_vs

```python
def get_mesh_per_vertex_u_vs(
    uv_set_index: int,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptUVList, bool, bool, bool]
```

x.get_mesh_per_vertex_u_vs(uv_set_index, debug=None) -> (DynamicMesh, uv_list=GeometryScriptUVList, is_valid_uv_set=bool, has_vertex_id_gaps=bool, has_split_u_vs=bool)
Get a list of single vertex UVs for each mesh vertex in the TargetMesh, derived from the specified UV Channel.
The UV Channel may store multiple UVs for a single vertex (along UV seams)
In such cases an arbitrary UV will be stored for that vertex, and bHasSplitUVs will be returned as true

Args:
    uv_set_index (int32): index of UV Channel to read
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    uv_list (GeometryScriptUVList): output UV list will be stored here. Size will be equal to the MaxVertexID of TargetMesh  (not the VertexCount!)

    is_valid_uv_set (bool): will be set to true if the UV Channel was valid

    has_vertex_id_gaps (bool): will be set to true if some vertex indices in TargetMesh were invalid, ie MaxVertexID > VertexCount

    has_split_u_vs (bool): will be set to true if there were split UVs in the UV Channel

<a id="unreal.DynamicMesh.copy_uv_set"></a>

#### copy_uv_set

```python
def copy_uv_set(from_uv_set: int,
                to_uv_set: int,
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.copy_uv_set(from_uv_set, to_uv_set, debug=None) -> DynamicMesh
Copy the data in one UV Channel to another UV Channel on the same Target Mesh.

Args:
    from_uv_set (int32): 
    to_uv_set (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.copy_mesh_uv_layer_to_mesh"></a>

#### copy_mesh_uv_layer_to_mesh

```python
def copy_mesh_uv_layer_to_mesh(
    uv_set_index: int,
    copy_to_uv_mesh: DynamicMesh,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh, bool, bool]
```

x.copy_mesh_uv_layer_to_mesh(uv_set_index, copy_to_uv_mesh, debug=None) -> (DynamicMesh, copy_to_uv_mesh=DynamicMesh, copy_to_uv_mesh_out=DynamicMesh, invalid_topology=bool, is_valid_uv_set=bool)
Copy the 2D UVs from the given UV Channel in CopyFromMesh to the 3D vertex positions in CopyToUVMesh,
with the triangle mesh topology defined by the UV Channel. Generally this "UV Mesh" topology will not
be the same as the 3D mesh topology. PolyGroup IDs and Material IDs are preserved in the UVMesh.

2D UV Positions are copied to 3D as (X, Y, 0)

CopyMeshToMeshUVChannel will copy the 3D UV Mesh back to the UV Channel. This pair of functions can
then be used to implement UV generation/editing via other mesh functions.

Args:
    uv_set_index (int32): 
    copy_to_uv_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_uv_mesh (DynamicMesh): 

    copy_to_uv_mesh_out (DynamicMesh): 

    invalid_topology (bool): will be returned true if any topological issues were found

    is_valid_uv_set (bool): will be returned false if UVSetIndex is not available

<a id="unreal.DynamicMesh.copy_mesh_to_mesh_uv_layer"></a>

#### copy_mesh_to_mesh_uv_layer

```python
def copy_mesh_to_mesh_uv_layer(
    to_uv_set_index: int,
    copy_to_mesh: DynamicMesh,
    only_uv_positions: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh, bool, bool]
```

x.copy_mesh_to_mesh_uv_layer(to_uv_set_index, copy_to_mesh, only_uv_positions=True, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh, found_topology_errors=bool, is_valid_uv_set=bool)
Transfer the 3D vertex positions and triangles of CopyFromUVMesh to the given UV Channel identified by ToUVChannel of CopyToMesh.
3D positions (X,Y,Z) will be copied as UV positions (X,Y), ie Z is ignored.

bOnlyUVPositions controls whether only UV positions will be updated, or if the UV topology will be fully replaced.
When false, CopyFromUVMesh must currently have a MaxVertexID <= that of the UV Channel MaxElementID
When true, CopyFromUVMesh must currently have a MaxTriangleID <= that of CopyToMesh

Args:
    to_uv_set_index (int32): 
    copy_to_mesh (DynamicMesh): 
    only_uv_positions (bool): if true, only (valid, matching) UV positions are updated, a full new UV topology is created
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): 

    copy_to_mesh_out (DynamicMesh): 

    found_topology_errors (bool): 

    is_valid_uv_set (bool): will be returned false if To UV Channel is not available

<a id="unreal.DynamicMesh.compute_mesh_local_uv_param"></a>

#### compute_mesh_local_uv_param

```python
def compute_mesh_local_uv_param(
    center_point: Vector,
    center_point_triangle_id: int,
    radius: float = 1.000000,
    use_interpolated_normal: bool = False,
    tangent_y_direction: Vector = [0.000000, 0.000000, 0.000000],
    uv_rotation_deg: float = 0.000000,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[int], Array[Vector2D]]
```

x.compute_mesh_local_uv_param(center_point, center_point_triangle_id, radius=1.000000, use_interpolated_normal=False, tangent_y_direction=[0.000000, 0.000000, 0.000000], uv_rotation_deg=0.000000, debug=None) -> (DynamicMesh, vertex_i_ds=Array[int32], vertex_u_vs=Array[Vector2D])
Compute local UV parameterization on TargetMesh vertices around the given CenterPoint / Triangle. This method
uses a Discrete Exponential Map parameterization, which unwraps the mesh locally based on geodesic distances and angles.
The CenterPoint will have UV value (0,0), and the computed vertex UVs will be such that Length(UV) == geodesic distance.

Args:
    center_point (Vector): the center point of the parameterization. This point must lie on the triangle specified by CenterPointTriangleID
    center_point_triangle_id (int32): the ID of the Triangle that contains CenterPoint
    radius (double): the parameterization will be computed out to this geodesic radius
    use_interpolated_normal (bool): if true (default false), the normal frame used for the parameterization will be taken from the normal overlay, otherwise the CenterPointTriangleID normal will be used
    tangent_y_direction (Vector): 
    uv_rotation_deg (double): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    vertex_i_ds (Array[int32]): output list of VertexIDs that UVs have been computed for, ie are within geodesic distance Radius from the CenterPoint

    vertex_u_vs (Array[Vector2D]): output list of Vertex UVs that corresponds to VertexIDs

<a id="unreal.DynamicMesh.auto_generate_x_atlas_mesh_u_vs"></a>

#### auto_generate_x_atlas_mesh_u_vs

```python
def auto_generate_x_atlas_mesh_u_vs(
        uv_set_index: int,
        options: GeometryScriptXAtlasOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.auto_generate_x_atlas_mesh_u_vs(uv_set_index, options, debug=None) -> DynamicMesh
Computes new UVs for the specified UV Channel using XAtlas, and optionally packs.

Args:
    uv_set_index (int32): 
    options (GeometryScriptXAtlasOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.auto_generate_patch_builder_mesh_u_vs"></a>

#### auto_generate_patch_builder_mesh_u_vs

```python
def auto_generate_patch_builder_mesh_u_vs(
        uv_set_index: int,
        options: GeometryScriptPatchBuilderOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.auto_generate_patch_builder_mesh_u_vs(uv_set_index, options, debug=None) -> DynamicMesh
Computes new UVs for the specified UV Channel using PatchBuilder method in the Options, and optionally packs.

Args:
    uv_set_index (int32): 
    options (GeometryScriptPatchBuilderOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_texel_density_uv_scaling"></a>

#### apply_texel_density_uv_scaling

```python
def apply_texel_density_uv_scaling(
        uv_set_index: int,
        options: GeometryScriptUVTexelDensityOptions,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_texel_density_uv_scaling(uv_set_index, options, selection, debug=None) -> DynamicMesh
Rescales UVs in the UV Channel for a Mesh to match a specified texel density, described by the options passed in. Supports
processing on a subset of UVs via a non-empty Selection.

Args:
    uv_set_index (int32): 
    options (GeometryScriptUVTexelDensityOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.add_uv_element_to_mesh"></a>

#### add_uv_element_to_mesh

```python
def add_uv_element_to_mesh(
        uv_set_index: int,
        new_uv_position: Vector2D,
        defer_change_notifications: bool = False
) -> Tuple[DynamicMesh, int, bool]
```

x.add_uv_element_to_mesh(uv_set_index, new_uv_position, defer_change_notifications=False) -> (DynamicMesh, new_uv_element_id=int32, is_valid_uv_set=bool)
Adds a new UV Element to the specified UV Channel of the Mesh and returns a new UV Element ID.

Args:
    uv_set_index (int32): 
    new_uv_position (Vector2D): 
    defer_change_notifications (bool): 

Returns:
    tuple: 

    new_uv_element_id (int32): 

    is_valid_uv_set (bool):

<a id="unreal.DynamicMesh.set_mesh_selection_vertex_color"></a>

#### set_mesh_selection_vertex_color

```python
def set_mesh_selection_vertex_color(
        selection: GeometryScriptMeshSelection,
        color: LinearColor,
        flags: GeometryScriptColorFlags,
        create_color_seam: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_mesh_selection_vertex_color(selection, color, flags, create_color_seam=False, debug=None) -> DynamicMesh
Set the colors in the TargetMesh VertexColor Overlay identified by the Selection to a constant value.
For a Vertex Selection, each existing VertexColor Overlay Element for the vertex is updated.
For a Triangle or PolyGroup Selection, all Overlay Elements in the identified Triangles are updated.

Args:
    selection (GeometryScriptMeshSelection): 
    color (LinearColor): the constant color to set
    flags (GeometryScriptColorFlags): specify which RGBA channels to set (default all channels)
    create_color_seam (bool): if true, a "hard edge" in the vertex colors is created, by creating new Elements for all the triangles in the selection. If enabled, Vertex selections are converted to Triangle selections, and Flags is ignored.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_mesh_per_vertex_colors"></a>

#### set_mesh_per_vertex_colors

```python
def set_mesh_per_vertex_colors(
        vertex_color_list: GeometryScriptColorList,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_mesh_per_vertex_colors(vertex_color_list, debug=None) -> DynamicMesh
Set all vertex colors in the TargetMesh VertexColor Overlay to the specified per-vertex colors

Args:
    vertex_color_list (GeometryScriptColorList): per-vertex colors. Size must be less than or equal to the MaxVertexID of TargetMesh  (ie gaps are supported)
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.set_mesh_constant_vertex_color"></a>

#### set_mesh_constant_vertex_color

```python
def set_mesh_constant_vertex_color(
        color: LinearColor,
        flags: GeometryScriptColorFlags,
        clear_existing: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.set_mesh_constant_vertex_color(color, flags, clear_existing=False, debug=None) -> DynamicMesh
Set all vertex colors (optionally specific channels) in the TargetMesh VertexColor Overlay to a constant value

Args:
    color (LinearColor): the constant color to set
    flags (GeometryScriptColorFlags): specify which RGBA channels to set (default all channels)
    clear_existing (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.get_mesh_per_vertex_colors"></a>

#### get_mesh_per_vertex_colors

```python
def get_mesh_per_vertex_colors(
    blend_split_vertex_values: bool = True
) -> Tuple[DynamicMesh, GeometryScriptColorList, bool, bool]
```

x.get_mesh_per_vertex_colors(blend_split_vertex_values=True) -> (DynamicMesh, color_list=GeometryScriptColorList, is_valid_color_set=bool, has_vertex_id_gaps=bool)
Get a list of single vertex colors for each mesh vertex in the TargetMesh, derived from the VertexColor Overlay.
The VertexColor Overlay may store multiple colors for a single vertex (ie different colors for that vertex on different triangles)
In such cases the colors can either be averaged, or the last color seen will be used, depending on the bBlendSplitVertexValues parameter.

Args:
    blend_split_vertex_values (bool): control how multiple colors at the same vertex should be interpreted

Returns:
    tuple: 

    color_list (GeometryScriptColorList): output color list will be stored here. Size will be equal to the MaxVertexID of TargetMesh  (not the VertexCount!)

    is_valid_color_set (bool): will be set to true if the VertexColor Overlay was valid

    has_vertex_id_gaps (bool): will be set to true if some vertex indices in TargetMesh were invalid, ie MaxVertexID > VertexCount

<a id="unreal.DynamicMesh.convert_mesh_vertex_colors_srgb_to_linear"></a>

#### convert_mesh_vertex_colors_srgb_to_linear

```python
def convert_mesh_vertex_colors_srgb_to_linear(
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.convert_mesh_vertex_colors_srgb_to_linear(debug=None) -> DynamicMesh
Apply a SRGB to Linear color transformation on all vertex colors
on the mesh.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.convert_mesh_vertex_colors_linear_to_srgb"></a>

#### convert_mesh_vertex_colors_linear_to_srgb

```python
def convert_mesh_vertex_colors_linear_to_srgb(
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.convert_mesh_vertex_colors_linear_to_srgb(debug=None) -> DynamicMesh
Apply a Linear to SRGB color transformation on all vertex colors
on the mesh.

Args:
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.blur_mesh_vertex_colors"></a>

#### blur_mesh_vertex_colors

```python
def blur_mesh_vertex_colors(
        selection: GeometryScriptMeshSelection,
        num_iterations: int = 1,
        strength: float = 0.500000,
        blur_mode: GeometryScriptBlurColorMode = GeometryScriptBlurColorMode.
    UNIFORM,
        options: GeometryScriptBlurMeshVertexColorsOptions = [
            True, True, True, True
        ],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.blur_mesh_vertex_colors(selection, num_iterations=1, strength=0.500000, blur_mode=GeometryScriptBlurColorMode.UNIFORM, options=[True, True, True, True], debug=None) -> DynamicMesh
Blur the color attribute of the mesh. If the mesh has no color attribute, the function returns the mesh unchanged.

Args:
    selection (GeometryScriptMeshSelection): Only vertices in the selection will have their color attribute blurred.
    num_iterations (int32): The number of blur iterations.
    strength (double): Each iteration, we will blur between the vertex of the color at the previous iteration and its neighbors' average by Strength amount (expected to be in the zero to one range).
    blur_mode (GeometryScriptBlurColorMode): Determines how neighbors are weighted when computing their average.
    options (GeometryScriptBlurMeshVertexColorsOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_solidify"></a>

#### apply_mesh_solidify

```python
def apply_mesh_solidify(options: GeometryScriptSolidifyOptions,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_solidify(options, debug=None) -> DynamicMesh
Replaces the mesh with a voxelized-and-meshed approximation (VoxWrap operation).

Args:
    options (GeometryScriptSolidifyOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_mesh_morphology"></a>

#### apply_mesh_morphology

```python
def apply_mesh_morphology(options: GeometryScriptMorphologyOptions,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_mesh_morphology(options, debug=None) -> DynamicMesh
Replaces the mesh with an SDF-based offset mesh approximation.

Args:
    options (GeometryScriptMorphologyOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_triangle_loop_sub_d"></a>

#### apply_triangle_loop_sub_d

```python
def apply_triangle_loop_sub_d(subdivisions: int,
                              debug: GeometryScriptDebug = None
                              ) -> DynamicMesh
```

x.apply_triangle_loop_sub_d(subdivisions, debug=None) -> DynamicMesh
Apply Triangle Loop Sub D

Args:
    subdivisions (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMesh.apply_polygroup_catmull_clark_sub_d"></a>

#### apply_polygroup_catmull_clark_sub_d

```python
def apply_polygroup_catmull_clark_sub_d(
        subdivisions: int,
        group_layer: GeometryScriptGroupLayer,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

x.apply_polygroup_catmull_clark_sub_d(subdivisions, group_layer, debug=None) -> DynamicMesh
Apply Polygroup Catmull Clark Sub D

Args:
    subdivisions (int32): 
    group_layer (GeometryScriptGroupLayer): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.DynamicMeshPool"></a>