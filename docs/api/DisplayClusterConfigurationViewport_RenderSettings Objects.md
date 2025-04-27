## DisplayClusterConfigurationViewport_RenderSettings Objects

```python
class DisplayClusterConfigurationViewport_RenderSettings(StructBase)
```

Display Cluster Configuration Viewport Render Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Viewport.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_ratio`` (float):  [Read-Write] Adjust resolution scaling for an individual viewport.  Viewport Screen Percentage Multiplier is applied to this value.
- ``enable_cross_gpu_transfer`` (bool):  [Read-Write] Enable cross-GPU transfer for this viewport.
         * It may be disabled in some configurations. For example, when using offscreen rendering with TextureShare,
         * cross-gpu transfer can be disabled for this viewport to improve performance, because when transfer is called,
         * it freezes the GPUs until synchronization is reached.
         * (TextureShare uses its own implementation of the crossGPU transfer for the shared textures.)
- ``generate_mips`` (DisplayClusterConfigurationPostRender_GenerateMips):  [Read-Write] Generate Mips texture for this viewport (used, only if projection policy supports this feature)
- ``media`` (DisplayClusterConfigurationMediaViewport):  [Read-Write] Media settings
- ``overscan`` (DisplayClusterConfigurationViewport_Overscan):  [Read-Write] Render a larger frame than specified in the configuration to achieve continuity across displays when using post-processing effects.
- ``postprocess_blur`` (DisplayClusterConfigurationPostRender_BlurPostprocess):  [Read-Write] Add postprocess blur to viewport
- ``replace`` (DisplayClusterConfigurationPostRender_Override):  [Read-Write] Override viewport render from source texture
- ``stereo_gpu_index`` (int32):  [Read-Write] Specifies the GPU index for the nDisplay viewport in stereo rendering for the second eye.
  A value of '-1' means to use the value from the GPU Index parameter. (the same value is used for both eyes).
  Used to improve rendering performance by spreading the load across multiple GPUs.
- ``stereo_mode`` (DisplayClusterConfigurationViewport_StereoMode):  [Read-Write] Enables and sets Stereo mode

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.__init__"></a>

#### __init__

```python
def __init__(
    enable_cross_gpu_transfer: bool = False,
    stereo_mode:
    DisplayClusterConfigurationViewport_StereoMode = DisplayClusterConfigurationViewport_StereoMode
    .DEFAULT,
    buffer_ratio: float = 0.000000,
    replace: DisplayClusterConfigurationPostRender_Override = [
        False, None, False, [[0, 0], [0, 0]]
    ],
    postprocess_blur: DisplayClusterConfigurationPostRender_BlurPostprocess = [
        DisplayClusterConfiguration_PostRenderBlur.NONE, 5, 20.000000
    ],
    generate_mips: DisplayClusterConfigurationPostRender_GenerateMips = [
        False, TextureFilter.TF_TRILINEAR, TextureAddress.TA_CLAMP,
        TextureAddress.TA_CLAMP, False, 0
    ],
    overscan: DisplayClusterConfigurationViewport_Overscan = [
        False, DisplayClusterConfigurationViewportOverscanMode.PERCENT,
        0.000000, 0.000000, 0.000000, 0.000000, True
    ],
    media: DisplayClusterConfigurationMediaViewport = [False, [None],
                                                       []]) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.enable_cross_gpu_transfer"></a>

#### enable_cross_gpu_transfer

```python
@property
def enable_cross_gpu_transfer() -> bool
```

(bool):  [Read-Write] Enable cross-GPU transfer for this viewport.
       * It may be disabled in some configurations. For example, when using offscreen rendering with TextureShare,
       * cross-gpu transfer can be disabled for this viewport to improve performance, because when transfer is called,
       * it freezes the GPUs until synchronization is reached.
       * (TextureShare uses its own implementation of the crossGPU transfer for the shared textures.)

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.enable_cross_gpu_transfer"></a>

#### enable_cross_gpu_transfer

```python
@enable_cross_gpu_transfer.setter
def enable_cross_gpu_transfer(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.stereo_mode"></a>

#### stereo_mode

```python
@property
def stereo_mode() -> DisplayClusterConfigurationViewport_StereoMode
```

(DisplayClusterConfigurationViewport_StereoMode):  [Read-Write] Enables and sets Stereo mode

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.stereo_mode"></a>

#### stereo_mode

```python
@stereo_mode.setter
def stereo_mode(value: DisplayClusterConfigurationViewport_StereoMode) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.buffer_ratio"></a>

#### buffer_ratio

```python
@property
def buffer_ratio() -> float
```

(float):  [Read-Write] Adjust resolution scaling for an individual viewport.  Viewport Screen Percentage Multiplier is applied to this value.

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.buffer_ratio"></a>

#### buffer_ratio

```python
@buffer_ratio.setter
def buffer_ratio(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.replace"></a>

#### replace

```python
@property
def replace() -> DisplayClusterConfigurationPostRender_Override
```

(DisplayClusterConfigurationPostRender_Override):  [Read-Write] Override viewport render from source texture

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.replace"></a>

#### replace

```python
@replace.setter
def replace(value: DisplayClusterConfigurationPostRender_Override) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.postprocess_blur"></a>

#### postprocess_blur

```python
@property
def postprocess_blur(
) -> DisplayClusterConfigurationPostRender_BlurPostprocess
```

(DisplayClusterConfigurationPostRender_BlurPostprocess):  [Read-Write] Add postprocess blur to viewport

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.postprocess_blur"></a>

#### postprocess_blur

```python
@postprocess_blur.setter
def postprocess_blur(
        value: DisplayClusterConfigurationPostRender_BlurPostprocess) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.generate_mips"></a>

#### generate_mips

```python
@property
def generate_mips() -> DisplayClusterConfigurationPostRender_GenerateMips
```

(DisplayClusterConfigurationPostRender_GenerateMips):  [Read-Write] Generate Mips texture for this viewport (used, only if projection policy supports this feature)

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.generate_mips"></a>

#### generate_mips

```python
@generate_mips.setter
def generate_mips(
        value: DisplayClusterConfigurationPostRender_GenerateMips) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.overscan"></a>

#### overscan

```python
@property
def overscan() -> DisplayClusterConfigurationViewport_Overscan
```

(DisplayClusterConfigurationViewport_Overscan):  [Read-Write] Render a larger frame than specified in the configuration to achieve continuity across displays when using post-processing effects.

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.overscan"></a>

#### overscan

```python
@overscan.setter
def overscan(value: DisplayClusterConfigurationViewport_Overscan) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.media"></a>

#### media

```python
@property
def media() -> DisplayClusterConfigurationMediaViewport
```

(DisplayClusterConfigurationMediaViewport):  [Read-Write] Media settings

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings.media"></a>

#### media

```python
@media.setter
def media(value: DisplayClusterConfigurationMediaViewport) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_Overscan"></a>