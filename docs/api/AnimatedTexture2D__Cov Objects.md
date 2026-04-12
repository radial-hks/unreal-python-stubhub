## AnimatedTexture2D\_Cov Objects

```python
class AnimatedTexture2D_Cov(Texture2DDynamic)
```

Animated Texture 2D Cov

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: AnimatedTexture2D_Cov.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``address_x`` (TextureAddress):  [Read-Write]
- ``address_y`` (TextureAddress):  [Read-Write]
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
- ``default_frame_delay`` (float):  [Read-Write]
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
- ``looping`` (bool):  [Read-Write]
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
- ``play_rate`` (float):  [Read-Write] used while Frame.Delay==0
- ``power_of_two_mode`` (TexturePowerOfTwoSetting):  [Read-Write] How to pad the texture to a power of 2 size (if necessary)
- ``preserve_border`` (bool):  [Read-Write] When true the texture's border will be preserved during mipmap generation.
- ``resize_during_build_x`` (int32):  [Read-Write] Width of the resized texture when using "Resize To Specific Resolution" padding and resizing option. If set to zero, original width will be used.
- ``resize_during_build_y`` (int32):  [Read-Write] Width of the resized texture when using "Resize To Specific Resolution" padding and resizing option. If set to zero, original height will be used.
- ``source_color_settings`` (TextureSourceColorSettings):  [Read-Write] Texture color management settings: source encoding and color space.
- ``srgb`` (bool):  [Read-Write] Whether Texture and its source are in SRGB Gamma color space.  Can only be used with 8-bit and compressed formats.  This should be unchecked if using alpha channels individually as masks.
- ``supports_transparency`` (bool):  [Read-Write]
- ``use_legacy_gamma`` (bool):  [Read-Write] A flag for using the simplified legacy gamma space e.g pow(color,1/2.2) for converting from FColor to FLinearColor, if we're doing sRGB.
- ``use_new_mip_filter`` (bool):  [Read-Write] Disable for legacy compatibility.  New and changed textures should set this to use modern improved image processing.
- ``virtual_texture_streaming`` (bool):  [Read-Write] Is this texture streamed in using VT

<a id="unreal.AnimatedTexture2D_Cov.address_x"></a>

#### address\_x

```python
@property
def address_x() -> TextureAddress
```

(TextureAddress):  [Read-Write]

<a id="unreal.AnimatedTexture2D_Cov.address_x"></a>

#### address\_x

```python
@address_x.setter
def address_x(value: TextureAddress) -> None
```

<a id="unreal.AnimatedTexture2D_Cov.address_y"></a>

#### address\_y

```python
@property
def address_y() -> TextureAddress
```

(TextureAddress):  [Read-Write]

<a id="unreal.AnimatedTexture2D_Cov.address_y"></a>

#### address\_y

```python
@address_y.setter
def address_y(value: TextureAddress) -> None
```

<a id="unreal.AnimatedTexture2D_Cov.supports_transparency"></a>

#### supports\_transparency

```python
@property
def supports_transparency() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimatedTexture2D_Cov.supports_transparency"></a>

#### supports\_transparency

```python
@supports_transparency.setter
def supports_transparency(value: bool) -> None
```

<a id="unreal.AnimatedTexture2D_Cov.default_frame_delay"></a>

#### default\_frame\_delay

```python
@property
def default_frame_delay() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimatedTexture2D_Cov.default_frame_delay"></a>

#### default\_frame\_delay

```python
@default_frame_delay.setter
def default_frame_delay(value: float) -> None
```

<a id="unreal.AnimatedTexture2D_Cov.play_rate"></a>

#### play\_rate

```python
@property
def play_rate() -> float
```

(float):  [Read-Write] used while Frame.Delay==0

<a id="unreal.AnimatedTexture2D_Cov.play_rate"></a>

#### play\_rate

```python
@play_rate.setter
def play_rate(value: float) -> None
```

<a id="unreal.AnimatedTexture2D_Cov.looping"></a>

#### looping

```python
@property
def looping() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimatedTexture2D_Cov.looping"></a>

#### looping

```python
@looping.setter
def looping(value: bool) -> None
```

<a id="unreal.AnimatedTexture2D_Cov.stop"></a>

#### stop

```python
def stop() -> None
```

x.stop() -> None
Stop

<a id="unreal.AnimatedTexture2D_Cov.set_play_rate"></a>

#### set\_play\_rate

```python
def set_play_rate(new_rate: float) -> None
```

x.set_play_rate(new_rate) -> None
Set Play Rate

Args:
    new_rate (float):

<a id="unreal.AnimatedTexture2D_Cov.set_looping"></a>

#### set\_looping

```python
def set_looping(new_looping: bool) -> None
```

x.set_looping(new_looping) -> None
Set Looping

Args:
    new_looping (bool):

<a id="unreal.AnimatedTexture2D_Cov.play_from_start"></a>

#### play\_from\_start

```python
def play_from_start() -> None
```

x.play_from_start() -> None
Play from Start

<a id="unreal.AnimatedTexture2D_Cov.play"></a>

#### play

```python
def play() -> None
```

x.play() -> None
Play

<a id="unreal.AnimatedTexture2D_Cov.is_playing"></a>

#### is\_playing

```python
def is_playing() -> bool
```

x.is_playing() -> bool
Is Playing

Returns:
    bool:

<a id="unreal.AnimatedTexture2D_Cov.is_looping"></a>

#### is\_looping

```python
def is_looping() -> bool
```

x.is_looping() -> bool
Is Looping

Returns:
    bool:

<a id="unreal.AnimatedTexture2D_Cov.get_play_rate"></a>

#### get\_play\_rate

```python
def get_play_rate() -> float
```

x.get_play_rate() -> float
Get Play Rate

Returns:
    float:

<a id="unreal.AnimatedTexture2D_Cov.get_animation_length"></a>

#### get\_animation\_length

```python
def get_animation_length() -> float
```

x.get_animation_length() -> float
Get Animation Length

Returns:
    float:

<a id="unreal.AsyncTaskDownloadImage_51"></a>