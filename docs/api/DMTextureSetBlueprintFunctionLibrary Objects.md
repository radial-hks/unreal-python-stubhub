## DMTextureSetBlueprintFunctionLibrary Objects

```python
class DMTextureSetBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Material Designer Texture Set Blueprint Function Library

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialTextureSetEditor
- **File**: DMTextureSetBlueprintFunctionLibrary.h

<a id="unreal.DMTextureSetBlueprintFunctionLibrary.create_texture_set_from_assets"></a>

#### create_texture_set_from_assets

```python
@classmethod
def create_texture_set_from_assets(cls,
                                   assets: Array[AssetData]) -> DMTextureSet
```

X.create_texture_set_from_assets(assets) -> DMTextureSet
Uses the filters from the Texture Set Settings to create a Texture Set based on the given assets.

Args:
    assets (Array[AssetData]): The texture assets to assign to the texture slot.

Returns:
    DMTextureSet: A new texture set or nullptr if no textures were filtered.

<a id="unreal.DMTextureSetFactory"></a>