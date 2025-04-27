## RenderingLibrary Objects

```python
class RenderingLibrary(BlueprintFunctionLibrary)
```

Kismet Rendering Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetRenderingLibrary.h

<a id="unreal.RenderingLibrary.set_cast_inset_shadow_for_all_attachments"></a>

#### set_cast_inset_shadow_for_all_attachments

```python
@classmethod
def set_cast_inset_shadow_for_all_attachments(
        cls, primitive_component: PrimitiveComponent, cast_inset_shadow: bool,
        light_attachments_as_group: bool) -> None
```

X.set_cast_inset_shadow_for_all_attachments(primitive_component, cast_inset_shadow, light_attachments_as_group) -> None
Set the inset shadow casting state of the given component and all its child attachments.
    Also choose if all attachments should be grouped for the inset shadow rendering. If enabled, one depth target will be shared for all attachments.

Args:
    primitive_component (PrimitiveComponent): 
    cast_inset_shadow (bool): 
    light_attachments_as_group (bool):

<a id="unreal.RenderingLibrary.resize_render_target2d"></a>

#### resize_render_target2d

```python
@classmethod
def resize_render_target2d(cls,
                           texture_render_target: TextureRenderTarget2D,
                           width: int = 256,
                           height: int = 256) -> None
```

X.resize_render_target2d(texture_render_target, width=256, height=256) -> None
Changes the resolution of a render target. This is useful for when you need to resize the game viewport or change the in-game resolution during runtime
and thus need to update the sizes of all the render targets in the game accordingly.

Args:
    texture_render_target (TextureRenderTarget2D): 
    width (int32): 
    height (int32):

<a id="unreal.RenderingLibrary.render_target_create_static_volume_texture_editor_only"></a>

#### render_target_create_static_volume_texture_editor_only

```python
@classmethod
def render_target_create_static_volume_texture_editor_only(
    cls,
    render_target: TextureRenderTargetVolume,
    name: str = "Texture",
    compression_settings:
    TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT,
    mip_settings: TextureMipGenSettings = TextureMipGenSettings.
    TMGS_FROM_TEXTURE_GROUP
) -> VolumeTexture
```

X.render_target_create_static_volume_texture_editor_only(render_target, name="Texture", compression_settings=TextureCompressionSettings.TC_DEFAULT, mip_settings=TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP) -> VolumeTexture
Creates a new Static Volume Texture from a Render Target Volume.
Only works in the editor

Args:
    render_target (TextureRenderTargetVolume): 
    name (str): 
    compression_settings (TextureCompressionSettings): 
    mip_settings (TextureMipGenSettings): 

Returns:
    VolumeTexture:

<a id="unreal.RenderingLibrary.render_target_create_static_texture_cube_editor_only"></a>

#### render_target_create_static_texture_cube_editor_only

```python
@classmethod
def render_target_create_static_texture_cube_editor_only(
    cls,
    render_target: TextureRenderTargetCube,
    name: str = "Texture",
    compression_settings:
    TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT,
    mip_settings: TextureMipGenSettings = TextureMipGenSettings.
    TMGS_FROM_TEXTURE_GROUP
) -> TextureCube
```

X.render_target_create_static_texture_cube_editor_only(render_target, name="Texture", compression_settings=TextureCompressionSettings.TC_DEFAULT, mip_settings=TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP) -> TextureCube
Creates a new Static Texture Cube from a Render Target Cube.
Only works in the editor

Args:
    render_target (TextureRenderTargetCube): 
    name (str): 
    compression_settings (TextureCompressionSettings): 
    mip_settings (TextureMipGenSettings): 

Returns:
    TextureCube:

<a id="unreal.RenderingLibrary.render_target_create_static_texture2d_editor_only"></a>

#### render_target_create_static_texture2d_editor_only

```python
@classmethod
def render_target_create_static_texture2d_editor_only(
    cls,
    render_target: TextureRenderTarget2D,
    name: str = "Texture",
    compression_settings:
    TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT,
    mip_settings: TextureMipGenSettings = TextureMipGenSettings.
    TMGS_FROM_TEXTURE_GROUP
) -> Texture2D
```

