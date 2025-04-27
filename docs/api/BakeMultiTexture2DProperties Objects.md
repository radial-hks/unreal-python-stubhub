## BakeMultiTexture2DProperties Objects

```python
class BakeMultiTexture2DProperties(InteractiveToolPropertySet)
```

Bake Multi Texture 2DProperties

**C++ Source:**

- **Plugin**: MeshModelingToolsetExp
- **Module**: MeshModelingToolsExp
- **File**: BakeMeshAttributeToolCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``all_source_textures`` (Array[Texture2D]):  [Read-Only] The set of all source textures from all input materials
- ``material_id_source_textures`` (Array[Texture2D]):  [Read-Write] For each material ID, the source texture that will be resampled in that material's region
- ``uv_layer`` (str):  [Read-Write] UV channel to use for the source mesh texture

<a id="unreal.BakeMultiTexture2DProperties.all_source_textures"></a>

#### all_source_textures

```python
@property
def all_source_textures() -> Array[Texture2D]
```

(Array[Texture2D]):  [Read-Only] The set of all source textures from all input materials

<a id="unreal.DataflowAssetFactory"></a>