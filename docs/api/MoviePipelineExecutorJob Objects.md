## MoviePipelineExecutorJob Objects

```python
class MoviePipelineExecutorJob(Object)
```

A particular job within the Queue

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineQueue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``author`` (str):  [Read-Write] (Optional) If left blank, will default to system username. Can be shown in burn in as a first point of contact about the content.
- ``comment`` (str):  [Read-Write] (Optional) If specified, will be shown in the burn in to allow users to keep track of notes about a render.
- ``console_variable_overrides`` (Array[MoviePipelineConsoleVariableEntry]):  [Read-Write] (Optional) Console variable overrides which are applied after cvars set via nodes. Only applies to graph-based configs.
- ``graph_variable_assignments`` (Array[MovieJobVariableAssignmentContainer]):  [Read-Write] Overrides on the variables in the graph (and subgraphs) associated with this job.
- ``job_name`` (str):  [Read-Write] (Optional) Name of the job. Shown on the default burn-in.
- ``map`` (SoftObjectPath):  [Read-Write] Which map should this job render on
- ``sequence`` (SoftObjectPath):  [Read-Write] Which sequence should this job render?
- ``shot_info`` (Array[MoviePipelineExecutorShot]):  [Read-Write] (Optional) Shot specific information. If a shot is missing from this list it will assume to be enabled and will be rendered.
- ``user_data`` (str):  [Read-Write] Arbitrary data that can be associated with the job. Not used by default implementations, nor read.
  This can be used to attach third party metadata such as job ids from remote farms.
  Not shown in the user interface.

<a id="unreal.MoviePipelineExecutorJob.job_name"></a>

#### job_name

```python
@property
def job_name() -> str
```

(str):  [Read-Write] (Optional) Name of the job. Shown on the default burn-in.

<a id="unreal.MoviePipelineExecutorJob.job_name"></a>

#### job_name

```python
@job_name.setter
def job_name(value: str) -> None
```

<a id="unreal.MoviePipelineExecutorJob.sequence"></a>

#### sequence

```python
@property
def sequence() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] Which sequence should this job render?

<a id="unreal.MoviePipelineExecutorJob.sequence"></a>

#### sequence

```python
@sequence.setter
def sequence(value: SoftObjectPath) -> None
```

<a id="unreal.MoviePipelineExecutorJob.map"></a>

#### map

```python
@property
def map() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] Which map should this job render on

<a id="unreal.MoviePipelineExecutorJob.map"></a>

#### map

```python
@map.setter
def map(value: SoftObjectPath) -> None
```

<a id="unreal.MoviePipelineExecutorJob.author"></a>

#### author

```python
@property
def author() -> str
```

(str):  [Read-Write] (Optional) If left blank, will default to system username. Can be shown in burn in as a first point of contact about the content.

<a id="unreal.MoviePipelineExecutorJob.author"></a>

#### author

```python
@author.setter
def author(value: str) -> None
```

<a id="unreal.MoviePipelineExecutorJob.comment"></a>

#### comment

```python
@property
def comment() -> str
```

(str):  [Read-Write] (Optional) If specified, will be shown in the burn in to allow users to keep track of notes about a render.

<a id="unreal.MoviePipelineExecutorJob.comment"></a>

#### comment

```python
@comment.setter
def comment(value: str) -> None
```

<a id="unreal.MoviePipelineExecutorJob.shot_info"></a>

#### shot_info

```python
@property
def shot_info() -> Array[MoviePipelineExecutorShot]
```

(Array[MoviePipelineExecutorShot]):  [Read-Write] (Optional) Shot specific information. If a shot is missing from this list it will assume to be enabled and will be rendered.

<a id="unreal.MoviePipelineExecutorJob.shot_info"></a>

#### shot_info

```python
@shot_info.setter
def shot_info(value: Array[MoviePipelineExecutorShot]) -> None
```

<a id="unreal.MoviePipelineExecutorJob.user_data"></a>

#### user_data

```python
@property
def user_data() -> str
```

(str):  [Read-Write] Arbitrary data that can be associated with the job. Not used by default implementations, nor read.
This can be used to attach third party metadata such as job ids from remote farms.
Not shown in the user interface.

<a id="unreal.MoviePipelineExecutorJob.user_data"></a>

#### user_data

```python
@user_data.setter
def user_data(value: str) -> None
```

<a id="unreal.MoviePipelineExecutorJob.console_variable_overrides"></a>

#### console_variable_overrides

```python
@property
def console_variable_overrides() -> Array[MoviePipelineConsoleVariableEntry]
```

