## MoviePipelinePythonHostExecutor Objects

```python
class MoviePipelinePythonHostExecutor(MoviePipelineExecutorBase)
```

This is a dummy executor that is designed to host a executor implemented in
python. Python defined UClasses are not available when the executor is initialized
and not all callbacks are available in Python. By inheriting from this in Python
and overriding which UClass to latently spawn, this class can just forward certain
events onto Python (by overriding the relevant function).

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelinePythonHostExecutor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_widget_class`` (type(Class)):  [Read-Write]
- ``executor_class`` (type(Class)):  [Read-Write] You should override this class type on the CDO of the object with your Python type when Python is initialized.
- ``http_response_recieved_delegate`` (MoviePipelineHttpResponseRecieved):  [Read-Write] If an HTTP Request has been made and a response returned, the returned response will be broadcast on this event.
- ``on_executor_errored_delegate`` (OnMoviePipelineExecutorErrored):  [Read-Write] Called when an individual job reports a warning/error. Jobs are considered fatal
  if the severity was bad enough to abort the job (missing sequence, write failure, etc.)

  Exposed for Blueprints/Python. Called at the same time as the native one.
- ``on_executor_finished_delegate`` (OnMoviePipelineExecutorFinished):  [Read-Write] Called when the Executor has finished all jobs. Reports success if no jobs
  had fatal errors. Subscribe to the error delegate for more information about
  any errors.

  Exposed for Blueprints/Python. Called at the same time as the native one.
- ``pipeline_queue`` (MoviePipelineQueue):  [Read-Write]
- ``socket_message_recieved_delegate`` (MoviePipelineSocketMessageRecieved):  [Read-Write] If this executor has been configured to connect to a socket, this event will be called each time the socket recieves something.
  The message response expected from the server should have a 4 byte (int32) size prefix for the string to specify how much data
  we should expect. This delegate will not get invoked until we recieve that many bytes from the socket connection to avoid broadcasting
  partial messages.
- ``target_pipeline_class`` (type(Class)):  [Read-Write] Which Pipeline Class should be created by this Executor. May be null.
- ``user_data`` (str):  [Read-Write] Arbitrary data that can be associated with the executor. Not used by default implementations, nor read.
  This can be used to attach third party metadata such as job ids from remote farms.

<a id="unreal.MoviePipelinePythonHostExecutor.executor_class"></a>

#### executor_class

```python
@property
def executor_class() -> Class
```

(type(Class)):  [Read-Write] You should override this class type on the CDO of the object with your Python type when Python is initialized.

<a id="unreal.MoviePipelinePythonHostExecutor.executor_class"></a>

#### executor_class

```python
@executor_class.setter
def executor_class(value: Class) -> None
```

<a id="unreal.MoviePipelinePythonHostExecutor.pipeline_queue"></a>

#### pipeline_queue

```python
@property
def pipeline_queue() -> MoviePipelineQueue
```

(MoviePipelineQueue):  [Read-Write]

<a id="unreal.MoviePipelinePythonHostExecutor.pipeline_queue"></a>

#### pipeline_queue

```python
@pipeline_queue.setter
def pipeline_queue(value: MoviePipelineQueue) -> None
```

<a id="unreal.MoviePipelinePythonHostExecutor.on_map_load"></a>

#### on_map_load

```python
def on_map_load(world: World) -> None
```

x.on_map_load(world) -> None
On Map Load

Args:
    world (World):

<a id="unreal.MoviePipelinePythonHostExecutor.get_last_loaded_world"></a>

#### get_last_loaded_world

```python
def get_last_loaded_world() -> World
```

x.get_last_loaded_world() -> World
~Python/Blueprint API

Returns:
    World:

<a id="unreal.MoviePipelinePythonHostExecutor.execute_delayed"></a>

#### execute_delayed

```python
def execute_delayed(pipeline_queue: MoviePipelineQueue) -> None
```

x.execute_delayed(pipeline_queue) -> None
Python/Blueprint API

Args:
    pipeline_queue (MoviePipelineQueue):

<a id="unreal.MoviePipelineExecutorShot"></a>