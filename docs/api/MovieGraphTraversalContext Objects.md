## MovieGraphTraversalContext Objects

```python
class MovieGraphTraversalContext(StructBase)
```

Movie Graph Traversal Context

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphTraversalContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``job`` (MoviePipelineExecutorJob):  [Read-Write] The job in the queue this traversal context is for. Needed to fetch variable values from the job.
- ``render_data_identifier`` (MovieGraphRenderDataIdentifier):  [Read-Write] The name of the render resource this state was captured for.
- ``root_graph`` (MovieGraphConfig):  [Read-Write] The root graph to start our traversal from. This could be a shared config for the whole job, or a shot-specific override.
- ``shot`` (MoviePipelineExecutorShot):  [Read-Write] The shot in the queue this traversal context is for (if any).
- ``shot_count`` (int32):  [Read-Write] The total number of shots being rendered for this job. This is from the active shot list, not total in the Level Sequence.
- ``shot_index`` (int32):  [Read-Write] Which shot (out of ShotCount) is this time step for?
- ``time`` (MovieGraphTimeStepData):  [Read-Write] The time data(output frame, delta times, etc.)

<a id="unreal.MovieGraphTraversalContext.__init__"></a>

#### __init__

```python
def __init__(
    shot_index: int = 0,
    shot_count: int = 0,
    job: MoviePipelineExecutorJob = None,
    shot: MoviePipelineExecutorShot = None,
    root_graph: MovieGraphConfig = None,
    render_data_identifier: MovieGraphRenderDataIdentifier = [
        "None", "", "", "", ""
    ],
    time: MovieGraphTimeStepData = [
        0, 0, 0, 0.000000, 0.000000, 0.000000, 0.000000, [0, 0], 0, 0, 0, 0,
        False, False, False, False, None, [0, 0, 0, 0, 0.000000, False], [0],
        [0, 0, 0, 0, 0.000000, False], [0]
    ]
) -> None
```

<a id="unreal.MovieGraphTraversalContext.shot_index"></a>

#### shot_index

```python
@property
def shot_index() -> int
```

(int32):  [Read-Write] Which shot (out of ShotCount) is this time step for?

<a id="unreal.MovieGraphTraversalContext.shot_index"></a>

#### shot_index

```python
@shot_index.setter
def shot_index(value: int) -> None
```

<a id="unreal.MovieGraphTraversalContext.shot_count"></a>

#### shot_count

```python
@property
def shot_count() -> int
```

(int32):  [Read-Write] The total number of shots being rendered for this job. This is from the active shot list, not total in the Level Sequence.

<a id="unreal.MovieGraphTraversalContext.shot_count"></a>

#### shot_count

```python
@shot_count.setter
def shot_count(value: int) -> None
```

<a id="unreal.MovieGraphTraversalContext.job"></a>

#### job

```python
@property
def job() -> MoviePipelineExecutorJob
```

(MoviePipelineExecutorJob):  [Read-Write] The job in the queue this traversal context is for. Needed to fetch variable values from the job.

<a id="unreal.MovieGraphTraversalContext.job"></a>

#### job

```python
@job.setter
def job(value: MoviePipelineExecutorJob) -> None
```

<a id="unreal.MovieGraphTraversalContext.shot"></a>

#### shot

```python
@property
def shot() -> MoviePipelineExecutorShot
```

(MoviePipelineExecutorShot):  [Read-Write] The shot in the queue this traversal context is for (if any).

<a id="unreal.MovieGraphTraversalContext.shot"></a>

#### shot

```python
@shot.setter
def shot(value: MoviePipelineExecutorShot) -> None
```

<a id="unreal.MovieGraphTraversalContext.root_graph"></a>

#### root_graph

```python
@property
def root_graph() -> MovieGraphConfig
```

(MovieGraphConfig):  [Read-Write] The root graph to start our traversal from. This could be a shared config for the whole job, or a shot-specific override.

<a id="unreal.MovieGraphTraversalContext.root_graph"></a>

#### root_graph

```python
@root_graph.setter
def root_graph(value: MovieGraphConfig) -> None
```

<a id="unreal.MovieGraphTraversalContext.render_data_identifier"></a>

#### render_data_identifier

```python
@property
def render_data_identifier() -> MovieGraphRenderDataIdentifier
```

(MovieGraphRenderDataIdentifier):  [Read-Write] The name of the render resource this state was captured for.

<a id="unreal.MovieGraphTraversalContext.render_data_identifier"></a>

#### render_data_identifier

```python
@render_data_identifier.setter
def render_data_identifier(value: MovieGraphRenderDataIdentifier) -> None
```

<a id="unreal.MovieGraphTraversalContext.time"></a>

#### time

```python
@property
def time() -> MovieGraphTimeStepData
```

(MovieGraphTimeStepData):  [Read-Write] The time data(output frame, delta times, etc.)

<a id="unreal.MovieGraphTraversalContext.time"></a>

#### time

```python
@time.setter
def time(value: MovieGraphTimeStepData) -> None
```

<a id="unreal.MovieGraphTimeStepData"></a>