(Array[MoviePipelineConsoleVariableEntry]):  [Read-Write] (Optional) Console variable overrides which are applied after cvars set via nodes. Only applies to graph-based configs.

<a id="unreal.MoviePipelineExecutorJob.console_variable_overrides"></a>

#### console_variable_overrides

```python
@console_variable_overrides.setter
def console_variable_overrides(
        value: Array[MoviePipelineConsoleVariableEntry]) -> None
```

<a id="unreal.MoviePipelineExecutorJob.set_status_progress"></a>

#### set_status_progress

```python
def set_status_progress(progress: float) -> None
```

x.set_status_progress(progress) -> None
Set the progress of this job to the given value. If a positive value is provided
the UI will show the progress bar, while a negative value will make the UI show the
status message instead. Progress and Status Message are cosmetic and dependent on the
executor to update. Similar to the UMoviePipelineExecutor::SetStatusProgress function,
but at a per-job level basis instead.

For C++ implementations override `virtual void SetStatusProgress_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def set_status_progress(self, inProgress):

Args:
    progress (float): The progress (0-1 range) the executor should have.

<a id="unreal.MoviePipelineExecutorJob.set_status_message"></a>

#### set_status_message

```python
def set_status_message(status: str) -> None
```

x.set_status_message(status) -> None
Set the status of this job to the given value. This will be shown on the UI if progress
is set to a value less than zero. If progress is > 0 then the progress bar will be shown
on the UI instead. Progress and Status Message are cosmetic and dependent on the
executor to update. Similar to the UMoviePipelineExecutor::SetStatusMessage function,
but at a per-job level basis instead.

For C++ implementations override `virtual void SetStatusMessage_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def set_status_message(self, inStatus):

Args:
    status (str): The status message you wish the executor to have.

<a id="unreal.MoviePipelineExecutorJob.set_preset_origin"></a>

#### set_preset_origin

```python
def set_preset_origin(preset: MoviePipelinePrimaryConfig) -> None
```

x.set_preset_origin(preset) -> None
Set Preset Origin

Args:
    preset (MoviePipelinePrimaryConfig):

<a id="unreal.MoviePipelineExecutorJob.set_is_enabled"></a>

#### set_is_enabled

```python
def set_is_enabled(enabled: bool) -> None
```

x.set_is_enabled(enabled) -> None
Set the job to be enabled/disabled. This is exposed to the user in the Queue UI
so they can disable a job after loading a queue to skip trying to run it.

For C++ implementations override `virtual void SetIsEnabled_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def set_is_enabled(self, isEnabled):

Args:
    enabled (bool): True if the job should be enabled and rendered.

<a id="unreal.MoviePipelineExecutorJob.set_graph_preset"></a>

#### set_graph_preset

```python
def set_graph_preset(graph_preset: MovieGraphConfig,
                     update_variable_assignments: bool = True) -> None
```

x.set_graph_preset(graph_preset, update_variable_assignments=True) -> None
Sets the graph-style preset that this job will use. Note that this will cause the graph to switch over to using
graph-style configuration if it is not already using it.

Args:
    graph_preset (MovieGraphConfig): The graph preset to assign to the job.
    update_variable_assignments (bool): Set to false if variable assignments should NOT be automatically updated to reflect the graph preset being used. This is normally not what you want and should be used with caution.

<a id="unreal.MoviePipelineExecutorJob.set_consumed"></a>

#### set_consumed

```python
def set_consumed(consumed: bool) -> None
```

x.set_consumed(consumed) -> None
Set the job to be consumed. A consumed job is disabled in the UI and should not be
submitted for rendering again. This allows jobs to be added to a queue, the queue
submitted to a remote farm (consume the jobs) and then more jobs to be added and
the second submission to the farm won't re-submit the already in-progress jobs.

Jobs can be unconsumed when the render finishes to re-enable editing.

For C++ implementations override `virtual void SetConsumed_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def set_consumed(self, isConsumed):

Args:
    consumed (bool): True if the job should be consumed and disabled for editing in the UI.

<a id="unreal.MoviePipelineExecutorJob.set_configuration"></a>

#### set_configuration

```python
def set_configuration(preset: MoviePipelinePrimaryConfig) -> None
```

x.set_configuration(preset) -> None
Set Configuration

Args:
    preset (MoviePipelinePrimaryConfig):

<a id="unreal.MoviePipelineExecutorJob.on_duplicated"></a>

#### on_duplicated

```python
def on_duplicated() -> None
```

x.on_duplicated() -> None
Should be called to clear status and user data after duplication so that jobs stay
unique and don't pick up ids or other unwanted behavior from the pareant job.

