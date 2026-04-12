## InterchangeTextureFactoryNode Objects

```python
class InterchangeTextureFactoryNode(InterchangeFactoryBaseNode)
```

Interchange Texture Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeTextureFactoryNode.h

<a id="unreal.InterchangeTextureFactoryNode.set_custom_virtual_texture_streaming"></a>

#### set\_custom\_virtual\_texture\_streaming

```python
def set_custom_virtual_texture_streaming(attribute_value: bool,
                                         add_apply_delegate: bool = True
                                         ) -> bool
```

x.set_custom_virtual_texture_streaming(attribute_value, add_apply_delegate=True) -> bool
Set Custom Virtual Texture Streaming

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_translated_texture_node_uid"></a>

#### set\_custom\_translated\_texture\_node\_uid

```python
def set_custom_translated_texture_node_uid(attribute_value: str) -> bool
```

x.set_custom_translated_texture_node_uid(attribute_value) -> bool
Set the unique ID of the translated texture node. This is a reference to the node that was created by the translator. It is needed to get the texture payload.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_srgb"></a>

#### set\_custom\_srgb

```python
def set_custom_srgb(attribute_value: bool,
                    add_apply_delegate: bool = True) -> bool
```

x.set_custom_srgb(attribute_value, add_apply_delegate=True) -> bool
Set Custom SRGB

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_prefer_compressed_source_data"></a>

#### set\_custom\_prefer\_compressed\_source\_data

```python
def set_custom_prefer_compressed_source_data(attribute_value: bool) -> bool
```

x.set_custom_prefer_compressed_source_data(attribute_value) -> bool
* Determines whether the factory should tell the translator to provide a compressed source data payload when available.
* This will generally result in smaller assets. However, some operations like the texture build might be slower, because the source data first needs to be decompressed.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_power_of_two_mode"></a>

#### set\_custom\_power\_of\_two\_mode

```python
def set_custom_power_of_two_mode(attribute_value: int,
                                 add_apply_delegate: bool = True) -> bool
```

x.set_custom_power_of_two_mode(attribute_value, add_apply_delegate=True) -> bool
Set Custom Power Of Two Mode

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_padding_color"></a>

#### set\_custom\_padding\_color

```python
def set_custom_padding_color(attribute_value: Color,
                             add_apply_delegate: bool = True) -> bool
```

x.set_custom_padding_color(attribute_value, add_apply_delegate=True) -> bool
Set Custom Padding Color

Args:
    attribute_value (Color): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_mip_load_options"></a>

#### set\_custom\_mip\_load\_options

