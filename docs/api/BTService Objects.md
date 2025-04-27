## BTService Objects

```python
class BTService(BTAuxiliaryNode)
```

Behavior Tree service nodes is designed to perform "background" tasks that update AI's knowledge.

Services are being executed when underlying branch of behavior tree becomes active,
but unlike tasks they don't return any results and can't directly affect execution flow.

Usually they perform periodical checks (see TickNode) and often store results in blackboard.
If any decorator node below requires results of check beforehand, use OnSearchStart function.
Keep in mind that any checks performed there have to be instantaneous!

Other typical use case is creating a marker when specific branch is being executed
(see OnBecomeRelevant, OnCeaseRelevant), by setting a flag in blackboard.

Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
- OnBecomeRelevant (from UBTAuxiliaryNode)
- OnCeaseRelevant (from UBTAuxiliaryNode)
- TickNode (from UBTAuxiliaryNode)
- OnSearchStart

If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
Template nodes are shared across all behavior tree components using the same tree asset and must store
their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

**C++ Source:**

- **Module**: AIModule
- **File**: BTService.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``call_tick_on_search_start`` (bool):  [Read-Write] call Tick event when task search enters this node (SearchStart will be called as well)
- ``interval`` (float):  [Read-Write] defines time span between subsequent ticks of the service
- ``node_name`` (str):  [Read-Write] node name
- ``random_deviation`` (float):  [Read-Write] adds random range to service's Interval
- ``restart_timer_on_each_activation`` (bool):  [Read-Write] if set, next tick time will be always reset to service's interval when node is activated

<a id="unreal.BTService_BlueprintBase"></a>