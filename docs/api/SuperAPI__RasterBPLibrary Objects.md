## SuperAPI\_RasterBPLibrary Objects

```python
class SuperAPI_RasterBPLibrary(BlueprintFunctionLibrary)
```

*      Function library class.
*      Each function in it is expected to be static and represents blueprint node that can be called in any blueprint.
*
*      When declaring function you can define metadata for the node. Key function specifiers will be BlueprintPure and BlueprintCallable.
*      BlueprintPure - means the function does not affect the owning object in any way and thus creates a node without Exec pins.
*      BlueprintCallable - makes a function which can be executed in Blueprints - Thus it has Exec pins.
*      DisplayName - full name of the node, shown when you mouse over the node and in the blueprint drop down menu.
*                              Its lets you name the node using characters not allowed in C++ function names.
*      CompactNodeTitle - the word(s) that appear on the node.
*      Keywords -      the list of keywords that helps you to find node when you search for it using Blueprint drop-down menu.
*                              Good example is "Print String" node which you can find also by using keyword "log".
*      Category -      the category your node will be under in the Blueprint drop-down menu.
*
*      For more info on custom blueprint nodes visit documentation:
*      https://wiki.unrealengine.com/Custom_Blueprint_Node_Creation

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: SuperAPI_Raster
- **File**: SuperAPI_RasterBPLibrary.h

<a id="unreal.SuperAPI_RasterBPLibrary.unload_data_set"></a>

#### unload\_data\_set

```python
@classmethod
def unload_data_set(cls, dataset_holder: GDALDatasetHolder) -> None
```

X.unload_data_set(dataset_holder) -> None
Unload Data Set

Args:
    dataset_holder (GDALDatasetHolder):

<a id="unreal.SuperAPI_RasterBPLibrary.tif_data_trans"></a>

#### tif\_data\_trans

```python
@classmethod
def tif_data_trans(
        cls, dataset_holder: GDALDatasetHolder,
        texture_result: TextureRenderTarget2D
) -> Tuple[TextureBound, str, bool]
```

X.tif_data_trans(dataset_holder, texture_result) -> (data_bound=TextureBound, sr_sproj=str, success=bool)
Tif Data Trans

Args:
    dataset_holder (GDALDatasetHolder): 
    texture_result (TextureRenderTarget2D): 

Returns:
    tuple: 

    data_bound (TextureBound): 

    sr_sproj (str): 

    success (bool):

<a id="unreal.SuperAPI_RasterBPLibrary.super_api_raster_sample_function"></a>

#### super\_api\_raster\_sample\_function

```python
@classmethod
def super_api_raster_sample_function(cls, param: float) -> float
```

X.super_api_raster_sample_function(param) -> float
Super API Raster Sample Function

Args:
    param (float): 

Returns:
    float:

<a id="unreal.SuperAPI_RasterBPLibrary.set_gdal_num_threads"></a>

#### set\_gdal\_num\_threads

```python
@classmethod
def set_gdal_num_threads(cls, num_threads: int) -> None
```

X.set_gdal_num_threads(num_threads) -> None
Set GDALNum Threads

Args:
    num_threads (int32):

<a id="unreal.SuperAPI_RasterBPLibrary.resize_rt"></a>

#### resize\_rt

```python
@classmethod
def resize_rt(cls, texture_result: TextureRenderTarget2D, with_: int,
              height: int) -> None
```

X.resize_rt(texture_result, with_, height) -> None
Resize RT

Args:
    texture_result (TextureRenderTarget2D): 
    with_ (int32): 
    height (int32):

<a id="unreal.SuperAPI_RasterBPLibrary.load_tif_to_data_set"></a>

#### load\_tif\_to\_data\_set

```python
@classmethod
def load_tif_to_data_set(
        cls, tif_file_path: str) -> Tuple[GDALDatasetHolder, int, int]
```

X.load_tif_to_data_set(tif_file_path) -> (GDALDatasetHolder, width=int32, height=int32)
Load Tif to Data Set

Args:
    tif_file_path (str): 

Returns:
    tuple: 

    width (int32): 

    height (int32):

<a id="unreal.SuperAPI_RasterBPLibrary.get_number_of_cores_including_hyperthreads"></a>

#### get\_number\_of\_cores\_including\_hyperthreads

```python
@classmethod
def get_number_of_cores_including_hyperthreads(cls) -> int
```

X.get_number_of_cores_including_hyperthreads() -> int32
Get Number Of Cores Including Hyperthreads

Returns:
    int32:

<a id="unreal.SuperAPI_RasterBPLibrary.copy_texture_render_target2d"></a>

#### copy\_texture\_render\_target2d

```python
@classmethod
def copy_texture_render_target2d(cls, src: TextureRenderTarget2D,
                                 dest: TextureRenderTarget2D) -> None
```

X.copy_texture_render_target2d(src, dest) -> None
Copy Texture Render Target 2D

Args:
    src (TextureRenderTarget2D): 
    dest (TextureRenderTarget2D):

<a id="unreal.SuperAPI_RasterBPLibrary.clean_texture_render_target2d"></a>

#### clean\_texture\_render\_target2d

```python
@classmethod
def clean_texture_render_target2d(
        cls, texture_render_target2d: TextureRenderTarget2D) -> None
```

X.clean_texture_render_target2d(texture_render_target2d) -> None
Clean Texture Render Target 2D

Args:
    texture_render_target2d (TextureRenderTarget2D):

<a id="unreal.AnimatedTexture2D_Cov"></a>