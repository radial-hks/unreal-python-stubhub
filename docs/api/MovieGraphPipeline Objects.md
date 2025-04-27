## MovieGraphPipeline Objects

```python
class MovieGraphPipeline(MoviePipelineBase)
```

Movie Graph Pipeline

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphPipeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_movie_pipeline_shot_work_finished_delegate`` (MoviePipelineWorkFinished):  [Read-Write] This callback will not be called by default due to performance reasons. You need to opt into this (via scripting
  in MoviePipeline or in the node in Movie Graph) by setting FlushDiskWritesPerShot to true in the output setting
  for this job's configuration.

  Called after each shot is finished and files have been flushed to disk. The returned data in
  the params struct will have only the per-shot metadata for the just finished shot. Use
  OnMoviePipelineWorkFinishedDelegate if you need all of the metadata.
- ``on_movie_pipeline_work_finished_delegate`` (MoviePipelineWorkFinished):  [Read-Write] Called when we have completely finished this pipeline. This means that all frames have been rendered,
  all files written to disk, and any post-finalize exports have finished. This Pipeline will call
  Shutdown() on itself before calling this delegate to ensure we've unregistered from all delegates
  and are no longer trying to do anything (even if we still exist).

  The params struct in the return will have metadata about files written to disk for each shot.

<a id="unreal.MovieGraphPipeline.set_initialization_time"></a>

#### set_initialization_time

```python
def set_initialization_time(date_time: DateTime) -> None
```

x.set_initialization_time(date_time) -> None
Override the time this movie pipeline was initialized at. This can be used for render farms
to ensure that jobs on all machines use the same date/time instead of each calculating it locally.
Clears the auto-calculated InitializationTimeOffset, meaning time tokens will be written in UTC.

Needs to be called after ::Initialize(...)

Args:
    date_time (DateTime): Expected to be in UTC timezone.

<a id="unreal.MovieGraphPipeline.on_movie_pipeline_finished_impl"></a>

#### on_movie_pipeline_finished_impl

```python
def on_movie_pipeline_finished_impl() -> None
```

x.on_movie_pipeline_finished_impl() -> None
On Movie Pipeline Finished Impl

<a id="unreal.MovieGraphPipeline.initialize"></a>

#### initialize

```python
def initialize(job: MoviePipelineExecutorJob,
               init_config: MovieGraphInitConfig) -> None
```

x.initialize(job, init_config) -> None
Initialize

Args:
    job (MoviePipelineExecutorJob): 
    init_config (MovieGraphInitConfig):

<a id="unreal.MovieGraphPipeline.get_time_step_instance"></a>

#### get_time_step_instance

```python
def get_time_step_instance() -> MovieGraphTimeStepBase
```

x.get_time_step_instance() -> MovieGraphTimeStepBase
Used occasionally to cross-reference other components. Don't call this unless you know what you're doing.

Returns:
    MovieGraphTimeStepBase:

<a id="unreal.MovieGraphPipeline.get_renderer_instance"></a>

#### get_renderer_instance

```python
def get_renderer_instance() -> MovieGraphRendererBase
```

x.get_renderer_instance() -> MovieGraphRendererBase
Used occasionally to cross-reference other components. Don't call this unless you know what you're doing.

Returns:
    MovieGraphRendererBase:

<a id="unreal.MovieGraphPipeline.get_initialization_time_offset"></a>

#### get_initialization_time_offset

```python
def get_initialization_time_offset() -> Timespan
```

x.get_initialization_time_offset() -> Timespan
The offset that should be applied to the GetInitializationTime() when generating
the {time} related filename tokens. GetInitializationTime() is in UTC so this is
either zero (if you called SetInitializationTime) or your offset from UTC.

Returns:
    Timespan:

<a id="unreal.MovieGraphPipeline.get_initialization_time"></a>

#### get_initialization_time

```python
def get_initialization_time() -> DateTime
```

x.get_initialization_time() -> DateTime
Returns the time this movie pipeline was initialized at.

Returns:
    DateTime:

<a id="unreal.MovieGraphPipeline.get_current_traversal_context"></a>

#### get_current_traversal_context

```python
def get_current_traversal_context(
        for_shot: bool = True) -> MovieGraphTraversalContext
```

x.get_current_traversal_context(for_shot=True) -> MovieGraphTraversalContext
Get Current Traversal Context

Args:
    for_shot (bool): 

Returns:
    MovieGraphTraversalContext:

<a id="unreal.MovieGraphPipeline.get_current_job"></a>

#### get_current_job

```python
def get_current_job() -> MoviePipelineExecutorJob
```

x.get_current_job() -> MoviePipelineExecutorJob
Returns the internal job being used by the Movie Graph Pipeline, which is a duplicate of
the job provided originaly by Initialize. This allows scripting to mutate the job/configuration
without leaking changes into assets or the original user-defined queue entry.

Returns:
    MoviePipelineExecutorJob:

<a id="unreal.MovieGraphProjectSettings"></a>