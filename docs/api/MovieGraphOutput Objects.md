## MovieGraphOutput Objects

```python
class MovieGraphOutput(MovieGraphInterfaceBase)
```

An output exposed on the graph that will be available for nodes to connect to.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (str):  [Read-Write] The optional description of this member, which is user-facing.
- ``is_branch`` (bool):  [Read-Write] Whether this interface member represents a branch. If not a branch, then a value is associated with it.
- ``value`` (InstancedPropertyBag):  [Read-Write] The value held by this object.

<a id="unreal.MovieGraphEvaluatedConfig"></a>