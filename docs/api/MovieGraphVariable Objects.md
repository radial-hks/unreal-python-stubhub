## MovieGraphVariable Objects

```python
class MovieGraphVariable(MovieGraphMember)
```

A variable that can be used inside the graph. Most variables are created by the user, and can have their value
changed at the job level. Global variables, however, are not user-created and their values are provided when the
graph is evaluated. Overriding them at the job level is not possible.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (str):  [Read-Write] The optional description of this member, which is user-facing.
- ``value`` (InstancedPropertyBag):  [Read-Write] The value held by this object.

<a id="unreal.MovieGraphGlobalVariable"></a>