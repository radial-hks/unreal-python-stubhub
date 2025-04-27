## AvaTransitionTreeEditorData Objects

```python
class AvaTransitionTreeEditorData(StateTreeEditorData)
```

Ava Transition Tree Editor Data

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheTransitionEditor
- **File**: AvaTransitionTreeEditorData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``colors`` (Set[StateTreeEditorColor]):  [Read-Write] Color Options to assign to a State
- ``evaluators`` (Array[StateTreeEditorNode]):  [Read-Write]
- ``global_tasks`` (Array[StateTreeEditorNode]):  [Read-Write]
- ``root_parameters`` (StateTreeStateParameters):  [Read-Write] Public parameters that could be used for bindings within the Tree.
- ``schema`` (StateTreeSchema):  [Read-Write] Schema describing which inputs, evaluators, and tasks a StateTree can contain
- ``transition_layer`` (AvaTagHandle):  [Read-Write] The Layer this Transition Logic Tree deals with

<a id="unreal.AvaTransitionTreeFactory"></a>