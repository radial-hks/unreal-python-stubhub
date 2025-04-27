## MovieGraphRenderPassNode Objects

```python
class MovieGraphRenderPassNode(MovieGraphSettingNode)
```

The UMovieGraphRenderPassNode node defines a render pass that MRQ may produce. This node can be implemented
in the graph multiple times, and the exact settings it should use can be created out of a mixture of nodes. Because
of this, when rendering, MRQ will figure out how many layers there are that actually use this CDO and will call
the function on the CDO once, providing the information about all instances. This will allow the node to create any
number of instances (decoupled from the number of times the node is used in the graph).

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderPassNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphWidgetRendererBaseNode"></a>