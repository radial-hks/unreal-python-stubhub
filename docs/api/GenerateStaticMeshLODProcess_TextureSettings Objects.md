## GenerateStaticMeshLODProcess_TextureSettings Objects

```python
class GenerateStaticMeshLODProcess_TextureSettings(StructBase)
```

Generate Static Mesh LODProcess Texture Settings

**C++ Source:**

- **Plugin**: MeshLODToolset
- **Module**: MeshLODToolset
- **File**: GenerateStaticMeshLODProcess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bake_resolution`` (GenerateStaticMeshLODBakeResolution):  [Read-Write] Resolution for normal map and texture baking
- ``bake_thickness`` (float):  [Read-Write] How far away from the output mesh to search for input mesh during baking
- ``combine_textures`` (bool):  [Read-Write] Generate an atlassed texture where multiple textures are combined into a single output texture

<a id="unreal.GenerateStaticMeshLODProcess_TextureSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GenerateStaticMeshLODProcess_UVSettings"></a>