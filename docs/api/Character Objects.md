## Character Objects

```python
class Character(Pawn)
```

Characters are Pawns that have a mesh, collision, and built-in movement logic.
They are responsible for all physical interaction between the player or AI and the world, and also implement basic networking and input models.
They are designed for a vertically-oriented player representation that can walk, jump, fly, and swim through the world using CharacterMovementComponent.
see: APawn, UCharacterMovementComponent
see: https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Pawn/Character/

**C++ Source:**

- **Module**: Engine
- **File**: Character.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``ai_controller_class`` (type(Class)):  [Read-Write] Default class to use when pawn is controlled by AI.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_possess_ai`` (AutoPossessAI):  [Read-Write] Determines when the Pawn creates and is possessed by an AI Controller (on level start, when spawned, etc).
  Only possible if AIControllerClassRef is set, and ignored if AutoPossessPlayer is enabled.
  see: AutoPossessPlayer
- ``auto_possess_player`` (AutoReceiveInput):  [Read-Write] Determines which PlayerController, if any, should automatically possess the pawn when the level starts or when the pawn is spawned.
  see: AutoPossessAI
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``base_eye_height`` (float):  [Read-Write] Base eye height above collision center.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_affect_navigation_generation`` (bool):  [Read-Write] If set to false (default) given pawn instance will never affect navigation generation (but components could).
  Setting it to true will result in using regular AActor's navigation relevancy
  calculation to check if this pawn instance should affect navigation generation.
  note: Use SetCanAffectNavigationGeneration() to change this value at runtime.
  note: Modifying this value at runtime will result in any navigation change only if runtime navigation generation is enabled.
  note: Override UpdateNavigationRelevance() to propagate the flag to the desired components.
  see: SetCanAffectNavigationGeneration(), UpdateNavigationRelevance()
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``capsule_component`` (CapsuleComponent):  [Read-Only] The CapsuleComponent being used for movement collision (by CharacterMovement). Always treated as being vertically aligned in simple collision check functions.
- ``character_movement`` (CharacterMovementComponent):  [Read-Only] Movement component used for movement logic in various movement modes (walking, falling, etc), containing relevant settings and functions to control movement.
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``crouched_eye_height`` (float):  [Read-Write] Default crouched eye height
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
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
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_crouched`` (bool):  [Read-Write] Set by character movement to specify that this Character is currently crouched.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``jump_current_count`` (int32):  [Read-Only] Tracks the current number of jumps performed.
  This is incremented in CheckJumpInput, used in CanJump_Implementation, and reset in OnMovementModeChanged.
  When providing overrides for these methods, it's recommended to either manually
  increment / reset this value, or call the Super:: method.
- ``jump_current_count_pre_jump`` (int32):  [Read-Only] Represents the current number of jumps performed before CheckJumpInput modifies JumpCurrentCount.
  This is set in CheckJumpInput and is used in SetMoveFor and PrepMoveFor instead of JumpCurrentCount
  since CheckJumpInput can modify JumpCurrentCount.
  When providing overrides for these methods, it's recommended to either manually
  set this value, or call the Super:: method.
- ``jump_force_time_remaining`` (float):  [Read-Only] Amount of jump force time remaining, if JumpMaxHoldTime > 0.
- ``jump_key_hold_time`` (float):  [Read-Only] Jump key Held Time.
  This is the time that the player has held the jump key, in seconds.
- ``jump_max_count`` (int32):  [Read-Write] The max number of jumps the character can perform.
  Note that if JumpMaxHoldTime is non zero and StopJumping is not called, the player
  may be able to perform and unlimited number of jumps. Therefore it is usually
  best to call StopJumping() when jump input has ceased (such as a button up event).
- ``jump_max_hold_time`` (float):  [Read-Write] The max time the jump key can be held.
  Note that if StopJumping() is not called before the max jump hold time is reached,
  then the character will carry on receiving vertical velocity. Therefore it is usually
  best to call StopJumping() when jump input has ceased (such as a button up event).
