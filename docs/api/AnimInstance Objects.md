## AnimInstance Objects

```python
class AnimInstance(Object)
```

Anim Instance

**C++ Source:**

- **Module**: Engine
- **File**: AnimInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_all_montage_instances_ended`` (OnAllMontageInstancesEndedMCDelegate):  [Read-Write] Called when all Montage instances have ended.
- ``on_montage_blended_in`` (OnMontageBlendedInEndedMCDelegate):  [Read-Write] Called when a montage finishes blending in
- ``on_montage_blending_out`` (OnMontageBlendingOutStartedMCDelegate):  [Read-Write] Called when a montage starts blending out, whether interrupted or finished
- ``on_montage_ended`` (OnMontageEndedMCDelegate):  [Read-Write] Called when a montage has ended, whether interrupted or finished
- ``on_montage_started`` (OnMontageStartedMCDelegate):  [Read-Write] Called when a montage has started
- ``propagate_notifies_to_linked_instances`` (bool):  [Read-Write] Whether to propagate notifies to any linked anim instances
- ``receive_notifies_from_linked_instances`` (bool):  [Read-Write] Whether to process notifies from any linked anim instances
- ``root_motion_mode`` (RootMotionMode):  [Read-Write] Sets where this blueprint pulls Root Motion from
- ``use_main_instance_montage_evaluation_data`` (bool):  [Read-Write] If true, linked instances will use the main instance's montage data. (i.e. playing a montage on a main instance will play it on the linked layer too.)

<a id="unreal.AnimInstance.on_montage_blending_out"></a>

#### on_montage_blending_out

```python
@property
def on_montage_blending_out() -> OnMontageBlendingOutStartedMCDelegate
```

(OnMontageBlendingOutStartedMCDelegate):  [Read-Write] Called when a montage starts blending out, whether interrupted or finished

<a id="unreal.AnimInstance.on_montage_blending_out"></a>

#### on_montage_blending_out

```python
@on_montage_blending_out.setter
def on_montage_blending_out(
        value: OnMontageBlendingOutStartedMCDelegate) -> None
```

<a id="unreal.AnimInstance.on_montage_blended_in"></a>

#### on_montage_blended_in

```python
@property
def on_montage_blended_in() -> OnMontageBlendedInEndedMCDelegate
```

(OnMontageBlendedInEndedMCDelegate):  [Read-Write] Called when a montage finishes blending in

<a id="unreal.AnimInstance.on_montage_blended_in"></a>

#### on_montage_blended_in

```python
@on_montage_blended_in.setter
def on_montage_blended_in(value: OnMontageBlendedInEndedMCDelegate) -> None
```

<a id="unreal.AnimInstance.on_montage_started"></a>

#### on_montage_started

```python
@property
def on_montage_started() -> OnMontageStartedMCDelegate
```

(OnMontageStartedMCDelegate):  [Read-Write] Called when a montage has started

<a id="unreal.AnimInstance.on_montage_started"></a>

#### on_montage_started

```python
@on_montage_started.setter
def on_montage_started(value: OnMontageStartedMCDelegate) -> None
```

<a id="unreal.AnimInstance.on_montage_ended"></a>

#### on_montage_ended

```python
@property
def on_montage_ended() -> OnMontageEndedMCDelegate
```

(OnMontageEndedMCDelegate):  [Read-Write] Called when a montage has ended, whether interrupted or finished

<a id="unreal.AnimInstance.on_montage_ended"></a>

#### on_montage_ended

```python
@on_montage_ended.setter
def on_montage_ended(value: OnMontageEndedMCDelegate) -> None
```

<a id="unreal.AnimInstance.on_all_montage_instances_ended"></a>

#### on_all_montage_instances_ended

```python
@property
def on_all_montage_instances_ended() -> OnAllMontageInstancesEndedMCDelegate
```

(OnAllMontageInstancesEndedMCDelegate):  [Read-Write] Called when all Montage instances have ended.

<a id="unreal.AnimInstance.on_all_montage_instances_ended"></a>

#### on_all_montage_instances_ended

```python
@on_all_montage_instances_ended.setter
def on_all_montage_instances_ended(
        value: OnAllMontageInstancesEndedMCDelegate) -> None
```

<a id="unreal.AnimInstance.was_anim_notify_state_active_in_any_state"></a>

#### was_anim_notify_state_active_in_any_state

```python
def was_anim_notify_state_active_in_any_state(
        anim_notify_state_type: Class) -> bool
```

x.was_anim_notify_state_active_in_any_state(anim_notify_state_type) -> bool
Get whether a particular notify state was active in any state machine last tick.

Args:
    anim_notify_state_type (type(Class)): 

Returns:
    bool:

<a id="unreal.AnimInstance.unlock_ai_resources"></a>

#### unlock_ai_resources

```python
def unlock_ai_resources(unlock_movement: bool, unlock_ai_logic: bool) -> None
```

x.unlock_ai_resources(unlock_movement, unlock_ai_logic) -> None
unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources.
    DEPRECATED. Use UnlockAIResourcesWithAnimation instead
deprecated: Use UnlockAIResourcesWithAnimation instead

Args:
    unlock_movement (bool): 
    unlock_ai_logic (bool):

<a id="unreal.AnimInstance.unlink_anim_class_layers"></a>

#### unlink_anim_class_layers

```python
def unlink_anim_class_layers(class_: Class) -> None
```

x.unlink_anim_class_layers(class_) -> None
Runs through all layer nodes, attempting to find layer nodes that are currently running the specified class, then resets each to its default value.
State sharing rules are as with SetLayerOverlay.
If InClass is null, does nothing.

Args:
    class_ (type(Class)):

<a id="unreal.AnimInstance.clear_layer_overlay"></a>

#### clear_layer_overlay

