## StateTreeEditorData Objects

```python
class StateTreeEditorData(Object)
```

Edit time data for StateTree asset. This data gets baked into runtime format before being used by the StateTreeInstance.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeEditorModule
- **File**: StateTreeEditorData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``colors`` (Set[StateTreeEditorColor]):  [Read-Write] Color Options to assign to a State
- ``evaluators`` (Array[StateTreeEditorNode]):  [Read-Write]
- ``global_tasks`` (Array[StateTreeEditorNode]):  [Read-Write]
- ``root_parameters`` (StateTreeStateParameters):  [Read-Write] Public parameters that could be used for bindings within the Tree.
- ``schema`` (StateTreeSchema):  [Read-Write] Schema describing which inputs, evaluators, and tasks a StateTree can contain

<a id="unreal.StateTreeFactory"></a>