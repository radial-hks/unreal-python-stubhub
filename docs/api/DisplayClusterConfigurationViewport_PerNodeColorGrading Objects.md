## DisplayClusterConfigurationViewport_PerNodeColorGrading Objects

```python
class DisplayClusterConfigurationViewport_PerNodeColorGrading(StructBase)
```

Display Cluster Configuration Viewport Per Node Color Grading

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``all_nodes_color_grading`` (bool):  [Read-Write] Optionally include the All Nodes Color Grading settings specified above in nDisplay's color grading stack for these nodes.
- ``apply_post_process_to_objects`` (Array[str]):  [Read-Write] Specify the nodes to apply these color grading settings.
- ``color_grading_settings`` (DisplayClusterConfigurationViewport_ColorGradingRenderingSettings):  [Read-Write] Color Grading
- ``entire_cluster_color_grading`` (bool):  [Read-Write] Optionally include Entire Cluster Color Grading settings specified on the root actor in nDisplay's color grading stack for these nodes.
- ``is_enabled`` (bool):  [Read-Write] Enable the color grading settings for the node(s) specified and add them to nDisplay's color grading stack.
- ``name`` (Text):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.__init__"></a>

#### __init__

```python
def __init__(
        is_enabled: bool = False,
        entire_cluster_color_grading: bool = False,
        all_nodes_color_grading: bool = False,
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

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Write] Enable the color grading settings for the node(s) specified and add them to nDisplay's color grading stack.

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.is_enabled"></a>

#### is_enabled

```python
@is_enabled.setter
def is_enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.entire_cluster_color_grading"></a>

#### entire_cluster_color_grading

```python
@property
def entire_cluster_color_grading() -> bool
```

(bool):  [Read-Write] Optionally include Entire Cluster Color Grading settings specified on the root actor in nDisplay's color grading stack for these nodes.

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.entire_cluster_color_grading"></a>

#### entire_cluster_color_grading

```python
@entire_cluster_color_grading.setter
def entire_cluster_color_grading(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.all_nodes_color_grading"></a>

#### all_nodes_color_grading

```python
@property
def all_nodes_color_grading() -> bool
```

(bool):  [Read-Write] Optionally include the All Nodes Color Grading settings specified above in nDisplay's color grading stack for these nodes.

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.all_nodes_color_grading"></a>

#### all_nodes_color_grading

```python
@all_nodes_color_grading.setter
def all_nodes_color_grading(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.color_grading_settings"></a>

#### color_grading_settings

```python
@property
def color_grading_settings(
) -> DisplayClusterConfigurationViewport_ColorGradingRenderingSettings
```

(DisplayClusterConfigurationViewport_ColorGradingRenderingSettings):  [Read-Write] Color Grading

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.color_grading_settings"></a>

#### color_grading_settings

```python
@color_grading_settings.setter
def color_grading_settings(
    value: DisplayClusterConfigurationViewport_ColorGradingRenderingSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading.apply_post_process_to_objects"></a>

#### apply_post_process_to_objects

```python
@property
def apply_post_process_to_objects() -> Array[str]
```

(Array[str]):  [Read-Only] Specify the nodes to apply these color grading settings.

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings"></a>