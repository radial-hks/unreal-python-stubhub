## UrbanBuildTemplateTextureComponent Objects

```python
class UrbanBuildTemplateTextureComponent(Object)
```

Urban Build Template Texture Component

**C++ Source:**

- **Plugin**: AesBuilder
- **Module**: UrbanBuilder
- **File**: UrbanBuildTemplateTextureComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``address_x`` (TextureAddress):  [Read-Write] The addressing mode to use for the X axis.
- ``address_y`` (TextureAddress):  [Read-Write] The addressing mode to use for the Y axis.
- ``adjust_brightness`` (float):  [Read-Write] Static texture brightness adjustment (scales HSV value.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_brightness_curve`` (float):  [Read-Write] Static texture curve adjustment (raises HSV value to the specified power.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_hue`` (float):  [Read-Write] Static texture hue adjustment (0 - 360) (offsets HSV hue by value in degrees.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_max_alpha`` (float):  [Read-Write] Remaps the alpha to the specified min/max range, defines the new value of 1 (Non-destructive; Requires texture source art to be available.)
- ``adjust_min_alpha`` (float):  [Read-Write] Remaps the alpha to the specified min/max range, defines the new value of 0 (Non-destructive; Requires texture source art to be available.)
- ``adjust_rgb_curve`` (float):  [Read-Write] Static texture RGB curve adjustment (raises linear-space RGB color to the specified power.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_saturation`` (float):  [Read-Write] Static texture saturation adjustment (scales HSV saturation.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_vibrance`` (float):  [Read-Write] Static texture "vibrance" adjustment (0 - 1) (HSV saturation algorithm adjustment.)  (Non-destructive; Requires texture source art to be available.)
- ``alpha_coverage_thresholds`` (Vector4):  [Read-Write] Alpha values per channel to compare to when preserving alpha coverage.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``chroma_key_color`` (Color):  [Read-Write] The color that will be replaced with transparent black if chroma keying is enabled
- ``chroma_key_texture`` (bool):  [Read-Write] Whether to chroma key the image, replacing any pixels that match ChromaKeyColor with transparent black
- ``chroma_key_threshold`` (float):  [Read-Write] The threshold that components have to match for the texel to be considered equal to the ChromaKeyColor when chroma keying (<=, set to 0 to require a perfect exact match)
- ``composite_power`` (float):  [Read-Write] default 1, high values result in a stronger effect e.g 1, 2, 4, 8
  this is no slider because the texture update would not be fast enough
- ``composite_texture`` (Texture):  [Read-Write] Can be defined to modify the roughness based on the normal map variation (mostly from mip maps).
  MaxAlpha comes in handy to define a base roughness if no source alpha was there.
  Make sure the normal map has at least as many mips as this texture.
- ``composite_texture_mode`` (CompositeTextureMode):  [Read-Write] defines how the CompositeTexture is applied, e.g. CTM_RoughnessFromNormalAlpha
- ``compression_no_alpha`` (bool):  [Read-Write] If enabled, the texture's alpha channel will be discarded during compression
- ``compression_quality`` (TextureCompressionQuality):  [Read-Write] The compression quality for generated textures.
- ``compression_settings`` (TextureCompressionSettings):  [Read-Write]
- ``defer_compression`` (bool):  [Read-Write] If enabled, defer compression of the texture until save.
- ``dither_mip_map_alpha`` (bool):  [Read-Write] When true, the alpha channel of mip-maps and the base image are dithered for smooth LOD transitions.
- ``downscale`` (PerPlatformFloat):  [Read-Write]
- ``downscale_options`` (TextureDownscaleOptions):  [Read-Write] Texture downscaling options
- ``filter`` (TextureFilter):  [Read-Write] The texture filtering mode to use when sampling this texture.
- ``flip_green_channel`` (bool):  [Read-Write] When true the texture's green channel will be inverted. This is useful for some normal maps.
- ``force_pvrtc4`` (bool):  [Read-Write] For DXT1 textures, setting this will cause the texture to be twice the size, but better looking, on iPhone
- ``global_force_mip_levels_to_be_resident`` (bool):  [Read-Write] Global and serialized version of ForceMiplevelsToBeResident.
- ``lod_bias`` (int32):  [Read-Write] A bias to the index of the top mip level to use.
- ``lod_group`` (TextureGroup):  [Read-Write] Texture group this texture belongs to
- ``lossy_compression_amount`` (TextureLossyCompressionAmount):  [Read-Write] How aggressively should any relevant lossy compression be applied.
- ``max_texture_size`` (int32):  [Read-Write] The maximum resolution for generated textures. A value of 0 means the maximum size for the format on each platform, except HDR long/lat cubemaps, which default to a resolution of 512.
- ``mip_gen_settings`` (TextureMipGenSettings):  [Read-Write] Per asset specific setting to define the mip-map generation properties like sharpening and kernel size.
- ``mip_load_options`` (TextureMipLoadOptions):  [Read-Write] The texture mip load options.
- ``never_stream`` (bool):  [Read-Write]
- ``num_cinematic_mip_levels`` (int32):  [Read-Write] Number of mip-levels to use for cinematic quality.
- ``padding_color`` (Color):  [Read-Write] The color used to pad the texture out if it is resized due to PowerOfTwoMode
- ``power_of_two_mode`` (TexturePowerOfTwoSetting):  [Read-Write] How to pad the texture to a power of 2 size (if necessary)
- ``preserve_border`` (bool):  [Read-Write] When true the texture's border will be preserved during mipmap generation.
- ``srgb`` (bool):  [Read-Write] This should be unchecked if using alpha channels individually as masks.
- ``use_legacy_gamma`` (bool):  [Read-Write] A flag for using the simplified legacy gamma space e.g pow(color,1/2.2) for converting from FColor to FLinearColor, if we're doing sRGB.
- ``virtual_texture_streaming`` (bool):  [Read-Write] Is this texture streamed in using VT

<a id="unreal.UrbanBuildTemplateTextureComponent.power_of_two_mode"></a>

#### power\_of\_two\_mode

```python
@property
def power_of_two_mode() -> TexturePowerOfTwoSetting
```

(TexturePowerOfTwoSetting):  [Read-Write] How to pad the texture to a power of 2 size (if necessary)

<a id="unreal.UrbanBuildTemplateTextureComponent.power_of_two_mode"></a>

#### power\_of\_two\_mode

```python
@power_of_two_mode.setter
def power_of_two_mode(value: TexturePowerOfTwoSetting) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.srgb"></a>

#### srgb

```python
@property
def srgb() -> bool
```

(bool):  [Read-Write] This should be unchecked if using alpha channels individually as masks.

<a id="unreal.UrbanBuildTemplateTextureComponent.srgb"></a>

#### srgb

```python
@srgb.setter
def srgb(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.padding_color"></a>

#### padding\_color

```python
@property
def padding_color() -> Color
```

(Color):  [Read-Write] The color used to pad the texture out if it is resized due to PowerOfTwoMode

<a id="unreal.UrbanBuildTemplateTextureComponent.padding_color"></a>

#### padding\_color

```python
@padding_color.setter
def padding_color(value: Color) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.use_legacy_gamma"></a>

#### use\_legacy\_gamma

```python
@property
def use_legacy_gamma() -> bool
```

(bool):  [Read-Write] A flag for using the simplified legacy gamma space e.g pow(color,1/2.2) for converting from FColor to FLinearColor, if we're doing sRGB.

<a id="unreal.UrbanBuildTemplateTextureComponent.use_legacy_gamma"></a>

#### use\_legacy\_gamma

```python
@use_legacy_gamma.setter
def use_legacy_gamma(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.address_x"></a>

#### address\_x

```python
@property
def address_x() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the X axis.

<a id="unreal.UrbanBuildTemplateTextureComponent.address_x"></a>

#### address\_x

```python
@address_x.setter
def address_x(value: TextureAddress) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.address_y"></a>

#### address\_y

```python
@property
def address_y() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the Y axis.

<a id="unreal.UrbanBuildTemplateTextureComponent.address_y"></a>

#### address\_y

```python
@address_y.setter
def address_y(value: TextureAddress) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.filter"></a>

#### filter

```python
@property
def filter() -> TextureFilter
```

(TextureFilter):  [Read-Write] The texture filtering mode to use when sampling this texture.

<a id="unreal.UrbanBuildTemplateTextureComponent.filter"></a>

#### filter

```python
@filter.setter
def filter(value: TextureFilter) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.mip_load_options"></a>

#### mip\_load\_options

```python
@property
def mip_load_options() -> TextureMipLoadOptions
```

(TextureMipLoadOptions):  [Read-Write] The texture mip load options.

<a id="unreal.UrbanBuildTemplateTextureComponent.mip_load_options"></a>

#### mip\_load\_options

```python
@mip_load_options.setter
def mip_load_options(value: TextureMipLoadOptions) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.virtual_texture_streaming"></a>

#### virtual\_texture\_streaming

```python
@property
def virtual_texture_streaming() -> bool
```

(bool):  [Read-Only] Is this texture streamed in using VT

<a id="unreal.UrbanBuildTemplateTextureComponent.alpha_coverage_thresholds"></a>

#### alpha\_coverage\_thresholds

```python
@property
def alpha_coverage_thresholds() -> Vector4
```

(Vector4):  [Read-Write] Alpha values per channel to compare to when preserving alpha coverage.

<a id="unreal.UrbanBuildTemplateTextureComponent.alpha_coverage_thresholds"></a>

#### alpha\_coverage\_thresholds

```python
@alpha_coverage_thresholds.setter
def alpha_coverage_thresholds(value: Vector4) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.dither_mip_map_alpha"></a>

#### dither\_mip\_map\_alpha

```python
@property
def dither_mip_map_alpha() -> bool
```

(bool):  [Read-Write] When true, the alpha channel of mip-maps and the base image are dithered for smooth LOD transitions.

<a id="unreal.UrbanBuildTemplateTextureComponent.dither_mip_map_alpha"></a>

#### dither\_mip\_map\_alpha

```python
@dither_mip_map_alpha.setter
def dither_mip_map_alpha(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.flip_green_channel"></a>

#### flip\_green\_channel

```python
@property
def flip_green_channel() -> bool
```

(bool):  [Read-Write] When true the texture's green channel will be inverted. This is useful for some normal maps.

<a id="unreal.UrbanBuildTemplateTextureComponent.flip_green_channel"></a>

#### flip\_green\_channel

```python
@flip_green_channel.setter
def flip_green_channel(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.compression_no_alpha"></a>

#### compression\_no\_alpha

```python
@property
def compression_no_alpha() -> bool
```

(bool):  [Read-Write] If enabled, the texture's alpha channel will be discarded during compression

<a id="unreal.UrbanBuildTemplateTextureComponent.compression_no_alpha"></a>

#### compression\_no\_alpha

```python
@compression_no_alpha.setter
def compression_no_alpha(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.defer_compression"></a>

#### defer\_compression

```python
@property
def defer_compression() -> bool
```

(bool):  [Read-Write] If enabled, defer compression of the texture until save.

<a id="unreal.UrbanBuildTemplateTextureComponent.defer_compression"></a>

#### defer\_compression

```python
@defer_compression.setter
def defer_compression(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.compression_settings"></a>

#### compression\_settings

```python
@property
def compression_settings() -> TextureCompressionSettings
```

(TextureCompressionSettings):  [Read-Write]

<a id="unreal.UrbanBuildTemplateTextureComponent.compression_settings"></a>

#### compression\_settings

```python
@compression_settings.setter
def compression_settings(value: TextureCompressionSettings) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.max_texture_size"></a>

#### max\_texture\_size

```python
@property
def max_texture_size() -> int
```

(int32):  [Read-Only] The maximum resolution for generated textures. A value of 0 means the maximum size for the format on each platform, except HDR long/lat cubemaps, which default to a resolution of 512.

<a id="unreal.UrbanBuildTemplateTextureComponent.compression_quality"></a>

#### compression\_quality

```python
@property
def compression_quality() -> TextureCompressionQuality
```

(TextureCompressionQuality):  [Read-Write] The compression quality for generated textures.

<a id="unreal.UrbanBuildTemplateTextureComponent.compression_quality"></a>

#### compression\_quality

```python
@compression_quality.setter
def compression_quality(value: TextureCompressionQuality) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.lossy_compression_amount"></a>

#### lossy\_compression\_amount

```python
@property
def lossy_compression_amount() -> TextureLossyCompressionAmount
```

(TextureLossyCompressionAmount):  [Read-Write] How aggressively should any relevant lossy compression be applied.

<a id="unreal.UrbanBuildTemplateTextureComponent.lossy_compression_amount"></a>

#### lossy\_compression\_amount

```python
@lossy_compression_amount.setter
def lossy_compression_amount(value: TextureLossyCompressionAmount) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_brightness"></a>

#### adjust\_brightness

```python
@property
def adjust_brightness() -> float
```

(float):  [Read-Write] Static texture brightness adjustment (scales HSV value.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_brightness"></a>

#### adjust\_brightness

```python
@adjust_brightness.setter
def adjust_brightness(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_brightness_curve"></a>

#### adjust\_brightness\_curve

```python
@property
def adjust_brightness_curve() -> float
```

(float):  [Read-Write] Static texture curve adjustment (raises HSV value to the specified power.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_brightness_curve"></a>

#### adjust\_brightness\_curve

```python
@adjust_brightness_curve.setter
def adjust_brightness_curve(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_vibrance"></a>

#### adjust\_vibrance

```python
@property
def adjust_vibrance() -> float
```

(float):  [Read-Write] Static texture "vibrance" adjustment (0 - 1) (HSV saturation algorithm adjustment.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_vibrance"></a>

#### adjust\_vibrance

```python
@adjust_vibrance.setter
def adjust_vibrance(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_saturation"></a>

#### adjust\_saturation

```python
@property
def adjust_saturation() -> float
```

(float):  [Read-Write] Static texture saturation adjustment (scales HSV saturation.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_saturation"></a>

#### adjust\_saturation

```python
@adjust_saturation.setter
def adjust_saturation(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_rgb_curve"></a>

#### adjust\_rgb\_curve

```python
@property
def adjust_rgb_curve() -> float
```

(float):  [Read-Write] Static texture RGB curve adjustment (raises linear-space RGB color to the specified power.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_rgb_curve"></a>

#### adjust\_rgb\_curve

```python
@adjust_rgb_curve.setter
def adjust_rgb_curve(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_hue"></a>

#### adjust\_hue

```python
@property
def adjust_hue() -> float
```

(float):  [Read-Write] Static texture hue adjustment (0 - 360) (offsets HSV hue by value in degrees.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_hue"></a>

#### adjust\_hue

```python
@adjust_hue.setter
def adjust_hue(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_min_alpha"></a>

#### adjust\_min\_alpha

```python
@property
def adjust_min_alpha() -> float
```

(float):  [Read-Write] Remaps the alpha to the specified min/max range, defines the new value of 0 (Non-destructive; Requires texture source art to be available.)

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_min_alpha"></a>

#### adjust\_min\_alpha

```python
@adjust_min_alpha.setter
def adjust_min_alpha(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_max_alpha"></a>

#### adjust\_max\_alpha

```python
@property
def adjust_max_alpha() -> float
```

(float):  [Read-Write] Remaps the alpha to the specified min/max range, defines the new value of 1 (Non-destructive; Requires texture source art to be available.)

<a id="unreal.UrbanBuildTemplateTextureComponent.adjust_max_alpha"></a>

#### adjust\_max\_alpha

```python
@adjust_max_alpha.setter
def adjust_max_alpha(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.chroma_key_texture"></a>

#### chroma\_key\_texture

```python
@property
def chroma_key_texture() -> bool
```

(bool):  [Read-Write] Whether to chroma key the image, replacing any pixels that match ChromaKeyColor with transparent black

<a id="unreal.UrbanBuildTemplateTextureComponent.chroma_key_texture"></a>

#### chroma\_key\_texture

```python
@chroma_key_texture.setter
def chroma_key_texture(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.chroma_key_threshold"></a>

#### chroma\_key\_threshold

```python
@property
def chroma_key_threshold() -> float
```

(float):  [Read-Write] The threshold that components have to match for the texel to be considered equal to the ChromaKeyColor when chroma keying (<=, set to 0 to require a perfect exact match)

<a id="unreal.UrbanBuildTemplateTextureComponent.chroma_key_threshold"></a>

#### chroma\_key\_threshold

```python
@chroma_key_threshold.setter
def chroma_key_threshold(value: float) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.chroma_key_color"></a>

#### chroma\_key\_color

```python
@property
def chroma_key_color() -> Color
```

(Color):  [Read-Write] The color that will be replaced with transparent black if chroma keying is enabled

<a id="unreal.UrbanBuildTemplateTextureComponent.chroma_key_color"></a>

#### chroma\_key\_color

```python
@chroma_key_color.setter
def chroma_key_color(value: Color) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.mip_gen_settings"></a>

#### mip\_gen\_settings

```python
@property
def mip_gen_settings() -> TextureMipGenSettings
```

(TextureMipGenSettings):  [Read-Write] Per asset specific setting to define the mip-map generation properties like sharpening and kernel size.

<a id="unreal.UrbanBuildTemplateTextureComponent.mip_gen_settings"></a>

#### mip\_gen\_settings

```python
@mip_gen_settings.setter
def mip_gen_settings(value: TextureMipGenSettings) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.lod_bias"></a>

#### lod\_bias

```python
@property
def lod_bias() -> int
```

(int32):  [Read-Write] A bias to the index of the top mip level to use.

<a id="unreal.UrbanBuildTemplateTextureComponent.lod_bias"></a>

#### lod\_bias

```python
@lod_bias.setter
def lod_bias(value: int) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.lod_group"></a>

#### lod\_group

```python
@property
def lod_group() -> TextureGroup
```

(TextureGroup):  [Read-Write] Texture group this texture belongs to

<a id="unreal.UrbanBuildTemplateTextureComponent.lod_group"></a>

#### lod\_group

```python
@lod_group.setter
def lod_group(value: TextureGroup) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.preserve_border"></a>

#### preserve\_border

```python
@property
def preserve_border() -> bool
```

(bool):  [Read-Write] When true the texture's border will be preserved during mipmap generation.

<a id="unreal.UrbanBuildTemplateTextureComponent.preserve_border"></a>

#### preserve\_border

```python
@preserve_border.setter
def preserve_border(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.never_stream"></a>

#### never\_stream

```python
@property
def never_stream() -> bool
```

(bool):  [Read-Write]

<a id="unreal.UrbanBuildTemplateTextureComponent.never_stream"></a>

#### never\_stream

```python
@never_stream.setter
def never_stream(value: bool) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.global_force_mip_levels_to_be_resident"></a>

#### global\_force\_mip\_levels\_to\_be\_resident

```python
@property
def global_force_mip_levels_to_be_resident() -> bool
```

(bool):  [Read-Only] Global and serialized version of ForceMiplevelsToBeResident.

<a id="unreal.UrbanBuildTemplateTextureComponent.num_cinematic_mip_levels"></a>

#### num\_cinematic\_mip\_levels

```python
@property
def num_cinematic_mip_levels() -> int
```

(int32):  [Read-Write] Number of mip-levels to use for cinematic quality.

<a id="unreal.UrbanBuildTemplateTextureComponent.num_cinematic_mip_levels"></a>

#### num\_cinematic\_mip\_levels

```python
@num_cinematic_mip_levels.setter
def num_cinematic_mip_levels(value: int) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.composite_texture"></a>

#### composite\_texture

```python
@property
def composite_texture() -> Texture
```

(Texture):  [Read-Write] Can be defined to modify the roughness based on the normal map variation (mostly from mip maps).
MaxAlpha comes in handy to define a base roughness if no source alpha was there.
Make sure the normal map has at least as many mips as this texture.

<a id="unreal.UrbanBuildTemplateTextureComponent.composite_texture"></a>

#### composite\_texture

```python
@composite_texture.setter
def composite_texture(value: Texture) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.composite_texture_mode"></a>

#### composite\_texture\_mode

```python
@property
def composite_texture_mode() -> CompositeTextureMode
```

(CompositeTextureMode):  [Read-Write] defines how the CompositeTexture is applied, e.g. CTM_RoughnessFromNormalAlpha

<a id="unreal.UrbanBuildTemplateTextureComponent.composite_texture_mode"></a>

#### composite\_texture\_mode

```python
@composite_texture_mode.setter
def composite_texture_mode(value: CompositeTextureMode) -> None
```

<a id="unreal.UrbanBuildTemplateTextureComponent.composite_power"></a>

#### composite\_power

```python
@property
def composite_power() -> float
```

(float):  [Read-Write] default 1, high values result in a stronger effect e.g 1, 2, 4, 8
this is no slider because the texture update would not be fast enough

<a id="unreal.UrbanBuildTemplateTextureComponent.composite_power"></a>

#### composite\_power

```python
@composite_power.setter
def composite_power(value: float) -> None
```

<a id="unreal.UrbanEntityVariabilizationObject"></a>