## DummyRenderLayerOnlyNode Objects

```python
class DummyRenderLayerOnlyNode(MovieGraphSettingNode)
```

A dummy render layer only node. Currently MRG does not ship with any nodes which are restricted to just render layer branches, so this node
exists solely to test functionality of restricting nodes to just render layer branches (EMovieGraphBranchRestriction::RenderLayer). Can be removed
once a shipped node with this restriction exists.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineEditor
- **File**: MovieGraphEditorTestUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MoviePipelinePIEExecutorSettings"></a>