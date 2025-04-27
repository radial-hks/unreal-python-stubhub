## DisplayClusterConfigurationICVFX_StageSettings Objects

```python
class DisplayClusterConfigurationICVFX_StageSettings(StructBase)
```

Display Cluster Configuration ICVFX Stage Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_frame_size`` (DisplayClusterConfigurationICVFX_Size):  [Read-Write] Default In-Cameras texture resolution.
- ``enable_color_grading`` (bool):  [Read-Write] Viewport Color Grading
- ``enable_inner_frustum_chromakey_overlap`` (bool):  [Read-Write] Render the chromakey where the inner frustum overlaps.
- ``enable_inner_frustums`` (bool):  [Read-Write] Enable/disable the inner frustum on all ICVFX cameras.
- ``entire_cluster_color_grading`` (DisplayClusterConfigurationViewport_EntireClusterColorGrading):  [Read-Write] Entire Cluster Color Grading
- ``freeze_render_outer_viewports`` (bool):  [Read-Write] Freeze rendering for viewports. This improves performance.
- ``global_chromakey`` (DisplayClusterConfigurationICVFX_GlobalChromakeySettings):  [Read-Write] Global chromakey settings that all ICVFX camera components can opt to use
- ``hide_list`` (DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will not appear anywhere in the nDisplay cluster
- ``lightcard`` (DisplayClusterConfigurationICVFX_LightcardSettings):  [Read-Write]
- ``outer_viewport_hide_list`` (DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will not appear in the nDisplay viewports, but can appear in the inner frustum.
- ``per_viewport_color_grading`` (Array[DisplayClusterConfigurationViewport_PerViewportColorGrading]):  [Read-Write] Perform advanced color grading operations on a per-viewport or group-of-viewports basis.
- ``viewport_ocio`` (DisplayClusterConfigurationICVFX_ViewportOCIO):  [Read-Write] OpenColorIO configuration for the Outer viewports.

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.__init__"></a>

#### __init__

```python
def __init__(
    enable_inner_frustums: bool = False,
    enable_inner_frustum_chromakey_overlap: bool = False,
    default_frame_size: DisplayClusterConfigurationICVFX_Size = [
        2560, 1440, True
    ],
    lightcard: DisplayClusterConfigurationICVFX_LightcardSettings = [
        True, True, DisplayClusterConfigurationICVFX_LightcardRenderMode.UNDER,
        [[], [], []],
        [
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
        [
            DisplayClusterConfigurationViewportLightcardOCIOMode.N_DISPLAY,
            [[
                False,
                [
                    None, ["", -1, ""], ["", -1, ""], ["", ""],
                    OpenColorIOViewTransformDirection.FORWARD
                ]
            ], []]
        ]
    ],
    freeze_render_outer_viewports: bool = False,
    hide_list: DisplayClusterConfigurationICVFX_VisibilityList = [[], [], []],
    outer_viewport_hide_list: DisplayClusterConfigurationICVFX_VisibilityList = [
        [], [], []
    ],
    enable_color_grading: bool = False,
    entire_cluster_color_grading:
    DisplayClusterConfigurationViewport_EntireClusterColorGrading = [
        True,
        [
            False, False, False, False, 0.000000,
            [
                False, False, False, TemperatureMethod.TEMP_WHITE_BALANCE,
                6500.000000, 0.000000
            ],
            [
                False, False, False, False, False,
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [0.000000, 0.000000, 0.000000, 0.000000]
            ],
            [
                False, False, False, False, False,
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [0.000000, 0.000000, 0.000000, 0.000000]
            ], 0.000000,
            [
                False, False, False, False, False,
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [0.000000, 0.000000, 0.000000, 0.000000]
            ],
            [
                False, False, False, False, False,
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [1.000000, 1.000000, 1.000000, 1.000000],
                [0.000000, 0.000000, 0.000000, 0.000000]
            ], 0.000000, 1.000000,
            [
                False, False, False, 0.000000, 0.000000,
                [0.000000, 0.000000, 0.000000, 0.000000]
            ]
        ]
    ],
    per_viewport_color_grading: Array[
        DisplayClusterConfigurationViewport_PerViewportColorGrading] = [],
    viewport_ocio: DisplayClusterConfigurationICVFX_ViewportOCIO = [[
        False,
        [
            None, ["", -1, ""], ["", -1, ""], ["", ""],
            OpenColorIOViewTransformDirection.FORWARD
        ]
    ], []],
    global_chromakey:
    DisplayClusterConfigurationICVFX_GlobalChromakeySettings = [
        [0.000000, 0.500000, 0.000000, 1.000000],
        [
            True, [0.000000, 0.250000, 0.000000, 1.000000], None, 0.500000,
            1.500000, [0.000000, 0.000000]
        ]
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.enable_inner_frustums"></a>

#### enable_inner_frustums

```python
@property
def enable_inner_frustums() -> bool
```

(bool):  [Read-Write] Enable/disable the inner frustum on all ICVFX cameras.

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.enable_inner_frustums"></a>

#### enable_inner_frustums

```python
@enable_inner_frustums.setter
def enable_inner_frustums(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.enable_inner_frustum_chromakey_overlap"></a>

#### enable_inner_frustum_chromakey_overlap

```python
@property
def enable_inner_frustum_chromakey_overlap() -> bool
```

(bool):  [Read-Write] Render the chromakey where the inner frustum overlaps.

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.enable_inner_frustum_chromakey_overlap"></a>

#### enable_inner_frustum_chromakey_overlap

```python
@enable_inner_frustum_chromakey_overlap.setter
def enable_inner_frustum_chromakey_overlap(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.default_frame_size"></a>

#### default_frame_size

```python
@property
def default_frame_size() -> DisplayClusterConfigurationICVFX_Size
```

(DisplayClusterConfigurationICVFX_Size):  [Read-Write] Default In-Cameras texture resolution.

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.default_frame_size"></a>

#### default_frame_size

```python
@default_frame_size.setter
def default_frame_size(value: DisplayClusterConfigurationICVFX_Size) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.lightcard"></a>

#### lightcard

```python
@property
def lightcard() -> DisplayClusterConfigurationICVFX_LightcardSettings
```

(DisplayClusterConfigurationICVFX_LightcardSettings):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.lightcard"></a>

#### lightcard

```python
@lightcard.setter
def lightcard(
        value: DisplayClusterConfigurationICVFX_LightcardSettings) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.freeze_render_outer_viewports"></a>

#### freeze_render_outer_viewports

```python
@property
def freeze_render_outer_viewports() -> bool
```

(bool):  [Read-Write] Freeze rendering for viewports. This improves performance.

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.freeze_render_outer_viewports"></a>

#### freeze_render_outer_viewports

```python
@freeze_render_outer_viewports.setter
def freeze_render_outer_viewports(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.hide_list"></a>

#### hide_list

```python
@property
def hide_list() -> DisplayClusterConfigurationICVFX_VisibilityList
```

(DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will not appear anywhere in the nDisplay cluster

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.hide_list"></a>

#### hide_list

```python
@hide_list.setter
def hide_list(value: DisplayClusterConfigurationICVFX_VisibilityList) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.outer_viewport_hide_list"></a>

#### outer_viewport_hide_list

```python
@property
def outer_viewport_hide_list(
) -> DisplayClusterConfigurationICVFX_VisibilityList
```

(DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will not appear in the nDisplay viewports, but can appear in the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.outer_viewport_hide_list"></a>

#### outer_viewport_hide_list

```python
@outer_viewport_hide_list.setter
def outer_viewport_hide_list(
        value: DisplayClusterConfigurationICVFX_VisibilityList) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.enable_color_grading"></a>

#### enable_color_grading

```python
@property
def enable_color_grading() -> bool
```

(bool):  [Read-Write] Viewport Color Grading

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.enable_color_grading"></a>

#### enable_color_grading

```python
@enable_color_grading.setter
def enable_color_grading(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.entire_cluster_color_grading"></a>

#### entire_cluster_color_grading

```python
@property
def entire_cluster_color_grading(
) -> DisplayClusterConfigurationViewport_EntireClusterColorGrading
```

(DisplayClusterConfigurationViewport_EntireClusterColorGrading):  [Read-Write] Entire Cluster Color Grading

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.entire_cluster_color_grading"></a>

#### entire_cluster_color_grading

```python
@entire_cluster_color_grading.setter
def entire_cluster_color_grading(
    value: DisplayClusterConfigurationViewport_EntireClusterColorGrading
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.per_viewport_color_grading"></a>

#### per_viewport_color_grading

```python
@property
def per_viewport_color_grading(
) -> Array[DisplayClusterConfigurationViewport_PerViewportColorGrading]
```

(Array[DisplayClusterConfigurationViewport_PerViewportColorGrading]):  [Read-Write] Perform advanced color grading operations on a per-viewport or group-of-viewports basis.

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.per_viewport_color_grading"></a>

#### per_viewport_color_grading

```python
@per_viewport_color_grading.setter
def per_viewport_color_grading(
    value: Array[DisplayClusterConfigurationViewport_PerViewportColorGrading]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.viewport_ocio"></a>

#### viewport_ocio

```python
@property
def viewport_ocio() -> DisplayClusterConfigurationICVFX_ViewportOCIO
```

(DisplayClusterConfigurationICVFX_ViewportOCIO):  [Read-Write] OpenColorIO configuration for the Outer viewports.

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.viewport_ocio"></a>

#### viewport_ocio

```python
@viewport_ocio.setter
def viewport_ocio(
        value: DisplayClusterConfigurationICVFX_ViewportOCIO) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.global_chromakey"></a>

#### global_chromakey

```python
@property
def global_chromakey(
) -> DisplayClusterConfigurationICVFX_GlobalChromakeySettings
```

(DisplayClusterConfigurationICVFX_GlobalChromakeySettings):  [Read-Write] Global chromakey settings that all ICVFX camera components can opt to use

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings.global_chromakey"></a>

#### global_chromakey

```python
@global_chromakey.setter
def global_chromakey(
        value: DisplayClusterConfigurationICVFX_GlobalChromakeySettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading"></a>