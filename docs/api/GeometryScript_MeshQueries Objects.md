## GeometryScript_MeshQueries Objects

```python
class GeometryScript_MeshQueries(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Query Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshQueryFunctions.h

<a id="unreal.GeometryScript_MeshQueries.is_valid_vertex_id"></a>

#### is_valid_vertex_id

```python
@classmethod
def is_valid_vertex_id(cls, target_mesh: DynamicMesh, vertex_id: int) -> bool
```

X.is_valid_vertex_id(target_mesh, vertex_id) -> bool
Returns true if Vertex ID refers to a valid vertex in the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.is_valid_triangle_id"></a>

#### is_valid_triangle_id

```python
@classmethod
def is_valid_triangle_id(cls, target_mesh: DynamicMesh,
                         triangle_id: int) -> bool
```

X.is_valid_triangle_id(target_mesh, triangle_id) -> bool
Returns true if Triangle ID refers to a valid Triangle in the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.get_vertex_position"></a>

#### get_vertex_position

```python
@classmethod
def get_vertex_position(cls, target_mesh: DynamicMesh,
                        vertex_id: int) -> Tuple[Vector, bool]
```

X.get_vertex_position(target_mesh, vertex_id) -> (Vector, is_valid_vertex=bool)
Gets the 3D position of a mesh vertex in the mesh local space, by Vertex ID.

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): 

Returns:
    bool: 

    is_valid_vertex (bool):

<a id="unreal.GeometryScript_MeshQueries.get_vertex_count"></a>

#### get_vertex_count

```python
@classmethod
def get_vertex_count(cls, target_mesh: DynamicMesh) -> int
```

X.get_vertex_count(target_mesh) -> int32
Gets the number of vertices in the mesh. Note this may be less than the number of Vertex IDs used as some vertices may have been deleted.

Args:
    target_mesh (DynamicMesh): 

Returns:
    int32:

<a id="unreal.GeometryScript_MeshQueries.get_vertex_connected_vertices"></a>

#### get_vertex_connected_vertices

```python
@classmethod
def get_vertex_connected_vertices(
        cls, target_mesh: DynamicMesh,
        vertex_id: int) -> Tuple[DynamicMesh, Array[int]]
```

X.get_vertex_connected_vertices(target_mesh, vertex_id) -> (DynamicMesh, vertices=Array[int32])
Return array of Vertex IDs connected via a mesh edge to the given VertexID, ie the vertex one-ring

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): 

Returns:
    Array[int32]: 

    vertices (Array[int32]):

<a id="unreal.GeometryScript_MeshQueries.get_vertex_connected_triangles"></a>

#### get_vertex_connected_triangles

```python
@classmethod
def get_vertex_connected_triangles(
        cls, target_mesh: DynamicMesh,
        vertex_id: int) -> Tuple[DynamicMesh, Array[int]]
```

X.get_vertex_connected_triangles(target_mesh, vertex_id) -> (DynamicMesh, triangles=Array[int32])
Return array of Triangle IDs connected to the given VertexID, ie the triangle one-ring

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): 

Returns:
    Array[int32]: 

    triangles (Array[int32]):

<a id="unreal.GeometryScript_MeshQueries.get_uv_set_bounding_box"></a>

#### get_uv_set_bounding_box

```python
@classmethod
def get_uv_set_bounding_box(cls, target_mesh: DynamicMesh,
                            uv_set_index: int) -> Tuple[Box2D, bool, bool]