```python
def clear_layer_overlay(class_: Class) -> None
```

deprecated: 'clear_layer_overlay' was renamed to 'unlink_anim_class_layers'.

<a id="unreal.AnimInstance.try_get_pawn_owner"></a>

#### try_get_pawn_owner

```python
def try_get_pawn_owner() -> Pawn
```

x.try_get_pawn_owner() -> Pawn
kismet event functions

Returns:
    Pawn:

<a id="unreal.AnimInstance.stop_slot_animation"></a>

#### stop_slot_animation

```python
def stop_slot_animation(blend_out_time: float = 0.250000,
                        slot_node_name: Name = "None") -> None
```

x.stop_slot_animation(blend_out_time=0.250000, slot_node_name="None") -> None
Stops currently playing slot animation slot or all

Args:
    blend_out_time (float): 
    slot_node_name (Name):

<a id="unreal.AnimInstance.snapshot_pose"></a>

#### snapshot_pose

```python
def snapshot_pose(snapshot: PoseSnapshot) -> PoseSnapshot
```

x.snapshot_pose(snapshot) -> PoseSnapshot
Takes a snapshot of the current skeletal mesh component pose and saves it to the specified snapshot.
The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
and then used it at LOD0 any bones not in LOD1 will use the reference pose

Args:
    snapshot (PoseSnapshot): 

Returns:
    PoseSnapshot: 

    snapshot (PoseSnapshot):

<a id="unreal.AnimInstance.set_use_main_instance_montage_evaluation_data"></a>

#### set_use_main_instance_montage_evaluation_data

```python
def set_use_main_instance_montage_evaluation_data(set: bool) -> None
```

x.set_use_main_instance_montage_evaluation_data(set) -> None
Set Use Main Instance Montage Evaluation Data

Args:
    set (bool):

<a id="unreal.AnimInstance.set_root_motion_mode"></a>

#### set_root_motion_mode

```python
def set_root_motion_mode(value: RootMotionMode) -> None
```

x.set_root_motion_mode(value) -> None
Set RootMotionMode

Args:
    value (RootMotionMode):

<a id="unreal.AnimInstance.set_receive_notifies_from_linked_instances"></a>

#### set_receive_notifies_from_linked_instances

```python
def set_receive_notifies_from_linked_instances(set: bool) -> None
```

x.set_receive_notifies_from_linked_instances(set) -> None
Set whether to process notifies from any linked anim instances

Args:
    set (bool):

<a id="unreal.AnimInstance.set_propagate_notifies_to_linked_instances"></a>

#### set_propagate_notifies_to_linked_instances

```python
def set_propagate_notifies_to_linked_instances(set: bool) -> None
```

x.set_propagate_notifies_to_linked_instances(set) -> None
Set whether to propagate notifies to any linked anim instances

Args:
    set (bool):

<a id="unreal.AnimInstance.set_morph_target"></a>

#### set_morph_target

```python
def set_morph_target(morph_target_name: Name, value: float) -> None
```

x.set_morph_target(morph_target_name, value) -> None
Sets a morph target to a certain weight.

Args:
    morph_target_name (Name): 
    value (float):

<a id="unreal.AnimInstance.save_pose_snapshot"></a>

#### save_pose_snapshot

```python
def save_pose_snapshot(snapshot_name: Name) -> None
```

x.save_pose_snapshot(snapshot_name) -> None
Takes a snapshot of the current skeletal mesh component pose & saves it internally.
This snapshot can then be retrieved by name in the animation blueprint for blending.
The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1 and then used it at LOD0 any bones not in LOD1 will use the reference pose

Args:
    snapshot_name (Name):

<a id="unreal.AnimInstance.reset_dynamics"></a>

#### reset_dynamics

```python
def reset_dynamics(teleport_type: TeleportType) -> None
```

x.reset_dynamics(teleport_type) -> None
Reset any dynamics running simulation-style updates (e.g. on teleport, time skip etc.)

Args:
    teleport_type (TeleportType):

<a id="unreal.AnimInstance.request_transition_event"></a>

#### request_transition_event

```python
def request_transition_event(
        event_name: Name, request_timeout: float,
        queue_mode: TransitionRequestQueueMode,
        overwrite_mode: TransitionRequestOverwriteMode) -> bool
```

x.request_transition_event(event_name, request_timeout, queue_mode, overwrite_mode) -> bool
Attempts to queue a transition request, returns true if the request was successful

Args:
    event_name (Name): 
    request_timeout (double): 
    queue_mode (TransitionRequestQueueMode): 
    overwrite_mode (TransitionRequestOverwriteMode): 

Returns:
    bool:

<a id="unreal.AnimInstance.request_slot_group_inertialization"></a>

#### request_slot_group_inertialization

```python
def request_slot_group_inertialization(
        slot_group_name: Name,
        duration: float,
        blend_profile: BlendProfile = None) -> None
```

x.request_slot_group_inertialization(slot_group_name, duration, blend_profile=None) -> None
Requests an inertial blend during the next anim graph update. Requires your anim graph to have a slot node belonging to the specified group name

Args:
    slot_group_name (Name): 
    duration (float): 
    blend_profile (BlendProfile):

<a id="unreal.AnimInstance.remove_pose_snapshot"></a>

#### remove_pose_snapshot

```python
def remove_pose_snapshot(snapshot_name: Name) -> None
```

x.remove_pose_snapshot(snapshot_name) -> None
Remove a previously saved pose snapshot from the internal snapshot cache

Args:
    snapshot_name (Name):

<a id="unreal.AnimInstance.play_slot_animation_as_dynamic_montage_with_blend_settings"></a>

#### play_slot_animation_as_dynamic_montage_with_blend_settings

