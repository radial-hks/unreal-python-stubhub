## UDIMTextureFunctionLibrary Objects

```python
class UDIMTextureFunctionLibrary(BlueprintFunctionLibrary)
```

UDIMTexture Function Library

**C++ Source:**

- **Module**: UnrealEd
- **File**: TextureFactory.h

<a id="unreal.UDIMTextureFunctionLibrary.make_udim_virtual_texture_from_texture2_ds"></a>

#### make_udim_virtual_texture_from_texture2_ds

```python
@classmethod
def make_udim_virtual_texture_from_texture2_ds(
        cls,
        output_path_name: str,
        source_textures: Array[Texture2D],
        block_coords: Array[IntPoint],
        keep_existing_settings: bool = False,
        check_out_and_save: bool = False) -> Texture2D
```

X.make_udim_virtual_texture_from_texture2_ds(output_path_name, source_textures, block_coords, keep_existing_settings=False, check_out_and_save=False) -> Texture2D
Make a UDIM virtual texture from a list of regular 2D textures

Args:
    output_path_name (str): Path name of the UDIM texture (e.g. /Game/MyTexture)
    source_textures (Array[Texture2D]): List of regular 2D textures to be packed into the atlas
    block_coords (Array[IntPoint]): Coordinates of the corresponding texture in the atlas
    keep_existing_settings (bool): Whether to keep existing settings if a texture with the same path name exists. Otherwise, settings will be copied from the first source texture
    check_out_and_save (bool): Whether to check out and save the UDIM texture

Returns:
    Texture2D: UTexture2D*                   Pointer to the UDIM texture or null if failed

<a id="unreal.TextureRenderTarget2DArrayFactoryNew"></a>