```

X.get_uv_set_bounding_box(target_mesh, uv_set_index) -> (Box2D, is_valid_uv_set=bool, uv_set_is_empty=bool)
Gets the 2D bounding box of all UVs in the UV Channel.  If the UV Channel does not exist, or if the UV Channel is empty, the resulting box will be invalid.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 

Returns:
    tuple: 

    is_valid_uv_set (bool): 

    uv_set_is_empty (bool):

<a id="unreal.GeometryScript_MeshQueries.get_triangle_vertex_colors"></a>

#### get_triangle_vertex_colors

```python
@classmethod
def get_triangle_vertex_colors(
    cls, target_mesh: DynamicMesh, triangle_id: int
) -> Tuple[DynamicMesh, LinearColor, LinearColor, LinearColor, bool]
```

X.get_triangle_vertex_colors(target_mesh, triangle_id) -> (DynamicMesh, color1=LinearColor, color2=LinearColor, color3=LinearColor, tri_has_valid_vertex_colors=bool)
For the specified TriangleID of the TargetMesh, get the Vertex Colors at each vertex of the Triangle.
These Colors will be taken from the Vertex Color Attribute, ie they will potentially be split-colors.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 

Returns:
    tuple: 

    color1 (LinearColor): 

    color2 (LinearColor): 

    color3 (LinearColor): 

    tri_has_valid_vertex_colors (bool): will be returned true if TriangleID exists in TargetMesh and has Vertex Colors set

<a id="unreal.GeometryScript_MeshQueries.get_triangle_u_vs"></a>

#### get_triangle_u_vs

```python
@classmethod
def get_triangle_u_vs(
        cls, target_mesh: DynamicMesh, uv_set_index: int,
        triangle_id: int) -> Tuple[Vector2D, Vector2D, Vector2D, bool]
```

X.get_triangle_u_vs(target_mesh, uv_set_index, triangle_id) -> (uv1=Vector2D, uv2=Vector2D, uv3=Vector2D, have_valid_u_vs=bool)
Returns the UV values associated with the three vertices of the triangle in the specified UV Channel.
If the Triangle does not exist in the mesh or if no UVs are set in the specified UV Channel for the triangle, the resulting values will be (0,0) and bHaveValidUVs will be set to false.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    triangle_id (int32): 

Returns:
    tuple: 

    uv1 (Vector2D): 

    uv2 (Vector2D): 

    uv3 (Vector2D): 

    have_valid_u_vs (bool):

<a id="unreal.GeometryScript_MeshQueries.get_triangle_positions"></a>

#### get_triangle_positions

```python
@classmethod
def get_triangle_positions(
        cls, target_mesh: DynamicMesh,
        triangle_id: int) -> Tuple[bool, Vector, Vector, Vector]
```

X.get_triangle_positions(target_mesh, triangle_id) -> (is_valid_triangle=bool, vertex1=Vector, vertex2=Vector, vertex3=Vector)
* Returns the 3D positions (in the mesh local space) of the three vertices of the requested triangle.
* If the Triangle ID is not an element of the Target Mesh, all three vertices will be returned as (0, 0, 0) and bIsValidTriangle will be set to false.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 

Returns:
    tuple: 

    is_valid_triangle (bool): 

    vertex1 (Vector): 

    vertex2 (Vector): 

    vertex3 (Vector):

<a id="unreal.GeometryScript_MeshQueries.get_triangle_normal_tangents"></a>

#### get_triangle_normal_tangents

```python
@classmethod
def get_triangle_normal_tangents(
    cls, target_mesh: DynamicMesh, triangle_id: int
) -> Tuple[DynamicMesh, bool, GeometryScriptTriangle, GeometryScriptTriangle,
           GeometryScriptTriangle]
```

X.get_triangle_normal_tangents(target_mesh, triangle_id) -> (DynamicMesh, tri_has_valid_elements=bool, normals=GeometryScriptTriangle, tangents=GeometryScriptTriangle, bi_tangents=GeometryScriptTriangle)
For the specified Triangle ID of the TargetMesh, get the Normal and Tangent vectors at each vertex of the Triangle.
These Normals/Tangents will be taken from the Normal and Tangents Overlays, i.e. they will potentially be split-normals.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 

Returns:
    tuple: 

    tri_has_valid_elements (bool): will be returned true if TriangleID exists in TargetMesh and has Normals and Tangents set.

    normals (GeometryScriptTriangle): 

    tangents (GeometryScriptTriangle): 

    bi_tangents (GeometryScriptTriangle):

<a id="unreal.GeometryScript_MeshQueries.get_triangle_normals"></a>

#### get_triangle_normals

```python
@classmethod
def get_triangle_normals(
        cls, target_mesh: DynamicMesh,
        triangle_id: int) -> Tuple[DynamicMesh, Vector, Vector, Vector, bool]