For C++ implementations override `virtual bool OnDuplicated_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def on_duplicated(self):

<a id="unreal.MoviePipelineExecutorJob.is_using_graph_configuration"></a>

#### is_using_graph_configuration

```python
def is_using_graph_configuration() -> bool
```

x.is_using_graph_configuration() -> bool
Returns true if this job is using graph-style configuration, else false.

Returns:
    bool:

<a id="unreal.MoviePipelineExecutorJob.is_enabled"></a>

#### is_enabled

```python
def is_enabled() -> bool
```

x.is_enabled() -> bool
Gets whether or not the job has been marked as being enabled.

For C++ implementations override `virtual bool IsEnabled_Implementation() const override`
For Python/BP implementations override
unreal.ufunction(override=True): def is_enabled(self): return ?

Returns:
    bool:

<a id="unreal.MoviePipelineExecutorJob.is_consumed"></a>

#### is_consumed

```python
def is_consumed() -> bool
```

x.is_consumed() -> bool
Gets whether or not the job has been marked as being consumed. A consumed job is not editable
in the UI and should not be submitted for rendering as it is either already finished or
already in progress.

For C++ implementations override `virtual bool IsConsumed_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def is_consumed(self): return ?

Returns:
    bool:

<a id="unreal.MoviePipelineExecutorJob.get_status_progress"></a>

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

<a id="unreal.MoviePipelineExecutorJob.get_status_message"></a>

#### get_status_message

```python
def get_status_message() -> str
```

x.get_status_message() -> str
Get the current status message for this job. May be an empty string.

For C++ implementations override `virtual FString GetStatusMessage_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def get_status_message(self): return ?

Returns:
    str:

<a id="unreal.MoviePipelineExecutorJob.get_preset_origin"></a>

#### get_preset_origin

```python
def get_preset_origin() -> MoviePipelinePrimaryConfig
```

x.get_preset_origin() -> MoviePipelinePrimaryConfig
Gets the preset for this job, but only if the preset has not been modified. If it has been modified, or the preset
no longer exists, returns nullptr.
see: GetConfiguration()

Returns:
    MoviePipelinePrimaryConfig:

<a id="unreal.MoviePipelineExecutorJob.get_or_create_variable_overrides"></a>

#### get_or_create_variable_overrides

```python
def get_or_create_variable_overrides(
        graph: MovieGraphConfig) -> MovieJobVariableAssignmentContainer
```

x.get_or_create_variable_overrides(graph) -> MovieJobVariableAssignmentContainer
This method will return you the object which contains variable overrides for the Primary Graph assigned to this job. You need to provide
a pointer to the exact graph you want (as the Primary Graph may contain sub-graphs, and those sub-graphs can have their own variables),
though this will be the same as GetGraphPreset() if you're not using any sub-graphs, or your variables only exist on the Primary graph.

If you want to override a variable on the primary graph but only for a specific shot, you should get the UMoviePipelineExecutorShot and
call that classes version of this function, except passing True for the extra boolean.  See comment on that function for more details.

Args:
    graph (MovieGraphConfig): The graph asset to get the Job Override values for. Should be the graph the variables you want to edit are defined on, which can either be the primary graph (GetGraphPreset()) or one of the sub-graphs it points to (as sub-graphs can contain their own variables which are all shown at the top level job in the Editor UI).

Returns:
    MovieJobVariableAssignmentContainer: A container object which holds a copy of the variables for the specified Graph Asset that can be used to override their values on jobs without actually editing the default asset.

<a id="unreal.MoviePipelineExecutorJob.get_graph_preset"></a>

#### get_graph_preset

```python
def get_graph_preset() -> MovieGraphConfig
```

x.get_graph_preset() -> MovieGraphConfig
Gets the graph-style preset that this job is using. If the job is not using a graph-style preset, returns nullptr.
see: GetPresetOrigin()

Returns:
    MovieGraphConfig:

<a id="unreal.MoviePipelineExecutorJob.get_configuration"></a>

#### get_configuration

```python
def get_configuration() -> MoviePipelinePrimaryConfig
```

x.get_configuration() -> MoviePipelinePrimaryConfig
Gets the configuration for the job. This configuration is either standalone (not associated with any preset), or
contains a copy of the preset origin plus any modifications made on top of it. If the preset that this
configuration was originally based on no longer exists, this configuration will still be valid.
see: GetPresetOrigin()

Returns:
    MoviePipelinePrimaryConfig:

<a id="unreal.MoviePipelineQueue"></a>