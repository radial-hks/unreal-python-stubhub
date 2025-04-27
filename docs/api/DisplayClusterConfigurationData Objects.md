## DisplayClusterConfigurationData Objects

```python
class DisplayClusterConfigurationData(DisplayClusterConfigurationData_Base)
```

/
 Main configuration data container

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cluster`` (DisplayClusterConfigurationCluster):  [Read-Only]
- ``custom_parameters`` (Map[str, str]):  [Read-Write]
- ``default_frame_size_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``diagnostics`` (DisplayClusterConfigurationDiagnostics):  [Read-Write]
- ``exit_on_esc`` (bool):  [Read-Write]
- ``follow_local_player_camera`` (bool):  [Read-Write]
- ``info`` (DisplayClusterConfigurationInfo):  [Read-Write]
- ``media_settings`` (DisplayClusterConfigurationGlobalMediaSettings):  [Read-Write]
- ``override_transforms_from_external_config`` (bool):  [Read-Write]
- ``override_viewports_from_external_config`` (bool):  [Read-Write]
- ``render_frame_settings`` (DisplayClusterConfigurationRenderFrame):  [Read-Write]
- ``scene`` (DisplayClusterConfigurationScene):  [Read-Only]
- ``stage_settings`` (DisplayClusterConfigurationICVFX_StageSettings):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.info"></a>

#### info

```python
@property
def info() -> DisplayClusterConfigurationInfo
```

(DisplayClusterConfigurationInfo):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.info"></a>

#### info

```python
@info.setter
def info(value: DisplayClusterConfigurationInfo) -> None
```

<a id="unreal.DisplayClusterConfigurationData.scene"></a>

#### scene

```python
@property
def scene() -> DisplayClusterConfigurationScene
```

(DisplayClusterConfigurationScene):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationData.cluster"></a>

#### cluster

```python
@property
def cluster() -> DisplayClusterConfigurationCluster
```

(DisplayClusterConfigurationCluster):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationData.custom_parameters"></a>

#### custom_parameters

```python
@property
def custom_parameters() -> Map[str, str]
```

(Map[str, str]):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.custom_parameters"></a>

#### custom_parameters

```python
@custom_parameters.setter
def custom_parameters(value: Map[str, str]) -> None
```

<a id="unreal.DisplayClusterConfigurationData.diagnostics"></a>

#### diagnostics

```python
@property
def diagnostics() -> DisplayClusterConfigurationDiagnostics
```

(DisplayClusterConfigurationDiagnostics):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.diagnostics"></a>

#### diagnostics

```python
@diagnostics.setter
def diagnostics(value: DisplayClusterConfigurationDiagnostics) -> None
```

<a id="unreal.DisplayClusterConfigurationData.render_frame_settings"></a>

#### render_frame_settings

```python
@property
def render_frame_settings() -> DisplayClusterConfigurationRenderFrame
```

(DisplayClusterConfigurationRenderFrame):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.render_frame_settings"></a>

#### render_frame_settings

```python
@render_frame_settings.setter
def render_frame_settings(
        value: DisplayClusterConfigurationRenderFrame) -> None
```

<a id="unreal.DisplayClusterConfigurationData.stage_settings"></a>

#### stage_settings

```python
@property
def stage_settings() -> DisplayClusterConfigurationICVFX_StageSettings
```

(DisplayClusterConfigurationICVFX_StageSettings):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.stage_settings"></a>

#### stage_settings

```python
@stage_settings.setter
def stage_settings(
        value: DisplayClusterConfigurationICVFX_StageSettings) -> None
```

<a id="unreal.DisplayClusterConfigurationData.follow_local_player_camera"></a>

#### follow_local_player_camera