```

X.get_triangle_normals(target_mesh, triangle_id) -> (DynamicMesh, normal1=Vector, normal2=Vector, normal3=Vector, tri_has_valid_normals=bool)
For the specified TriangleID of the Target Mesh, get the Normal vectors at each vertex of the Triangle.
These Normals will be taken from the Normal Overlay, i.e. they will potentially be split-normals.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 

Returns:
    tuple: 

    normal1 (Vector): 

    normal2 (Vector): 

    normal3 (Vector): 

    tri_has_valid_normals (bool): will be returned true if TriangleID exists in TargetMesh and has Normals set.

<a id="unreal.GeometryScript_MeshQueries.get_triangle_indices"></a>

#### get_triangle_indices

```python
@classmethod
def get_triangle_indices(cls, target_mesh: DynamicMesh,
                         triangle_id: int) -> Tuple[IntVector, bool]
```

X.get_triangle_indices(target_mesh, triangle_id) -> (IntVector, is_valid_triangle=bool)
Returns the Vertex ID triplet for the specified Triangle.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): indicates the triangle to query on the Target Mesh.

Returns:
    bool: 

    is_valid_triangle (bool): will be false on return if the Triangle ID does not exist in the Target Mesh, in that case the returned vertex triplet will be (-1, -1, -1).

<a id="unreal.GeometryScript_MeshQueries.get_triangle_face_normal"></a>

#### get_triangle_face_normal

```python
@classmethod
def get_triangle_face_normal(cls, target_mesh: DynamicMesh,
                             triangle_id: int) -> Tuple[Vector, bool]
```

X.get_triangle_face_normal(target_mesh, triangle_id) -> (Vector, is_valid_triangle=bool)
Get Triangle Face Normal

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.GeometryScript_MeshQueries.get_num_vertex_i_ds"></a>

#### get_num_vertex_i_ds

```python
@classmethod
def get_num_vertex_i_ds(cls, target_mesh: DynamicMesh) -> int
```

X.get_num_vertex_i_ds(target_mesh) -> int32
Gets the number of Vertex IDs in the mesh, which may be larger than the Vertex Count, if the mesh is not dense (e.g.  after deleting vertices).

Args:
    target_mesh (DynamicMesh): 

Returns:
    int32:

<a id="unreal.GeometryScript_MeshQueries.get_num_uv_sets"></a>

#### get_num_uv_sets

```python
@classmethod
def get_num_uv_sets(cls, target_mesh: DynamicMesh) -> int
```

X.get_num_uv_sets(target_mesh) -> int32
Gets the number of UV Channels on the Target Mesh.

Args:
    target_mesh (DynamicMesh): 

Returns:
    int32:

<a id="unreal.GeometryScript_MeshQueries.get_num_uv_islands"></a>

#### get_num_uv_islands

```python
@classmethod
def get_num_uv_islands(cls, target_mesh: DynamicMesh,
                       uv_channel: int) -> Tuple[int, bool]
```

X.get_num_uv_islands(target_mesh, uv_channel) -> (int32, is_valid_uv_channel=bool)
Returns the number of UV islands in a given UV channel.

Args:
    target_mesh (DynamicMesh): The mesh to query.
    uv_channel (int32): The UV channel to query

Returns:
    bool: The number of UV islands

    is_valid_uv_channel (bool): True, if the mesh has UVs for the given UVSetIndex.

<a id="unreal.GeometryScript_MeshQueries.get_num_triangle_i_ds"></a>

#### get_num_triangle_i_ds

```python
@classmethod
def get_num_triangle_i_ds(cls, target_mesh: DynamicMesh) -> int
```

X.get_num_triangle_i_ds(target_mesh) -> int32
Gets the number of Triangle IDs in the mesh. This may be larger than the Triangle Count if the mesh is not dense, even after deleting triangles.

Args:
    target_mesh (DynamicMesh): 

Returns:
    int32:

<a id="unreal.GeometryScript_MeshQueries.get_num_open_border_loops"></a>

#### get_num_open_border_loops

```python
@classmethod
def get_num_open_border_loops(cls,
                              target_mesh: DynamicMesh) -> Tuple[int, bool]
