## MoviePipelineQueue Objects

```python
class MoviePipelineQueue(Object)
```

A queue is a list of jobs that have been executed, are executing and are waiting to be executed. These can be saved
to specific assets to allow

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineQueue.h

<a id="unreal.MoviePipelineQueue.set_queue_origin"></a>

#### set_queue_origin

```python
def set_queue_origin(config: MoviePipelineQueue) -> None
```

x.set_queue_origin(config) -> None
Sets the queue that this queue originated from (if any). The origin should only be set for transient queues.

Args:
    config (MoviePipelineQueue):

<a id="unreal.MoviePipelineQueue.set_job_index"></a>

#### set_job_index

```python
def set_job_index(job: MoviePipelineExecutorJob, index: int) -> None
```

x.set_job_index(job, index) -> None
Set the index of the given job

Args:
    job (MoviePipelineExecutorJob): 
    index (int32):

<a id="unreal.MoviePipelineQueue.set_is_dirty"></a>

#### set_is_dirty

```python
def set_is_dirty(new_dirty_state: bool) -> None
```

x.set_is_dirty(new_dirty_state) -> None
Sets the dirty state of this queue. Generally the queue will correctly track the dirty state; however, there are
situations where a queue may need its dirty state reset (eg, it may be appropriate to reset the dirty state after
a call to CopyFrom(), depending on the use case).

Args:
    new_dirty_state (bool):

<a id="unreal.MoviePipelineQueue.is_dirty"></a>

#### is_dirty

```python
def is_dirty() -> bool
```

x.is_dirty() -> bool
Gets the dirty state of this queue. Note that dirty state is only tracked when the editor is active.

Returns:
    bool:

<a id="unreal.MoviePipelineQueue.get_queue_origin"></a>

#### get_queue_origin

```python
def get_queue_origin() -> MoviePipelineQueue
```

x.get_queue_origin() -> MoviePipelineQueue
Gets the queue that this queue was originally based on (if any). The origin will only be set on transient
queues; the origin will be nullptr for non-transient queues because the origin will be this object.

Returns:
    MoviePipelineQueue:

<a id="unreal.MoviePipelineQueue.get_jobs"></a>

#### get_jobs

```python
def get_jobs() -> Array[MoviePipelineExecutorJob]
```

x.get_jobs() -> Array[MoviePipelineExecutorJob]
Get all of the Jobs contained in this Queue.

Returns:
    Array[MoviePipelineExecutorJob]: The jobs contained by this queue.

<a id="unreal.MoviePipelineQueue.duplicate_job"></a>

#### duplicate_job

```python
def duplicate_job(job: MoviePipelineExecutorJob) -> MoviePipelineExecutorJob
```

x.duplicate_job(job) -> MoviePipelineExecutorJob
Duplicate the specific job and return the duplicate. Configurations are duplicated and not shared.

Args:
    job (MoviePipelineExecutorJob): The job to look for to duplicate.

Returns:
    MoviePipelineExecutorJob: The duplicated instance or nullptr if a duplicate could not be made.

<a id="unreal.MoviePipelineQueue.delete_job"></a>

#### delete_job

```python
def delete_job(job: MoviePipelineExecutorJob) -> None
```

x.delete_job(job) -> None
Deletes the specified job from the Queue.

Args:
    job (MoviePipelineExecutorJob): The job to look for and delete.

<a id="unreal.MoviePipelineQueue.delete_all_jobs"></a>

#### delete_all_jobs

```python
def delete_all_jobs() -> None
```

x.delete_all_jobs() -> None
Delete all jobs from the Queue.

<a id="unreal.MoviePipelineQueue.copy_from"></a>

#### copy_from

```python
def copy_from(queue: MoviePipelineQueue) -> MoviePipelineQueue
```

x.copy_from(queue) -> MoviePipelineQueue
Replace the contents of this queue with a copy of the contents from another queue.
Returns a pointer to this queue if the copy was successful, else nullptr.

Args:
    queue (MoviePipelineQueue): 

Returns:
    MoviePipelineQueue:

<a id="unreal.MoviePipelineQueue.allocate_new_job"></a>

#### allocate_new_job

```python
def allocate_new_job(job_type: Class = None) -> MoviePipelineExecutorJob
```

x.allocate_new_job(job_type=None) -> MoviePipelineExecutorJob
Allocates a new Job in this Queue. The Queue owns the jobs for memory management purposes,
and this will handle that for you.

Args:
    job_type (type(Class)): Specify the specific Job type that should be created. Custom Executors can use custom Job types to allow the user to provide more information.

Returns:
    MoviePipelineExecutorJob: The created Executor job instance.

<a id="unreal.MoviePipelineQueueEngineSubsystem"></a>