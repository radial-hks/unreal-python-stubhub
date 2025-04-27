## DisplayClusterConfigurationViewport_EntireClusterColorGrading Objects

```python
class DisplayClusterConfigurationViewport_EntireClusterColorGrading(
        StructBase)
```

Display Cluster Configuration Viewport Entire Cluster Color Grading

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_grading_settings`` (DisplayClusterConfigurationViewport_ColorGradingRenderingSettings):  [Read-Write] Entire Cluster Color Grading
- ``enable_entire_cluster_color_grading`` (bool):  [Read-Write] Enable the color grading settings for the entire cluster and add them to nDisplay's color grading stack.  This will affect both the viewports and inner frustum.

<a id="unreal.DisplayClusterConfigurationViewport_EntireClusterColorGrading.__init__"></a>

#### __init__

```python
def __init__(
    enable_entire_cluster_color_grading: bool = False,
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
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_EntireClusterColorGrading.enable_entire_cluster_color_grading"></a>

#### enable_entire_cluster_color_grading

```python
@property
def enable_entire_cluster_color_grading() -> bool
```

(bool):  [Read-Write] Enable the color grading settings for the entire cluster and add them to nDisplay's color grading stack.  This will affect both the viewports and inner frustum.

<a id="unreal.DisplayClusterConfigurationViewport_EntireClusterColorGrading.enable_entire_cluster_color_grading"></a>

#### enable_entire_cluster_color_grading

```python
@enable_entire_cluster_color_grading.setter
def enable_entire_cluster_color_grading(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_EntireClusterColorGrading.color_grading_settings"></a>

#### color_grading_settings

```python
@property
def color_grading_settings(
) -> DisplayClusterConfigurationViewport_ColorGradingRenderingSettings
```

(DisplayClusterConfigurationViewport_ColorGradingRenderingSettings):  [Read-Write] Entire Cluster Color Grading

<a id="unreal.DisplayClusterConfigurationViewport_EntireClusterColorGrading.color_grading_settings"></a>

#### color_grading_settings

```python
@color_grading_settings.setter
def color_grading_settings(
    value: DisplayClusterConfigurationViewport_ColorGradingRenderingSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaNodeBackbuffer"></a>