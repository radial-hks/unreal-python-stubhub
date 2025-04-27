## MoviePipelineExecutorBase Objects

```python
class MoviePipelineExecutorBase(Object)
```

A Movie Pipeline Executor is responsible for executing an array of Movie Pipelines,
and (optionally) reporting progress back for the movie pipelines. The entire array
is passed at once to allow the implementations to choose how to split up the work.
By default we provide a local execution (UMoviePipelineLocalExecutor) which works
on them serially, but you can create an implementation of this class, change the
default in the Project Settings and use your own distribution logic. For example,
you may want to distribute the work to multiple computers over a network, which
may involve running command line options on each machine to sync the latest content
from the project before the execution starts.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineExecutor.h

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

<a id="unreal.MoviePipelineExecutorBase.on_executor_finished_delegate"></a>

#### on_executor_finished_delegate

```python
@property
def on_executor_finished_delegate() -> OnMoviePipelineExecutorFinished
```

(OnMoviePipelineExecutorFinished):  [Read-Write] Called when the Executor has finished all jobs. Reports success if no jobs
had fatal errors. Subscribe to the error delegate for more information about
any errors.

Exposed for Blueprints/Python. Called at the same time as the native one.

<a id="unreal.MoviePipelineExecutorBase.on_executor_finished_delegate"></a>

#### on_executor_finished_delegate

```python
@on_executor_finished_delegate.setter
def on_executor_finished_delegate(
        value: OnMoviePipelineExecutorFinished) -> None
```

<a id="unreal.MoviePipelineExecutorBase.on_executor_errored_delegate"></a>

#### on_executor_errored_delegate

```python
@property
def on_executor_errored_delegate() -> OnMoviePipelineExecutorErrored
```

(OnMoviePipelineExecutorErrored):  [Read-Write] Called when an individual job reports a warning/error. Jobs are considered fatal
if the severity was bad enough to abort the job (missing sequence, write failure, etc.)

Exposed for Blueprints/Python. Called at the same time as the native one.

<a id="unreal.MoviePipelineExecutorBase.on_executor_errored_delegate"></a>

#### on_executor_errored_delegate

```python
@on_executor_errored_delegate.setter
def on_executor_errored_delegate(
        value: OnMoviePipelineExecutorErrored) -> None
```

<a id="unreal.MoviePipelineExecutorBase.socket_message_recieved_delegate"></a>

#### socket_message_recieved_delegate

```python
@property
def socket_message_recieved_delegate() -> MoviePipelineSocketMessageRecieved
```

(MoviePipelineSocketMessageRecieved):  [Read-Write] If this executor has been configured to connect to a socket, this event will be called each time the socket recieves something.
The message response expected from the server should have a 4 byte (int32) size prefix for the string to specify how much data
we should expect. This delegate will not get invoked until we recieve that many bytes from the socket connection to avoid broadcasting
partial messages.

<a id="unreal.MoviePipelineExecutorBase.socket_message_recieved_delegate"></a>

#### socket_message_recieved_delegate

```python
@socket_message_recieved_delegate.setter
def socket_message_recieved_delegate(
        value: MoviePipelineSocketMessageRecieved) -> None
```

<a id="unreal.MoviePipelineExecutorBase.http_response_recieved_delegate"></a>

#### http_response_recieved_delegate

```python
@property
def http_response_recieved_delegate() -> MoviePipelineHttpResponseRecieved
```

(MoviePipelineHttpResponseRecieved):  [Read-Write] If an HTTP Request has been made and a response returned, the returned response will be broadcast on this event.

<a id="unreal.MoviePipelineExecutorBase.http_response_recieved_delegate"></a>

#### http_response_recieved_delegate

```python
@http_response_recieved_delegate.setter
def http_response_recieved_delegate(
        value: MoviePipelineHttpResponseRecieved) -> None
```

<a id="unreal.MoviePipelineExecutorBase.debug_widget_class"></a>

#### debug_widget_class