X.render_target_create_static_texture2d_editor_only(render_target, name="Texture", compression_settings=TextureCompressionSettings.TC_DEFAULT, mip_settings=TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP) -> Texture2D
Creates a new Static Texture from a Render Target 2D.
Only works in the editor

Args:
    render_target (TextureRenderTarget2D): 
    name (str): 
    compression_settings (TextureCompressionSettings): 
    mip_settings (TextureMipGenSettings): 

Returns:
    Texture2D:

<a id="unreal.RenderingLibrary.render_target_create_static_texture2d_array_editor_only"></a>

#### render_target_create_static_texture2d_array_editor_only

```python
@classmethod
def render_target_create_static_texture2d_array_editor_only(
    cls,
    render_target: TextureRenderTarget2DArray,
    name: str = "Texture",
    compression_settings:
    TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT,
    mip_settings: TextureMipGenSettings = TextureMipGenSettings.
    TMGS_FROM_TEXTURE_GROUP
) -> Texture2DArray
```

X.render_target_create_static_texture2d_array_editor_only(render_target, name="Texture", compression_settings=TextureCompressionSettings.TC_DEFAULT, mip_settings=TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP) -> Texture2DArray
Creates a new Static Texture 2D Array from a Render Target 2D Array.
Only works in the editor

Args:
    render_target (TextureRenderTarget2DArray): 
    name (str): 
    compression_settings (TextureCompressionSettings): 
    mip_settings (TextureMipGenSettings): 

Returns:
    Texture2DArray:

<a id="unreal.RenderingLibrary.release_render_target2d"></a>

#### release_render_target2d

```python
@classmethod
def release_render_target2d(
        cls, texture_render_target: TextureRenderTarget2D) -> None
```

X.release_render_target2d(texture_render_target) -> None
Manually releases GPU resources of a render target. This is useful for blueprint creating a lot of render target that would
normally be released too late by the garbage collector that can be problematic on platforms that have tight GPU memory constrains.

Args:
    texture_render_target (TextureRenderTarget2D):

<a id="unreal.RenderingLibrary.refresh_path_tracing_output"></a>

#### refresh_path_tracing_output

```python
@classmethod
def refresh_path_tracing_output(cls) -> None
```

X.refresh_path_tracing_output() -> None
Forces the path tracer to restart sample accumulation.
This can be used to force the path tracer to compute a new frame in situations where it can not detect a change in the scene automatically.

<a id="unreal.RenderingLibrary.read_render_target_uv"></a>

#### read_render_target_uv

```python
@classmethod
def read_render_target_uv(cls, world_context_object: Object,
                          texture_render_target: TextureRenderTarget2D,
                          u: float, v: float) -> Color
```

X.read_render_target_uv(world_context_object, texture_render_target, u, v) -> Color
Incredibly inefficient and slow operation! Read a value as sRGB color from a render target using UV [0,1]x[0,1] coordinates.
LDR render targets are assumed to be in sRGB space. HDR ones are assumed to be in linear space.
Result is 8-bit per channel [0,255] BGRA in sRGB space.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    u (float): 
    v (float): 

Returns:
    Color:

<a id="unreal.RenderingLibrary.read_render_target_raw_uv_area"></a>

#### read_render_target_raw_uv_area

```python
@classmethod
def read_render_target_raw_uv_area(
        cls,
        world_context_object: Object,
        texture_render_target: TextureRenderTarget2D,
        area: Box2D,
        normalize: bool = True) -> Array[LinearColor]
```

X.read_render_target_raw_uv_area(world_context_object, texture_render_target, area, normalize=True) -> Array[LinearColor]
Incredibly inefficient and slow operation! Read an area of values as-is from a render target using a rectangle defined by UV [0,1]x[0,1] coordinates.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    area (Box2D): 
    normalize (bool): 

Returns:
    Array[LinearColor]:

<a id="unreal.RenderingLibrary.read_render_target_raw_uv"></a>

#### read_render_target_raw_uv

