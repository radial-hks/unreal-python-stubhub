## GeometryScript_MeshVoxelProcessing Objects

```python
class GeometryScript_MeshVoxelProcessing(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Voxel Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshVoxelFunctions.h

<a id="unreal.GeometryScript_MeshVoxelProcessing.apply_mesh_solidify"></a>

#### apply_mesh_solidify

```python
@classmethod
def apply_mesh_solidify(cls,
                        target_mesh: DynamicMesh,
                        options: GeometryScriptSolidifyOptions,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_solidify(target_mesh, options, debug=None) -> DynamicMesh
Replaces the mesh with a voxelized-and-meshed approximation (VoxWrap operation).

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptSolidifyOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshVoxelProcessing.apply_mesh_morphology"></a>

#### apply_mesh_morphology

```python
@classmethod
def apply_mesh_morphology(cls,
                          target_mesh: DynamicMesh,
                          options: GeometryScriptMorphologyOptions,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_mesh_morphology(target_mesh, options, debug=None) -> DynamicMesh
Replaces the mesh with an SDF-based offset mesh approximation.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMorphologyOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PointSetSampling"></a>