```

X.get_num_open_border_loops(target_mesh) -> (int32, ambiguous_topology_found=bool)
Returns the number of open border loops, such as "holes" in the mesh.

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool: 

    ambiguous_topology_found (bool):

<a id="unreal.GeometryScript_MeshQueries.get_num_open_border_edges"></a>

#### get_num_open_border_edges

```python
@classmethod
def get_num_open_border_edges(cls, target_mesh: DynamicMesh) -> int
```

X.get_num_open_border_edges(target_mesh) -> int32
Returns the number of topological boundary edges in the mesh, i.e counts edges that only have one adjacent triangle.

Args:
    target_mesh (DynamicMesh): 

Returns:
    int32:

<a id="unreal.GeometryScript_MeshQueries.get_num_extended_polygroup_layers"></a>

#### get_num_extended_polygroup_layers

```python
@classmethod
def get_num_extended_polygroup_layers(cls, target_mesh: DynamicMesh) -> int
```

X.get_num_extended_polygroup_layers(target_mesh) -> int32
Returns the count of extended PolyGroup Layers.

Args:
    target_mesh (DynamicMesh): 

Returns:
    int32:

<a id="unreal.GeometryScript_MeshQueries.get_num_connected_components"></a>

#### get_num_connected_components

```python
@classmethod
def get_num_connected_components(cls, target_mesh: DynamicMesh) -> int
```

X.get_num_connected_components(target_mesh) -> int32
Returns the number of separate connected components in the mesh, such as "triangle patches" internally connected by shared edges.

Args:
    target_mesh (DynamicMesh): 

Returns:
    int32:

<a id="unreal.GeometryScript_MeshQueries.get_mesh_volume_area_center"></a>

#### get_mesh_volume_area_center

```python
@classmethod
def get_mesh_volume_area_center(
        cls, target_mesh: DynamicMesh) -> Tuple[float, float, Vector]
```

X.get_mesh_volume_area_center(target_mesh) -> (surface_area=float, volume=float, center_of_mass=Vector)
Computes the volume, area and center-of-mass of the mesh.

Args:
    target_mesh (DynamicMesh): 

Returns:
    tuple: 

    surface_area (float): 

    volume (float): 

    center_of_mass (Vector):

<a id="unreal.GeometryScript_MeshQueries.get_mesh_volume_area"></a>

#### get_mesh_volume_area

```python
@classmethod
def get_mesh_volume_area(cls, target_mesh: DynamicMesh) -> Tuple[float, float]
```

X.get_mesh_volume_area(target_mesh) -> (surface_area=float, volume=float)
Computes the volume and area of the mesh.

Args:
    target_mesh (DynamicMesh): 

Returns:
    tuple: 

    surface_area (float): 

    volume (float):

<a id="unreal.GeometryScript_MeshQueries.get_mesh_uv_area"></a>

#### get_mesh_uv_area

```python
@classmethod
def get_mesh_uv_area(cls, target_mesh: DynamicMesh,
                     uv_channel: int) -> Tuple[float, bool]
