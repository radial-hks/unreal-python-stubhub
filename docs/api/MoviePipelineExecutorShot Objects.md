## MoviePipelineExecutorShot Objects

```python
class MoviePipelineExecutorShot(Object)
```

This class represents a segment of work within the Executor Job. This should be owned
by the UMoviePipelineExecutorJob and can be created before the movie pipeline starts to
configure some aspects about the segment (such as disabling it). When the movie pipeline
starts, it will use the already existing ones, or generate new ones as needed.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineQueue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``console_variable_overrides`` (Array[MoviePipelineConsoleVariableEntry]):  [Read-Write] (Optional) Console variable overrides which are applied after cvars set via nodes. Only applies to graph-based configs.
- ``enabled`` (bool):  [Read-Write] Does the user want to render this shot?
- ``graph_variable_assignments`` (Array[MovieJobVariableAssignmentContainer]):  [Read-Write] Overrides on the variables in the graph (and subgraphs) associated with this job.
- ``inner_name`` (str):  [Read-Write] The name of the camera cut section that this shot represents. Can be empty.
- ``outer_name`` (str):  [Read-Write] The name of the shot section that contains this shot. Can be empty.
- ``primary_graph_variable_assignments`` (Array[MovieJobVariableAssignmentContainer]):  [Read-Write] Overrides on the variables in the primary graph (and its subgraphs) associated with this job.
- ``sidecar_cameras`` (Array[MoviePipelineSidecarCamera]):  [Read-Write] List of cameras to render for this shot. Only used if the setting flag is set in the Camera setting.

<a id="unreal.MoviePipelineExecutorShot.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Does the user want to render this shot?

<a id="unreal.MoviePipelineExecutorShot.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.MoviePipelineExecutorShot.outer_name"></a>

#### outer_name

```python
@property
def outer_name() -> str
```

(str):  [Read-Write] The name of the shot section that contains this shot. Can be empty.

<a id="unreal.MoviePipelineExecutorShot.outer_name"></a>

#### outer_name

```python
@outer_name.setter
def outer_name(value: str) -> None
```

<a id="unreal.MoviePipelineExecutorShot.inner_name"></a>

#### inner_name

```python
@property
def inner_name() -> str
```

(str):  [Read-Write] The name of the camera cut section that this shot represents. Can be empty.

<a id="unreal.MoviePipelineExecutorShot.inner_name"></a>

#### inner_name

```python
@inner_name.setter
def inner_name(value: str) -> None
```

<a id="unreal.MoviePipelineExecutorShot.sidecar_cameras"></a>

#### sidecar_cameras

```python
@property
def sidecar_cameras() -> Array[MoviePipelineSidecarCamera]
```

(Array[MoviePipelineSidecarCamera]):  [Read-Write] List of cameras to render for this shot. Only used if the setting flag is set in the Camera setting.

<a id="unreal.MoviePipelineExecutorShot.sidecar_cameras"></a>

#### sidecar_cameras

```python
@sidecar_cameras.setter
def sidecar_cameras(value: Array[MoviePipelineSidecarCamera]) -> None
```

<a id="unreal.MoviePipelineExecutorShot.console_variable_overrides"></a>

#### console_variable_overrides

```python
@property
def console_variable_overrides() -> Array[MoviePipelineConsoleVariableEntry]
```

(Array[MoviePipelineConsoleVariableEntry]):  [Read-Write] (Optional) Console variable overrides which are applied after cvars set via nodes. Only applies to graph-based configs.

<a id="unreal.MoviePipelineExecutorShot.console_variable_overrides"></a>

#### console_variable_overrides

```python
@console_variable_overrides.setter
def console_variable_overrides(
        value: Array[MoviePipelineConsoleVariableEntry]) -> None
```

<a id="unreal.MoviePipelineExecutorShot.should_render"></a>

#### should_render

```python
def should_render() -> bool
```

x.should_render() -> bool
Returns whether this should should be rendered

Returns:
    bool:

<a id="unreal.MoviePipelineExecutorShot.set_status_progress"></a>

#### set_status_progress

```python
def set_status_progress(progress: float) -> None
```

x.set_status_progress(progress) -> None
Set the progress of this shot to the given value. If a positive value is provided
the UI will show the progress bar, while a negative value will make the UI show the
status message instead. Progress and Status Message are cosmetic and dependent on the
executor to update. Similar to the UMoviePipelineExecutor::SetStatusProgress function,
but at a per-job level basis instead.

For C++ implementations override `virtual void SetStatusProgress_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def set_status_progress(self, inStatus):

Args:
    progress (float): The progress (0-1 range) the executor should have.

<a id="unreal.MoviePipelineExecutorShot.set_status_message"></a>

#### set_status_message

```python
def set_status_message(status: str) -> None
```

x.set_status_message(status) -> None
Set the status of this shot to the given value. This will be shown on the UI if progress
is set to a value less than zero. If progress is > 0 then the progress bar will be shown
on the UI instead. Progress and Status Message are cosmetic.

For C++ implementations override `virtual void SetStatusMessage_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def set_status_message(self, inStatus):

Args:
    status (str): The status message you wish the executor to have.

<a id="unreal.MoviePipelineExecutorShot.set_shot_override_preset_origin"></a>

#### set_shot_override_preset_origin

```python
def set_shot_override_preset_origin(preset: MoviePipelineShotConfig) -> None
```

x.set_shot_override_preset_origin(preset) -> None
Set Shot Override Preset Origin

Args:
    preset (MoviePipelineShotConfig):

<a id="unreal.MoviePipelineExecutorShot.set_shot_override_configuration"></a>

#### set_shot_override_configuration

