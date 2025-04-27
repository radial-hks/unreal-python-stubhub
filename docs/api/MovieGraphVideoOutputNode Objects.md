## MovieGraphVideoOutputNode Objects

```python
class MovieGraphVideoOutputNode(MovieGraphFileOutputNode)
```

A base node for nodes that generate video in the Movie Render Graph.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphVideoOutputNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``file_name_format`` (str):  [Read-Write] What format string should the final files use? Can include folder prefixes, and format string ({shot_name}, etc.)
- ``override_file_name_format`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MoviePipeline"></a>