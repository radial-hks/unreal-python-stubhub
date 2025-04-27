## MovieGraphSelectNode Objects

```python
class MovieGraphSelectNode(MovieGraphNode)
```

A node which creates a condition that selects from a set of input branches.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSelectNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``select_options`` (MovieGraphValueContainer):  [Read-Write] The options that are available on the node.
- ``selected_option`` (MovieGraphValueContainer):  [Read-Write] The currently selected option.

<a id="unreal.MovieGraphSequenceDataSource"></a>