```

X.get_mesh_uv_area(target_mesh, uv_channel) -> (double, is_valid_uv_channel=bool)
Gets the area of triangles in UV space for the given UV Channel.

Args:
    target_mesh (DynamicMesh): The mesh to query.
    uv_channel (int32): The UV channel to query

Returns:
    bool: The number of UV islands

    is_valid_uv_channel (bool): True, if the mesh has UVs for the given UVSetIndex.

<a id="unreal.GeometryScript_MeshQueries.get_mesh_info_string"></a>

#### get_mesh_info_string

```python
@classmethod
def get_mesh_info_string(cls, target_mesh: DynamicMesh) -> str
```

X.get_mesh_info_string(target_mesh) -> str
Returns information about the Target Mesh, such as the vertex and triangle count as well as some attribute information.

Args:
    target_mesh (DynamicMesh): 

Returns:
    str:

<a id="unreal.GeometryScript_MeshQueries.get_mesh_has_attribute_set"></a>

#### get_mesh_has_attribute_set

```python
@classmethod
def get_mesh_has_attribute_set(cls, target_mesh: DynamicMesh) -> bool
```

X.get_mesh_has_attribute_set(target_mesh) -> bool
Returns true if the Target Mesh has attributes enabled.

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.get_mesh_bounding_box"></a>

#### get_mesh_bounding_box

```python
@classmethod
def get_mesh_bounding_box(cls, target_mesh: DynamicMesh) -> Box
```

X.get_mesh_bounding_box(target_mesh) -> Box
Computes the bounding box of the mesh vertices in the local space of the mesh.

Args:
    target_mesh (DynamicMesh): 

Returns:
    Box:

<a id="unreal.GeometryScript_MeshQueries.get_is_dense_mesh"></a>

#### get_is_dense_mesh

```python
@classmethod
def get_is_dense_mesh(cls, target_mesh: DynamicMesh) -> bool
```

X.get_is_dense_mesh(target_mesh) -> bool
Returns true if the mesh is dense. For example, no gaps in Vertex IDs or Triangle IDs.
Note if a mesh is not dense, the Compact Mesh node can be used to removed the gaps.

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.get_is_closed_mesh"></a>

#### get_is_closed_mesh

```python
@classmethod
def get_is_closed_mesh(cls, target_mesh: DynamicMesh) -> bool
```

X.get_is_closed_mesh(target_mesh) -> bool
Returns true if the mesh is closed, such as no topological boundary edges.

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.get_interpolated_triangle_vertex_color"></a>

#### get_interpolated_triangle_vertex_color

```python
@classmethod
def get_interpolated_triangle_vertex_color(
        cls, target_mesh: DynamicMesh, triangle_id: int,
        barycentric_coords: Vector,
        default_color: LinearColor) -> Tuple[DynamicMesh, bool, LinearColor]
```

X.get_interpolated_triangle_vertex_color(target_mesh, triangle_id, barycentric_coords, default_color) -> (DynamicMesh, tri_has_valid_vertex_colors=bool, interpolated_color=LinearColor)
Compute the interpolated Vertex Color (A*Color1 + B*Color2 + C*Color3), where (A,B,C)=BarycentricCoords and the Colors are taken
from the specified TriangleID in the Vertex Color layer of the TargetMesh.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 
    barycentric_coords (Vector): 
    default_color (LinearColor): 

Returns:
    tuple: 

    tri_has_valid_vertex_colors (bool): will be returned true if TriangleID exists in TargetMesh and has Colors set, and otherwise will be returned false

    interpolated_color (LinearColor):

<a id="unreal.GeometryScript_MeshQueries.get_interpolated_triangle_uv"></a>

#### get_interpolated_triangle_uv

```python
@classmethod
def get_interpolated_triangle_uv(
        cls, target_mesh: DynamicMesh, uv_set_index: int, triangle_id: int,
        barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector2D]
```

X.get_interpolated_triangle_uv(target_mesh, uv_set_index, triangle_id, barycentric_coords) -> (DynamicMesh, tri_has_valid_u_vs=bool, interpolated_uv=Vector2D)
Compute the interpolated UV (A*UV1+ B*UV2+ C*UV3), where (A,B,C)=BarycentricCoords and the UV positions are taken
from the specified TriangleID in the specified UVSet of the TargetMesh.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    triangle_id (int32): 
    barycentric_coords (Vector): 

Returns:
    tuple: 

    tri_has_valid_u_vs (bool): 

    interpolated_uv (Vector2D):

<a id="unreal.GeometryScript_MeshQueries.get_interpolated_triangle_position"></a>

#### get_interpolated_triangle_position

```python
@classmethod
def get_interpolated_triangle_position(
        cls, target_mesh: DynamicMesh, triangle_id: int,
        barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector]
