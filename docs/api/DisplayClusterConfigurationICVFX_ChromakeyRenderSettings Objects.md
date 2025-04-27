## DisplayClusterConfigurationICVFX_ChromakeyRenderSettings Objects

```python
class DisplayClusterConfigurationICVFX_ChromakeyRenderSettings(StructBase)
```

Display Cluster Configuration ICVFX Chromakey Render Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_render_settings`` (DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings):  [Read-Write] Advanced render settings
- ``chromakey_size_mult`` (float):  [Read-Write] Resolution multiplier for RTT chromakey. The default is the ICVFX camera frame resolution.
- ``custom_size`` (DisplayClusterConfigurationICVFX_CustomSize):  [Read-Write]
  deprecated: Use the 'Chromakey Resolution Multiplier' instead
- ``enable`` (bool):  [Read-Write]
  deprecated: Use the Chromakey Type enum in the chromakey settings instead
- ``generate_mips`` (DisplayClusterConfigurationPostRender_GenerateMips):  [Read-Write]
- ``postprocess_blur`` (DisplayClusterConfigurationPostRender_BlurPostprocess):  [Read-Write] Apply blur to the Custom Chromakey content.
- ``replace`` (DisplayClusterConfigurationPostRender_Override):  [Read-Write] Replace viewport render from source texture
- ``replace_camera_viewport`` (bool):  [Read-Write] Replace the texture of the camera viewport from this chromakey RTT
- ``show_only_list`` (DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will be overridden to use the chromakey color specified and include chromakey markers if enabled.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.__init__"></a>

#### __init__

```python
def __init__(
    replace_camera_viewport: bool = False,
    chromakey_size_mult: float = 0.000000,
    show_only_list: DisplayClusterConfigurationICVFX_VisibilityList = [[], [],
                                                                       []],
    replace: DisplayClusterConfigurationPostRender_Override = [
        False, None, False, [[0, 0], [0, 0]]
    ],
    postprocess_blur: DisplayClusterConfigurationPostRender_BlurPostprocess = [
        DisplayClusterConfiguration_PostRenderBlur.NONE, 5, 20.000000
    ],
    generate_mips: DisplayClusterConfigurationPostRender_GenerateMips = [
        False, TextureFilter.TF_TRILINEAR, TextureAddress.TA_CLAMP,
        TextureAddress.TA_CLAMP, False, 0
    ],
    advanced_render_settings:
    DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings = [
        1.000000, 1.000000, -1, -1,
        DisplayClusterConfigurationViewport_StereoMode.DEFAULT
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write]
deprecated: Use the Chromakey Type enum in the chromakey settings instead

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.replace_camera_viewport"></a>

#### replace_camera_viewport

```python
@property
def replace_camera_viewport() -> bool
```

(bool):  [Read-Write] Replace the texture of the camera viewport from this chromakey RTT

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.replace_camera_viewport"></a>

#### replace_camera_viewport

```python
@replace_camera_viewport.setter
def replace_camera_viewport(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.custom_size"></a>

#### custom_size

```python
@property
def custom_size() -> DisplayClusterConfigurationICVFX_CustomSize
```

(DisplayClusterConfigurationICVFX_CustomSize):  [Read-Write]
deprecated: Use the 'Chromakey Resolution Multiplier' instead

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.custom_size"></a>

#### custom_size

```python
@custom_size.setter
def custom_size(value: DisplayClusterConfigurationICVFX_CustomSize) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.chromakey_size_mult"></a>

#### chromakey_size_mult

```python
@property
def chromakey_size_mult() -> float
```

(float):  [Read-Write] Resolution multiplier for RTT chromakey. The default is the ICVFX camera frame resolution.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.chromakey_size_mult"></a>

#### chromakey_size_mult

```python
@chromakey_size_mult.setter
def chromakey_size_mult(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.show_only_list"></a>

#### show_only_list

```python
@property
def show_only_list() -> DisplayClusterConfigurationICVFX_VisibilityList
```

(DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will be overridden to use the chromakey color specified and include chromakey markers if enabled.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.show_only_list"></a>

#### show_only_list

```python
@show_only_list.setter
def show_only_list(
        value: DisplayClusterConfigurationICVFX_VisibilityList) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.replace"></a>

#### replace

```python
@property
def replace() -> DisplayClusterConfigurationPostRender_Override
```

(DisplayClusterConfigurationPostRender_Override):  [Read-Write] Replace viewport render from source texture

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.replace"></a>

#### replace

```python
@replace.setter
def replace(value: DisplayClusterConfigurationPostRender_Override) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.postprocess_blur"></a>

#### postprocess_blur

```python
@property
def postprocess_blur(
) -> DisplayClusterConfigurationPostRender_BlurPostprocess
```

(DisplayClusterConfigurationPostRender_BlurPostprocess):  [Read-Write] Apply blur to the Custom Chromakey content.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.postprocess_blur"></a>

#### postprocess_blur

```python
@postprocess_blur.setter
def postprocess_blur(
        value: DisplayClusterConfigurationPostRender_BlurPostprocess) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.generate_mips"></a>

#### generate_mips

```python
@property
def generate_mips() -> DisplayClusterConfigurationPostRender_GenerateMips
```

(DisplayClusterConfigurationPostRender_GenerateMips):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.generate_mips"></a>

#### generate_mips

```python
@generate_mips.setter
def generate_mips(
        value: DisplayClusterConfigurationPostRender_GenerateMips) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.advanced_render_settings"></a>

#### advanced_render_settings

```python
@property
def advanced_render_settings(
) -> DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings
```

(DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings):  [Read-Write] Advanced render settings

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings.advanced_render_settings"></a>

#### advanced_render_settings

```python
@advanced_render_settings.setter
def advanced_render_settings(
    value: DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips"></a>