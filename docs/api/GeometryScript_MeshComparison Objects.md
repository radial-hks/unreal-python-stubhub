## GeometryScript_MeshComparison Objects

```python
class GeometryScript_MeshComparison(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Comparison Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshComparisonFunctions.h

<a id="unreal.GeometryScript_MeshComparison.measure_distances_between_meshes"></a>

#### measure_distances_between_meshes

```python
@classmethod
def measure_distances_between_meshes(
    cls,
    target_mesh: DynamicMesh,
    other_mesh: DynamicMesh,
    options: GeometryScriptMeasureMeshDistanceOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, float, float, float, float]
```

X.measure_distances_between_meshes(target_mesh, other_mesh, options, debug=None) -> (DynamicMesh, max_distance=double, min_distance=double, average_distance=double, root_mean_sqr_deviation=double)
Measures the min/max and average closest-point distances between two meshes.

Args:
    target_mesh (DynamicMesh): 
    other_mesh (DynamicMesh): 
    options (GeometryScriptMeasureMeshDistanceOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    max_distance (double): 

    min_distance (double): 

    average_distance (double): 

    root_mean_sqr_deviation (double):

<a id="unreal.GeometryScript_MeshComparison.is_same_mesh_as"></a>

#### is_same_mesh_as

```python
@classmethod
def is_same_mesh_as(
    cls,
    target_mesh: DynamicMesh,
    other_mesh: DynamicMesh,
    options: GeometryScriptIsSameMeshOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, bool, GeometryScriptMeshDifferenceInfo]
```

X.is_same_mesh_as(target_mesh, other_mesh, options, debug=None) -> (DynamicMesh, is_same_mesh=bool, difference_info=GeometryScriptMeshDifferenceInfo)
Returns true if the two input meshes are equivalent under the comparisons defined by the input options. If false, DifferenceInfo provides info on the first difference found.

Args:
    target_mesh (DynamicMesh): 
    other_mesh (DynamicMesh): 
    options (GeometryScriptIsSameMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_same_mesh (bool): 

    difference_info (GeometryScriptMeshDifferenceInfo): If the meshes are different, provides info on the first difference found.

<a id="unreal.GeometryScript_MeshComparison.is_intersecting_mesh"></a>

#### is_intersecting_mesh

```python
@classmethod
def is_intersecting_mesh(
        cls,
        target_mesh: DynamicMesh,
        target_transform: Transform,
        other_mesh: DynamicMesh,
        other_transform: Transform,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

X.is_intersecting_mesh(target_mesh, target_transform, other_mesh, other_transform, debug=None) -> (DynamicMesh, is_intersecting=bool)
Returns true if the two input meshes (with optional transforms) are geometrically intersecting.

Args:
    target_mesh (DynamicMesh): 
    target_transform (Transform): 
    other_mesh (DynamicMesh): 
    other_transform (Transform): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    is_intersecting (bool):

<a id="unreal.GeometryScript_MeshDecomposition"></a>