```python
def play_slot_animation_as_dynamic_montage_with_blend_settings(
        asset: AnimSequenceBase,
        slot_node_name: Name,
        blend_in_settings: MontageBlendSettings,
        blend_out_settings: MontageBlendSettings,
        play_rate: float = 1.000000,
        loop_count: int = 1,
        blend_out_trigger_time: float = -1.000000,
        time_to_start_montage_at: float = 0.000000) -> AnimMontage
```

x.play_slot_animation_as_dynamic_montage_with_blend_settings(asset, slot_node_name, blend_in_settings, blend_out_settings, play_rate=1.000000, loop_count=1, blend_out_trigger_time=-1.000000, time_to_start_montage_at=0.000000) -> AnimMontage
Play normal animation asset on the slot node by creating a dynamic UAnimMontage with blend in settings. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

Args:
    asset (AnimSequenceBase): 
    slot_node_name (Name): 
    blend_in_settings (MontageBlendSettings): 
    blend_out_settings (MontageBlendSettings): 
    play_rate (float): 
    loop_count (int32): 
    blend_out_trigger_time (float): 
    time_to_start_montage_at (float): 

Returns:
    AnimMontage:

<a id="unreal.AnimInstance.play_slot_animation_as_dynamic_montage_with_blend_args"></a>

#### play_slot_animation_as_dynamic_montage_with_blend_args

```python
def play_slot_animation_as_dynamic_montage_with_blend_args(
        asset: AnimSequenceBase,
        slot_node_name: Name,
        blend_in: AlphaBlendArgs,
        blend_out: AlphaBlendArgs,
        play_rate: float = 1.000000,
        loop_count: int = 1,
        blend_out_trigger_time: float = -1.000000,
        time_to_start_montage_at: float = 0.000000) -> AnimMontage
```

x.play_slot_animation_as_dynamic_montage_with_blend_args(asset, slot_node_name, blend_in, blend_out, play_rate=1.000000, loop_count=1, blend_out_trigger_time=-1.000000, time_to_start_montage_at=0.000000) -> AnimMontage
Play normal animation asset on the slot node by creating a dynamic UAnimMontage with blend in arguments. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

Args:
    asset (AnimSequenceBase): 
    slot_node_name (Name): 
    blend_in (AlphaBlendArgs): 
    blend_out (AlphaBlendArgs): 
    play_rate (float): 
    loop_count (int32): 
    blend_out_trigger_time (float): 
    time_to_start_montage_at (float): 

Returns:
    AnimMontage:

<a id="unreal.AnimInstance.play_slot_animation_as_dynamic_montage"></a>

#### play_slot_animation_as_dynamic_montage

```python
def play_slot_animation_as_dynamic_montage(
        asset: AnimSequenceBase,
        slot_node_name: Name,
        blend_in_time: float = 0.250000,
        blend_out_time: float = 0.250000,
        play_rate: float = 1.000000,
        loop_count: int = 1,
        blend_out_trigger_time: float = -1.000000,
        time_to_start_montage_at: float = 0.000000) -> AnimMontage
```

x.play_slot_animation_as_dynamic_montage(asset, slot_node_name, blend_in_time=0.250000, blend_out_time=0.250000, play_rate=1.000000, loop_count=1, blend_out_trigger_time=-1.000000, time_to_start_montage_at=0.000000) -> AnimMontage
Play normal animation asset on the slot node by creating a dynamic UAnimMontage. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

Args:
    asset (AnimSequenceBase): 
    slot_node_name (Name): 
    blend_in_time (float): 
    blend_out_time (float): 
    play_rate (float): 
    loop_count (int32): 
    blend_out_trigger_time (float): 
    time_to_start_montage_at (float): 

Returns:
    AnimMontage:

<a id="unreal.AnimInstance.montage_sync_stop_following"></a>

#### montage_sync_stop_following

```python
def montage_sync_stop_following(montage_follower: AnimMontage) -> None
```

x.montage_sync_stop_following(montage_follower) -> None
Stop following the montage's leader in this anim instance

Args:
    montage_follower (AnimMontage): : The montage we want to stop synchronizing

<a id="unreal.AnimInstance.montage_sync_follow"></a>

#### montage_sync_follow

```python
def montage_sync_follow(montage_follower: AnimMontage,
                        other_anim_instance: AnimInstance,
                        montage_leader: AnimMontage) -> None
```

x.montage_sync_follow(montage_follower, other_anim_instance, montage_leader) -> None
Synchronize a montage to another anim instance's montage. Both montages must be playing already

Args:
    montage_follower (AnimMontage): : The montage that will follow the leader in OtherAnimInstance
    other_anim_instance (AnimInstance): : The other anim instance we want to synchronize to. Can be set to self
    montage_leader (AnimMontage): : The montage we want to follow in the other anim instance

<a id="unreal.AnimInstance.montage_stop_with_blend_settings"></a>

#### montage_stop_with_blend_settings

```python
def montage_stop_with_blend_settings(blend_out_settings: MontageBlendSettings,
                                     montage: AnimMontage = None) -> None
```

x.montage_stop_with_blend_settings(blend_out_settings, montage=None) -> None
Same as Montage_Stop, but all blend settings are provided instead of using the ones on the montage asset

Args:
    blend_out_settings (MontageBlendSettings): 
    montage (AnimMontage):

<a id="unreal.AnimInstance.montage_stop_with_blend_out"></a>

#### montage_stop_with_blend_out

```python
def montage_stop_with_blend_out(blend_out: AlphaBlendArgs,
                                montage: AnimMontage = None) -> None
```

x.montage_stop_with_blend_out(blend_out, montage=None) -> None
Same as Montage_Stop. Uses values from the AlphaBlendArgs. Other settings come from the montage asset

Args:
    blend_out (AlphaBlendArgs): 
    montage (AnimMontage):

<a id="unreal.AnimInstance.montage_stop_group_by_name"></a>

#### montage_stop_group_by_name

