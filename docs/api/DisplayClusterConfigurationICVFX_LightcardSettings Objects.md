## DisplayClusterConfigurationICVFX_LightcardSettings Objects

```python
class DisplayClusterConfigurationICVFX_LightcardSettings(StructBase)
```

Display Cluster Configuration ICVFX Lightcard Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blendingmode`` (DisplayClusterConfigurationICVFX_LightcardRenderMode):  [Read-Write] Specify how to render Light Cards in relation to the inner frustum.
- ``enable`` (bool):  [Read-Write] Enable Light Cards
- ``ignore_outer_viewports_freezing_for_lightcards`` (bool):  [Read-Write] Enable\Disable freeze rendering for lightcards when outer viewports rendering also freezed. This will impact performance.
- ``lightcard_ocio`` (DisplayClusterConfigurationICVFX_LightcardOCIO):  [Read-Write] OpenColorIO configuration for the lightcards.
- ``render_settings`` (DisplayClusterConfigurationICVFX_LightcardRenderSettings):  [Read-Write] Configure global render settings for this viewport
- ``show_only_list`` (DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will be treated as a Light Card and adhere to the Blending Mode setting

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.__init__"></a>

#### __init__

```python
def __init__(
    enable: bool = False,
    ignore_outer_viewports_freezing_for_lightcards: bool = False,
    blendingmode:
    DisplayClusterConfigurationICVFX_LightcardRenderMode = DisplayClusterConfigurationICVFX_LightcardRenderMode
    .OVER,
    show_only_list: DisplayClusterConfigurationICVFX_VisibilityList = [[], [],
                                                                       []],
    render_settings: DisplayClusterConfigurationICVFX_LightcardRenderSettings = [
        False, [False, None, False, [[0, 0], [0, 0]]],
        [
            False, TextureFilter.TF_TRILINEAR, TextureAddress.TA_CLAMP,
            TextureAddress.TA_CLAMP, False, 0
        ],
        [
            1.000000, 1.000000, -1, -1,
            DisplayClusterConfigurationViewport_StereoMode.DEFAULT
        ]
    ],
    lightcard_ocio: DisplayClusterConfigurationICVFX_LightcardOCIO = [
        DisplayClusterConfigurationViewportLightcardOCIOMode.N_DISPLAY,
        [[
            False,
            [
                None, ["", -1, ""], ["", -1, ""], ["", ""],
                OpenColorIOViewTransformDirection.FORWARD
            ]
        ], []]
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Enable Light Cards

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.ignore_outer_viewports_freezing_for_lightcards"></a>

#### ignore_outer_viewports_freezing_for_lightcards

```python
@property
def ignore_outer_viewports_freezing_for_lightcards() -> bool
```

(bool):  [Read-Write] Enable\Disable freeze rendering for lightcards when outer viewports rendering also freezed. This will impact performance.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.ignore_outer_viewports_freezing_for_lightcards"></a>

#### ignore_outer_viewports_freezing_for_lightcards

```python
@ignore_outer_viewports_freezing_for_lightcards.setter
def ignore_outer_viewports_freezing_for_lightcards(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.blendingmode"></a>

#### blendingmode

```python
@property
def blendingmode() -> DisplayClusterConfigurationICVFX_LightcardRenderMode
```

(DisplayClusterConfigurationICVFX_LightcardRenderMode):  [Read-Write] Specify how to render Light Cards in relation to the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.blendingmode"></a>

#### blendingmode

```python
@blendingmode.setter
def blendingmode(
        value: DisplayClusterConfigurationICVFX_LightcardRenderMode) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.show_only_list"></a>

#### show_only_list

```python
@property
def show_only_list() -> DisplayClusterConfigurationICVFX_VisibilityList
```

(DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will be treated as a Light Card and adhere to the Blending Mode setting

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.show_only_list"></a>

#### show_only_list

```python
@show_only_list.setter
def show_only_list(
        value: DisplayClusterConfigurationICVFX_VisibilityList) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.render_settings"></a>

#### render_settings

```python
@property
def render_settings(
) -> DisplayClusterConfigurationICVFX_LightcardRenderSettings
```

(DisplayClusterConfigurationICVFX_LightcardRenderSettings):  [Read-Write] Configure global render settings for this viewport

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.render_settings"></a>

#### render_settings

```python
@render_settings.setter
def render_settings(
        value: DisplayClusterConfigurationICVFX_LightcardRenderSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.lightcard_ocio"></a>

#### lightcard_ocio

```python
@property
def lightcard_ocio() -> DisplayClusterConfigurationICVFX_LightcardOCIO
```

(DisplayClusterConfigurationICVFX_LightcardOCIO):  [Read-Write] OpenColorIO configuration for the lightcards.

<a id="unreal.DisplayClusterConfigurationICVFX_LightcardSettings.lightcard_ocio"></a>

#### lightcard_ocio

```python
@lightcard_ocio.setter
def lightcard_ocio(
        value: DisplayClusterConfigurationICVFX_LightcardOCIO) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings"></a>