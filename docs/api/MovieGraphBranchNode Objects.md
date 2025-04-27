## MovieGraphBranchNode Objects

```python
class MovieGraphBranchNode(MovieGraphNode)
```

A node which creates a True/False branching condition. A user Graph Variable can be plugged
into the conditional pin and this will be evaluated when flattening the graph, choosing which
branch path to follow.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphBranchNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphRenderPassNode"></a>