```python
@property
def debug_widget_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.MoviePipelineExecutorBase.debug_widget_class"></a>

#### debug_widget_class

```python
@debug_widget_class.setter
def debug_widget_class(value: Class) -> None
```

<a id="unreal.MoviePipelineExecutorBase.user_data"></a>

#### user_data

```python
@property
def user_data() -> str
```

(str):  [Read-Write] Arbitrary data that can be associated with the executor. Not used by default implementations, nor read.
This can be used to attach third party metadata such as job ids from remote farms.

<a id="unreal.MoviePipelineExecutorBase.user_data"></a>

#### user_data

```python
@user_data.setter
def user_data(value: str) -> None
```

<a id="unreal.MoviePipelineExecutorBase.target_pipeline_class"></a>

#### target_pipeline_class

```python
@property
def target_pipeline_class() -> Class
```

(type(Class)):  [Read-Write] Which Pipeline Class should be created by this Executor. May be null.

<a id="unreal.MoviePipelineExecutorBase.target_pipeline_class"></a>

#### target_pipeline_class

```python
@target_pipeline_class.setter
def target_pipeline_class(value: Class) -> None
```

<a id="unreal.MoviePipelineExecutorBase.set_status_progress"></a>

#### set_status_progress

```python
def set_status_progress(progress: float) -> None
```

x.set_status_progress(progress) -> None
Set the progress of this Executor. Does nothing in default implementations, but a useful shorthand
for implementations to broadcast progress updates, ie: You can call SetStatusProgress as your executor
changes progress, and override the SetStatusProgress function to make it actually do something (such as
printing to a log or updating a third party API).

Does not necessairly reflect the overall progress of the work, it is an arbitrary 0-1 value that
can be used to indicate different things (depending on implementation).

For C++ implementations override `virtual bool SetStatusProgress_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def set_status_progress(self, inStatus):

Args:
    progress (float): The progress (0-1 range) the executor should have.

<a id="unreal.MoviePipelineExecutorBase.set_status_message"></a>

#### set_status_message

```python
def set_status_message(status: str) -> None
```

x.set_status_message(status) -> None
Set the status of this Executor. Does nothing in default implementations, but a useful shorthand
for implementations to broadcast status updates, ie: You can call SetStatusMessage as your executor
changes state, and override the SetStatusMessage function to make it actually do something (such as
printing to a log or updating a third party API).

For C++ implementations override `virtual bool SetStatusMessage_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def set_status_message(self, inStatus):

Args:
    status (str): The status message you wish the executor to have.

<a id="unreal.MoviePipelineExecutorBase.set_movie_pipeline_class"></a>

#### set_movie_pipeline_class

```python
def set_movie_pipeline_class(pipeline_class: Class) -> None
```

x.set_movie_pipeline_class(pipeline_class) -> None
Specify which MoviePipeline class type should be created by this executor when processing jobs.

Args:
    pipeline_class (type(Class)):

<a id="unreal.MoviePipelineExecutorBase.send_socket_message"></a>

#### send_socket_message

```python
def send_socket_message(message: str) -> bool
```

x.send_socket_message(message) -> bool
Sends a socket message if the socket is currently connected. Messages back will happen in the OnSocketMessageRecieved event.

Args:
    message (str): The message to send. This will be sent over the socket (if connected) with a 4 byte (int32) size prefix on the message so the recieving end knows how much data to recieve before considering it done. This prevents accidentally chopping json strings in half.

Returns:
    bool: True if the message was sent succesfully.

<a id="unreal.MoviePipelineExecutorBase.send_http_request"></a>

#### send_http_request

```python
def send_http_request(url: str, verb: str, message: str,
                      headers: Map[str, str]) -> int
```

x.send_http_request(url, verb, message, headers) -> int32
Sends a asynchronous HTTP request. Responses will be returned in the the OnHTTPResponseRecieved event.

Args:
    url (str): The URL to send the request to.
    verb (str): The HTTP verb for the request. GET, PUT, POST, etc.
    message (str): The content of the request.
    headers (Map[str, str]): Headers that should be set on the request.

Returns:
    int32: Returns an index for the request. This index will be provided in the OnHTTPResponseRecieved event so you can make multiple HTTP requests at once and tell them apart when you recieve them, even if they come out of order.

<a id="unreal.MoviePipelineExecutorBase.on_executor_finished_impl"></a>

#### on_executor_finished_impl

```python
def on_executor_finished_impl() -> None
```

x.on_executor_finished_impl() -> None
This should be called when the Executor has finished executing all of the things
it has been asked to execute. This should be called in the event of a failure as
well, and passing in false for success to allow the caller to know failure. Errors
should be broadcast on the error delegate, so this is just a handy way to know at
the end without having to track it yourself.

<a id="unreal.MoviePipelineExecutorBase.on_executor_errored_impl"></a>

#### on_executor_errored_impl

```python
def on_executor_errored_impl(errored_pipeline: MoviePipeline, fatal: bool,
                             error_reason: Text) -> None