```

X.get_interpolated_triangle_position(target_mesh, triangle_id, barycentric_coords) -> (DynamicMesh, is_valid_triangle=bool, interpolated_position=Vector)
Compute the interpolated Position (A*Vertex1 + B*Vertex2 + C*Vertex3), where (A,B,C)=BarycentricCoords and the Vertex positions are taken
from the specified TriangleID of the TargetMesh.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 
    barycentric_coords (Vector): 

Returns:
    tuple: 

    is_valid_triangle (bool): will be returned true if TriangleID exists in TargetMesh, and otherwise will be returned false

    interpolated_position (Vector):

<a id="unreal.GeometryScript_MeshQueries.get_interpolated_triangle_normal_tangents"></a>

#### get_interpolated_triangle_normal_tangents

```python
@classmethod
def get_interpolated_triangle_normal_tangents(
    cls, target_mesh: DynamicMesh, triangle_id: int, barycentric_coords: Vector
) -> Tuple[DynamicMesh, bool, Vector, Vector, Vector]
```

X.get_interpolated_triangle_normal_tangents(target_mesh, triangle_id, barycentric_coords) -> (DynamicMesh, tri_has_valid_elements=bool, interpolated_normal=Vector, interpolated_tangent=Vector, interpolated_bi_tangent=Vector)
Compute the interpolated Normal and Tangents for the specified specified TriangleID in the Normal and Tangent attributes of the TargetMesh.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 
    barycentric_coords (Vector): 

Returns:
    tuple: 

    tri_has_valid_elements (bool): will be returned true if TriangleID exists in TargetMesh and has Normals and Tangents set, and otherwise will be returned false

    interpolated_normal (Vector): 

    interpolated_tangent (Vector): 

    interpolated_bi_tangent (Vector):

<a id="unreal.GeometryScript_MeshQueries.get_interpolated_triangle_normal"></a>

#### get_interpolated_triangle_normal

```python
@classmethod
def get_interpolated_triangle_normal(
        cls, target_mesh: DynamicMesh, triangle_id: int,
        barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector]
```

X.get_interpolated_triangle_normal(target_mesh, triangle_id, barycentric_coords) -> (DynamicMesh, tri_has_valid_normals=bool, interpolated_normal=Vector)
Compute the interpolated Normal (A*Normal1 + B*Normal2 + C*Normal3), where (A,B,C)=BarycentricCoords and the Normals are taken
from the specified TriangleID in the Normal layer of the TargetMesh.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 
    barycentric_coords (Vector): 

Returns:
    tuple: 

    tri_has_valid_normals (bool): will be returned true if TriangleID exists in TargetMesh and has Normals set, and otherwise will be returned false.

    interpolated_normal (Vector):

<a id="unreal.GeometryScript_MeshQueries.get_has_vertex_id_gaps"></a>

#### get_has_vertex_id_gaps

```python
@classmethod
def get_has_vertex_id_gaps(cls, target_mesh: DynamicMesh) -> bool
```

X.get_has_vertex_id_gaps(target_mesh) -> bool
Returns true if there are gaps in the Vertex ID list. For example, Get Number of Vertex IDs is greater than Get Vertex Count.

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.get_has_vertex_colors"></a>

#### get_has_vertex_colors

```python
@classmethod
def get_has_vertex_colors(cls, target_mesh: DynamicMesh) -> bool
```

X.get_has_vertex_colors(target_mesh) -> bool


Args:
    target_mesh (DynamicMesh): 

Returns:
    bool: true if the TargetMesh has the Vertex Colors attribute enabled

<a id="unreal.GeometryScript_MeshQueries.get_has_triangle_normals"></a>

#### get_has_triangle_normals

```python
@classmethod
def get_has_triangle_normals(cls, target_mesh: DynamicMesh) -> bool
```

X.get_has_triangle_normals(target_mesh) -> bool


Args:
    target_mesh (DynamicMesh): 

Returns:
    bool: true if the TargetMesh has the Normals Attribute enabled (which allows for storing split normals)

<a id="unreal.GeometryScript_MeshQueries.get_has_triangle_id_gaps"></a>

#### get_has_triangle_id_gaps

```python
@classmethod
def get_has_triangle_id_gaps(cls, target_mesh: DynamicMesh) -> bool
```

X.get_has_triangle_id_gaps(target_mesh) -> bool
Returns true if there are gaps in the Triangle ID list, such that Get Num Triangle IDs is greater than Get Triangle Count.

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.get_has_polygroups"></a>

#### get_has_polygroups

```python
@classmethod
def get_has_polygroups(cls, target_mesh: DynamicMesh) -> bool
```

X.get_has_polygroups(target_mesh) -> bool
Returns true if the mesh has a standard PolyGroup Layer.

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.get_has_material_i_ds"></a>

#### get_has_material_i_ds

```python
@classmethod
def get_has_material_i_ds(cls, target_mesh: DynamicMesh) -> bool
```

X.get_has_material_i_ds(target_mesh) -> bool
Returns true if the mesh has Material IDs available/enabled.

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool:

<a id="unreal.GeometryScript_MeshQueries.get_all_vertex_positions_at_edges"></a>

#### get_all_vertex_positions_at_edges

```python
@classmethod
def get_all_vertex_positions_at_edges(
    cls, target_mesh: DynamicMesh, edge_i_ds: GeometryScriptIndexList
) -> Tuple[DynamicMesh, GeometryScriptVectorList, GeometryScriptVectorList]
```

X.get_all_vertex_positions_at_edges(target_mesh, edge_i_ds) -> (DynamicMesh, start=GeometryScriptVectorList, end=GeometryScriptVectorList)
Returns the vertex positions for each edge in the given index list.

Args:
    target_mesh (DynamicMesh): The mesh to query
    edge_i_ds (GeometryScriptIndexList): The edge IDs to query

Returns:
    tuple: The target mesh that was queried

    start (GeometryScriptVectorList): The output list of start vertex positions

    end (GeometryScriptVectorList): The output list of end vertex positions

<a id="unreal.GeometryScript_MeshQueries.get_all_vertex_positions"></a>

#### get_all_vertex_positions

```python
@classmethod
def get_all_vertex_positions(
        cls, target_mesh: DynamicMesh,
        skip_gaps: bool) -> Tuple[DynamicMesh, GeometryScriptVectorList, bool]
