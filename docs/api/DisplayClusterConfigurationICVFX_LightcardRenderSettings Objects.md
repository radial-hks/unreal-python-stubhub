## DisplayClusterConfigurationICVFX_LightcardRenderSettings Objects

```python
class DisplayClusterConfigurationICVFX_LightcardRenderSettings(StructBase)
```

Display Cluster Configuration ICVFX Lightcard Render Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_render_settings`` (DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings):  [Read-Write] Advanced render settings
- ``generate_mips`` (DisplayClusterConfigurationPostRender_GenerateMips):  [Read-Write]
- ``replace`` (DisplayClusterConfigurationPostRender_Override):  [Read-Write] Override viewport render from source texture
- ``replace_viewport`` (bool):  [Read-Write] override the texture of the target viewport from this lightcard RTT

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.__init__"></a>

#### __init__

```python
def __init__(
    replace_viewport: bool = False,
    replace: DisplayClusterConfigurationPostRender_Override = [
        False, None, False, [[0, 0], [0, 0]]
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

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.replace_viewport"></a>

#### replace_viewport

```python
@property
def replace_viewport() -> bool
```

(bool):  [Read-Write] override the texture of the target viewport from this lightcard RTT

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.replace_viewport"></a>

#### replace_viewport

```python
@replace_viewport.setter
def replace_viewport(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.replace"></a>

#### replace

```python
@property
def replace() -> DisplayClusterConfigurationPostRender_Override
```

(DisplayClusterConfigurationPostRender_Override):  [Read-Write] Override viewport render from source texture

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.replace"></a>

#### replace

```python
@replace.setter
def replace(value: DisplayClusterConfigurationPostRender_Override) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.generate_mips"></a>

#### generate_mips

```python
@property
def generate_mips() -> DisplayClusterConfigurationPostRender_GenerateMips
```

(DisplayClusterConfigurationPostRender_GenerateMips):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.generate_mips"></a>

#### generate_mips

```python
@generate_mips.setter
def generate_mips(
        value: DisplayClusterConfigurationPostRender_GenerateMips) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.advanced_render_settings"></a>

#### advanced_render_settings

```python
@property
def advanced_render_settings(
) -> DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings
```

(DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings):  [Read-Write] Advanced render settings

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardRenderSettings.advanced_render_settings"></a>

#### advanced_render_settings

```python
@advanced_render_settings.setter
def advanced_render_settings(
    value: DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings"></a>