```python
def montage_stop_group_by_name(blend_out_time: float,
                               group_name: Name) -> None
```

x.montage_stop_group_by_name(blend_out_time, group_name) -> None
Stops all active montages belonging to a group.

Args:
    blend_out_time (float): 
    group_name (Name):

<a id="unreal.AnimInstance.montage_stop"></a>

#### montage_stop

```python
def montage_stop(blend_out_time: float, montage: AnimMontage = None) -> None
```

x.montage_stop(blend_out_time, montage=None) -> None
Stopped montages will blend out using their montage asset's BlendOut, with InBlendOutTime as the BlendTime

Args:
    blend_out_time (float): 
    montage (AnimMontage):

<a id="unreal.AnimInstance.montage_set_position"></a>

#### montage_set_position

```python
def montage_set_position(montage: AnimMontage, new_position: float) -> None
```

x.montage_set_position(montage, new_position) -> None
Set position.

Args:
    montage (AnimMontage): 
    new_position (float):

<a id="unreal.AnimInstance.montage_set_play_rate"></a>

#### montage_set_play_rate

```python
def montage_set_play_rate(montage: AnimMontage,
                          new_play_rate: float = 1.000000) -> None
```

x.montage_set_play_rate(montage, new_play_rate=1.000000) -> None
Change AnimMontage play rate. NewPlayRate = 1.0 is the default playback rate.

Args:
    montage (AnimMontage): 
    new_play_rate (float):

<a id="unreal.AnimInstance.montage_set_next_section"></a>

#### montage_set_next_section

```python
def montage_set_next_section(section_name_to_change: Name,
                             next_section: Name,
                             montage: AnimMontage = None) -> None
```

x.montage_set_next_section(section_name_to_change, next_section, montage=None) -> None
Relink new next section AFTER SectionNameToChange in run-time
    You can link section order the way you like in editor, but in run-time if you'd like to change it dynamically,
    use this function to relink the next section
    For example, you can have Start->Loop->Loop->Loop.... but when you want it to end, you can relink
    next section of Loop to be End to finish the montage, in which case, it stops looping by Loop->End.

Args:
    section_name_to_change (Name): : This should be the name of the Montage Section after which you want to insert a new next section
    next_section (Name): : new next section
    montage (AnimMontage):

<a id="unreal.AnimInstance.montage_resume"></a>

#### montage_resume

```python
def montage_resume(montage: AnimMontage) -> None
```

x.montage_resume(montage) -> None
Resumes a paused animation montage. If reference is NULL, it will resume ALL active montages.

Args:
    montage (AnimMontage):

<a id="unreal.AnimInstance.montage_play_with_blend_settings"></a>

#### montage_play_with_blend_settings

```python
def montage_play_with_blend_settings(
        montage_to_play: AnimMontage,
        blend_in_settings: MontageBlendSettings,
        play_rate: float = 1.000000,
        return_value_type: MontagePlayReturnType = MontagePlayReturnType.
    MONTAGE_LENGTH,
        time_to_start_montage_at: float = 0.000000,
        stop_all_montages: bool = True) -> float
```

x.montage_play_with_blend_settings(montage_to_play, blend_in_settings, play_rate=1.000000, return_value_type=MontagePlayReturnType.MONTAGE_LENGTH, time_to_start_montage_at=0.000000, stop_all_montages=True) -> float
Plays an animation montage. Same as Montage_Play, but you can overwrite all of the montage's default blend in settings.

Args:
    montage_to_play (AnimMontage): 
    blend_in_settings (MontageBlendSettings): 
    play_rate (float): 
    return_value_type (MontagePlayReturnType): 
    time_to_start_montage_at (float): 
    stop_all_montages (bool): 

Returns:
    float:

<a id="unreal.AnimInstance.montage_play_with_blend_in"></a>

#### montage_play_with_blend_in

```python
def montage_play_with_blend_in(
        montage_to_play: AnimMontage,
        blend_in: AlphaBlendArgs,
        play_rate: float = 1.000000,
        return_value_type: MontagePlayReturnType = MontagePlayReturnType.
    MONTAGE_LENGTH,
        time_to_start_montage_at: float = 0.000000,
        stop_all_montages: bool = True) -> float
```

x.montage_play_with_blend_in(montage_to_play, blend_in, play_rate=1.000000, return_value_type=MontagePlayReturnType.MONTAGE_LENGTH, time_to_start_montage_at=0.000000, stop_all_montages=True) -> float
Plays an animation montage. Same as Montage_Play, but you can specify an AlphaBlend for Blend In settings.

Args:
    montage_to_play (AnimMontage): 
    blend_in (AlphaBlendArgs): 
    play_rate (float): 
    return_value_type (MontagePlayReturnType): 
    time_to_start_montage_at (float): 
    stop_all_montages (bool): 

Returns:
    float:

<a id="unreal.AnimInstance.montage_play"></a>

#### montage_play

```python
def montage_play(
        montage_to_play: AnimMontage,
        play_rate: float = 1.000000,
        return_value_type: MontagePlayReturnType = MontagePlayReturnType.
    MONTAGE_LENGTH,
        time_to_start_montage_at: float = 0.000000,
        stop_all_montages: bool = True) -> float
```

x.montage_play(montage_to_play, play_rate=1.000000, return_value_type=MontagePlayReturnType.MONTAGE_LENGTH, time_to_start_montage_at=0.000000, stop_all_montages=True) -> float
Plays an animation montage. Returns the length of the animation montage in seconds. Returns 0.f if failed to play.

Args:
    montage_to_play (AnimMontage): 
    play_rate (float): 
    return_value_type (MontagePlayReturnType): 
    time_to_start_montage_at (float): 
    stop_all_montages (bool): 

Returns:
    float:

<a id="unreal.AnimInstance.montage_pause"></a>

