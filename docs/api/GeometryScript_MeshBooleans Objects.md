## GeometryScript_MeshBooleans Objects

```python
class GeometryScript_MeshBooleans(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Boolean Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBooleanFunctions.h

<a id="unreal.GeometryScript_MeshBooleans.apply_mesh_self_union"></a>

#### apply_mesh_self_union

```python
@classmethod
def apply_mesh_self_union(cls,
                          target_mesh: DynamicMesh,
                          options: GeometryScriptMeshSelfUnionOptions,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_self_union(target_mesh, options, debug=None) -> DynamicMesh
Mesh-Boolean-Union an object with itself to repair self-intersections, remove floating geometry, etc.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshSelfUnionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshBooleans.apply_mesh_plane_slice"></a>

#### apply_mesh_plane_slice

```python
@classmethod
def apply_mesh_plane_slice(cls,
                           target_mesh: DynamicMesh,
                           cut_frame: Transform,
                           options: GeometryScriptMeshPlaneSliceOptions,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_plane_slice(target_mesh, cut_frame, options, debug=None) -> DynamicMesh
Slices a mesh into two halves, with optional hole filling.

Args:
    target_mesh (DynamicMesh): Dynamic Mesh to be updated by the slice.
    cut_frame (Transform): defines the plane used to slice the TargetMesh.
    options (GeometryScriptMeshPlaneSliceOptions): selects additional clean-up operations performed after the cut.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshBooleans.apply_mesh_plane_cut"></a>

#### apply_mesh_plane_cut

```python
@classmethod
def apply_mesh_plane_cut(cls,
                         target_mesh: DynamicMesh,
                         cut_frame: Transform,
                         options: GeometryScriptMeshPlaneCutOptions,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_plane_cut(target_mesh, cut_frame, options, debug=None) -> DynamicMesh
Applies a plane cut to a mesh, optionally filling any holes created.

Args:
    target_mesh (DynamicMesh): Dynamic Mesh to updated with the cut
    cut_frame (Transform): defines the plane used to cut the TargetMesh
    options (GeometryScriptMeshPlaneCutOptions): selects additional clean-up operations performed after the cut.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshBooleans.apply_mesh_mirror"></a>

#### apply_mesh_mirror

```python
@classmethod
def apply_mesh_mirror(cls,
                      target_mesh: DynamicMesh,
                      mirror_frame: Transform,
                      options: GeometryScriptMeshMirrorOptions,
                      debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_mirror(target_mesh, mirror_frame, options, debug=None) -> DynamicMesh
Mirrors a mesh across a plane, with optional cutting and welding of triangles.

Args:
    target_mesh (DynamicMesh): Dynamic Mesh to be updated by the mirror operation.
    mirror_frame (Transform): defines the plane used to mirror the TargetMesh.
    options (GeometryScriptMeshMirrorOptions): selects  additional clean-up operations performed after the mirror.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshBooleans.apply_mesh_boolean"></a>

#### apply_mesh_boolean

```python
@classmethod
def apply_mesh_boolean(cls,
                       target_mesh: DynamicMesh,
                       target_transform: Transform,
                       tool_mesh: DynamicMesh,
                       tool_transform: Transform,
                       operation: GeometryScriptBooleanOperation,
                       options: GeometryScriptMeshBooleanOptions,
                       debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_boolean(target_mesh, target_transform, tool_mesh, tool_transform, operation, options, debug=None) -> DynamicMesh
Applies a Boolean operation (such as, Union, Intersect, and Subtract) to the Target Dynamic Mesh based on a Tool Dynamic Mesh.

Args:
    target_mesh (DynamicMesh): Dynamic Mesh to be acted upon
    target_transform (Transform): used to position the TargetMesh
    tool_mesh (DynamicMesh): Dynamic Mesh that acts as the cutting tool
    tool_transform (Transform): used to position the ToolMesh
    operation (GeometryScriptBooleanOperation): selects the specific boolean operation
    options (GeometryScriptMeshBooleanOptions): selects additional options that are applied to the result
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshComparison"></a>