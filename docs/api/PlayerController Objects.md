## PlayerController Objects

```python
class PlayerController(Controller)
```

PlayerControllers are used by human players to control Pawns.

ControlRotation (accessed via GetControlRotation()), determines the aiming
orientation of the controlled Pawn.

In networked games, PlayerControllers exist on the server for every player-controlled pawn,
and also on the controlling client's machine. They do NOT exist on a client's
machine for pawns controlled by remote players elsewhere on the network.
see: https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Controller/PlayerController/

**C++ Source:**

- **Module**: Engine
- **File**: PlayerController.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``attach_to_pawn`` (bool):  [Read-Write] If true, the controller location will match the possessed Pawn's location. If false, it will not be updated. Rotation will match ControlRotation in either case.
  Since a Controller's location is normally inaccessible, this is intended mainly for purposes of being able to attach
  an Actor that follows the possessed Pawn location, but that still has the full aim rotation (since a Pawn might
  update only some components of the rotation).
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_manage_active_camera_target`` (bool):  [Read-Write] True to allow this player controller to manage the camera target for you,
  typically by using the possessed pawn as the camera target. Set to false
  if you want to manually control the camera target.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``cheat_class`` (type(Class)):  [Read-Write] Class of my CheatManager.
  see: CheatManager for more information about when it will be instantiated.
- ``cheat_manager`` (CheatManager):  [Read-Write] Object that manages "cheat" commands.

  By default:
        - In Shipping configurations, the manager is always disabled because UE_WITH_CHEAT_MANAGER is 0
    - When playing in the editor, cheats are always enabled
    - In other cases, cheats are enabled by default in single player games but can be forced on with the EnableCheats console command

  This behavior can be changed either by overriding APlayerController::EnableCheats or AGameModeBase::AllowCheats.
- ``click_event_keys`` (Array[Key]):  [Read-Write] List of keys that will cause click events to be forwarded, default to left click
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``current_click_trace_channel`` (CollisionChannel):  [Read-Write] Trace channel currently being used for determining what world object was clicked on.
- ``current_mouse_cursor`` (MouseCursor):  [Read-Write] Currently visible mouse cursor
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_click_trace_channel`` (CollisionChannel):  [Read-Write] Default trace channel used for determining what world object was clicked on.
- ``default_mouse_cursor`` (MouseCursor):  [Read-Write] Type of mouse cursor to show by default
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enable_click_events`` (bool):  [Read-Write] Whether actor/component click events should be generated.
- ``enable_motion_controls`` (bool):  [Read-Write] Whether or not to consider input from motion sources (tilt, acceleration, etc)
- ``enable_mouse_over_events`` (bool):  [Read-Write] Whether actor/component mouse over events should be generated.
- ``enable_streaming_source`` (bool):  [Read-Write] Whether the PlayerController should be used as a World Partiton streaming source.
- ``enable_touch_events`` (bool):  [Read-Write] Whether actor/component touch events should be generated.
- ``enable_touch_over_events`` (bool):  [Read-Write] Whether actor/component touch over events should be generated.
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``force_feedback_enabled`` (bool):  [Read-Write]
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hit_result_trace_distance`` (float):  [Read-Write] Distance to trace when computing click events
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_pitch_scale`` (float):  [Read-Write] Pitch input speed scaling
  deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``input_roll_scale`` (float):  [Read-Write] Roll input speed scaling
  deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior
- ``input_yaw_scale`` (float):  [Read-Write] Yaw input speed scaling
  deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``net_cull_distance_squared`` (float):  [Read-Write]