#### montage_pause

```python
def montage_pause(montage: AnimMontage = None) -> None
```

x.montage_pause(montage=None) -> None
Pauses the animation montage. If reference is NULL, it will pause ALL active montages.

Args:
    montage (AnimMontage):

<a id="unreal.AnimInstance.montage_jump_to_sections_end"></a>

#### montage_jump_to_sections_end

```python
def montage_jump_to_sections_end(section_name: Name,
                                 montage: AnimMontage = None) -> None
```

x.montage_jump_to_sections_end(section_name, montage=None) -> None
Makes a montage jump to the end of a named section. If Montage reference is NULL, it will do that to all active montages.

Args:
    section_name (Name): 
    montage (AnimMontage):

<a id="unreal.AnimInstance.montage_jump_to_section"></a>

#### montage_jump_to_section

```python
def montage_jump_to_section(section_name: Name,
                            montage: AnimMontage = None) -> None
```

x.montage_jump_to_section(section_name, montage=None) -> None
Makes a montage jump to a named section. If Montage reference is NULL, it will do that to all active montages.

Args:
    section_name (Name): 
    montage (AnimMontage):

<a id="unreal.AnimInstance.montage_is_playing"></a>

#### montage_is_playing

```python
def montage_is_playing(montage: AnimMontage) -> bool
```

x.montage_is_playing(montage) -> bool
Returns true if the animation montage is currently active and playing.
      If reference is NULL, it will return true is ANY montage is currently active and playing.

Args:
    montage (AnimMontage): 

Returns:
    bool:

<a id="unreal.AnimInstance.montage_is_active"></a>

#### montage_is_active

```python
def montage_is_active(montage: AnimMontage) -> bool
```

x.montage_is_active(montage) -> bool
Returns true if the animation montage is active. If the Montage reference is NULL, it will return true if any Montage is active.

Args:
    montage (AnimMontage): 

Returns:
    bool:

<a id="unreal.AnimInstance.montage_get_position"></a>

#### montage_get_position

```python
def montage_get_position(montage: AnimMontage) -> float
```

x.montage_get_position(montage) -> float
Get Current Montage Position

Args:
    montage (AnimMontage): 

Returns:
    float:

<a id="unreal.AnimInstance.montage_get_play_rate"></a>

#### montage_get_play_rate

```python
def montage_get_play_rate(montage: AnimMontage) -> float
```

x.montage_get_play_rate(montage) -> float
Get PlayRate for Montage. This does not account for RateScale, so it may not reflect the actual play rate seen in game (see Montage_GetEffectivePlayRate).
      If Montage reference is NULL, PlayRate for any Active Montage will be returned.
      If Montage is not playing, 0 is returned.

Args:
    montage (AnimMontage): 

Returns:
    float:

<a id="unreal.AnimInstance.montage_get_is_stopped"></a>

#### montage_get_is_stopped

```python
def montage_get_is_stopped(montage: AnimMontage) -> bool
```

x.montage_get_is_stopped(montage) -> bool
return true if Montage is not currently active. (not valid or blending out)

Args:
    montage (AnimMontage): 

Returns:
    bool:

<a id="unreal.AnimInstance.montage_get_effective_play_rate"></a>

#### montage_get_effective_play_rate

```python
def montage_get_effective_play_rate(montage: AnimMontage) -> float
```

x.montage_get_effective_play_rate(montage) -> float
Get scaled PlayRate for Montage. This accounts for RateScale, so it will reflect the actual play rate seen in game.
      If Montage reference is NULL, scaled PlayRate for any Active Montage will be returned.
      If Montage is not playing, 0 is returned.

Args:
    montage (AnimMontage): 

Returns:
    float:

<a id="unreal.AnimInstance.montage_get_current_section"></a>

#### montage_get_current_section

```python
def montage_get_current_section(montage: AnimMontage = None) -> Name
```

x.montage_get_current_section(montage=None) -> Name
Returns the name of the current animation montage section.

Args:
    montage (AnimMontage): 

Returns:
    Name:

<a id="unreal.AnimInstance.montage_get_blend_time"></a>

#### montage_get_blend_time

```python
def montage_get_blend_time(montage: AnimMontage) -> float
```

x.montage_get_blend_time(montage) -> float
Get the current blend time of the Montage.
      If Montage reference is NULL, it will return the current blend time on the first active Montage found.

Args:
    montage (AnimMontage): 

Returns:
    float:

<a id="unreal.AnimInstance.lock_ai_resources"></a>

#### lock_ai_resources

```python
def lock_ai_resources(lock_movement: bool, lock_ai_logic: bool) -> None
```

x.lock_ai_resources(lock_movement, lock_ai_logic) -> None
locks indicated AI resources of animated pawn
    DEPRECATED. Use LockAIResourcesWithAnimation instead
deprecated: Use LockAIResourcesWithAnimation instead

Args:
    lock_movement (bool): 
    lock_ai_logic (bool):

<a id="unreal.AnimInstance.link_anim_graph_by_tag"></a>

#### link_anim_graph_by_tag

```python
def link_anim_graph_by_tag(tag: Name, class_: Class) -> None
```

x.link_anim_graph_by_tag(tag, class_) -> None
Runs through all nodes, attempting to find a linked instance by name/tag, then sets the class of each node if the tag matches

Args:
    tag (Name): 
    class_ (type(Class)):

<a id="unreal.AnimInstance.set_sub_instance_class_by_tag"></a>

#### set_sub_instance_class_by_tag

```python
def set_sub_instance_class_by_tag(tag: Name, class_: Class) -> None
```

deprecated: 'set_sub_instance_class_by_tag' was renamed to 'link_anim_graph_by_tag'.

<a id="unreal.AnimInstance.link_anim_class_layers"></a>

#### link_anim_class_layers

