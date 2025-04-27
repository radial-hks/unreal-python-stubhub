## AnimNode_StateMachine Objects

```python
class AnimNode_StateMachine(AnimNode_Base)
```

State machine node

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_StateMachine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_conduit_entry_states`` (bool):  [Read-Write] Allows a conduit to be used as this state machine's entry state
  If a valid entry state cannot be found at runtime then this will generate a reference pose!
- ``create_notify_meta_data`` (bool):  [Read-Write] Tag Notifies with meta data such as the active state and mirroring state.  Producing this
  data has a  slight performance cost.
- ``max_transitions_per_frame`` (int32):  [Read-Write] The maximum number of transitions that can be taken by this machine 'simultaneously' in a single frame
- ``max_transitions_requests`` (int32):  [Read-Write] The maximum number of transition requests that can be buffered at any time.
  The oldest transition requests are dropped to accommodate for newly created requests.
- ``reinitialize_on_becoming_relevant`` (bool):  [Read-Write] Reinitialize the state machine if we have become relevant to the graph
  after not being ticked on the previous frame(s)
- ``skip_first_update_transition`` (bool):  [Read-Write] When the state machine becomes relevant, it is initialized into the Entry state.
  It then tries to take any valid transitions to possibly end up in a different state on that same frame.
  - if true, that new state starts full weight.
  - if false, a blend is created between the entry state and that new state.
  In either case all visited State notifications (Begin/End) will be triggered.

<a id="unreal.AnimNode_StateMachine.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.BoneNode"></a>