```python
def set_shot_override_configuration(preset: MoviePipelineShotConfig) -> None
```

x.set_shot_override_configuration(preset) -> None
Set Shot Override Configuration

Args:
    preset (MoviePipelineShotConfig):

<a id="unreal.MoviePipelineExecutorShot.set_graph_preset"></a>

#### set_graph_preset

```python
def set_graph_preset(graph_preset: MovieGraphConfig,
                     update_variable_assignments: bool = True) -> None
```

x.set_graph_preset(graph_preset, update_variable_assignments=True) -> None
Sets the graph-style preset that this job will use. Note that this will cause the graph to switch over to using
graph-style configuration if it is not already using it.

Args:
    graph_preset (MovieGraphConfig): The graph preset to assign to the shot.
    update_variable_assignments (bool): Set to false if variable assignments should NOT be automatically updated to reflect the graph preset being used. This is normally not what you want and should be used with caution.

<a id="unreal.MoviePipelineExecutorShot.is_using_graph_configuration"></a>

#### is_using_graph_configuration

```python
def is_using_graph_configuration() -> bool
```

x.is_using_graph_configuration() -> bool
Returns true if this job is using graph-style configuration, else false.

Returns:
    bool:

<a id="unreal.MoviePipelineExecutorShot.get_status_progress"></a>

#### get_status_progress

```python
def get_status_progress() -> float
```

x.get_status_progress() -> float
Get the current progress as last set by SetStatusProgress. 0 by default.

For C++ implementations override `virtual float GetStatusProgress_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def get_status_progress(self): return ?

Returns:
    float:

<a id="unreal.MoviePipelineExecutorShot.get_status_message"></a>

#### get_status_message

```python
def get_status_message() -> str
```

x.get_status_message() -> str
Get the current status message for this shot. May be an empty string.

For C++ implementations override `virtual FString GetStatusMessage_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def get_status_message(self): return ?

Returns:
    str:

<a id="unreal.MoviePipelineExecutorShot.get_shot_override_preset_origin"></a>

#### get_shot_override_preset_origin

```python
def get_shot_override_preset_origin() -> MoviePipelineShotConfig
```

x.get_shot_override_preset_origin() -> MoviePipelineShotConfig
Get Shot Override Preset Origin

Returns:
    MoviePipelineShotConfig:

<a id="unreal.MoviePipelineExecutorShot.get_shot_override_configuration"></a>

#### get_shot_override_configuration

```python
def get_shot_override_configuration() -> MoviePipelineShotConfig
```

x.get_shot_override_configuration() -> MoviePipelineShotConfig
Get Shot Override Configuration

Returns:
    MoviePipelineShotConfig:

<a id="unreal.MoviePipelineExecutorShot.get_or_create_variable_overrides"></a>

#### get_or_create_variable_overrides

```python
def get_or_create_variable_overrides(
    graph: MovieGraphConfig,
    is_for_primary_overrides: bool = False
) -> MovieJobVariableAssignmentContainer
```

x.get_or_create_variable_overrides(graph, is_for_primary_overrides=False) -> MovieJobVariableAssignmentContainer
This method will return you the object which contains variable overrides for either the Job's Primary or the Shot's GraphPreset. UMoviePipelineExecutorShot
has two separate sets of overrides. You can use the shot to override a variable on the Primary Graph (ie: the one assigned to the whole job),
but a graph can also have an entirely separate UMovieGraph config asset to run (though at runtime some variables will only be read from the
Primary Graph, ie: Custom Frame Range due to it applying to the entire sequence).

If you specify true for bIsForPrimaryOverrides it returns an object that allows this shot to override a variable that comes from the primary
graph. If you return false, then it returns an object that allows overriding a variable for this shot's override config (see: GetGraphPreset).
See UMoviePipelineExecutorJob's version of this functoin for more details.

Args:
    graph (MovieGraphConfig): The graph asset to return the config for. If this shot has its own Graph Preset override, you should return GetGraphPreset() or one of it's sub-graph pointers. If this shot is just trying to override the Primary Graph from the parent UMoviePipelineExecutorJob then you should return a pointer to the Job's GetGraphPreset() (or one of it's sub-graphs). Each graph/sub-graph gets its own set of overrides since sub-graphs can have different variables than the parents, so you have to provide the pointer to the one you want to override variables for.
    is_for_primary_overrides (bool): 

Returns:
    MovieJobVariableAssignmentContainer: A container object which holds a copy of the variables for the specified Graph Asset that can be used to override their values on jobs without actually editing the default asset.

<a id="unreal.MoviePipelineExecutorShot.get_graph_preset"></a>

#### get_graph_preset

```python
def get_graph_preset() -> MovieGraphConfig
```

x.get_graph_preset() -> MovieGraphConfig
Gets the graph-style preset that this job is using. If the job is not using a graph-style preset, returns nullptr.

Returns:
    MovieGraphConfig:

<a id="unreal.MoviePipelineExecutorShot.get_camera_name"></a>

#### get_camera_name

```python
def get_camera_name(camera_index: int) -> str
```

x.get_camera_name(camera_index) -> str
Get Camera Name

Args:
    camera_index (int32): 

Returns:
    str:

<a id="unreal.MoviePipelineExecutorShot.allocate_new_shot_override_config"></a>

#### allocate_new_shot_override_config

```python
def allocate_new_shot_override_config(
        config_type: Class = None) -> MoviePipelineShotConfig
```

x.allocate_new_shot_override_config(config_type=None) -> MoviePipelineShotConfig
Allocate New Shot Override Config

Args:
    config_type (type(Class)): 

Returns:
    MoviePipelineShotConfig:

<a id="unreal.MoviePipelineExecutorJob"></a>