```python
def link_anim_class_layers(class_: Class) -> None
```

x.link_anim_class_layers(class_) -> None
Runs through all layer nodes, attempting to find layer nodes that are implemented by the specified class, then sets up a linked instance of the class for each.
Allocates one linked instance to run each of the groups specified in the class, so state is shared. If a layer is not grouped (ie. NAME_None), then state is not shared
and a separate linked instance is allocated for each layer node.
If InClass is null, then all layers are reset to their defaults.

Args:
    class_ (type(Class)):

<a id="unreal.AnimInstance.set_layer_overlay"></a>

#### set_layer_overlay

```python
def set_layer_overlay(class_: Class) -> None
```

deprecated: 'set_layer_overlay' was renamed to 'link_anim_class_layers'.

<a id="unreal.AnimInstance.is_using_main_instance_montage_evaluation_data"></a>

#### is_using_main_instance_montage_evaluation_data

```python
def is_using_main_instance_montage_evaluation_data() -> bool
```

x.is_using_main_instance_montage_evaluation_data() -> bool
Is Using Main Instance Montage Evaluation Data

Returns:
    bool:

<a id="unreal.AnimInstance.is_sync_group_between_markers"></a>

#### is_sync_group_between_markers

```python
def is_sync_group_between_markers(sync_group_name: Name,
                                  previous_marker: Name,
                                  next_marker: Name,
                                  respect_marker_order: bool = True) -> bool
```

x.is_sync_group_between_markers(sync_group_name, previous_marker, next_marker, respect_marker_order=True) -> bool
Is Sync Group Between Markers

Args:
    sync_group_name (Name): 
    previous_marker (Name): 
    next_marker (Name): 
    respect_marker_order (bool): 

Returns:
    bool:

<a id="unreal.AnimInstance.is_slot_active"></a>

#### is_slot_active

```python
def is_slot_active(slot_node_name: Name) -> bool
```

x.is_slot_active(slot_node_name) -> bool
Return true if this instance has an active montage in the given slot. A UAnimMontage that is playing in the slot and blending out is not determined to be "active".

Args:
    slot_node_name (Name): 

Returns:
    bool:

<a id="unreal.AnimInstance.is_playing_slot_animation"></a>

#### is_playing_slot_animation

```python
def is_playing_slot_animation(asset: AnimSequenceBase,
                              slot_node_name: Name) -> bool
```

x.is_playing_slot_animation(asset, slot_node_name) -> bool
Return true if it's playing the slot animation

Args:
    asset (AnimSequenceBase): 
    slot_node_name (Name): 

Returns:
    bool:

<a id="unreal.AnimInstance.is_any_montage_playing"></a>

#### is_any_montage_playing

```python
def is_any_montage_playing() -> bool
```

x.is_any_montage_playing() -> bool
Returns true if any montage is playing currently. Doesn't mean it's active though, it could be blending out.

Returns:
    bool:

<a id="unreal.AnimInstance.has_marker_been_hit_this_frame"></a>

#### has_marker_been_hit_this_frame

```python
def has_marker_been_hit_this_frame(sync_group: Name,
                                   marker_name: Name) -> bool
```

x.has_marker_been_hit_this_frame(sync_group, marker_name) -> bool
Has Marker Been Hit This Frame

Args:
    sync_group (Name): 
    marker_name (Name): 

Returns:
    bool:

<a id="unreal.AnimInstance.get_time_to_closest_marker"></a>

#### get_time_to_closest_marker

```python
def get_time_to_closest_marker(sync_group: Name,
                               marker_name: Name) -> Optional[float]
```

x.get_time_to_closest_marker(sync_group, marker_name) -> float or None
--- AI communication end ---

Args:
    sync_group (Name): 
    marker_name (Name): 

Returns:
    float or None: 

    out_marker_time (float):

<a id="unreal.AnimInstance.get_sync_group_position"></a>

#### get_sync_group_position

```python
def get_sync_group_position(sync_group_name: Name) -> MarkerSyncAnimPosition
```

x.get_sync_group_position(sync_group_name) -> MarkerSyncAnimPosition
Get Sync Group Position

Args:
    sync_group_name (Name): 

Returns:
    MarkerSyncAnimPosition:

<a id="unreal.AnimInstance.get_receive_notifies_from_linked_instances"></a>

#### get_receive_notifies_from_linked_instances

```python
def get_receive_notifies_from_linked_instances() -> bool
```

x.get_receive_notifies_from_linked_instances() -> bool
Get whether to process notifies from any linked anim instances

Returns:
    bool:

<a id="unreal.AnimInstance.get_propagate_notifies_to_linked_instances"></a>

#### get_propagate_notifies_to_linked_instances

```python
def get_propagate_notifies_to_linked_instances() -> bool
```

x.get_propagate_notifies_to_linked_instances() -> bool
Get whether to propagate notifies to any linked anim instances

Returns:
    bool:

<a id="unreal.AnimInstance.get_owning_component"></a>

#### get_owning_component

```python
def get_owning_component() -> SkeletalMeshComponent
```

x.get_owning_component() -> SkeletalMeshComponent
Returns the skeletal mesh component that has created this AnimInstance

Returns:
    SkeletalMeshComponent:

<a id="unreal.AnimInstance.get_owning_actor"></a>

#### get_owning_actor

```python
def get_owning_actor() -> Actor
```

x.get_owning_actor() -> Actor
Returns the owning actor of this AnimInstance

Returns:
    Actor:

<a id="unreal.AnimInstance.get_linked_anim_layer_instances_by_group"></a>

#### get_linked_anim_layer_instances_by_group

```python
def get_linked_anim_layer_instances_by_group(
        group: Name) -> Array[AnimInstance]
```

x.get_linked_anim_layer_instances_by_group(group) -> Array[AnimInstance]
Runs through all nodes, attempting to find all distinct layer linked instances in the group

