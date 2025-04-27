## GeometryScript_EditorTextureUtils Objects

```python
class GeometryScript_EditorTextureUtils(BlueprintFunctionLibrary)
```

Geometry Script Library Editor Texture Map Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingEditor
- **File**: EditorTextureMapFunctions.h

<a id="unreal.GeometryScript_EditorTextureUtils.channel_pack"></a>

#### channel_pack

```python
@classmethod
def channel_pack(
        cls,
        r_channel_source: GeometryScriptChannelPackSource,
        g_channel_source: GeometryScriptChannelPackSource,
        b_channel_source: GeometryScriptChannelPackSource,
        a_channel_source: GeometryScriptChannelPackSource,
        output_srgb: bool,
        debug: GeometryScriptDebug = None) -> GeometryScriptChannelPackResult
```

X.channel_pack(r_channel_source, g_channel_source, b_channel_source, a_channel_source, output_srgb, debug=None) -> GeometryScriptChannelPackResult
Channel Pack

Args:
    r_channel_source (GeometryScriptChannelPackSource): 
    g_channel_source (GeometryScriptChannelPackSource): 
    b_channel_source (GeometryScriptChannelPackSource): 
    a_channel_source (GeometryScriptChannelPackSource): 
    output_srgb (bool): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptChannelPackResult:

<a id="unreal.GeometryScript_NewAssetUtils"></a>