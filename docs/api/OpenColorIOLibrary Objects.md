## OpenColorIOLibrary Objects

```python
class OpenColorIOLibrary(BlueprintFunctionLibrary)
```

Open Color IOBlueprint Library

**C++ Source:**

- **Plugin**: OpenColorIO
- **Module**: OpenColorIO
- **File**: OpenColorIOBlueprintLibrary.h

<a id="unreal.OpenColorIOLibrary.apply_color_space_transform"></a>

#### apply_color_space_transform

```python
@classmethod
def apply_color_space_transform(
        cls, world_context_object: Object,
        conversion_settings: OpenColorIOColorConversionSettings,
        input_texture: Texture,
        output_render_target: TextureRenderTarget2D) -> bool
```

X.apply_color_space_transform(world_context_object, conversion_settings, input_texture, output_render_target) -> bool
Applies a rendering pass of the color transform described in the settings

Args:
    world_context_object (Object): World from which to get the actual shader feature level we need to render
    conversion_settings (OpenColorIOColorConversionSettings): Settings describing the color space transform to apply
    input_texture (Texture): Texture in the source color space
    output_render_target (TextureRenderTarget2D): RenderTarget where to draw the input texture in the destination color space

Returns:
    bool: True if a rendering command to apply the transform was queued.

<a id="unreal.OpenColorIOConfiguration"></a>