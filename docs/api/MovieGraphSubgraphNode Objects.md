## MovieGraphSubgraphNode Objects

```python
class MovieGraphSubgraphNode(MovieGraphNode)
```

A node which represents another graph asset. Inputs/outputs on this subgraph will update if the underlying graph
asset's inputs/outputs change.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSubgraphNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``subgraph_asset`` (MovieGraphConfig):  [Read-Write]

<a id="unreal.MovieGraphSubgraphNode.set_sub_graph_asset"></a>

#### set_sub_graph_asset

```python
def set_sub_graph_asset(subgraph_asset: MovieGraphConfig) -> None
```

x.set_sub_graph_asset(subgraph_asset) -> None
Sets the graph asset this subgraph points to.

Args:
    subgraph_asset (MovieGraphConfig):

<a id="unreal.MovieGraphSubgraphNode.get_subgraph_asset"></a>

#### get_subgraph_asset

```python
def get_subgraph_asset() -> MovieGraphConfig
```

x.get_subgraph_asset() -> MovieGraphConfig
Gets the graph asset this subgraph points to.

Returns:
    MovieGraphConfig:

<a id="unreal.MovieGraphUIRendererNode"></a>