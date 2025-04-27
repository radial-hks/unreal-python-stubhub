## DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS Objects

```python
class DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS(StructBase)
```

Display Cluster Configuration ICVFX Camera Motion Blur Override PPS

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``motion_blur_amount`` (float):  [Read-Write] Strength of motion blur, 0:off.
- ``motion_blur_max`` (float):  [Read-Write] Max distortion caused by motion blur in percent of the screen width, 0:off
- ``motion_blur_per_object_size`` (float):  [Read-Write] The minimum projected screen radius for a primitive to be drawn in the velocity pass.Percentage of screen width, smaller numbers cause more draw calls, default: 4 %
- ``replace_enable`` (bool):  [Read-Write] If enabled, override the overall motion blur settings that would otherwise come from the current post-process volume or Cine Camera.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.__init__"></a>

#### __init__

```python
def __init__(replace_enable: bool = False,
             motion_blur_amount: float = 0.000000,
             motion_blur_max: float = 0.000000,
             motion_blur_per_object_size: float = 0.000000) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.replace_enable"></a>

#### replace_enable

```python
@property
def replace_enable() -> bool
```

(bool):  [Read-Write] If enabled, override the overall motion blur settings that would otherwise come from the current post-process volume or Cine Camera.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.replace_enable"></a>

#### replace_enable

```python
@replace_enable.setter
def replace_enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.motion_blur_amount"></a>

#### motion_blur_amount

```python
@property
def motion_blur_amount() -> float
```

(float):  [Read-Write] Strength of motion blur, 0:off.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.motion_blur_amount"></a>

#### motion_blur_amount

```python
@motion_blur_amount.setter
def motion_blur_amount(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.motion_blur_max"></a>

#### motion_blur_max

```python
@property
def motion_blur_max() -> float
```

(float):  [Read-Write] Max distortion caused by motion blur in percent of the screen width, 0:off

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.motion_blur_max"></a>

#### motion_blur_max

```python
@motion_blur_max.setter
def motion_blur_max(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.motion_blur_per_object_size"></a>

#### motion_blur_per_object_size

```python
@property
def motion_blur_per_object_size() -> float
```

(float):  [Read-Write] The minimum projected screen radius for a primitive to be drawn in the velocity pass.Percentage of screen width, smaller numbers cause more draw calls, default: 4 %

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS.motion_blur_per_object_size"></a>

#### motion_blur_per_object_size

```python
@motion_blur_per_object_size.setter
def motion_blur_per_object_size(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlur"></a>