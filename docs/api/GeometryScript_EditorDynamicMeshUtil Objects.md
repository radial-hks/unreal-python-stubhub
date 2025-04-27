## GeometryScript_EditorDynamicMeshUtil Objects

```python
class GeometryScript_EditorDynamicMeshUtil(BlueprintFunctionLibrary)
```

Geometry Script Library Editor Dynamic Mesh Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingEditor
- **File**: EditorDynamicMeshUtilityFunctions.h

<a id="unreal.GeometryScript_EditorDynamicMeshUtil.stash_debug_mesh"></a>

#### stash_debug_mesh

```python
@classmethod
def stash_debug_mesh(cls, target_mesh: DynamicMesh,
                     debug_mesh_name: str) -> DynamicMesh
```

X.stash_debug_mesh(target_mesh, debug_mesh_name) -> DynamicMesh
Store a copy of TargetMesh with name DebugMeshName.
The mesh can later be recovered via FetchDebugMesh.
warning: This function stores the mesh in a global data structure, the caller must take care to avoid storing large numbers of debug meshes

Args:
    target_mesh (DynamicMesh): 
    debug_mesh_name (str): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_EditorDynamicMeshUtil.fetch_debug_mesh"></a>

#### fetch_debug_mesh

```python
@classmethod
def fetch_debug_mesh(cls, debug_mesh_name: str, to_target_mesh: DynamicMesh,
                     clear_debug_mesh: bool) -> Tuple[DynamicMesh, bool]
```

X.fetch_debug_mesh(debug_mesh_name, to_target_mesh, clear_debug_mesh) -> (DynamicMesh, debug_mesh_exists=bool)
Fetch a debug FDynamicMesh3 saved with DebugMeshName from the global debug mesh storage and copy to ToTargetMesh.
If DebugMeshName does not exist, a cube will be returned.

Args:
    debug_mesh_name (str): 
    to_target_mesh (DynamicMesh): 
    clear_debug_mesh (bool): if true, debug mesh will be removed from global storage

Returns:
    bool: 

    debug_mesh_exists (bool): will return as true if DebugMeshName existed

<a id="unreal.GeometryScript_EditorDynamicMeshUtil.emit_tracked_mesh_change"></a>

#### emit_tracked_mesh_change

```python
@classmethod
def emit_tracked_mesh_change(
    cls, target_mesh: DynamicMesh, change_tracker: DynamicMeshChangeContainer
) -> Tuple[DynamicMesh, DynamicMeshChangeContainer]
```

X.emit_tracked_mesh_change(target_mesh, change_tracker) -> (DynamicMesh, change_tracker=DynamicMeshChangeContainer)
Emit an undo/redo Change for a modified TargetMesh, based on the ChangeTracker information that was
saved (via call to BeginTrackedMeshChange) before TargetMesh was modified. This function must be
called in the context of a Transaction (ie BeginTransaction / EndTransaction pair)

Args:
    target_mesh (DynamicMesh): 
    change_tracker (DynamicMeshChangeContainer): 

Returns:
    DynamicMeshChangeContainer: 

    change_tracker (DynamicMeshChangeContainer):

<a id="unreal.GeometryScript_EditorDynamicMeshUtil.begin_tracked_mesh_change"></a>

#### begin_tracked_mesh_change

```python
@classmethod
def begin_tracked_mesh_change(
    cls, target_mesh: DynamicMesh
) -> Tuple[DynamicMesh, DynamicMeshChangeContainer]
```

X.begin_tracked_mesh_change(target_mesh) -> (DynamicMesh, change_tracker=DynamicMeshChangeContainer)
Save current state of TargetMesh so that an undoable/redoable Change can be emitted
after TargetMesh is modified, using EmitTrackedMeshChange().

Args:
    target_mesh (DynamicMesh): 

Returns:
    DynamicMeshChangeContainer: 

    change_tracker (DynamicMeshChangeContainer): output structure containing initial TargetMesh state

<a id="unreal.GeometryScript_EditorTextureUtils"></a>