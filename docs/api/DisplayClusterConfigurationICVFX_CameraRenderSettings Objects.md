## DisplayClusterConfigurationICVFX_CameraRenderSettings Objects

```python
class DisplayClusterConfigurationICVFX_CameraRenderSettings(StructBase)
```

Display Cluster Configuration ICVFX Camera Render Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_render_settings`` (DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings):  [Read-Write] Advanced render settings
- ``custom_frame_size`` (DisplayClusterConfigurationICVFX_CustomSize):  [Read-Write] Custom resolution of the ICVFX Camera. If it is not used, the Default Frame Resolution value is used by default.
- ``generate_mips`` (DisplayClusterConfigurationPostRender_GenerateMips):  [Read-Write] Mipmapping can help avoid visual artifacts when the inner frustum is rendered at a lower resolution than specified in the configuration and is smaller on screen than the available pixels on the display device.
- ``media`` (DisplayClusterConfigurationMediaICVFX):  [Read-Write] Media settings
- ``render_order`` (int32):  [Read-Write] Camera render order, bigger value is over
- ``replace`` (DisplayClusterConfigurationPostRender_Override):  [Read-Write] Replace viewport render from source texture
- ``use_camera_component_postprocess`` (bool):  [Read-Write] Use postprocess settings from camera component

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.__init__"></a>

#### __init__

```python
def __init__(
    custom_frame_size: DisplayClusterConfigurationICVFX_CustomSize = [
        False, 2560, 1440, True
    ],
    render_order: int = 0,
    use_camera_component_postprocess: bool = False,
    replace: DisplayClusterConfigurationPostRender_Override = [
        False, None, False, [[0, 0], [0, 0]]
    ],
    media: DisplayClusterConfigurationMediaICVFX = [
        False, DisplayClusterConfigurationMediaSplitType.FULL_FRAME, [], [],
        [1, 1],
        [
            False, True, True,
            DisplayClusterConfigurationViewportOverscanMode.PERCENT, 10.000000
        ], [[]], [], [], False
    ],
    generate_mips: DisplayClusterConfigurationPostRender_GenerateMips = [
        False, TextureFilter.TF_TRILINEAR, TextureAddress.TA_CLAMP,
        TextureAddress.TA_CLAMP, False, 0
    ],
    advanced_render_settings:
    DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings = [
        1.000000, -1, -1,
        DisplayClusterConfigurationViewport_StereoMode.DEFAULT
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.custom_frame_size"></a>

#### custom_frame_size

```python
@property
def custom_frame_size() -> DisplayClusterConfigurationICVFX_CustomSize
```

(DisplayClusterConfigurationICVFX_CustomSize):  [Read-Write] Custom resolution of the ICVFX Camera. If it is not used, the Default Frame Resolution value is used by default.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.custom_frame_size"></a>

#### custom_frame_size

```python
@custom_frame_size.setter
def custom_frame_size(
        value: DisplayClusterConfigurationICVFX_CustomSize) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.render_order"></a>

#### render_order

```python
@property
def render_order() -> int
```

(int32):  [Read-Write] Camera render order, bigger value is over

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.render_order"></a>

#### render_order

```python
@render_order.setter
def render_order(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.use_camera_component_postprocess"></a>

#### use_camera_component_postprocess

```python
@property
def use_camera_component_postprocess() -> bool
```

(bool):  [Read-Write] Use postprocess settings from camera component

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.use_camera_component_postprocess"></a>

#### use_camera_component_postprocess

```python
@use_camera_component_postprocess.setter
def use_camera_component_postprocess(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.replace"></a>

#### replace

```python
@property
def replace() -> DisplayClusterConfigurationPostRender_Override
```

(DisplayClusterConfigurationPostRender_Override):  [Read-Write] Replace viewport render from source texture

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.replace"></a>

#### replace

```python
@replace.setter
def replace(value: DisplayClusterConfigurationPostRender_Override) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.media"></a>

#### media

```python
@property
def media() -> DisplayClusterConfigurationMediaICVFX
```

(DisplayClusterConfigurationMediaICVFX):  [Read-Write] Media settings

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.media"></a>

#### media

```python
@media.setter
def media(value: DisplayClusterConfigurationMediaICVFX) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.generate_mips"></a>

#### generate_mips

```python
@property
def generate_mips() -> DisplayClusterConfigurationPostRender_GenerateMips
```

(DisplayClusterConfigurationPostRender_GenerateMips):  [Read-Write] Mipmapping can help avoid visual artifacts when the inner frustum is rendered at a lower resolution than specified in the configuration and is smaller on screen than the available pixels on the display device.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.generate_mips"></a>

#### generate_mips

```python
@generate_mips.setter
def generate_mips(
        value: DisplayClusterConfigurationPostRender_GenerateMips) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.advanced_render_settings"></a>

#### advanced_render_settings

```python
@property
def advanced_render_settings(
) -> DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings
```

(DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings):  [Read-Write] Advanced render settings

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings.advanced_render_settings"></a>

#### advanced_render_settings

```python
@advanced_render_settings.setter
def advanced_render_settings(
    value: DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX"></a>