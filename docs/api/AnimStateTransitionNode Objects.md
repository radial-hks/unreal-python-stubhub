## AnimStateTransitionNode Objects

```python
class AnimStateTransitionNode(AnimStateNodeBase)
```

Anim State Transition Node

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimStateTransitionNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``automatic_rule_based_on_sequence_player_in_state`` (bool):  [Read-Write] Try setting the rule automatically based on most relevant asset player node's remaining time and the Automatic Rule Trigger Time of the transition, ignoring the internal time
- ``automatic_rule_trigger_time`` (float):  [Read-Write] When should the automatic transition rule trigger relative to the time remaining on the relevant asset player:
   < 0 means trigger the transition 'Crossfade Duration' seconds before the end of the asset player, so a standard blend would finish just as the asset player ends
  >= 0 means trigger the transition 'Automatic Rule Trigger Time' seconds before the end of the asset player
- ``bidirectional`` (bool):  [Read-Write] This transition can go both directions
- ``blend_mode`` (AlphaBlendOption):  [Read-Write]
- ``blend_profile`` (BlendProfile):  [Read-Write] The blend profile to use to evaluate this transition per-bone
- ``crossfade_duration`` (float):  [Read-Write] The duration to cross-fade for
- ``custom_blend_curve`` (CurveFloat):  [Read-Write]
- ``logic_type`` (TransitionLogicType):  [Read-Write] What transition logic to use
- ``priority_order`` (int32):  [Read-Write] The priority order of this transition. If multiple transitions out of a state go
  true at the same time, the one with the smallest priority order will take precedent
- ``sync_group_name_to_require_valid_markers_rule`` (Name):  [Read-Write] If SyncGroupName is specified, Transition will only be taken if the SyncGroup has valid markers (other transition rules still apply in addition to that).
- ``transition_end`` (AnimNotifyEvent):  [Read-Write]
- ``transition_interrupt`` (AnimNotifyEvent):  [Read-Write]
- ``transition_start`` (AnimNotifyEvent):  [Read-Write]

<a id="unreal.AnimStateTransitionNode.logic_type"></a>

#### logic_type

```python
@property
def logic_type() -> TransitionLogicType
```

(TransitionLogicType):  [Read-Write] What transition logic to use

<a id="unreal.AnimStateTransitionNode.logic_type"></a>

#### logic_type

```python
@logic_type.setter
def logic_type(value: TransitionLogicType) -> None
```

<a id="unreal.AnimBlueprint"></a>