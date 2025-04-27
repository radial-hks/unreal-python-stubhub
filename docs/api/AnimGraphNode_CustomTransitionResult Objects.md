## AnimGraphNode_CustomTransitionResult Objects

```python
class AnimGraphNode_CustomTransitionResult(AnimGraphNode_StateResult)
```

Anim Graph Node Custom Transition Result

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimGraphNode_CustomTransitionResult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``become_relevant_function`` (MemberReference):  [Read-Write] Function called when the node becomes relevant, meaning it goes from having no weight to any weight.
- ``binding`` (AnimGraphNodeBinding):  [Read-Write] Bindings for pins that this node exposes
- ``initial_update_function`` (MemberReference):  [Read-Write] Function called before the node is updated for the first time
- ``node`` (AnimNode_StateResult):  [Read-Write]
- ``show_pin_for_properties`` (Array[OptionalPinFromProperty]):  [Read-Write]
- ``state_entry_function`` (MemberReference):  [Read-Write] Function called when the owning state is entered, meaning it becomes the state machine's current state.
- ``state_exit_function`` (MemberReference):  [Read-Write] Function called when the owning state is exited, meaning it stops being the state machine's current state.

  Notes:
  - This will not be called if the state machine node loses relevancy. Please use "On State Interrupt" for that case.
- ``state_fully_blended_in_function`` (MemberReference):  [Read-Write] Function called when the owning state is fully blended in.

  Notes:
  - This is only called for the state machine's current state since its the most recent transition's target state.
  - This will not be called if the state is skipped. This can happen when the flag bSkipFirstUpdateTransition on the state machine node is set to true.
- ``state_fully_blended_out_function`` (MemberReference):  [Read-Write] Function called when the owning state is fully blended out.

  Notes:
  - This will be called for any states that had weight.
  - This will not be called if the state is skipped. This can happen when the flag bSkipFirstUpdateTransition on the state machine node is set to true.
  - This will not be called if the state machine node loses relevancy. Please use "On State Interrupt" for that case.
- ``tag`` (Name):  [Read-Write] Optional reference tag name. If this is set then this node can be referenced from elsewhere in this animation blueprint using an anim node reference
- ``update_function`` (MemberReference):  [Read-Write] Function called when the node is updated

<a id="unreal.AnimGraphNode_DeadBlending"></a>