## MoviePipeline Objects

```python
class MoviePipeline(MoviePipelineBase)
```

Movie Pipeline

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipeline.h

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

<a id="unreal.MoviePipeline.set_initialization_time"></a>

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

<a id="unreal.MoviePipeline.on_movie_pipeline_finished_impl"></a>

#### on_movie_pipeline_finished_impl

```python
def on_movie_pipeline_finished_impl() -> None
```

x.on_movie_pipeline_finished_impl() -> None
This function should be called by the Executor when execution has finished (this should still be called in the event of an error)

<a id="unreal.MoviePipeline.initialize"></a>

#### initialize

```python
def initialize(job: MoviePipelineExecutorJob) -> None
```

x.initialize(job) -> None
Initialize the movie pipeline with the specified settings. This kicks off the rendering process.

Args:
    job (MoviePipelineExecutorJob): This contains settings and sequence to render this Movie Pipeline with.

<a id="unreal.MoviePipeline.get_preview_texture"></a>

#### get_preview_texture

```python
def get_preview_texture() -> Texture
```

x.get_preview_texture() -> Texture
Get Preview Texture

Returns:
    Texture:

<a id="unreal.MoviePipeline.get_pipeline_primary_config"></a>

#### get_pipeline_primary_config

```python
def get_pipeline_primary_config() -> MoviePipelinePrimaryConfig
```

x.get_pipeline_primary_config() -> MoviePipelinePrimaryConfig
Get the Primary Configuration used to render this shot. This contains the global settings for the shot, as well as per-shot
configurations which can contain their own settings.

Returns:
    MoviePipelinePrimaryConfig:

<a id="unreal.MoviePipeline.get_initialization_time_offset"></a>

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

<a id="unreal.MoviePipeline.get_initialization_time"></a>

#### get_initialization_time

```python
def get_initialization_time() -> DateTime
```

x.get_initialization_time() -> DateTime
Returns the time this movie pipeline was initialized at.

Returns:
    DateTime:

<a id="unreal.MoviePipeline.get_current_job"></a>

#### get_current_job

```python
def get_current_job() -> MoviePipelineExecutorJob
```

x.get_current_job() -> MoviePipelineExecutorJob
Get Current Job

Returns:
    MoviePipelineExecutorJob:

<a id="unreal.MoviePipelineAntiAliasingSetting"></a>