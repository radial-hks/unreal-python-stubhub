## DisplayClusterConfigurationICVFX_CameraMotionBlur Objects

```python
class DisplayClusterConfigurationICVFX_CameraMotionBlur(StructBase)
```

Display Cluster Configuration ICVFX Camera Motion Blur

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``motion_blur_mode`` (DisplayClusterConfigurationCameraMotionBlurMode):  [Read-Write] Specify the motion blur mode for the inner frustum, correcting for the motion of the camera. Blur due to camera motion will be incorrectly doubled in the physically exposed image if there is already camera blur applied to the inner frustum.
- ``motion_blur_pps`` (DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS):  [Read-Write] Motion Blur Settings Override
- ``translation_scale`` (float):  [Read-Write] Translation Scale

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlur.__init__"></a>

#### __init__

```python
def __init__(
    motion_blur_mode:
    DisplayClusterConfigurationCameraMotionBlurMode = DisplayClusterConfigurationCameraMotionBlurMode
    .OFF,
    translation_scale: float = 0.000000,
    motion_blur_pps:
    DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS = [
        False, 1.000000, 50.000000, 4.000000
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlur.motion_blur_mode"></a>

#### motion_blur_mode

```python
@property
def motion_blur_mode() -> DisplayClusterConfigurationCameraMotionBlurMode
```

(DisplayClusterConfigurationCameraMotionBlurMode):  [Read-Write] Specify the motion blur mode for the inner frustum, correcting for the motion of the camera. Blur due to camera motion will be incorrectly doubled in the physically exposed image if there is already camera blur applied to the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlur.motion_blur_mode"></a>

#### motion_blur_mode

```python
@motion_blur_mode.setter
def motion_blur_mode(
        value: DisplayClusterConfigurationCameraMotionBlurMode) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlur.translation_scale"></a>

#### translation_scale

```python
@property
def translation_scale() -> float
```

(float):  [Read-Write] Translation Scale

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlur.translation_scale"></a>

#### translation_scale

```python
@translation_scale.setter
def translation_scale(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlur.motion_blur_pps"></a>

#### motion_blur_pps

```python
@property
def motion_blur_pps(
) -> DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS
```

(DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS):  [Read-Write] Motion Blur Settings Override

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlur.motion_blur_pps"></a>

#### motion_blur_pps

```python
@motion_blur_pps.setter
def motion_blur_pps(
    value: DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField"></a>