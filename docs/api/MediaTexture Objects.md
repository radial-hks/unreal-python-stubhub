## MediaTexture Objects

```python
class MediaTexture(Texture)
```

Implements a texture asset for rendering video tracks from UMediaPlayer assets.

note: derives directly from UTexture, not from UTexture2D or UTexture2DDynamic
   maybe should have been UTexture2DDynamic?

**C++ Source:**

- **Module**: MediaAssets
- **File**: MediaTexture.h

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
- ``alpha_coverage_thresholds`` (Vector4):  [Read-Write] Alpha values per channel to compare to when preserving alpha coverage. 0 means disable channel.  Typical good values in 0.5 - 0.9, not 1.0
- ``asset_import_data`` (AssetImportData):  [Read-Only]
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``auto_clear`` (bool):  [Read-Write] Whether to clear the texture when no media is being played (default = enabled).
- ``availability`` (TextureAvailability):  [Read-Write] Whether the texture will be encoded to a gpu format and uploaded to the graphics card, or kept on the CPU for access by gamecode / blueprint.
  For CPU availability, the texture will still upload a tiny black texture as a placeholder. Only applies to 2d textures.
- ``chroma_key_color`` (Color):  [Read-Write] The color that will be replaced with transparent black if chroma keying is enabled
- ``chroma_key_texture`` (bool):  [Read-Write] Whether to chroma key the image, replacing any pixels that match ChromaKeyColor with transparent black
- ``chroma_key_threshold`` (float):  [Read-Write] The threshold that components have to match for the texel to be considered equal to the ChromaKeyColor when chroma keying (<=, set to 0 to require a perfect exact match)
- ``clear_color`` (LinearColor):  [Read-Write] The color used to clear the texture if AutoClear is enabled (default = black).
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
- ``current_aspect_ratio`` (float):  [Read-Write] Current aspect ratio
- ``current_orientation`` (MediaTextureOrientation):  [Read-Write] Current media orientation
- ``defer_compression`` (bool):  [Read-Write] If enabled, defer compression of the texture until save or manually compressed in the texture editor.
- ``do_scale_mips_for_alpha_coverage`` (bool):  [Read-Write] Whether mip RGBA should be scaled to preserve the number of pixels with Value >= AlphaCoverageThresholds.  AlphaCoverageThresholds are ignored if this is off.
- ``downscale`` (PerPlatformFloat):  [Read-Write] Downscale source texture, applied only to 2d textures without mips
  < 1.0 - use scale value from texture group
  1.0 - do not scale texture
  > 1.0 - scale texure
- ``downscale_options`` (TextureDownscaleOptions):  [Read-Write] Texture downscaling options
- ``enable_gen_mips`` (bool):  [Read-Write] Basic enablement for mip generation (default = false).
- ``filter`` (TextureFilter):  [Read-Write] The texture filtering mode to use when sampling this texture.
- ``flip_green_channel`` (bool):  [Read-Write] When true the texture's green channel will be inverted. This is useful for some normal maps.
- ``global_force_mip_levels_to_be_resident`` (bool):  [Read-Write] Global and serialized version of ForceMiplevelsToBeResident.
- ``lod_bias`` (int32):  [Read-Write] A bias to the index of the top mip level to use.  That is, number of mip levels to drop when cooking.
- ``lod_group`` (TextureGroup):  [Read-Write] Texture group this texture belongs to
- ``lossy_compression_amount`` (TextureLossyCompressionAmount):  [Read-Write] How aggressively should any relevant lossy compression be applied. For compressors that support EncodeSpeed (i.e. Oodle), this is only
       applied if enabled (see Project Settings -> Texture Encoding). Note that this is *in addition* to any
       unavoidable loss due to the target format - selecting "No Lossy Compression" will not result in zero distortion for BCn formats.
- ``max_texture_size`` (int32):  [Read-Write] The maximum resolution for generated textures. A value of 0 means the maximum size for the format on each platform.
- ``media_player`` (MediaPlayer):  [Read-Write] The media player asset associated with this texture.

  This property is meant for design-time convenience. To change the
  associated media player at run-time, use the SetMediaPlayer method.
  see: SetMediaPlayer
- ``mip_gen_settings`` (TextureMipGenSettings):  [Read-Write] Per asset specific setting to define the mip-map generation properties like sharpening and kernel size.
- ``mip_load_options`` (TextureMipLoadOptions):  [Read-Write] The texture mip load options.
- ``never_stream`` (bool):  [Read-Write]
- ``new_style_output`` (bool):  [Read-Write] Enable new style output.
- ``normalize_normals`` (bool):  [Read-Write] Normalize colors in Normal Maps after mip generation for better and sharper quality; recommended on if not required to match legacy behavior.
- ``num_cinematic_mip_levels`` (int32):  [Read-Write] Number of mip-levels to use for cinematic quality.
- ``num_mips`` (uint8):  [Read-Write] The number of mips to use (default = 1).
- ``oodle_preserve_extremes`` (bool):  [Read-Write] If set to true, then Oodle encoder preserves 0 and 255 (0.0 and 1.0) values exactly in alpha channel for BC3/BC7 and in all channels for BC4/BC5.
- ``oodle_texture_sdk_version`` (Name):  [Read-Write] Oodle Texture SDK Version to encode with.  Enter 'latest' to update; 'None' preserves legacy encoding to avoid patches.
- ``output_format`` (MediaTextureOutputFormat):  [Read-Write] DEPRECATED 5.4
  deprecated: Output format was unused (not connected to active logic) and is now deprecated. References to it can be safely deleted.
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

