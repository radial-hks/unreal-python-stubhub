## PythonTextureLib Objects

```python
class PythonTextureLib(BlueprintFunctionLibrary)
```

Python Texture Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonTextureLib.h

<a id="unreal.PythonTextureLib.set_texture_render_target2d_array_format"></a>

#### set\_texture\_render\_target2d\_array\_format

```python
@classmethod
def set_texture_render_target2d_array_format(
        cls, texture_array: TextureRenderTarget2DArray,
        format: PixelFormat) -> bool
```

X.set_texture_render_target2d_array_format(texture_array, format) -> bool
Set Texture Render Target 2DArray Format

Args:
    texture_array (TextureRenderTarget2DArray): 
    format (PixelFormat): 

Returns:
    bool:

<a id="unreal.PythonTextureLib.set_texture_array_render_target2d"></a>

#### set\_texture\_array\_render\_target2d

```python
@classmethod
def set_texture_array_render_target2d(
        cls, render_target: TextureRenderTarget2DArray, slice: int) -> bool
```

X.set_texture_array_render_target2d(render_target, slice) -> bool
UFUNCTION(BlueprintCallable, meta = (Keywords = "Python Editor"), Category = "PythonEditor")
static bool SetTextureRenderTarget2DArraFromMemory(UTextureRenderTarget2DArray* TextureArray, const TArray<int64>& EachLayerAddresses, const int64& Length, int32 Width, int32 Height, int32 ChannelNum, bool bBGR);

Args:
    render_target (TextureRenderTarget2DArray): 
    slice (int32): 

Returns:
    bool:

<a id="unreal.PythonTextureLib.set_texture2d_array_slice"></a>

#### set\_texture2d\_array\_slice

```python
@classmethod
def set_texture2d_array_slice(cls, texture_array: Texture2DArray,
                              slice_index: int, texture: Texture2D) -> bool
```

X.set_texture2d_array_slice(texture_array, slice_index, texture) -> bool
Set Texture 2DArray Slice

Args:
    texture_array (Texture2DArray): 
    slice_index (int32): 
    texture (Texture2D): 

Returns:
    bool:

<a id="unreal.PythonTextureLib.set_texture2d_array_rhi_slices"></a>

#### set\_texture2d\_array\_rhi\_slices

```python
@classmethod
def set_texture2d_array_rhi_slices(cls,
                                   texture2d_array: Texture2DArray,
                                   each_layer_addresses: Array[int],
                                   length: int,
                                   bgr: bool = False) -> bool
```

X.set_texture2d_array_rhi_slices(texture2d_array, each_layer_addresses, length, bgr=False) -> bool
Set Texture 2DArray RHISlices

Args:
    texture2d_array (Texture2DArray): 
    each_layer_addresses (Array[int64]): 
    length (int64): 
    bgr (bool): 

Returns:
    bool:

<a id="unreal.PythonTextureLib.set_texture2d_array_rhi_slice"></a>

#### set\_texture2d\_array\_rhi\_slice

```python
@classmethod
def set_texture2d_array_rhi_slice(cls,
                                  texture2d_array: Texture2DArray,
                                  slice_index: int,
                                  address: int,
                                  length: int,
                                  bgr: bool = False) -> bool
```

X.set_texture2d_array_rhi_slice(texture2d_array, slice_index, address, length, bgr=False) -> bool
Set Texture 2DArray RHISlice

Args:
    texture2d_array (Texture2DArray): 
    slice_index (int32): 
    address (int64): 
    length (int64): 
    bgr (bool): 

Returns:
    bool:

<a id="unreal.PythonTextureLib.set_texture2d_array_data_from_memory"></a>

#### set\_texture2d\_array\_data\_from\_memory

```python
@classmethod
def set_texture2d_array_data_from_memory(cls,
                                         texture_array: Texture2DArray,
                                         each_layer_addresses: Array[int],
                                         length: int,
                                         width: int,
                                         height: int,
                                         channel_num: int = 4,
                                         bgr: bool = True) -> bool
```

X.set_texture2d_array_data_from_memory(texture_array, each_layer_addresses, length, width, height, channel_num=4, bgr=True) -> bool
Set Texture 2DArray Data from Memory

Args:
    texture_array (Texture2DArray): 
    each_layer_addresses (Array[int64]): 
    length (int64): 
    width (int32): 
    height (int32): 
    channel_num (int32): 
    bgr (bool): 

Returns:
    bool:

<a id="unreal.PythonTextureLib.set_texture2d_array_data_at"></a>

#### set\_texture2d\_array\_data\_at

```python
@classmethod
def set_texture2d_array_data_at(cls,
                                texture_array: Texture2DArray,
                                slice_index: int,
                                pos_x: int,
                                pos_y: int,
                                address: int,
                                length: int,
                                width: int,
                                height: int,
                                bgr: bool = True) -> bool
```

X.set_texture2d_array_data_at(texture_array, slice_index, pos_x, pos_y, address, length, width, height, bgr=True) -> bool
Set Texture 2DArray Data At

