## GeometryScript_MeshSelectionQueries Objects

```python
class GeometryScript_MeshSelectionQueries(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Selection Query Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSelectionQueryFunctions.h

<a id="unreal.GeometryScript_MeshSelectionQueries.get_mesh_selection_bounding_box"></a>

#### get_mesh_selection_bounding_box

```python
@classmethod
def get_mesh_selection_bounding_box(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Box, bool]
```

X.get_mesh_selection_bounding_box(target_mesh, selection, debug=None) -> (DynamicMesh, selection_bounds=Box, is_empty=bool)
Get the 3D Bounding Box of a Mesh Selection, ie bounding box of vertices contained in the Selection

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    selection_bounds (Box): 

    is_empty (bool): will return as true if the selection was empty (the box will be initialized to 0 in this case)

<a id="unreal.GeometryScript_MeshSelectionQueries.get_mesh_selection_boundary_loops"></a>

#### get_mesh_selection_boundary_loops

```python
@classmethod
def get_mesh_selection_boundary_loops(
    cls,
    target_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[GeometryScriptIndexList],
           Array[GeometryScriptPolyPath], int, bool]
```

X.get_mesh_selection_boundary_loops(target_mesh, selection, debug=None) -> (DynamicMesh, index_loops=Array[GeometryScriptIndexList], path_loops=Array[GeometryScriptPolyPath], num_loops=int32, found_errors=bool)
Compute the set of Vertex Loops bordering a Mesh Selection. Both the 3D polylines and lists of vertex indices are returned for each Loop.
Note that for a Vertex selection this will function return the border loops around the set of vertex triangle one-rings.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    index_loops (Array[GeometryScriptIndexList]): for each discovered Loop, the IndexList of mesh vertex indices around the loop is returned here

    path_loops (Array[GeometryScriptPolyPath]): for each discovered Loop, the PolyPath of mesh vertex positions around the loop is returned here. The ordering for each loop is the same as IndexLoops.

    num_loops (int32): number of loops found is returned here

    found_errors (bool): true is returned here if topological errors were found during loop computation. In this case the Loop set may be incomplete.

<a id="unreal.GeometryScript_MeshSimplification"></a>