## MovieGraphRenderLayerOutputData Objects

```python
class MovieGraphRenderLayerOutputData(StructBase)
```

Movie Graph Render Layer Output Data

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderDataIdentifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``file_paths`` (Array[str]):  [Read-Only] A list of file paths on disk (in order) that were generated for this particular render pass.

<a id="unreal.MovieGraphRenderLayerOutputData.__init__"></a>

#### __init__

```python
def __init__(file_paths: Array[str] = []) -> None
```

<a id="unreal.MovieGraphRenderLayerOutputData.file_paths"></a>

#### file_paths

```python
@property
def file_paths() -> Array[str]
```

(Array[str]):  [Read-Only] A list of file paths on disk (in order) that were generated for this particular render pass.

<a id="unreal.MoviePipelineShotOutputData"></a>