Args:
    group (Name): 

Returns:
    Array[AnimInstance]: 

    out_linked_instances (Array[AnimInstance]):

<a id="unreal.AnimInstance.get_linked_anim_layer_instance_by_group_and_class"></a>

#### get_linked_anim_layer_instance_by_group_and_class

```python
def get_linked_anim_layer_instance_by_group_and_class(
        group: Name, class_: Class) -> AnimInstance
```

x.get_linked_anim_layer_instance_by_group_and_class(group, class_) -> AnimInstance
Gets layer linked instance that matches group and class

Args:
    group (Name): 
    class_ (type(Class)): 

Returns:
    AnimInstance:

<a id="unreal.AnimInstance.get_linked_anim_layer_instance_by_group"></a>

#### get_linked_anim_layer_instance_by_group

```python
def get_linked_anim_layer_instance_by_group(group: Name) -> AnimInstance
```

x.get_linked_anim_layer_instance_by_group(group) -> AnimInstance
Gets the layer linked instance corresponding to the specified group

Args:
    group (Name): 

Returns:
    AnimInstance:

<a id="unreal.AnimInstance.get_layer_sub_instance_by_group"></a>

#### get_layer_sub_instance_by_group

```python
def get_layer_sub_instance_by_group(group: Name) -> AnimInstance
```

deprecated: 'get_layer_sub_instance_by_group' was renamed to 'get_linked_anim_layer_instance_by_group'.

<a id="unreal.AnimInstance.get_linked_anim_layer_instance_by_class"></a>

#### get_linked_anim_layer_instance_by_class

```python
def get_linked_anim_layer_instance_by_class(class_: Class,
                                            check_for_child_class: bool = False
                                            ) -> AnimInstance
```

x.get_linked_anim_layer_instance_by_class(class_, check_for_child_class=False) -> AnimInstance
Gets the first layer linked instance corresponding to the specified class, optionally if bCheckForChildClass is true, it will check IsChildOf on InClass.

Args:
    class_ (type(Class)): 
    check_for_child_class (bool): 

Returns:
    AnimInstance:

<a id="unreal.AnimInstance.get_layer_sub_instance_by_class"></a>

#### get_layer_sub_instance_by_class

```python
def get_layer_sub_instance_by_class(class_: Class,
                                    check_for_child_class: bool = False
                                    ) -> AnimInstance
```

deprecated: 'get_layer_sub_instance_by_class' was renamed to 'get_linked_anim_layer_instance_by_class'.

<a id="unreal.AnimInstance.get_linked_anim_graph_instances_by_tag"></a>

#### get_linked_anim_graph_instances_by_tag

```python
def get_linked_anim_graph_instances_by_tag(tag: Name) -> Array[AnimInstance]
```

x.get_linked_anim_graph_instances_by_tag(tag) -> Array[AnimInstance]
Get Linked Anim Graph Instances by Tag
deprecated: Tags are unique so this function is no longer supported. Please use GetLinkedAnimGraphInstanceByTag instead

Args:
    tag (Name): 

Returns:
    Array[AnimInstance]: 

    out_linked_instances (Array[AnimInstance]):

<a id="unreal.AnimInstance.get_sub_instances_by_tag"></a>

#### get_sub_instances_by_tag

```python
def get_sub_instances_by_tag(tag: Name) -> Array[AnimInstance]
```

deprecated: 'get_sub_instances_by_tag' was renamed to 'get_linked_anim_graph_instances_by_tag'.

<a id="unreal.AnimInstance.get_linked_anim_graph_instance_by_tag"></a>

#### get_linked_anim_graph_instance_by_tag

```python
def get_linked_anim_graph_instance_by_tag(tag: Name) -> AnimInstance
```

x.get_linked_anim_graph_instance_by_tag(tag) -> AnimInstance
Runs through all nodes, attempting to find the first linked instance by name/tag

Args:
    tag (Name): 

Returns:
    AnimInstance:

<a id="unreal.AnimInstance.get_sub_instance_by_tag"></a>

#### get_sub_instance_by_tag

```python
def get_sub_instance_by_tag(tag: Name) -> AnimInstance
```

deprecated: 'get_sub_instance_by_tag' was renamed to 'get_linked_anim_graph_instance_by_tag'.

<a id="unreal.AnimInstance.get_delta_seconds"></a>

#### get_delta_seconds

```python
def get_delta_seconds() -> float
```

x.get_delta_seconds() -> float
Get the current delta time

Returns:
    float:

<a id="unreal.AnimInstance.get_curve_value_with_default"></a>

#### get_curve_value_with_default

```python
def get_curve_value_with_default(curve_name: Name,
                                 default_value: float) -> Optional[float]
```

x.get_curve_value_with_default(curve_name, default_value) -> float or None
Returns whether a named curve was found, its value, and a default value when it's not found.

Args:
    curve_name (Name): The name of the curve.
    default_value (float): Value to use when the curve is not found.

Returns:
    float or None: 

    out_value (float): The curve's value.

<a id="unreal.AnimInstance.get_curve_value"></a>

#### get_curve_value

```python
def get_curve_value(curve_name: Name) -> float
```

x.get_curve_value(curve_name) -> float
Returns the value of a named curve.

Args:
    curve_name (Name): 

Returns:
    float:

<a id="unreal.AnimInstance.get_current_active_montage"></a>

#### get_current_active_montage

```python
def get_current_active_montage() -> AnimMontage
```

x.get_current_active_montage() -> AnimMontage
Get a current Active Montage in this AnimInstance.
              Note that there might be multiple Active at the same time. This will only return the first active one it finds. *

Returns:
    AnimMontage:

<a id="unreal.AnimInstance.get_blend_profile_by_name"></a>

#### get_blend_profile_by_name

