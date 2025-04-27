## MoviePipelineShotOutputData Objects

```python
class MoviePipelineShotOutputData(StructBase)
```

Movie Pipeline Shot Output Data

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieRenderPipelineDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``render_pass_data`` (Map[MoviePipelinePassIdentifier, MoviePipelineRenderPassOutputData]):  [Read-Only] A mapping between render passes (such as 'FinalImage') and an array containing the files written for that shot.
  Will be multiple files if using image sequences.
- ``shot`` (MoviePipelineExecutorShot):  [Read-Only] Which shot was this output data for?

<a id="unreal.MoviePipelineShotOutputData.__init__"></a>

#### __init__

```python
def __init__(
    shot: MoviePipelineExecutorShot = None,
    render_pass_data: Map[MoviePipelinePassIdentifier,
                          MoviePipelineRenderPassOutputData] = {}
) -> None
```

<a id="unreal.MoviePipelineShotOutputData.shot"></a>

#### shot

```python
@property
def shot() -> MoviePipelineExecutorShot
```

(MoviePipelineExecutorShot):  [Read-Only] Which shot was this output data for?

<a id="unreal.MoviePipelineShotOutputData.render_pass_data"></a>

#### render_pass_data

```python
@property
def render_pass_data(
) -> Map[MoviePipelinePassIdentifier, MoviePipelineRenderPassOutputData]
```

(Map[MoviePipelinePassIdentifier, MoviePipelineRenderPassOutputData]):  [Read-Only] A mapping between render passes (such as 'FinalImage') and an array containing the files written for that shot.
Will be multiple files if using image sequences.

<a id="unreal.MoviePipelinePassIdentifier"></a>