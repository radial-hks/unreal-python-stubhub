## MoviePipelineBase Objects

```python
class MoviePipelineBase(Object)
```

Movie Pipeline Base

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineBase.h

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

<a id="unreal.MoviePipelineBase.on_movie_pipeline_work_finished_delegate"></a>

#### on_movie_pipeline_work_finished_delegate

```python
@property
def on_movie_pipeline_work_finished_delegate() -> MoviePipelineWorkFinished
```

(MoviePipelineWorkFinished):  [Read-Write] Called when we have completely finished this pipeline. This means that all frames have been rendered,
all files written to disk, and any post-finalize exports have finished. This Pipeline will call
Shutdown() on itself before calling this delegate to ensure we've unregistered from all delegates
and are no longer trying to do anything (even if we still exist).

The params struct in the return will have metadata about files written to disk for each shot.

<a id="unreal.MoviePipelineBase.on_movie_pipeline_work_finished_delegate"></a>

#### on_movie_pipeline_work_finished_delegate

```python
@on_movie_pipeline_work_finished_delegate.setter
def on_movie_pipeline_work_finished_delegate(
        value: MoviePipelineWorkFinished) -> None
```

<a id="unreal.MoviePipelineBase.on_movie_pipeline_shot_work_finished_delegate"></a>

#### on_movie_pipeline_shot_work_finished_delegate

```python
@property
def on_movie_pipeline_shot_work_finished_delegate(
) -> MoviePipelineWorkFinished
```

(MoviePipelineWorkFinished):  [Read-Write] This callback will not be called by default due to performance reasons. You need to opt into this (via scripting
in MoviePipeline or in the node in Movie Graph) by setting FlushDiskWritesPerShot to true in the output setting
for this job's configuration.

Called after each shot is finished and files have been flushed to disk. The returned data in
the params struct will have only the per-shot metadata for the just finished shot. Use
OnMoviePipelineWorkFinishedDelegate if you need all of the metadata.

<a id="unreal.MoviePipelineBase.on_movie_pipeline_shot_work_finished_delegate"></a>

#### on_movie_pipeline_shot_work_finished_delegate

```python
@on_movie_pipeline_shot_work_finished_delegate.setter
def on_movie_pipeline_shot_work_finished_delegate(
        value: MoviePipelineWorkFinished) -> None
```

<a id="unreal.MoviePipelineBase.shutdown"></a>

#### shutdown

```python
def shutdown(is_error: bool = False) -> None
```

x.shutdown(is_error=False) -> None
Abandons any future work on this Movie Pipeline and runs through the shutdown flow to ensure already
completed work is written to disk. This is a blocking-operation and will not return until all outstanding
work has been completed.

Args:
    is_error (bool): Whether this is an early shut down due to an error This function should only be called from the game thread.

<a id="unreal.MoviePipelineBase.request_shutdown"></a>

#### request_shutdown

```python
def request_shutdown(is_error: bool = False) -> None
```

x.request_shutdown(is_error=False) -> None
Request the movie pipeline to shut down at the next available time. The pipeline will attempt to abandon
the current frame (such as if there are more temporal samples pending) but may be forced into finishing if
there are spatial samples already submitted to the GPU. The shutdown flow will be run to ensure already
completed work is written to disk. This is a non-blocking operation, use Shutdown() instead if you need to
block until it is fully shut down.

Args:
    is_error (bool): Whether this is a request for early shut down due to an error This function is thread safe.

<a id="unreal.MoviePipelineBase.is_shutdown_requested"></a>

#### is_shutdown_requested

```python
def is_shutdown_requested() -> bool
```

x.is_shutdown_requested() -> bool
Has RequestShutdown() been called?

Returns:
    bool:

<a id="unreal.MoviePipelineBase.get_pipeline_state"></a>

#### get_pipeline_state

```python
def get_pipeline_state() -> MovieRenderPipelineState
```

x.get_pipeline_state() -> MovieRenderPipelineState
Get Pipeline State

Returns:
    MovieRenderPipelineState:

<a id="unreal.MovieGraphPipeline"></a>