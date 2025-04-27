## AnimNode_MotionMatchingInteraction Objects

```python
class AnimNode_MotionMatchingInteraction(AnimNode_BlendStack)
```

Anim Node Motion Matching Interaction

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: AnimNode_MotionMatchingInteraction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``activation_delay_time`` (float):  [Read-Write] delay in seconds before activating AnimationAsset playing from AnimationTime
  assets queued with an ActivationDelayTime will be discarded when a new blend gets requested
- ``animation_asset`` (AnimationAsset):  [Read-Write] requested animation to play
- ``animation_time`` (float):  [Read-Write] requested animation time
- ``availabilities`` (Array[PoseSearchInteractionAvailability]):  [Read-Write]
- ``blend_option`` (AlphaBlendOption):  [Read-Write]
- ``blend_parameters`` (Vector):  [Read-Write] requested blend space blend parameters (if AnimationAsset is a blend space)
- ``blend_parameters_delta_threshold`` (float):  [Read-Write] Use this to define a threshold to trigger a new blend when blendspace xy input pins change.
  By default, any delta will trigger a blend.
- ``blend_profile`` (BlendProfile):  [Read-Write]
- ``blend_time`` (float):  [Read-Write] tunable animation transition blend time
- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``blendspace_update_mode`` (BlendStack_BlendspaceUpdateMode):  [Read-Write] How we should update individual blend space parameters. See dropdown options tooltips.
- ``enable_warping`` (bool):  [Read-Write]
- ``evaluation_mode`` (MotionMatchingInteractionEvaluationMode):  [Read-Write]
- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group). Note that
  this is the name of the group used to sync the output of this node - it will not force
  syncing of animations contained by it.
- ``group_role`` (AnimGroupRole):  [Read-Write] The role this node can assume within the group (ignored if GroupName is not set). Note
  that this is the role of the output of this node, not of animations contained by it.
- ``ignore_for_relevancy_test`` (bool):  [Read-Write] If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node
- ``initial_rotation_warp_time`` (float):  [Read-Write] time from the beginning of the interaction to warp to full rotation alignment
- ``initial_translation_warp_time`` (float):  [Read-Write] time from the beginning of the interaction to warp to full translation alignment
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``loop`` (bool):  [Read-Write] requested AnimationAsset looping
- ``max_active_blends`` (int32):  [Read-Write] Number of max active blending animation in the blend stack. If MaxActiveBlends is zero then blend stack is disabled
- ``max_animation_delta_time`` (float):  [Read-Write] if MaxAnimationDeltaTime is positive and the currently playing animation accumulated time differs more than MaxAnimationDeltaTime from AnimationTime
  (animation desynchronized from the requested time) this blend stack will force a blend into the same animation
- ``max_blend_in_time_to_override_animation`` (float):  [Read-Write] if the most relevant (recently added) animation is within MaxBlendInTimeToOverrideAnimation, the new requested blend will take its spot
  otherwise a new blended will be added to the stack
- ``method`` (AnimSyncMethod):  [Read-Write] How this node will synchronize with other animations. Note that this determines how the output
  of this node is used for synchronization, not of animations contained by it.
- ``mirror_data_table`` (MirrorDataTable):  [Read-Write] if set and bMirrored MirrorDataTable will be used for mirroring the aniamtion
- ``mirrored`` (bool):  [Read-Write] requested AnimationAsset mirroring
- ``notify_recency_time_out`` (float):  [Read-Write] Window of time after firing a notify that any instance of the same notify will be filtered out.
- ``player_depth_blend_in_time_multiplier`` (float):  [Read-Write] AnimPlayers blend in timer will be incremented PlayerDepthBlendInTimeMultiplier times faster on a deeper blend
- ``reset_on_becoming_relevant`` (bool):  [Read-Write] Reset the blend stack if it has become relevant to the graph after not being updated on previous frames.
- ``should_filter_notifies`` (bool):  [Read-Write] Flag that determines if any notifies from originating from an anim player samples should be filtered or not.
- ``stitch_blend_max_cost`` (float):  [Read-Write] if the cost from searching StitchDatabase is above StitchBlendMaxCost, blend stack will perform a regular blend,
  and not using the returned stitch animation as blend
- ``stitch_blend_time`` (float):  [Read-Write] blend time in seconds used to blend into and out from a stitch animation
- ``stitch_database`` (Object):  [Read-Write] database used to search for an animation stitch to use as blend
- ``store_blended_pose`` (bool):  [Read-Write] if the number of requested blends is higher than MaxActiveBlends, blend stack will blend and accumulate
  into a stored pose all the overflowing animations. if bStoreBlendedPose is false, the memory to store the pose will be saved,
  but once reached the MaxActiveBlends, blendstack will start discarding animations, potentially resulting in animation pops
- ``use_anim_root_motion_provider`` (bool):  [Read-Write]
- ``use_inertial_blend`` (bool):  [Read-Write] tunable animation transition blend time
- ``validate_result_against_availabilities`` (bool):  [Read-Write]
- ``wanted_play_rate`` (float):  [Read-Write] requested animation play rate

<a id="unreal.AnimNode_MotionMatchingInteraction.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000,
             stitch_database: Object = None,
             stitch_blend_time: float = 0.000000,
             stitch_blend_max_cost: float = 0.000000,
             notify_recency_time_out: float = 0.000000,
             animation_asset: AnimationAsset = None,
             animation_time: float = 0.000000,
             activation_delay_time: float = 0.000000,
             loop: bool = False,
             mirrored: bool = False,
             wanted_play_rate: float = 0.000000,
             blend_time: float = 0.000000,
             max_animation_delta_time: float = 0.000000,
             blend_profile: BlendProfile = None,
             blend_option: AlphaBlendOption = AlphaBlendOption.LINEAR,
             blend_parameters: Vector = [0.000000, 0.000000, 0.000000],
             initial_translation_warp_time: float = 0.000000,
             initial_rotation_warp_time: float = 0.000000) -> None
```

<a id="unreal.AnimNode_MotionMatchingInteraction.initial_translation_warp_time"></a>

#### initial_translation_warp_time

```python
@property
def initial_translation_warp_time() -> float
```

(float):  [Read-Write] time from the beginning of the interaction to warp to full translation alignment

<a id="unreal.AnimNode_MotionMatchingInteraction.initial_translation_warp_time"></a>

#### initial_translation_warp_time

```python
@initial_translation_warp_time.setter
def initial_translation_warp_time(value: float) -> None
```

<a id="unreal.AnimNode_MotionMatchingInteraction.initial_rotation_warp_time"></a>

#### initial_rotation_warp_time

```python
@property
def initial_rotation_warp_time() -> float
```

(float):  [Read-Write] time from the beginning of the interaction to warp to full rotation alignment

<a id="unreal.AnimNode_MotionMatchingInteraction.initial_rotation_warp_time"></a>

#### initial_rotation_warp_time

```python
@initial_rotation_warp_time.setter
def initial_rotation_warp_time(value: float) -> None
```

<a id="unreal.PoseSearchInteractionAvailability"></a>