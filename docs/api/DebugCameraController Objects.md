## DebugCameraController Objects

```python
class DebugCameraController(PlayerController)
```

Camera controller that allows you to fly around a level mostly unrestricted by normal movement rules.

To turn it on, please press Alt+C or both (left and right) analogs on XBox pad,
or use the "ToggleDebugCamera" console command. Check the debug camera bindings
in DefaultPawn.cpp for the camera controls.

**C++ Source:**

- **Module**: Engine
- **File**: DebugCameraController.h

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
- ``initial_accel`` (float):  [Read-Write] Initial acceleration of the spectator pawn when we start possession.
- ``initial_decel`` (float):  [Read-Write] Initial deceleration of the spectator pawn when we start possession.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``initial_max_speed`` (float):  [Read-Write] Initial max speed of the spectator pawn when we start possession.
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
- ``speed_scale`` (float):  [Read-Write] Allows control over the speed of the spectator pawn. This scales the speed based on the InitialMaxSpeed. Use Set Pawn Movement Speed Scale during runtime
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

<a id="unreal.DebugCameraController.speed_scale"></a>

#### speed_scale

```python
@property
def speed_scale() -> float
```

(float):  [Read-Only] Allows control over the speed of the spectator pawn. This scales the speed based on the InitialMaxSpeed. Use Set Pawn Movement Speed Scale during runtime

<a id="unreal.DebugCameraController.initial_max_speed"></a>

#### initial_max_speed

```python
@property
def initial_max_speed() -> float
```

(float):  [Read-Only] Initial max speed of the spectator pawn when we start possession.

<a id="unreal.DebugCameraController.initial_accel"></a>

#### initial_accel

```python
@property
def initial_accel() -> float
```

(float):  [Read-Only] Initial acceleration of the spectator pawn when we start possession.

<a id="unreal.DebugCameraController.initial_decel"></a>

#### initial_decel

```python
@property
def initial_decel() -> float
```

(float):  [Read-Only] Initial deceleration of the spectator pawn when we start possession.

<a id="unreal.DebugCameraController.toggle_display"></a>

#### toggle_display

```python
def toggle_display() -> None
```

x.toggle_display() -> None
Toggles the display of debug info and input commands for the Debug Camera.

<a id="unreal.DebugCameraController.set_pawn_movement_speed_scale"></a>

#### set_pawn_movement_speed_scale

```python
def set_pawn_movement_speed_scale(new_speed_scale: float) -> None
```

x.set_pawn_movement_speed_scale(new_speed_scale) -> None
Sets the pawn movement speed scale.

Args:
    new_speed_scale (float):

<a id="unreal.DebugCameraController.receive_on_deactivate"></a>

#### receive_on_deactivate

```python
def receive_on_deactivate(restored_pc: PlayerController) -> None
```

x.receive_on_deactivate(restored_pc) -> None
Function called on deactivation of debug camera controller.

Args:
    restored_pc (PlayerController): The Player Controller that the player input is being returned to.

<a id="unreal.DebugCameraController.receive_on_actor_selected"></a>

#### receive_on_actor_selected

```python
def receive_on_actor_selected(new_selected_actor: Actor,
                              select_hit_location: Vector,
                              select_hit_normal: Vector,
                              hit: HitResult) -> None
```

x.receive_on_actor_selected(new_selected_actor, select_hit_location, select_hit_normal, hit) -> None
Called when an actor has been selected with the primary key (e.g. left mouse button).

The selection trace starts from the center of the debug camera's view.

Args:
    new_selected_actor (Actor): 
    select_hit_location (Vector): The exact world-space location where the selection trace hit the New Selected Actor.
    select_hit_normal (Vector): The world-space surface normal of the New Selected Actor at the hit location.
    hit (HitResult):

<a id="unreal.DebugCameraController.receive_on_activate"></a>

#### receive_on_activate

```python
def receive_on_activate(original_pc: PlayerController) -> None
```

x.receive_on_activate(original_pc) -> None
Function called on activation of debug camera controller.

Args:
    original_pc (PlayerController): The active player controller before this debug camera controller was possessed by the player.

<a id="unreal.DebugCameraController.get_selected_actor"></a>

#### get_selected_actor

```python
def get_selected_actor() -> Actor
```

x.get_selected_actor() -> Actor
Returns the currently selected actor, or null if it is invalid or not set

Returns:
    Actor:

<a id="unreal.HUD"></a>