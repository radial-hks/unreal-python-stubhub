## DisplayClusterConfigurationViewport_ICVFX Objects

```python
class DisplayClusterConfigurationViewport_ICVFX(StructBase)
```

Display Cluster Configuration Viewport ICVFX

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Viewport.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_icvfx`` (bool):  [Read-Write] Enable in-camera VFX for this Viewport (works only with supported Projection Policies)
- ``allow_inner_frustum`` (bool):  [Read-Write] Allow the inner frustum to appear on this Viewport
- ``camera_render_mode`` (DisplayClusterConfigurationICVFX_OverrideCameraRenderMode):  [Read-Write] Disable incamera render to this viewport
- ``lightcard_render_mode`` (DisplayClusterConfigurationICVFX_OverrideLightcardRenderMode):  [Read-Write] Use unique lightcard mode for this viewport

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.__init__"></a>

#### __init__

```python
def __init__(
    allow_icvfx: bool = False,
    allow_inner_frustum: bool = False,
    camera_render_mode:
    DisplayClusterConfigurationICVFX_OverrideCameraRenderMode = DisplayClusterConfigurationICVFX_OverrideCameraRenderMode
    .DEFAULT,
    lightcard_render_mode:
    DisplayClusterConfigurationICVFX_OverrideLightcardRenderMode = DisplayClusterConfigurationICVFX_OverrideLightcardRenderMode
    .DEFAULT
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.allow_icvfx"></a>

#### allow_icvfx

```python
@property
def allow_icvfx() -> bool
```

(bool):  [Read-Write] Enable in-camera VFX for this Viewport (works only with supported Projection Policies)

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.allow_icvfx"></a>

#### allow_icvfx

```python
@allow_icvfx.setter
def allow_icvfx(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.allow_inner_frustum"></a>

#### allow_inner_frustum

```python
@property
def allow_inner_frustum() -> bool
```

(bool):  [Read-Write] Allow the inner frustum to appear on this Viewport

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.allow_inner_frustum"></a>

#### allow_inner_frustum

```python
@allow_inner_frustum.setter
def allow_inner_frustum(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.camera_render_mode"></a>

#### camera_render_mode

```python
@property
def camera_render_mode(
) -> DisplayClusterConfigurationICVFX_OverrideCameraRenderMode
```

(DisplayClusterConfigurationICVFX_OverrideCameraRenderMode):  [Read-Write] Disable incamera render to this viewport

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.camera_render_mode"></a>

#### camera_render_mode

```python
@camera_render_mode.setter
def camera_render_mode(
        value: DisplayClusterConfigurationICVFX_OverrideCameraRenderMode
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.lightcard_render_mode"></a>

#### lightcard_render_mode

```python
@property
def lightcard_render_mode(
) -> DisplayClusterConfigurationICVFX_OverrideLightcardRenderMode
```

(DisplayClusterConfigurationICVFX_OverrideLightcardRenderMode):  [Read-Write] Use unique lightcard mode for this viewport

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX.lightcard_render_mode"></a>

#### lightcard_render_mode

```python
@lightcard_render_mode.setter
def lightcard_render_mode(
    value: DisplayClusterConfigurationICVFX_OverrideLightcardRenderMode
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_RenderSettings"></a>