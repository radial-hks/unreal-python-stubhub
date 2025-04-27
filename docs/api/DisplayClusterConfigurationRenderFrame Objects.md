## DisplayClusterConfigurationRenderFrame Objects

```python
class DisplayClusterConfigurationRenderFrame(StructBase)
```

This struct now stored in UDisplayClusterConfigurationData, and replicated with MultiUser

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Viewport.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_warp_blend`` (bool):  [Read-Write] Allow warpblend render
- ``cluster_buffer_ratio_mult`` (float):  [Read-Write] Multiplies all screen percentages within nDisplay by this value.
- ``cluster_icvfx_inner_frustum_buffer_ratio_mult`` (float):  [Read-Write] Multiplies the screen percentage for all ICVFX Inner Frustum viewports by this value.
- ``cluster_icvfx_inner_viewport_render_target_ratio_mult`` (float):  [Read-Write] Multiplies the RTT size of the ICVFX Inner Frustum viewports by this value.
- ``cluster_icvfx_outer_viewport_buffer_ratio_mult`` (float):  [Read-Write] Multiplies the screen percentage for viewports by this value.
  (Excluding ICVFX internal viewports such as Inner Frustum, LightCards and Chromakey.)
- ``cluster_icvfx_outer_viewport_render_target_ratio_mult`` (float):  [Read-Write] Multiplies the RTT size of the viewports by this value.
  (Excluding ICVFX internal viewports such as Inner frustum, LightCards, Chromakey, etc.)
- ``cluster_render_target_ratio_mult`` (float):  [Read-Write] Multiplies the RTT size of all viewports within nDisplay by this value.

<a id="unreal.DisplayClusterConfigurationRenderFrame.__init__"></a>

#### __init__

```python
def __init__(
        cluster_render_target_ratio_mult: float = 0.000000,
        cluster_icvfx_inner_viewport_render_target_ratio_mult: float = 0.000000,
        cluster_icvfx_outer_viewport_render_target_ratio_mult: float = 0.000000,
        cluster_buffer_ratio_mult: float = 0.000000,
        cluster_icvfx_inner_frustum_buffer_ratio_mult: float = 0.000000,
        cluster_icvfx_outer_viewport_buffer_ratio_mult: float = 0.000000,
        allow_warp_blend: bool = False) -> None
```

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_render_target_ratio_mult"></a>

#### cluster_render_target_ratio_mult

```python
@property
def cluster_render_target_ratio_mult() -> float
```

(float):  [Read-Write] Multiplies the RTT size of all viewports within nDisplay by this value.

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_render_target_ratio_mult"></a>

#### cluster_render_target_ratio_mult

```python
@cluster_render_target_ratio_mult.setter
def cluster_render_target_ratio_mult(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_icvfx_inner_viewport_render_target_ratio_mult"></a>

#### cluster_icvfx_inner_viewport_render_target_ratio_mult

```python
@property
def cluster_icvfx_inner_viewport_render_target_ratio_mult() -> float
```

(float):  [Read-Write] Multiplies the RTT size of the ICVFX Inner Frustum viewports by this value.

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_icvfx_inner_viewport_render_target_ratio_mult"></a>

#### cluster_icvfx_inner_viewport_render_target_ratio_mult

```python
@cluster_icvfx_inner_viewport_render_target_ratio_mult.setter
def cluster_icvfx_inner_viewport_render_target_ratio_mult(
        value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_icvfx_outer_viewport_render_target_ratio_mult"></a>

#### cluster_icvfx_outer_viewport_render_target_ratio_mult

```python
@property
def cluster_icvfx_outer_viewport_render_target_ratio_mult() -> float
```

(float):  [Read-Write] Multiplies the RTT size of the viewports by this value.
(Excluding ICVFX internal viewports such as Inner frustum, LightCards, Chromakey, etc.)

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_icvfx_outer_viewport_render_target_ratio_mult"></a>

#### cluster_icvfx_outer_viewport_render_target_ratio_mult

```python
@cluster_icvfx_outer_viewport_render_target_ratio_mult.setter
def cluster_icvfx_outer_viewport_render_target_ratio_mult(
        value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_buffer_ratio_mult"></a>

#### cluster_buffer_ratio_mult

```python
@property
def cluster_buffer_ratio_mult() -> float
```

(float):  [Read-Write] Multiplies all screen percentages within nDisplay by this value.

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_buffer_ratio_mult"></a>

#### cluster_buffer_ratio_mult

```python
@cluster_buffer_ratio_mult.setter
def cluster_buffer_ratio_mult(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_icvfx_inner_frustum_buffer_ratio_mult"></a>

#### cluster_icvfx_inner_frustum_buffer_ratio_mult

```python
@property
def cluster_icvfx_inner_frustum_buffer_ratio_mult() -> float
```

(float):  [Read-Write] Multiplies the screen percentage for all ICVFX Inner Frustum viewports by this value.

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_icvfx_inner_frustum_buffer_ratio_mult"></a>

#### cluster_icvfx_inner_frustum_buffer_ratio_mult

```python
@cluster_icvfx_inner_frustum_buffer_ratio_mult.setter
def cluster_icvfx_inner_frustum_buffer_ratio_mult(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_icvfx_outer_viewport_buffer_ratio_mult"></a>

#### cluster_icvfx_outer_viewport_buffer_ratio_mult

```python
@property
def cluster_icvfx_outer_viewport_buffer_ratio_mult() -> float
```

(float):  [Read-Write] Multiplies the screen percentage for viewports by this value.
(Excluding ICVFX internal viewports such as Inner Frustum, LightCards and Chromakey.)

<a id="unreal.DisplayClusterConfigurationRenderFrame.cluster_icvfx_outer_viewport_buffer_ratio_mult"></a>

#### cluster_icvfx_outer_viewport_buffer_ratio_mult

```python
@cluster_icvfx_outer_viewport_buffer_ratio_mult.setter
def cluster_icvfx_outer_viewport_buffer_ratio_mult(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationRenderFrame.allow_warp_blend"></a>

#### allow_warp_blend

```python
@property
def allow_warp_blend() -> bool
```

(bool):  [Read-Write] Allow warpblend render

<a id="unreal.DisplayClusterConfigurationRenderFrame.allow_warp_blend"></a>

#### allow_warp_blend

```python
@allow_warp_blend.setter
def allow_warp_blend(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RemapData"></a>