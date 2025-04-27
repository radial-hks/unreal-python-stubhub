## MovieGraphGlobalVariable Objects

```python
class MovieGraphGlobalVariable(MovieGraphVariable)
```

Similar to normal UMovieGraphVariable instances. However, their values are provided by the graph, they cannot be
edited/deleted, and they cannot be overridden at the job level.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (str):  [Read-Write] The optional description of this member, which is user-facing.
- ``value`` (InstancedPropertyBag):  [Read-Write] The value held by this object.

<a id="unreal.MovieGraphGlobalVariable_ShotName"></a>