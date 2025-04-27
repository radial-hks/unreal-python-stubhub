## GenerateStaticMeshLODProcess_UVSettings Objects

```python
class GenerateStaticMeshLODProcess_UVSettings(StructBase)
```

Generate Static Mesh LODProcess UVSettings

**C++ Source:**

- **Plugin**: MeshLODToolset
- **Module**: MeshLODToolset
- **File**: GenerateStaticMeshLODProcess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_angle_deviation`` (float):  [Read-Write] UV islands will not be merged if their average face normals deviate by larger than this amount
- ``merging_threshold`` (float):  [Read-Write] Distortion/Stretching Threshold for island merging - larger values increase the allowable UV stretching
- ``num_initial_patches`` (int32):  [Read-Write] Number of initial patches mesh will be split into before computing island merging
- ``num_uv_atlas_charts`` (int32):  [Read-Write] Maximum number of charts to create in UVAtlas
- ``patch_builder`` (GenerateStaticMeshLODProcess_UVSettings_PatchBuilder):  [Read-Write]
- ``uv_method`` (GenerateStaticMeshLODProcess_AutoUVMethod):  [Read-Write]

<a id="unreal.GenerateStaticMeshLODProcess_UVSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GenerateStaticMeshLODProcess_CollisionSettings"></a>