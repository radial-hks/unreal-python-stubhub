## StaticMeshLODGenerationSettings Objects

```python
class StaticMeshLODGenerationSettings(Object)
```

UStaticMeshLODGenerationSettings is intended to be a stored version of the settings used
by UGenerateStaticMeshLODProcess (and the associated UGenerateStaticMeshLODAssetTool).
This UObject is exposed as an Asset type in the Editor via UStaticMeshLODGenerationSettingsFactory.

The Tool uses these serialized settings as a 'Preset', ie the user can save a set
of configured settings, or load previously-saved settings.

**C++ Source:**

- **Plugin**: MeshLODToolset
- **Module**: MeshLODToolset
- **File**: LODGenerationSettingsAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mesh_generation`` (GenerateStaticMeshLODProcessSettings):  [Read-Write]
- ``normals`` (GenerateStaticMeshLODProcess_NormalsSettings):  [Read-Write]
- ``preprocessing`` (GenerateStaticMeshLODProcess_PreprocessSettings):  [Read-Write]
- ``simple_collision`` (GenerateStaticMeshLODProcess_CollisionSettings):  [Read-Write]
- ``simplification`` (GenerateStaticMeshLODProcess_SimplifySettings):  [Read-Write]
- ``texture_baking`` (GenerateStaticMeshLODProcess_TextureSettings):  [Read-Write]
- ``uv_generation`` (GenerateStaticMeshLODProcess_UVSettings):  [Read-Write]

<a id="unreal.StaticMeshLODGenerationSettingsFactory"></a>