```python
@classmethod
def read_render_target_raw_uv(cls,
                              world_context_object: Object,
                              texture_render_target: TextureRenderTarget2D,
                              u: float,
                              v: float,
                              normalize: bool = True) -> LinearColor
```

X.read_render_target_raw_uv(world_context_object, texture_render_target, u, v, normalize=True) -> LinearColor
Incredibly inefficient and slow operation! Read a value as-is from a render target using UV [0,1]x[0,1] coordinates.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    u (float): 
    v (float): 
    normalize (bool): 

Returns:
    LinearColor:

<a id="unreal.RenderingLibrary.read_render_target_raw_pixel_area"></a>

#### read_render_target_raw_pixel_area

```python
@classmethod
def read_render_target_raw_pixel_area(
        cls,
        world_context_object: Object,
        texture_render_target: TextureRenderTarget2D,
        min_x: int,
        min_y: int,
        max_x: int,
        max_y: int,
        normalize: bool = True) -> Array[LinearColor]
```

X.read_render_target_raw_pixel_area(world_context_object, texture_render_target, min_x, min_y, max_x, max_y, normalize=True) -> Array[LinearColor]
Incredibly inefficient and slow operation! Read an area of values as-is from a render target using a rectangle defined by integer pixel coordinates.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    min_x (int32): 
    min_y (int32): 
    max_x (int32): 
    max_y (int32): 
    normalize (bool): 

Returns:
    Array[LinearColor]:

<a id="unreal.RenderingLibrary.read_render_target_raw_pixel"></a>

#### read_render_target_raw_pixel

```python
@classmethod
def read_render_target_raw_pixel(cls,
                                 world_context_object: Object,
                                 texture_render_target: TextureRenderTarget2D,
                                 x: int,
                                 y: int,
                                 normalize: bool = True) -> LinearColor
```

X.read_render_target_raw_pixel(world_context_object, texture_render_target, x, y, normalize=True) -> LinearColor
Incredibly inefficient and slow operation! Read a value as-is from a render target using integer pixel coordinates.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    x (int32): 
    y (int32): 
    normalize (bool): 

Returns:
    LinearColor:

<a id="unreal.RenderingLibrary.read_render_target_raw"></a>

#### read_render_target_raw

```python
@classmethod
def read_render_target_raw(
        cls,
        world_context_object: Object,
        texture_render_target: TextureRenderTarget2D,
        normalize: bool = True) -> Optional[Array[LinearColor]]
```

X.read_render_target_raw(world_context_object, texture_render_target, normalize=True) -> Array[LinearColor] or None
Incredibly inefficient and slow operation! Read entire texture as-is from a render target.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    normalize (bool): 

Returns:
    Array[LinearColor] or None: 

    out_linear_samples (Array[LinearColor]):

<a id="unreal.RenderingLibrary.read_render_target_pixel"></a>

#### read_render_target_pixel

```python
@classmethod
def read_render_target_pixel(cls, world_context_object: Object,
                             texture_render_target: TextureRenderTarget2D,
                             x: int, y: int) -> Color
```

X.read_render_target_pixel(world_context_object, texture_render_target, x, y) -> Color
Incredibly inefficient and slow operation! Read a value as sRGB color from a render target using integer pixel coordinates.
LDR render targets are assumed to be in sRGB space. HDR ones are assumed to be in linear space.
Result is 8-bit per channel [0,255] BGRA in sRGB space.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    x (int32): 
    y (int32): 

Returns:
    Color:

<a id="unreal.RenderingLibrary.read_render_target"></a>

#### read_render_target

```python
@classmethod
def read_render_target(cls,
                       world_context_object: Object,
                       texture_render_target: TextureRenderTarget2D,
                       normalize: bool = True) -> Optional[Array[Color]]
```

X.read_render_target(world_context_object, texture_render_target, normalize=True) -> Array[Color] or None
Incredibly inefficient and slow operation! Reads entire render target as sRGB color and returns a linear array of sRGB colors.
LDR render targets are assumed to be in sRGB space. HDR ones are assumed to be in linear space.
Result whether the operation succeeded.  If successful, OutSamples will an entry per pixel, where each is 8-bit per channel [0,255] BGRA in sRGB space.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    normalize (bool): 