```python
@property
def follow_local_player_camera() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.follow_local_player_camera"></a>

#### follow_local_player_camera

```python
@follow_local_player_camera.setter
def follow_local_player_camera(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationData.exit_on_esc"></a>

#### exit_on_esc

```python
@property
def exit_on_esc() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.exit_on_esc"></a>

#### exit_on_esc

```python
@exit_on_esc.setter
def exit_on_esc(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationData.override_viewports_from_external_config"></a>

#### override_viewports_from_external_config

```python
@property
def override_viewports_from_external_config() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.override_viewports_from_external_config"></a>

#### override_viewports_from_external_config

```python
@override_viewports_from_external_config.setter
def override_viewports_from_external_config(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationData.override_transforms_from_external_config"></a>

#### override_transforms_from_external_config

```python
@property
def override_transforms_from_external_config() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.override_transforms_from_external_config"></a>

#### override_transforms_from_external_config

```python
@override_transforms_from_external_config.setter
def override_transforms_from_external_config(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationData.media_settings"></a>

#### media_settings

```python
@property
def media_settings() -> DisplayClusterConfigurationGlobalMediaSettings
```

(DisplayClusterConfigurationGlobalMediaSettings):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationData.media_settings"></a>

#### media_settings

```python
@media_settings.setter
def media_settings(
        value: DisplayClusterConfigurationGlobalMediaSettings) -> None
```

<a id="unreal.DisplayClusterConfigurationData.remove_postprocess"></a>

#### remove_postprocess

```python
def remove_postprocess(node_id: str, postprocess_id: str) -> bool
```

x.remove_postprocess(node_id, postprocess_id) -> bool
Remove Postprocess

Args:
    node_id (str): 
    postprocess_id (str): 

Returns:
    bool:

<a id="unreal.DisplayClusterConfigurationData.get_viewport"></a>

#### get_viewport

```python
def get_viewport(node_id: str,
                 viewport_id: str) -> DisplayClusterConfigurationViewport
```

x.get_viewport(node_id, viewport_id) -> DisplayClusterConfigurationViewport
Viewports API

Args:
    node_id (str): 
    viewport_id (str): 

Returns:
    DisplayClusterConfigurationViewport:

<a id="unreal.DisplayClusterConfigurationData.get_referenced_mesh_names"></a>

#### get_referenced_mesh_names

```python
def get_referenced_mesh_names() -> Array[str]
```

x.get_referenced_mesh_names() -> Array[str]
Return all references to meshes from policy, and other

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.DisplayClusterConfigurationData.get_projection_policy"></a>

#### get_projection_policy

```python
def get_projection_policy(
        node_id: str,
        viewport_id: str) -> Optional[DisplayClusterConfigurationProjection]
```

x.get_projection_policy(node_id, viewport_id) -> DisplayClusterConfigurationProjection or None
Get Projection Policy

Args:
    node_id (str): 
    viewport_id (str): 

Returns:
    DisplayClusterConfigurationProjection or None: 

    out_projection (DisplayClusterConfigurationProjection):

<a id="unreal.DisplayClusterConfigurationData.get_postprocess"></a>

#### get_postprocess

```python
def get_postprocess(
        node_id: str, postprocess_id: str
) -> Optional[DisplayClusterConfigurationPostprocess]
```

x.get_postprocess(node_id, postprocess_id) -> DisplayClusterConfigurationPostprocess or None
Get Postprocess

Args:
    node_id (str): 
    postprocess_id (str): 

Returns:
    DisplayClusterConfigurationPostprocess or None: 

    out_postprocess (DisplayClusterConfigurationPostprocess):

<a id="unreal.DisplayClusterConfigurationData.assign_postprocess"></a>

#### assign_postprocess

```python
def assign_postprocess(node_id: str,
                       postprocess_id: str,
                       type: str,
                       parameters: Map[str, str],
                       order: int = -1) -> bool
```

x.assign_postprocess(node_id, postprocess_id, type, parameters, order=-1) -> bool
Update\Create node postprocess

Args:
    node_id (str): 
    postprocess_id (str): Unique postprocess name
    type (str): Postprocess type id
    parameters (Map[str, str]): Postprocess parameters
    order (int32): Control the rendering order of post-processing. Larger value is displayed last

Returns:
    bool: true, if success

<a id="unreal.DisplayClusterMediaOutputSynchronizationPolicy"></a>