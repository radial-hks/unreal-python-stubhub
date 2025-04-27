## DisplayClusterConfigurationViewport Objects

```python
class DisplayClusterConfigurationViewport(DisplayClusterConfigurationData_Base
                                          )
```

Display Cluster Configuration Viewport

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Viewport.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_preview_frustum_rendering`` (bool):  [Read-Write]
- ``allow_rendering`` (bool):  [Read-Write] Enables or disables rendering of this specific Viewport
- ``camera`` (str):  [Read-Write] Reference to the nDisplay View Point
- ``display_device_name`` (str):  [Read-Write] Select a display device to use during preview. An empty string will use the default display device
- ``fixed_aspect_ratio`` (bool):  [Read-Write] Locks the Viewport aspect ratio for easier resizing
- ``gpu_index`` (int32):  [Read-Write] Specifies the GPU index for the nDisplay viewport.
  Value '-1' means do not use multi-GPU
  Used to improve rendering performance by spreading the load across multiple GPUs.
- ``icvfx`` (DisplayClusterConfigurationViewport_ICVFX):  [Read-Write] Configure ICVFX for this viewport
- ``is_unlocked`` (bool):  [Read-Write]
- ``is_visible`` (bool):  [Read-Write]
- ``overlap_order`` (int32):  [Read-Write] Allows Viewports to overlap and sets Viewport overlapping order priority
- ``projection_policy`` (DisplayClusterConfigurationProjection):  [Read-Write] Specify your Projection Policy Settings
- ``region`` (DisplayClusterConfigurationRectangle):  [Read-Write] Define the Viewport 2D coordinates
- ``render_settings`` (DisplayClusterConfigurationViewport_RenderSettings):  [Read-Write] Configure render for this viewport
- ``viewport_remap`` (DisplayClusterConfigurationViewport_Remap):  [Read-Write] Define the Viewport Remap settings

<a id="unreal.DisplayClusterConfigurationViewport.allow_rendering"></a>

#### allow_rendering

```python
@property
def allow_rendering() -> bool
```

(bool):  [Read-Write] Enables or disables rendering of this specific Viewport

<a id="unreal.DisplayClusterConfigurationViewport.allow_rendering"></a>

#### allow_rendering

```python
@allow_rendering.setter
def allow_rendering(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.camera"></a>

#### camera

```python
@property
def camera() -> str
```

(str):  [Read-Write] Reference to the nDisplay View Point

<a id="unreal.DisplayClusterConfigurationViewport.camera"></a>

#### camera

```python
@camera.setter
def camera(value: str) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.projection_policy"></a>

#### projection_policy

```python
@property
def projection_policy() -> DisplayClusterConfigurationProjection
```

(DisplayClusterConfigurationProjection):  [Read-Write] Specify your Projection Policy Settings

<a id="unreal.DisplayClusterConfigurationViewport.projection_policy"></a>

#### projection_policy

```python
@projection_policy.setter
def projection_policy(value: DisplayClusterConfigurationProjection) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.allow_preview_frustum_rendering"></a>

#### allow_preview_frustum_rendering

```python
@property
def allow_preview_frustum_rendering() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport.allow_preview_frustum_rendering"></a>

#### allow_preview_frustum_rendering

```python
@allow_preview_frustum_rendering.setter
def allow_preview_frustum_rendering(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.region"></a>

#### region

```python
@property
def region() -> DisplayClusterConfigurationRectangle
```

(DisplayClusterConfigurationRectangle):  [Read-Write] Define the Viewport 2D coordinates

<a id="unreal.DisplayClusterConfigurationViewport.region"></a>

#### region

```python
@region.setter
def region(value: DisplayClusterConfigurationRectangle) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.viewport_remap"></a>

#### viewport_remap

```python
@property
def viewport_remap() -> DisplayClusterConfigurationViewport_Remap
```

(DisplayClusterConfigurationViewport_Remap):  [Read-Write] Define the Viewport Remap settings

<a id="unreal.DisplayClusterConfigurationViewport.viewport_remap"></a>

#### viewport_remap

```python
@viewport_remap.setter
def viewport_remap(value: DisplayClusterConfigurationViewport_Remap) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.overlap_order"></a>

#### overlap_order

```python
@property
def overlap_order() -> int
```

(int32):  [Read-Write] Allows Viewports to overlap and sets Viewport overlapping order priority

<a id="unreal.DisplayClusterConfigurationViewport.overlap_order"></a>

#### overlap_order

```python
@overlap_order.setter
def overlap_order(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.gpu_index"></a>

#### gpu_index

```python
@property
def gpu_index() -> int
```

(int32):  [Read-Write] Specifies the GPU index for the nDisplay viewport.
Value '-1' means do not use multi-GPU
Used to improve rendering performance by spreading the load across multiple GPUs.

<a id="unreal.DisplayClusterConfigurationViewport.gpu_index"></a>

#### gpu_index

```python
@gpu_index.setter
def gpu_index(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.render_settings"></a>

#### render_settings

```python
@property
def render_settings() -> DisplayClusterConfigurationViewport_RenderSettings
```

(DisplayClusterConfigurationViewport_RenderSettings):  [Read-Write] Configure render for this viewport

<a id="unreal.DisplayClusterConfigurationViewport.render_settings"></a>

#### render_settings

```python
@render_settings.setter
def render_settings(
        value: DisplayClusterConfigurationViewport_RenderSettings) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport.icvfx"></a>

#### icvfx

```python
@property
def icvfx() -> DisplayClusterConfigurationViewport_ICVFX
```

(DisplayClusterConfigurationViewport_ICVFX):  [Read-Write] Configure ICVFX for this viewport

<a id="unreal.DisplayClusterConfigurationViewport.icvfx"></a>

#### icvfx

```python
@icvfx.setter
def icvfx(value: DisplayClusterConfigurationViewport_ICVFX) -> None
```

<a id="unreal.EnhancedPlayerMappableKeyProfile"></a>