Args:
    texture_array (Texture2DArray): 
    slice_index (int32): 
    pos_x (int32): 
    pos_y (int32): 
    address (int64): 
    length (int64): 
    width (int32): 
    height (int32): 
    bgr (bool): 

Returns:
    bool:

<a id="unreal.PythonTextureLib.set_render_target_data"></a>

#### set\_render\_target\_data

```python
@classmethod
def set_render_target_data(cls,
                           render_target_texture: TextureRenderTarget2D,
                           raw_data: Array[int],
                           raw_data_width: int,
                           raw_data_height: int,
                           raw_data_channel_num: int,
                           use_srgb: bool = False,
                           texture_filter_value: int = -1,
                           bgr: bool = False,
                           flip_y: bool = False) -> None
```

X.set_render_target_data(render_target_texture, raw_data, raw_data_width, raw_data_height, raw_data_channel_num, use_srgb=False, texture_filter_value=-1, bgr=False, flip_y=False) -> None
Set the RenderTexture2D By Raw Data.
note: The order of RawData is row first. Lower left corner is the first pixel, and upper right is the last
note: added in v1.0.7

Args:
    render_target_texture (TextureRenderTarget2D): The target RenderTarget2D
    raw_data (Array[uint8]): The flatten uint8 raw data of image, len(RawData) == RawDataWidth * RawDataHeight * RawDataChannelNum
    raw_data_width (int32): The width of the RawData, we can fill the rt with smaller RawData
    raw_data_height (int32): The Height of the RawData
    raw_data_channel_num (int32): The Number of RawData's Channel. 1: grayscale; 2: grayscale with alpha; 3: rgb; 4 rgb with alpha
    use_srgb (bool): Use SRGB or not
    texture_filter_value (int32): The filter of texture: 0: Nearest, 1: Bilinear, 2: Trilinear, Use setting from the Texture Group.
    bgr (bool): Is the order of RawData is Blue, Green, Red, otherwise RGB
    flip_y (bool):

<a id="unreal.PythonTextureLib.set_image_data_from_memory"></a>

#### set\_image\_data\_from\_memory

```python
@classmethod
def set_image_data_from_memory(cls,
                               texture_array: Texture2DArray,
                               slice_index: int,
                               address: int,
                               length: int,
                               width: int,
                               height: int,
                               channel_num: int = 4,
                               bgr: bool = True) -> bool
```

X.set_image_data_from_memory(texture_array, slice_index, address, length, width, height, channel_num=4, bgr=True) -> bool
Set Image Data from Memory

Args:
    texture_array (Texture2DArray): 
    slice_index (int32): 
    address (int64): 
    length (int64): 
    width (int32): 
    height (int32): 
    channel_num (int32): 
    bgr (bool): 

Returns:
    bool:

<a id="unreal.PythonTextureLib.png_compress_image_array"></a>

#### png\_compress\_image\_array

```python
@classmethod
def png_compress_image_array(cls, image_width: int, image_height: int,
                             src_data: Array[Color]) -> Array[int]
```

X.png_compress_image_array(image_width, image_height, src_data) -> Array[uint8]
PNGCompressImageArray

Args:
    image_width (int32): 
    image_height (int32): 
    src_data (Array[Color]): 

Returns:
    Array[uint8]: 

    dst_data (Array[uint8]):

<a id="unreal.PythonTextureLib.get_texture2d_content"></a>

#### get\_texture2d\_content

```python
@classmethod
def get_texture2d_content(cls, texture: Texture2D,
                          mip_level: int) -> Optional[Array[int]]
```

X.get_texture2d_content(texture, mip_level) -> Array[uint8] or None
Get the Raw Data from Texture2D
note: added in v1.2.1

Args:
    texture (Texture2D): The source Texture2D
    mip_level (int32): The mip level of the Texture2D

Returns:
    Array[uint8] or None: The raw data of the Texture2D, pixel order is BGRA

    dst_data (Array[uint8]):

<a id="unreal.PythonTextureLib.get_texture2d_array_content"></a>

#### get\_texture2d\_array\_content

```python
@classmethod
def get_texture2d_array_content(cls, texture_array: Texture2DArray,
                                index: int) -> Optional[Array[int]]
```

X.get_texture2d_array_content(texture_array, index) -> Array[uint8] or None
Get Texture 2DArray Content

Args:
    texture_array (Texture2DArray): 
    index (int32): 

Returns:
    Array[uint8] or None: 

    dst_data (Array[uint8]):

<a id="unreal.PythonTextureLib.get_textexture2d_array_size"></a>

#### get\_textexture2d\_array\_size

```python
@classmethod
def get_textexture2d_array_size(cls,
                                texture_array: Texture2DArray) -> Array[int]
```

X.get_textexture2d_array_size(texture_array) -> Array[int32]
Get Textexture 2DArray Size

Args:
    texture_array (Texture2DArray): 

Returns:
    Array[int32]:

