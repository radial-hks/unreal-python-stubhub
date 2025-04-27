## MovieGraphRenderLayerNode Objects

```python
class MovieGraphRenderLayerNode(MovieGraphSettingNode)
```

Movie Graph Render Layer Node

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``layer_name`` (str):  [Read-Write]
- ``override_layer_name`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphRenderLayerNode.override_layer_name"></a>

#### override_layer_name

```python
@property
def override_layer_name() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphRenderLayerNode.override_layer_name"></a>

#### override_layer_name

```python
@override_layer_name.setter
def override_layer_name(value: bool) -> None
```

<a id="unreal.MovieGraphRenderLayerNode.layer_name"></a>

#### layer_name

```python
@property
def layer_name() -> str
```

(str):  [Read-Write]

<a id="unreal.MovieGraphRenderLayerNode.layer_name"></a>

#### layer_name

```python
@layer_name.setter
def layer_name(value: str) -> None
```

<a id="unreal.MovieGraphConditionGroupQueryBase"></a>