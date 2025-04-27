## GeometryScript_Normals Objects

```python
class GeometryScript_Normals(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Normals Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshNormalsFunctions.h

<a id="unreal.GeometryScript_Normals.update_vertex_normal"></a>

#### update_vertex_normal

```python
@classmethod
def update_vertex_normal(
        cls,
        target_mesh: DynamicMesh,
        vertex_id: int,
        update_normal: bool = True,
        new_normal: Vector = ...,
        update_tangents: bool = ...,
        new_tangent_x: Vector = ...,
        new_tangent_y: Vector = ...,
        merge_split_values: bool = ...,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.update_vertex_normal(target_mesh, vertex_id, update_normal=True, new_normal, update_tangents, new_tangent_x, new_tangent_y, merge_split_values, defer_change_notifications=False) -> (DynamicMesh, is_valid_vertex=bool)
Update the Normals and/or Tangents at VertexID of TargetMesh. Note that the specified vertex may have "split normals"
or "split tangents", ie in the case of hard/crease normals, UV seams, and so on. In these situations, by default
each of the unique normals/tangents at the vertex will be updated, but they will not be "merged", ie they will remain split.
However if bMergeSplitValues=true, then the vertex will be "un-split", ie after the function call the vertex will have
a single unique shared normal and/or tangents.

Note that this function requires that some normals/tangents already exist on the TargetMesh. If this is not the case,
functions like SetPerVertexNormals and ComputeTangents can be used to initialize the normals/tangents first.

Args:
    target_mesh (DynamicMesh): 
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

<a id="unreal.GeometryScript_Normals.set_split_normals_along_selected_edges"></a>

#### set_split_normals_along_selected_edges

```python
@classmethod
def set_split_normals_along_selected_edges(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        split: bool = True,
        recalculate_normals: bool = True,
        calculate_options: GeometryScriptCalculateNormalsOptions = [
            True, True
        ],
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_split_normals_along_selected_edges(target_mesh, selection, split=True, recalculate_normals=True, calculate_options=[True, True], defer_change_notifications=False, debug=None) -> DynamicMesh
Set or remove split normals (aka sharp normals) for all edges in the Selection

Args:
    target_mesh (DynamicMesh): The mesh to update
    selection (GeometryScriptMeshSelection): Which edges to operate on
    split (bool): Whether to split normals along the selected edges; if false, they will be merged instead
    recalculate_normals (bool): Whether to recalculate normals along edges where they were split/merged
    calculate_options (GeometryScriptCalculateNormalsOptions): Options for computing the normals, if bRecalculateNormals is true
    defer_change_notifications (bool): If true, no mesh change notification will be sent. Set to true if performing many changes in a loop.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.set_per_vertex_normals"></a>

#### set_per_vertex_normals

```python
@classmethod
def set_per_vertex_normals(cls,
                           target_mesh: DynamicMesh,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_per_vertex_normals(target_mesh, debug=None) -> DynamicMesh
Recompute the normals of TargetMesh by averaging the triangle/face normals around each vertex, using combined area and angle weighting.
Each vertex will have a single normal, ie there will be no hard edges.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.set_per_face_normals"></a>

#### set_per_face_normals

```python
@classmethod
def set_per_face_normals(cls,
                         target_mesh: DynamicMesh,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_per_face_normals(target_mesh, debug=None) -> DynamicMesh
Recompute the normals of TargetMesh by setting the normals of each triangle vertex to the triangle/face normal.
Each vertex will have a unique normal in each triangle, ie there will be hard edges / split normals at every mesh edge

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.set_mesh_triangle_normals"></a>

#### set_mesh_triangle_normals

```python
@classmethod
def set_mesh_triangle_normals(
        cls,
        target_mesh: DynamicMesh,
        triangle_id: int,
        normals: GeometryScriptTriangle,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.set_mesh_triangle_normals(target_mesh, triangle_id, normals, defer_change_notifications=False) -> (DynamicMesh, is_valid_triangle=bool)
Set the triangle-vertex normals for the given TriangleID on the TargetMesh. This will
create unique triangle-vertex normals, ie it will create hard edges / split normals in
the normal overlay for each edge of the triangle.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 
    normals (GeometryScriptTriangle): 
    defer_change_notifications (bool): if true, no mesh change notification will be sent. Set to true if changing many normals in a loop.

Returns:
    bool: 

    is_valid_triangle (bool): will be returned as false if TriangleID does not refer to a valid triangle

<a id="unreal.GeometryScript_Normals.set_mesh_per_vertex_tangents"></a>

#### set_mesh_per_vertex_tangents

```python
@classmethod
def set_mesh_per_vertex_tangents(
        cls,
        target_mesh: DynamicMesh,
        tangent_x_list: GeometryScriptVectorList,
        tangent_y_list: GeometryScriptVectorList,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_mesh_per_vertex_tangents(target_mesh, tangent_x_list, tangent_y_list, debug=None) -> DynamicMesh
Set all tangents in the TargetMesh Tangents Overlays to the specified per-vertex tangents
note: If setting Tangents for use with a DynamicMeshComponent, it is also necessary to set the Tangents Type on the Component to "Externally Provided"

Args:
    target_mesh (DynamicMesh): 
    tangent_x_list (GeometryScriptVectorList): per-vertex tangent vectors. Size must be equal to the MaxVertexID of TargetMesh  (ie non-compact TargetMesh is supported)
    tangent_y_list (GeometryScriptVectorList): per-vertex bitangent/binormal vectors. Size must be equal to TangentXList
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.set_mesh_per_vertex_normals"></a>

#### set_mesh_per_vertex_normals

```python
@classmethod
def set_mesh_per_vertex_normals(
        cls,
        target_mesh: DynamicMesh,
        vertex_normal_list: GeometryScriptVectorList,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_mesh_per_vertex_normals(target_mesh, vertex_normal_list, debug=None) -> DynamicMesh
Set all normals in the TargetMesh Normals Overlay to the specified per-vertex normals

Args:
    target_mesh (DynamicMesh): 
    vertex_normal_list (GeometryScriptVectorList): per-vertex normals. Size must be equal to the MaxVertexID of TargetMesh  (ie non-compact TargetMesh is supported)
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.recompute_normals_for_mesh_selection"></a>

#### recompute_normals_for_mesh_selection

```python
@classmethod
def recompute_normals_for_mesh_selection(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        calculate_options: GeometryScriptCalculateNormalsOptions,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.recompute_normals_for_mesh_selection(target_mesh, selection, calculate_options, defer_change_notifications=False, debug=None) -> DynamicMesh
Recompute the normals of TargetMesh on all the triangles/vertices of the given Selection using the given CalculateOptions.
This method will preserve any existing hard edges, ie each shared triangle-vertex normal is recomputed by averaging
the face normals of triangles that reference that shared triangle-vertex normal

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    calculate_options (GeometryScriptCalculateNormalsOptions): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.recompute_normals"></a>

#### recompute_normals

```python
@classmethod
def recompute_normals(cls,
                      target_mesh: DynamicMesh,
                      calculate_options: GeometryScriptCalculateNormalsOptions,
                      defer_change_notifications: bool = False,
                      debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.recompute_normals(target_mesh, calculate_options, defer_change_notifications=False, debug=None) -> DynamicMesh
Recompute the normals of TargetMesh using the given CalculateOptions. This method will preserve any existing hard
edges, ie each shared triangle-vertex normal is recomputed by averaging the face normals of triangles that reference
that shared triangle-vertex normal

Args:
    target_mesh (DynamicMesh): 
    calculate_options (GeometryScriptCalculateNormalsOptions): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.get_mesh_per_vertex_tangents"></a>

#### get_mesh_per_vertex_tangents

```python
@classmethod
def get_mesh_per_vertex_tangents(
    cls,
    target_mesh: DynamicMesh,
    average_split_vertex_values: bool = True
) -> Tuple[DynamicMesh, GeometryScriptVectorList, GeometryScriptVectorList,
           bool, bool]
```

X.get_mesh_per_vertex_tangents(target_mesh, average_split_vertex_values=True) -> (DynamicMesh, tangent_x_list=GeometryScriptVectorList, tangent_y_list=GeometryScriptVectorList, is_valid_tangent_set=bool, has_vertex_id_gaps=bool)
Get a list of single tangent vectors for each mesh vertex in the TargetMesh, derived from the Tangents Overlays.
The Tangents Overlay may store multiple tangents for a single vertex (ie split tangents)
In such cases the tangents can either be averaged, or the last tangent seen will be used, depending on the bAverageSplitVertexValues parameter.

Args:
    target_mesh (DynamicMesh): 
    average_split_vertex_values (bool): control how multiple tangents at the same vertex should be interpreted

Returns:
    tuple: 

    tangent_x_list (GeometryScriptVectorList): output Tangent "X" vectors list will be stored here. Size will be equal to the MaxVertexID of TargetMesh  (not the VertexCount!)

    tangent_y_list (GeometryScriptVectorList): output Tangent "Y" vectors (Binormal/Bitangent) list will be stored here. Size will be equal to TangentXList

    is_valid_tangent_set (bool): will be set to true if the Tangent Overlay was valid

    has_vertex_id_gaps (bool): will be set to true if some vertex indices in TargetMesh were invalid, ie MaxVertexID > VertexCount

<a id="unreal.GeometryScript_Normals.get_mesh_per_vertex_normals"></a>

#### get_mesh_per_vertex_normals

```python
@classmethod
def get_mesh_per_vertex_normals(
    cls,
    target_mesh: DynamicMesh,
    average_split_vertex_values: bool = True
) -> Tuple[DynamicMesh, GeometryScriptVectorList, bool, bool]
```

X.get_mesh_per_vertex_normals(target_mesh, average_split_vertex_values=True) -> (DynamicMesh, normal_list=GeometryScriptVectorList, is_valid_normal_set=bool, has_vertex_id_gaps=bool)
Get a list of single normal vectors for each mesh vertex in the TargetMesh, derived from the Normals Overlay.
The Normals Overlay may store multiple normals for a single vertex (ie split normals)
In such cases the normals can either be averaged, or the last normal seen will be used, depending on the bAverageSplitVertexValues parameter.

Args:
    target_mesh (DynamicMesh): 
    average_split_vertex_values (bool): control how multiple normals at the same vertex should be interpreted

Returns:
    tuple: 

    normal_list (GeometryScriptVectorList): output normal list will be stored here. Size will be equal to the MaxVertexID of TargetMesh  (not the VertexCount!)

    is_valid_normal_set (bool): will be set to true if the Normal Overlay was valid

    has_vertex_id_gaps (bool): will be set to true if some vertex indices in TargetMesh were invalid, ie MaxVertexID > VertexCount

<a id="unreal.GeometryScript_Normals.get_mesh_has_tangents"></a>

#### get_mesh_has_tangents

```python
@classmethod
def get_mesh_has_tangents(
        cls,
        target_mesh: DynamicMesh,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

X.get_mesh_has_tangents(target_mesh, debug=None) -> (DynamicMesh, has_tangents=bool)
Check if the TargetMesh has a Tangents Attribute Layer enabled

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    has_tangents (bool):

<a id="unreal.GeometryScript_Normals.flip_normals"></a>

#### flip_normals

```python
@classmethod
def flip_normals(cls,
                 target_mesh: DynamicMesh,
                 debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.flip_normals(target_mesh, debug=None) -> DynamicMesh
Flip/Invert the normal vectors of TargetMesh by multiplying them by -1, as well as reversing the mesh triangle orientations, ie triangle (a,b,c) becomes (b,a,c)

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.discard_tangents"></a>

#### discard_tangents

```python
@classmethod
def discard_tangents(cls,
                     target_mesh: DynamicMesh,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.discard_tangents(target_mesh, debug=None) -> DynamicMesh
Remove any existing Tangents Attribute Layer from the TargetMesh

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.compute_tangents"></a>

#### compute_tangents

```python
@classmethod
def compute_tangents(cls,
                     target_mesh: DynamicMesh,
                     options: GeometryScriptTangentsOptions,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.compute_tangents(target_mesh, options, debug=None) -> DynamicMesh
Recompute Tangents for the TargetMesh, using the method and settings specified by FGeometryScriptTangentsOptions
note: If recomputing Tangents for use with a DynamicMeshComponent, it is also necessary to set the Tangents Type on the Component to "Externally Provided"

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptTangentsOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.compute_split_normals"></a>

#### compute_split_normals

```python
@classmethod
def compute_split_normals(
        cls,
        target_mesh: DynamicMesh,
        split_options: GeometryScriptSplitNormalsOptions,
        calculate_options: GeometryScriptCalculateNormalsOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.compute_split_normals(target_mesh, split_options, calculate_options, debug=None) -> DynamicMesh
Recompute hard edges / split-normals for TargetMesh based on the provided SplitOptions, and then
recompute the new shared triangle-vertex normals using the given CalculateOptions.
The normal recomputation is identical to calling RecomputeNormals.

Args:
    target_mesh (DynamicMesh): 
    split_options (GeometryScriptSplitNormalsOptions): 
    calculate_options (GeometryScriptCalculateNormalsOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals.auto_repair_normals"></a>

#### auto_repair_normals

```python
@classmethod
def auto_repair_normals(cls,
                        target_mesh: DynamicMesh,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.auto_repair_normals(target_mesh, debug=None) -> DynamicMesh
Attempt to repair inconsistent normals in TargetMesh. Currently this is done in two passes. In the first pass, triangles with
reversed orientation from their neighours are incrementally flipped until each connected component has a consistent orientation,
if this is possible (note that this is not always globally possible, eg for a mobius-strip topology there is no consistent orientation).
In the second pass, the "global" orientation is detected by casting rays from outside the mesh. This may produce incorrect results for
meshes that are not closed.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PolyGroups"></a>