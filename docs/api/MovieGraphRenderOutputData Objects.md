## MovieGraphRenderOutputData Objects

```python
class MovieGraphRenderOutputData(StructBase)
```

Movie Graph Render Output Data

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderDataIdentifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``render_layer_data`` (Map[MovieGraphRenderDataIdentifier, MovieGraphRenderLayerOutputData]):  [Read-Only] A mapping between render layers (such as "beauty") and an array containing the files written for that shot.
  Will be multiple files if using image sequences.
- ``shot`` (MoviePipelineExecutorShot):  [Read-Only] Which shot is this output data for.

<a id="unreal.MovieGraphRenderOutputData.__init__"></a>

#### __init__

```python
def __init__(
    shot: MoviePipelineExecutorShot = None,
    render_layer_data: Map[MovieGraphRenderDataIdentifier,
                           MovieGraphRenderLayerOutputData] = {}
) -> None
```

<a id="unreal.MovieGraphRenderOutputData.shot"></a>

#### shot

```python
@property
def shot() -> MoviePipelineExecutorShot
```

(MoviePipelineExecutorShot):  [Read-Only] Which shot is this output data for.

<a id="unreal.MovieGraphRenderOutputData.render_layer_data"></a>

#### render_layer_data

```python
@property
def render_layer_data(
) -> Map[MovieGraphRenderDataIdentifier, MovieGraphRenderLayerOutputData]
```

(Map[MovieGraphRenderDataIdentifier, MovieGraphRenderLayerOutputData]):  [Read-Only] A mapping between render layers (such as "beauty") and an array containing the files written for that shot.
Will be multiple files if using image sequences.

<a id="unreal.MovieGraphRenderDataIdentifier"></a>