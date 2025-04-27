## AnimNode_SequencePlayer_Standalone Objects

```python
class AnimNode_SequencePlayer_Standalone(AnimNode_SequencePlayerBase)
```

Sequence player node that can be used standalone (without constant folding)

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_SequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group).
- ``group_role`` (AnimGroupRole):  [Read-Write] The role this node can assume within the group (ignored if GroupName is not set)
- ``ignore_for_relevancy_test`` (bool):  [Read-Write] If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``loop_animation`` (bool):  [Read-Write] Should the animation loop back to the start when it reaches the end?
- ``method`` (AnimSyncMethod):  [Read-Write] How this node will synchronize with other animations.
- ``override_position_when_joining_sync_group_as_leader`` (bool):  [Read-Only] When enabled, acting as the leader, and using marker-based sync, this asset player will not sync to the previous leader's sync position when joining a sync group and before becoming the leader but instead force everyone else to match its position.
- ``play_rate`` (float):  [Read-Write] The play rate multiplier. Can be negative, which will cause the animation to play in reverse.
- ``play_rate_basis`` (float):  [Read-Write] The Basis in which the PlayRate is expressed in. This is used to rescale PlayRate inputs.
  For example a Basis of 100 means that the PlayRate input will be divided by 100.
- ``play_rate_scale_bias_clamp_constants`` (InputScaleBiasClampConstants):  [Read-Write] Additional scaling, offsetting and clamping of PlayRate input.
  Performed after PlayRateBasis.
- ``sequence`` (AnimSequenceBase):  [Read-Write] The animation sequence asset to play
- ``start_from_matching_pose`` (bool):  [Read-Write] Use pose matching to choose the start position. Requires experimental PoseSearch plugin.
- ``start_position`` (float):  [Read-Write] The start position between 0 and the length of the sequence to use when initializing. When looping, play will still jump back to the beginning when reaching the end.

<a id="unreal.AnimNode_SequencePlayer_Standalone.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000) -> None
```

<a id="unreal.AnimNode_StateResult"></a>