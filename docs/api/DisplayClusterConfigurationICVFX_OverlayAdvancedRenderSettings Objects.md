## DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings Objects

```python
class DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings(
        StructBase)
```

Display Cluster Configuration ICVFX Overlay Advanced Render Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_ratio`` (float):  [Read-Write] Allow ScreenPercentage
- ``gpu_index`` (int32):  [Read-Write] Specifies the GPU index for the ICVFX viewport (LC or CK).
  A value of '-1' means using the same GPU index as defined in the base viewport:
  - The In-Camera viewport is used as the base viewport for the Chromakey (CK) viewport.
  - An outer viewport is used as the base viewport for the Light Card (LC) viewport.
  Used to improve rendering performance by spreading the load across multiple GPUs.
- ``render_target_ratio`` (float):  [Read-Write] Performance: Render to scale RTT, resolved with shader to viewport (Custom value)
- ``stereo_gpu_index`` (int32):  [Read-Write] Specifies the GPU index for the ICVFX viewport (LC or CK) in stereo rendering for the second eye.
  A value of '-1' means to use the value from the GPU Index parameter. (the same value is used for both eyes).
  Used to improve rendering performance by spreading the load across multiple GPUs.
- ``stereo_mode`` (DisplayClusterConfigurationViewport_StereoMode):  [Read-Write] Performance: force monoscopic render, resolved to stereo viewport

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.__init__"></a>

#### __init__

```python
def __init__(
    buffer_ratio: float = 0.000000,
    render_target_ratio: float = 0.000000,
    gpu_index: int = 0,
    stereo_gpu_index: int = 0,
    stereo_mode:
    DisplayClusterConfigurationViewport_StereoMode = DisplayClusterConfigurationViewport_StereoMode
    .DEFAULT
) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.buffer_ratio"></a>

#### buffer_ratio

```python
@property
def buffer_ratio() -> float
```

(float):  [Read-Write] Allow ScreenPercentage

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.buffer_ratio"></a>

#### buffer_ratio

```python
@buffer_ratio.setter
def buffer_ratio(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.render_target_ratio"></a>

#### render_target_ratio

```python
@property
def render_target_ratio() -> float
```

(float):  [Read-Write] Performance: Render to scale RTT, resolved with shader to viewport (Custom value)

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.render_target_ratio"></a>

#### render_target_ratio

```python
@render_target_ratio.setter
def render_target_ratio(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.gpu_index"></a>

#### gpu_index

```python
@property
def gpu_index() -> int
```

(int32):  [Read-Write] Specifies the GPU index for the ICVFX viewport (LC or CK).
A value of '-1' means using the same GPU index as defined in the base viewport:
- The In-Camera viewport is used as the base viewport for the Chromakey (CK) viewport.
- An outer viewport is used as the base viewport for the Light Card (LC) viewport.
Used to improve rendering performance by spreading the load across multiple GPUs.

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.gpu_index"></a>

#### gpu_index

```python
@gpu_index.setter
def gpu_index(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.stereo_gpu_index"></a>

#### stereo_gpu_index

```python
@property
def stereo_gpu_index() -> int
```

(int32):  [Read-Write] Specifies the GPU index for the ICVFX viewport (LC or CK) in stereo rendering for the second eye.
A value of '-1' means to use the value from the GPU Index parameter. (the same value is used for both eyes).
Used to improve rendering performance by spreading the load across multiple GPUs.

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.stereo_gpu_index"></a>

#### stereo_gpu_index

```python
@stereo_gpu_index.setter
def stereo_gpu_index(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.stereo_mode"></a>

#### stereo_mode

```python
@property
def stereo_mode() -> DisplayClusterConfigurationViewport_StereoMode
```

(DisplayClusterConfigurationViewport_StereoMode):  [Read-Write] Performance: force monoscopic render, resolved to stereo viewport

<a id="unreal.DisplayClusterConfigurationICVFX_OverlayAdvancedRenderSettings.stereo_mode"></a>

#### stereo_mode

```python
@stereo_mode.setter
def stereo_mode(value: DisplayClusterConfigurationViewport_StereoMode) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyRenderSettings"></a>