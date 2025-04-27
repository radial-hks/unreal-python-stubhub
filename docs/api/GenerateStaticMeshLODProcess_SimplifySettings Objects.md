## GenerateStaticMeshLODProcess_SimplifySettings Objects

```python
class GenerateStaticMeshLODProcess_SimplifySettings(StructBase)
```

Generate Static Mesh LODProcess Simplify Settings

**C++ Source:**

- **Plugin**: MeshLODToolset
- **Module**: MeshLODToolset
- **File**: GenerateStaticMeshLODProcess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``method`` (GenerateStaticMeshLODProcess_SimplifyMethod):  [Read-Write] Method used to simplify the mesh created in the Mesh Generation step
- ``target_count`` (int32):  [Read-Write] Target triangle/vertex count after simplification
- ``target_percentage`` (float):  [Read-Write] Target triangle/vertex count after simplification
- ``tolerance`` (float):  [Read-Write] Deviation in World Units (Centimeters)

<a id="unreal.GenerateStaticMeshLODProcess_SimplifySettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GenerateStaticMeshLODProcess_NormalsSettings"></a>