- ``landed_delegate`` (LandedSignature):  [Read-Write] Called upon landing when falling, to perform actions based on the Hit result.
  Note that movement mode is still "Falling" during this event. Current Velocity value is the velocity at the time of landing.
  Consider OnMovementModeChanged() as well, as that can be used once the movement mode changes to the new mode (most likely Walking).
  see: OnMovementModeChanged()
- ``last_hit_by`` (Controller):  [Read-Write] Controller of the last Actor that caused us damage.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``mesh`` (SkeletalMeshComponent):  [Read-Only] The main skeletal mesh associated with this Character (optional sub-object).
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``movement_mode_changed_delegate`` (MovementModeChangedSignature):  [Read-Write] Multicast delegate for MovementMode changing.
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
- ``on_character_movement_updated`` (CharacterMovementUpdatedSignature):  [Read-Write] Event triggered at the end of a CharacterMovementComponent movement update.
  This is the preferred event to use rather than the Tick event when performing custom updates to CharacterMovement properties based on the current state.
  This is mainly due to the nature of network updates, where client corrections in position from the server can cause multiple iterations of a movement update,
  which allows this event to update as well, while a Tick event would not.
- ``on_clicked`` (ActorOnClickedSignature):  [Read-Write] Called when the left mouse button is clicked while the mouse is over this actor and click events are enabled in the player controller.
- ``on_destroyed`` (ActorDestroyedSignature):  [Read-Write] Event triggered when the actor has been explicitly destroyed.
- ``on_end_cursor_over`` (ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.
- ``on_end_play`` (ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.
- ``on_input_touch_begin`` (ActorOnInputTouchBeginSignature):  [Read-Write] Called when a touch input is received over this actor when touch events are enabled in the player controller.
- ``on_input_touch_end`` (ActorOnInputTouchEndSignature):  [Read-Write] Called when a touch input is received over this component when touch events are enabled in the player controller.
- ``on_input_touch_enter`` (ActorBeginTouchOverSignature):  [Read-Write] Called when a finger is moved over this actor when touch over events are enabled in the player controller.
- ``on_input_touch_leave`` (ActorEndTouchOverSignature):  [Read-Write] Called when a finger is moved off this actor when touch over events are enabled in the player controller.
- ``on_reached_jump_apex`` (CharacterReachedApexSignature):  [Read-Write] Broadcast when Character's jump reaches its apex. Needs CharacterMovement->bNotifyApex = true
- ``on_released`` (ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``override_input_component_class`` (type(Class)):  [Read-Write] If set, then this InputComponent class will be used instead of the Input Settings' DefaultInputComponentClass
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``player_state`` (PlayerState):  [Read-Write] If Pawn is possessed by a player, points to its Player State.  Needed for network play as controllers are not replicated to clients.
- ``pressed_jump`` (bool):  [Read-Write] When true, player wants to jump
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``proxy_jump_force_started_time`` (float):  [Read-Only] Track last time a jump force started for a proxy.
- ``receive_controller_changed_delegate`` (PawnControllerChangedSignature):  [Read-Write] Event called after a pawn's controller has changed, on the server and owning client. This will happen at the same time as the delegate on GameInstance
- ``receive_restarted_delegate`` (PawnRestartedSignature):  [Read-Write] Event called after a pawn has been restarted, usually by a possession change. This is called on the server for all pawns and the owning client for player pawns
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
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
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
- ``use_controller_rotation_pitch`` (bool):  [Read-Write] If true, this Pawn's pitch will be updated to match the Controller's ControlRotation pitch, if controlled by a PlayerController.
- ``use_controller_rotation_roll`` (bool):  [Read-Write] If true, this Pawn's roll will be updated to match the Controller's ControlRotation roll, if controlled by a PlayerController.
- ``use_controller_rotation_yaw`` (bool):  [Read-Write] If true, this Pawn's yaw will be updated to match the Controller's ControlRotation yaw, if controlled by a PlayerController.
- ``was_jumping`` (bool):  [Read-Only] Tracks whether or not the character was already jumping last frame.

<a id="unreal.Character.mesh"></a>

#### mesh

```python
@property
def mesh() -> SkeletalMeshComponent
```

(SkeletalMeshComponent):  [Read-Only] The main skeletal mesh associated with this Character (optional sub-object).

<a id="unreal.Character.character_movement"></a>

#### character_movement

```python
@property
def character_movement() -> CharacterMovementComponent
```

(CharacterMovementComponent):  [Read-Only] Movement component used for movement logic in various movement modes (walking, falling, etc), containing relevant settings and functions to control movement.

<a id="unreal.Character.capsule_component"></a>

#### capsule_component

```python
@property
def capsule_component() -> CapsuleComponent
```

(CapsuleComponent):  [Read-Only] The CapsuleComponent being used for movement collision (by CharacterMovement). Always treated as being vertically aligned in simple collision check functions.

<a id="unreal.Character.crouched_eye_height"></a>

#### crouched_eye_height

```python
@property
def crouched_eye_height() -> float
```

(float):  [Read-Write] Default crouched eye height

<a id="unreal.Character.crouched_eye_height"></a>

#### crouched_eye_height

```python
@crouched_eye_height.setter
def crouched_eye_height(value: float) -> None
```

<a id="unreal.Character.is_crouched"></a>

#### is_crouched

```python
@property
def is_crouched() -> bool
```

(bool):  [Read-Only] Set by character movement to specify that this Character is currently crouched.

<a id="unreal.Character.pressed_jump"></a>

#### pressed_jump

```python
@property
def pressed_jump() -> bool
```

(bool):  [Read-Only] When true, player wants to jump

<a id="unreal.Character.was_jumping"></a>

#### was_jumping

```python
@property
def was_jumping() -> bool
```

(bool):  [Read-Only] Tracks whether or not the character was already jumping last frame.

<a id="unreal.Character.jump_key_hold_time"></a>

#### jump_key_hold_time

```python
@property
def jump_key_hold_time() -> float
```

(float):  [Read-Only] Jump key Held Time.
This is the time that the player has held the jump key, in seconds.

<a id="unreal.Character.jump_force_time_remaining"></a>

#### jump_force_time_remaining

```python
@property
def jump_force_time_remaining() -> float
```

(float):  [Read-Only] Amount of jump force time remaining, if JumpMaxHoldTime > 0.

<a id="unreal.Character.proxy_jump_force_started_time"></a>

#### proxy_jump_force_started_time

```python
@property
def proxy_jump_force_started_time() -> float
```

(float):  [Read-Only] Track last time a jump force started for a proxy.

<a id="unreal.Character.jump_max_hold_time"></a>

#### jump_max_hold_time

```python
@property
def jump_max_hold_time() -> float
```

(float):  [Read-Write] The max time the jump key can be held.
Note that if StopJumping() is not called before the max jump hold time is reached,
then the character will carry on receiving vertical velocity. Therefore it is usually
best to call StopJumping() when jump input has ceased (such as a button up event).

<a id="unreal.Character.jump_max_hold_time"></a>

#### jump_max_hold_time

```python
@jump_max_hold_time.setter
def jump_max_hold_time(value: float) -> None
```

<a id="unreal.Character.jump_max_count"></a>

#### jump_max_count

```python
@property
def jump_max_count() -> int
```

(int32):  [Read-Write] The max number of jumps the character can perform.
Note that if JumpMaxHoldTime is non zero and StopJumping is not called, the player
may be able to perform and unlimited number of jumps. Therefore it is usually
best to call StopJumping() when jump input has ceased (such as a button up event).

<a id="unreal.Character.jump_max_count"></a>

#### jump_max_count

```python
@jump_max_count.setter
def jump_max_count(value: int) -> None
```

<a id="unreal.Character.jump_current_count"></a>

#### jump_current_count

```python
@property
def jump_current_count() -> int
```

(int32):  [Read-Only] Tracks the current number of jumps performed.
This is incremented in CheckJumpInput, used in CanJump_Implementation, and reset in OnMovementModeChanged.
When providing overrides for these methods, it's recommended to either manually
increment / reset this value, or call the Super:: method.

<a id="unreal.Character.jump_current_count_pre_jump"></a>

#### jump_current_count_pre_jump

```python
@property
def jump_current_count_pre_jump() -> int
```

(int32):  [Read-Only] Represents the current number of jumps performed before CheckJumpInput modifies JumpCurrentCount.
This is set in CheckJumpInput and is used in SetMoveFor and PrepMoveFor instead of JumpCurrentCount
since CheckJumpInput can modify JumpCurrentCount.
When providing overrides for these methods, it's recommended to either manually
set this value, or call the Super:: method.

<a id="unreal.Character.on_reached_jump_apex"></a>

#### on_reached_jump_apex

```python
@property
def on_reached_jump_apex() -> CharacterReachedApexSignature
```

(CharacterReachedApexSignature):  [Read-Write] Broadcast when Character's jump reaches its apex. Needs CharacterMovement->bNotifyApex = true

<a id="unreal.Character.on_reached_jump_apex"></a>

#### on_reached_jump_apex

```python
@on_reached_jump_apex.setter
def on_reached_jump_apex(value: CharacterReachedApexSignature) -> None
```

<a id="unreal.Character.landed_delegate"></a>

#### landed_delegate

```python
@property
def landed_delegate() -> LandedSignature
```

(LandedSignature):  [Read-Write] Called upon landing when falling, to perform actions based on the Hit result.
Note that movement mode is still "Falling" during this event. Current Velocity value is the velocity at the time of landing.
Consider OnMovementModeChanged() as well, as that can be used once the movement mode changes to the new mode (most likely Walking).
see: OnMovementModeChanged()

<a id="unreal.Character.landed_delegate"></a>

#### landed_delegate

```python
@landed_delegate.setter
def landed_delegate(value: LandedSignature) -> None
```

<a id="unreal.Character.movement_mode_changed_delegate"></a>

#### movement_mode_changed_delegate

```python
@property
def movement_mode_changed_delegate() -> MovementModeChangedSignature
```

(MovementModeChangedSignature):  [Read-Write] Multicast delegate for MovementMode changing.

<a id="unreal.Character.movement_mode_changed_delegate"></a>

#### movement_mode_changed_delegate

```python
@movement_mode_changed_delegate.setter
def movement_mode_changed_delegate(
        value: MovementModeChangedSignature) -> None
```

<a id="unreal.Character.on_character_movement_updated"></a>

#### on_character_movement_updated

```python
@property
def on_character_movement_updated() -> CharacterMovementUpdatedSignature
```

(CharacterMovementUpdatedSignature):  [Read-Write] Event triggered at the end of a CharacterMovementComponent movement update.
This is the preferred event to use rather than the Tick event when performing custom updates to CharacterMovement properties based on the current state.
This is mainly due to the nature of network updates, where client corrections in position from the server can cause multiple iterations of a movement update,
which allows this event to update as well, while a Tick event would not.

<a id="unreal.Character.on_character_movement_updated"></a>

#### on_character_movement_updated

```python
@on_character_movement_updated.setter
def on_character_movement_updated(
        value: CharacterMovementUpdatedSignature) -> None
```

<a id="unreal.Character.un_crouch"></a>

#### un_crouch

```python
def un_crouch(client_simulation: bool = False) -> None
```

x.un_crouch(client_simulation=False) -> None
Request the character to stop crouching. The request is processed on the next update of the CharacterMovementComponent.
see: OnEndCrouch
see: IsCrouched
see: CharacterMovement->WantsToCrouch

Args:
    client_simulation (bool):

<a id="unreal.Character.stop_jumping"></a>

#### stop_jumping

```python
def stop_jumping() -> None
```

x.stop_jumping() -> None
Stop the character from jumping on the next update.
Call this from an input event (such as a button 'up' event) to cease applying
jump Z-velocity. If this is not called, then jump z-velocity will be applied
until JumpMaxHoldTime is reached.

<a id="unreal.Character.stop_anim_montage"></a>

#### stop_anim_montage

```python
def stop_anim_montage(anim_montage: AnimMontage = None) -> None
```

x.stop_anim_montage(anim_montage=None) -> None
Stop Animation Montage. If nullptr, it will stop what's currently active. The Blend Out Time is taken from the montage asset that is being stopped. *

Args:
    anim_montage (AnimMontage):

<a id="unreal.Character.play_anim_montage"></a>

#### play_anim_montage

```python
def play_anim_montage(anim_montage: AnimMontage,
                      play_rate: float = 1.000000,
                      start_section_name: Name = "None") -> float
```

x.play_anim_montage(anim_montage, play_rate=1.000000, start_section_name="None") -> float
Play Animation Montage on the character mesh. Returns the length of the animation montage in seconds, or 0.f if failed to play. *

Args:
    anim_montage (AnimMontage): 
    play_rate (float): 
    start_section_name (Name): 

Returns:
    float:

<a id="unreal.Character.on_walking_off_ledge"></a>

#### on_walking_off_ledge

```python
def on_walking_off_ledge(previous_floor_impact_normal: Vector,
                         previous_floor_contact_normal: Vector,
                         previous_location: Vector, time_delta: float) -> None
```

x.on_walking_off_ledge(previous_floor_impact_normal, previous_floor_contact_normal, previous_location, time_delta) -> None
Event fired when the Character is walking off a surface and is about to fall because CharacterMovement->CurrentFloor became unwalkable.
If CharacterMovement->MovementMode does not change during this event then the character will automatically start falling afterwards.
note: Z velocity is zero during walking movement, and will be here as well. Another velocity can be computed here if desired and will be used when starting to fall.

Args:
    previous_floor_impact_normal (Vector): Normal of the previous walkable floor.
    previous_floor_contact_normal (Vector): Normal of the contact with the previous walkable floor.
    previous_location (Vector): Previous character location before movement off the ledge.
    time_delta (float):

<a id="unreal.Character.on_launched"></a>

#### on_launched

```python
def on_launched(launch_velocity: Vector, xy_override: bool,
                z_override: bool) -> None
```

x.on_launched(launch_velocity, xy_override, z_override) -> None
Let blueprint know that we were launched

Args:
    launch_velocity (Vector): 
    xy_override (bool): 
    z_override (bool):

<a id="unreal.Character.on_landed"></a>

#### on_landed

```python
def on_landed(hit: HitResult) -> None
```

x.on_landed(hit) -> None
Called upon landing when falling, to perform actions based on the Hit result.
Note that movement mode is still "Falling" during this event. Current Velocity value is the velocity at the time of landing.
Consider OnMovementModeChanged() as well, as that can be used once the movement mode changes to the new mode (most likely Walking).
see: OnMovementModeChanged()

Args:
    hit (HitResult): Result describing the landing that resulted in a valid landing spot.

<a id="unreal.Character.on_jumped"></a>

#### on_jumped

```python
def on_jumped() -> None
```

x.on_jumped() -> None
Event fired when the character has just started jumping

<a id="unreal.Character.launch_character"></a>

#### launch_character

```python
def launch_character(launch_velocity: Vector, xy_override: bool,
                     z_override: bool) -> None
```

x.launch_character(launch_velocity, xy_override, z_override) -> None
Set a pending launch velocity on the Character. This velocity will be processed on the next CharacterMovementComponent tick,
and will set it to the "falling" state. Triggers the OnLaunched event.

Args:
    launch_velocity (Vector): is the velocity to impart to the Character
    xy_override (bool): if true replace the XY part of the Character's velocity instead of adding to it.
    z_override (bool): if true replace the Z component of the Character's velocity instead of adding to it.

<a id="unreal.Character.launch"></a>

#### launch

```python
def launch(launch_velocity: Vector, xy_override: bool,
           z_override: bool) -> None
```

deprecated: 'launch' was renamed to 'launch_character'.

<a id="unreal.Character.update_custom_movement"></a>

#### update_custom_movement

```python
def update_custom_movement(delta_time: float) -> None
```

x.update_custom_movement(delta_time) -> None
Event for implementing custom character movement mode. Called by CharacterMovement if MovementMode is set to Custom.
note: C++ code should override UCharacterMovementComponent::PhysCustom() instead.
see: UCharacterMovementComponent::PhysCustom()

Args:
    delta_time (float):

<a id="unreal.Character.on_start_crouch"></a>

#### on_start_crouch

```python
def on_start_crouch(half_height_adjust: float,
                    scaled_half_height_adjust: float) -> None
```

x.on_start_crouch(half_height_adjust, scaled_half_height_adjust) -> None
Event when Character crouches.

Args:
    half_height_adjust (float): difference between default collision half-height, and actual crouched capsule half-height.
    scaled_half_height_adjust (float): difference after component scale is taken in to account.

<a id="unreal.Character.on_movement_mode_changed"></a>

#### on_movement_mode_changed

```python
def on_movement_mode_changed(prev_movement_mode: MovementMode,
                             new_movement_mode: MovementMode,
                             prev_custom_mode: int,
                             new_custom_mode: int) -> None
```

x.on_movement_mode_changed(prev_movement_mode, new_movement_mode, prev_custom_mode, new_custom_mode) -> None
Called from CharacterMovementComponent to notify the character that the movement mode has changed.

Args:
    prev_movement_mode (MovementMode): Movement mode before the change
    new_movement_mode (MovementMode): New movement mode
    prev_custom_mode (uint8): Custom mode before the change (applicable if PrevMovementMode is Custom)
    new_custom_mode (uint8): New custom mode (applicable if NewMovementMode is Custom)

<a id="unreal.Character.on_end_crouch"></a>

#### on_end_crouch

```python
def on_end_crouch(half_height_adjust: float,
                  scaled_half_height_adjust: float) -> None
```

x.on_end_crouch(half_height_adjust, scaled_half_height_adjust) -> None
Event when Character stops crouching.

Args:
    half_height_adjust (float): difference between default collision half-height, and actual crouched capsule half-height.
    scaled_half_height_adjust (float): difference after component scale is taken in to account.

<a id="unreal.Character.jump"></a>

#### jump

```python
def jump() -> None
```

x.jump() -> None
Make the character jump on the next update.
If you want your character to jump according to the time that the jump key is held,
then you can set JumpMaxHoldTime to some non-zero value. Make sure in this case to
call StopJumping() when you want the jump's z-velocity to stop being applied (such
as on a button up event), otherwise the character will carry on receiving the
velocity until JumpKeyHoldTime reaches JumpMaxHoldTime.

<a id="unreal.Character.is_playing_root_motion"></a>

#### is_playing_root_motion

```python
def is_playing_root_motion() -> bool
```

x.is_playing_root_motion() -> bool
True if we are playing Anim root motion right now

Returns:
    bool:

<a id="unreal.Character.is_playing_networked_root_motion_montage"></a>

#### is_playing_networked_root_motion_montage

```python
def is_playing_networked_root_motion_montage() -> bool
```

x.is_playing_networked_root_motion_montage() -> bool
True if we are playing Root Motion right now, through a Montage with RootMotionMode == ERootMotionMode::RootMotionFromMontagesOnly.
This means code path for networked root motion is enabled.

Returns:
    bool:

<a id="unreal.Character.is_jump_providing_force"></a>

#### is_jump_providing_force

```python
def is_jump_providing_force() -> bool
```

x.is_jump_providing_force() -> bool
True if jump is actively providing a force, such as when the jump key is held and the time it has been held is less than JumpMaxHoldTime.
see: CharacterMovement->IsFalling

Returns:
    bool:

<a id="unreal.Character.is_jumping"></a>

#### is_jumping

```python
def is_jumping() -> bool
```

deprecated: 'is_jumping' was renamed to 'is_jump_providing_force'.

<a id="unreal.Character.has_any_root_motion"></a>

#### has_any_root_motion

```python
def has_any_root_motion() -> bool
```

x.has_any_root_motion() -> bool
True if we are playing root motion from any source right now (anim root motion, root motion source)

Returns:
    bool:

<a id="unreal.Character.get_current_montage"></a>

#### get_current_montage

```python
def get_current_montage() -> AnimMontage
```

x.get_current_montage() -> AnimMontage
Return current playing Montage *

Returns:
    AnimMontage:

<a id="unreal.Character.get_base_translation_offset"></a>

#### get_base_translation_offset

```python
def get_base_translation_offset() -> Vector
```

x.get_base_translation_offset() -> Vector
Get the saved translation offset of mesh. This is how much extra offset is applied from the center of the capsule.

Returns:
    Vector:

<a id="unreal.Character.get_base_rotation_offset"></a>

#### get_base_rotation_offset

```python
def get_base_rotation_offset() -> Rotator
```

x.get_base_rotation_offset() -> Rotator
Get the saved rotation offset of mesh. This is how much extra rotation is applied from the capsule rotation.

Returns:
    Rotator:

<a id="unreal.Character.get_anim_root_motion_translation_scale"></a>

#### get_anim_root_motion_translation_scale

```python
def get_anim_root_motion_translation_scale() -> float
```

x.get_anim_root_motion_translation_scale() -> float
Returns current value of AnimRootMotionScale

Returns:
    float:

<a id="unreal.Character.crouch"></a>

#### crouch

```python
def crouch(client_simulation: bool = False) -> None
```

x.crouch(client_simulation=False) -> None
Request the character to start crouching. The request is processed on the next update of the CharacterMovementComponent.
see: OnStartCrouch
see: IsCrouched
see: CharacterMovement->WantsToCrouch

Args:
    client_simulation (bool):

<a id="unreal.Character.can_jump_internal"></a>

#### can_jump_internal

```python
def can_jump_internal() -> bool
```

x.can_jump_internal() -> bool
Customizable event to check if the character can jump in the current state.
Default implementation returns true if the character is on the ground and not crouching,
has a valid CharacterMovementComponent and CanEverJump() returns true.
Default implementation also allows for 'hold to jump higher' functionality:
As well as returning true when on the ground, it also returns true when GetMaxJumpTime is more
than zero and IsJumping returns true.

Returns:
    bool: Whether the character can jump in the current state.

<a id="unreal.Character.can_jump"></a>

#### can_jump

```python
def can_jump() -> bool
```

x.can_jump() -> bool
Check if the character can jump in the current state.

The default implementation may be overridden or extended by implementing the custom CanJump event in Blueprints.

Returns:
    bool: Whether the character can jump in the current state.

<a id="unreal.Character.can_crouch"></a>

#### can_crouch

```python
def can_crouch() -> bool
```

x.can_crouch() -> bool


Returns:
    bool: true if this character is currently able to crouch (and is not currently crouched)

<a id="unreal.Character.cache_initial_mesh_offset"></a>

#### cache_initial_mesh_offset

```python
def cache_initial_mesh_offset(mesh_relative_location: Vector,
                              mesh_relative_rotation: Rotator) -> None
```

x.cache_initial_mesh_offset(mesh_relative_location, mesh_relative_rotation) -> None
Cache mesh offset from capsule. This is used as the target for network smoothing interpolation, when the mesh is offset with lagged smoothing.
This is automatically called during initialization; call this at runtime if you intend to change the default mesh offset from the capsule.
see: GetBaseTranslationOffset(), GetBaseRotationOffset()

Args:
    mesh_relative_location (Vector): 
    mesh_relative_rotation (Rotator):

<a id="unreal.EQSTestingPawn"></a>