<a id="unreal.PythonTextureLib.get_render_target_raw_data"></a>

#### get\_render\_target\_raw\_data

```python
@classmethod
def get_render_target_raw_data(
        cls, render_target_texture: TextureRenderTarget2D) -> Array[int]
```

X.get_render_target_raw_data(render_target_texture) -> Array[uint8]
Get the Raw Data from RenderTarget2D
note: added in v1.0.7

Args:
    render_target_texture (TextureRenderTarget2D): The source RenderTarget2D

Returns:
    Array[uint8]: 

    out_raw_data (Array[uint8]):

<a id="unreal.PythonTextureLib.get_pixel_at_texture2d_array"></a>

#### get\_pixel\_at\_texture2d\_array

```python
@classmethod
def get_pixel_at_texture2d_array(cls, texture_array: Texture2DArray,
                                 slice_index: int, x: int,
                                 y: int) -> Optional[Array[int]]
```

X.get_pixel_at_texture2d_array(texture_array, slice_index, x, y) -> Array[int32] or None
Get Pixel at Texture 2DArray

Args:
    texture_array (Texture2DArray): 
    slice_index (int32): 
    x (int32): 
    y (int32): 

Returns:
    Array[int32] or None: 

    out_data (Array[int32]):

<a id="unreal.PythonTextureLib.finish_compilation_texture"></a>

#### finish\_compilation\_texture

```python
@classmethod
def finish_compilation_texture(cls, texture: Texture2D) -> Texture2D
```

X.finish_compilation_texture(texture) -> Texture2D
Blocks until completion of the requested textures
note: added in v1.2.0
note: need UE5

Args:
    texture (Texture2D): 

Returns:
    Texture2D: Texture2D

<a id="unreal.PythonTextureLib.create_texture2d_from_raw"></a>

#### create\_texture2d\_from\_raw

```python
@classmethod
def create_texture2d_from_raw(cls,
                              raw_data: Array[int],
                              width: int,
                              height: int,
                              channel_num: int,
                              use_srgb: bool = False,
                              texture_filter_value: int = -1,
                              bgr: bool = False,
                              flip_y: bool = False) -> Texture2D
```

X.create_texture2d_from_raw(raw_data, width, height, channel_num, use_srgb=False, texture_filter_value=-1, bgr=False, flip_y=False) -> Texture2D
Create a Texture2D from pixel RawData
note: The Texture2D type is EPixelFormat::PF_R8G8B8A8
note: added in v1.0.7

Args:
    raw_data (Array[uint8]): The flatten uint8 raw data of image, len(RawData) == RawDataWidth * RawDataHeight * RawDataChannelNum
    width (int32): The width of the Texture2D
    height (int32): The Height of the Texture2D
    channel_num (int32): The Number of RawData's Channel. 1: grayscale; 2: grayscale with alpha; 3: rgb; 4 rgb with alpha
    use_srgb (bool): Use SRGB or no0t
    texture_filter_value (int32): The filter of texture: 0: Nearest, 1: Bilinear, 2: Trilinear, 3: Use setting from the Texture Group.
    bgr (bool): Is the order of RawData is Blue, Green, Red, otherwise RGB
    flip_y (bool): 

Returns:
    Texture2D: The created Texture2D

<a id="unreal.PythonTextureLib.create_texture2d"></a>

#### create\_texture2d

```python
@classmethod
def create_texture2d(cls,
                     width: int,
                     height: int,
                     use_srgb: bool = False,
                     texture_filter_value: int = -1,
                     texture_source_format: int = 2) -> Texture2D
```

X.create_texture2d(width, height, use_srgb=False, texture_filter_value=-1, texture_source_format=2) -> Texture2D
Create a Texture2D with specified size
note: The Texture2D type is EPixelFormat::PF_B8G8R8A8
note: added in v1.2.0

Args:
    width (int32): The width of the Texture2D
    height (int32): The Height of the Texture2D
    use_srgb (bool): Use SRGB or not
    texture_filter_value (int32): The filter of texture: 0: Nearest, 1: Bilinear, 2: Trilinear, 3: Use setting from the Texture Group.
    texture_source_format (int32): TextureFormat: 0: Invalid, 1: G8, 2: BGRA8, 3: BGRE8, 4: RGBA16, 5 RGBA16F, 8: G16, 9: RGBA32F, 10: R16F, 11 R32F

Returns:
    Texture2D: The created Texture2D

<a id="unreal.PythonTextureLib.compress_image_array"></a>

#### compress\_image\_array

```python
@classmethod
def compress_image_array(cls, image_width: int, image_height: int,
                         src_data: Array[Color]) -> Array[int]
```

X.compress_image_array(image_width, image_height, src_data) -> Array[uint8]
CompressImageArray

Args:
    image_width (int32): 
    image_height (int32): 
    src_data (Array[Color]): 

Returns:
    Array[uint8]: 

    dst_data (Array[uint8]):

<a id="unreal.LandscapeLayerInfoObjectFactory"></a>