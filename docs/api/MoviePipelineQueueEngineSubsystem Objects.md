## MoviePipelineQueueEngineSubsystem Objects

```python
class MoviePipelineQueueEngineSubsystem(EngineSubsystem)
```

This subsystem is intended for use when rendering in a shipping game (but can also be used in PIE
during development/testing). See UMoviePipelineQueueSubsystem for the Editor-only queue which is
bound to the Movie Render Queue UI. To do simple renders at runtime, call AllocateJob(...)
with the Level Sequence you want to render, then call FindOrAddSettingByClass on the job to add
the settings (such as render pass, output type, and output directory) that you want for the job.
Finally, call RenderJob with the job you just configured. Register a delegate to OnRenderFinished
to be notified when the render finished. You can optionally call SetConfiguration(...) before
RenderJob to configure some advanced options.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineQueueEngineSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_render_finished`` (MoviePipelineWorkFinished):  [Read-Write] Assign a function to this delegate to get notified when each individual job is finished.

  THIS WILL ONLY BE CALLED IF USING THE RENDERJOB CONVENIENCE FUNCTION.

  Because there can only be one job in the queue when using RenderJob, this will be called when
  the render is complete, and the executor has been released. This allows you to queue up another
  job immediately as a result of the OnRenderFinished callback.

<a id="unreal.MoviePipelineQueueEngineSubsystem.on_render_finished"></a>

#### on_render_finished

```python
@property
def on_render_finished() -> MoviePipelineWorkFinished
```

(MoviePipelineWorkFinished):  [Read-Write] Assign a function to this delegate to get notified when each individual job is finished.

THIS WILL ONLY BE CALLED IF USING THE RENDERJOB CONVENIENCE FUNCTION.

Because there can only be one job in the queue when using RenderJob, this will be called when
the render is complete, and the executor has been released. This allows you to queue up another
job immediately as a result of the OnRenderFinished callback.

<a id="unreal.MoviePipelineQueueEngineSubsystem.on_render_finished"></a>

#### on_render_finished

```python
@on_render_finished.setter
def on_render_finished(value: MoviePipelineWorkFinished) -> None
```

<a id="unreal.MoviePipelineQueueEngineSubsystem.set_configuration"></a>

#### set_configuration

```python
def set_configuration(progress_widget_class: Class = None,
                      render_player_viewport: bool = False) -> None
```

x.set_configuration(progress_widget_class=None, render_player_viewport=False) -> None
Sets some advanced configuration options that are used only occasionally to have better control over integrating it into
your game/application. This applies to both RenderQueueWithExecutor(Instance) and the simplified RenderJob API. This persists
until you call it again with different settings, and needs to be called before the Render* functions.

Args:
    progress_widget_class (type(Class)): 
    render_player_viewport (bool): If true, we will render the regular player viewport in addition to the off-screen MRQ render. This is significantly performance heavy (doubles render times) but can be useful in the event that you want to keep rendering the player viewport to better integrate the render into your own application.

<a id="unreal.MoviePipelineQueueEngineSubsystem.render_queue_with_executor_instance"></a>

#### render_queue_with_executor_instance

```python
def render_queue_with_executor_instance(
        executor: MoviePipelineExecutorBase) -> None
```

x.render_queue_with_executor_instance(executor) -> None
Starts processing the current queue with the supplied executor. This starts an async process which
may or may not run in a separate process (or on separate machines), determined by the executor implementation.
The executor should report progress for jobs depending on the implementation.

Args:
    executor (MoviePipelineExecutorBase): Instance of a subclass of UMoviePipelineExecutorBase.

<a id="unreal.MoviePipelineQueueEngineSubsystem.render_queue_with_executor"></a>

#### render_queue_with_executor

```python
def render_queue_with_executor(
        executor_type: Class) -> MoviePipelineExecutorBase
```

x.render_queue_with_executor(executor_type) -> MoviePipelineExecutorBase
Starts processing the current queue with the supplied executor class. This starts an async process which
may or may not run in a separate process (or on separate machines), determined by the executor implementation.
The executor should report progress for jobs depending on the implementation.

Args:
    executor_type (type(Class)): A subclass of UMoviePipelineExecutorBase. An instance of this class is created and started.

Returns:
    MoviePipelineExecutorBase: A pointer to the instance of the class created. This instance will be kept alive by the Queue Subsystem until it has finished (or been canceled). Register for progress reports and various callbacks on this instance.

<a id="unreal.MoviePipelineQueueEngineSubsystem.render_job"></a>

#### render_job

```python
def render_job(job: MoviePipelineExecutorJob) -> None
```

x.render_job(job) -> None
Convenience function for rendering the specified job. Calling this will render the specified job (if it was
allocated using AllocateJob) and then it will reset the queue once finished. If you need to render multiple
jobs (in a queue) then you need to either implement the queue behavior yourself, or use
GetQueue()->AllocateJob(...) instead and use the non-convenience functions.

Calling this function will clear the queue (after completion).

Using this function while IsRendering() returns true will result in an exception being thrown and no attempt
being made to render the job.

Args:
    job (MoviePipelineExecutorJob):

<a id="unreal.MoviePipelineQueueEngineSubsystem.is_rendering"></a>

#### is_rendering

```python
def is_rendering() -> bool
```

x.is_rendering() -> bool
Returns true if there is an active executor working on producing a movie. This could be actively rendering frames,
or working on post processing (finalizing file writes, etc.). Use GetActiveExecutor() and query it directly for
more information, progress updates, etc.

Returns:
    bool:

<a id="unreal.MoviePipelineQueueEngineSubsystem.get_queue"></a>

#### get_queue

```python
def get_queue() -> MoviePipelineQueue
```

x.get_queue() -> MoviePipelineQueue
Returns the queue of Movie Pipelines that need to be rendered.

Returns:
    MoviePipelineQueue:

<a id="unreal.MoviePipelineQueueEngineSubsystem.get_active_executor"></a>

#### get_active_executor

```python
def get_active_executor() -> MoviePipelineExecutorBase
```

x.get_active_executor() -> MoviePipelineExecutorBase
Returns the active executor (if there is one). This can be used to subscribe to events on an already in-progress render. May be null.

Returns:
    MoviePipelineExecutorBase:

<a id="unreal.MoviePipelineQueueEngineSubsystem.allocate_job"></a>

#### allocate_job

```python
def allocate_job(sequence: LevelSequence) -> MoviePipelineExecutorJob
```

x.allocate_job(sequence) -> MoviePipelineExecutorJob
Convenience function for creating a UMoviePipelineExecutorJob out of the given Level Sequence asset. The
newly created job will be initialized to render on the current level, and will not have any default settings
added to it - instead you will need to call FindOrAddSettingByClass on the job's configuration to add
settings such as render passes (UMoviePipelineDeferredPassBase), output types (UMoviePipelineImageSequenceOutput_PNG),
and configure the output directory (UMoviePipelineOutputSetting). Once configuration is complete, register
a delegate to OnRenderFinished and then call RenderJob.

Calling this function will clear the internal queue, see RenderJob for more details.

Using this function while IsRendering() returns true will result in an exception being thrown and no attempt
being made to create the job.

Args:
    sequence (LevelSequence): 

Returns:
    MoviePipelineExecutorJob:

<a id="unreal.MoviePipelineRenderPass"></a>