```

X.get_all_vertex_positions(target_mesh, skip_gaps) -> (DynamicMesh, position_list=GeometryScriptVectorList, has_vertex_id_gaps=bool)
Returns a Vector List of all the mesh vertex 3D positions (possibly large!).

Args:
    target_mesh (DynamicMesh): 
    skip_gaps (bool): if false there will be a one-to-one correspondence between Vertex ID and entries in the Position List where a zero vector (0,0,0) will correspond to Vertex IDs not found in the Target Mesh.

Returns:
    tuple: 

    position_list (GeometryScriptVectorList): 

    has_vertex_id_gaps (bool): will be false if the mesh had no gaps in Vertex IDs or if bSkipGaps was set to true.

<a id="unreal.GeometryScript_MeshQueries.get_all_vertex_i_ds"></a>

#### get_all_vertex_i_ds

```python
@classmethod
def get_all_vertex_i_ds(
    cls, target_mesh: DynamicMesh
) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

X.get_all_vertex_i_ds(target_mesh) -> (DynamicMesh, vertex_id_list=GeometryScriptIndexList, has_vertex_id_gaps=bool)
Returns an IndexList of all Vertex IDs in mesh.

Args:
    target_mesh (DynamicMesh): 

Returns:
    tuple: 

    vertex_id_list (GeometryScriptIndexList): 

    has_vertex_id_gaps (bool):

<a id="unreal.GeometryScript_MeshQueries.get_all_uv_seam_edges"></a>

#### get_all_uv_seam_edges

```python
@classmethod
def get_all_uv_seam_edges(
        cls, target_mesh: DynamicMesh, uv_set_index: int
) -> Tuple[DynamicMesh, bool, GeometryScriptIndexList]
```

X.get_all_uv_seam_edges(target_mesh, uv_set_index) -> (DynamicMesh, have_valid_u_vs=bool, element_i_ds=GeometryScriptIndexList)
Returns all edge element IDs that are UV seam edges for a given UV channel.

Args:
    target_mesh (DynamicMesh): The mesh to query.
    uv_set_index (int32): The UV channel to query

Returns:
    tuple: The target mesh that was queried.

    have_valid_u_vs (bool): True, if the mesh has UVs for the given UVSetIndex.

    element_i_ds (GeometryScriptIndexList): The returned edge element IDs

<a id="unreal.GeometryScript_MeshQueries.get_all_triangle_indices"></a>

#### get_all_triangle_indices

```python
@classmethod
def get_all_triangle_indices(
        cls, target_mesh: DynamicMesh, skip_gaps: bool
) -> Tuple[DynamicMesh, GeometryScriptTriangleList, bool]
```

