## DisplayClusterConfigurationViewport_AllNodesColorGrading Objects

```python
class DisplayClusterConfigurationViewport_AllNodesColorGrading(StructBase)
```

Display Cluster Configuration Viewport All Nodes Color Grading

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_grading_settings`` (DisplayClusterConfigurationViewport_ColorGradingRenderingSettings):  [Read-Write] Color Grading
- ``enable_entire_cluster_color_grading`` (bool):  [Read-Write] Optionally include Entire Cluster Color Grading settings specified on the root actor in nDisplay's color grading stack for the inner frustum.
- ``enable_inner_frustum_all_nodes_color_grading`` (bool):  [Read-Write] Enable the color grading settings on the inner frustum for the all nodes and add them to nDisplay's color grading stack.

<a id="unreal.DisplayClusterConfigurationViewport_AllNodesColorGrading.__init__"></a>

#### __init__

```python
def __init__(
    enable_inner_frustum_all_nodes_color_grading: bool = False,
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

<a id="unreal.DisplayClusterConfigurationViewport_AllNodesColorGrading.enable_inner_frustum_all_nodes_color_grading"></a>

#### enable_inner_frustum_all_nodes_color_grading

```python
@property
def enable_inner_frustum_all_nodes_color_grading() -> bool
```

(bool):  [Read-Write] Enable the color grading settings on the inner frustum for the all nodes and add them to nDisplay's color grading stack.

<a id="unreal.DisplayClusterConfigurationViewport_AllNodesColorGrading.enable_inner_frustum_all_nodes_color_grading"></a>

#### enable_inner_frustum_all_nodes_color_grading

```python
@enable_inner_frustum_all_nodes_color_grading.setter
def enable_inner_frustum_all_nodes_color_grading(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_AllNodesColorGrading.enable_entire_cluster_color_grading"></a>

#### enable_entire_cluster_color_grading

```python
@property
def enable_entire_cluster_color_grading() -> bool
```

(bool):  [Read-Write] Optionally include Entire Cluster Color Grading settings specified on the root actor in nDisplay's color grading stack for the inner frustum.

<a id="unreal.DisplayClusterConfigurationViewport_AllNodesColorGrading.enable_entire_cluster_color_grading"></a>

#### enable_entire_cluster_color_grading

```python
@enable_entire_cluster_color_grading.setter
def enable_entire_cluster_color_grading(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_AllNodesColorGrading.color_grading_settings"></a>

#### color_grading_settings

```python
@property
def color_grading_settings(
) -> DisplayClusterConfigurationViewport_ColorGradingRenderingSettings
```

(DisplayClusterConfigurationViewport_ColorGradingRenderingSettings):  [Read-Write] Color Grading

<a id="unreal.DisplayClusterConfigurationViewport_AllNodesColorGrading.color_grading_settings"></a>

#### color_grading_settings

```python
@color_grading_settings.setter
def color_grading_settings(
    value: DisplayClusterConfigurationViewport_ColorGradingRenderingSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_StageSettings"></a>