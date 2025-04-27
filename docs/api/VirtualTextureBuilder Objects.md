## VirtualTextureBuilder Objects

```python
class VirtualTextureBuilder(Object)
```

Container for a UVirtualTexture2D that can be built from a FVirtualTextureBuildDesc description.
This has a simple BuildTexture() interface but we may want to extend in the future to support partial builds
or other more blueprint driven approaches for data generation.

**C++ Source:**

- **Module**: Engine
- **File**: VirtualTextureBuilder.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``separate_texture_for_mobile`` (bool):  [Read-Write] Whether to use a separate texture for Mobile rendering, only if virtual texture support on Mobile is enabled and if RVT support on mobile is enabled in the project settings (see r.Mobile.VirtualTextures). A separate texture will be built using mobile preview editor mode. Use this in case there is too much discrepancy between the RVT used for desktop vs. mobile.
- ``texture`` (VirtualTexture2D):  [Read-Only] The (embedded) texture asset. Use Build Virtual Textures in the Build menu, or the Build button in the Runtime Virtual Texture Component to create/update it.
- ``texture_mobile`` (VirtualTexture2D):  [Read-Only] The (embedded) texture asset for mobile rendering, only if virtual texture support on Mobile is enabled and if RVT support on mobile is enabled in the project settings (see r.Mobile.VirtualTextures). Use Build Virtual Textures or the Build button in the Runtime Virtual Texture Component to create/update it.

<a id="unreal.VirtualTextureBuilder.texture"></a>

#### texture

```python
@property
def texture() -> VirtualTexture2D
```

(VirtualTexture2D):  [Read-Only] The (embedded) texture asset. Use Build Virtual Textures in the Build menu, or the Build button in the Runtime Virtual Texture Component to create/update it.

<a id="unreal.VirtualTextureBuilder.texture_mobile"></a>

#### texture_mobile

```python
@property
def texture_mobile() -> VirtualTexture2D
```

(VirtualTexture2D):  [Read-Only] The (embedded) texture asset for mobile rendering, only if virtual texture support on Mobile is enabled and if RVT support on mobile is enabled in the project settings (see r.Mobile.VirtualTextures). Use Build Virtual Textures or the Build button in the Runtime Virtual Texture Component to create/update it.

<a id="unreal.WindDirectionalSource"></a>