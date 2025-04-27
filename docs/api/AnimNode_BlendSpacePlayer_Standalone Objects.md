## AnimNode_BlendSpacePlayer_Standalone Objects

```python
class AnimNode_BlendSpacePlayer_Standalone(AnimNode_BlendSpacePlayerBase)
```

TODO:: Comment

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendSpacePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_space`` (BlendSpace):  [Read-Write] The blendspace asset to play
- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group). Note that
  this is the name of the group used to sync the output of this node - it will not force
  syncing of animations contained by it. Animations inside this Blend Space have their own
  options for syncing.
- ``group_role`` (AnimGroupRole):  [Read-Write] The role this Blend Space can assume within the group (ignored if GroupName is not set). Note
  that this is the role of the output of this node, not of animations contained by it.
- ``ignore_for_relevancy_test`` (bool):  [Read-Write] If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``loop`` (bool):  [Read-Write] Should the animation loop back to the start when it reaches the end?
- ``method`` (AnimSyncMethod):  [Read-Write] How this asset will synchronize with other assets. Note that this determines how the output
  of this node is used for synchronization, not of animations contained by it.
- ``override_position_when_joining_sync_group_as_leader`` (bool):  [Read-Only] When enabled, acting as the leader, and using marker-based sync, this asset player will not sync to the previous leader's sync position when joining a sync group and before becoming the leader but instead force everyone else to match its position.
- ``play_rate`` (float):  [Read-Write] The play rate multiplier. Can be negative, which will cause the animation to play in reverse.
- ``reset_play_time_when_blend_space_changes`` (bool):  [Read-Write] Whether we should reset the current play time when the blend space changes
- ``start_position`` (float):  [Read-Write] The start position in [0, 1] to use when initializing. When looping, play will still jump back to the beginning when reaching the end.
- ``x`` (float):  [Read-Write] The X coordinate to sample in the blendspace
- ``y`` (float):  [Read-Write] The Y coordinate to sample in the blendspace

<a id="unreal.AnimNode_BlendSpacePlayer_Standalone.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000) -> None
```

<a id="unreal.AnimNode_CallFunction"></a>