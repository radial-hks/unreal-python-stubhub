## DisplayClusterConfigurationICVFX_CameraSettings Objects

```python
class DisplayClusterConfigurationICVFX_CameraSettings(StructBase)
```

Display Cluster Configuration ICVFX Camera Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``all_nodes_color_grading`` (DisplayClusterConfigurationViewport_AllNodesColorGrading):  [Read-Write] All Nodes Color Grading
- ``border`` (DisplayClusterConfigurationICVFX_CameraBorder):  [Read-Write] Border for the inner frustum.
- ``buffer_ratio`` (float):  [Read-Write] Adjust resolution scaling for the inner frustum.
- ``camera_depth_of_field`` (DisplayClusterConfigurationICVFX_CameraDepthOfField):  [Read-Write] Settings that control the depth of field blur applied to the ICVFX image
- ``camera_hide_list`` (DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will not appear in the inner frustum, but can appear in the nDisplay viewports.
- ``camera_motion_blur`` (DisplayClusterConfigurationICVFX_CameraMotionBlur):  [Read-Write] Render motion blur more accurately by subtracting blur from camera motion and avoiding amplification of blur by the physical camera.
- ``camera_ocio`` (DisplayClusterConfigurationICVFX_CameraOCIO):  [Read-Write]
- ``chromakey`` (DisplayClusterConfigurationICVFX_ChromakeySettings):  [Read-Write]
- ``custom_frustum`` (DisplayClusterConfigurationICVFX_CameraCustomFrustum):  [Read-Write] Render a larger or smaller inner frame
- ``enable`` (bool):  [Read-Write] Render the inner frustum for this ICVFX camera.
- ``enable_inner_frustum_color_grading`` (bool):  [Read-Write] Entire Cluster Color Grading
- ``external_camera_actor`` (CineCameraActor):  [Read-Write] Specify a Cine Camera Actor for this ICVFX camera to use instead of the default nDisplay camera.
- ``frustum_offset`` (Vector):  [Read-Write] Specify an offset on the inner frustum.
- ``frustum_rotation`` (Rotator):  [Read-Write] Rotate the inner frustum.
- ``hidden_icvfx_viewports`` (DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] A list of viewports that the inner frustum is not rendered to.
- ``off_center_projection_offset`` (Vector2D):  [Read-Write] Off-axis / off-center projection offset as proportion of screen dimensions.
- ``per_node_color_grading`` (Array[DisplayClusterConfigurationViewport_PerNodeColorGrading]):  [Read-Write] Perform advanced color grading operations for the inner frustum on a per-node or group-of-nodes basis.
- ``render_settings`` (DisplayClusterConfigurationICVFX_CameraRenderSettings):  [Read-Write] Configure global render settings for this viewport
- ``soft_edge`` (DisplayClusterConfigurationICVFX_CameraSoftEdge):  [Read-Write] Soften the edges of the inner frustum to help avoid hard lines in reflections seen by the live-action camera.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.__init__"></a>

#### __init__

```python
def __init__(
    enable: bool = False,
    external_camera_actor: CineCameraActor = None,
    buffer_ratio: float = 0.000000,
    custom_frustum: DisplayClusterConfigurationICVFX_CameraCustomFrustum = [
        [2560, 1440], [2560, 1440], 0.000000, False, False, 1.000000,
        DisplayClusterConfigurationViewportCustomFrustumMode.PERCENT, 0.000000,
        0.000000, 0.000000, 0.000000
    ],
    soft_edge: DisplayClusterConfigurationICVFX_CameraSoftEdge = [
        0.000000, 0.000000, 1.000000
    ],
    frustum_rotation: Rotator = [0.000000, 0.000000, 0.000000],
    frustum_offset: Vector = [0.000000, 0.000000, 0.000000],
    off_center_projection_offset: Vector2D = [0.000000, 0.000000],
    border: DisplayClusterConfigurationICVFX_CameraBorder = [
        False, 0.050000, [0.000000, 0.000000, 1.000000, 1.000000]
    ],
    camera_motion_blur: DisplayClusterConfigurationICVFX_CameraMotionBlur = [
        DisplayClusterConfigurationCameraMotionBlurMode.OVERRIDE, 1.000000,
        [False, 1.000000, 50.000000, 4.000000]
    ],
    camera_depth_of_field:
    DisplayClusterConfigurationICVFX_CameraDepthOfField = [
        False, True, 0.000000, 0.000000, 1.000000, None
    ],
    render_settings: DisplayClusterConfigurationICVFX_CameraRenderSettings = [
        [False, 2560, 1440, True], -1, True,
        [False, None, False, [[0, 0], [0, 0]]],
        [
            False, DisplayClusterConfigurationMediaSplitType.FULL_FRAME, [],
            [], [1, 1],
            [
                False, True, True,
                DisplayClusterConfigurationViewportOverscanMode.PERCENT,
                10.000000
            ], [[]], [], [], False
        ],
        [
            True, TextureFilter.TF_TRILINEAR, TextureAddress.TA_CLAMP,
            TextureAddress.TA_CLAMP, False, 0
        ],
        [
            1.000000, -1, -1,
            DisplayClusterConfigurationViewport_StereoMode.DEFAULT
        ]
    ],
    chromakey: DisplayClusterConfigurationICVFX_ChromakeySettings = [
        False, DisplayClusterConfigurationICVFX_ChromakeyType.INNER_FRUSTUM,
        DisplayClusterConfigurationICVFX_ChromakeySettingsSource.VIEWPORT,
        [0.000000, 0.500000, 0.000000, 1.000000],
        [
            False, 1.000000, [[], [], []],
            [False, None, False, [[0, 0], [0, 0]]],
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
        [
            True, [0.000000, 0.250000, 0.000000, 1.000000], None, 0.500000,
            1.500000, [0.000000, 0.000000]
        ]
    ],
    camera_ocio: DisplayClusterConfigurationICVFX_CameraOCIO = [[
        False,
        [
            None, ["", -1, ""], ["", -1, ""], ["", ""],
            OpenColorIOViewTransformDirection.FORWARD
        ]
    ], []],
    enable_inner_frustum_color_grading: bool = False,
    all_nodes_color_grading:
    DisplayClusterConfigurationViewport_AllNodesColorGrading = [
        True, True,
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
    per_node_color_grading: Array[
        DisplayClusterConfigurationViewport_PerNodeColorGrading] = [],
    camera_hide_list: DisplayClusterConfigurationICVFX_VisibilityList = [[],
                                                                         [],
                                                                         []],
    hidden_icvfx_viewports:
    DisplayClusterConfigurationClusterItemReferenceList = [[]]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Render the inner frustum for this ICVFX camera.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.external_camera_actor"></a>

#### external_camera_actor

```python
@property
def external_camera_actor() -> CineCameraActor
```

(CineCameraActor):  [Read-Write] Specify a Cine Camera Actor for this ICVFX camera to use instead of the default nDisplay camera.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.external_camera_actor"></a>

#### external_camera_actor

```python
@external_camera_actor.setter
def external_camera_actor(value: CineCameraActor) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.buffer_ratio"></a>

#### buffer_ratio

```python
@property
def buffer_ratio() -> float
```

(float):  [Read-Write] Adjust resolution scaling for the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.buffer_ratio"></a>

#### buffer_ratio

```python
@buffer_ratio.setter
def buffer_ratio(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.custom_frustum"></a>

#### custom_frustum

```python
@property
def custom_frustum() -> DisplayClusterConfigurationICVFX_CameraCustomFrustum
```

(DisplayClusterConfigurationICVFX_CameraCustomFrustum):  [Read-Write] Render a larger or smaller inner frame

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.custom_frustum"></a>

#### custom_frustum

```python
@custom_frustum.setter
def custom_frustum(
        value: DisplayClusterConfigurationICVFX_CameraCustomFrustum) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.soft_edge"></a>

#### soft_edge

```python
@property
def soft_edge() -> DisplayClusterConfigurationICVFX_CameraSoftEdge
```

(DisplayClusterConfigurationICVFX_CameraSoftEdge):  [Read-Write] Soften the edges of the inner frustum to help avoid hard lines in reflections seen by the live-action camera.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.soft_edge"></a>

#### soft_edge

```python
@soft_edge.setter
def soft_edge(value: DisplayClusterConfigurationICVFX_CameraSoftEdge) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.frustum_rotation"></a>

#### frustum_rotation

```python
@property
def frustum_rotation() -> Rotator
```

(Rotator):  [Read-Write] Rotate the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.frustum_rotation"></a>

#### frustum_rotation

```python
@frustum_rotation.setter
def frustum_rotation(value: Rotator) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.frustum_offset"></a>

#### frustum_offset

```python
@property
def frustum_offset() -> Vector
```

(Vector):  [Read-Write] Specify an offset on the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.frustum_offset"></a>

#### frustum_offset

```python
@frustum_offset.setter
def frustum_offset(value: Vector) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.off_center_projection_offset"></a>

#### off_center_projection_offset

```python
@property
def off_center_projection_offset() -> Vector2D
```

(Vector2D):  [Read-Write] Off-axis / off-center projection offset as proportion of screen dimensions.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.off_center_projection_offset"></a>

#### off_center_projection_offset

```python
@off_center_projection_offset.setter
def off_center_projection_offset(value: Vector2D) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.border"></a>

#### border

```python
@property
def border() -> DisplayClusterConfigurationICVFX_CameraBorder
```

(DisplayClusterConfigurationICVFX_CameraBorder):  [Read-Write] Border for the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.border"></a>

#### border

```python
@border.setter
def border(value: DisplayClusterConfigurationICVFX_CameraBorder) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.camera_motion_blur"></a>

#### camera_motion_blur

```python
@property
def camera_motion_blur() -> DisplayClusterConfigurationICVFX_CameraMotionBlur
```

(DisplayClusterConfigurationICVFX_CameraMotionBlur):  [Read-Write] Render motion blur more accurately by subtracting blur from camera motion and avoiding amplification of blur by the physical camera.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.camera_motion_blur"></a>

#### camera_motion_blur

```python
@camera_motion_blur.setter
def camera_motion_blur(
        value: DisplayClusterConfigurationICVFX_CameraMotionBlur) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.camera_depth_of_field"></a>

#### camera_depth_of_field

```python
@property
def camera_depth_of_field(
) -> DisplayClusterConfigurationICVFX_CameraDepthOfField
```

(DisplayClusterConfigurationICVFX_CameraDepthOfField):  [Read-Write] Settings that control the depth of field blur applied to the ICVFX image

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.camera_depth_of_field"></a>

#### camera_depth_of_field

```python
@camera_depth_of_field.setter
def camera_depth_of_field(
        value: DisplayClusterConfigurationICVFX_CameraDepthOfField) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.render_settings"></a>

#### render_settings

```python
@property
def render_settings() -> DisplayClusterConfigurationICVFX_CameraRenderSettings
```

(DisplayClusterConfigurationICVFX_CameraRenderSettings):  [Read-Write] Configure global render settings for this viewport

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.render_settings"></a>

#### render_settings

```python
@render_settings.setter
def render_settings(
        value: DisplayClusterConfigurationICVFX_CameraRenderSettings) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.chromakey"></a>

#### chromakey

```python
@property
def chromakey() -> DisplayClusterConfigurationICVFX_ChromakeySettings
```

(DisplayClusterConfigurationICVFX_ChromakeySettings):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.chromakey"></a>

#### chromakey

```python
@chromakey.setter
def chromakey(
        value: DisplayClusterConfigurationICVFX_ChromakeySettings) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.camera_ocio"></a>

#### camera_ocio

```python
@property
def camera_ocio() -> DisplayClusterConfigurationICVFX_CameraOCIO
```

(DisplayClusterConfigurationICVFX_CameraOCIO):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.camera_ocio"></a>

#### camera_ocio

```python
@camera_ocio.setter
def camera_ocio(value: DisplayClusterConfigurationICVFX_CameraOCIO) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.enable_inner_frustum_color_grading"></a>

#### enable_inner_frustum_color_grading

```python
@property
def enable_inner_frustum_color_grading() -> bool
```

(bool):  [Read-Write] Entire Cluster Color Grading

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.enable_inner_frustum_color_grading"></a>

#### enable_inner_frustum_color_grading

```python
@enable_inner_frustum_color_grading.setter
def enable_inner_frustum_color_grading(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.all_nodes_color_grading"></a>

#### all_nodes_color_grading

```python
@property
def all_nodes_color_grading(
) -> DisplayClusterConfigurationViewport_AllNodesColorGrading
```

(DisplayClusterConfigurationViewport_AllNodesColorGrading):  [Read-Write] All Nodes Color Grading

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.all_nodes_color_grading"></a>

#### all_nodes_color_grading

```python
@all_nodes_color_grading.setter
def all_nodes_color_grading(
        value: DisplayClusterConfigurationViewport_AllNodesColorGrading
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.per_node_color_grading"></a>

#### per_node_color_grading

```python
@property
def per_node_color_grading(
) -> Array[DisplayClusterConfigurationViewport_PerNodeColorGrading]
```

(Array[DisplayClusterConfigurationViewport_PerNodeColorGrading]):  [Read-Write] Perform advanced color grading operations for the inner frustum on a per-node or group-of-nodes basis.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.per_node_color_grading"></a>

#### per_node_color_grading

```python
@per_node_color_grading.setter
def per_node_color_grading(
    value: Array[DisplayClusterConfigurationViewport_PerNodeColorGrading]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.camera_hide_list"></a>

#### camera_hide_list

```python
@property
def camera_hide_list() -> DisplayClusterConfigurationICVFX_VisibilityList
```

(DisplayClusterConfigurationICVFX_VisibilityList):  [Read-Write] Content specified here will not appear in the inner frustum, but can appear in the nDisplay viewports.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.camera_hide_list"></a>

#### camera_hide_list

```python
@camera_hide_list.setter
def camera_hide_list(
        value: DisplayClusterConfigurationICVFX_VisibilityList) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.hidden_icvfx_viewports"></a>

#### hidden_icvfx_viewports

```python
@property
def hidden_icvfx_viewports(
) -> DisplayClusterConfigurationClusterItemReferenceList
```

(DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] A list of viewports that the inner frustum is not rendered to.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings.hidden_icvfx_viewports"></a>

#### hidden_icvfx_viewports

```python
@hidden_icvfx_viewports.setter
def hidden_icvfx_viewports(
        value: DisplayClusterConfigurationClusterItemReferenceList) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_PerNodeColorGrading"></a>