```python
def get_blend_profile_by_name(blend_profile_name: Name) -> BlendProfile
```

x.get_blend_profile_by_name(blend_profile_name) -> BlendProfile
Returns a blend profile by name from our current skeleton. Null if not found.

Args:
    blend_profile_name (Name): 

Returns:
    BlendProfile:

<a id="unreal.AnimInstance.get_all_curve_names"></a>

#### get_all_curve_names

```python
def get_all_curve_names() -> Array[Name]
```

x.get_all_curve_names() -> Array[Name]
This returns all curve names. This is the same as calling GetActiveCurveNames with CurveType == AttributeCurve

Returns:
    Array[Name]: 

    out_names (Array[Name]):

<a id="unreal.AnimInstance.get_active_curve_names"></a>

#### get_active_curve_names

```python
def get_active_curve_names(curve_type: AnimCurveType) -> Array[Name]
```

x.get_active_curve_names(curve_type) -> Array[Name]
This returns last up-to-date list of active curve names

Args:
    curve_type (AnimCurveType): 

Returns:
    Array[Name]: 

    out_names (Array[Name]):

<a id="unreal.AnimInstance.dynamic_montage_is_playing_from"></a>

#### dynamic_montage_is_playing_from

```python
def dynamic_montage_is_playing_from(animation: AnimSequenceBase) -> bool
```

x.dynamic_montage_is_playing_from(animation) -> bool
Returns true if there is an animation montage is currently active and playing that was created from the provided animation.

Args:
    animation (AnimSequenceBase): 

Returns:
    bool:

<a id="unreal.AnimInstance.clear_transition_events"></a>

#### clear_transition_events

```python
def clear_transition_events(event_name: Name) -> None
```

x.clear_transition_events(event_name) -> None
Removes all queued transition requests with the given event name

Args:
    event_name (Name):

<a id="unreal.AnimInstance.clear_morph_targets"></a>

#### clear_morph_targets

```python
def clear_morph_targets() -> None
```

x.clear_morph_targets() -> None
Clears the current morph targets.

<a id="unreal.AnimInstance.clear_all_transition_events"></a>

#### clear_all_transition_events

```python
def clear_all_transition_events() -> None
```

x.clear_all_transition_events() -> None
Removes all queued transition requests

<a id="unreal.AnimInstance.calculate_direction"></a>

#### calculate_direction

```python
def calculate_direction(velocity: Vector, base_rotation: Rotator) -> float
```

x.calculate_direction(velocity, base_rotation) -> float
Calculate Direction

Args:
    velocity (Vector): 
    base_rotation (Rotator): 

Returns:
    float:

<a id="unreal.AnimInstance.blueprint_update_animation"></a>

#### blueprint_update_animation

```python
def blueprint_update_animation(delta_time_x: float) -> None
```

x.blueprint_update_animation(delta_time_x) -> None
Executed when the Animation is updated

Args:
    delta_time_x (float):

<a id="unreal.AnimInstance.kismet_update_animation"></a>

#### kismet_update_animation

```python
def kismet_update_animation(delta_time_x: float) -> None
```

deprecated: 'kismet_update_animation' was renamed to 'blueprint_update_animation'.

<a id="unreal.AnimInstance.blueprint_thread_safe_update_animation"></a>

#### blueprint_thread_safe_update_animation

```python
def blueprint_thread_safe_update_animation(delta_time: float) -> None
```

x.blueprint_thread_safe_update_animation(delta_time) -> None
Executed when the Animation Blueprint is updated on a worker thread, just prior to graph update

Args:
    delta_time (float):

<a id="unreal.AnimInstance.blueprint_post_evaluate_animation"></a>

#### blueprint_post_evaluate_animation

```python
def blueprint_post_evaluate_animation() -> None
```

x.blueprint_post_evaluate_animation() -> None
Executed after the Animation is evaluated

<a id="unreal.AnimInstance.blueprint_linked_animation_layers_initialized"></a>

#### blueprint_linked_animation_layers_initialized

```python
def blueprint_linked_animation_layers_initialized() -> None
```

x.blueprint_linked_animation_layers_initialized() -> None
Executed when the all Linked Animation Layers are initialized

<a id="unreal.AnimInstance.blueprint_initialize_animation"></a>

#### blueprint_initialize_animation

```python
def blueprint_initialize_animation() -> None
```

x.blueprint_initialize_animation() -> None
Executed when the Animation is initialized

<a id="unreal.AnimInstance.kismet_initialize_animation"></a>

#### kismet_initialize_animation

```python
def kismet_initialize_animation() -> None
```

deprecated: 'kismet_initialize_animation' was renamed to 'blueprint_initialize_animation'.

<a id="unreal.AnimInstance.blueprint_begin_play"></a>

#### blueprint_begin_play

```python
def blueprint_begin_play() -> None
```

x.blueprint_begin_play() -> None
Executed when begin play is called on the owning component

<a id="unreal.AnimInstance.blueprint_get_slot_montage_local_weight"></a>

#### blueprint_get_slot_montage_local_weight

```python
def blueprint_get_slot_montage_local_weight(slot_node_name: Name) -> float
```

x.blueprint_get_slot_montage_local_weight(slot_node_name) -> float
Get local weight of any montages this slot node is playing. If this slot is not currently playing a montage, it will return 0.

Args:
    slot_node_name (Name): 

Returns:
    float:

<a id="unreal.AnimInstance.blueprint_get_main_anim_instance"></a>

#### blueprint_get_main_anim_instance

```python
def blueprint_get_main_anim_instance() -> AnimInstance
```

x.blueprint_get_main_anim_instance() -> AnimInstance
Get the 'main' anim instance, i.e. the one that is hosted on the skeletal mesh component

Returns:
    AnimInstance:

<a id="unreal.VimInstance"></a>