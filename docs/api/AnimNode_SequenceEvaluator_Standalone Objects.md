## AnimNode_SequenceEvaluator_Standalone Objects

```python
class AnimNode_SequenceEvaluator_Standalone(AnimNode_SequenceEvaluatorBase)
```

Sequence evaluator node that can be used standalone (without constant folding)

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_SequenceEvaluator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``explicit_frame`` (int32):  [Read-Write]
- ``explicit_time`` (float):  [Read-Write] The time at which to evaluate the associated sequence
- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group).
- ``group_role`` (AnimGroupRole):  [Read-Write] The role this node can assume within the group (ignored if GroupName is not set)
- ``ignore_for_relevancy_test`` (bool):  [Read-Write] If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``method`` (AnimSyncMethod):  [Read-Write] How this node will synchronize with other animations.
- ``reinitialization_behavior`` (SequenceEvalReinit):  [Read-Write] What to do when SequenceEvaluator is reinitialized
- ``sequence`` (AnimSequenceBase):  [Read-Write] The animation sequence asset to evaluate
- ``should_loop`` (bool):  [Read-Write] This only works if bTeleportToExplicitTime is false OR this node is set to use SyncGroup
- ``start_position`` (float):  [Read-Write] The start up position, it only applies when ReinitializationBehavior == StartPosition. Only used when bTeleportToExplicitTime is false.
- ``teleport_to_explicit_time`` (bool):  [Read-Write] If true, teleport to explicit time, does NOT advance time (does not trigger notifies, does not extract Root Motion, etc.)
        If false, will advance time (will trigger notifies, extract root motion if applicable, etc.)
        Note: using a sync group forces advancing time regardless of what this option is set to.
- ``use_explicit_frame`` (bool):  [Read-Write]

<a id="unreal.AnimNode_SequenceEvaluator_Standalone.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000) -> None
```

<a id="unreal.AnimNode_Slot"></a>