```

x.on_executor_errored_impl(errored_pipeline, fatal, error_reason) -> None
On Executor Errored Impl

Args:
    errored_pipeline (MoviePipeline): 
    fatal (bool): 
    error_reason (Text):

<a id="unreal.MoviePipelineExecutorBase.on_begin_frame"></a>

#### on_begin_frame

```python
def on_begin_frame() -> None
```

x.on_begin_frame() -> None
Called once at the beginning of each engine frame.

For C++ implementations override `virtual bool OnBeginFrame_Implementation() override`
For Python/BP implementations override
unreal.ufunction(override=True): def on_begin_frame(self): super().on_begin_frame()

<a id="unreal.MoviePipelineExecutorBase.is_socket_connected"></a>

#### is_socket_connected

```python
def is_socket_connected() -> bool
```

x.is_socket_connected() -> bool
Returns true if the socket is currently connected, false otherwise. Call ConnectSocket to attempt a connection.

Returns:
    bool:

<a id="unreal.MoviePipelineExecutorBase.is_rendering"></a>

#### is_rendering

```python
def is_rendering() -> bool
```

x.is_rendering() -> bool
Report the current state of the executor. This is used to know if we can call Execute again.

For C++ implementations override `virtual bool IsRendering_Implementation() const override`
For Python/BP implementations override
unreal.ufunction(override=True): def is_rendering(self): return ?

Returns:
    bool: True if the executor is currently working on a queue to produce a render.

<a id="unreal.MoviePipelineExecutorBase.get_status_progress"></a>

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

<a id="unreal.MoviePipelineExecutorBase.get_status_message"></a>

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

<a id="unreal.MoviePipelineExecutorBase.execute"></a>

#### execute

```python
def execute(pipeline_queue: MoviePipelineQueue) -> None
```

x.execute(pipeline_queue) -> None
Execute the provided Queue. You are responsible for deciding how to handle each job
in the queue and processing them. OnExecutorFinished should be called when all jobs
are completed, which can report both success, warning, cancel, or error.

For C++ implementations override `virtual void Execute_Implementation() const override`
For Python/BP implementations override
unreal.ufunction(override=True): def execute(self):

Args:
    pipeline_queue (MoviePipelineQueue): The queue that this should process all jobs for. This can be null when using certain combination of command line render flags/scripting.

<a id="unreal.MoviePipelineExecutorBase.disconnect_socket"></a>

#### disconnect_socket

```python
def disconnect_socket() -> None
```

x.disconnect_socket() -> None
* Disconnects the socket (if currently connected.)

<a id="unreal.MoviePipelineExecutorBase.connect_socket"></a>

#### connect_socket

```python
def connect_socket(host_name: str, port: int) -> bool
```

x.connect_socket(host_name, port) -> bool
Attempts to connect a socket to the specified host and port. This is a blocking call.

Args:
    host_name (str): The host name as to connect to such as "127.0.0.1"
    port (int32): The port to attempt to connect to the host on.

Returns:
    bool: True if the socket was succesfully connected to the given host and port.

<a id="unreal.MoviePipelineExecutorBase.cancel_current_job"></a>

#### cancel_current_job

```python
def cancel_current_job() -> None
```

x.cancel_current_job() -> None
Abort the currently executing job.

<a id="unreal.MoviePipelineExecutorBase.cancel_all_jobs"></a>

#### cancel_all_jobs

```python
def cancel_all_jobs() -> None
```

x.cancel_all_jobs() -> None
Abort the currently executing job and skip all other jobs.

<a id="unreal.MoviePipelineFCPXMLExporter"></a>