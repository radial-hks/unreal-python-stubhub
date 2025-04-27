## GeometryScript_MeshRepair Objects

```python
class GeometryScript_MeshRepair(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Repair Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRepairFunctions.h

<a id="unreal.GeometryScript_MeshRepair.weld_mesh_edges"></a>

#### weld_mesh_edges

```python
@classmethod
def weld_mesh_edges(cls,
                    target_mesh: DynamicMesh,
                    weld_options: GeometryScriptWeldEdgesOptions,
                    debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.weld_mesh_edges(target_mesh, weld_options, debug=None) -> DynamicMesh
Welds any open boundary edges of the mesh together if possible in order to remove "cracks."

Args:
    target_mesh (DynamicMesh): 
    weld_options (GeometryScriptWeldEdgesOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair.split_mesh_bowties"></a>

#### split_mesh_bowties

```python
@classmethod
def split_mesh_bowties(cls,
                       target_mesh: DynamicMesh,
                       mesh_bowties: bool = True,
                       attribute_bowties: bool = True,
                       debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.split_mesh_bowties(target_mesh, mesh_bowties=True, attribute_bowties=True, debug=None) -> DynamicMesh
Splits Bowties in the mesh and/or the attributes.  A Bowtie is formed when a single vertex is connected to more than two boundary edges,
and splitting duplicates the shared vertex so each triangle will have a unique copy.

Args:
    target_mesh (DynamicMesh): 
    mesh_bowties (bool): 
    attribute_bowties (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair.snap_mesh_open_boundaries"></a>

#### snap_mesh_open_boundaries

```python
@classmethod
def snap_mesh_open_boundaries(
        cls,
        target_mesh: DynamicMesh,
        snap_options: GeometryScriptSnapBoundariesOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.snap_mesh_open_boundaries(target_mesh, snap_options, debug=None) -> DynamicMesh
Snap vertices on open edges to the closest compatible open boundary, if found within the tolerance distance
Unlike ResolveMeshTJunctions, does not introduce new vertices to the mesh

Args:
    target_mesh (DynamicMesh): 
    snap_options (GeometryScriptSnapBoundariesOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair.resolve_mesh_t_junctions"></a>

#### resolve_mesh_t_junctions

```python
@classmethod
def resolve_mesh_t_junctions(
        cls,
        target_mesh: DynamicMesh,
        resolve_options: GeometryScriptResolveTJunctionOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.resolve_mesh_t_junctions(target_mesh, resolve_options, debug=None) -> DynamicMesh
Attempts to resolve T-Junctions in the mesh by addition of vertices and welding.

Args:
    target_mesh (DynamicMesh): 
    resolve_options (GeometryScriptResolveTJunctionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair.repair_mesh_degenerate_geometry"></a>

#### repair_mesh_degenerate_geometry

```python
@classmethod
def repair_mesh_degenerate_geometry(
        cls,
        target_mesh: DynamicMesh,
        options: GeometryScriptDegenerateTriangleOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.repair_mesh_degenerate_geometry(target_mesh, options, debug=None) -> DynamicMesh
Removes triangles that have area or edge length below specified amounts depending on the Options requested.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptDegenerateTriangleOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair.remove_unused_vertices"></a>

#### remove_unused_vertices

```python
@classmethod
def remove_unused_vertices(cls,
                           target_mesh: DynamicMesh,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.remove_unused_vertices(target_mesh, debug=None) -> DynamicMesh
Remove vertices that are not used by any triangles. Note: Does not update the IDs of any remaining vertices; use CompactMesh to do so.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair.remove_small_components"></a>

#### remove_small_components

```python
@classmethod
def remove_small_components(cls,
                            target_mesh: DynamicMesh,
                            options: GeometryScriptRemoveSmallComponentOptions,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.remove_small_components(target_mesh, options, debug=None) -> DynamicMesh
* Removes connected components of the mesh that have a volume, area, or triangle count below a threshold as specified by the Options.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptRemoveSmallComponentOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair.remove_hidden_triangles"></a>

#### remove_hidden_triangles

```python
@classmethod
def remove_hidden_triangles(
        cls,
        target_mesh: DynamicMesh,
        options: GeometryScriptRemoveHiddenTrianglesOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.remove_hidden_triangles(target_mesh, options, debug=None) -> DynamicMesh
Removes any triangles in the mesh that are not visible from the exterior view, under various definitions of "visible" and "outside"
as specified by the Options.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptRemoveHiddenTrianglesOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair.fill_all_mesh_holes"></a>

#### fill_all_mesh_holes

```python
@classmethod
def fill_all_mesh_holes(
        cls,
        target_mesh: DynamicMesh,
        fill_options: GeometryScriptFillHolesOptions,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int, int]
```

X.fill_all_mesh_holes(target_mesh, fill_options, debug=None) -> (DynamicMesh, num_filled_holes=int32, num_failed_hole_fills=int32)
Tries to fill all open boundary loops (such as holes in the geometry surface) of a mesh.

Args:
    target_mesh (DynamicMesh): 
    fill_options (GeometryScriptFillHolesOptions): specifies the method used to fill the holes.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    num_filled_holes (int32): reports the number of holes filled by the function.

    num_failed_hole_fills (int32):

<a id="unreal.GeometryScript_MeshRepair.compact_mesh"></a>

#### compact_mesh

```python
@classmethod
def compact_mesh(cls,
                 target_mesh: DynamicMesh,
                 debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.compact_mesh(target_mesh, debug=None) -> DynamicMesh
Compacts the mesh's vertices and triangles to remove any "holes" in the Vertex ID or Triangle ID lists.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshSampling"></a>