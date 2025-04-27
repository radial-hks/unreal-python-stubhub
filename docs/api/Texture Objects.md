## Texture Objects

```python
class Texture(StreamableRenderAsset)
```

Texture

**C++ Source:**

- **Module**: Engine
- **File**: Texture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adjust_brightness`` (float):  [Read-Write] Static texture brightness adjustment (scales HSV value.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_brightness_curve`` (float):  [Read-Write] Static texture curve adjustment (raises HSV value to the specified power.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_hue`` (float):  [Read-Write] Static texture hue adjustment (0 - 360) (offsets HSV hue by value in degrees.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_max_alpha`` (float):  [Read-Write] Remaps the alpha to the specified min/max range, defines the new value of 1 (Non-destructive; Requires texture source art to be available.)
- ``adjust_min_alpha`` (float):  [Read-Write] Remaps the alpha to the specified min/max range, defines the new value of 0 (Non-destructive; Requires texture source art to be available.)
- ``adjust_rgb_curve`` (float):  [Read-Write] Static texture RGB curve adjustment (raises linear-space RGB color to the specified power.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_saturation`` (float):  [Read-Write] Static texture saturation adjustment (scales HSV saturation.)  (Non-destructive; Requires texture source art to be available.)
- ``adjust_vibrance`` (float):  [Read-Write] Static texture "vibrance" adjustment (0 - 1) (HSV saturation algorithm adjustment.)  (Non-destructive; Requires texture source art to be available.)
- ``alpha_coverage_thresholds`` (Vector4):  [Read-Write] Alpha values per channel to compare to when preserving alpha coverage. 0 means disable channel.  Typical good values in 0.5 - 0.9, not 1.0
- ``asset_import_data`` (AssetImportData):  [Read-Only]
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``availability`` (TextureAvailability):  [Read-Write] Whether the texture will be encoded to a gpu format and uploaded to the graphics card, or kept on the CPU for access by gamecode / blueprint.
  For CPU availability, the texture will still upload a tiny black texture as a placeholder. Only applies to 2d textures.
- ``chroma_key_color`` (Color):  [Read-Write] The color that will be replaced with transparent black if chroma keying is enabled
- ``chroma_key_texture`` (bool):  [Read-Write] Whether to chroma key the image, replacing any pixels that match ChromaKeyColor with transparent black
- ``chroma_key_threshold`` (float):  [Read-Write] The threshold that components have to match for the texel to be considered equal to the ChromaKeyColor when chroma keying (<=, set to 0 to require a perfect exact match)
- ``composite_power`` (float):  [Read-Write] default 1, high values result in a stronger effect e.g 1, 2, 4, 8
  this is not a slider because the texture update would not be fast enough
- ``composite_texture`` (Texture):  [Read-Write]
- ``composite_texture_mode`` (CompositeTextureMode):  [Read-Write] defines how the CompositeTexture is applied, e.g. CTM_RoughnessFromNormalAlpha
- ``compress_final`` (bool):  [Read-Write] If enabled, compress with Final quality during this Editor session.
- ``compression_cache_id`` (Guid):  [Read-Write] Change this optional ID to force the texture to be recompressed by changing its cache key.
- ``compression_no_alpha`` (bool):  [Read-Write] If enabled, the texture's alpha channel will be forced to opaque for any compressed texture output format.  Does not apply if output format is uncompressed RGBA.
- ``compression_quality`` (TextureCompressionQuality):  [Read-Write] The compression quality for generated ASTC textures (i.e. mobile platform textures).
- ``compression_settings`` (TextureCompressionSettings):  [Read-Write] Compression settings to use when building the texture.
- ``cook_platform_tiling_settings`` (TextureCookPlatformTilingSettings):  [Read-Write] If the platform supports it, tile the texture when cooking, or keep it linear and tile it when it's actually submitted to the GPU.
- ``defer_compression`` (bool):  [Read-Write] If enabled, defer compression of the texture until save or manually compressed in the texture editor.
- ``do_scale_mips_for_alpha_coverage`` (bool):  [Read-Write] Whether mip RGBA should be scaled to preserve the number of pixels with Value >= AlphaCoverageThresholds.  AlphaCoverageThresholds are ignored if this is off.
- ``downscale`` (PerPlatformFloat):  [Read-Write] Downscale source texture, applied only to 2d textures without mips
  < 1.0 - use scale value from texture group
  1.0 - do not scale texture
  > 1.0 - scale texure
- ``downscale_options`` (TextureDownscaleOptions):  [Read-Write] Texture downscaling options
- ``filter`` (TextureFilter):  [Read-Write] The texture filtering mode to use when sampling this texture.
- ``flip_green_channel`` (bool):  [Read-Write] When true the texture's green channel will be inverted. This is useful for some normal maps.
- ``global_force_mip_levels_to_be_resident`` (bool):  [Read-Write] Global and serialized version of ForceMiplevelsToBeResident.
- ``lod_bias`` (int32):  [Read-Write] A bias to the index of the top mip level to use.  That is, number of mip levels to drop when cooking.
- ``lod_group`` (TextureGroup):  [Read-Write] Texture group this texture belongs to
- ``lossy_compression_amount`` (TextureLossyCompressionAmount):  [Read-Write] How aggressively should any relevant lossy compression be applied. For compressors that support EncodeSpeed (i.e. Oodle), this is only
       applied if enabled (see Project Settings -> Texture Encoding). Note that this is *in addition* to any
       unavoidable loss due to the target format - selecting "No Lossy Compression" will not result in zero distortion for BCn formats.
- ``max_texture_size`` (int32):  [Read-Write] The maximum resolution for generated textures. A value of 0 means the maximum size for the format on each platform.
- ``mip_gen_settings`` (TextureMipGenSettings):  [Read-Write] Per asset specific setting to define the mip-map generation properties like sharpening and kernel size.
- ``mip_load_options`` (TextureMipLoadOptions):  [Read-Write] The texture mip load options.
- ``never_stream`` (bool):  [Read-Write]
- ``normalize_normals`` (bool):  [Read-Write] Normalize colors in Normal Maps after mip generation for better and sharper quality; recommended on if not required to match legacy behavior.
- ``num_cinematic_mip_levels`` (int32):  [Read-Write] Number of mip-levels to use for cinematic quality.
- ``oodle_preserve_extremes`` (bool):  [Read-Write] If set to true, then Oodle encoder preserves 0 and 255 (0.0 and 1.0) values exactly in alpha channel for BC3/BC7 and in all channels for BC4/BC5.
- ``oodle_texture_sdk_version`` (Name):  [Read-Write] Oodle Texture SDK Version to encode with.  Enter 'latest' to update; 'None' preserves legacy encoding to avoid patches.
- ``pad_with_border_color`` (bool):  [Read-Write] If set to true, texture padding will be performed using colors of the border pixels. This can be used to improve quality of the generated mipmaps for padded textures.
- ``padding_color`` (Color):  [Read-Write] The color used to pad the texture out if it is padded due to PowerOfTwoMode
- ``power_of_two_mode`` (TexturePowerOfTwoSetting):  [Read-Write] How to pad the texture to a power of 2 size (if necessary)
- ``preserve_border`` (bool):  [Read-Write] When true the texture's border will be preserved during mipmap generation.
- ``resize_during_build_x`` (int32):  [Read-Write] Width of the resized texture when using "Resize To Specific Resolution" padding and resizing option. If set to zero, original width will be used.
- ``resize_during_build_y`` (int32):  [Read-Write] Width of the resized texture when using "Resize To Specific Resolution" padding and resizing option. If set to zero, original height will be used.
- ``source_color_settings`` (TextureSourceColorSettings):  [Read-Write] Texture color management settings: source encoding and color space.
- ``srgb`` (bool):  [Read-Write] Whether Texture and its source are in SRGB Gamma color space.  Can only be used with 8-bit and compressed formats.  This should be unchecked if using alpha channels individually as masks.
- ``use_legacy_gamma`` (bool):  [Read-Write] A flag for using the simplified legacy gamma space e.g pow(color,1/2.2) for converting from FColor to FLinearColor, if we're doing sRGB.
- ``use_new_mip_filter`` (bool):  [Read-Write] Disable for legacy compatibility.  New and changed textures should set this to use modern improved image processing.
- ``virtual_texture_streaming`` (bool):  [Read-Write] Is this texture streamed in using VT

<a id="unreal.Texture.adjust_brightness"></a>

#### adjust_brightness

```python
@property
def adjust_brightness() -> float
```

(float):  [Read-Write] Static texture brightness adjustment (scales HSV value.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.Texture.adjust_brightness"></a>

#### adjust_brightness

```python
@adjust_brightness.setter
def adjust_brightness(value: float) -> None
```

<a id="unreal.Texture.adjust_brightness_curve"></a>

#### adjust_brightness_curve

```python
@property
def adjust_brightness_curve() -> float
```

(float):  [Read-Write] Static texture curve adjustment (raises HSV value to the specified power.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.Texture.adjust_brightness_curve"></a>

#### adjust_brightness_curve

```python
@adjust_brightness_curve.setter
def adjust_brightness_curve(value: float) -> None
```

<a id="unreal.Texture.adjust_vibrance"></a>

#### adjust_vibrance

```python
@property
def adjust_vibrance() -> float
```

(float):  [Read-Write] Static texture "vibrance" adjustment (0 - 1) (HSV saturation algorithm adjustment.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.Texture.adjust_vibrance"></a>

#### adjust_vibrance

```python
@adjust_vibrance.setter
def adjust_vibrance(value: float) -> None
```

<a id="unreal.Texture.adjust_saturation"></a>

#### adjust_saturation

```python
@property
def adjust_saturation() -> float
```

(float):  [Read-Write] Static texture saturation adjustment (scales HSV saturation.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.Texture.adjust_saturation"></a>

#### adjust_saturation

```python
@adjust_saturation.setter
def adjust_saturation(value: float) -> None
```

<a id="unreal.Texture.adjust_rgb_curve"></a>

#### adjust_rgb_curve

```python
@property
def adjust_rgb_curve() -> float
```

(float):  [Read-Write] Static texture RGB curve adjustment (raises linear-space RGB color to the specified power.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.Texture.adjust_rgb_curve"></a>

#### adjust_rgb_curve

```python
@adjust_rgb_curve.setter
def adjust_rgb_curve(value: float) -> None
```

<a id="unreal.Texture.adjust_hue"></a>

#### adjust_hue

```python
@property
def adjust_hue() -> float
```

(float):  [Read-Write] Static texture hue adjustment (0 - 360) (offsets HSV hue by value in degrees.)  (Non-destructive; Requires texture source art to be available.)

<a id="unreal.Texture.adjust_hue"></a>

#### adjust_hue

```python
@adjust_hue.setter
def adjust_hue(value: float) -> None
```

<a id="unreal.Texture.adjust_min_alpha"></a>

#### adjust_min_alpha

```python
@property
def adjust_min_alpha() -> float
```

(float):  [Read-Write] Remaps the alpha to the specified min/max range, defines the new value of 0 (Non-destructive; Requires texture source art to be available.)

<a id="unreal.Texture.adjust_min_alpha"></a>

#### adjust_min_alpha

```python
@adjust_min_alpha.setter
def adjust_min_alpha(value: float) -> None
```

<a id="unreal.Texture.adjust_max_alpha"></a>

#### adjust_max_alpha

```python
@property
def adjust_max_alpha() -> float
```

(float):  [Read-Write] Remaps the alpha to the specified min/max range, defines the new value of 1 (Non-destructive; Requires texture source art to be available.)

<a id="unreal.Texture.adjust_max_alpha"></a>

#### adjust_max_alpha

```python
@adjust_max_alpha.setter
def adjust_max_alpha(value: float) -> None
```

<a id="unreal.Texture.compression_no_alpha"></a>

#### compression_no_alpha

```python
@property
def compression_no_alpha() -> bool
```

(bool):  [Read-Write] If enabled, the texture's alpha channel will be forced to opaque for any compressed texture output format.  Does not apply if output format is uncompressed RGBA.

<a id="unreal.Texture.compression_no_alpha"></a>

#### compression_no_alpha

```python
@compression_no_alpha.setter
def compression_no_alpha(value: bool) -> None
```

<a id="unreal.Texture.compress_final"></a>

#### compress_final

```python
@property
def compress_final() -> bool
```

(bool):  [Read-Write] If enabled, compress with Final quality during this Editor session.

<a id="unreal.Texture.compress_final"></a>

#### compress_final

```python
@compress_final.setter
def compress_final(value: bool) -> None
```

<a id="unreal.Texture.defer_compression"></a>

#### defer_compression

```python
@property
def defer_compression() -> bool
```

(bool):  [Read-Write] If enabled, defer compression of the texture until save or manually compressed in the texture editor.

<a id="unreal.Texture.defer_compression"></a>

#### defer_compression

```python
@defer_compression.setter
def defer_compression(value: bool) -> None
```

<a id="unreal.Texture.lossy_compression_amount"></a>

#### lossy_compression_amount

```python
@property
def lossy_compression_amount() -> TextureLossyCompressionAmount
```

(TextureLossyCompressionAmount):  [Read-Write] How aggressively should any relevant lossy compression be applied. For compressors that support EncodeSpeed (i.e. Oodle), this is only
     applied if enabled (see Project Settings -> Texture Encoding). Note that this is *in addition* to any
     unavoidable loss due to the target format - selecting "No Lossy Compression" will not result in zero distortion for BCn formats.

<a id="unreal.Texture.lossy_compression_amount"></a>

#### lossy_compression_amount

```python
@lossy_compression_amount.setter
def lossy_compression_amount(value: TextureLossyCompressionAmount) -> None
```

<a id="unreal.Texture.oodle_texture_sdk_version"></a>

#### oodle_texture_sdk_version

```python
@property
def oodle_texture_sdk_version() -> Name
```

(Name):  [Read-Write] Oodle Texture SDK Version to encode with.  Enter 'latest' to update; 'None' preserves legacy encoding to avoid patches.

<a id="unreal.Texture.oodle_texture_sdk_version"></a>

#### oodle_texture_sdk_version

```python
@oodle_texture_sdk_version.setter
def oodle_texture_sdk_version(value: Name) -> None
```

<a id="unreal.Texture.max_texture_size"></a>

#### max_texture_size

```python
@property
def max_texture_size() -> int
```

(int32):  [Read-Write] The maximum resolution for generated textures. A value of 0 means the maximum size for the format on each platform.

<a id="unreal.Texture.max_texture_size"></a>

#### max_texture_size

```python
@max_texture_size.setter
def max_texture_size(value: int) -> None
```

<a id="unreal.Texture.compression_quality"></a>

#### compression_quality

```python
@property
def compression_quality() -> TextureCompressionQuality
```

(TextureCompressionQuality):  [Read-Write] The compression quality for generated ASTC textures (i.e. mobile platform textures).

<a id="unreal.Texture.compression_quality"></a>

#### compression_quality

```python
@compression_quality.setter
def compression_quality(value: TextureCompressionQuality) -> None
```

<a id="unreal.Texture.do_scale_mips_for_alpha_coverage"></a>

#### do_scale_mips_for_alpha_coverage

```python
@property
def do_scale_mips_for_alpha_coverage() -> bool
```

(bool):  [Read-Write] Whether mip RGBA should be scaled to preserve the number of pixels with Value >= AlphaCoverageThresholds.  AlphaCoverageThresholds are ignored if this is off.

<a id="unreal.Texture.do_scale_mips_for_alpha_coverage"></a>

#### do_scale_mips_for_alpha_coverage

```python
@do_scale_mips_for_alpha_coverage.setter
def do_scale_mips_for_alpha_coverage(value: bool) -> None
```

<a id="unreal.Texture.alpha_coverage_thresholds"></a>

#### alpha_coverage_thresholds

```python
@property
def alpha_coverage_thresholds() -> Vector4
```

(Vector4):  [Read-Write] Alpha values per channel to compare to when preserving alpha coverage. 0 means disable channel.  Typical good values in 0.5 - 0.9, not 1.0

<a id="unreal.Texture.alpha_coverage_thresholds"></a>

#### alpha_coverage_thresholds

```python
@alpha_coverage_thresholds.setter
def alpha_coverage_thresholds(value: Vector4) -> None
```

<a id="unreal.Texture.use_new_mip_filter"></a>

#### use_new_mip_filter

```python
@property
def use_new_mip_filter() -> bool
```

(bool):  [Read-Write] Disable for legacy compatibility.  New and changed textures should set this to use modern improved image processing.

<a id="unreal.Texture.use_new_mip_filter"></a>

#### use_new_mip_filter

```python
@use_new_mip_filter.setter
def use_new_mip_filter(value: bool) -> None
```

<a id="unreal.Texture.preserve_border"></a>

#### preserve_border

```python
@property
def preserve_border() -> bool
```

(bool):  [Read-Write] When true the texture's border will be preserved during mipmap generation.

<a id="unreal.Texture.preserve_border"></a>

#### preserve_border

```python
@preserve_border.setter
def preserve_border(value: bool) -> None
```

<a id="unreal.Texture.flip_green_channel"></a>

#### flip_green_channel

```python
@property
def flip_green_channel() -> bool
```

(bool):  [Read-Write] When true the texture's green channel will be inverted. This is useful for some normal maps.

<a id="unreal.Texture.flip_green_channel"></a>

#### flip_green_channel

```python
@flip_green_channel.setter
def flip_green_channel(value: bool) -> None
```

<a id="unreal.Texture.power_of_two_mode"></a>

#### power_of_two_mode

```python
@property
def power_of_two_mode() -> TexturePowerOfTwoSetting
```

(TexturePowerOfTwoSetting):  [Read-Write] How to pad the texture to a power of 2 size (if necessary)

<a id="unreal.Texture.power_of_two_mode"></a>

#### power_of_two_mode

```python
@power_of_two_mode.setter
def power_of_two_mode(value: TexturePowerOfTwoSetting) -> None
```

<a id="unreal.Texture.padding_color"></a>

#### padding_color

```python
@property
def padding_color() -> Color
```

(Color):  [Read-Write] The color used to pad the texture out if it is padded due to PowerOfTwoMode

<a id="unreal.Texture.padding_color"></a>

#### padding_color

```python
@padding_color.setter
def padding_color(value: Color) -> None
```

<a id="unreal.Texture.pad_with_border_color"></a>

#### pad_with_border_color

```python
@property
def pad_with_border_color() -> bool
```

(bool):  [Read-Write] If set to true, texture padding will be performed using colors of the border pixels. This can be used to improve quality of the generated mipmaps for padded textures.

<a id="unreal.Texture.pad_with_border_color"></a>

#### pad_with_border_color

```python
@pad_with_border_color.setter
def pad_with_border_color(value: bool) -> None
```

<a id="unreal.Texture.resize_during_build_x"></a>

#### resize_during_build_x

```python
@property
def resize_during_build_x() -> int
```

(int32):  [Read-Write] Width of the resized texture when using "Resize To Specific Resolution" padding and resizing option. If set to zero, original width will be used.

<a id="unreal.Texture.resize_during_build_x"></a>

#### resize_during_build_x

```python
@resize_during_build_x.setter
def resize_during_build_x(value: int) -> None
```

<a id="unreal.Texture.resize_during_build_y"></a>

#### resize_during_build_y

```python
@property
def resize_during_build_y() -> int
```

(int32):  [Read-Write] Width of the resized texture when using "Resize To Specific Resolution" padding and resizing option. If set to zero, original height will be used.

<a id="unreal.Texture.resize_during_build_y"></a>

#### resize_during_build_y

```python
@resize_during_build_y.setter
def resize_during_build_y(value: int) -> None
```

<a id="unreal.Texture.chroma_key_texture"></a>

#### chroma_key_texture

```python
@property
def chroma_key_texture() -> bool
```

(bool):  [Read-Write] Whether to chroma key the image, replacing any pixels that match ChromaKeyColor with transparent black

<a id="unreal.Texture.chroma_key_texture"></a>

#### chroma_key_texture

```python
@chroma_key_texture.setter
def chroma_key_texture(value: bool) -> None
```

<a id="unreal.Texture.chroma_key_threshold"></a>

#### chroma_key_threshold

```python
@property
def chroma_key_threshold() -> float
```

(float):  [Read-Write] The threshold that components have to match for the texel to be considered equal to the ChromaKeyColor when chroma keying (<=, set to 0 to require a perfect exact match)

<a id="unreal.Texture.chroma_key_threshold"></a>

#### chroma_key_threshold

```python
@chroma_key_threshold.setter
def chroma_key_threshold(value: float) -> None
```

<a id="unreal.Texture.chroma_key_color"></a>

#### chroma_key_color

```python
@property
def chroma_key_color() -> Color
```

(Color):  [Read-Write] The color that will be replaced with transparent black if chroma keying is enabled

<a id="unreal.Texture.chroma_key_color"></a>

#### chroma_key_color

```python
@chroma_key_color.setter
def chroma_key_color(value: Color) -> None
```

<a id="unreal.Texture.mip_gen_settings"></a>

#### mip_gen_settings

```python
@property
def mip_gen_settings() -> TextureMipGenSettings
```

(TextureMipGenSettings):  [Read-Write] Per asset specific setting to define the mip-map generation properties like sharpening and kernel size.

<a id="unreal.Texture.mip_gen_settings"></a>

#### mip_gen_settings

```python
@mip_gen_settings.setter
def mip_gen_settings(value: TextureMipGenSettings) -> None
```

<a id="unreal.Texture.composite_texture"></a>

#### composite_texture

```python
@property
def composite_texture() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.Texture.composite_texture"></a>

#### composite_texture

```python
@composite_texture.setter
def composite_texture(value: Texture) -> None
```

<a id="unreal.Texture.composite_texture_mode"></a>

#### composite_texture_mode

```python
@property
def composite_texture_mode() -> CompositeTextureMode
```

(CompositeTextureMode):  [Read-Write] defines how the CompositeTexture is applied, e.g. CTM_RoughnessFromNormalAlpha

<a id="unreal.Texture.composite_texture_mode"></a>

#### composite_texture_mode

```python
@composite_texture_mode.setter
def composite_texture_mode(value: CompositeTextureMode) -> None
```

<a id="unreal.Texture.composite_power"></a>

#### composite_power

```python
@property
def composite_power() -> float
```

(float):  [Read-Write] default 1, high values result in a stronger effect e.g 1, 2, 4, 8
this is not a slider because the texture update would not be fast enough

<a id="unreal.Texture.composite_power"></a>

#### composite_power

```python
@composite_power.setter
def composite_power(value: float) -> None
```

<a id="unreal.Texture.lod_bias"></a>

#### lod_bias

```python
@property
def lod_bias() -> int
```

(int32):  [Read-Write] A bias to the index of the top mip level to use.  That is, number of mip levels to drop when cooking.

<a id="unreal.Texture.lod_bias"></a>

#### lod_bias

```python
@lod_bias.setter
def lod_bias(value: int) -> None
```

<a id="unreal.Texture.compression_settings"></a>

#### compression_settings

```python
@property
def compression_settings() -> TextureCompressionSettings
```

(TextureCompressionSettings):  [Read-Write] Compression settings to use when building the texture.

<a id="unreal.Texture.compression_settings"></a>

#### compression_settings

```python
@compression_settings.setter
def compression_settings(value: TextureCompressionSettings) -> None
```

<a id="unreal.Texture.filter"></a>

#### filter

```python
@property
def filter() -> TextureFilter
```

(TextureFilter):  [Read-Write] The texture filtering mode to use when sampling this texture.

<a id="unreal.Texture.filter"></a>

#### filter

```python
@filter.setter
def filter(value: TextureFilter) -> None
```

<a id="unreal.Texture.mip_load_options"></a>

#### mip_load_options

```python
@property
def mip_load_options() -> TextureMipLoadOptions
```

(TextureMipLoadOptions):  [Read-Write] The texture mip load options.

<a id="unreal.Texture.mip_load_options"></a>

#### mip_load_options

```python
@mip_load_options.setter
def mip_load_options(value: TextureMipLoadOptions) -> None
```

<a id="unreal.Texture.cook_platform_tiling_settings"></a>

#### cook_platform_tiling_settings

```python
@property
def cook_platform_tiling_settings() -> TextureCookPlatformTilingSettings
```

(TextureCookPlatformTilingSettings):  [Read-Write] If the platform supports it, tile the texture when cooking, or keep it linear and tile it when it's actually submitted to the GPU.

<a id="unreal.Texture.cook_platform_tiling_settings"></a>

#### cook_platform_tiling_settings

```python
@cook_platform_tiling_settings.setter
def cook_platform_tiling_settings(
        value: TextureCookPlatformTilingSettings) -> None
```

<a id="unreal.Texture.oodle_preserve_extremes"></a>

#### oodle_preserve_extremes

```python
@property
def oodle_preserve_extremes() -> bool
```

(bool):  [Read-Write] If set to true, then Oodle encoder preserves 0 and 255 (0.0 and 1.0) values exactly in alpha channel for BC3/BC7 and in all channels for BC4/BC5.

<a id="unreal.Texture.oodle_preserve_extremes"></a>

#### oodle_preserve_extremes

```python
@oodle_preserve_extremes.setter
def oodle_preserve_extremes(value: bool) -> None
```

<a id="unreal.Texture.lod_group"></a>

#### lod_group

```python
@property
def lod_group() -> TextureGroup
```

(TextureGroup):  [Read-Write] Texture group this texture belongs to

<a id="unreal.Texture.lod_group"></a>

#### lod_group

```python
@lod_group.setter
def lod_group(value: TextureGroup) -> None
```

<a id="unreal.Texture.availability"></a>

#### availability

```python
@property
def availability() -> TextureAvailability
```

(TextureAvailability):  [Read-Write] Whether the texture will be encoded to a gpu format and uploaded to the graphics card, or kept on the CPU for access by gamecode / blueprint.
For CPU availability, the texture will still upload a tiny black texture as a placeholder. Only applies to 2d textures.

<a id="unreal.Texture.availability"></a>

#### availability

```python
@availability.setter
def availability(value: TextureAvailability) -> None
```

<a id="unreal.Texture.srgb"></a>

#### srgb

```python
@property
def srgb() -> bool
```

(bool):  [Read-Write] Whether Texture and its source are in SRGB Gamma color space.  Can only be used with 8-bit and compressed formats.  This should be unchecked if using alpha channels individually as masks.

<a id="unreal.Texture.srgb"></a>

#### srgb

```python
@srgb.setter
def srgb(value: bool) -> None
```

<a id="unreal.Texture.normalize_normals"></a>

#### normalize_normals

```python
@property
def normalize_normals() -> bool
```

(bool):  [Read-Write] Normalize colors in Normal Maps after mip generation for better and sharper quality; recommended on if not required to match legacy behavior.

<a id="unreal.Texture.normalize_normals"></a>

#### normalize_normals

```python
@normalize_normals.setter
def normalize_normals(value: bool) -> None
```

<a id="unreal.Texture.use_legacy_gamma"></a>

#### use_legacy_gamma

```python
@property
def use_legacy_gamma() -> bool
```

(bool):  [Read-Write] A flag for using the simplified legacy gamma space e.g pow(color,1/2.2) for converting from FColor to FLinearColor, if we're doing sRGB.

<a id="unreal.Texture.use_legacy_gamma"></a>

#### use_legacy_gamma

```python
@use_legacy_gamma.setter
def use_legacy_gamma(value: bool) -> None
```

<a id="unreal.Texture.source_color_settings"></a>

#### source_color_settings

```python
@property
def source_color_settings() -> TextureSourceColorSettings
```

(TextureSourceColorSettings):  [Read-Write] Texture color management settings: source encoding and color space.

<a id="unreal.Texture.source_color_settings"></a>

#### source_color_settings

```python
@source_color_settings.setter
def source_color_settings(value: TextureSourceColorSettings) -> None
```

<a id="unreal.Texture.virtual_texture_streaming"></a>

#### virtual_texture_streaming

```python
@property
def virtual_texture_streaming() -> bool
```

(bool):  [Read-Only] Is this texture streamed in using VT

<a id="unreal.Texture.compute_texture_source_channel_min_max"></a>

#### compute_texture_source_channel_min_max

```python
def compute_texture_source_channel_min_max(
) -> Optional[Tuple[LinearColor, LinearColor]]
```

x.compute_texture_source_channel_min_max() -> (out_color_min=LinearColor, out_color_max=LinearColor) or None
Scan the texture source pixels to compute the min & max values of the RGBA channels.
Uses texture source, not available in runtime games.
Causes texture source data to be loaded, is computed by scanning pixels when called.
Will set Min=Max=zero and return false on failure

Returns:
    tuple or None: 

    out_color_min (LinearColor): 

    out_color_max (LinearColor):

<a id="unreal.Texture.blueprint_get_texture_source_id_string"></a>

#### blueprint_get_texture_source_id_string

```python
def blueprint_get_texture_source_id_string() -> Optional[str]
```

x.blueprint_get_texture_source_id_string() -> str or None
Return the ID for the texture source.
If the source isn't valid or editor data isn't available, returns false.

Returns:
    str or None: 

    out_texture_source_id (str):

<a id="unreal.Texture.blueprint_get_texture_source_disk_and_memory_size"></a>

#### blueprint_get_texture_source_disk_and_memory_size

```python
def blueprint_get_texture_source_disk_and_memory_size() -> Tuple[int, int]
```

x.blueprint_get_texture_source_disk_and_memory_size() -> (out_disk_size=int64, out_memory_size=int64)
Gets the memory size of the texture source top mip, in bytes, and the size on disk of the asset, which may be compressed.
Uses texture source, not available in runtime games.
Does not cause texture source to be loaded, queries cached values.
Returns zero for error.

Returns:
    tuple: 

    out_disk_size (int64): 

    out_memory_size (int64):

<a id="unreal.Texture.blueprint_get_memory_size"></a>

#### blueprint_get_memory_size

```python
def blueprint_get_memory_size() -> int
```

x.blueprint_get_memory_size() -> int64
Gets the memory size of the texture, in bytes.
This is the size in GPU memory of the built platformdata, accounting for LODBias, etc.
Returns zero for error.

Returns:
    int64:

<a id="unreal.Texture.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.Texture.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.Texture.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.Texture.export_to_disk"></a>

#### export_to_disk

```python
def export_to_disk(filename: str, options: ImageWriteOptions) -> None
```

x.export_to_disk(filename, options) -> None
Export the specified texture to disk

Args:
    filename (str): The filename on disk to save as
    options (ImageWriteOptions): Parameters defining the various export options

<a id="unreal.MediaTexture"></a>