## GeometryScript_MeshSimplification Objects

```python
class GeometryScript_MeshSimplification(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Simplify Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSimplifyFunctions.h

<a id="unreal.GeometryScript_MeshSimplification.apply_simplify_to_vertex_count"></a>

#### apply_simplify_to_vertex_count

```python
@classmethod
def apply_simplify_to_vertex_count(
        cls,
        target_mesh: DynamicMesh,
        vertex_count: int,
        options: GeometryScriptSimplifyMeshOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_simplify_to_vertex_count(target_mesh, vertex_count, options, debug=None) -> DynamicMesh
Simplifies the mesh until a target vertex count is reached. Behavior can be additionally controlled with the Options.

Args:
    target_mesh (DynamicMesh): 
    vertex_count (int32): 
    options (GeometryScriptSimplifyMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshSimplification.apply_simplify_to_triangle_count"></a>

#### apply_simplify_to_triangle_count

```python
@classmethod
def apply_simplify_to_triangle_count(
        cls,
        target_mesh: DynamicMesh,
        triangle_count: int,
        options: GeometryScriptSimplifyMeshOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_simplify_to_triangle_count(target_mesh, triangle_count, options, debug=None) -> DynamicMesh
Simplifies the mesh until a target triangle count is reached. Behavior can be additionally controlled with the Options.

Args:
    target_mesh (DynamicMesh): 
    triangle_count (int32): 
    options (GeometryScriptSimplifyMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshSimplification.apply_simplify_to_tolerance"></a>

#### apply_simplify_to_tolerance

```python
@classmethod
def apply_simplify_to_tolerance(
        cls,
        target_mesh: DynamicMesh,
        tolerance: float,
        options: GeometryScriptSimplifyMeshOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_simplify_to_tolerance(target_mesh, tolerance, options, debug=None) -> DynamicMesh
Simplifies the mesh to a target geometric tolerance. Stops when any further simplification would result in a deviation from the input mesh larger than the tolerance.
Behavior can be additionally controlled with the Options.

Args:
    target_mesh (DynamicMesh): 
    tolerance (float): 
    options (GeometryScriptSimplifyMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshSimplification.apply_simplify_to_polygroup_topology"></a>

#### apply_simplify_to_polygroup_topology

```python
@classmethod
def apply_simplify_to_polygroup_topology(
        cls,
        target_mesh: DynamicMesh,
        options: GeometryScriptPolygroupSimplifyOptions,
        group_layer: GeometryScriptGroupLayer,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_simplify_to_polygroup_topology(target_mesh, options, group_layer, debug=None) -> DynamicMesh
Simplifies the mesh down to the PolyGroup Topology. For example, the high-level faces of the mesh PolyGroups.
Another example would be on a default Box-Sphere where simplifying to PolyGroup topology produces a box.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptPolygroupSimplifyOptions): 
    group_layer (GeometryScriptGroupLayer): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshSimplification.apply_simplify_to_planar"></a>

#### apply_simplify_to_planar

```python
@classmethod
def apply_simplify_to_planar(cls,
                             target_mesh: DynamicMesh,
                             options: GeometryScriptPlanarSimplifyOptions,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_simplify_to_planar(target_mesh, options, debug=None) -> DynamicMesh
Simplifies planar areas of the mesh that have more triangles than necessary. Note that it does not change the 3D shape of the mesh.
Planar regions are identified by comparison of face normals using a Angle Threshold in the Options.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptPlanarSimplifyOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshSpatial"></a>