## MovieGraphBranchRestriction Objects

```python
class MovieGraphBranchRestriction(EnumBase)
```

Describes a restriction on what kind of branch a node can be created in within the graph.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphNode.h

<a id="unreal.MovieGraphBranchRestriction.ANY"></a>

#### ANY

0

<a id="unreal.MovieGraphBranchRestriction.GLOBALS"></a>

#### GLOBALS

1: < The node can be created in any type of branch

<a id="unreal.MovieGraphBranchRestriction.RENDER_LAYER"></a>

#### RENDER_LAYER

2: < The node must be created in the Globals branch

<a id="unreal.MovieGraphPinQueryRequirement"></a>