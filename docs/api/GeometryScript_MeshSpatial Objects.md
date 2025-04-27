## GeometryScript_MeshSpatial Objects

```python
class GeometryScript_MeshSpatial(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Spatial

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSpatialFunctions.h

<a id="unreal.GeometryScript_MeshSpatial.select_mesh_elements_in_box_with_bvh"></a>

#### select_mesh_elements_in_box_with_bvh

```python
@classmethod
def select_mesh_elements_in_box_with_bvh(
    cls,
    target_mesh: DynamicMesh,
    query_bvh: GeometryScriptDynamicMeshBVH,
    query_box: Box,
    options: GeometryScriptSpatialQueryOptions,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.VERTICES,
    min_num_triangle_points: int = 3,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_elements_in_box_with_bvh(target_mesh, query_bvh, query_box, options, selection_type=GeometryScriptMeshSelectionType.VERTICES, min_num_triangle_points=3, debug=None) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create Mesh Selection of mesh elements in TargetMesh contained by QueryBox, using QueryBVH to accellerate the computation.
Triangles and Edges are selected if Min Element Vertices (clamped to a 1-3 or 1-2 range, for triangles or edges respectively) or more are inside the box.
PolyGroups are selected if any of their triangles are inside the box

Note that this method cannot select mesh elements that cut through the query box without having any vertices in the query box.

Args:
    target_mesh (DynamicMesh): 
    query_bvh (GeometryScriptDynamicMeshBVH): is an acceleration structure previously built with TargetMesh.
    query_box (Box): 
    options (GeometryScriptSpatialQueryOptions): control the fast winding number threshold
    selection_type (GeometryScriptMeshSelectionType): 
    min_num_triangle_points (int32): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSpatial.reset_bvh"></a>

#### reset_bvh

```python
@classmethod
def reset_bvh(
        cls, reset_bvh: GeometryScriptDynamicMeshBVH
) -> GeometryScriptDynamicMeshBVH
```

X.reset_bvh(reset_bvh) -> GeometryScriptDynamicMeshBVH
Reset the Bounding Volume Hierarchy (BVH) by clearing all the internal data.

Args:
    reset_bvh (GeometryScriptDynamicMeshBVH): 

Returns:
    GeometryScriptDynamicMeshBVH: 

    reset_bvh (GeometryScriptDynamicMeshBVH):

<a id="unreal.GeometryScript_MeshSpatial.rebuild_bvh_for_mesh"></a>

#### rebuild_bvh_for_mesh

```python
@classmethod
def rebuild_bvh_for_mesh(
    cls,
    target_mesh: DynamicMesh,
    update_bvh: GeometryScriptDynamicMeshBVH,
    only_if_invalid: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptDynamicMeshBVH]
```

X.rebuild_bvh_for_mesh(target_mesh, update_bvh, only_if_invalid=True, debug=None) -> (DynamicMesh, update_bvh=GeometryScriptDynamicMeshBVH)
Rebuilds the Bounding Volume Hierarchy (BVH) for the mesh in-place, which can reduce memory allocations, compared to building a new BVH.

Args:
    target_mesh (DynamicMesh): 
    update_bvh (GeometryScriptDynamicMeshBVH): 
    only_if_invalid (bool): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptDynamicMeshBVH: 

    update_bvh (GeometryScriptDynamicMeshBVH):

<a id="unreal.GeometryScript_MeshSpatial.is_point_inside_mesh"></a>

#### is_point_inside_mesh

```python
@classmethod
def is_point_inside_mesh(
    cls,
    target_mesh: DynamicMesh,
    query_bvh: GeometryScriptDynamicMeshBVH,
    query_point: Vector,
    options: GeometryScriptSpatialQueryOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, bool, GeometryScriptContainmentOutcomePins]
```

X.is_point_inside_mesh(target_mesh, query_bvh, query_point, options, debug=None) -> (DynamicMesh, is_inside=bool, outcome=GeometryScriptContainmentOutcomePins)
Tests if a point is inside the mesh using the Fast Winding Number query and data stored in the BVH.

Args:
    target_mesh (DynamicMesh): 
    query_bvh (GeometryScriptDynamicMeshBVH): is an acceleration structure previously built with this mesh.
    query_point (Vector): the point in the mesh's 3D local space.
    options (GeometryScriptSpatialQueryOptions): control the fast winding number threshold
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_inside (bool): 

    outcome (GeometryScriptContainmentOutcomePins):

<a id="unreal.GeometryScript_MeshSpatial.is_bvh_valid_for_mesh"></a>

#### is_bvh_valid_for_mesh

```python
@classmethod
def is_bvh_valid_for_mesh(
        cls,
        target_mesh: DynamicMesh,
        test_bvh: GeometryScriptDynamicMeshBVH,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

X.is_bvh_valid_for_mesh(target_mesh, test_bvh, debug=None) -> (DynamicMesh, is_valid=bool)
Checks if the provided Bounding Volume Hierarchy (BVH) can still be used with the Mesh — it generally returns false if the mesh has been changed.

Args:
    target_mesh (DynamicMesh): 
    test_bvh (GeometryScriptDynamicMeshBVH): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.GeometryScript_MeshSpatial.find_nearest_ray_intersection_with_mesh"></a>

#### find_nearest_ray_intersection_with_mesh

```python
@classmethod
def find_nearest_ray_intersection_with_mesh(
    cls,
    target_mesh: DynamicMesh,
    query_bvh: GeometryScriptDynamicMeshBVH,
    ray_origin: Vector,
    ray_direction: Vector,
    options: GeometryScriptSpatialQueryOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptRayHitResult,
           GeometryScriptSearchOutcomePins]
```

X.find_nearest_ray_intersection_with_mesh(target_mesh, query_bvh, ray_origin, ray_direction, options, debug=None) -> (DynamicMesh, hit_result=GeometryScriptRayHitResult, outcome=GeometryScriptSearchOutcomePins)
Finds the nearest intersection of a 3D ray with the mesh by using the Query BVH.
Note, depending on the Ray Origin and Ray Direction, there is the possibility that the ray might not intersect with the Target Mesh.
Should the ray miss, the HitResult.bHit will be false and the Outcome  will be Not Found.

Args:
    target_mesh (DynamicMesh): 
    query_bvh (GeometryScriptDynamicMeshBVH): 
    ray_origin (Vector): 
    ray_direction (Vector): 
    options (GeometryScriptSpatialQueryOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    hit_result (GeometryScriptRayHitResult): 

    outcome (GeometryScriptSearchOutcomePins):

<a id="unreal.GeometryScript_MeshSpatial.find_nearest_point_on_mesh"></a>

#### find_nearest_point_on_mesh

```python
@classmethod
def find_nearest_point_on_mesh(
    cls,
    target_mesh: DynamicMesh,
    query_bvh: GeometryScriptDynamicMeshBVH,
    query_point: Vector,
    options: GeometryScriptSpatialQueryOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptTrianglePoint,
           GeometryScriptSearchOutcomePins]
```

X.find_nearest_point_on_mesh(target_mesh, query_bvh, query_point, options, debug=None) -> (DynamicMesh, nearest_result=GeometryScriptTrianglePoint, outcome=GeometryScriptSearchOutcomePins)
Finds the nearest point (Nearest Result) on the Target Mesh to a given 3D point (Query Point) by using the Query BVH.

Args:
    target_mesh (DynamicMesh): 
    query_bvh (GeometryScriptDynamicMeshBVH): a BVH associated with the Target Mesh
    query_point (Vector): a 3D location relative to the local space of the mesh
    options (GeometryScriptSpatialQueryOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    nearest_result (GeometryScriptTrianglePoint): on return, holds the nearest point on the mesh to the QueryPoint

    outcome (GeometryScriptSearchOutcomePins): will be either Found or Not Found depending on the success of the query. Note NearestResult.bValid will be false if the query failed.

<a id="unreal.GeometryScript_MeshSpatial.build_bvh_for_mesh"></a>

#### build_bvh_for_mesh

```python
@classmethod
def build_bvh_for_mesh(
    cls,
    target_mesh: DynamicMesh,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptDynamicMeshBVH]
```

X.build_bvh_for_mesh(target_mesh, debug=None) -> (DynamicMesh, output_bvh=GeometryScriptDynamicMeshBVH)
Builds a Bounding Volume Hierarchy (BVH) object for a mesh that can be used with multiple spatial queries.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptDynamicMeshBVH: 

    output_bvh (GeometryScriptDynamicMeshBVH):

<a id="unreal.GeometryScript_MeshSubdivide"></a>