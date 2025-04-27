## MeshDescriptionBase Objects

```python
class MeshDescriptionBase(Object)
```

Mesh Description Base

**C++ Source:**

- **Module**: MeshDescription
- **File**: MeshDescriptionBase.h

<a id="unreal.MeshDescriptionBase.set_vertex_position"></a>

#### set_vertex_position

```python
def set_vertex_position(vertex_id: VertexID, position: Vector) -> None
```

x.set_vertex_position(vertex_id, position) -> None
Sets a vertex position

Args:
    vertex_id (VertexID): 
    position (Vector):

<a id="unreal.MeshDescriptionBase.set_polygon_vertex_instances"></a>

#### set_polygon_vertex_instances

```python
def set_polygon_vertex_instances(
        polygon_id: PolygonID,
        vertex_instance_i_ds: Array[VertexInstanceID]) -> None
```

x.set_polygon_vertex_instances(polygon_id, vertex_instance_i_ds) -> None
Set the vertex instance at the given index around the polygon to the new value

Args:
    polygon_id (PolygonID): 
    vertex_instance_i_ds (Array[VertexInstanceID]):

<a id="unreal.MeshDescriptionBase.set_polygon_polygon_group"></a>

#### set_polygon_polygon_group

```python
def set_polygon_polygon_group(polygon_id: PolygonID,
                              polygon_group_id: PolygonGroupID) -> None
```

x.set_polygon_polygon_group(polygon_id, polygon_group_id) -> None
Sets the polygon group associated with a polygon

Args:
    polygon_id (PolygonID): 
    polygon_group_id (PolygonGroupID):

<a id="unreal.MeshDescriptionBase.reverse_polygon_facing"></a>

#### reverse_polygon_facing

```python
def reverse_polygon_facing(polygon_id: PolygonID) -> None
```

x.reverse_polygon_facing(polygon_id) -> None
Reverse the winding order of the vertices of this polygon

Args:
    polygon_id (PolygonID):

<a id="unreal.MeshDescriptionBase.reserve_new_vertices"></a>

#### reserve_new_vertices

```python
def reserve_new_vertices(number_of_new_vertices: int) -> None
```

x.reserve_new_vertices(number_of_new_vertices) -> None
Reserves space for this number of new vertices

Args:
    number_of_new_vertices (int32):

<a id="unreal.MeshDescriptionBase.reserve_new_vertex_instances"></a>

#### reserve_new_vertex_instances

```python
def reserve_new_vertex_instances(number_of_new_vertex_instances: int) -> None
```

x.reserve_new_vertex_instances(number_of_new_vertex_instances) -> None
Reserves space for this number of new vertex instances

Args:
    number_of_new_vertex_instances (int32):

<a id="unreal.MeshDescriptionBase.reserve_new_triangles"></a>

#### reserve_new_triangles

```python
def reserve_new_triangles(number_of_new_triangles: int) -> None
```

x.reserve_new_triangles(number_of_new_triangles) -> None
Reserves space for this number of new triangles

Args:
    number_of_new_triangles (int32):

<a id="unreal.MeshDescriptionBase.reserve_new_polygons"></a>

#### reserve_new_polygons

```python
def reserve_new_polygons(number_of_new_polygons: int) -> None
```

x.reserve_new_polygons(number_of_new_polygons) -> None
Reserves space for this number of new polygons

Args:
    number_of_new_polygons (int32):

<a id="unreal.MeshDescriptionBase.reserve_new_polygon_groups"></a>

#### reserve_new_polygon_groups

```python
def reserve_new_polygon_groups(number_of_new_polygon_groups: int) -> None
```

x.reserve_new_polygon_groups(number_of_new_polygon_groups) -> None
Reserves space for this number of new polygon groups

Args:
    number_of_new_polygon_groups (int32):

<a id="unreal.MeshDescriptionBase.reserve_new_edges"></a>

#### reserve_new_edges

```python
def reserve_new_edges(number_of_new_edges: int) -> None
```

x.reserve_new_edges(number_of_new_edges) -> None
Reserves space for this number of new edges

Args:
    number_of_new_edges (int32):

<a id="unreal.MeshDescriptionBase.is_vertex_valid"></a>

#### is_vertex_valid

```python
def is_vertex_valid(vertex_id: VertexID) -> bool
```

x.is_vertex_valid(vertex_id) -> bool
Returns whether the passed vertex ID is valid

