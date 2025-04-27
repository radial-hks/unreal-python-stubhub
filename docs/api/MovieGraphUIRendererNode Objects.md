## MovieGraphUIRendererNode Objects

```python
class MovieGraphUIRendererNode(MovieGraphWidgetRendererBaseNode)
```

A node which renders the viewport's UMG widget to a standalone image, or composited on top of a render layer.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphUIRendererNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``composite_onto_final_image`` (bool):  [Read-Write] If true, the pass will be composited onto each render. Does not apply to multi-layer EXR files.
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_b_composite_onto_final_image`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphVariableNode"></a>