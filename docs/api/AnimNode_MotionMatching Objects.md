## AnimNode_MotionMatching Objects

```python
class AnimNode_MotionMatching(AnimNode_BlendStack_Standalone)
```

Anim Node Motion Matching

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: AnimNode_MotionMatching.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_option`` (AlphaBlendOption):  [Read-Write] How the blend is applied over time to the bones. Common selections are linear, ease in, ease out, and ease in and out.
- ``blend_parameters`` (Vector):  [Read-Write] requested blend space blend parameters (if AnimationAsset is a blend space)
- ``blend_parameters_delta_threshold`` (float):  [Read-Write] Use this to define a threshold to trigger a new blend when blendspace xy input pins change.
  By default, any delta will trigger a blend.
- ``blend_profile`` (BlendProfile):  [Read-Write] Set Blend Profiles (editable in the skeleton) to determine how the blending is distributed among your character's bones. It could be used to differentiate between upper body and lower body to blend timing.
- ``blend_time`` (float):  [Read-Write] Time in seconds to blend out to the new pose. Uses either inertial blending, requiring an Inertialization node after this node, or the internal blend stack, if MaxActiveBlends is greater than zero.
- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``blendspace_update_mode`` (BlendStack_BlendspaceUpdateMode):  [Read-Write] How we should update individual blend space parameters. See dropdown options tooltips.
- ``database`` (PoseSearchDatabase):  [Read-Write] The database to search. This can be overridden by Anim Node Functions such as "On Become Relevant" and "On Update" via SetDatabaseToSearch/SetDatabasesToSearch.
- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group). Note that
  this is the name of the group used to sync the output of this node - it will not force
  syncing of animations contained by it.
- ``group_role`` (AnimGroupRole):  [Read-Only] The role this node can assume within the group (ignored if GroupName is not set). Note
  that this is the role of the output of this node, not of animations contained by it.
- ``ignore_for_relevancy_test`` (bool):  [Read-Write] If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``max_active_blends`` (int32):  [Read-Write] Number of max active blending animation in the blend stack. If MaxActiveBlends is zero then blend stack is disabled
- ``max_blend_in_time_to_override_animation`` (float):  [Read-Write] if the most relevant (recently added) animation is within MaxBlendInTimeToOverrideAnimation, the new requested blend will take its spot
  otherwise a new blended will be added to the stack
- ``method`` (AnimSyncMethod):  [Read-Write] How this node will synchronize with other animations. Note that this determines how the output
  of this node is used for synchronization, not of animations contained by it.
- ``notify_recency_time_out`` (float):  [Read-Write] Window of time after firing a notify that any instance of the same notify will be filtered out.
- ``override_position_when_joining_sync_group_as_leader`` (bool):  [Read-Only] When enabled, acting as the leader, and using marker-based sync, this asset player will not sync to the previous leader's sync position when joining a sync group and before becoming the leader but instead force everyone else to match its position.
- ``play_rate`` (FloatInterval):  [Read-Write] Effective range of play rate that can be applied to the animations to account for discrepancies in estimated velocity between the movement model and the animation.
- ``play_rate_multiplier`` (float):  [Read-Write] Experimental: Multiplier applied to the play rate of the selected animation after Motion Matching State has been updated.
- ``player_depth_blend_in_time_multiplier`` (float):  [Read-Write] AnimPlayers blend in timer will be incremented PlayerDepthBlendInTimeMultiplier times faster on a deeper blend
- ``pose_jump_threshold_time`` (FloatInterval):  [Read-Write] Don't jump to poses of the same segment that are within the interval this many seconds away from the continuing pose.
- ``pose_reselect_history`` (float):  [Read-Write] Prevent re-selection of poses that have been selected previously within this much time (in seconds) in the past. This is across all animation segments that have been selected within this time range.
- ``reset_on_becoming_relevant`` (bool):  [Read-Write] Reset the motion matching selection state if it has become relevant to the graph after not being updated on previous frames.
- ``search_throttle_time`` (float):  [Read-Write] Minimum amount of time to wait between searching for a new pose segment. It allows users to define how often the system searches, default for locomotion is searching every update, but you may only want to search once for other situations, like jump.
- ``should_filter_notifies`` (bool):  [Read-Write] Flag that determines if any notifies from originating from an anim player samples should be filtered or not.
- ``should_search`` (bool):  [Read-Write] If set to false, the motion matching node will perform a search only if the continuing pose is invalid. This is useful if you want to stagger searches of different nodes for performance reasons
- ``should_use_cached_channel_data`` (bool):  [Read-Write] If set to true, the search of multiple databases with different schemas will try to share pose features data calculated during query build
  the idea is to be able to share as much as possible the continuing pose features vector across different schemas (and potentially improve performances)
  defaulted to false to preserve behavior backward compatibility
- ``stitch_blend_max_cost`` (float):  [Read-Write] if the cost from searching StitchDatabase is above StitchBlendMaxCost, blend stack will perform a regular blend,
  and not using the returned stitch animation as blend
- ``stitch_blend_time`` (float):  [Read-Write] blend time in seconds used to blend into and out from a stitch animation
- ``stitch_database`` (Object):  [Read-Write] database used to search for an animation stitch to use as blend
- ``store_blended_pose`` (bool):  [Read-Write] if the number of requested blends is higher than MaxActiveBlends, blend stack will blend and accumulate
  into a stored pose all the overflowing animations. if bStoreBlendedPose is false, the memory to store the pose will be saved,
  but once reached the MaxActiveBlends, blendstack will start discarding animations, potentially resulting in animation pops
- ``use_inertial_blend`` (bool):  [Read-Write]

<a id="unreal.AnimNode_MotionMatching.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000,
             stitch_database: Object = None,
             stitch_blend_time: float = 0.000000,
             stitch_blend_max_cost: float = 0.000000,
             notify_recency_time_out: float = 0.000000) -> None
```

<a id="unreal.AnimNode_PoseSearchHistoryCollector_Base"></a>