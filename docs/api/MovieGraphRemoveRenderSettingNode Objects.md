## MovieGraphRemoveRenderSettingNode Objects

```python
class MovieGraphRemoveRenderSettingNode(MovieGraphNode)
```

A node which can remove other nodes in the graph.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRemoveRenderSettingNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``node_type`` (type(Class)):  [Read-Write] The type of node (exact match) that should be removed.
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphRemoveRenderSettingNode.node_type"></a>

#### node_type

```python
@property
def node_type() -> Class
```

(type(Class)):  [Read-Write] The type of node (exact match) that should be removed.

<a id="unreal.MovieGraphRemoveRenderSettingNode.node_type"></a>

#### node_type

```python
@node_type.setter
def node_type(value: Class) -> None
```

<a id="unreal.MovieGraphRenderLayerNode"></a>