<a id="unreal.MediaTexture.address_x"></a>

#### address_x

```python
@property
def address_x() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the X axis.

<a id="unreal.MediaTexture.address_x"></a>

#### address_x

```python
@address_x.setter
def address_x(value: TextureAddress) -> None
```

<a id="unreal.MediaTexture.address_y"></a>

#### address_y

```python
@property
def address_y() -> TextureAddress
```

(TextureAddress):  [Read-Write] The addressing mode to use for the Y axis.

<a id="unreal.MediaTexture.address_y"></a>

#### address_y

```python
@address_y.setter
def address_y(value: TextureAddress) -> None
```

<a id="unreal.MediaTexture.auto_clear"></a>

#### auto_clear

```python
@property
def auto_clear() -> bool
```

(bool):  [Read-Write] Whether to clear the texture when no media is being played (default = enabled).

<a id="unreal.MediaTexture.auto_clear"></a>

#### auto_clear

```python
@auto_clear.setter
def auto_clear(value: bool) -> None
```

<a id="unreal.MediaTexture.clear_color"></a>

#### clear_color

```python
@property
def clear_color() -> LinearColor
```

(LinearColor):  [Read-Write] The color used to clear the texture if AutoClear is enabled (default = black).

<a id="unreal.MediaTexture.clear_color"></a>

#### clear_color

```python
@clear_color.setter
def clear_color(value: LinearColor) -> None
```

<a id="unreal.MediaTexture.enable_gen_mips"></a>

#### enable_gen_mips

```python
@property
def enable_gen_mips() -> bool
```

(bool):  [Read-Only] Basic enablement for mip generation (default = false).

<a id="unreal.MediaTexture.num_mips"></a>

#### num_mips

```python
@property
def num_mips() -> int
```

(uint8):  [Read-Write] The number of mips to use (default = 1).

<a id="unreal.MediaTexture.num_mips"></a>

#### num_mips

```python
@num_mips.setter
def num_mips(value: int) -> None
```

<a id="unreal.MediaTexture.new_style_output"></a>

#### new_style_output

```python
@property
def new_style_output() -> bool
```

(bool):  [Read-Write] Enable new style output.

<a id="unreal.MediaTexture.new_style_output"></a>

#### new_style_output

```python
@new_style_output.setter
def new_style_output(value: bool) -> None
```

<a id="unreal.MediaTexture.output_format"></a>

#### output_format

```python
@property
def output_format() -> MediaTextureOutputFormat
```

(MediaTextureOutputFormat):  [Read-Write] DEPRECATED 5.4
deprecated: Output format was unused (not connected to active logic) and is now deprecated. References to it can be safely deleted.

<a id="unreal.MediaTexture.output_format"></a>

#### output_format

```python
@output_format.setter
def output_format(value: MediaTextureOutputFormat) -> None
```

<a id="unreal.MediaTexture.current_aspect_ratio"></a>

#### current_aspect_ratio

```python
@property
def current_aspect_ratio() -> float
```

(float):  [Read-Only] Current aspect ratio

<a id="unreal.MediaTexture.current_orientation"></a>

#### current_orientation

```python
@property
def current_orientation() -> MediaTextureOrientation
```

(MediaTextureOrientation):  [Read-Only] Current media orientation

<a id="unreal.MediaTexture.update_resource"></a>

#### update_resource

```python
def update_resource() -> None
```

x.update_resource() -> None
Creates a new resource for the texture, and updates any cached references to the resource.
This obviously is just an override to expose to blueprints.

<a id="unreal.MediaTexture.set_media_player"></a>

#### set_media_player

```python
def set_media_player(new_media_player: MediaPlayer) -> None
```

x.set_media_player(new_media_player) -> None
Set the media player that provides the video samples.
see: GetMediaPlayer

Args:
    new_media_player (MediaPlayer): The player to set.

<a id="unreal.MediaTexture.get_width"></a>

#### get_width

```python
def get_width() -> int
```

x.get_width() -> int32
Gets the current width of the texture.
see: GetAspectRatio, GetHeight

Returns:
    int32: Texture width (in pixels).

<a id="unreal.MediaTexture.get_texture_num_mips"></a>

#### get_texture_num_mips

```python
def get_texture_num_mips() -> int
```

x.get_texture_num_mips() -> int32
Gets the current numbe of mips of the texture.

Returns:
    int32: Number of mips.

<a id="unreal.MediaTexture.get_media_player"></a>

#### get_media_player

```python
def get_media_player() -> MediaPlayer
```

x.get_media_player() -> MediaPlayer
Get the media player that provides the video samples.
see: SetMediaPlayer

Returns:
    MediaPlayer: The texture's media player, or nullptr if not set.

<a id="unreal.MediaTexture.get_height"></a>

#### get_height

```python
def get_height() -> int
```

x.get_height() -> int32
Gets the current height of the texture.
see: GetAspectRatio, GetWidth

Returns:
    int32: Texture height (in pixels).

<a id="unreal.MediaTexture.get_aspect_ratio"></a>

#### get_aspect_ratio

```python
def get_aspect_ratio() -> float
```

x.get_aspect_ratio() -> float
Gets the current aspect ratio of the texture.
see: GetHeight, GetWidth

Returns:
    float: Texture aspect ratio.

<a id="unreal.MediaSource"></a>