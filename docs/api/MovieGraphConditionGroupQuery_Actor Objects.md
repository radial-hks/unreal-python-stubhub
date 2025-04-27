## MovieGraphConditionGroupQuery_Actor Objects

```python
class MovieGraphConditionGroupQuery_Actor(MovieGraphConditionGroupQueryBase)
```

Query type which filters actors via an explicit actor list.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actors_to_match`` (Array[Actor]):  [Read-Write] The query must match one of the actors in order to be a match. If these are editor actors, they will be converted to PIE actors automatically.

<a id="unreal.MovieGraphConditionGroupQuery_ActorTagName"></a>