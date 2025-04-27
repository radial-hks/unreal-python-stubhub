## GeometryScript_UVs Objects

```python
class GeometryScript_UVs(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh UVFunctions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshUVFunctions.h

<a id="unreal.GeometryScript_UVs.translate_mesh_u_vs"></a>

#### translate_mesh_u_vs

```python
@classmethod
def translate_mesh_u_vs(cls,
                        target_mesh: DynamicMesh,
                        uv_set_index: int,
                        translation: Vector2D,
                        selection: GeometryScriptMeshSelection,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.translate_mesh_u_vs(target_mesh, uv_set_index, translation, selection, debug=None) -> DynamicMesh
Update all selected UV values in the specified UV Channel by adding the Translation value to each.
If the provided Selection is empty, the Translation is applied to the entire UV Channel.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    translation (Vector2D): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.set_uv_seams_along_selected_edges"></a>

#### set_uv_seams_along_selected_edges

```python
@classmethod
def set_uv_seams_along_selected_edges(
        cls,
        target_mesh: DynamicMesh,
        uv_channel: int,
        selection: GeometryScriptMeshSelection,
        insert_seams: bool = True,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_uv_seams_along_selected_edges(target_mesh, uv_channel, selection, insert_seams=True, defer_change_notifications=False, debug=None) -> DynamicMesh
Convert Selection to an Edge selection, and set or remove UV seams along all of the selected edges

Args:
    target_mesh (DynamicMesh): The mesh to update
    uv_channel (int32): The UV Channel to update
    selection (GeometryScriptMeshSelection): Which edges to operate on
    insert_seams (bool): Whether to insert new seams. If false, removes existing seams instead.
    defer_change_notifications (bool): If true, no mesh change notification will be sent. Set to true if performing many changes in a loop.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.set_num_uv_sets"></a>

#### set_num_uv_sets

```python
@classmethod
def set_num_uv_sets(cls,
                    target_mesh: DynamicMesh,
                    num_uv_sets: int,
                    debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_num_uv_sets(target_mesh, num_uv_sets, debug=None) -> DynamicMesh
Set the number of UV Channels on the Target Mesh. If not already enabled, this will enable the mesh attributes.

Args:
    target_mesh (DynamicMesh): 
    num_uv_sets (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.set_mesh_u_vs_from_planar_projection"></a>

#### set_mesh_u_vs_from_planar_projection

```python
@classmethod
def set_mesh_u_vs_from_planar_projection(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        plane_transform: Transform,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_mesh_u_vs_from_planar_projection(target_mesh, uv_set_index, plane_transform, selection, debug=None) -> DynamicMesh
Scale of PlaneTransform defines world-space dimension that maps to 1 UV dimension

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    plane_transform (Transform): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.set_mesh_u_vs_from_cylinder_projection"></a>

#### set_mesh_u_vs_from_cylinder_projection

```python
@classmethod
def set_mesh_u_vs_from_cylinder_projection(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        cylinder_transform: Transform,
        selection: GeometryScriptMeshSelection,
        split_angle: float = 45.000000,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_mesh_u_vs_from_cylinder_projection(target_mesh, uv_set_index, cylinder_transform, selection, split_angle=45.000000, debug=None) -> DynamicMesh
Using Cylinder Projection, update the UVs in the UV Channel for an entire mesh or a subset defined by a non-empty Selection.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    cylinder_transform (Transform): 
    selection (GeometryScriptMeshSelection): 
    split_angle (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.set_mesh_u_vs_from_box_projection"></a>

#### set_mesh_u_vs_from_box_projection

```python
@classmethod
def set_mesh_u_vs_from_box_projection(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        box_transform: Transform,
        selection: GeometryScriptMeshSelection,
        min_island_tri_count: int = 2,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_mesh_u_vs_from_box_projection(target_mesh, uv_set_index, box_transform, selection, min_island_tri_count=2, debug=None) -> DynamicMesh
Using Box Projection, update the UVs in the UV Channel for an entire mesh or a subset defined by a non-empty Selection.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    box_transform (Transform): 
    selection (GeometryScriptMeshSelection): 
    min_island_tri_count (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.set_mesh_uv_element_position"></a>

#### set_mesh_uv_element_position

```python
@classmethod
def set_mesh_uv_element_position(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        element_id: int,
        new_uv_position: Vector2D,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.set_mesh_uv_element_position(target_mesh, uv_set_index, element_id, new_uv_position, defer_change_notifications=False) -> (DynamicMesh, is_valid_element_id=bool)
Sets the UV position of a specific ElementID in the given UV Set/Channel
If the UV Set or Element ID does not exist, bIsValidElementID will be returned as false.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    element_id (int32): 
    new_uv_position (Vector2D): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_element_id (bool):

<a id="unreal.GeometryScript_UVs.set_mesh_triangle_u_vs"></a>

#### set_mesh_triangle_u_vs

```python
@classmethod
def set_mesh_triangle_u_vs(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        triangle_id: int,
        u_vs: GeometryScriptUVTriangle,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.set_mesh_triangle_u_vs(target_mesh, uv_set_index, triangle_id, u_vs, defer_change_notifications=False) -> (DynamicMesh, is_valid_triangle=bool)
Sets the UVs of a mesh triangle in the given UV Channel.
This function will create new UV elements for each vertex of the triangle, meaning that
the triangle will become an isolated UV island.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    triangle_id (int32): 
    u_vs (GeometryScriptUVTriangle): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.GeometryScript_UVs.set_mesh_triangle_uv_element_i_ds"></a>

#### set_mesh_triangle_uv_element_i_ds

```python
@classmethod
def set_mesh_triangle_uv_element_i_ds(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        triangle_id: int,
        triangle_uv_elements: IntVector,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.set_mesh_triangle_uv_element_i_ds(target_mesh, uv_set_index, triangle_id, triangle_uv_elements, defer_change_notifications=False) -> (DynamicMesh, is_valid_triangle=bool)
Sets the UV Element IDs for a given Triangle in the specified UV Channel, ie the "UV Triangle" indices.
This function does not create new UVs, the provided UV Elements must already.
The UV Triangle can only be set if the resulting topology would be valid, ie the Elements cannot be shared
between different base Mesh Vertices, so they must either be unused by any other triangles, or already associated
with the same mesh vertex in other UV triangles.
If any conditions are not met, bIsValidTriangle will be returned as false.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    triangle_id (int32): 
    triangle_uv_elements (IntVector): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.GeometryScript_UVs.scale_mesh_u_vs"></a>

#### scale_mesh_u_vs

```python
@classmethod
def scale_mesh_u_vs(cls,
                    target_mesh: DynamicMesh,
                    uv_set_index: int,
                    scale: Vector2D,
                    scale_origin: Vector2D,
                    selection: GeometryScriptMeshSelection,
                    debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.scale_mesh_u_vs(target_mesh, uv_set_index, scale, scale_origin, selection, debug=None) -> DynamicMesh
Update all selected UV values in the specified UV Channel by Scale, mathematically the new value is given by (UV - ScaleOrigin) * Scale + ScaleOrigin
If the provided Selection is empty, the update is applied to the entire UV Channel.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    scale (Vector2D): 
    scale_origin (Vector2D): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.rotate_mesh_u_vs"></a>

#### rotate_mesh_u_vs

```python
@classmethod
def rotate_mesh_u_vs(cls,
                     target_mesh: DynamicMesh,
                     uv_set_index: int,
                     rotation_angle: float,
                     rotation_origin: Vector2D,
                     selection: GeometryScriptMeshSelection,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.rotate_mesh_u_vs(target_mesh, uv_set_index, rotation_angle, rotation_origin, selection, debug=None) -> DynamicMesh
Update all the selected UV values in the specified UV Channel by a rotation of Rotation Angle (in degrees) relative to the Rotation Origin.
If the provided Selection is empty, the update is applied to the entire UV Channel.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    rotation_angle (float): 
    rotation_origin (Vector2D): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.repack_mesh_u_vs"></a>

#### repack_mesh_u_vs

```python
@classmethod
def repack_mesh_u_vs(cls,
                     target_mesh: DynamicMesh,
                     uv_set_index: int,
                     repack_options: GeometryScriptRepackUVsOptions,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.repack_mesh_u_vs(target_mesh, uv_set_index, repack_options, debug=None) -> DynamicMesh
Packs the existing UV islands in the specified UV Channel into standard UV space based on the Repack Options.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    repack_options (GeometryScriptRepackUVsOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.recompute_mesh_u_vs"></a>

#### recompute_mesh_u_vs

```python
@classmethod
def recompute_mesh_u_vs(cls,
                        target_mesh: DynamicMesh,
                        uv_set_index: int,
                        options: GeometryScriptRecomputeUVsOptions,
                        selection: GeometryScriptMeshSelection,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.recompute_mesh_u_vs(target_mesh, uv_set_index, options, selection, debug=None) -> DynamicMesh
Recomputes UVs in the UV Channel for a Mesh based on different types of well-defined UV islands, such as existing UV islands, PolyGroups,
or a subset of the mesh based on a non-empty Selection.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    options (GeometryScriptRecomputeUVsOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.layout_mesh_u_vs"></a>

#### layout_mesh_u_vs

```python
@classmethod
def layout_mesh_u_vs(cls,
                     target_mesh: DynamicMesh,
                     uv_set_index: int,
                     layout_options: GeometryScriptLayoutUVsOptions,
                     selection: GeometryScriptMeshSelection,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.layout_mesh_u_vs(target_mesh, uv_set_index, layout_options, selection, debug=None) -> DynamicMesh
Packs the existing UV islands in the specified UV Channel into standard UV space based on the Repack Options.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    layout_options (GeometryScriptLayoutUVsOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.get_mesh_uv_size_info"></a>

#### get_mesh_uv_size_info

```python
@classmethod
def get_mesh_uv_size_info(
    cls,
    target_mesh: DynamicMesh,
    uv_set_index: int,
    selection: GeometryScriptMeshSelection,
    only_include_valid_uv_tris: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, float, float, Box, Box2D, bool, bool]
```

X.get_mesh_uv_size_info(target_mesh, uv_set_index, selection, only_include_valid_uv_tris=True, debug=None) -> (DynamicMesh, mesh_area=double, uv_area=double, mesh_bounds=Box, uv_bounds=Box2D, is_valid_uv_set=bool, found_unset_u_vs=bool)
Compute information about dimensions and areas for a UV Set of a Mesh, with an optional Mesh Selection

Args:
    target_mesh (DynamicMesh): 
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

<a id="unreal.GeometryScript_UVs.get_mesh_uv_element_position"></a>

#### get_mesh_uv_element_position

```python
@classmethod
def get_mesh_uv_element_position(
        cls, target_mesh: DynamicMesh, uv_set_index: int,
        element_id: int) -> Tuple[DynamicMesh, Vector2D, bool]
```

X.get_mesh_uv_element_position(target_mesh, uv_set_index, element_id) -> (DynamicMesh, uv_position=Vector2D, is_valid_element_id=bool)
Returns the UV Position for a given UV Element ID in the specified UV Channel.
If the UV Set or Element ID does not exist, bIsValidElementID will be returned as false.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    element_id (int32): 

Returns:
    tuple: 

    uv_position (Vector2D): 

    is_valid_element_id (bool):

<a id="unreal.GeometryScript_UVs.get_mesh_triangle_uv_element_i_ds"></a>

#### get_mesh_triangle_uv_element_i_ds

```python
@classmethod
def get_mesh_triangle_uv_element_i_ds(
        cls, target_mesh: DynamicMesh, uv_set_index: int,
        triangle_id: int) -> Tuple[DynamicMesh, IntVector, bool]
```

X.get_mesh_triangle_uv_element_i_ds(target_mesh, uv_set_index, triangle_id) -> (DynamicMesh, triangle_uv_elements=IntVector, have_valid_u_vs=bool)
Returns the UV Element IDs associated with the three vertices of the triangle in the specified UV Channel.
If the Triangle does not exist in the mesh or if no UVs are set in the specified UV Channel for the triangle, bHaveValidUVs will be returned as false.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    triangle_id (int32): 

Returns:
    tuple: 

    triangle_uv_elements (IntVector): 

    have_valid_u_vs (bool):

<a id="unreal.GeometryScript_UVs.get_mesh_per_vertex_u_vs"></a>

#### get_mesh_per_vertex_u_vs

```python
@classmethod
def get_mesh_per_vertex_u_vs(
    cls,
    target_mesh: DynamicMesh,
    uv_set_index: int,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptUVList, bool, bool, bool]
```

X.get_mesh_per_vertex_u_vs(target_mesh, uv_set_index, debug=None) -> (DynamicMesh, uv_list=GeometryScriptUVList, is_valid_uv_set=bool, has_vertex_id_gaps=bool, has_split_u_vs=bool)
Get a list of single vertex UVs for each mesh vertex in the TargetMesh, derived from the specified UV Channel.
The UV Channel may store multiple UVs for a single vertex (along UV seams)
In such cases an arbitrary UV will be stored for that vertex, and bHasSplitUVs will be returned as true

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): index of UV Channel to read
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    uv_list (GeometryScriptUVList): output UV list will be stored here. Size will be equal to the MaxVertexID of TargetMesh  (not the VertexCount!)

    is_valid_uv_set (bool): will be set to true if the UV Channel was valid

    has_vertex_id_gaps (bool): will be set to true if some vertex indices in TargetMesh were invalid, ie MaxVertexID > VertexCount

    has_split_u_vs (bool): will be set to true if there were split UVs in the UV Channel

<a id="unreal.GeometryScript_UVs.copy_uv_set"></a>

#### copy_uv_set

```python
@classmethod
def copy_uv_set(cls,
                target_mesh: DynamicMesh,
                from_uv_set: int,
                to_uv_set: int,
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.copy_uv_set(target_mesh, from_uv_set, to_uv_set, debug=None) -> DynamicMesh
Copy the data in one UV Channel to another UV Channel on the same Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    from_uv_set (int32): 
    to_uv_set (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.copy_mesh_uv_layer_to_mesh"></a>

#### copy_mesh_uv_layer_to_mesh

```python
@classmethod
def copy_mesh_uv_layer_to_mesh(
    cls,
    copy_from_mesh: DynamicMesh,
    uv_set_index: int,
    copy_to_uv_mesh: DynamicMesh,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh, bool, bool]
```

X.copy_mesh_uv_layer_to_mesh(copy_from_mesh, uv_set_index, copy_to_uv_mesh, debug=None) -> (DynamicMesh, copy_to_uv_mesh=DynamicMesh, copy_to_uv_mesh_out=DynamicMesh, invalid_topology=bool, is_valid_uv_set=bool)
Copy the 2D UVs from the given UV Channel in CopyFromMesh to the 3D vertex positions in CopyToUVMesh,
with the triangle mesh topology defined by the UV Channel. Generally this "UV Mesh" topology will not
be the same as the 3D mesh topology. PolyGroup IDs and Material IDs are preserved in the UVMesh.

2D UV Positions are copied to 3D as (X, Y, 0)

CopyMeshToMeshUVChannel will copy the 3D UV Mesh back to the UV Channel. This pair of functions can
then be used to implement UV generation/editing via other mesh functions.

Args:
    copy_from_mesh (DynamicMesh): 
    uv_set_index (int32): 
    copy_to_uv_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_uv_mesh (DynamicMesh): 

    copy_to_uv_mesh_out (DynamicMesh): 

    invalid_topology (bool): will be returned true if any topological issues were found

    is_valid_uv_set (bool): will be returned false if UVSetIndex is not available

<a id="unreal.GeometryScript_UVs.copy_mesh_to_mesh_uv_layer"></a>

#### copy_mesh_to_mesh_uv_layer

```python
@classmethod
def copy_mesh_to_mesh_uv_layer(
    cls,
    copy_from_uv_mesh: DynamicMesh,
    to_uv_set_index: int,
    copy_to_mesh: DynamicMesh,
    only_uv_positions: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh, bool, bool]
```

X.copy_mesh_to_mesh_uv_layer(copy_from_uv_mesh, to_uv_set_index, copy_to_mesh, only_uv_positions=True, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh, found_topology_errors=bool, is_valid_uv_set=bool)
Transfer the 3D vertex positions and triangles of CopyFromUVMesh to the given UV Channel identified by ToUVChannel of CopyToMesh.
3D positions (X,Y,Z) will be copied as UV positions (X,Y), ie Z is ignored.

bOnlyUVPositions controls whether only UV positions will be updated, or if the UV topology will be fully replaced.
When false, CopyFromUVMesh must currently have a MaxVertexID <= that of the UV Channel MaxElementID
When true, CopyFromUVMesh must currently have a MaxTriangleID <= that of CopyToMesh

Args:
    copy_from_uv_mesh (DynamicMesh): 
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

<a id="unreal.GeometryScript_UVs.compute_mesh_local_uv_param"></a>

#### compute_mesh_local_uv_param

```python
@classmethod
def compute_mesh_local_uv_param(
    cls,
    target_mesh: DynamicMesh,
    center_point: Vector,
    center_point_triangle_id: int,
    radius: float = 1.000000,
    use_interpolated_normal: bool = False,
    tangent_y_direction: Vector = [0.000000, 0.000000, 0.000000],
    uv_rotation_deg: float = 0.000000,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[int], Array[Vector2D]]
```

X.compute_mesh_local_uv_param(target_mesh, center_point, center_point_triangle_id, radius=1.000000, use_interpolated_normal=False, tangent_y_direction=[0.000000, 0.000000, 0.000000], uv_rotation_deg=0.000000, debug=None) -> (DynamicMesh, vertex_i_ds=Array[int32], vertex_u_vs=Array[Vector2D])
Compute local UV parameterization on TargetMesh vertices around the given CenterPoint / Triangle. This method
uses a Discrete Exponential Map parameterization, which unwraps the mesh locally based on geodesic distances and angles.
The CenterPoint will have UV value (0,0), and the computed vertex UVs will be such that Length(UV) == geodesic distance.

Args:
    target_mesh (DynamicMesh): 
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

<a id="unreal.GeometryScript_UVs.auto_generate_x_atlas_mesh_u_vs"></a>

#### auto_generate_x_atlas_mesh_u_vs

```python
@classmethod
def auto_generate_x_atlas_mesh_u_vs(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        options: GeometryScriptXAtlasOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.auto_generate_x_atlas_mesh_u_vs(target_mesh, uv_set_index, options, debug=None) -> DynamicMesh
Computes new UVs for the specified UV Channel using XAtlas, and optionally packs.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    options (GeometryScriptXAtlasOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.auto_generate_patch_builder_mesh_u_vs"></a>

#### auto_generate_patch_builder_mesh_u_vs

```python
@classmethod
def auto_generate_patch_builder_mesh_u_vs(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        options: GeometryScriptPatchBuilderOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.auto_generate_patch_builder_mesh_u_vs(target_mesh, uv_set_index, options, debug=None) -> DynamicMesh
Computes new UVs for the specified UV Channel using PatchBuilder method in the Options, and optionally packs.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    options (GeometryScriptPatchBuilderOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.apply_texel_density_uv_scaling"></a>

#### apply_texel_density_uv_scaling

```python
@classmethod
def apply_texel_density_uv_scaling(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        options: GeometryScriptUVTexelDensityOptions,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_texel_density_uv_scaling(target_mesh, uv_set_index, options, selection, debug=None) -> DynamicMesh
Rescales UVs in the UV Channel for a Mesh to match a specified texel density, described by the options passed in. Supports
processing on a subset of UVs via a non-empty Selection.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    options (GeometryScriptUVTexelDensityOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs.add_uv_element_to_mesh"></a>

#### add_uv_element_to_mesh

```python
@classmethod
def add_uv_element_to_mesh(
        cls,
        target_mesh: DynamicMesh,
        uv_set_index: int,
        new_uv_position: Vector2D,
        defer_change_notifications: bool = False
) -> Tuple[DynamicMesh, int, bool]
```

X.add_uv_element_to_mesh(target_mesh, uv_set_index, new_uv_position, defer_change_notifications=False) -> (DynamicMesh, new_uv_element_id=int32, is_valid_uv_set=bool)
Adds a new UV Element to the specified UV Channel of the Mesh and returns a new UV Element ID.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    new_uv_position (Vector2D): 
    defer_change_notifications (bool): 

Returns:
    tuple: 

    new_uv_element_id (int32): 

    is_valid_uv_set (bool):

<a id="unreal.GeometryScript_VertexColors"></a>