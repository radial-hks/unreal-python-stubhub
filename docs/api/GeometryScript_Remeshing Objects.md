## GeometryScript_Remeshing Objects

```python
class GeometryScript_Remeshing(BlueprintFunctionLibrary)
```

Geometry Script Library Remeshing Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRemeshFunctions.h

<a id="unreal.GeometryScript_Remeshing.apply_uniform_remesh"></a>

#### apply_uniform_remesh

```python
@classmethod
def apply_uniform_remesh(cls,
                         target_mesh: DynamicMesh,
                         remesh_options: GeometryScriptRemeshOptions,
                         uniform_options: GeometryScriptUniformRemeshOptions,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_uniform_remesh(target_mesh, remesh_options, uniform_options, debug=None) -> DynamicMesh
Apply Uniform Remeshing to the TargetMesh.
warning: this function can be quite expensive. The results may be non-deterministic, and are expected to change in future versions.

Args:
    target_mesh (DynamicMesh): 
    remesh_options (GeometryScriptRemeshOptions): 
    uniform_options (GeometryScriptUniformRemeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshRepair"></a>