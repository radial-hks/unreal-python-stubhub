## MovieRenderPipelineProjectSettings Objects

```python
class MovieRenderPipelineProjectSettings(Object)
```

Universal Movie Render Pipeline settings that apply to the whole project.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineEditor
- **File**: MovieRenderPipelineSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_classes`` (Array[SoftClassPath]):  [Read-Write] The settings specified here will automatically be added to a Movie Pipeline Primary Configuration when using the UI.
  This does not apply to scripting and does not apply to runtime. It is only a convenience function so that when a job is
  created, it can be pre-filled with some settings to make the render functional out of the gate. It can also be
  used to automatically add your own setting to jobs.

  This only applies to jobs created via the UI. If you do not use the UI (ie: Scripting/Python) you will need to
  add settings by hand for each job you create.
- ``default_executor_job`` (SoftClassPath):  [Read-Write] Which Job class should we create by default when adding a job? This allows you to make custom jobs
  that will have editable properties in the UI for special handling with your executor. This can be
  made dynamic if you add jobs to the queue programatically instead of through the UI.
- ``default_graph`` (MovieGraphConfig):  [Read-Write] The graph that newly-created graph assets will be based off of.
- ``default_local_executor`` (SoftClassPath):  [Read-Write] When the user uses the UI to request we render a movie locally, which implementation should we use
  to execute the queue of things they want rendered. This allows you to implement your own executor
  which does different logic. See UMoviePipelineExecutorBase for more information. This is used for
  the Render button on the UI.
- ``default_pipeline`` (SoftClassPath):  [Read-Write] This allows you to implement your own Pipeline to handle timing and rendering of a movie. Changing
  this will allow you to re-use the existing UI/Executors while providing your own logic for producing
  a single render.
- ``default_remote_executor`` (SoftClassPath):  [Read-Write] When the user uses the UI to request we render a movie remotely, which implementation should we use
  to execute the queue of things they want rendered. This allows you to implement your own executor
  which does different logic. See UMoviePipelineExecutorBase for more information. This is used for
  the Render Remotely button on the UI.
- ``last_preset_origin`` (MoviePipelinePrimaryConfig):  [Read-Write] What was the last configuration preset the user used? Can be null.
- ``preset_save_dir`` (DirectoryPath):  [Read-Write] Which directory should we try to save presets in by default?

<a id="unreal.MovieRenderPipelineProjectSettings.default_pipeline"></a>

#### default_pipeline

```python
@property
def default_pipeline() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] This allows you to implement your own Pipeline to handle timing and rendering of a movie. Changing
this will allow you to re-use the existing UI/Executors while providing your own logic for producing
a single render.

<a id="unreal.MovieRenderPipelineProjectSettings.default_pipeline"></a>

#### default_pipeline

```python
@default_pipeline.setter
def default_pipeline(value: SoftClassPath) -> None
```

<a id="unreal.MovieRenderPipelineProjectSettings.preset_save_dir"></a>

#### preset_save_dir

```python
@property
def preset_save_dir() -> DirectoryPath
```

(DirectoryPath):  [Read-Write] Which directory should we try to save presets in by default?

<a id="unreal.MovieRenderPipelineProjectSettings.preset_save_dir"></a>

#### preset_save_dir

```python
@preset_save_dir.setter
def preset_save_dir(value: DirectoryPath) -> None
```

<a id="unreal.MovieRenderPipelineProjectSettings.last_preset_origin"></a>

#### last_preset_origin

```python
@property
def last_preset_origin() -> MoviePipelinePrimaryConfig
```

(MoviePipelinePrimaryConfig):  [Read-Write] What was the last configuration preset the user used? Can be null.

<a id="unreal.MovieRenderPipelineProjectSettings.last_preset_origin"></a>

#### last_preset_origin

```python
@last_preset_origin.setter
def last_preset_origin(value: MoviePipelinePrimaryConfig) -> None
```

<a id="unreal.MovieRenderPipelineProjectSettings.default_local_executor"></a>

#### default_local_executor

```python
@property
def default_local_executor() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] When the user uses the UI to request we render a movie locally, which implementation should we use
to execute the queue of things they want rendered. This allows you to implement your own executor
which does different logic. See UMoviePipelineExecutorBase for more information. This is used for
the Render button on the UI.

<a id="unreal.MovieRenderPipelineProjectSettings.default_local_executor"></a>

#### default_local_executor

```python
@default_local_executor.setter
def default_local_executor(value: SoftClassPath) -> None
```

<a id="unreal.MovieRenderPipelineProjectSettings.default_remote_executor"></a>

#### default_remote_executor

```python
@property
def default_remote_executor() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] When the user uses the UI to request we render a movie remotely, which implementation should we use
to execute the queue of things they want rendered. This allows you to implement your own executor
which does different logic. See UMoviePipelineExecutorBase for more information. This is used for
the Render Remotely button on the UI.

<a id="unreal.MovieRenderPipelineProjectSettings.default_remote_executor"></a>

#### default_remote_executor

```python
@default_remote_executor.setter
def default_remote_executor(value: SoftClassPath) -> None
```

<a id="unreal.MovieRenderPipelineProjectSettings.default_executor_job"></a>

#### default_executor_job

```python
@property
def default_executor_job() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] Which Job class should we create by default when adding a job? This allows you to make custom jobs
that will have editable properties in the UI for special handling with your executor. This can be
made dynamic if you add jobs to the queue programatically instead of through the UI.

<a id="unreal.MovieRenderPipelineProjectSettings.default_executor_job"></a>

#### default_executor_job

```python
@default_executor_job.setter
def default_executor_job(value: SoftClassPath) -> None
```

<a id="unreal.MovieRenderPipelineProjectSettings.default_graph"></a>

#### default_graph

```python
@property
def default_graph() -> MovieGraphConfig
```

(MovieGraphConfig):  [Read-Write] The graph that newly-created graph assets will be based off of.

<a id="unreal.MovieRenderPipelineProjectSettings.default_graph"></a>

#### default_graph

```python
@default_graph.setter
def default_graph(value: MovieGraphConfig) -> None
```

<a id="unreal.MovieRenderPipelineProjectSettings.default_classes"></a>

#### default_classes

```python
@property
def default_classes() -> Array[SoftClassPath]
```

(Array[SoftClassPath]):  [Read-Write] The settings specified here will automatically be added to a Movie Pipeline Primary Configuration when using the UI.
This does not apply to scripting and does not apply to runtime. It is only a convenience function so that when a job is
created, it can be pre-filled with some settings to make the render functional out of the gate. It can also be
used to automatically add your own setting to jobs.

This only applies to jobs created via the UI. If you do not use the UI (ie: Scripting/Python) you will need to
add settings by hand for each job you create.

<a id="unreal.MovieRenderPipelineProjectSettings.default_classes"></a>

#### default_classes

```python
@default_classes.setter
def default_classes(value: Array[SoftClassPath]) -> None
```

<a id="unreal.EditorModelingObjectsCreationAPI"></a>