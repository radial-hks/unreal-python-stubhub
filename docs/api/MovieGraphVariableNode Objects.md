## MovieGraphVariableNode Objects

```python
class MovieGraphVariableNode(MovieGraphNode)
```

A node which gets the value of a variable which has been defined on the graph.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphVariableNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphVariableNode.set_variable"></a>

#### set_variable

```python
def set_variable(variable: MovieGraphVariable) -> None
```

x.set_variable(variable) -> None
Sets the variable that this node represents.

Args:
    variable (MovieGraphVariable):

<a id="unreal.MovieGraphVariableNode.get_variable"></a>

#### get_variable

```python
def get_variable() -> MovieGraphVariable
```

x.get_variable() -> MovieGraphVariable
Gets the variable that this node represents.

Returns:
    MovieGraphVariable:

<a id="unreal.MovieGraphWarmUpSettingNode"></a>