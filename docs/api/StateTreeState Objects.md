## StateTreeState Objects

```python
class StateTreeState(Object)
```

Editor representation of a state in StateTree

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeEditorModule
- **File**: StateTreeState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``check_prerequisites_when_activating_child_directly`` (bool):  [Read-Write] Should state's required event and enter conditions be evaluated when transition leads directly to it's child.
- ``color_ref`` (StateTreeEditorColorRef):  [Read-Write] Display color of the State
- ``considerations`` (Array[StateTreeEditorNode]):  [Read-Write] Expression of enter conditions that needs to evaluate true to allow the state to be selected.
- ``enabled`` (bool):  [Read-Write]
- ``enter_conditions`` (Array[StateTreeEditorNode]):  [Read-Write] Expression of enter conditions that needs to evaluate true to allow the state to be selected.
- ``has_required_event_to_enter`` (bool):  [Read-Write]
- ``id`` (Guid):  [Read-Write]
- ``linked_asset`` (StateTree):  [Read-Write] Another State Tree asset to run as extension of this State.
- ``linked_subtree`` (StateTreeStateLink):  [Read-Write] Subtree to run as extension of this State.
- ``name`` (Name):  [Read-Write] Display name of the State
- ``parameters`` (StateTreeStateParameters):  [Read-Write] Parameters of this state. If the state is linked to another state or asset, the parameters are for the linked state.
- ``required_event_to_enter`` (StateTreeEventDesc):  [Read-Write] Defines the event required to be present during state selection for the state to be selected.
- ``selection_behavior`` (StateTreeStateSelectionBehavior):  [Read-Write] How to treat child states when this State is selected.
- ``single_task`` (StateTreeEditorNode):  [Read-Write] Single item used when schema calls for single task per state.
- ``tag`` (GameplayTag):  [Read-Write] GameplayTag describing the State
- ``tasks`` (Array[StateTreeEditorNode]):  [Read-Write]
- ``transitions`` (Array[StateTreeTransition]):  [Read-Write]
- ``type`` (StateTreeStateType):  [Read-Write] Type the State, allows e.g. states to be linked to other States.
- ``weight`` (float):  [Read-Write] Weight used to scale the normalized final utility score for this state

<a id="unreal.AudioImpulseResponse"></a>