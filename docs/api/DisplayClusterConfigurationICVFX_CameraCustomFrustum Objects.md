## DisplayClusterConfigurationICVFX_CameraCustomFrustum Objects

```python
class DisplayClusterConfigurationICVFX_CameraCustomFrustum(StructBase)
```

Display Cluster Configuration ICVFX Camera Custom Frustum

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adapt_resolution`` (bool):  [Read-Write] Enable adaptive resolution.
- ``bottom`` (float):  [Read-Write] Pixel/Percent value to alter the frustum to the bottom
- ``enable`` (bool):  [Read-Write] Enable Custom Frustum.
- ``estimated_overscan_resolution`` (IntPoint):  [Read-Only] Expected ICVFX camera resolution when both 'Adapt Resolution' and 'Enable Inner Frustum Overscan' are enabled.
- ``field_of_view_multiplier`` (float):  [Read-Write] Multiply the field of view for the ICVFX camera by this value.  This can increase the overall size of the inner frustum to help provide a buffer against latency when moving the camera.
- ``inner_frustum_resolution`` (IntPoint):  [Read-Only] Real ICVFX camera resolution for current settings.
- ``left`` (float):  [Read-Write] Pixel/Percent value to alter the frustum to the left side
- ``mode`` (DisplayClusterConfigurationViewportCustomFrustumMode):  [Read-Write] Enable/disable inner camera custom frustum and specify units as percent or pixel values.
- ``overscan_pixels_increase`` (float):  [Read-Write] This value shows the ratio of "Overscan Estimated Resolution" pixels to "Frustum Internal Resolution" pixels.
- ``right`` (float):  [Read-Write] Pixel/Percent value to alter the frustum to the right side
- ``top`` (float):  [Read-Write] Pixel/Percent value to alter the frustum to the top

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.__init__"></a>

#### __init__

```python
def __init__(
        estimated_overscan_resolution: IntPoint = [0, 0],
        inner_frustum_resolution: IntPoint = [0, 0],
        overscan_pixels_increase: float = 0.000000,
        enable: bool = False,
        adapt_resolution: bool = False,
        field_of_view_multiplier: float = 0.000000,
        mode:
    DisplayClusterConfigurationViewportCustomFrustumMode = DisplayClusterConfigurationViewportCustomFrustumMode
    .PERCENT,
        left: float = 0.000000,
        right: float = 0.000000,
        top: float = 0.000000,
        bottom: float = 0.000000) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.estimated_overscan_resolution"></a>

#### estimated_overscan_resolution

```python
@property
def estimated_overscan_resolution() -> IntPoint
```

(IntPoint):  [Read-Only] Expected ICVFX camera resolution when both 'Adapt Resolution' and 'Enable Inner Frustum Overscan' are enabled.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.inner_frustum_resolution"></a>

#### inner_frustum_resolution

```python
@property
def inner_frustum_resolution() -> IntPoint
```

(IntPoint):  [Read-Only] Real ICVFX camera resolution for current settings.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.overscan_pixels_increase"></a>

#### overscan_pixels_increase

```python
@property
def overscan_pixels_increase() -> float
```

(float):  [Read-Only] This value shows the ratio of "Overscan Estimated Resolution" pixels to "Frustum Internal Resolution" pixels.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Enable Custom Frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.adapt_resolution"></a>

#### adapt_resolution

```python
@property
def adapt_resolution() -> bool
```

(bool):  [Read-Write] Enable adaptive resolution.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.adapt_resolution"></a>

#### adapt_resolution

```python
@adapt_resolution.setter
def adapt_resolution(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.field_of_view_multiplier"></a>

#### field_of_view_multiplier

```python
@property
def field_of_view_multiplier() -> float
```

(float):  [Read-Write] Multiply the field of view for the ICVFX camera by this value.  This can increase the overall size of the inner frustum to help provide a buffer against latency when moving the camera.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.field_of_view_multiplier"></a>

#### field_of_view_multiplier

```python
@field_of_view_multiplier.setter
def field_of_view_multiplier(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.mode"></a>

#### mode

```python
@property
def mode() -> DisplayClusterConfigurationViewportCustomFrustumMode
```

(DisplayClusterConfigurationViewportCustomFrustumMode):  [Read-Write] Enable/disable inner camera custom frustum and specify units as percent or pixel values.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.mode"></a>

#### mode

```python
@mode.setter
def mode(value: DisplayClusterConfigurationViewportCustomFrustumMode) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.left"></a>

#### left

```python
@property
def left() -> float
```

(float):  [Read-Write] Pixel/Percent value to alter the frustum to the left side

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.left"></a>

#### left

```python
@left.setter
def left(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.right"></a>

#### right

```python
@property
def right() -> float
```

(float):  [Read-Write] Pixel/Percent value to alter the frustum to the right side

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.right"></a>

#### right

```python
@right.setter
def right(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.top"></a>

#### top

```python
@property
def top() -> float
```

(float):  [Read-Write] Pixel/Percent value to alter the frustum to the top

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.top"></a>

#### top

```python
@top.setter
def top(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.bottom"></a>

#### bottom

```python
@property
def bottom() -> float
```

(float):  [Read-Write] Pixel/Percent value to alter the frustum to the bottom

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum.bottom"></a>

#### bottom

```python
@bottom.setter
def bottom(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSettings"></a>