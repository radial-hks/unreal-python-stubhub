## GeometryScript_TextureUtils Objects

```python
class GeometryScript_TextureUtils(BlueprintFunctionLibrary)
```

Geometry Script Library Texture Map Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: TextureMapFunctions.h

<a id="unreal.GeometryScript_TextureUtils.sample_texture_render_target2d_at_uv_positions"></a>

#### sample_texture_render_target2d_at_uv_positions

```python
@classmethod
def sample_texture_render_target2d_at_uv_positions(
        cls,
        uv_list: GeometryScriptUVList,
        texture: TextureRenderTarget2D,
        sample_options: GeometryScriptSampleTextureOptions,
        debug: GeometryScriptDebug = None) -> GeometryScriptColorList
```

X.sample_texture_render_target2d_at_uv_positions(uv_list, texture, sample_options, debug=None) -> GeometryScriptColorList
Sample the the given TextureMap at the list of UV positions and return the color at each position in ColorList output.
This function fetches GPU data before sampling so, depending on your application, it can be inefficient and slow!

Args:
    uv_list (GeometryScriptUVList): 
    texture (TextureRenderTarget2D): 
    sample_options (GeometryScriptSampleTextureOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptColorList: 

    color_list (GeometryScriptColorList):

<a id="unreal.GeometryScript_TextureUtils.sample_texture2d_at_uv_positions"></a>

#### sample_texture2d_at_uv_positions

```python
@classmethod
def sample_texture2d_at_uv_positions(
        cls,
        uv_list: GeometryScriptUVList,
        texture: Texture2D,
        sample_options: GeometryScriptSampleTextureOptions,
        debug: GeometryScriptDebug = None) -> GeometryScriptColorList
```

X.sample_texture2d_at_uv_positions(uv_list, texture, sample_options, debug=None) -> GeometryScriptColorList
Samples the given TextureMap at the list of UV positions and returns the color at each position in ColorList output.

Args:
    uv_list (GeometryScriptUVList): 
    texture (Texture2D): 
    sample_options (GeometryScriptSampleTextureOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptColorList: 

    color_list (GeometryScriptColorList):

<a id="unreal.GeometryScript_VectorMath"></a>