X.get_all_triangle_indices(target_mesh, skip_gaps) -> (DynamicMesh, triangle_list=GeometryScriptTriangleList, has_triangle_id_gaps=bool)
* Returns a TriangleList of all Triangle Vertex ID triplets in a mesh.
*

Args:
    target_mesh (DynamicMesh): 
    skip_gaps (bool): if false there will be a one-to-one correspondence between Triangle ID and entries in the triangle list and invalid triplets of (-1,-1,-1) will correspond to Triangle IDs not found in the Target Mesh. *

Returns:
    tuple: 

    triangle_list (GeometryScriptTriangleList): 

    has_triangle_id_gaps (bool): will be false on return if the mesh had no gaps in Triangle IDs or if bSkipGaps was set to true.

<a id="unreal.GeometryScript_MeshQueries.get_all_triangle_i_ds"></a>

#### get_all_triangle_i_ds

```python
@classmethod
def get_all_triangle_i_ds(
    cls, target_mesh: DynamicMesh
) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

X.get_all_triangle_i_ds(target_mesh) -> (DynamicMesh, triangle_id_list=GeometryScriptIndexList, has_triangle_id_gaps=bool)
Returns an Index List of all Triangle IDs in a mesh.

Args:
    target_mesh (DynamicMesh): 

Returns:
    tuple: 

    triangle_id_list (GeometryScriptIndexList): 

    has_triangle_id_gaps (bool): will be true on return if there are breaks in the sequential numeration of Triangle IDs, as would happen after deleting triangles.

<a id="unreal.GeometryScript_MeshQueries.get_all_split_u_vs_at_vertex"></a>

#### get_all_split_u_vs_at_vertex

```python
@classmethod
def get_all_split_u_vs_at_vertex(
        cls, target_mesh: DynamicMesh, uv_set_index: int, vertex_id: int
) -> Tuple[DynamicMesh, Array[int], Array[Vector2D], bool]
```

X.get_all_split_u_vs_at_vertex(target_mesh, uv_set_index, vertex_id) -> (DynamicMesh, element_i_ds=Array[int32], element_u_vs=Array[Vector2D], have_valid_u_vs=bool)
Returns the unique UV element IDs and values associated with the mesh vertex, in the specified UV Channel.
If the Vertex or UV channel does not exist, the arrays will be empty and bHaveValidUVs will be set to false.

Args:
    target_mesh (DynamicMesh): 
    uv_set_index (int32): 
    vertex_id (int32): 

Returns:
    tuple: 

    element_i_ds (Array[int32]): 

    element_u_vs (Array[Vector2D]): 

    have_valid_u_vs (bool):

<a id="unreal.GeometryScript_MeshQueries.compute_triangle_barycentric_coords"></a>

#### compute_triangle_barycentric_coords

```python
@classmethod
def compute_triangle_barycentric_coords(
        cls, target_mesh: DynamicMesh, triangle_id: int, point: Vector
) -> Tuple[DynamicMesh, bool, Vector, Vector, Vector, Vector]
```

X.compute_triangle_barycentric_coords(target_mesh, triangle_id, point) -> (DynamicMesh, is_valid_triangle=bool, vertex1=Vector, vertex2=Vector, vertex3=Vector, barycentric_coords=Vector)
Compute the barycentric coordinates (A,B,C) of the Point relative to the specified TriangleID of the TargetMesh.
The properties of barycentric coordinates are such that A,B,C are all positive, A+B+C=1.0, and A*Vertex1 + B*Vertex2 + C*Vertex3 = Point.
So, the barycentric coordinates can be used to smoothly interpolate/blend any other per-triangle-vertex quantities.
The Point must lie in the plane of the Triangle, otherwise the coordinates are somewhat meaningless (but clamped to 0-1 range to avoid catastrophic errors)
The Positions of the Triangle Vertices are also returned for convenience (similar to GetTrianglePositions)

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 
    point (Vector): 

Returns:
    tuple: 

    is_valid_triangle (bool): will be returned true if TriangleID exists in TargetMesh, and otherwise will be returned false

    vertex1 (Vector): 

    vertex2 (Vector): 

    vertex3 (Vector): 

    barycentric_coords (Vector):

<a id="unreal.GeometryScript_Remeshing"></a>