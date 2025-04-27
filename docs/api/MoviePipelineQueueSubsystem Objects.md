## MoviePipelineQueueSubsystem Objects

```python
class MoviePipelineQueueSubsystem(EditorSubsystem)
```

Movie Pipeline Queue Subsystem

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineEditor
- **File**: MoviePipelineQueueSubsystem.h

<a id="unreal.MoviePipelineQueueSubsystem.render_queue_with_executor_instance"></a>

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

<a id="unreal.MoviePipelineQueueSubsystem.render_queue_with_executor"></a>

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

<a id="unreal.MoviePipelineQueueSubsystem.load_queue"></a>

#### load_queue

```python
def load_queue(queue_to_load: MoviePipelineQueue,
               prompt_on_replacing_dirty_queue: bool = True) -> bool
```

x.load_queue(queue_to_load, prompt_on_replacing_dirty_queue=True) -> bool
Loads a new queue by copying it into the queue subsystem's current transient queue (the one returned by GetQueue()).

If bPromptOnReplacingDirtyQueue is true and the current queue has been modified since being loaded, a dialog will prompt the
user if they want to discard their changes. If this dialog is rejected, or there was an error loading the queue, returns
false, else returns true. Note that bPromptOnReplacingDirtyQueue is effectively ignored if the application is in
"unattended" mode because the dialog is auto-accepted.

Args:
    queue_to_load (MoviePipelineQueue): 
    prompt_on_replacing_dirty_queue (bool): 

Returns:
    bool:

<a id="unreal.MoviePipelineQueueSubsystem.is_rendering"></a>

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

<a id="unreal.MoviePipelineQueueSubsystem.is_queue_dirty"></a>

#### is_queue_dirty

```python
def is_queue_dirty() -> bool
```

x.is_queue_dirty() -> bool
Returns true if the current queue has been modified since it was loaded, else returns false. Note that the empty
queue that is in use upon the initial load of MRQ is not considered dirty.

Returns:
    bool:

<a id="unreal.MoviePipelineQueueSubsystem.get_queue"></a>

#### get_queue

```python
def get_queue() -> MoviePipelineQueue
```

x.get_queue() -> MoviePipelineQueue
Returns the queue of Movie Pipelines that need to be rendered.

Returns:
    MoviePipelineQueue:

<a id="unreal.MoviePipelineQueueSubsystem.get_active_executor"></a>

#### get_active_executor

```python
def get_active_executor() -> MoviePipelineExecutorBase
```

x.get_active_executor() -> MoviePipelineExecutorBase
Returns the active executor (if there is one). This can be used to subscribe to events on an already in-progress render. May be null.

Returns:
    MoviePipelineExecutorBase:

<a id="unreal.MovieRenderPipelineProjectSettings"></a>