Returns:
    Array[Color] or None: 

    out_samples (Array[Color]):

<a id="unreal.RenderingLibrary.import_file_as_texture2d"></a>

#### import_file_as_texture2d

```python
@classmethod
def import_file_as_texture2d(cls, world_context_object: Object,
                             filename: str) -> Texture2D
```

X.import_file_as_texture2d(world_context_object, filename) -> Texture2D
Imports a texture file from disk and creates Texture2D from it.

Args:
    world_context_object (Object): 
    filename (str): 

Returns:
    Texture2D:

<a id="unreal.RenderingLibrary.import_buffer_as_texture2d"></a>

#### import_buffer_as_texture2d

```python
@classmethod
def import_buffer_as_texture2d(cls, world_context_object: Object,
                               buffer: Array[int]) -> Texture2D
```

X.import_buffer_as_texture2d(world_context_object, buffer) -> Texture2D
Imports a texture from a buffer and creates Texture2D from it.

Args:
    world_context_object (Object): 
    buffer (Array[uint8]): 

Returns:
    Texture2D:

<a id="unreal.RenderingLibrary.export_texture2d"></a>

#### export_texture2d

```python
@classmethod
def export_texture2d(cls, world_context_object: Object, texture: Texture2D,
                     file_path: str, file_name: str) -> None
```

X.export_texture2d(world_context_object, texture, file_path, file_name) -> None
Exports a Texture2D as a HDR image onto the disk.

Args:
    world_context_object (Object): 
    texture (Texture2D): 
    file_path (str): 
    file_name (str):

<a id="unreal.RenderingLibrary.export_render_target"></a>

#### export_render_target

```python
@classmethod
def export_render_target(cls, world_context_object: Object,
                         texture_render_target: TextureRenderTarget2D,
                         file_path: str, file_name: str) -> None
```

X.export_render_target(world_context_object, texture_render_target, file_path, file_name) -> None
Exports a render target as a HDR or PNG image onto the disk (depending on the format of the render target)

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    file_path (str): 
    file_name (str):

<a id="unreal.RenderingLibrary.end_draw_canvas_to_render_target"></a>

#### end_draw_canvas_to_render_target

```python
@classmethod
def end_draw_canvas_to_render_target(
        cls, world_context_object: Object,
        context: DrawToRenderTargetContext) -> None
```

X.end_draw_canvas_to_render_target(world_context_object, context) -> None
Must be paired with a BeginDrawCanvasToRenderTarget to complete rendering to a render target.

Args:
    world_context_object (Object): 
    context (DrawToRenderTargetContext):

<a id="unreal.RenderingLibrary.enable_path_tracing"></a>

#### enable_path_tracing

```python
@classmethod
def enable_path_tracing(cls, enable_path_tracer: bool) -> None
```

X.enable_path_tracing(enable_path_tracer) -> None
Enables or disables the path tracer for the current Game Viewport.
This command is equivalent to setting ShowFlag.PathTracing, but is accessible even from shipping builds.

Args:
    enable_path_tracer (bool):

<a id="unreal.RenderingLibrary.draw_material_to_render_target"></a>

#### draw_material_to_render_target

```python
@classmethod
def draw_material_to_render_target(
        cls, world_context_object: Object,
        texture_render_target: TextureRenderTarget2D,
        material: MaterialInterface) -> None
```

X.draw_material_to_render_target(world_context_object, texture_render_target, material) -> None
Renders a quad with the material applied to the specified render target.
This sets the render target even if it is already set, which is an expensive operation.
Use BeginDrawCanvasToRenderTarget / EndDrawCanvasToRenderTarget instead if rendering multiple primitives to the same render target.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    material (MaterialInterface):

<a id="unreal.RenderingLibrary.create_render_target_volume"></a>

#### create_render_target_volume

