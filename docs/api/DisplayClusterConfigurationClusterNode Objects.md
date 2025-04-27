## DisplayClusterConfigurationClusterNode Objects

```python
class DisplayClusterConfigurationClusterNode(
        DisplayClusterConfigurationData_Base)
```

Display Cluster Configuration Cluster Node

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_texture_share`` (bool):  [Read-Write] Enables texture sharing for this cluster node
- ``fixed_aspect_ratio`` (bool):  [Read-Write] Locks the application window aspect ratio for easier resizing
- ``graphics_adapter`` (int32):  [Read-Write] Hint for setting the r.GraphicsAdapter CVar when launching this cluster node. Note that this is distinct from the GPU Node Indices assigned to viewports.
- ``host`` (str):  [Read-Write] IP address of this specific cluster Node
- ``is_fullscreen`` (bool):  [Read-Write] Enables application window native fullscreen support
- ``is_sound_enabled`` (bool):  [Read-Write] Enables or disables sound on nDisplay primary Node
- ``is_unlocked`` (bool):  [Read-Write]
- ``is_visible`` (bool):  [Read-Write]
- ``media`` (DisplayClusterConfigurationMediaViewport):  [Read-Write]
  deprecated: This property has been deprecated. Please use 'MediaSettings'.
- ``media_settings`` (DisplayClusterConfigurationMediaNodeBackbuffer):  [Read-Write] Media settings
- ``output_remap`` (DisplayClusterConfigurationFramePostProcess_OutputRemap):  [Read-Write] Output remapping settings for the selected cluster node
- ``postprocess`` (Map[str, DisplayClusterConfigurationPostprocess]):  [Read-Write]
- ``preview_image`` (DisplayClusterConfigurationExternalImage):  [Read-Write] Binds a background preview image for easier output mapping
- ``render_headless`` (bool):  [Read-Write] Activates headless rendering for this cluster node
- ``viewports`` (Map[str, DisplayClusterConfigurationViewport]):  [Read-Write]
- ``window_rect`` (DisplayClusterConfigurationRectangle):  [Read-Write] Defines the application window size in pixels

<a id="unreal.DisplayClusterConfigurationClusterNode.host"></a>

#### host

```python
@property
def host() -> str
```

(str):  [Read-Only] IP address of this specific cluster Node

<a id="unreal.DisplayClusterConfigurationClusterNode.is_sound_enabled"></a>

#### is_sound_enabled

```python
@property
def is_sound_enabled() -> bool
```

(bool):  [Read-Write] Enables or disables sound on nDisplay primary Node

<a id="unreal.DisplayClusterConfigurationClusterNode.is_sound_enabled"></a>

#### is_sound_enabled

```python
@is_sound_enabled.setter
def is_sound_enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationClusterNode.is_fullscreen"></a>

#### is_fullscreen

```python
@property
def is_fullscreen() -> bool
```

(bool):  [Read-Only] Enables application window native fullscreen support

<a id="unreal.DisplayClusterConfigurationClusterNode.window_rect"></a>

#### window_rect

```python
@property
def window_rect() -> DisplayClusterConfigurationRectangle
```

(DisplayClusterConfigurationRectangle):  [Read-Write] Defines the application window size in pixels

<a id="unreal.DisplayClusterConfigurationClusterNode.window_rect"></a>

#### window_rect

```python
@window_rect.setter
def window_rect(value: DisplayClusterConfigurationRectangle) -> None
```

<a id="unreal.DisplayClusterConfigurationClusterNode.output_remap"></a>

#### output_remap

```python
@property
def output_remap() -> DisplayClusterConfigurationFramePostProcess_OutputRemap
```

(DisplayClusterConfigurationFramePostProcess_OutputRemap):  [Read-Write] Output remapping settings for the selected cluster node

<a id="unreal.DisplayClusterConfigurationClusterNode.output_remap"></a>

#### output_remap

```python
@output_remap.setter
def output_remap(
        value: DisplayClusterConfigurationFramePostProcess_OutputRemap
) -> None
```

<a id="unreal.DisplayClusterConfigurationClusterNode.render_headless"></a>

#### render_headless

```python
@property
def render_headless() -> bool
```

(bool):  [Read-Only] Activates headless rendering for this cluster node

<a id="unreal.DisplayClusterConfigurationClusterNode.graphics_adapter"></a>

#### graphics_adapter

```python
@property
def graphics_adapter() -> int
```

(int32):  [Read-Only] Hint for setting the r.GraphicsAdapter CVar when launching this cluster node. Note that this is distinct from the GPU Node Indices assigned to viewports.

<a id="unreal.DisplayClusterConfigurationClusterNode.enable_texture_share"></a>

#### enable_texture_share

```python
@property
def enable_texture_share() -> bool
```

(bool):  [Read-Only] Enables texture sharing for this cluster node

<a id="unreal.DisplayClusterConfigurationClusterNode.viewports"></a>

#### viewports

```python
@property
def viewports() -> Map[str, DisplayClusterConfigurationViewport]
```

(Map[str, DisplayClusterConfigurationViewport]):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationClusterNode.postprocess"></a>

#### postprocess

```python
@property
def postprocess() -> Map[str, DisplayClusterConfigurationPostprocess]
```

(Map[str, DisplayClusterConfigurationPostprocess]):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationClusterNode.media_settings"></a>

#### media_settings

```python
@property
def media_settings() -> DisplayClusterConfigurationMediaNodeBackbuffer
```

(DisplayClusterConfigurationMediaNodeBackbuffer):  [Read-Write] Media settings

<a id="unreal.DisplayClusterConfigurationClusterNode.media_settings"></a>

#### media_settings

```python
@media_settings.setter
def media_settings(
        value: DisplayClusterConfigurationMediaNodeBackbuffer) -> None
```

<a id="unreal.DisplayClusterConfigurationClusterNode.media"></a>

#### media

```python
@property
def media() -> DisplayClusterConfigurationMediaViewport
```

(DisplayClusterConfigurationMediaViewport):  [Read-Write]
deprecated: This property has been deprecated. Please use 'MediaSettings'.

<a id="unreal.DisplayClusterConfigurationClusterNode.media"></a>

#### media

```python
@media.setter
def media(value: DisplayClusterConfigurationMediaViewport) -> None
```

<a id="unreal.DisplayClusterConfigurationClusterNode.get_viewport_ids"></a>

#### get_viewport_ids

```python
def get_viewport_ids() -> Array[str]
```

x.get_viewport_ids() -> Array[str]
Get Viewport Ids

Returns:
    Array[str]: 

    out_viewport_ids (Array[str]):

<a id="unreal.DisplayClusterConfigurationClusterNode.get_viewport"></a>

#### get_viewport

```python
def get_viewport(viewport_id: str) -> DisplayClusterConfigurationViewport
```

x.get_viewport(viewport_id) -> DisplayClusterConfigurationViewport
Get Viewport

Args:
    viewport_id (str): 

Returns:
    DisplayClusterConfigurationViewport:

<a id="unreal.DisplayClusterConfigurationClusterNode.get_referenced_mesh_names"></a>

#### get_referenced_mesh_names

```python
def get_referenced_mesh_names() -> Array[str]
```

x.get_referenced_mesh_names() -> Array[str]
Return all references to meshes from policy, and other

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.DisplayClusterConfigurationHostDisplayData"></a>