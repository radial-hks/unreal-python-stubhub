## PaperSpriteAtlas Objects

```python
class PaperSpriteAtlas(Object)
```

Groups together a set of sprites that will try to share the same texture atlas (allowing them to be combined into a single draw call)

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperSpriteAtlas.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``atlas_description`` (str):  [Read-Write] Description of this atlas, which shows up in the content browser tooltip
- ``atlas_guid`` (Guid):  [Read-Only] The GUID of the atlas group, used to match up sprites that belong to this group even thru atlas renames
- ``compression_settings`` (TextureCompressionSettings):  [Read-Write] Compression settings to use on atlas texture
- ``filter`` (TextureFilter):  [Read-Write] Texture filtering mode when sampling these textures
- ``generated_textures`` (Array[Texture]):  [Read-Only] List of generated atlas textures
- ``max_height`` (int32):  [Read-Write] Maximum atlas page height (single pages might be smaller)
- ``max_width`` (int32):  [Read-Write] Maximum atlas page width (single pages might be smaller)
- ``mip_count`` (int32):  [Read-Write] Maximum atlas page height (single pages might be smaller)
- ``padding`` (int32):  [Read-Write] The number of pixels of padding
- ``padding_type`` (PaperSpriteAtlasPadding):  [Read-Write] The type of padding performed on this atlas
- ``rebuild_atlas`` (bool):  [Read-Write] Slots in the atlas

<a id="unreal.PaperSpriteLibrary"></a>