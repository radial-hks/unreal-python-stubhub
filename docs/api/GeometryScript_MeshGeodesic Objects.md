## GeometryScript_MeshGeodesic Objects

```python
class GeometryScript_MeshGeodesic(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Geodesic Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshGeodesicFunctions.h

<a id="unreal.GeometryScript_MeshGeodesic.get_shortest_vertex_path"></a>

#### get_shortest_vertex_path

```python
@classmethod
def get_shortest_vertex_path(
    cls,
    target_mesh: DynamicMesh,
    start_vertex_id: int,
    end_vertex_id: int,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

X.get_shortest_vertex_path(target_mesh, start_vertex_id, end_vertex_id, debug=None) -> (DynamicMesh, vertex_id_list=GeometryScriptIndexList, found_errors=bool)
Computes a vertex list that represents the shortest path constrained to travel along mesh triangle edges between the prescribed start and end vertex.
This can fail if the Start and End points are within separate connected components of the mesh.

Args:
    target_mesh (DynamicMesh): defines the surface where the path is computed.
    start_vertex_id (int32): indicates ID of mesh vertex that defines the starting point of the path.
    end_vertex_id (int32): indicates ID of the mesh vertex that defined the end point of the path.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    vertex_id_list (GeometryScriptIndexList): 

    found_errors (bool): will be false on success.

<a id="unreal.GeometryScript_MeshGeodesic.get_shortest_surface_path"></a>

#### get_shortest_surface_path

```python
@classmethod
def get_shortest_surface_path(
    cls,
    target_mesh: DynamicMesh,
    start_triangle_id: int,
    start_bary_coords: Vector,
    end_triangle_id: int,
    end_bary_coords: Vector,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptPolyPath, bool]
```

X.get_shortest_surface_path(target_mesh, start_triangle_id, start_bary_coords, end_triangle_id, end_bary_coords, debug=None) -> (DynamicMesh, shortest_path=GeometryScriptPolyPath, found_errors=bool)
Computes a PolyPath that represents the shortest mesh surface path between two prescribed points on the provided mesh.
This can fail if the Start and End points are within separate connected components of the mesh.

Args:
    target_mesh (DynamicMesh): defines the surface where the path is computed.
    start_triangle_id (int32): the ID of mesh Triangle that contains the start point of the path.
    start_bary_coords (Vector): indicates the location of start point within the start triangle, in terms of barycentric coordinates.
    end_triangle_id (int32): the ID of mesh Triangle that contains the end point of the path.
    end_bary_coords (Vector): indicates the location of the end point within the end triangle, in terms of barycentric coordinates.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    shortest_path (GeometryScriptPolyPath): 

    found_errors (bool):

<a id="unreal.GeometryScript_MeshGeodesic.create_surface_path"></a>

#### create_surface_path

```python
@classmethod
def create_surface_path(
    cls,
    target_mesh: DynamicMesh,
    direction: Vector,
    start_triangle_id: int,
    start_bary_coords: Vector,
    max_path_length: float,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptPolyPath, bool]
```

X.create_surface_path(target_mesh, direction, start_triangle_id, start_bary_coords, max_path_length, debug=None) -> (DynamicMesh, surface_path=GeometryScriptPolyPath, found_errors=bool)
Computes a PolyPath that represents a "straight" surface path starting at the prescribed point on the mesh, and continuing
in the indicated direction until reaching the requested path length or encountering a mesh boundary, whichever comes first.

Args:
    target_mesh (DynamicMesh): defines the surface where the path is computed.
    direction (Vector): is a three-dimensional vector that is projected onto the mesh surface to determine the path direction.
    start_triangle_id (int32): the ID of mesh Triangle that contains the start point of the path.
    start_bary_coords (Vector): indicates the location of start point within the start triangle, in terms of barycentric coordinates.
    max_path_length (float): sets the maximal length of the path, but the actual path may be shorter as it automatically terminates when encountering a mesh boundary edge.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    surface_path (GeometryScriptPolyPath): holds on return a PolyPath that forms a "straight" path along the mesh surface from the start position.

    found_errors (bool):

<a id="unreal.GeometryScript_Materials"></a>