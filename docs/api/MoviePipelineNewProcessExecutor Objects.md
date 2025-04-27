## MoviePipelineNewProcessExecutor Objects

```python
class MoviePipelineNewProcessExecutor(MoviePipelineExecutorBase)
```

This is the implementation responsible for executing the rendering of
multiple movie pipelines on the local machine in an external process.
This simply handles launching and managing the external processes and
acts as a proxy to them where possible. This internally uses the
UMoviePipelineInProcessExecutor on the launched instances.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineEditor
- **File**: MoviePipelineNewProcessExecutor.h

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
- ``socket_message_recieved_delegate`` (MoviePipelineSocketMessageRecieved):  [Read-Write] If this executor has been configured to connect to a socket, this event will be called each time the socket recieves something.
  The message response expected from the server should have a 4 byte (int32) size prefix for the string to specify how much data
  we should expect. This delegate will not get invoked until we recieve that many bytes from the socket connection to avoid broadcasting
  partial messages.
- ``target_pipeline_class`` (type(Class)):  [Read-Write] Which Pipeline Class should be created by this Executor. May be null.
- ``user_data`` (str):  [Read-Write] Arbitrary data that can be associated with the executor. Not used by default implementations, nor read.
  This can be used to attach third party metadata such as job ids from remote farms.

<a id="unreal.MoviePipelinePIEExecutor"></a>