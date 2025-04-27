## OpenColorIOEditorBlueprintLibrary Objects

```python
class OpenColorIOEditorBlueprintLibrary(BlueprintFunctionLibrary)
```

Open Color IOEditor Blueprint Library

**C++ Source:**

- **Plugin**: OpenColorIO
- **Module**: OpenColorIOEditor
- **File**: OpenColorIOEditorBlueprintLibrary.h

<a id="unreal.OpenColorIOEditorBlueprintLibrary.set_active_viewport_configuration"></a>

#### set_active_viewport_configuration

```python
@classmethod
def set_active_viewport_configuration(
        cls, configuration: OpenColorIODisplayConfiguration) -> None
```

X.set_active_viewport_configuration(configuration) -> None
Set the active editor viewport's display configuration color transform .

Args:
    configuration (OpenColorIODisplayConfiguration):

<a id="unreal.OpenColorIOEditorBlueprintLibrary.apply_color_space_transform_to_texture_compressed"></a>

#### apply_color_space_transform_to_texture_compressed

```python
@classmethod
def apply_color_space_transform_to_texture_compressed(
        cls, conversion_settings: OpenColorIOColorConversionSettings,
        target_compression: TextureCompressionSettings,
        out_texture: Texture) -> bool
```

X.apply_color_space_transform_to_texture_compressed(conversion_settings, target_compression, out_texture) -> bool
Apply a color space transform with a target compression setting to a texture asset.

Args:
    conversion_settings (OpenColorIOColorConversionSettings): Color transformation settings.
    target_compression (TextureCompressionSettings): Target texture compression setting.
    out_texture (Texture): Texture object to transform.

Returns:
    bool: true upon success.

<a id="unreal.OpenColorIOEditorBlueprintLibrary.apply_color_space_transform_to_texture"></a>

#### apply_color_space_transform_to_texture

```python
@classmethod
def apply_color_space_transform_to_texture(
        cls, conversion_settings: OpenColorIOColorConversionSettings,
        out_texture: Texture) -> bool
```

X.apply_color_space_transform_to_texture(conversion_settings, out_texture) -> bool
Apply a color space transform to a texture asset.

Args:
    conversion_settings (OpenColorIOColorConversionSettings): Color transformation settings.
    out_texture (Texture): Texture object to transform.

Returns:
    bool: true upon success.

<a id="unreal.OpenColorIOEditorBlueprintLibrary.apply_color_space_transform_to_color"></a>

#### apply_color_space_transform_to_color

```python
@classmethod
def apply_color_space_transform_to_color(
        cls, conversion_settings: OpenColorIOColorConversionSettings,
        color: LinearColor) -> Optional[LinearColor]
```

X.apply_color_space_transform_to_color(conversion_settings, color) -> LinearColor or None
Apply a color space transform to a color value.

Args:
    conversion_settings (OpenColorIOColorConversionSettings): Color transformation settings.
    color (LinearColor): 

Returns:
    LinearColor or None: true upon success.

    out_color (LinearColor):

<a id="unreal.AudioCurveSourceComponent"></a>