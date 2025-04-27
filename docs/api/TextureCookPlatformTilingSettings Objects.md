## TextureCookPlatformTilingSettings Objects

```python
class TextureCookPlatformTilingSettings(EnumBase)
```

Texture Cook Platform Tiling Settings

**C++ Source:**

- **Module**: Engine
- **File**: TextureDefines.h

<a id="unreal.TextureCookPlatformTilingSettings.TCPTS_FROM_TEXTURE_GROUP"></a>

#### TCPTS_FROM_TEXTURE_GROUP

0: Get the tiling setting from the texture's group CookPlatformTilingDisabled setting. By default it's to tile during cook, unless it has been changed in the texture group

<a id="unreal.TextureCookPlatformTilingSettings.TCPTS_TILE"></a>

#### TCPTS_TILE

1: The texture will be tiled during the cook process if the platform supports it.

<a id="unreal.TextureCookPlatformTilingSettings.TCPTS_DO_NOT_TILE"></a>

#### TCPTS_DO_NOT_TILE

2: The texture will not be tiled during the cook process, and will be tiled when uploaded to the GPU if the platform supports it.

<a id="unreal.TextureGroup"></a>