```python
@classmethod
def create_render_target_volume(
        cls,
        world_context_object: Object,
        width: int = 16,
        height: int = 16,
        depth: int = 16,
        format: TextureRenderTargetFormat = TextureRenderTargetFormat.
    RTF_RGBA16F,
        clear_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000],
        auto_generate_mip_maps: bool = False,
        support_ua_vs: bool = False) -> TextureRenderTargetVolume
```

X.create_render_target_volume(world_context_object, width=16, height=16, depth=16, format=TextureRenderTargetFormat.RTF_RGBA16F, clear_color=[0.000000, 0.000000, 0.000000, 1.000000], auto_generate_mip_maps=False, support_ua_vs=False) -> TextureRenderTargetVolume
Creates a new volume render target and initializes it to the specified dimensions

Args:
    world_context_object (Object): 
    width (int32): 
    height (int32): 
    depth (int32): 
    format (TextureRenderTargetFormat): 
    clear_color (LinearColor): 
    auto_generate_mip_maps (bool): 
    support_ua_vs (bool): 

Returns:
    TextureRenderTargetVolume:

<a id="unreal.RenderingLibrary.create_render_target2d_array"></a>

#### create_render_target2d_array

```python
@classmethod
def create_render_target2d_array(
        cls,
        world_context_object: Object,
        width: int = 256,
        height: int = 256,
        slices: int = 1,
        format: TextureRenderTargetFormat = TextureRenderTargetFormat.
    RTF_RGBA16F,
        clear_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000],
        auto_generate_mip_maps: bool = False,
        support_ua_vs: bool = False) -> TextureRenderTarget2DArray
```

X.create_render_target2d_array(world_context_object, width=256, height=256, slices=1, format=TextureRenderTargetFormat.RTF_RGBA16F, clear_color=[0.000000, 0.000000, 0.000000, 1.000000], auto_generate_mip_maps=False, support_ua_vs=False) -> TextureRenderTarget2DArray
Creates a new render target array and initializes it to the specified dimensions

Args:
    world_context_object (Object): 
    width (int32): 
    height (int32): 
    slices (int32): 
    format (TextureRenderTargetFormat): 
    clear_color (LinearColor): 
    auto_generate_mip_maps (bool): 
    support_ua_vs (bool): 

Returns:
    TextureRenderTarget2DArray:

<a id="unreal.RenderingLibrary.create_render_target2d"></a>

#### create_render_target2d

```python
@classmethod
def create_render_target2d(
        cls,
        world_context_object: Object,
        width: int = 256,
        height: int = 256,
        format: TextureRenderTargetFormat = TextureRenderTargetFormat.
    RTF_RGBA16F,
        clear_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000],
        auto_generate_mip_maps: bool = False,
        support_ua_vs: bool = False) -> TextureRenderTarget2D
```

X.create_render_target2d(world_context_object, width=256, height=256, format=TextureRenderTargetFormat.RTF_RGBA16F, clear_color=[0.000000, 0.000000, 0.000000, 1.000000], auto_generate_mip_maps=False, support_ua_vs=False) -> TextureRenderTarget2D
Creates a new render target and initializes it to the specified dimensions

Args:
    world_context_object (Object): 
    width (int32): 
    height (int32): 
    format (TextureRenderTargetFormat): 
    clear_color (LinearColor): 
    auto_generate_mip_maps (bool): 
    support_ua_vs (bool): 

Returns:
    TextureRenderTarget2D:

<a id="unreal.RenderingLibrary.convert_render_target_to_texture_volume_editor_only"></a>

#### convert_render_target_to_texture_volume_editor_only

```python
@classmethod
def convert_render_target_to_texture_volume_editor_only(
        cls, world_context_object: Object,
        render_target: TextureRenderTargetVolume,
        texture: VolumeTexture) -> None
```

X.convert_render_target_to_texture_volume_editor_only(world_context_object, render_target, texture) -> None
Copies the contents of a UTextureRenderTargetVolume to a UVolumeTexture
Only works in the editor

Args:
    world_context_object (Object): 
    render_target (TextureRenderTargetVolume): 
    texture (VolumeTexture):

<a id="unreal.RenderingLibrary.convert_render_target_to_texture_cube_editor_only"></a>

