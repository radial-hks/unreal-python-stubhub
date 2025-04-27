## DisplayClusterConfigurationViewport_PerViewportColorGrading Objects

```python
class DisplayClusterConfigurationViewport_PerViewportColorGrading(StructBase)
```

Display Cluster Configuration Viewport Per Viewport Color Grading

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_post_process_to_objects`` (Array[str]):  [Read-Write] Specify the viewports to apply these color grading settings.
- ``color_grading_settings`` (DisplayClusterConfigurationViewport_ColorGradingRenderingSettings):  [Read-Write] Color Grading
- ``is_enabled`` (bool):  [Read-Write] Enable the color grading settings for the viewport(s) specified and add them to nDisplay's color grading stack.  This will not affect the inner frustum.
- ``is_entire_cluster_enabled`` (bool):  [Read-Write] Optionally include the Entire Cluster Color Grading settings specified above in nDisplay's color grading stack for these viewports.
- ``name`` (Text):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading.__init__"></a>

#### __init__

```python
def __init__(
        is_enabled: bool = False,
        is_entire_cluster_enabled: bool = False,
        color_grading_settings:
    DisplayClusterConfigurationViewport_ColorGradingRenderingSettings = [
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
    ],
        apply_post_process_to_objects: Array[str] = []) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Write] Enable the color grading settings for the viewport(s) specified and add them to nDisplay's color grading stack.  This will not affect the inner frustum.

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading.is_enabled"></a>

#### is_enabled

```python
@is_enabled.setter
def is_enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading.is_entire_cluster_enabled"></a>

#### is_entire_cluster_enabled

```python
@property
def is_entire_cluster_enabled() -> bool
```

(bool):  [Read-Write] Optionally include the Entire Cluster Color Grading settings specified above in nDisplay's color grading stack for these viewports.

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading.is_entire_cluster_enabled"></a>

#### is_entire_cluster_enabled

```python
@is_entire_cluster_enabled.setter
def is_entire_cluster_enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading.color_grading_settings"></a>

#### color_grading_settings

```python
@property
def color_grading_settings(
) -> DisplayClusterConfigurationViewport_ColorGradingRenderingSettings
```

(DisplayClusterConfigurationViewport_ColorGradingRenderingSettings):  [Read-Write] Color Grading

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading.color_grading_settings"></a>

#### color_grading_settings

```python
@color_grading_settings.setter
def color_grading_settings(
    value: DisplayClusterConfigurationViewport_ColorGradingRenderingSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerViewportColorGrading.apply_post_process_to_objects"></a>

#### apply_post_process_to_objects

```python
@property
def apply_post_process_to_objects() -> Array[str]
```

(Array[str]):  [Read-Only] Specify the viewports to apply these color grading settings.

<a id="unreal.DisplayClusterConfigurationViewport_EntireClusterColorGrading"></a>