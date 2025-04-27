## AvaTransitionTaskBlueprint Objects

```python
class AvaTransitionTaskBlueprint(StateTreeTaskBlueprintBase)
```

Ava Transition Task Blueprint

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheTransition
- **File**: AvaTransitionTaskBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (Text):  [Read-Write] Description of the node.
- ``icon_color`` (Color):  [Read-Write] Color of the icon.
- ``icon_name`` (Name):  [Read-Write] Name of the icon in format:
               StyleSetName | StyleName [ | SmallStyleName | StatusOverlayStyleName]
               SmallStyleName and StatusOverlayStyleName are optional.
               Example: "StateTreeEditorStyle|Node.Animation"
- ``should_call_tick_only_on_events`` (bool):  [Read-Write] If set to true, Tick() is called. Default false.
- ``should_copy_bound_properties_on_exit_state`` (bool):  [Read-Write] If set to true, copy the values of bound properties before calling ExitState(). Default true.
- ``should_copy_bound_properties_on_tick`` (bool):  [Read-Write] If set to true, copy the values of bound properties before calling Tick(). Default true.
- ``should_state_change_on_reselect`` (bool):  [Read-Write] If set to true, the task will receive EnterState/ExitState even if the state was previously active.
  Generally this should be true for action type tasks, like playing animation,
  and false on state like tasks like claiming a resource that is expected to be acquired on child states.

<a id="unreal.AvaTransitionTree"></a>