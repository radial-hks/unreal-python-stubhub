## StateTreeTransition Objects

```python
class StateTreeTransition(StructBase)
```

Editor representation of a transition in StateTree

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeEditorModule
- **File**: StateTreeState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``conditions`` (Array[StateTreeEditorNode]):  [Read-Write] Expression of conditions that need to evaluate to true to allow transition to be triggered.
- ``delay_duration`` (float):  [Read-Write] Transition delay duration in seconds.
- ``delay_random_variance`` (float):  [Read-Write] Transition delay random variance in seconds.
- ``delay_transition`` (bool):  [Read-Write] Delay the triggering of the transition.
- ``id`` (Guid):  [Read-Write]
- ``priority`` (StateTreeTransitionPriority):  [Read-Write] Transition priority when multiple transitions happen at the same time.
  During transition handling, the transitions are visited from leaf to root.
  The first visited transition, of highest priority, that leads to a state selection, will be activated.
- ``required_event`` (StateTreeEventDesc):  [Read-Write] Defines the event required to be present during state selection for the transition to trigger.
- ``state`` (StateTreeStateLink):  [Read-Write] Transition target state.
- ``transition_enabled`` (bool):  [Read-Write] True if the Transition is Enabled (i.e. not explicitly disabled in the asset).
- ``trigger`` (StateTreeTransitionTrigger):  [Read-Write] When to try trigger the transition.

<a id="unreal.StateTreeTransition.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.StateTreeTransition2"></a>