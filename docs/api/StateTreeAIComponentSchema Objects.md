## StateTreeAIComponentSchema Objects

```python
class StateTreeAIComponentSchema(StateTreeComponentSchema)
```

State tree schema to be used with StateTreeAIComponent.
It guarantees access to an AIController and the Actor context value can be used to access the controlled pawn.

**C++ Source:**

- **Plugin**: GameplayStateTree
- **Module**: GameplayStateTreeModule
- **File**: StateTreeAIComponentSchema.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ai_controller_class`` (type(Class)):  [Read-Write] AIController class the StateTree is expected to run on. Allows to bind to specific Actor class' properties.
- ``context_actor_class`` (type(Class)):  [Read-Write] Actor class the StateTree is expected to run on. Allows to bind to specific Actor class' properties.

<a id="unreal.GeometryScriptDebug"></a>