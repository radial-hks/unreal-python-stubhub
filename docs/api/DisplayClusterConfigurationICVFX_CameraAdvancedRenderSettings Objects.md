## DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings Objects

```python
class DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings(
        StructBase)
```

Display Cluster Configuration ICVFX Camera Advanced Render Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gpu_index`` (int32):  [Read-Write] Specifies the GPU index for the ICVFX camera viewport.
  Value '-1' means do not use multi-GPU
  Used to improve rendering performance by spreading the load across multiple GPUs.
- ``render_target_ratio`` (float):  [Read-Write] Performance: Render to scale RTT, resolved with shader to viewport (Custom value)
- ``stereo_gpu_index`` (int32):  [Read-Write] Specifies the GPU index for the ICVFX camera viewport in stereo rendering for the second eye.
  A value of '-1' means to use the value from the GPU Index parameter. (the same value is used for both eyes).
  Used to improve rendering performance by spreading the load across multiple GPUs.
- ``stereo_mode`` (DisplayClusterConfigurationViewport_StereoMode):  [Read-Write] Performance: force monoscopic render, resolved to stereo viewport

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.__init__"></a>

#### __init__

```python
def __init__(
    render_target_ratio: float = 0.000000,
    gpu_index: int = 0,
    stereo_gpu_index: int = 0,
    stereo_mode:
    DisplayClusterConfigurationViewport_StereoMode = DisplayClusterConfigurationViewport_StereoMode
    .DEFAULT
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.render_target_ratio"></a>

#### render_target_ratio

```python
@property
def render_target_ratio() -> float
```

(float):  [Read-Write] Performance: Render to scale RTT, resolved with shader to viewport (Custom value)

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.render_target_ratio"></a>

#### render_target_ratio

```python
@render_target_ratio.setter
def render_target_ratio(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.gpu_index"></a>

#### gpu_index

```python
@property
def gpu_index() -> int
```

(int32):  [Read-Write] Specifies the GPU index for the ICVFX camera viewport.
Value '-1' means do not use multi-GPU
Used to improve rendering performance by spreading the load across multiple GPUs.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.gpu_index"></a>

#### gpu_index

```python
@gpu_index.setter
def gpu_index(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.stereo_gpu_index"></a>

#### stereo_gpu_index

```python
@property
def stereo_gpu_index() -> int
```

(int32):  [Read-Write] Specifies the GPU index for the ICVFX camera viewport in stereo rendering for the second eye.
A value of '-1' means to use the value from the GPU Index parameter. (the same value is used for both eyes).
Used to improve rendering performance by spreading the load across multiple GPUs.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.stereo_gpu_index"></a>

#### stereo_gpu_index

```python
@stereo_gpu_index.setter
def stereo_gpu_index(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.stereo_mode"></a>

#### stereo_mode

```python
@property
def stereo_mode() -> DisplayClusterConfigurationViewport_StereoMode
```

(DisplayClusterConfigurationViewport_StereoMode):  [Read-Write] Performance: force monoscopic render, resolved to stereo viewport

<a id="unreal.DisplayClusterConfigurationICVFX_CameraAdvancedRenderSettings.stereo_mode"></a>

#### stereo_mode

```python
@stereo_mode.setter
def stereo_mode(value: DisplayClusterConfigurationViewport_StereoMode) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraRenderSettings"></a>