## BTDecorator Objects

```python
class BTDecorator(BTAuxiliaryNode)
```

Decorators are supporting nodes placed on parent-child connection, that receive notification about execution flow and can be ticked

Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
 - OnNodeActivation
 - OnNodeDeactivation
 - OnNodeProcessed
 - OnBecomeRelevant (from UBTAuxiliaryNode)
 - OnCeaseRelevant (from UBTAuxiliaryNode)
 - TickNode (from UBTAuxiliaryNode)

If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
Template nodes are shared across all behavior tree components using the same tree asset and must store
their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

**C++ Source:**

- **Module**: AIModule
- **File**: BTDecorator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flow_abort_mode`` (BTFlowAbortMode):  [Read-Write] flow controller settings
- ``inverse_condition`` (bool):  [Read-Write] if set, condition check result will be inversed
- ``node_name`` (str):  [Read-Write] node name

<a id="unreal.BTDecorator_BlueprintBase"></a>