Args:
    vertex_id (VertexID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_vertex_orphaned"></a>

#### is_vertex_orphaned

```python
def is_vertex_orphaned(vertex_id: VertexID) -> bool
```

x.is_vertex_orphaned(vertex_id) -> bool
Returns whether a given vertex is orphaned, i.e. it doesn't form part of any polygon

Args:
    vertex_id (VertexID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_vertex_instance_valid"></a>

#### is_vertex_instance_valid

```python
def is_vertex_instance_valid(vertex_instance_id: VertexInstanceID) -> bool
```

x.is_vertex_instance_valid(vertex_instance_id) -> bool
Returns whether the passed vertex instance ID is valid

Args:
    vertex_instance_id (VertexInstanceID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_triangle_valid"></a>

#### is_triangle_valid

```python
def is_triangle_valid(triangle_id: TriangleID) -> bool
```

x.is_triangle_valid(triangle_id) -> bool
Returns whether the passed triangle ID is valid

Args:
    triangle_id (TriangleID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_triangle_part_of_ngon"></a>

#### is_triangle_part_of_ngon

```python
def is_triangle_part_of_ngon(triangle_id: TriangleID) -> bool
```

x.is_triangle_part_of_ngon(triangle_id) -> bool
Determines if this triangle is part of an n-gon

Args:
    triangle_id (TriangleID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_polygon_valid"></a>

#### is_polygon_valid

```python
def is_polygon_valid(polygon_id: PolygonID) -> bool
```

x.is_polygon_valid(polygon_id) -> bool
Returns whether the passed polygon ID is valid

Args:
    polygon_id (PolygonID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_polygon_group_valid"></a>

#### is_polygon_group_valid

```python
def is_polygon_group_valid(polygon_group_id: PolygonGroupID) -> bool
```

x.is_polygon_group_valid(polygon_group_id) -> bool
Returns whether the passed polygon group ID is valid

Args:
    polygon_group_id (PolygonGroupID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_empty"></a>

#### is_empty

```python
def is_empty() -> bool
```

x.is_empty() -> bool
Return whether the mesh description is empty

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_edge_valid"></a>

#### is_edge_valid

```python
def is_edge_valid(edge_id: EdgeID) -> bool
```

x.is_edge_valid(edge_id) -> bool
Returns whether the passed edge ID is valid

Args:
    edge_id (EdgeID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_edge_internal_to_polygon"></a>

#### is_edge_internal_to_polygon

```python
def is_edge_internal_to_polygon(edge_id: EdgeID,
                                polygon_id: PolygonID) -> bool
```

x.is_edge_internal_to_polygon(edge_id, polygon_id) -> bool
Determine whether a given edge is an internal edge between triangles of a specific polygon

Args:
    edge_id (EdgeID): 
    polygon_id (PolygonID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.is_edge_internal"></a>

#### is_edge_internal

```python
def is_edge_internal(edge_id: EdgeID) -> bool
```

x.is_edge_internal(edge_id) -> bool
Determine whether a given edge is an internal edge between triangles of a polygon

Args:
    edge_id (EdgeID): 

Returns:
    bool:

<a id="unreal.MeshDescriptionBase.get_vertex_vertex_instances"></a>

#### get_vertex_vertex_instances

```python
def get_vertex_vertex_instances(
        vertex_id: VertexID) -> Array[VertexInstanceID]
```

x.get_vertex_vertex_instances(vertex_id) -> Array[VertexInstanceID]
Returns reference to an array of VertexInstance IDs instanced from this vertex

Args:
    vertex_id (VertexID): 

Returns:
    Array[VertexInstanceID]: 

    out_vertex_instance_i_ds (Array[VertexInstanceID]):

<a id="unreal.MeshDescriptionBase.get_vertex_position"></a>

#### get_vertex_position

```python
def get_vertex_position(vertex_id: VertexID) -> Vector
```

x.get_vertex_position(vertex_id) -> Vector
Gets a vertex position

Args:
    vertex_id (VertexID): 

Returns:
    Vector:

<a id="unreal.MeshDescriptionBase.get_vertex_pair_edge"></a>

#### get_vertex_pair_edge

```python
def get_vertex_pair_edge(vertex_id0: VertexID, vertex_id1: VertexID) -> EdgeID
```

x.get_vertex_pair_edge(vertex_id0, vertex_id1) -> EdgeID
Returns the edge ID defined by the two given vertex IDs, if there is one; otherwise INDEX_NONE

Args:
    vertex_id0 (VertexID): 
    vertex_id1 (VertexID): 

Returns:
    EdgeID:

<a id="unreal.MeshDescriptionBase.get_vertex_instance_vertex"></a>

#### get_vertex_instance_vertex

```python
def get_vertex_instance_vertex(
        vertex_instance_id: VertexInstanceID) -> VertexID
```

x.get_vertex_instance_vertex(vertex_instance_id) -> VertexID
Returns the vertex ID associated with the given vertex instance

Args:
    vertex_instance_id (VertexInstanceID): 

Returns:
    VertexID:

<a id="unreal.MeshDescriptionBase.get_vertex_instance_pair_edge"></a>

#### get_vertex_instance_pair_edge

```python
def get_vertex_instance_pair_edge(
        vertex_instance_id0: VertexInstanceID,
        vertex_instance_id1: VertexInstanceID) -> EdgeID
```

x.get_vertex_instance_pair_edge(vertex_instance_id0, vertex_instance_id1) -> EdgeID
Returns the edge ID defined by the two given vertex instance IDs, if there is one; otherwise INDEX_NONE

Args:
    vertex_instance_id0 (VertexInstanceID): 
    vertex_instance_id1 (VertexInstanceID): 

Returns:
    EdgeID:

<a id="unreal.MeshDescriptionBase.get_vertex_instance_for_triangle_vertex"></a>

#### get_vertex_instance_for_triangle_vertex

```python
def get_vertex_instance_for_triangle_vertex(
        triangle_id: TriangleID, vertex_id: VertexID) -> VertexInstanceID
```

x.get_vertex_instance_for_triangle_vertex(triangle_id, vertex_id) -> VertexInstanceID
Return the vertex instance which corresponds to the given vertex on the given triangle, or INDEX_NONE

Args:
    triangle_id (TriangleID): 
    vertex_id (VertexID): 

Returns:
    VertexInstanceID:

<a id="unreal.MeshDescriptionBase.get_vertex_instance_for_polygon_vertex"></a>

#### get_vertex_instance_for_polygon_vertex

```python
def get_vertex_instance_for_polygon_vertex(
        polygon_id: PolygonID, vertex_id: VertexID) -> VertexInstanceID
```

x.get_vertex_instance_for_polygon_vertex(polygon_id, vertex_id) -> VertexInstanceID
Return the vertex instance which corresponds to the given vertex on the given polygon, or INDEX_NONE

Args:
    polygon_id (PolygonID): 
    vertex_id (VertexID): 

Returns:
    VertexInstanceID:

<a id="unreal.MeshDescriptionBase.get_vertex_instance_count"></a>

#### get_vertex_instance_count

```python
def get_vertex_instance_count() -> int
```

x.get_vertex_instance_count() -> int32
Returns the number of vertex instances

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_vertex_instance_connected_triangles"></a>

#### get_vertex_instance_connected_triangles

```python
def get_vertex_instance_connected_triangles(
        vertex_instance_id: VertexInstanceID) -> Array[TriangleID]
```

x.get_vertex_instance_connected_triangles(vertex_instance_id) -> Array[TriangleID]
Returns reference to an array of Triangle IDs connected to this vertex instance

Args:
    vertex_instance_id (VertexInstanceID): 

Returns:
    Array[TriangleID]: 

    out_connected_triangle_i_ds (Array[TriangleID]):

<a id="unreal.MeshDescriptionBase.get_vertex_instance_connected_polygons"></a>

#### get_vertex_instance_connected_polygons

```python
def get_vertex_instance_connected_polygons(
        vertex_instance_id: VertexInstanceID) -> Array[PolygonID]
```

x.get_vertex_instance_connected_polygons(vertex_instance_id) -> Array[PolygonID]
Returns the polygons connected to this vertex instance

Args:
    vertex_instance_id (VertexInstanceID): 

Returns:
    Array[PolygonID]: 

    out_connected_polygon_i_ds (Array[PolygonID]):

<a id="unreal.MeshDescriptionBase.get_vertex_count"></a>

#### get_vertex_count

```python
def get_vertex_count() -> int
```

x.get_vertex_count() -> int32
Returns the number of vertices

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_vertex_connected_triangles"></a>

#### get_vertex_connected_triangles

```python
def get_vertex_connected_triangles(vertex_id: VertexID) -> Array[TriangleID]
```

x.get_vertex_connected_triangles(vertex_id) -> Array[TriangleID]
Returns the triangles connected to this vertex

Args:
    vertex_id (VertexID): 

Returns:
    Array[TriangleID]: 

    out_connected_triangle_i_ds (Array[TriangleID]):

<a id="unreal.MeshDescriptionBase.get_vertex_connected_polygons"></a>

#### get_vertex_connected_polygons

```python
def get_vertex_connected_polygons(vertex_id: VertexID) -> Array[PolygonID]
```

x.get_vertex_connected_polygons(vertex_id) -> Array[PolygonID]
Returns the polygons connected to this vertex

Args:
    vertex_id (VertexID): 

Returns:
    Array[PolygonID]: 

    out_connected_polygon_i_ds (Array[PolygonID]):

<a id="unreal.MeshDescriptionBase.get_vertex_connected_edges"></a>

#### get_vertex_connected_edges

```python
def get_vertex_connected_edges(vertex_id: VertexID) -> Array[EdgeID]
```

x.get_vertex_connected_edges(vertex_id) -> Array[EdgeID]
Returns reference to an array of Edge IDs connected to this vertex

Args:
    vertex_id (VertexID): 

Returns:
    Array[EdgeID]: 

    out_edge_i_ds (Array[EdgeID]):

<a id="unreal.MeshDescriptionBase.get_vertex_adjacent_vertices"></a>

#### get_vertex_adjacent_vertices

```python
def get_vertex_adjacent_vertices(vertex_id: VertexID) -> Array[VertexID]
```

x.get_vertex_adjacent_vertices(vertex_id) -> Array[VertexID]
Returns the vertices adjacent to this vertex

Args:
    vertex_id (VertexID): 

Returns:
    Array[VertexID]: 

    out_adjacent_vertex_i_ds (Array[VertexID]):

<a id="unreal.MeshDescriptionBase.get_triangle_vertices"></a>

#### get_triangle_vertices

```python
def get_triangle_vertices(triangle_id: TriangleID) -> Array[VertexID]
```

x.get_triangle_vertices(triangle_id) -> Array[VertexID]
Returns the vertices which define this triangle

Args:
    triangle_id (TriangleID): 

Returns:
    Array[VertexID]: 

    out_vertex_i_ds (Array[VertexID]):

<a id="unreal.MeshDescriptionBase.get_triangle_vertex_instances"></a>

#### get_triangle_vertex_instances

```python
def get_triangle_vertex_instances(
        triangle_id: TriangleID) -> Array[VertexInstanceID]
```

x.get_triangle_vertex_instances(triangle_id) -> Array[VertexInstanceID]
Get the vertex instances which define this triangle

Args:
    triangle_id (TriangleID): 

Returns:
    Array[VertexInstanceID]: 

    out_vertex_instance_i_ds (Array[VertexInstanceID]):

<a id="unreal.MeshDescriptionBase.get_triangle_vertex_instance"></a>

#### get_triangle_vertex_instance

```python
def get_triangle_vertex_instance(triangle_id: TriangleID,
                                 index: int) -> VertexInstanceID
```

x.get_triangle_vertex_instance(triangle_id, index) -> VertexInstanceID
Get the specified vertex instance by index

Args:
    triangle_id (TriangleID): 
    index (int32): 

Returns:
    VertexInstanceID:

<a id="unreal.MeshDescriptionBase.get_triangle_polygon_group"></a>

#### get_triangle_polygon_group

```python
def get_triangle_polygon_group(triangle_id: TriangleID) -> PolygonGroupID
```

x.get_triangle_polygon_group(triangle_id) -> PolygonGroupID
Get the polygon group which contains this triangle

Args:
    triangle_id (TriangleID): 

Returns:
    PolygonGroupID:

<a id="unreal.MeshDescriptionBase.get_triangle_polygon"></a>

#### get_triangle_polygon

```python
def get_triangle_polygon(triangle_id: TriangleID) -> PolygonID
```

x.get_triangle_polygon(triangle_id) -> PolygonID
Get the polygon which contains this triangle

Args:
    triangle_id (TriangleID): 

Returns:
    PolygonID:

<a id="unreal.MeshDescriptionBase.get_triangle_edges"></a>

#### get_triangle_edges

```python
def get_triangle_edges(triangle_id: TriangleID) -> Array[EdgeID]
```

x.get_triangle_edges(triangle_id) -> Array[EdgeID]
Returns the edges which define this triangle

Args:
    triangle_id (TriangleID): 

Returns:
    Array[EdgeID]: 

    out_edge_i_ds (Array[EdgeID]):

<a id="unreal.MeshDescriptionBase.get_triangle_count"></a>

#### get_triangle_count

```python
def get_triangle_count() -> int
```

x.get_triangle_count() -> int32
Returns the number of triangles

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_triangle_adjacent_triangles"></a>

#### get_triangle_adjacent_triangles

```python
def get_triangle_adjacent_triangles(
        triangle_id: TriangleID) -> Array[TriangleID]
```

x.get_triangle_adjacent_triangles(triangle_id) -> Array[TriangleID]
Returns the adjacent triangles to this triangle

Args:
    triangle_id (TriangleID): 

Returns:
    Array[TriangleID]: 

    out_triangle_i_ds (Array[TriangleID]):

<a id="unreal.MeshDescriptionBase.get_polygon_vertices"></a>

#### get_polygon_vertices

```python
def get_polygon_vertices(polygon_id: PolygonID) -> Array[VertexID]
```

x.get_polygon_vertices(polygon_id) -> Array[VertexID]
Returns the vertices which form the polygon perimeter

Args:
    polygon_id (PolygonID): 

Returns:
    Array[VertexID]: 

    out_vertex_i_ds (Array[VertexID]):

<a id="unreal.MeshDescriptionBase.get_polygon_vertex_instances"></a>

#### get_polygon_vertex_instances

```python
def get_polygon_vertex_instances(
        polygon_id: PolygonID) -> Array[VertexInstanceID]
```

x.get_polygon_vertex_instances(polygon_id) -> Array[VertexInstanceID]
Returns reference to an array of VertexInstance IDs forming the perimeter of this polygon

Args:
    polygon_id (PolygonID): 

Returns:
    Array[VertexInstanceID]: 

    out_vertex_instance_i_ds (Array[VertexInstanceID]):

<a id="unreal.MeshDescriptionBase.get_polygon_triangles"></a>

#### get_polygon_triangles

```python
def get_polygon_triangles(polygon_id: PolygonID) -> Array[TriangleID]
```

x.get_polygon_triangles(polygon_id) -> Array[TriangleID]
Return reference to an array of triangle IDs which comprise this polygon

Args:
    polygon_id (PolygonID): 

Returns:
    Array[TriangleID]: 

    out_triangle_i_ds (Array[TriangleID]):

<a id="unreal.MeshDescriptionBase.get_polygon_polygon_group"></a>

#### get_polygon_polygon_group

```python
def get_polygon_polygon_group(polygon_id: PolygonID) -> PolygonGroupID
```

x.get_polygon_polygon_group(polygon_id) -> PolygonGroupID
Return the polygon group associated with a polygon

Args:
    polygon_id (PolygonID): 

Returns:
    PolygonGroupID:

<a id="unreal.MeshDescriptionBase.get_polygon_perimeter_edges"></a>

#### get_polygon_perimeter_edges

```python
def get_polygon_perimeter_edges(polygon_id: PolygonID) -> Array[EdgeID]
```

x.get_polygon_perimeter_edges(polygon_id) -> Array[EdgeID]
Returns the edges which form the polygon perimeter

Args:
    polygon_id (PolygonID): 

Returns:
    Array[EdgeID]: 

    out_edge_i_ds (Array[EdgeID]):

<a id="unreal.MeshDescriptionBase.get_polygon_internal_edges"></a>

#### get_polygon_internal_edges

```python
def get_polygon_internal_edges(polygon_id: PolygonID) -> Array[EdgeID]
```

x.get_polygon_internal_edges(polygon_id) -> Array[EdgeID]
Populate the provided array with a list of edges which are internal to the polygon, i.e. those which separate
          constituent triangles.

Args:
    polygon_id (PolygonID): 

Returns:
    Array[EdgeID]: 

    out_edge_i_ds (Array[EdgeID]):

<a id="unreal.MeshDescriptionBase.get_polygon_group_polygons"></a>

#### get_polygon_group_polygons

```python
def get_polygon_group_polygons(
        polygon_group_id: PolygonGroupID) -> Array[PolygonID]
```

x.get_polygon_group_polygons(polygon_group_id) -> Array[PolygonID]
Returns the polygons associated with the given polygon group

Args:
    polygon_group_id (PolygonGroupID): 

Returns:
    Array[PolygonID]: 

    out_polygon_i_ds (Array[PolygonID]):

<a id="unreal.MeshDescriptionBase.get_polygon_group_count"></a>

#### get_polygon_group_count

```python
def get_polygon_group_count() -> int
```

x.get_polygon_group_count() -> int32
Returns the number of polygon groups

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_polygon_count"></a>

#### get_polygon_count

```python
def get_polygon_count() -> int
```

x.get_polygon_count() -> int32
Returns the number of polygons

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_polygon_adjacent_polygons"></a>

#### get_polygon_adjacent_polygons

```python
def get_polygon_adjacent_polygons(polygon_id: PolygonID) -> Array[PolygonID]
```

x.get_polygon_adjacent_polygons(polygon_id) -> Array[PolygonID]
Populates the passed array with adjacent polygons

Args:
    polygon_id (PolygonID): 

Returns:
    Array[PolygonID]: 

    out_polygon_i_ds (Array[PolygonID]):

<a id="unreal.MeshDescriptionBase.get_num_vertex_vertex_instances"></a>

#### get_num_vertex_vertex_instances

```python
def get_num_vertex_vertex_instances(vertex_id: VertexID) -> int
```

x.get_num_vertex_vertex_instances(vertex_id) -> int32
Returns number of vertex instances created from this vertex

Args:
    vertex_id (VertexID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_vertex_instance_connected_triangles"></a>

#### get_num_vertex_instance_connected_triangles

```python
def get_num_vertex_instance_connected_triangles(
        vertex_instance_id: VertexInstanceID) -> int
```

x.get_num_vertex_instance_connected_triangles(vertex_instance_id) -> int32
Returns the number of triangles connected to this vertex instance

Args:
    vertex_instance_id (VertexInstanceID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_vertex_instance_connected_polygons"></a>

#### get_num_vertex_instance_connected_polygons

```python
def get_num_vertex_instance_connected_polygons(
        vertex_instance_id: VertexInstanceID) -> int
```

x.get_num_vertex_instance_connected_polygons(vertex_instance_id) -> int32
Returns the number of polygons connected to this vertex instance.

Args:
    vertex_instance_id (VertexInstanceID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_vertex_connected_triangles"></a>

#### get_num_vertex_connected_triangles

```python
def get_num_vertex_connected_triangles(vertex_id: VertexID) -> int
```

x.get_num_vertex_connected_triangles(vertex_id) -> int32
Returns number of triangles connected to this vertex

Args:
    vertex_id (VertexID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_vertex_connected_polygons"></a>

#### get_num_vertex_connected_polygons

```python
def get_num_vertex_connected_polygons(vertex_id: VertexID) -> int
```

x.get_num_vertex_connected_polygons(vertex_id) -> int32
Returns the number of polygons connected to this vertex

Args:
    vertex_id (VertexID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_vertex_connected_edges"></a>

#### get_num_vertex_connected_edges

```python
def get_num_vertex_connected_edges(vertex_id: VertexID) -> int
```

x.get_num_vertex_connected_edges(vertex_id) -> int32
Returns number of edges connected to this vertex

Args:
    vertex_id (VertexID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_polygon_vertices"></a>

#### get_num_polygon_vertices

```python
def get_num_polygon_vertices(polygon_id: PolygonID) -> int
```

x.get_num_polygon_vertices(polygon_id) -> int32
Returns the number of vertices this polygon has

Args:
    polygon_id (PolygonID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_polygon_triangles"></a>

#### get_num_polygon_triangles

```python
def get_num_polygon_triangles(polygon_id: PolygonID) -> int
```

x.get_num_polygon_triangles(polygon_id) -> int32
Return the number of triangles which comprise this polygon

Args:
    polygon_id (PolygonID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_polygon_internal_edges"></a>

#### get_num_polygon_internal_edges

```python
def get_num_polygon_internal_edges(polygon_id: PolygonID) -> int
```

x.get_num_polygon_internal_edges(polygon_id) -> int32
Return the number of internal edges in this polygon

Args:
    polygon_id (PolygonID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_polygon_group_polygons"></a>

#### get_num_polygon_group_polygons

```python
def get_num_polygon_group_polygons(polygon_group_id: PolygonGroupID) -> int
```

x.get_num_polygon_group_polygons(polygon_group_id) -> int32
Returns the number of polygons in this polygon group

Args:
    polygon_group_id (PolygonGroupID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_edge_connected_triangles"></a>

#### get_num_edge_connected_triangles

```python
def get_num_edge_connected_triangles(edge_id: EdgeID) -> int
```

x.get_num_edge_connected_triangles(edge_id) -> int32
Returns the number of triangles connected to this edge

Args:
    edge_id (EdgeID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_num_edge_connected_polygons"></a>

#### get_num_edge_connected_polygons

```python
def get_num_edge_connected_polygons(edge_id: EdgeID) -> int
```

x.get_num_edge_connected_polygons(edge_id) -> int32
Returns the number of polygons connected to this edge

Args:
    edge_id (EdgeID): 

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_edge_vertices"></a>

#### get_edge_vertices

```python
def get_edge_vertices(edge_id: EdgeID) -> Array[VertexID]
```

x.get_edge_vertices(edge_id) -> Array[VertexID]
Returns a pair of vertex IDs defining the edge

Args:
    edge_id (EdgeID): 

Returns:
    Array[VertexID]: 

    out_vertex_i_ds (Array[VertexID]):

<a id="unreal.MeshDescriptionBase.get_edge_vertex"></a>

#### get_edge_vertex

```python
def get_edge_vertex(edge_id: EdgeID, vertex_number: int) -> VertexID
```

x.get_edge_vertex(edge_id, vertex_number) -> VertexID
Returns the vertex ID corresponding to one of the edge endpoints

Args:
    edge_id (EdgeID): 
    vertex_number (int32): 

Returns:
    VertexID:

<a id="unreal.MeshDescriptionBase.get_edge_count"></a>

#### get_edge_count

```python
def get_edge_count() -> int
```

x.get_edge_count() -> int32
Returns the number of edges

Returns:
    int32:

<a id="unreal.MeshDescriptionBase.get_edge_connected_triangles"></a>

#### get_edge_connected_triangles

```python
def get_edge_connected_triangles(edge_id: EdgeID) -> Array[TriangleID]
```

x.get_edge_connected_triangles(edge_id) -> Array[TriangleID]
Returns reference to an array of triangle IDs connected to this edge

Args:
    edge_id (EdgeID): 

Returns:
    Array[TriangleID]: 

    out_connected_triangle_i_ds (Array[TriangleID]):

<a id="unreal.MeshDescriptionBase.get_edge_connected_polygons"></a>

#### get_edge_connected_polygons

```python
def get_edge_connected_polygons(edge_id: EdgeID) -> Array[PolygonID]
```

x.get_edge_connected_polygons(edge_id) -> Array[PolygonID]
Returns the polygons connected to this edge

Args:
    edge_id (EdgeID): 

Returns:
    Array[PolygonID]: 

    out_connected_polygon_i_ds (Array[PolygonID]):

<a id="unreal.MeshDescriptionBase.empty"></a>

#### empty

```python
def empty() -> None
```

x.empty() -> None
Empty the mesh description

<a id="unreal.MeshDescriptionBase.delete_vertex_instance"></a>

#### delete_vertex_instance

```python
def delete_vertex_instance(
        vertex_instance_id: VertexInstanceID) -> Array[VertexID]
```

x.delete_vertex_instance(vertex_instance_id) -> Array[VertexID]
Deletes a vertex instance from a mesh

Args:
    vertex_instance_id (VertexInstanceID): 

Returns:
    Array[VertexID]: 

    orphaned_vertices (Array[VertexID]):

<a id="unreal.MeshDescriptionBase.delete_vertex"></a>

#### delete_vertex

```python
def delete_vertex(vertex_id: VertexID) -> None
```

x.delete_vertex(vertex_id) -> None
Deletes a vertex from the mesh

Args:
    vertex_id (VertexID):

<a id="unreal.MeshDescriptionBase.delete_triangle"></a>

#### delete_triangle

```python
def delete_triangle(
    triangle_id: TriangleID
) -> Tuple[Array[EdgeID], Array[VertexInstanceID], Array[PolygonGroupID]]
```

x.delete_triangle(triangle_id) -> (orphaned_edges=Array[EdgeID], orphaned_vertex_instances=Array[VertexInstanceID], orphaned_polygon_groups_ptr=Array[PolygonGroupID])
Deletes a triangle from the mesh

Args:
    triangle_id (TriangleID): 

Returns:
    tuple: 

    orphaned_edges (Array[EdgeID]): 

    orphaned_vertex_instances (Array[VertexInstanceID]): 

    orphaned_polygon_groups_ptr (Array[PolygonGroupID]):

<a id="unreal.MeshDescriptionBase.delete_polygon_group"></a>

#### delete_polygon_group

```python
def delete_polygon_group(polygon_group_id: PolygonGroupID) -> None
```

x.delete_polygon_group(polygon_group_id) -> None
Deletes a polygon group from the mesh

Args:
    polygon_group_id (PolygonGroupID):

<a id="unreal.MeshDescriptionBase.delete_polygon"></a>

#### delete_polygon

```python
def delete_polygon(
    polygon_id: PolygonID
) -> Tuple[Array[EdgeID], Array[VertexInstanceID], Array[PolygonGroupID]]
```

x.delete_polygon(polygon_id) -> (orphaned_edges=Array[EdgeID], orphaned_vertex_instances=Array[VertexInstanceID], orphaned_polygon_groups=Array[PolygonGroupID])
Deletes a polygon from the mesh

Args:
    polygon_id (PolygonID): 

Returns:
    tuple: 

    orphaned_edges (Array[EdgeID]): 

    orphaned_vertex_instances (Array[VertexInstanceID]): 

    orphaned_polygon_groups (Array[PolygonGroupID]):

<a id="unreal.MeshDescriptionBase.delete_edge"></a>

#### delete_edge

```python
def delete_edge(edge_id: EdgeID) -> Array[VertexID]
```

x.delete_edge(edge_id) -> Array[VertexID]
Deletes an edge from a mesh

Args:
    edge_id (EdgeID): 

Returns:
    Array[VertexID]: 

    orphaned_vertices (Array[VertexID]):

<a id="unreal.MeshDescriptionBase.create_vertex_with_id"></a>

#### create_vertex_with_id

```python
def create_vertex_with_id(vertex_id: VertexID) -> None
```

x.create_vertex_with_id(vertex_id) -> None
Adds a new vertex to the mesh with the given ID

Args:
    vertex_id (VertexID):

<a id="unreal.MeshDescriptionBase.create_vertex_instance_with_id"></a>

#### create_vertex_instance_with_id

```python
def create_vertex_instance_with_id(vertex_instance_id: VertexInstanceID,
                                   vertex_id: VertexID) -> None
```

x.create_vertex_instance_with_id(vertex_instance_id, vertex_id) -> None
Adds a new vertex instance to the mesh with the given ID

Args:
    vertex_instance_id (VertexInstanceID): 
    vertex_id (VertexID):

<a id="unreal.MeshDescriptionBase.create_vertex_instance"></a>

#### create_vertex_instance

```python
def create_vertex_instance(vertex_id: VertexID) -> VertexInstanceID
```

x.create_vertex_instance(vertex_id) -> VertexInstanceID
Adds a new vertex instance to the mesh and returns its ID

Args:
    vertex_id (VertexID): 

Returns:
    VertexInstanceID:

<a id="unreal.MeshDescriptionBase.create_vertex"></a>

#### create_vertex

```python
def create_vertex() -> VertexID
```

x.create_vertex() -> VertexID
Adds a new vertex to the mesh and returns its ID

Returns:
    VertexID:

<a id="unreal.MeshDescriptionBase.create_triangle_with_id"></a>

#### create_triangle_with_id

```python
def create_triangle_with_id(
        triangle_id: TriangleID, polygon_group_id: PolygonGroupID,
        vertex_instance_i_ds: Array[VertexInstanceID]) -> Array[EdgeID]
```

x.create_triangle_with_id(triangle_id, polygon_group_id, vertex_instance_i_ds) -> Array[EdgeID]
Adds a new triangle to the mesh with the given ID. This will also make an encapsulating polygon, and any missing edges.

Args:
    triangle_id (TriangleID): 
    polygon_group_id (PolygonGroupID): 
    vertex_instance_i_ds (Array[VertexInstanceID]): 

Returns:
    Array[EdgeID]: 

    new_edge_i_ds (Array[EdgeID]):

<a id="unreal.MeshDescriptionBase.create_triangle"></a>

#### create_triangle

```python
def create_triangle(
    polygon_group_id: PolygonGroupID,
    vertex_instance_i_ds: Array[VertexInstanceID]
) -> Tuple[TriangleID, Array[EdgeID]]
```

x.create_triangle(polygon_group_id, vertex_instance_i_ds) -> (TriangleID, new_edge_i_ds=Array[EdgeID])
Adds a new triangle to the mesh and returns its ID. This will also make an encapsulating polygon, and any missing edges.

Args:
    polygon_group_id (PolygonGroupID): 
    vertex_instance_i_ds (Array[VertexInstanceID]): 

Returns:
    Array[EdgeID]: 

    new_edge_i_ds (Array[EdgeID]):

<a id="unreal.MeshDescriptionBase.create_polygon_with_id"></a>

#### create_polygon_with_id

```python
def create_polygon_with_id(
    polygon_id: PolygonID, polygon_group_id: PolygonGroupID
) -> Tuple[Array[VertexInstanceID], Array[EdgeID]]
```

x.create_polygon_with_id(polygon_id, polygon_group_id) -> (vertex_instance_i_ds=Array[VertexInstanceID], new_edge_i_ds=Array[EdgeID])
Adds a new polygon to the mesh with the given ID. This will also make any missing edges, and all constituent triangles.

Args:
    polygon_id (PolygonID): 
    polygon_group_id (PolygonGroupID): 

Returns:
    tuple: 

    vertex_instance_i_ds (Array[VertexInstanceID]): 

    new_edge_i_ds (Array[EdgeID]):

<a id="unreal.MeshDescriptionBase.create_polygon_group_with_id"></a>

#### create_polygon_group_with_id

```python
def create_polygon_group_with_id(polygon_group_id: PolygonGroupID) -> None
```

x.create_polygon_group_with_id(polygon_group_id) -> None
Adds a new polygon group to the mesh with the given ID

Args:
    polygon_group_id (PolygonGroupID):

<a id="unreal.MeshDescriptionBase.create_polygon_group"></a>

#### create_polygon_group

```python
def create_polygon_group() -> PolygonGroupID
```

x.create_polygon_group() -> PolygonGroupID
Adds a new polygon group to the mesh and returns its ID

Returns:
    PolygonGroupID:

<a id="unreal.MeshDescriptionBase.create_polygon"></a>

#### create_polygon

```python
def create_polygon(
    polygon_group_id: PolygonGroupID
) -> Tuple[PolygonID, Array[VertexInstanceID], Array[EdgeID]]
```

x.create_polygon(polygon_group_id) -> (PolygonID, vertex_instance_i_ds=Array[VertexInstanceID], new_edge_i_ds=Array[EdgeID])
Adds a new polygon to the mesh and returns its ID. This will also make any missing edges, and all constituent triangles.

Args:
    polygon_group_id (PolygonGroupID): 

Returns:
    tuple: 

    vertex_instance_i_ds (Array[VertexInstanceID]): 

    new_edge_i_ds (Array[EdgeID]):

<a id="unreal.MeshDescriptionBase.create_edge_with_id"></a>

#### create_edge_with_id

```python
def create_edge_with_id(edge_id: EdgeID, vertex_id0: VertexID,
                        vertex_id1: VertexID) -> None
```

x.create_edge_with_id(edge_id, vertex_id0, vertex_id1) -> None
Adds a new edge to the mesh with the given ID

Args:
    edge_id (EdgeID): 
    vertex_id0 (VertexID): 
    vertex_id1 (VertexID):

<a id="unreal.MeshDescriptionBase.create_edge"></a>

#### create_edge

```python
def create_edge(vertex_id0: VertexID, vertex_id1: VertexID) -> EdgeID
```

x.create_edge(vertex_id0, vertex_id1) -> EdgeID
Adds a new edge to the mesh and returns its ID

Args:
    vertex_id0 (VertexID): 
    vertex_id1 (VertexID): 

Returns:
    EdgeID:

<a id="unreal.MeshDescriptionBase.compute_polygon_triangulation"></a>

#### compute_polygon_triangulation

```python
def compute_polygon_triangulation(polygon_id: PolygonID) -> None
```

x.compute_polygon_triangulation(polygon_id) -> None
Generates triangles and internal edges for the given polygon

Args:
    polygon_id (PolygonID):

<a id="unreal.StaticMeshDescription"></a>