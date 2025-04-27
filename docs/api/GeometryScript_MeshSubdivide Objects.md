## GeometryScript_MeshSubdivide Objects

```python
class GeometryScript_MeshSubdivide(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Subdivide Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSubdivideFunctions.h

<a id="unreal.GeometryScript_MeshSubdivide.apply_uniform_tessellation"></a>

#### apply_uniform_tessellation

```python
@classmethod
def apply_uniform_tessellation(
        cls,
        target_mesh: DynamicMesh,
        tessellation_level: int = 3,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_uniform_tessellation(target_mesh, tessellation_level=3, debug=None) -> DynamicMesh
Apply Uniform Tessellation to the Target Mesh as controlled by the Tessellation Level and the Options.

Args:
    target_mesh (DynamicMesh): 
    tessellation_level (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshSubdivide.apply_selective_tessellation"></a>

#### apply_selective_tessellation

```python
@classmethod
def apply_selective_tessellation(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        options: GeometryScriptSelectiveTessellateOptions,
        tessellation_level: int = 1,
        pattern_type:
    SelectiveTessellatePatternType = SelectiveTessellatePatternType.
    CONCENTRIC_RINGS,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_selective_tessellation(target_mesh, selection, options, tessellation_level=1, pattern_type=SelectiveTessellatePatternType.CONCENTRIC_RINGS, debug=None) -> DynamicMesh
Selectively Tessellate a Selection of the Target Mesh or possibly the entire mesh as controlled by
the Options.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): selects the triangles of the mesh to be tessellated.
    options (GeometryScriptSelectiveTessellateOptions): controls the behavior of the tessellation if the Selection is empty.
    tessellation_level (int32): determines the amount of tessellation
    pattern_type (SelectiveTessellatePatternType): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshSubdivide.apply_pn_tessellation"></a>

#### apply_pn_tessellation

```python
@classmethod
def apply_pn_tessellation(cls,
                          target_mesh: DynamicMesh,
                          options: GeometryScriptPNTessellateOptions,
                          tessellation_level: int = 3,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_pn_tessellation(target_mesh, options, tessellation_level=3, debug=None) -> DynamicMesh
Apply PN Tessellation to the Target Mesh as controlled by the Tessellation Level and the Options.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptPNTessellateOptions): 
    tessellation_level (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms"></a>