- ``net_dormancy`` (NetDormancy):  [Read-Write] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.
- ``net_load_on_client`` (bool):  [Read-Write] This actor will be loaded on network clients during map load
- ``net_priority`` (float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate
- ``net_update_frequency`` (float):  [Read-Write]
- ``net_use_owner_relevancy`` (bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority
- ``on_actor_begin_overlap`` (ActorBeginOverlapSignature):  [Read-Write] Called when another actor begins to overlap this actor, for example a player walking into a trigger.
  For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
  note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.
- ``on_actor_end_overlap`` (ActorEndOverlapSignature):  [Read-Write] Called when another actor stops overlapping this actor.
  note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.
- ``on_actor_hit`` (ActorHitSignature):  [Read-Write] Called when this Actor hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
  For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.
  note: For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled.
- ``on_begin_cursor_over`` (ActorBeginCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved over this actor if mouse over events are enabled in the player controller.
- ``on_clicked`` (ActorOnClickedSignature):  [Read-Write] Called when the left mouse button is clicked while the mouse is over this actor and click events are enabled in the player controller.
- ``on_destroyed`` (ActorDestroyedSignature):  [Read-Write] Event triggered when the actor has been explicitly destroyed.
- ``on_end_cursor_over`` (ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.
- ``on_end_play`` (ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.
- ``on_input_touch_begin`` (ActorOnInputTouchBeginSignature):  [Read-Write] Called when a touch input is received over this actor when touch events are enabled in the player controller.
- ``on_input_touch_end`` (ActorOnInputTouchEndSignature):  [Read-Write] Called when a touch input is received over this component when touch events are enabled in the player controller.
- ``on_input_touch_enter`` (ActorBeginTouchOverSignature):  [Read-Write] Called when a finger is moved over this actor when touch over events are enabled in the player controller.
- ``on_input_touch_leave`` (ActorEndTouchOverSignature):  [Read-Write] Called when a finger is moved off this actor when touch over events are enabled in the player controller.
- ``on_instigated_any_damage`` (InstigatedAnyDamageSignature):  [Read-Write] Called when the controller has instigated damage in any way
- ``on_possessed_pawn_changed`` (OnPossessedPawnChanged):  [Read-Write] Called on both authorities and clients when the possessed pawn changes (either OldPawn or NewPawn might be nullptr)
- ``on_released`` (ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``override_player_input_class`` (type(Class)):  [Read-Write] If set, then this UPlayerInput class will be used instead of the Input Settings' DefaultPlayerInputClass
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``player_camera_manager`` (PlayerCameraManager):  [Read-Write] Camera manager associated with this Player Controller.
- ``player_camera_manager_class`` (type(Class)):  [Read-Write] PlayerCamera class should be set for each game, otherwise Engine.PlayerCameraManager is used
- ``player_is_waiting`` (bool):  [Read-Only] True if PlayerController is currently waiting for the match to start or to respawn. Only valid in Spectating state.
- ``player_state`` (PlayerState):  [Read-Write] PlayerState containing replicated information about the player using this controller (only exists for players, not NPCs).
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``relevant_for_level_bounds`` (bool):  [Read-Write] If true, this actor's component's bounds will be included in the level's
  bounding box unless the Actor's class has overridden IsLevelBoundsRelevant
- ``remote_role`` (NetRole):  [Read-Only] Describes how much control the remote machine has over the actor.
- ``replay_rewindable`` (bool):  [Read-Write] If true, this actor will only be destroyed during scrubbing if the replay is set to a time before the actor existed.
  Otherwise, RewindForReplay will be called if we detect the actor needs to be reset.
  Note, this Actor must not be destroyed by gamecode, and RollbackViaDeletion may not be used.
- ``replicate_movement`` (bool):  [Read-Write] If true, replicate movement/location related properties.
  Actor must also be set to replicate.
  see: SetReplicates()
  see: https://docs.unrealengine.com/InteractiveExperiences/Networking/Actors
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects and the replicated actor components list
  When false the replication system will instead call the virtual ReplicateSubobjects() function where the subobjects and actor components need to be manually replicated.
- ``replicated_movement`` (RepMovement):  [Read-Write] Used for replication of our RootComponent's position and velocity
- ``replicates`` (bool):  [Read-Write] If true, this actor will replicate to remote machines
  see: SetReplicates()
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``should_perform_full_tick_when_paused`` (bool):  [Read-Write] Whether we fully tick when the game is paused, if our tick function is allowed to do so. If false, we do a minimal update during the tick.
- ``show_mouse_cursor`` (bool):  [Read-Write] Whether the mouse cursor should be displayed.
- ``smooth_target_view_rotation_speed`` (float):  [Read-Write] Interp speed for blending remote view rotation for smoother client updates
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``streaming_source_debug_color`` (Color):  [Read-Write] Color used for debugging.
- ``streaming_source_priority`` (StreamingSourcePriority):  [Read-Write] PlayerController streaming source priority.
- ``streaming_source_shapes`` (Array[StreamingSourceShape]):  [Read-Write] Optional aggregated shape list used to build a custom shape for the streaming source. When empty, fallbacks sphere shape with a radius equal to grid's loading range.
- ``streaming_source_should_activate`` (bool):  [Read-Write] Whether the PlayerController streaming source should activate cells after loading.
- ``streaming_source_should_block_on_slow_streaming`` (bool):  [Read-Write] Whether the PlayerController streaming source should block on slow streaming.
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Write] Condition for calling UpdateOverlaps() to initialize overlap state when loaded in during level streaming.
  If set to 'UseConfigDefault', the default specified in ini (displayed in 'DefaultUpdateOverlapsMethodDuringLevelStreaming') will be used.
  If overlaps are not initialized, this actor and attached components will not have an initial state of what objects are touching it,
  and overlap events may only come in once one of those objects update overlaps themselves (for example when moving).
  However if an object touching it *does* initialize state, both objects will know about their touching state with each other.
  This can be a potentially large performance savings during level loading and streaming, and is safe if the object and others initially
  overlapping it do not need the overlap state because they will not trigger overlap notifications.

  Note that if 'bGenerateOverlapEventsDuringLevelStreaming' is true, overlaps are always updated in this case, but that flag
  determines whether the Begin/End overlap events are triggered.
  see: bGenerateOverlapEventsDuringLevelStreaming, DefaultUpdateOverlapsMethodDuringLevelStreaming, GetUpdateOverlapsMethodDuringLevelStreaming()

<a id="unreal.PlayerController.player_camera_manager"></a>

#### player_camera_manager

```python
@property
def player_camera_manager() -> PlayerCameraManager
```

(PlayerCameraManager):  [Read-Only] Camera manager associated with this Player Controller.

<a id="unreal.PlayerController.player_camera"></a>

#### player_camera

```python
@property
def player_camera() -> PlayerCameraManager
```

deprecated: 'player_camera' was renamed to 'player_camera_manager'.

<a id="unreal.PlayerController.player_camera_manager_class"></a>

#### player_camera_manager_class

```python
@property
def player_camera_manager_class() -> Class
```

(type(Class)):  [Read-Only] PlayerCamera class should be set for each game, otherwise Engine.PlayerCameraManager is used

<a id="unreal.PlayerController.player_camera_class"></a>

#### player_camera_class

```python
@property
def player_camera_class() -> Class
```

deprecated: 'player_camera_class' was renamed to 'player_camera_manager_class'.

<a id="unreal.PlayerController.smooth_target_view_rotation_speed"></a>

#### smooth_target_view_rotation_speed

```python
@property
def smooth_target_view_rotation_speed() -> float
```

(float):  [Read-Write] Interp speed for blending remote view rotation for smoother client updates

<a id="unreal.PlayerController.smooth_target_view_rotation_speed"></a>

#### smooth_target_view_rotation_speed

```python
@smooth_target_view_rotation_speed.setter
def smooth_target_view_rotation_speed(value: float) -> None
```

<a id="unreal.PlayerController.cheat_manager"></a>

#### cheat_manager

```python
@property
def cheat_manager() -> CheatManager
```

(CheatManager):  [Read-Only] Object that manages "cheat" commands.

By default:
      - In Shipping configurations, the manager is always disabled because UE_WITH_CHEAT_MANAGER is 0
  - When playing in the editor, cheats are always enabled
  - In other cases, cheats are enabled by default in single player games but can be forced on with the EnableCheats console command

This behavior can be changed either by overriding APlayerController::EnableCheats or AGameModeBase::AllowCheats.

<a id="unreal.PlayerController.cheat_class"></a>

#### cheat_class

```python
@property
def cheat_class() -> Class
```

(type(Class)):  [Read-Only] Class of my CheatManager.
see: CheatManager for more information about when it will be instantiated.

<a id="unreal.PlayerController.player_is_waiting"></a>

#### player_is_waiting

```python
@property
def player_is_waiting() -> bool
```

(bool):  [Read-Only] True if PlayerController is currently waiting for the match to start or to respawn. Only valid in Spectating state.

<a id="unreal.PlayerController.input_yaw_scale"></a>

#### input_yaw_scale

```python
@property
def input_yaw_scale() -> float
```

(float):  [Read-Write] Yaw input speed scaling
deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior

<a id="unreal.PlayerController.input_yaw_scale"></a>

#### input_yaw_scale

```python
@input_yaw_scale.setter
def input_yaw_scale(value: float) -> None
```

<a id="unreal.PlayerController.look_right_scale"></a>

#### look_right_scale

```python
@property
def look_right_scale() -> float
```

deprecated: 'look_right_scale' was renamed to 'input_yaw_scale'.

<a id="unreal.PlayerController.look_right_scale"></a>

#### look_right_scale

```python
@look_right_scale.setter
def look_right_scale(value: float) -> None
```

<a id="unreal.PlayerController.input_pitch_scale"></a>

#### input_pitch_scale

```python
@property
def input_pitch_scale() -> float
```

(float):  [Read-Write] Pitch input speed scaling
deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior

<a id="unreal.PlayerController.input_pitch_scale"></a>

#### input_pitch_scale

```python
@input_pitch_scale.setter
def input_pitch_scale(value: float) -> None
```

<a id="unreal.PlayerController.look_up_scale"></a>

#### look_up_scale

```python
@property
def look_up_scale() -> float
```

deprecated: 'look_up_scale' was renamed to 'input_pitch_scale'.

<a id="unreal.PlayerController.look_up_scale"></a>

#### look_up_scale

```python
@look_up_scale.setter
def look_up_scale(value: float) -> None
```

<a id="unreal.PlayerController.input_roll_scale"></a>

#### input_roll_scale

```python
@property
def input_roll_scale() -> float
```

(float):  [Read-Write] Roll input speed scaling
deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior

<a id="unreal.PlayerController.input_roll_scale"></a>

#### input_roll_scale

```python
@input_roll_scale.setter
def input_roll_scale(value: float) -> None
```

<a id="unreal.PlayerController.show_mouse_cursor"></a>

#### show_mouse_cursor

```python
@property
def show_mouse_cursor() -> bool
```

(bool):  [Read-Write] Whether the mouse cursor should be displayed.

<a id="unreal.PlayerController.show_mouse_cursor"></a>

#### show_mouse_cursor

```python
@show_mouse_cursor.setter
def show_mouse_cursor(value: bool) -> None
```

<a id="unreal.PlayerController.enable_click_events"></a>

#### enable_click_events

```python
@property
def enable_click_events() -> bool
```

(bool):  [Read-Write] Whether actor/component click events should be generated.

<a id="unreal.PlayerController.enable_click_events"></a>

#### enable_click_events

```python
@enable_click_events.setter
def enable_click_events(value: bool) -> None
```

<a id="unreal.PlayerController.enable_touch_events"></a>

#### enable_touch_events

```python
@property
def enable_touch_events() -> bool
```

(bool):  [Read-Write] Whether actor/component touch events should be generated.

<a id="unreal.PlayerController.enable_touch_events"></a>

#### enable_touch_events

```python
@enable_touch_events.setter
def enable_touch_events(value: bool) -> None
```

<a id="unreal.PlayerController.enable_mouse_over_events"></a>

#### enable_mouse_over_events

```python
@property
def enable_mouse_over_events() -> bool
```

(bool):  [Read-Write] Whether actor/component mouse over events should be generated.

<a id="unreal.PlayerController.enable_mouse_over_events"></a>

#### enable_mouse_over_events

```python
@enable_mouse_over_events.setter
def enable_mouse_over_events(value: bool) -> None
```

<a id="unreal.PlayerController.enable_touch_over_events"></a>

#### enable_touch_over_events

```python
@property
def enable_touch_over_events() -> bool
```

(bool):  [Read-Write] Whether actor/component touch over events should be generated.

<a id="unreal.PlayerController.enable_touch_over_events"></a>

#### enable_touch_over_events

```python
@enable_touch_over_events.setter
def enable_touch_over_events(value: bool) -> None
```

<a id="unreal.PlayerController.force_feedback_enabled"></a>

#### force_feedback_enabled

```python
@property
def force_feedback_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PlayerController.force_feedback_enabled"></a>

#### force_feedback_enabled

```python
@force_feedback_enabled.setter
def force_feedback_enabled(value: bool) -> None
```

<a id="unreal.PlayerController.enable_motion_controls"></a>

#### enable_motion_controls

```python
@property
def enable_motion_controls() -> bool
```

(bool):  [Read-Write] Whether or not to consider input from motion sources (tilt, acceleration, etc)

<a id="unreal.PlayerController.enable_motion_controls"></a>

#### enable_motion_controls

```python
@enable_motion_controls.setter
def enable_motion_controls(value: bool) -> None
```

<a id="unreal.PlayerController.enable_streaming_source"></a>

#### enable_streaming_source

```python
@property
def enable_streaming_source() -> bool
```

(bool):  [Read-Write] Whether the PlayerController should be used as a World Partiton streaming source.

<a id="unreal.PlayerController.enable_streaming_source"></a>

#### enable_streaming_source

```python
@enable_streaming_source.setter
def enable_streaming_source(value: bool) -> None
```

<a id="unreal.PlayerController.streaming_source_should_activate"></a>

#### streaming_source_should_activate

```python
@property
def streaming_source_should_activate() -> bool
```

(bool):  [Read-Write] Whether the PlayerController streaming source should activate cells after loading.

<a id="unreal.PlayerController.streaming_source_should_activate"></a>

#### streaming_source_should_activate

```python
@streaming_source_should_activate.setter
def streaming_source_should_activate(value: bool) -> None
```

<a id="unreal.PlayerController.streaming_source_should_block_on_slow_streaming"></a>

#### streaming_source_should_block_on_slow_streaming

```python
@property
def streaming_source_should_block_on_slow_streaming() -> bool
```

(bool):  [Read-Write] Whether the PlayerController streaming source should block on slow streaming.

<a id="unreal.PlayerController.streaming_source_should_block_on_slow_streaming"></a>

#### streaming_source_should_block_on_slow_streaming

```python
@streaming_source_should_block_on_slow_streaming.setter
def streaming_source_should_block_on_slow_streaming(value: bool) -> None
```

<a id="unreal.PlayerController.streaming_source_priority"></a>

#### streaming_source_priority

```python
@property
def streaming_source_priority() -> StreamingSourcePriority
```

(StreamingSourcePriority):  [Read-Write] PlayerController streaming source priority.

<a id="unreal.PlayerController.streaming_source_priority"></a>

#### streaming_source_priority

```python
@streaming_source_priority.setter
def streaming_source_priority(value: StreamingSourcePriority) -> None
```

<a id="unreal.PlayerController.streaming_source_debug_color"></a>

#### streaming_source_debug_color

```python
@property
def streaming_source_debug_color() -> Color
```

(Color):  [Read-Write] Color used for debugging.

<a id="unreal.PlayerController.streaming_source_debug_color"></a>

#### streaming_source_debug_color

```python
@streaming_source_debug_color.setter
def streaming_source_debug_color(value: Color) -> None
```

<a id="unreal.PlayerController.streaming_source_shapes"></a>

#### streaming_source_shapes

```python
@property
def streaming_source_shapes() -> Array[StreamingSourceShape]
```

(Array[StreamingSourceShape]):  [Read-Write] Optional aggregated shape list used to build a custom shape for the streaming source. When empty, fallbacks sphere shape with a radius equal to grid's loading range.

<a id="unreal.PlayerController.streaming_source_shapes"></a>

#### streaming_source_shapes

```python
@streaming_source_shapes.setter
def streaming_source_shapes(value: Array[StreamingSourceShape]) -> None
```

<a id="unreal.PlayerController.click_event_keys"></a>

#### click_event_keys

```python
@property
def click_event_keys() -> Array[Key]
```

(Array[Key]):  [Read-Write] List of keys that will cause click events to be forwarded, default to left click

<a id="unreal.PlayerController.click_event_keys"></a>

#### click_event_keys

```python
@click_event_keys.setter
def click_event_keys(value: Array[Key]) -> None
```

<a id="unreal.PlayerController.default_mouse_cursor"></a>

#### default_mouse_cursor

```python
@property
def default_mouse_cursor() -> MouseCursor
```

(MouseCursor):  [Read-Only] Type of mouse cursor to show by default

<a id="unreal.PlayerController.current_mouse_cursor"></a>

#### current_mouse_cursor

```python
@property
def current_mouse_cursor() -> MouseCursor
```

(MouseCursor):  [Read-Write] Currently visible mouse cursor

<a id="unreal.PlayerController.current_mouse_cursor"></a>

#### current_mouse_cursor

```python
@current_mouse_cursor.setter
def current_mouse_cursor(value: MouseCursor) -> None
```

<a id="unreal.PlayerController.default_click_trace_channel"></a>

#### default_click_trace_channel

```python
@property
def default_click_trace_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Only] Default trace channel used for determining what world object was clicked on.

<a id="unreal.PlayerController.current_click_trace_channel"></a>

#### current_click_trace_channel

```python
@property
def current_click_trace_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write] Trace channel currently being used for determining what world object was clicked on.

<a id="unreal.PlayerController.current_click_trace_channel"></a>

#### current_click_trace_channel

```python
@current_click_trace_channel.setter
def current_click_trace_channel(value: CollisionChannel) -> None
```

<a id="unreal.PlayerController.hit_result_trace_distance"></a>

#### hit_result_trace_distance

```python
@property
def hit_result_trace_distance() -> float
```

(float):  [Read-Write] Distance to trace when computing click events

<a id="unreal.PlayerController.hit_result_trace_distance"></a>

#### hit_result_trace_distance

```python
@hit_result_trace_distance.setter
def hit_result_trace_distance(value: float) -> None
```

<a id="unreal.PlayerController.should_perform_full_tick_when_paused"></a>

#### should_perform_full_tick_when_paused

```python
@property
def should_perform_full_tick_when_paused() -> bool
```

(bool):  [Read-Write] Whether we fully tick when the game is paused, if our tick function is allowed to do so. If false, we do a minimal update during the tick.

<a id="unreal.PlayerController.should_perform_full_tick_when_paused"></a>

#### should_perform_full_tick_when_paused

```python
@should_perform_full_tick_when_paused.setter
def should_perform_full_tick_when_paused(value: bool) -> None
```

<a id="unreal.PlayerController.was_input_key_just_released"></a>

#### was_input_key_just_released

```python
def was_input_key_just_released(key: Key) -> bool
```

x.was_input_key_just_released(key) -> bool
Returns true if the given key/button was down last frame and up this frame.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.PlayerController.was_input_key_just_pressed"></a>

#### was_input_key_just_pressed

```python
def was_input_key_just_pressed(key: Key) -> bool
```

x.was_input_key_just_pressed(key) -> bool
Returns true if the given key/button was up last frame and down this frame.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.PlayerController.streaming_source_should_block_on_slow_streaming"></a>

#### streaming_source_should_block_on_slow_streaming

```python
def streaming_source_should_block_on_slow_streaming() -> bool
```

x.streaming_source_should_block_on_slow_streaming() -> bool
Whether the PlayerController streaming source should block on slow streaming.
Default implementation returns bStreamingSourceShouldBlockOnSlowStreaming but can be overriden in child classes.

Returns:
    bool: true if it should.

<a id="unreal.PlayerController.streaming_source_should_activate"></a>

#### streaming_source_should_activate

```python
def streaming_source_should_activate() -> bool
```

x.streaming_source_should_activate() -> bool
Whether the PlayerController streaming source should activate cells after loading.
Default implementation returns bStreamingSourceShouldActivate but can be overriden in child classes.

Returns:
    bool: true if it should.

<a id="unreal.PlayerController.stop_haptic_effect"></a>

#### stop_haptic_effect

```python
def stop_haptic_effect(hand: ControllerHand) -> None
```

x.stop_haptic_effect(hand) -> None
Stops a playing haptic feedback curve

Args:
    hand (ControllerHand): Which hand to stop the effect for

<a id="unreal.PlayerController.set_virtual_joystick_visibility"></a>

#### set_virtual_joystick_visibility

```python
def set_virtual_joystick_visibility(visible: bool) -> None
```

x.set_virtual_joystick_visibility(visible) -> None
Set the virtual joystick visibility.

Args:
    visible (bool):

<a id="unreal.PlayerController.set_view_target_with_blend"></a>

#### set_view_target_with_blend

```python
def set_view_target_with_blend(
        new_view_target: Actor,
        blend_time: float = 0.000000,
        blend_func: ViewTargetBlendFunction = ViewTargetBlendFunction.
    VT_BLEND_LINEAR,
        blend_exp: float = 0.000000,
        lock_outgoing: bool = False) -> None
```

x.set_view_target_with_blend(new_view_target, blend_time=0.000000, blend_func=ViewTargetBlendFunction.VT_BLEND_LINEAR, blend_exp=0.000000, lock_outgoing=False) -> None
Set the view target blending with variable control

Args:
    new_view_target (Actor): new actor to set as view target
    blend_time (float): time taken to blend
    blend_func (ViewTargetBlendFunction): Cubic, Linear etc functions for blending
    blend_exp (float): Exponent, used by certain blend functions to control the shape of the curve.
    lock_outgoing (bool): If true, lock outgoing viewtarget to last frame's camera position for the remainder of the blend.

<a id="unreal.PlayerController.set_mouse_location"></a>

#### set_mouse_location

```python
def set_mouse_location(x: int, y: int) -> None
```

x.set_mouse_location(x, y) -> None
Positions the mouse cursor in screen space, in pixels.

Args:
    x (int32): 
    y (int32):

<a id="unreal.PlayerController.set_mouse_cursor_widget"></a>

#### set_mouse_cursor_widget

```python
def set_mouse_cursor_widget(cursor: MouseCursor,
                            cursor_widget: UserWidget) -> None
```

x.set_mouse_cursor_widget(cursor, cursor_widget) -> None
Sets the Widget for the Mouse Cursor to display

Args:
    cursor (MouseCursor): the cursor to set the widget for
    cursor_widget (UserWidget): the widget to set the cursor to

<a id="unreal.PlayerController.set_haptics_by_value"></a>

#### set_haptics_by_value

```python
def set_haptics_by_value(frequency: float, amplitude: float,
                         hand: ControllerHand) -> None
```

x.set_haptics_by_value(frequency, amplitude, hand) -> None
Sets the value of the haptics for the specified hand directly, using frequency and amplitude.  NOTE:  If a curve is already
playing for this hand, it will be cancelled in favour of the specified values.

Args:
    frequency (float): The normalized frequency [0.0, 1.0] to play through the haptics system
    amplitude (float): The normalized amplitude [0.0, 1.0] to set the haptic feedback to
    hand (ControllerHand): Which hand to play the effect on

<a id="unreal.PlayerController.set_disable_haptics"></a>

#### set_disable_haptics

```python
def set_disable_haptics(new_disabled: bool) -> None
```

x.set_disable_haptics(new_disabled) -> None
Allows the player controller to disable all haptic requests from being fired, e.g. in the case of a level loading

Args:
    new_disabled (bool): If TRUE, the haptics will stop and prevented from being enabled again until set to FALSE

<a id="unreal.PlayerController.set_deprecated_input_yaw_scale"></a>

#### set_deprecated_input_yaw_scale

```python
def set_deprecated_input_yaw_scale(new_value: float) -> None
```

x.set_deprecated_input_yaw_scale(new_value) -> None
Set Deprecated Input Yaw Scale

Args:
    new_value (float):

<a id="unreal.PlayerController.set_deprecated_input_roll_scale"></a>

#### set_deprecated_input_roll_scale

```python
def set_deprecated_input_roll_scale(new_value: float) -> None
```

x.set_deprecated_input_roll_scale(new_value) -> None
Set Deprecated Input Roll Scale

Args:
    new_value (float):

<a id="unreal.PlayerController.set_deprecated_input_pitch_scale"></a>

#### set_deprecated_input_pitch_scale

```python
def set_deprecated_input_pitch_scale(new_value: float) -> None
```

x.set_deprecated_input_pitch_scale(new_value) -> None
Set Deprecated Input Pitch Scale

Args:
    new_value (float):

<a id="unreal.PlayerController.set_controller_light_color"></a>

#### set_controller_light_color

```python
def set_controller_light_color(color: Color) -> None
```

x.set_controller_light_color(color) -> None
Sets the light color of the player's controller

Args:
    color (Color): The color for the light to be

<a id="unreal.PlayerController.set_controller_dead_zones"></a>

#### set_controller_dead_zones

```python
def set_controller_dead_zones(left_dead_zone: float,
                              right_dead_zone: float) -> None
```

x.set_controller_dead_zones(left_dead_zone, right_dead_zone) -> None
Sets the deadzones of the player's controller

Args:
    left_dead_zone (float): Inner DeadZone for the left analog stick
    right_dead_zone (float): Inner DeadZone for the right analog stick

<a id="unreal.PlayerController.set_cinematic_mode"></a>

#### set_cinematic_mode

```python
def set_cinematic_mode(cinematic_mode: bool,
                       hide_player: bool = True,
                       affects_hud: bool = True,
                       affects_movement: bool = ...,
                       affects_turning: bool = ...) -> None
```

x.set_cinematic_mode(cinematic_mode, hide_player=True, affects_hud=True, affects_movement, affects_turning) -> None
Server/SP only function for changing whether the player is in cinematic mode.  Updates values of various state variables, then replicates the call to the client
to sync the current cinematic mode.

Args:
    cinematic_mode (bool): specify true if the player is entering cinematic mode; false if the player is leaving cinematic mode.
    hide_player (bool): specify true to hide the player's pawn (only relevant if bInCinematicMode is true)
    affects_hud (bool): specify true if we should show/hide the HUD to match the value of bCinematicMode
    affects_movement (bool): specify true to disable movement in cinematic mode, enable it when leaving
    affects_turning (bool): specify true to disable turning in cinematic mode or enable it when leaving

<a id="unreal.PlayerController.set_audio_listener_override"></a>

#### set_audio_listener_override

```python
def set_audio_listener_override(attach_to_component: SceneComponent,
                                location: Vector, rotation: Rotator) -> None
```

x.set_audio_listener_override(attach_to_component, location, rotation) -> None
Used to override the default positioning of the audio listener

Args:
    attach_to_component (SceneComponent): Optional component to attach the audio listener to
    location (Vector): Depending on whether Component is attached this is either an offset from its location or an absolute position
    rotation (Rotator): Depending on whether Component is attached this is either an offset from its rotation or an absolute rotation

<a id="unreal.PlayerController.set_audio_listener_attenuation_override"></a>

#### set_audio_listener_attenuation_override

```python
def set_audio_listener_attenuation_override(
        attach_to_component: SceneComponent,
        attenuation_location_o_verride: Vector) -> None
```

x.set_audio_listener_attenuation_override(attach_to_component, attenuation_location_o_verride) -> None
Set Audio Listener Attenuation Override

Args:
    attach_to_component (SceneComponent): 
    attenuation_location_o_verride (Vector):

<a id="unreal.PlayerController.reset_controller_light_color"></a>

#### reset_controller_light_color

```python
def reset_controller_light_color() -> None
```

x.reset_controller_light_color() -> None
Resets the light color of the player's controller to default

<a id="unreal.PlayerController.reset_controller_dead_zones"></a>

#### reset_controller_dead_zones

```python
def reset_controller_dead_zones() -> None
```

x.reset_controller_dead_zones() -> None
Resets the player's controller deadzones to default

<a id="unreal.PlayerController.project_world_location_to_screen"></a>

#### project_world_location_to_screen

```python
def project_world_location_to_screen(
        world_location: Vector,
        player_viewport_relative: bool = False) -> Optional[Vector2D]
```

x.project_world_location_to_screen(world_location, player_viewport_relative=False) -> Vector2D or None
Convert a World Space 3D position into a 2D Screen Space position.

Args:
    world_location (Vector): 
    player_viewport_relative (bool): 

Returns:
    Vector2D or None: true if the world coordinate was successfully projected to the screen.

    screen_location (Vector2D):

<a id="unreal.PlayerController.play_haptic_effect"></a>

#### play_haptic_effect

```python
def play_haptic_effect(haptic_effect: HapticFeedbackEffect_Base,
                       hand: ControllerHand,
                       scale: float = 1.000000,
                       loop: bool = False) -> None
```

x.play_haptic_effect(haptic_effect, hand, scale=1.000000, loop=False) -> None
Play a haptic feedback curve on the player's controller

Args:
    haptic_effect (HapticFeedbackEffect_Base): The haptic effect to play
    hand (ControllerHand): Which hand to play the effect on
    scale (float): Scale between 0.0 and 1.0 on the intensity of playback
    loop (bool):

<a id="unreal.PlayerController.play_dynamic_force_feedback"></a>

#### play_dynamic_force_feedback

```python
def play_dynamic_force_feedback(intensity: float,
                                duration: float = -1.000000,
                                affects_left_large: bool = True,
                                affects_left_small: bool = True,
                                affects_right_large: bool = True,
                                affects_right_small: bool = True,
                                action: DynamicForceFeedbackAction = ...,
                                latent_info: LatentActionInfo = ...) -> None
```

x.play_dynamic_force_feedback(intensity, duration=-1.000000, affects_left_large=True, affects_left_small=True, affects_right_large=True, affects_right_small=True, action, latent_info) -> None
Latent action that controls the playing of force feedback
Begins playing when Start is called.  Calling Update or Stop if the feedback is not active will have no effect.
Completed will execute when Stop is called or the duration ends.
When Update is called the Intensity, Duration, and affect values will be updated with the current inputs

Args:
    intensity (float): How strong the feedback should be.  Valid values are between 0.0 and 1.0
    duration (float): How long the feedback should play for.  If the value is negative it will play until stopped
    affects_left_large (bool): Whether the intensity should be applied to the large left servo
    affects_left_small (bool): Whether the intensity should be applied to the small left servo
    affects_right_large (bool): Whether the intensity should be applied to the large right servo
    affects_right_small (bool): Whether the intensity should be applied to the small right servo
    action (DynamicForceFeedbackAction): 
    latent_info (LatentActionInfo):

<a id="unreal.PlayerController.k2_client_play_force_feedback"></a>

#### k2_client_play_force_feedback

```python
def k2_client_play_force_feedback(force_feedback_effect: ForceFeedbackEffect,
                                  tag: Name, looping: bool,
                                  ignore_time_dilation: bool,
                                  play_while_paused: bool) -> None
```

x.k2_client_play_force_feedback(force_feedback_effect, tag, looping, ignore_time_dilation, play_while_paused) -> None
Play a force feedback pattern on the player's controller

Args:
    force_feedback_effect (ForceFeedbackEffect): The force feedback pattern to play
    tag (Name): A tag that allows stopping of an effect.  If another effect with this Tag is playing, it will be stopped and replaced
    looping (bool): Whether the pattern should be played repeatedly or be a single one shot
    ignore_time_dilation (bool): Whether the pattern should ignore time dilation
    play_while_paused (bool): Whether the pattern should continue to play while the game is paused

<a id="unreal.PlayerController.client_play_force_feedback"></a>

#### client_play_force_feedback

```python
def client_play_force_feedback(force_feedback_effect: ForceFeedbackEffect,
                               tag: Name, looping: bool,
                               ignore_time_dilation: bool,
                               play_while_paused: bool) -> None
```

deprecated: 'client_play_force_feedback' was renamed to 'k2_client_play_force_feedback'.

<a id="unreal.PlayerController.is_streaming_source_enabled"></a>

#### is_streaming_source_enabled

```python
def is_streaming_source_enabled() -> bool
```

x.is_streaming_source_enabled() -> bool
Whether the PlayerController should be used as a World Partiton streaming source.
Default implementation returns bEnableStreamingSource but can be overriden in child classes.

Returns:
    bool: true if it should.

<a id="unreal.PlayerController.is_input_key_down"></a>

#### is_input_key_down

```python
def is_input_key_down(key: Key) -> bool
```

x.is_input_key_down(key) -> bool
Returns true if the given key/button is pressed on the input of the controller (if present)

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.PlayerController.get_viewport_size"></a>

#### get_viewport_size

```python
def get_viewport_size() -> Tuple[int, int]
```

x.get_viewport_size() -> (size_x=int32, size_y=int32)
Helper to get the size of the HUD canvas for this player controller.  Returns 0 if there is no HUD

Returns:
    tuple: 

    size_x (int32): 

    size_y (int32):

<a id="unreal.PlayerController.get_streaming_source_shapes"></a>

#### get_streaming_source_shapes

```python
def get_streaming_source_shapes() -> Array[StreamingSourceShape]
```

x.get_streaming_source_shapes() -> Array[StreamingSourceShape]
Gets the streaming source priority.
Default implementation returns StreamingSourceShapes but can be overriden in child classes.

Returns:
    Array[StreamingSourceShape]: 

    out_shapes (Array[StreamingSourceShape]):

<a id="unreal.PlayerController.get_streaming_source_priority"></a>

#### get_streaming_source_priority

```python
def get_streaming_source_priority() -> StreamingSourcePriority
```

x.get_streaming_source_priority() -> StreamingSourcePriority
Gets the streaming source priority.
Default implementation returns StreamingSourcePriority but can be overriden in child classes.

Returns:
    StreamingSourcePriority: the streaming source priority.

<a id="unreal.PlayerController.get_streaming_source_location_and_rotation"></a>

#### get_streaming_source_location_and_rotation

```python
def get_streaming_source_location_and_rotation() -> Tuple[Vector, Rotator]
```

x.get_streaming_source_location_and_rotation() -> (out_location=Vector, out_rotation=Rotator)
Gets the streaming source location and rotation.
Default implementation returns APlayerController::GetPlayerViewPoint but can be overriden in child classes.

Returns:
    tuple: 

    out_location (Vector): 

    out_rotation (Rotator):

<a id="unreal.PlayerController.get_spectator_pawn"></a>

#### get_spectator_pawn

```python
def get_spectator_pawn() -> SpectatorPawn
```

x.get_spectator_pawn() -> SpectatorPawn
Get the Pawn used when spectating. nullptr when not spectating.

Returns:
    SpectatorPawn:

<a id="unreal.PlayerController.get_platform_user_id"></a>

#### get_platform_user_id

```python
def get_platform_user_id() -> PlatformUserId
```

x.get_platform_user_id() -> PlatformUserId
Returns the platform user that is assigned to this Player Controller's Local Player.
If there is no local player, then this will return PLATFORMUSERID_NONE

Returns:
    PlatformUserId:

<a id="unreal.PlayerController.get_override_player_input_class"></a>

#### get_override_player_input_class

```python
def get_override_player_input_class() -> Class
```

x.get_override_player_input_class() -> type(Class)
Get Override Player Input Class

Returns:
    type(Class):

<a id="unreal.PlayerController.get_mouse_position"></a>

#### get_mouse_position

```python
def get_mouse_position() -> Optional[Tuple[float, float]]
```

x.get_mouse_position() -> (location_x=float, location_y=float) or None
Retrieves the X and Y screen coordinates of the mouse cursor. Returns false if there is no associated mouse device

Returns:
    tuple or None: 

    location_x (float): 

    location_y (float):

<a id="unreal.PlayerController.get_input_vector_key_state"></a>

#### get_input_vector_key_state

```python
def get_input_vector_key_state(key: Key) -> Vector
```

x.get_input_vector_key_state(key) -> Vector
Returns the vector value for the given key/button.

Args:
    key (Key): 

Returns:
    Vector:

<a id="unreal.PlayerController.get_input_touch_state"></a>

#### get_input_touch_state

```python
def get_input_touch_state(
        finger_index: TouchIndex) -> Tuple[float, float, bool]
```

x.get_input_touch_state(finger_index) -> (location_x=float, location_y=float, is_currently_pressed=bool)
Retrieves the X and Y screen coordinates of the specified touch key. Returns false if the touch index is not down

Args:
    finger_index (TouchIndex): 

Returns:
    tuple: 

    location_x (float): 

    location_y (float): 

    is_currently_pressed (bool):

<a id="unreal.PlayerController.get_input_mouse_delta"></a>

#### get_input_mouse_delta

```python
def get_input_mouse_delta() -> Tuple[float, float]
```

x.get_input_mouse_delta() -> (delta_x=float, delta_y=float)
Retrieves how far the mouse moved this frame.

Returns:
    tuple: 

    delta_x (float): 

    delta_y (float):

<a id="unreal.PlayerController.get_input_motion_state"></a>

#### get_input_motion_state

```python
def get_input_motion_state() -> Tuple[Vector, Vector, Vector, Vector]
```

x.get_input_motion_state() -> (tilt=Vector, rotation_rate=Vector, gravity=Vector, acceleration=Vector)
Retrieves the current motion state of the player's input device

Returns:
    tuple: 

    tilt (Vector): 

    rotation_rate (Vector): 

    gravity (Vector): 

    acceleration (Vector):

<a id="unreal.PlayerController.get_input_key_time_down"></a>

#### get_input_key_time_down

```python
def get_input_key_time_down(key: Key) -> float
```

x.get_input_key_time_down(key) -> float
Returns how long the given key/button has been down.  Returns 0 if it's up or it just went down this frame.

Args:
    key (Key): 

Returns:
    float:

<a id="unreal.PlayerController.get_input_analog_stick_state"></a>

#### get_input_analog_stick_state

```python
def get_input_analog_stick_state(
        which_stick: ControllerAnalogStick) -> Tuple[float, float]
```

x.get_input_analog_stick_state(which_stick) -> (stick_x=float, stick_y=float)
Retrieves the X and Y displacement of the given analog stick.

Args:
    which_stick (ControllerAnalogStick): 

Returns:
    tuple: 

    stick_x (float): 

    stick_y (float):

<a id="unreal.PlayerController.get_input_analog_key_state"></a>

#### get_input_analog_key_state

```python
def get_input_analog_key_state(key: Key) -> float
```

x.get_input_analog_key_state(key) -> float
Returns the analog value for the given key/button.  If analog isn't supported, returns 1 for down and 0 for up.

Args:
    key (Key): 

Returns:
    float:

<a id="unreal.PlayerController.get_hud"></a>

#### get_hud

```python
def get_hud() -> HUD
```

x.get_hud() -> HUD
Gets the HUD currently being used by this player controller

Returns:
    HUD:

<a id="unreal.PlayerController.get_hit_result_under_finger_for_objects"></a>

#### get_hit_result_under_finger_for_objects

```python
def get_hit_result_under_finger_for_objects(
        finger_index: TouchIndex,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool = True) -> Optional[HitResult]
```

x.get_hit_result_under_finger_for_objects(finger_index, object_types, trace_complex=True) -> HitResult or None
Performs a collision query under the finger, looking for object types

Args:
    finger_index (TouchIndex): 
    object_types (Array[ObjectTypeQuery]): 
    trace_complex (bool): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.PlayerController.get_hit_result_under_finger_by_channel"></a>

#### get_hit_result_under_finger_by_channel

```python
def get_hit_result_under_finger_by_channel(
        finger_index: TouchIndex,
        trace_channel: TraceTypeQuery,
        trace_complex: bool = True) -> Optional[HitResult]
```

x.get_hit_result_under_finger_by_channel(finger_index, trace_channel, trace_complex=True) -> HitResult or None
Performs a collision query under the finger, looking on a trace channel

Args:
    finger_index (TouchIndex): 
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.PlayerController.get_hit_result_under_finger"></a>

#### get_hit_result_under_finger

```python
def get_hit_result_under_finger(
        finger_index: TouchIndex,
        trace_channel: CollisionChannel = CollisionChannel.ECC_VISIBILITY,
        trace_complex: bool = True) -> Optional[HitResult]
```

x.get_hit_result_under_finger(finger_index, trace_channel=CollisionChannel.ECC_VISIBILITY, trace_complex=True) -> HitResult or None
Get Hit Result Under Finger
deprecated: Use new GetHitResultUnderFingerByChannel or GetHitResultUnderFingerForObject

Args:
    finger_index (TouchIndex): 
    trace_channel (CollisionChannel): 
    trace_complex (bool): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.PlayerController.get_hit_result_under_cursor_for_objects"></a>

#### get_hit_result_under_cursor_for_objects

```python
def get_hit_result_under_cursor_for_objects(
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool = True) -> Optional[HitResult]
```

x.get_hit_result_under_cursor_for_objects(object_types, trace_complex=True) -> HitResult or None
Performs a collision query under the mouse cursor, looking for object types

Args:
    object_types (Array[ObjectTypeQuery]): 
    trace_complex (bool): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.PlayerController.get_hit_result_under_cursor_by_channel"></a>

#### get_hit_result_under_cursor_by_channel

```python
def get_hit_result_under_cursor_by_channel(
        trace_channel: TraceTypeQuery,
        trace_complex: bool = True) -> Optional[HitResult]
```

x.get_hit_result_under_cursor_by_channel(trace_channel, trace_complex=True) -> HitResult or None
Performs a collision query under the mouse cursor, looking on a trace channel

Args:
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.PlayerController.get_hit_result_under_cursor"></a>

#### get_hit_result_under_cursor

```python
def get_hit_result_under_cursor(
        trace_channel: CollisionChannel = CollisionChannel.ECC_VISIBILITY,
        trace_complex: bool = True) -> Optional[HitResult]
```

x.get_hit_result_under_cursor(trace_channel=CollisionChannel.ECC_VISIBILITY, trace_complex=True) -> HitResult or None
Get Hit Result Under Cursor
deprecated: Use new GetHitResultUnderCursorByChannel or GetHitResultUnderCursorForObject

Args:
    trace_channel (CollisionChannel): 
    trace_complex (bool): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.PlayerController.get_focal_location"></a>

#### get_focal_location

```python
def get_focal_location() -> Vector
```

x.get_focal_location() -> Vector
Returns the location the PlayerController is focused on.
 If there is a possessed Pawn, returns the Pawn's location.
 If there is a spectator Pawn, returns that Pawn's location.
 Otherwise, returns the PlayerController's spawn location (usually the last known Pawn location after it has died).

Returns:
    Vector:

<a id="unreal.PlayerController.get_deprecated_input_yaw_scale"></a>

#### get_deprecated_input_yaw_scale

```python
def get_deprecated_input_yaw_scale() -> float
```

x.get_deprecated_input_yaw_scale() -> float
Get Deprecated Input Yaw Scale

Returns:
    float:

<a id="unreal.PlayerController.get_deprecated_input_roll_scale"></a>

#### get_deprecated_input_roll_scale

```python
def get_deprecated_input_roll_scale() -> float
```

x.get_deprecated_input_roll_scale() -> float
Get Deprecated Input Roll Scale

Returns:
    float:

<a id="unreal.PlayerController.get_deprecated_input_pitch_scale"></a>

#### get_deprecated_input_pitch_scale

```python
def get_deprecated_input_pitch_scale() -> float
```

x.get_deprecated_input_pitch_scale() -> float
Get Deprecated Input Pitch Scale

Returns:
    float:

<a id="unreal.PlayerController.deproject_screen_position_to_world"></a>

#### deproject_screen_position_to_world

```python
def deproject_screen_position_to_world(
        screen_x: float, screen_y: float) -> Optional[Tuple[Vector, Vector]]
```

x.deproject_screen_position_to_world(screen_x, screen_y) -> (world_location=Vector, world_direction=Vector) or None
Convert 2D screen position to World Space 3D position and direction. Returns false if unable to determine value. *

Args:
    screen_x (float): 
    screen_y (float): 

Returns:
    tuple or None: 

    world_location (Vector): 

    world_direction (Vector):

<a id="unreal.PlayerController.deproject_mouse_position_to_world"></a>

#### deproject_mouse_position_to_world

```python
def deproject_mouse_position_to_world() -> Optional[Tuple[Vector, Vector]]
```

x.deproject_mouse_position_to_world() -> (world_location=Vector, world_direction=Vector) or None
Convert current mouse 2D position to World Space 3D position and direction. Returns false if unable to determine value. *

Returns:
    tuple or None: 

    world_location (Vector): 

    world_direction (Vector):

<a id="unreal.PlayerController.client_stop_force_feedback"></a>

#### client_stop_force_feedback

```python
def client_stop_force_feedback(force_feedback_effect: ForceFeedbackEffect,
                               tag: Name) -> None
```

x.client_stop_force_feedback(force_feedback_effect, tag) -> None
Stops a playing force feedback pattern

Args:
    force_feedback_effect (ForceFeedbackEffect): If set only patterns from that effect will be stopped
    tag (Name): If not none only the pattern with this tag will be stopped

<a id="unreal.PlayerController.client_stop_camera_shakes_from_source"></a>

#### client_stop_camera_shakes_from_source

```python
def client_stop_camera_shakes_from_source(
        source_component: CameraShakeSourceComponent,
        immediately: bool = True) -> None
```

x.client_stop_camera_shakes_from_source(source_component, immediately=True) -> None
Stop camera shake on client.

Args:
    source_component (CameraShakeSourceComponent): 
    immediately (bool):

<a id="unreal.PlayerController.client_stop_camera_shake"></a>

#### client_stop_camera_shake

```python
def client_stop_camera_shake(shake: Class, immediately: bool = True) -> None
```

x.client_stop_camera_shake(shake, immediately=True) -> None
Stop camera shake on client.

Args:
    shake (type(Class)): 
    immediately (bool):

<a id="unreal.PlayerController.client_start_camera_shake_from_source"></a>

#### client_start_camera_shake_from_source

```python
def client_start_camera_shake_from_source(
        shake: Class, source_component: CameraShakeSourceComponent) -> None
```

x.client_start_camera_shake_from_source(shake, source_component) -> None
Play Camera Shake localized to a given source

Args:
    shake (type(Class)): Camera shake animation to play
    source_component (CameraShakeSourceComponent): The source from which the camera shakes originates

<a id="unreal.PlayerController.client_play_camera_shake_from_source"></a>

#### client_play_camera_shake_from_source

```python
def client_play_camera_shake_from_source(
        shake: Class, source_component: CameraShakeSourceComponent) -> None
```

deprecated: 'client_play_camera_shake_from_source' was renamed to 'client_start_camera_shake_from_source'.

<a id="unreal.PlayerController.client_start_camera_shake"></a>

#### client_start_camera_shake

```python
def client_start_camera_shake(
        shake: Class,
        scale: float = 1.000000,
        play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
        user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

x.client_start_camera_shake(shake, scale=1.000000, play_space=CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot=[0.000000, 0.000000, 0.000000]) -> None
Play Camera Shake

Args:
    shake (type(Class)): Camera shake animation to play
    scale (float): Scalar defining how "intense" to play the anim
    play_space (CameraShakePlaySpace): Which coordinate system to play the shake in (used for CameraAnims within the shake).
    user_play_space_rot (Rotator): Matrix used when PlaySpace = CAPS_UserDefined

<a id="unreal.PlayerController.client_play_camera_shake"></a>

#### client_play_camera_shake

```python
def client_play_camera_shake(
        shake: Class,
        scale: float = 1.000000,
        play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
        user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

deprecated: 'client_play_camera_shake' was renamed to 'client_start_camera_shake'.

<a id="unreal.PlayerController.client_spawn_generic_camera_lens_effect"></a>

#### client_spawn_generic_camera_lens_effect

```python
def client_spawn_generic_camera_lens_effect(
        lens_effect_emitter_class: Class) -> None
```

x.client_spawn_generic_camera_lens_effect(lens_effect_emitter_class) -> None
Spawn a camera lens effect (e.g. blood).

Args:
    lens_effect_emitter_class (type(Class)):

<a id="unreal.PlayerController.client_set_hud"></a>

#### client_set_hud

```python
def client_set_hud(new_hud_class: Class) -> None
```

x.client_set_hud(new_hud_class) -> None
Set the client's class of HUD and spawns a new instance of it. If there was already a HUD active, it is destroyed.

Args:
    new_hud_class (type(Class)):

<a id="unreal.PlayerController.client_clear_camera_lens_effects"></a>

#### client_clear_camera_lens_effects

```python
def client_clear_camera_lens_effects() -> None
```

x.client_clear_camera_lens_effects() -> None
Removes all Camera Lens Effects.

<a id="unreal.PlayerController.clear_audio_listener_override"></a>

#### clear_audio_listener_override

```python
def clear_audio_listener_override() -> None
```

x.clear_audio_listener_override() -> None
Clear any overrides that have been applied to audio listener

<a id="unreal.PlayerController.clear_audio_listener_attenuation_override"></a>

#### clear_audio_listener_attenuation_override

```python
def clear_audio_listener_attenuation_override() -> None
```

x.clear_audio_listener_attenuation_override() -> None
Clear Audio Listener Attenuation Override

<a id="unreal.PlayerController.can_restart_player"></a>

#### can_restart_player

```python
def can_restart_player() -> bool
```

x.can_restart_player() -> bool
Returns true if this controller thinks it's able to restart. Called from GameModeBase::PlayerCanRestart

Returns:
    bool:

<a id="unreal.PlayerController.add_yaw_input"></a>

#### add_yaw_input

```python
def add_yaw_input(val: float) -> None
```

x.add_yaw_input(val) -> None
Add Yaw (turn) input. This value is multiplied by InputYawScale.

Args:
    val (float): Amount to add to Yaw. This value is multiplied by InputYawScale.

<a id="unreal.PlayerController.add_turn_input"></a>

#### add_turn_input

```python
def add_turn_input(val: float) -> None
```

deprecated: 'add_turn_input' was renamed to 'add_yaw_input'.

<a id="unreal.PlayerController.add_roll_input"></a>

#### add_roll_input

```python
def add_roll_input(val: float) -> None
```

x.add_roll_input(val) -> None
Add Roll input. This value is multiplied by InputRollScale.

Args:
    val (float): Amount to add to Roll. This value is multiplied by InputRollScale.

<a id="unreal.PlayerController.add_pitch_input"></a>

#### add_pitch_input

```python
def add_pitch_input(val: float) -> None
```

x.add_pitch_input(val) -> None
Add Pitch (look up) input. This value is multiplied by InputPitchScale.

Args:
    val (float): Amount to add to Pitch. This value is multiplied by InputPitchScale.

<a id="unreal.PlayerController.add_look_up_input"></a>

#### add_look_up_input

```python
def add_look_up_input(val: float) -> None
```

deprecated: 'add_look_up_input' was renamed to 'add_pitch_input'.

<a id="unreal.PlayerController.activate_touch_interface"></a>

#### activate_touch_interface

```python
def activate_touch_interface(new_touch_interface: TouchInterface) -> None
```

x.activate_touch_interface(new_touch_interface) -> None
Activates a new touch interface for this player controller

Args:
    new_touch_interface (TouchInterface):

<a id="unreal.CheatManager"></a>