#### convert_render_target_to_texture_cube_editor_only

```python
@classmethod
def convert_render_target_to_texture_cube_editor_only(
        cls, world_context_object: Object,
        render_target: TextureRenderTargetCube, texture: TextureCube) -> None
```

X.convert_render_target_to_texture_cube_editor_only(world_context_object, render_target, texture) -> None
Copies the contents of a UTextureRenderTargetCube to a UTextureCube
Only works in the editor

Args:
    world_context_object (Object): 
    render_target (TextureRenderTargetCube): 
    texture (TextureCube):

<a id="unreal.RenderingLibrary.convert_render_target_to_texture2d_editor_only"></a>

#### convert_render_target_to_texture2d_editor_only

```python
@classmethod
def convert_render_target_to_texture2d_editor_only(
        cls, world_context_object: Object,
        render_target: TextureRenderTarget2D, texture: Texture2D) -> None
```

X.convert_render_target_to_texture2d_editor_only(world_context_object, render_target, texture) -> None
Copies the contents of a UTextureRenderTarget2D to a UTexture2D
Only works in the editor

Args:
    world_context_object (Object): 
    render_target (TextureRenderTarget2D): 
    texture (Texture2D):

<a id="unreal.RenderingLibrary.convert_render_target_to_texture2d_array_editor_only"></a>

#### convert_render_target_to_texture2d_array_editor_only

```python
@classmethod
def convert_render_target_to_texture2d_array_editor_only(
        cls, world_context_object: Object,
        render_target: TextureRenderTarget2DArray,
        texture: Texture2DArray) -> None
```

X.convert_render_target_to_texture2d_array_editor_only(world_context_object, render_target, texture) -> None
Copies the contents of a UTextureRenderTarget2DArray to a UTexture2DArray
Only works in the editor

Args:
    world_context_object (Object): 
    render_target (TextureRenderTarget2DArray): 
    texture (Texture2DArray):

<a id="unreal.RenderingLibrary.clear_render_target2d"></a>

#### clear_render_target2d

```python
@classmethod
def clear_render_target2d(
    cls,
    world_context_object: Object,
    texture_render_target: TextureRenderTarget2D,
    clear_color: LinearColor = [0.000000, 0.000000, 0.000000,
                                1.000000]) -> None
```

X.clear_render_target2d(world_context_object, texture_render_target, clear_color=[0.000000, 0.000000, 0.000000, 1.000000]) -> None
Clears the specified render target with the given ClearColor.

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 
    clear_color (LinearColor):

<a id="unreal.RenderingLibrary.calculate_projection_matrix"></a>

#### calculate_projection_matrix

```python
@classmethod
def calculate_projection_matrix(cls,
                                minimal_view_info: MinimalViewInfo) -> Matrix
```

X.calculate_projection_matrix(minimal_view_info) -> Matrix
Calculates the projection matrix using this view info's aspect ratio (regardless of bConstrainAspectRatio)

Args:
    minimal_view_info (MinimalViewInfo): 

Returns:
    Matrix:

<a id="unreal.RenderingLibrary.begin_draw_canvas_to_render_target"></a>

#### begin_draw_canvas_to_render_target

```python
@classmethod
def begin_draw_canvas_to_render_target(
    cls, world_context_object: Object,
    texture_render_target: TextureRenderTarget2D
) -> Tuple[Canvas, Vector2D, DrawToRenderTargetContext]
```

X.begin_draw_canvas_to_render_target(world_context_object, texture_render_target) -> (canvas=Canvas, size=Vector2D, context=DrawToRenderTargetContext)
Returns a Canvas object that can be used to draw to the specified render target.
Canvas has functions like DrawMaterial with size parameters that can be used to draw to a specific area of a render target.
Be sure to call EndDrawCanvasToRenderTarget to complete the rendering!

Args:
    world_context_object (Object): 
    texture_render_target (TextureRenderTarget2D): 

Returns:
    tuple: 

    canvas (Canvas): 

    size (Vector2D): 

    context (DrawToRenderTargetContext):

<a id="unreal.StringLibrary"></a>