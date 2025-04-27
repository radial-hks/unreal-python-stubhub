## GeometryScript_MeshModeling Objects

```python
class GeometryScript_MeshModeling(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Modeling Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_shell"></a>

#### apply_mesh_shell

```python
@classmethod
def apply_mesh_shell(cls,
                     target_mesh: DynamicMesh,
                     options: GeometryScriptMeshOffsetOptions,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_shell(target_mesh, options, debug=None) -> DynamicMesh
Create a thickened shell from TargetMesh by offsetting the vertex positions along averaged vertex normals, inwards or outwards.
Similar to ApplyMeshOffset but also includes the initial mesh (possibly flipped, if the offset is positive)

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshOffsetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_polygroup_bevel"></a>

#### apply_mesh_polygroup_bevel

```python
@classmethod
def apply_mesh_polygroup_bevel(
        cls,
        target_mesh: DynamicMesh,
        options: GeometryScriptMeshBevelOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_polygroup_bevel(target_mesh, options, debug=None) -> DynamicMesh
Apply a Mesh Bevel operation to all PolyGroup Edges.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshBevelOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_offset_faces"></a>

#### apply_mesh_offset_faces

```python
@classmethod
def apply_mesh_offset_faces(cls,
                            target_mesh: DynamicMesh,
                            options: GeometryScriptMeshOffsetFacesOptions,
                            selection: GeometryScriptMeshSelection,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_offset_faces(target_mesh, options, selection, debug=None) -> DynamicMesh
Apply an Offset to the faces of TargetMesh identified by the Selection, or all faces if the Selection is empty.
The Offset direction at each vertex can be derived from the averaged vertex normals or per-triangle normals.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshOffsetFacesOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_offset"></a>

#### apply_mesh_offset

```python
@classmethod
def apply_mesh_offset(cls,
                      target_mesh: DynamicMesh,
                      options: GeometryScriptMeshOffsetOptions,
                      debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_offset(target_mesh, options, debug=None) -> DynamicMesh
Offset the vertices of TargetMesh from their initial positions based on averaged vertex normals.
This function is intended for high-res meshes, for polymodeling-style offsets, ApplyMeshOffsetFaces will produce better results.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshOffsetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_linear_extrude_faces"></a>

#### apply_mesh_linear_extrude_faces

```python
@classmethod
def apply_mesh_linear_extrude_faces(
        cls,
        target_mesh: DynamicMesh,
        options: GeometryScriptMeshLinearExtrudeOptions,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_linear_extrude_faces(target_mesh, options, selection, debug=None) -> DynamicMesh
Apply Linear Extrusion (ie extrusion in a single direction) to the triangles of TargetMesh identified by the Selection.
The input Selection will still identify the same geometric elements after the Extrusion

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshLinearExtrudeOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_inset_outset_faces"></a>

#### apply_mesh_inset_outset_faces

```python
@classmethod
def apply_mesh_inset_outset_faces(
        cls,
        target_mesh: DynamicMesh,
        options: GeometryScriptMeshInsetOutsetFacesOptions,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_inset_outset_faces(target_mesh, options, selection, debug=None) -> DynamicMesh
Apply an Inset or Outset to the faces of TargetMesh identified by the Selection, or all faces if the Selection is empty.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshInsetOutsetFacesOptions): 
    selection (GeometryScriptMeshSelection): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_extrude_compatibility_5p0"></a>

#### apply_mesh_extrude_compatibility_5p0

```python
@classmethod
def apply_mesh_extrude_compatibility_5p0(
        cls,
        target_mesh: DynamicMesh,
        options: GeometryScriptMeshExtrudeOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_extrude_compatibility_5p0(target_mesh, options, debug=None) -> DynamicMesh
Backwards-Compatibility implementations
---------------------------------------------
These are versions/variants of the above functions that were released
in previous UE 5.x versions, that have since been updated.
To avoid breaking user scripts, these previous versions are currently kept and
called via redirectors registered in GeometryScriptingCoreModule.cpp.

These functions may be deprecated in future UE releases.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshExtrudeOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_extrude"></a>

#### apply_mesh_extrude

```python
@classmethod
def apply_mesh_extrude(cls,
                       target_mesh: DynamicMesh,
                       options: GeometryScriptMeshExtrudeOptions,
                       debug: GeometryScriptDebug = None) -> DynamicMesh
```

deprecated: 'apply_mesh_extrude' was renamed to 'apply_mesh_extrude_compatibility_5p0'.

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_duplicate_faces"></a>

#### apply_mesh_duplicate_faces

```python
@classmethod
def apply_mesh_duplicate_faces(
    cls,
    target_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    group_options: GeometryScriptMeshEditPolygroupOptions = [
        GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0
    ],
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.apply_mesh_duplicate_faces(target_mesh, selection, group_options=[GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0], debug=None) -> (DynamicMesh, new_triangles=GeometryScriptMeshSelection)
Duplicate the triangles of TargetMesh identified by the Selection

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    group_options (GeometryScriptMeshEditPolygroupOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptMeshSelection: 

    new_triangles (GeometryScriptMeshSelection): a Mesh Selection of the duplicate triangles is returned here (with type Triangles)

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_disconnect_faces_along_edges"></a>

#### apply_mesh_disconnect_faces_along_edges

```python
@classmethod
def apply_mesh_disconnect_faces_along_edges(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_disconnect_faces_along_edges(target_mesh, selection, debug=None) -> DynamicMesh
Disconnect triangles of TargetMesh along the edges of the Selection.
The input Selection will still identify the same geometric elements after Disconnecting.

Args:
    target_mesh (DynamicMesh): Mesh to operate on
    selection (GeometryScriptMeshSelection): Which edges to operate on. Non-edge selections will be interpreted as edge selections -- i.e., all selected triangles' edges, or all selected vertices' one-ring edges.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_disconnect_faces"></a>

#### apply_mesh_disconnect_faces

```python
@classmethod
def apply_mesh_disconnect_faces(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        allow_bowties_in_output: bool = True,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_disconnect_faces(target_mesh, selection, allow_bowties_in_output=True, debug=None) -> DynamicMesh
Disconnect the triangles of TargetMesh identified by the Selection.
The input Selection will still identify the same geometric elements after Disconnecting.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    allow_bowties_in_output (bool): if false, any bowtie vertices created by the operation will be automatically split
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_bevel_selection"></a>

#### apply_mesh_bevel_selection

```python
@classmethod
def apply_mesh_bevel_selection(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        bevel_mode: GeometryScriptMeshBevelSelectionMode,
        bevel_options: GeometryScriptMeshBevelSelectionOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_bevel_selection(target_mesh, selection, bevel_mode, bevel_options, debug=None) -> DynamicMesh
Apply a Mesh Bevel operation to parts of TargetMesh using the BevelOptions settings, with additional options to handle region selections

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): specifies which mesh edges to Bevel
    bevel_mode (GeometryScriptMeshBevelSelectionMode): specifies whether Selection should be optionally converted to a Triangle Region or set of PolyGroup Edges
    bevel_options (GeometryScriptMeshBevelSelectionOptions): settings for the Bevel Operation
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling.apply_mesh_bevel_edge_selection"></a>

#### apply_mesh_bevel_edge_selection

```python
@classmethod
def apply_mesh_bevel_edge_selection(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        bevel_options: GeometryScriptMeshBevelSelectionOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_bevel_edge_selection(target_mesh, selection, bevel_options, debug=None) -> DynamicMesh
Apply a Mesh Bevel operation to parts of TargetMesh using the BevelOptions settings.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): specifies which mesh edges to Bevel
    bevel_options (GeometryScriptMeshBevelSelectionOptions): settings for the Bevel Operation
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Normals"></a>