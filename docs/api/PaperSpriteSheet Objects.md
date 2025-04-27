## PaperSpriteSheet Objects

```python
class PaperSpriteSheet(Object)
```

Paper Sprite Sheet

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: PaperSpriteSheetImporter
- **File**: PaperSpriteSheet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] Import data for this
- ``normal_map_texture`` (Texture2D):  [Read-Only] The asset that was created for NormalMapTextureName (if any)
- ``normal_map_texture_name`` (str):  [Read-Only] The name of the normal map texture during import (if any)
- ``sprite_names`` (Array[str]):  [Read-Only] The names of sprites during import
- ``sprites`` (Array[PaperSprite]):  [Read-Only]
- ``texture`` (Texture2D):  [Read-Only] The asset that was created for TextureName
- ``texture_name`` (str):  [Read-Only] The name of the default or diffuse texture during import

<a id="unreal.PaperSpriteSheetImportFactory"></a>