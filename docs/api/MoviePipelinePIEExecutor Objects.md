## MoviePipelinePIEExecutor Objects

```python
class MoviePipelinePIEExecutor(MoviePipelineLinearExecutorBase)
```

This is the implementation responsible for executing the rendering of
multiple movie pipelines in the currently running Editor process. This
involves launching a Play in Editor session for each Movie Pipeline to
process.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineEditor
- **File**: MoviePipelinePIEExecutor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_widget_class`` (type(Class)):  [Read-Write]
- ``http_response_recieved_delegate`` (MoviePipelineHttpResponseRecieved):  [Read-Write] If an HTTP Request has been made and a response returned, the returned response will be broadcast on this event.
- ``on_executor_errored_delegate`` (OnMoviePipelineExecutorErrored):  [Read-Write] Called when an individual job reports a warning/error. Jobs are considered fatal
  if the severity was bad enough to abort the job (missing sequence, write failure, etc.)

  Exposed for Blueprints/Python. Called at the same time as the native one.
- ``on_executor_finished_delegate`` (OnMoviePipelineExecutorFinished):  [Read-Write] Called when the Executor has finished all jobs. Reports success if no jobs
  had fatal errors. Subscribe to the error delegate for more information about
  any errors.

  Exposed for Blueprints/Python. Called at the same time as the native one.
- ``on_individual_job_finished_delegate`` (OnMoviePipelineIndividualJobFinished):  [Read-Write]
- ``on_individual_job_started_delegate`` (OnMoviePipelineIndividualJobStarted):  [Read-Write] Called right before this job is used to initialize a UMoviePipeline.
- ``on_individual_job_work_finished_delegate`` (MoviePipelineWorkFinished):  [Read-Write] Called after each job is finished in the queue. Params struct contains an output of all files written.
- ``on_individual_shot_work_finished_delegate`` (MoviePipelineWorkFinished):  [Read-Write] Called after each shot is finished for a particular render. Params struct contains an output of files written for this shot.
  Only called if the UMoviePipeline is set up correctly, requires a flag in the output setting to be set.
- ``socket_message_recieved_delegate`` (MoviePipelineSocketMessageRecieved):  [Read-Write] If this executor has been configured to connect to a socket, this event will be called each time the socket recieves something.
  The message response expected from the server should have a 4 byte (int32) size prefix for the string to specify how much data
  we should expect. This delegate will not get invoked until we recieve that many bytes from the socket connection to avoid broadcasting
  partial messages.
- ``target_pipeline_class`` (type(Class)):  [Read-Write] Which Pipeline Class should be created by this Executor. May be null.
- ``user_data`` (str):  [Read-Write] Arbitrary data that can be associated with the executor. Not used by default implementations, nor read.
  This can be used to attach third party metadata such as job ids from remote farms.

<a id="unreal.MoviePipelinePIEExecutor.on_individual_job_finished_delegate"></a>

#### on_individual_job_finished_delegate

```python
@property
def on_individual_job_finished_delegate(
) -> OnMoviePipelineIndividualJobFinished
```

(OnMoviePipelineIndividualJobFinished):  [Read-Write]

<a id="unreal.MoviePipelinePIEExecutor.on_individual_job_finished_delegate"></a>

#### on_individual_job_finished_delegate

```python
@on_individual_job_finished_delegate.setter
def on_individual_job_finished_delegate(
        value: OnMoviePipelineIndividualJobFinished) -> None
```

<a id="unreal.MoviePipelinePIEExecutor.on_individual_job_work_finished_delegate"></a>

#### on_individual_job_work_finished_delegate

```python
@property
def on_individual_job_work_finished_delegate() -> MoviePipelineWorkFinished
```

(MoviePipelineWorkFinished):  [Read-Write] Called after each job is finished in the queue. Params struct contains an output of all files written.

<a id="unreal.MoviePipelinePIEExecutor.on_individual_job_work_finished_delegate"></a>

#### on_individual_job_work_finished_delegate

```python
@on_individual_job_work_finished_delegate.setter
def on_individual_job_work_finished_delegate(
        value: MoviePipelineWorkFinished) -> None
```

<a id="unreal.MoviePipelinePIEExecutor.on_individual_shot_work_finished_delegate"></a>

#### on_individual_shot_work_finished_delegate

```python
@property
def on_individual_shot_work_finished_delegate() -> MoviePipelineWorkFinished
```

(MoviePipelineWorkFinished):  [Read-Write] Called after each shot is finished for a particular render. Params struct contains an output of files written for this shot.
Only called if the UMoviePipeline is set up correctly, requires a flag in the output setting to be set.

<a id="unreal.MoviePipelinePIEExecutor.on_individual_shot_work_finished_delegate"></a>

#### on_individual_shot_work_finished_delegate

```python
@on_individual_shot_work_finished_delegate.setter
def on_individual_shot_work_finished_delegate(
        value: MoviePipelineWorkFinished) -> None
```

<a id="unreal.MoviePipelinePIEExecutor.on_individual_job_started_delegate"></a>

#### on_individual_job_started_delegate

```python
@property
def on_individual_job_started_delegate(
) -> OnMoviePipelineIndividualJobStarted
```

(OnMoviePipelineIndividualJobStarted):  [Read-Write] Called right before this job is used to initialize a UMoviePipeline.

<a id="unreal.MoviePipelinePIEExecutor.on_individual_job_started_delegate"></a>

#### on_individual_job_started_delegate

```python
@on_individual_job_started_delegate.setter
def on_individual_job_started_delegate(
        value: OnMoviePipelineIndividualJobStarted) -> None
```

<a id="unreal.MoviePipelinePIEExecutor.set_is_rendering_offscreen"></a>

#### set_is_rendering_offscreen

```python
def set_is_rendering_offscreen(render_offscreen: bool) -> None
```

x.set_is_rendering_offscreen(render_offscreen) -> None
Should it render without any UI elements showing up (such as the rendering progress window)?

Args:
    render_offscreen (bool):

<a id="unreal.MoviePipelinePIEExecutor.set_initialization_time"></a>

#### set_initialization_time

```python
def set_initialization_time(initialization_time: DateTime) -> None
```

x.set_initialization_time(initialization_time) -> None
Set Initialization Time

Args:
    initialization_time (DateTime):

<a id="unreal.MoviePipelinePIEExecutor.is_rendering_offscreen"></a>

#### is_rendering_offscreen

```python
def is_rendering_offscreen() -> bool
```

x.is_rendering_offscreen() -> bool
Will it render without any UI elements showing up (such as the rendering progress window)?

Returns:
    bool:

<a id="unreal.MoviePipelineQueueSubsystem"></a>