```python
def set_custom_mip_load_options(attribute_value: int,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_mip_load_options(attribute_value, add_apply_delegate=True) -> bool
Set Custom Mip Load Options

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_mip_gen_settings"></a>

#### set\_custom\_mip\_gen\_settings

```python
def set_custom_mip_gen_settings(attribute_value: int,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_mip_gen_settings(attribute_value, add_apply_delegate=True) -> bool
Set Custom Mip Gen Settings

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_max_texture_size"></a>

#### set\_custom\_max\_texture\_size

```python
def set_custom_max_texture_size(attribute_value: int,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_max_texture_size(attribute_value, add_apply_delegate=True) -> bool
Set Custom Max Texture Size

Args:
    attribute_value (int32): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_lossy_compression_amount"></a>

#### set\_custom\_lossy\_compression\_amount

```python
def set_custom_lossy_compression_amount(attribute_value: int,
                                        add_apply_delegate: bool = True
                                        ) -> bool
```

x.set_custom_lossy_compression_amount(attribute_value, add_apply_delegate=True) -> bool
Set Custom Lossy Compression Amount

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_lod_group"></a>

#### set\_custom\_lod\_group

```python
def set_custom_lod_group(attribute_value: int,
                         add_apply_delegate: bool = True) -> bool
```

x.set_custom_lod_group(attribute_value, add_apply_delegate=True) -> bool
Set Custom LODGroup

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_lod_bias"></a>

#### set\_custom\_lod\_bias

```python
def set_custom_lod_bias(attribute_value: int,
                        add_apply_delegate: bool = True) -> bool
```

x.set_custom_lod_bias(attribute_value, add_apply_delegate=True) -> bool
Set Custom LODBias

Args:
    attribute_value (int32): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_filter"></a>

#### set\_custom\_filter

```python
def set_custom_filter(attribute_value: int,
                      add_apply_delegate: bool = True) -> bool
```

x.set_custom_filter(attribute_value, add_apply_delegate=True) -> bool
Set Custom Filter

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_downscale_options"></a>

#### set\_custom\_downscale\_options

```python
def set_custom_downscale_options(attribute_value: int,
                                 add_apply_delegate: bool = True) -> bool
```

x.set_custom_downscale_options(attribute_value, add_apply_delegate=True) -> bool
Set Custom Downscale Options

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_downscale"></a>

#### set\_custom\_downscale

```python
def set_custom_downscale(attribute_value: float,
                         add_apply_delegate: bool = True) -> bool
```

x.set_custom_downscale(attribute_value, add_apply_delegate=True) -> bool
Set Custom Downscale

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_defer_compression"></a>

#### set\_custom\_defer\_compression

```python
def set_custom_defer_compression(attribute_value: bool,
                                 add_apply_delegate: bool = True) -> bool
```

x.set_custom_defer_compression(attribute_value, add_apply_delegate=True) -> bool
Set Custom Defer Compression

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_compression_settings"></a>

#### set\_custom\_compression\_settings

```python
def set_custom_compression_settings(attribute_value: int,
                                    add_apply_delegate: bool = True) -> bool
```

x.set_custom_compression_settings(attribute_value, add_apply_delegate=True) -> bool
Set Custom Compression Settings

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_compression_quality"></a>

#### set\_custom\_compression\_quality

```python
def set_custom_compression_quality(attribute_value: int,
                                   add_apply_delegate: bool = True) -> bool
```

x.set_custom_compression_quality(attribute_value, add_apply_delegate=True) -> bool
Set Custom Compression Quality

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_compression_no_alpha"></a>

#### set\_custom\_compression\_no\_alpha

```python
def set_custom_compression_no_alpha(attribute_value: bool,
                                    add_apply_delegate: bool = True) -> bool
```

x.set_custom_compression_no_alpha(attribute_value, add_apply_delegate=True) -> bool
Set Custom Compression No Alpha

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_composite_texture_mode"></a>

#### set\_custom\_composite\_texture\_mode

```python
def set_custom_composite_texture_mode(attribute_value: int,
                                      add_apply_delegate: bool = True) -> bool
```

x.set_custom_composite_texture_mode(attribute_value, add_apply_delegate=True) -> bool
Set Custom Composite Texture Mode

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_composite_power"></a>

#### set\_custom\_composite\_power

```python
def set_custom_composite_power(attribute_value: float,
                               add_apply_delegate: bool = True) -> bool
```

x.set_custom_composite_power(attribute_value, add_apply_delegate=True) -> bool
Set Custom Composite Power

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_color_space"></a>

#### set\_custom\_color\_space

```python
def set_custom_color_space(attribute_value: TextureColorSpace,
                           add_apply_delegate: bool = True) -> bool
```

x.set_custom_color_space(attribute_value, add_apply_delegate=True) -> bool
Set Custom Color Space

Args:
    attribute_value (TextureColorSpace): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_chroma_key_threshold"></a>

#### set\_custom\_chroma\_key\_threshold

```python
def set_custom_chroma_key_threshold(attribute_value: float,
                                    add_apply_delegate: bool = True) -> bool
```

x.set_custom_chroma_key_threshold(attribute_value, add_apply_delegate=True) -> bool
Set Custom Chroma Key Threshold

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_chroma_key_color"></a>

#### set\_custom\_chroma\_key\_color

```python
def set_custom_chroma_key_color(attribute_value: Color,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_chroma_key_color(attribute_value, add_apply_delegate=True) -> bool
Set Custom Chroma Key Color

Args:
    attribute_value (Color): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_customb_use_legacy_gamma"></a>

#### set\_customb\_use\_legacy\_gamma

```python
def set_customb_use_legacy_gamma(attribute_value: bool,
                                 add_apply_delegate: bool = True) -> bool
```

x.set_customb_use_legacy_gamma(attribute_value, add_apply_delegate=True) -> bool
Set Customb Use Legacy Gamma

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_customb_preserve_border"></a>

#### set\_customb\_preserve\_border

```python
def set_customb_preserve_border(attribute_value: bool,
                                add_apply_delegate: bool = True) -> bool
```

x.set_customb_preserve_border(attribute_value, add_apply_delegate=True) -> bool
Set Customb Preserve Border

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_customb_flip_green_channel"></a>

#### set\_customb\_flip\_green\_channel

```python
def set_customb_flip_green_channel(attribute_value: bool,
                                   add_apply_delegate: bool = True) -> bool
```

x.set_customb_flip_green_channel(attribute_value, add_apply_delegate=True) -> bool
Set Customb Flip Green Channel

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_customb_do_scale_mips_for_alpha_coverage"></a>

#### set\_customb\_do\_scale\_mips\_for\_alpha\_coverage

```python
def set_customb_do_scale_mips_for_alpha_coverage(
        attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

x.set_customb_do_scale_mips_for_alpha_coverage(attribute_value, add_apply_delegate=True) -> bool
Set Customb Do Scale Mips for Alpha Coverage

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_customb_chroma_key_texture"></a>

#### set\_customb\_chroma\_key\_texture

```python
def set_customb_chroma_key_texture(attribute_value: bool,
                                   add_apply_delegate: bool = True) -> bool
```

x.set_customb_chroma_key_texture(attribute_value, add_apply_delegate=True) -> bool
Set Customb Chroma Key Texture

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_alpha_coverage_thresholds"></a>

#### set\_custom\_alpha\_coverage\_thresholds

```python
def set_custom_alpha_coverage_thresholds(attribute_value: Vector4,
                                         add_apply_delegate: bool = True
                                         ) -> bool
```

x.set_custom_alpha_coverage_thresholds(attribute_value, add_apply_delegate=True) -> bool
Set Custom Alpha Coverage Thresholds

Args:
    attribute_value (Vector4): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_allow_non_power_of_two"></a>

#### set\_custom\_allow\_non\_power\_of\_two

```python
def set_custom_allow_non_power_of_two(attribute_value: bool) -> bool
```

x.set_custom_allow_non_power_of_two(attribute_value) -> bool
* Should the factory allow the import of texture that would have a resolution that is not a power of two
* By default this is not allowed

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_adjust_vibrance"></a>

#### set\_custom\_adjust\_vibrance

```python
def set_custom_adjust_vibrance(attribute_value: float,
                               add_apply_delegate: bool = True) -> bool
```

x.set_custom_adjust_vibrance(attribute_value, add_apply_delegate=True) -> bool
Set Custom Adjust Vibrance

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_adjust_saturation"></a>

#### set\_custom\_adjust\_saturation

```python
def set_custom_adjust_saturation(attribute_value: float,
                                 add_apply_delegate: bool = True) -> bool
```

x.set_custom_adjust_saturation(attribute_value, add_apply_delegate=True) -> bool
Set Custom Adjust Saturation

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_adjust_rgb_curve"></a>

#### set\_custom\_adjust\_rgb\_curve

```python
def set_custom_adjust_rgb_curve(attribute_value: float,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_adjust_rgb_curve(attribute_value, add_apply_delegate=True) -> bool
Set Custom Adjust RGBCurve

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_adjust_min_alpha"></a>

#### set\_custom\_adjust\_min\_alpha

```python
def set_custom_adjust_min_alpha(attribute_value: float,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_adjust_min_alpha(attribute_value, add_apply_delegate=True) -> bool
Set Custom Adjust Min Alpha

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_adjust_max_alpha"></a>

#### set\_custom\_adjust\_max\_alpha

```python
def set_custom_adjust_max_alpha(attribute_value: float,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_adjust_max_alpha(attribute_value, add_apply_delegate=True) -> bool
Set Custom Adjust Max Alpha

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_adjust_hue"></a>

#### set\_custom\_adjust\_hue

```python
def set_custom_adjust_hue(attribute_value: float,
                          add_apply_delegate: bool = True) -> bool
```

x.set_custom_adjust_hue(attribute_value, add_apply_delegate=True) -> bool
Set Custom Adjust Hue

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_adjust_brightness_curve"></a>

#### set\_custom\_adjust\_brightness\_curve

```python
def set_custom_adjust_brightness_curve(attribute_value: float,
                                       add_apply_delegate: bool = True
                                       ) -> bool
```

x.set_custom_adjust_brightness_curve(attribute_value, add_apply_delegate=True) -> bool
Set Custom Adjust Brightness Curve

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.set_custom_adjust_brightness"></a>

#### set\_custom\_adjust\_brightness

```python
def set_custom_adjust_brightness(attribute_value: float,
                                 add_apply_delegate: bool = True) -> bool
```

x.set_custom_adjust_brightness(attribute_value, add_apply_delegate=True) -> bool
Set Custom Adjust Brightness

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTextureFactoryNode.initialize_texture_node"></a>

#### initialize\_texture\_node

```python
def initialize_texture_node(unique_id: str, display_label: str,
                            asset_name: str) -> None
```

x.initialize_texture_node(unique_id, display_label, asset_name) -> None
Initialize node data.
param:: UniqueID - The unique ID for this node.

Args:
    unique_id (str): 
    display_label (str): The name of the node.
    asset_name (str):

<a id="unreal.InterchangeTextureFactoryNode.get_object_class"></a>

#### get\_object\_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get the class this node creates.

Returns:
    type(Class):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_virtual_texture_streaming"></a>

#### get\_custom\_virtual\_texture\_streaming

```python
def get_custom_virtual_texture_streaming() -> Optional[bool]
```

x.get_custom_virtual_texture_streaming() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_translated_texture_node_uid"></a>

#### get\_custom\_translated\_texture\_node\_uid

```python
def get_custom_translated_texture_node_uid() -> Optional[str]
```

x.get_custom_translated_texture_node_uid() -> str or None
Get the unique ID of the translated texture node.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_srgb"></a>

#### get\_custom\_srgb

```python
def get_custom_srgb() -> Optional[bool]
```

x.get_custom_srgb() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_prefer_compressed_source_data"></a>

#### get\_custom\_prefer\_compressed\_source\_data

```python
def get_custom_prefer_compressed_source_data() -> Optional[bool]
```

x.get_custom_prefer_compressed_source_data() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_power_of_two_mode"></a>

#### get\_custom\_power\_of\_two\_mode

```python
def get_custom_power_of_two_mode() -> Optional[int]
```

x.get_custom_power_of_two_mode() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_padding_color"></a>

#### get\_custom\_padding\_color

```python
def get_custom_padding_color() -> Optional[Color]
```

x.get_custom_padding_color() -> Color or None
Return false if the Attribute was not set previously.

Returns:
    Color or None: 

    attribute_value (Color):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_mip_load_options"></a>

#### get\_custom\_mip\_load\_options

```python
def get_custom_mip_load_options() -> Optional[int]
```

x.get_custom_mip_load_options() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_mip_gen_settings"></a>

#### get\_custom\_mip\_gen\_settings

```python
def get_custom_mip_gen_settings() -> Optional[int]
```

x.get_custom_mip_gen_settings() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_max_texture_size"></a>

#### get\_custom\_max\_texture\_size

```python
def get_custom_max_texture_size() -> Optional[int]
```

x.get_custom_max_texture_size() -> int32 or None
Return false if the Attribute was not set previously.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_lossy_compression_amount"></a>

#### get\_custom\_lossy\_compression\_amount

```python
def get_custom_lossy_compression_amount() -> Optional[int]
```

x.get_custom_lossy_compression_amount() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_lod_group"></a>

#### get\_custom\_lod\_group

```python
def get_custom_lod_group() -> Optional[int]
```

x.get_custom_lod_group() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_lod_bias"></a>

#### get\_custom\_lod\_bias

```python
def get_custom_lod_bias() -> Optional[int]
```

x.get_custom_lod_bias() -> int32 or None
Return false if the Attribute was not set previously.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_filter"></a>

#### get\_custom\_filter

```python
def get_custom_filter() -> Optional[int]
```

x.get_custom_filter() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_downscale_options"></a>

#### get\_custom\_downscale\_options

```python
def get_custom_downscale_options() -> Optional[int]
```

x.get_custom_downscale_options() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_downscale"></a>

#### get\_custom\_downscale

```python
def get_custom_downscale() -> Optional[float]
```

x.get_custom_downscale() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_defer_compression"></a>

#### get\_custom\_defer\_compression

```python
def get_custom_defer_compression() -> Optional[bool]
```

x.get_custom_defer_compression() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_compression_settings"></a>

#### get\_custom\_compression\_settings

```python
def get_custom_compression_settings() -> Optional[int]
```

x.get_custom_compression_settings() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_compression_quality"></a>

#### get\_custom\_compression\_quality

```python
def get_custom_compression_quality() -> Optional[int]
```

x.get_custom_compression_quality() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_compression_no_alpha"></a>

#### get\_custom\_compression\_no\_alpha

```python
def get_custom_compression_no_alpha() -> Optional[bool]
```

x.get_custom_compression_no_alpha() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_composite_texture_mode"></a>

#### get\_custom\_composite\_texture\_mode

```python
def get_custom_composite_texture_mode() -> Optional[int]
```

x.get_custom_composite_texture_mode() -> uint8 or None
Return false if the Attribute was not set previously.

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_composite_power"></a>

#### get\_custom\_composite\_power

```python
def get_custom_composite_power() -> Optional[float]
```

x.get_custom_composite_power() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_color_space"></a>

#### get\_custom\_color\_space

```python
def get_custom_color_space() -> Optional[TextureColorSpace]
```

x.get_custom_color_space() -> TextureColorSpace or None
Return false if the Attribute was not set previously.

Returns:
    TextureColorSpace or None: 

    attribute_value (TextureColorSpace):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_chroma_key_threshold"></a>

#### get\_custom\_chroma\_key\_threshold

```python
def get_custom_chroma_key_threshold() -> Optional[float]
```

x.get_custom_chroma_key_threshold() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_chroma_key_color"></a>

#### get\_custom\_chroma\_key\_color

```python
def get_custom_chroma_key_color() -> Optional[Color]
```

x.get_custom_chroma_key_color() -> Color or None
Return false if the Attribute was not set previously.

Returns:
    Color or None: 

    attribute_value (Color):

<a id="unreal.InterchangeTextureFactoryNode.get_customb_use_legacy_gamma"></a>

#### get\_customb\_use\_legacy\_gamma

```python
def get_customb_use_legacy_gamma() -> Optional[bool]
```

x.get_customb_use_legacy_gamma() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_customb_preserve_border"></a>

#### get\_customb\_preserve\_border

```python
def get_customb_preserve_border() -> Optional[bool]
```

x.get_customb_preserve_border() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_customb_flip_green_channel"></a>

#### get\_customb\_flip\_green\_channel

```python
def get_customb_flip_green_channel() -> Optional[bool]
```

x.get_customb_flip_green_channel() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_customb_do_scale_mips_for_alpha_coverage"></a>

#### get\_customb\_do\_scale\_mips\_for\_alpha\_coverage

```python
def get_customb_do_scale_mips_for_alpha_coverage() -> Optional[bool]
```

x.get_customb_do_scale_mips_for_alpha_coverage() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_customb_chroma_key_texture"></a>

#### get\_customb\_chroma\_key\_texture

```python
def get_customb_chroma_key_texture() -> Optional[bool]
```

x.get_customb_chroma_key_texture() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_alpha_coverage_thresholds"></a>

#### get\_custom\_alpha\_coverage\_thresholds

```python
def get_custom_alpha_coverage_thresholds() -> Optional[Vector4]
```

x.get_custom_alpha_coverage_thresholds() -> Vector4 or None
Return false if the Attribute was not set previously.

Returns:
    Vector4 or None: 

    attribute_value (Vector4):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_allow_non_power_of_two"></a>

#### get\_custom\_allow\_non\_power\_of\_two

```python
def get_custom_allow_non_power_of_two() -> Optional[bool]
```

x.get_custom_allow_non_power_of_two() -> bool or None
Return false if the Attribute was not set previously.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_adjust_vibrance"></a>

#### get\_custom\_adjust\_vibrance

```python
def get_custom_adjust_vibrance() -> Optional[float]
```

x.get_custom_adjust_vibrance() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_adjust_saturation"></a>

#### get\_custom\_adjust\_saturation

```python
def get_custom_adjust_saturation() -> Optional[float]
```

x.get_custom_adjust_saturation() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_adjust_rgb_curve"></a>

#### get\_custom\_adjust\_rgb\_curve

```python
def get_custom_adjust_rgb_curve() -> Optional[float]
```

x.get_custom_adjust_rgb_curve() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_adjust_min_alpha"></a>

#### get\_custom\_adjust\_min\_alpha

```python
def get_custom_adjust_min_alpha() -> Optional[float]
```

x.get_custom_adjust_min_alpha() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_adjust_max_alpha"></a>

#### get\_custom\_adjust\_max\_alpha

```python
def get_custom_adjust_max_alpha() -> Optional[float]
```

x.get_custom_adjust_max_alpha() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_adjust_hue"></a>

#### get\_custom\_adjust\_hue

```python
def get_custom_adjust_hue() -> Optional[float]
```

x.get_custom_adjust_hue() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_adjust_brightness_curve"></a>

#### get\_custom\_adjust\_brightness\_curve

```python
def get_custom_adjust_brightness_curve() -> Optional[float]
```

x.get_custom_adjust_brightness_curve() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTextureFactoryNode.get_custom_adjust_brightness"></a>

#### get\_custom\_adjust\_brightness

```python
def get_custom_adjust_brightness() -> Optional[float]
```

x.get_custom_adjust_brightness() -> float or None
Return false if the Attribute was not set previously.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeTexture2DArrayFactoryNode"></a>