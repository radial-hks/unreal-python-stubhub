## GeometryScript_Containment Objects

```python
class GeometryScript_Containment(BlueprintFunctionLibrary)
```

Geometry Script Library Containment Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: ContainmentFunctions.h

<a id="unreal.GeometryScript_Containment.compute_mesh_swept_hull"></a>

#### compute_mesh_swept_hull

```python
@classmethod
def compute_mesh_swept_hull(
    cls,
    target_mesh: DynamicMesh,
    copy_to_mesh: DynamicMesh,
    projection_frame: Transform,
    options: GeometryScriptSweptHullOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

X.compute_mesh_swept_hull(target_mesh, copy_to_mesh, projection_frame, options, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh)
Compute the Swept Hull of a given Target Mesh for a given 3D Plane defined by ProjectionFrame, and put the result in Hull Mesh
The Swept Hull is a linear sweep of the 2D convex hull of the mesh vertices projected onto the plane (the sweep precisely contains the mesh extents along the plane normal)

Args:
    target_mesh (DynamicMesh): 
    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the swept hull geometry.
    projection_frame (Transform): 
    options (GeometryScriptSweptHullOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the swept hull geometry.

    copy_to_mesh_out (DynamicMesh): The resulting swept hull.

<a id="unreal.GeometryScript_Containment.compute_mesh_convex_hull"></a>

#### compute_mesh_convex_hull

```python
@classmethod
def compute_mesh_convex_hull(
    cls,
    target_mesh: DynamicMesh,
    copy_to_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    options: GeometryScriptConvexHullOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

X.compute_mesh_convex_hull(target_mesh, copy_to_mesh, selection, options, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh)
Compute the Convex Hull of a given Target Mesh, or part of the mesh if an optional Selection is provided, and put the result in Hull Mesh

Args:
    target_mesh (DynamicMesh): 
    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the convex hull geometry.
    selection (GeometryScriptMeshSelection): Selection of mesh faces/vertices to contain in the convex hull. If not provided, entire mesh is used.
    options (GeometryScriptConvexHullOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the convex hull geometry.

    copy_to_mesh_out (DynamicMesh): The resulting convex hull.

<a id="unreal.GeometryScript_Containment.compute_mesh_convex_decomposition"></a>

#### compute_mesh_convex_decomposition

```python
@classmethod
def compute_mesh_convex_decomposition(
    cls,
    target_mesh: DynamicMesh,
    copy_to_mesh: DynamicMesh,
    options: GeometryScriptConvexDecompositionOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

X.compute_mesh_convex_decomposition(target_mesh, copy_to_mesh, options, debug=None) -> (DynamicMesh, copy_to_mesh=DynamicMesh, copy_to_mesh_out=DynamicMesh)
Compute a Convex Hull Decomposition of the given TargetMesh. Assuming more than one hull is requested,
multiple hulls will be returned that attempt to approximate the mesh. If simplification settings are enabled,
there is no guarantee that the entire mesh is contained in the hulls.
warning: this function can be quite expensive, and the results are expected to change in the future as the Convex Decomposition algorithm is improved

Args:
    target_mesh (DynamicMesh): 
    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the convex hulls as a single, combined mesh. Note: SplitMeshByComponents can separate this result into its convex parts.
    options (GeometryScriptConvexDecompositionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    copy_to_mesh (DynamicMesh): The Dynamic Mesh to store the convex hulls as a single, combined mesh. Note: SplitMeshByComponents can separate this result into its convex parts.

    copy_to_mesh_out (DynamicMesh): A combined mesh of the convex hulls. Note: SplitMeshByComponents can separate this result into its convex parts.

<a id="unreal.GeometryScript_List"></a>