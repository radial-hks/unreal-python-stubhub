## DisplayClusterConfigurationICVFX_ChromakeySettings Objects

```python
class DisplayClusterConfigurationICVFX_ChromakeySettings(StructBase)
```

Display Cluster Configuration ICVFX Chromakey Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chromakey_color`` (LinearColor):  [Read-Write] Chromakey Color
- ``chromakey_markers`` (DisplayClusterConfigurationICVFX_ChromakeyMarkers):  [Read-Write] Display Chromakey Markers to facilitate camera tracking in post production.
- ``chromakey_render_texture`` (DisplayClusterConfigurationICVFX_ChromakeyRenderSettings):  [Read-Write] Configure a custom chromakey based on content that will appear in the inner frustum, rather than the entire inner frustum.
- ``chromakey_settings_source`` (DisplayClusterConfigurationICVFX_ChromakeySettingsSource):  [Read-Write] The source of the chromakey settings, either the settings on the ICVFX camera or the global settings on the root actor
- ``chromakey_type`` (DisplayClusterConfigurationICVFX_ChromakeyType):  [Read-Write] The type of chromakey to use
- ``enable`` (bool):  [Read-Write] Set to True to fill the inner frustum with the specified Chromakey Color.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.__init__"></a>

#### __init__

```python
def __init__(
    enable: bool = False,
    chromakey_type:
    DisplayClusterConfigurationICVFX_ChromakeyType = DisplayClusterConfigurationICVFX_ChromakeyType
    .INNER_FRUSTUM,
    chromakey_settings_source:
    DisplayClusterConfigurationICVFX_ChromakeySettingsSource = DisplayClusterConfigurationICVFX_ChromakeySettingsSource
    .VIEWPORT,
    chromakey_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    chromakey_render_texture:
    DisplayClusterConfigurationICVFX_ChromakeyRenderSettings = [
        False, 1.000000, [[], [], []], [False, None, False, [[0, 0], [0, 0]]],
        [DisplayClusterConfiguration_PostRenderBlur.NONE, 5, 20.000000],
        [
            False, TextureFilter.TF_TRILINEAR, TextureAddress.TA_CLAMP,
            TextureAddress.TA_CLAMP, False, 0
        ],
        [
            1.000000, 1.000000, -1, -1,
            DisplayClusterConfigurationViewport_StereoMode.DEFAULT
        ]
    ],
    chromakey_markers: DisplayClusterConfigurationICVFX_ChromakeyMarkers = [
        True, [0.000000, 0.250000, 0.000000, 1.000000], None, 0.500000,
        1.500000, [0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Set to True to fill the inner frustum with the specified Chromakey Color.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_type"></a>

#### chromakey_type

```python
@property
def chromakey_type() -> DisplayClusterConfigurationICVFX_ChromakeyType
```

(DisplayClusterConfigurationICVFX_ChromakeyType):  [Read-Write] The type of chromakey to use

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_type"></a>

#### chromakey_type

```python
@chromakey_type.setter
def chromakey_type(
        value: DisplayClusterConfigurationICVFX_ChromakeyType) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_settings_source"></a>

#### chromakey_settings_source

```python
@property
def chromakey_settings_source(
) -> DisplayClusterConfigurationICVFX_ChromakeySettingsSource
```

(DisplayClusterConfigurationICVFX_ChromakeySettingsSource):  [Read-Write] The source of the chromakey settings, either the settings on the ICVFX camera or the global settings on the root actor

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_settings_source"></a>

#### chromakey_settings_source

```python
@chromakey_settings_source.setter
def chromakey_settings_source(
        value: DisplayClusterConfigurationICVFX_ChromakeySettingsSource
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_color"></a>

#### chromakey_color

```python
@property
def chromakey_color() -> LinearColor
```

(LinearColor):  [Read-Write] Chromakey Color

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_color"></a>

#### chromakey_color

```python
@chromakey_color.setter
def chromakey_color(value: LinearColor) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_render_texture"></a>

#### chromakey_render_texture

```python
@property
def chromakey_render_texture(
) -> DisplayClusterConfigurationICVFX_ChromakeyRenderSettings
```

(DisplayClusterConfigurationICVFX_ChromakeyRenderSettings):  [Read-Write] Configure a custom chromakey based on content that will appear in the inner frustum, rather than the entire inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_render_texture"></a>

#### chromakey_render_texture

```python
@chromakey_render_texture.setter
def chromakey_render_texture(
        value: DisplayClusterConfigurationICVFX_ChromakeyRenderSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_markers"></a>

#### chromakey_markers

```python
@property
def chromakey_markers() -> DisplayClusterConfigurationICVFX_ChromakeyMarkers
```

(DisplayClusterConfigurationICVFX_ChromakeyMarkers):  [Read-Write] Display Chromakey Markers to facilitate camera tracking in post production.

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeySettings.chromakey_markers"></a>

#### chromakey_markers

```python
@chromakey_markers.setter
def chromakey_markers(
        value: DisplayClusterConfigurationICVFX_ChromakeyMarkers) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_GlobalChromakeySettings"></a>