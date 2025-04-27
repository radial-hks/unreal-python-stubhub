## GenerateStaticMeshLODProcessSettings Objects

```python
class GenerateStaticMeshLODProcessSettings(StructBase)
```

Generate Static Mesh LODProcess Settings

**C++ Source:**

- **Plugin**: MeshLODToolset
- **Module**: MeshLODToolset
- **File**: GenerateStaticMeshLODProcess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``closure_distance`` (float):  [Read-Write] Offset distance in the Morpohological Closure operation
- ``mesh_generator`` (GenerateStaticMeshLODProcess_MeshGeneratorModes):  [Read-Write] Method used to generate the initial mesh for AutoLOD processing
- ``prefilter_grid_resolution`` (int32):  [Read-Write] Grid resolution (along the maximum-length axis) for subsampling before computing the convex hull
- ``prefilter_vertices`` (bool):  [Read-Write] Whether to subsample input vertices using a regular grid before computing the convex hull
- ``solidify_voxel_resolution`` (int32):  [Read-Write] Target number of voxels along the maximum dimension for Solidify operation
- ``winding_threshold`` (float):  [Read-Write] Winding number threshold to determine what is considered inside the mesh during Solidify

<a id="unreal.GenerateStaticMeshLODProcessSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GenerateStaticMeshLODProcess_SimplifySettings"></a>