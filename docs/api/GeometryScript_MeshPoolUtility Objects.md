## GeometryScript_MeshPoolUtility Objects

```python
class GeometryScript_MeshPoolUtility(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Pool Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPoolFunctions.h

<a id="unreal.GeometryScript_MeshPoolUtility.get_global_mesh_pool"></a>

#### get_global_mesh_pool

```python
@classmethod
def get_global_mesh_pool(cls) -> DynamicMeshPool
```

X.get_global_mesh_pool() -> DynamicMeshPool
Access a global compute mesh pool (created on first access)

Returns:
    DynamicMeshPool:

<a id="unreal.GeometryScript_MeshPoolUtility.discard_global_mesh_pool"></a>

#### discard_global_mesh_pool

```python
@classmethod
def discard_global_mesh_pool(cls) -> None
```

X.discard_global_mesh_pool() -> None
Fully clear/destroy the current global mesh pool, allowing it and all its meshes to be garbage collected

<a id="unreal.GeometryScript_Primitives"></a>