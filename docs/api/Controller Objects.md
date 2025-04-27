## Controller Objects

```python
class Controller(Actor)
```

Controllers are non-physical actors that can possess a Pawn to control
its actions.  PlayerControllers are used by human players to control pawns, while
AIControllers implement the artificial intelligence for the pawns they control.
Controllers take control of a pawn using their Possess() method, and relinquish
control of the pawn by calling UnPossess().

Controllers receive notifications for many of the events occurring for the Pawn they
are controlling.  This gives the controller the opportunity to implement the behavior
in response to this event, intercepting the event and superseding the Pawn's default
behavior.

ControlRotation (accessed via GetControlRotation()), determines the viewing/aiming
direction of the controlled Pawn and is affected by input such as from a mouse or gamepad.
see: https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Controller/

**C++ Source:**

- **Module**: Engine
- **File**: Controller.h

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
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
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
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
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

<a id="unreal.Controller.player_state"></a>

#### player_state

```python
@property
def player_state() -> PlayerState
```

(PlayerState):  [Read-Only] PlayerState containing replicated information about the player using this controller (only exists for players, not NPCs).

<a id="unreal.Controller.player_replication_info"></a>

#### player_replication_info

```python
@property
def player_replication_info() -> PlayerState
```

deprecated: 'player_replication_info' was renamed to 'player_state'.

<a id="unreal.Controller.on_instigated_any_damage"></a>

#### on_instigated_any_damage

```python
@property
def on_instigated_any_damage() -> InstigatedAnyDamageSignature
```

(InstigatedAnyDamageSignature):  [Read-Write] Called when the controller has instigated damage in any way

<a id="unreal.Controller.on_instigated_any_damage"></a>

#### on_instigated_any_damage

```python
@on_instigated_any_damage.setter
def on_instigated_any_damage(value: InstigatedAnyDamageSignature) -> None
```

<a id="unreal.Controller.on_possessed_pawn_changed"></a>

#### on_possessed_pawn_changed

```python
@property
def on_possessed_pawn_changed() -> OnPossessedPawnChanged
```

(OnPossessedPawnChanged):  [Read-Write] Called on both authorities and clients when the possessed pawn changes (either OldPawn or NewPawn might be nullptr)

<a id="unreal.Controller.on_possessed_pawn_changed"></a>

#### on_possessed_pawn_changed

```python
@on_possessed_pawn_changed.setter
def on_possessed_pawn_changed(value: OnPossessedPawnChanged) -> None
```

<a id="unreal.Controller.un_possess"></a>

#### un_possess

```python
def un_possess() -> None
```

x.un_possess() -> None
Called to unpossess our pawn for any reason that is not the pawn being destroyed (destruction handled by PawnDestroyed()).

<a id="unreal.Controller.stop_movement"></a>

#### stop_movement

```python
def stop_movement() -> None
```

x.stop_movement() -> None
Aborts the move the controller is currently performing

<a id="unreal.Controller.set_initial_location_and_rotation"></a>

#### set_initial_location_and_rotation

```python
def set_initial_location_and_rotation(new_location: Vector,
                                      new_rotation: Rotator) -> None
```

x.set_initial_location_and_rotation(new_location, new_rotation) -> None
Set the initial location and rotation of the controller, as well as the control rotation. Typically used when the controller is first created.

Args:
    new_location (Vector): 
    new_rotation (Rotator):

<a id="unreal.Controller.set_ignore_move_input"></a>

#### set_ignore_move_input

```python
def set_ignore_move_input(new_move_input: bool) -> None
```

x.set_ignore_move_input(new_move_input) -> None
Locks or unlocks movement input, consecutive calls stack up and require the same amount of calls to undo, or can all be undone using ResetIgnoreMoveInput.

Args:
    new_move_input (bool): If true, move input is ignored. If false, input is not ignored.

<a id="unreal.Controller.set_ignore_look_input"></a>

#### set_ignore_look_input

```python
def set_ignore_look_input(new_look_input: bool) -> None
```

x.set_ignore_look_input(new_look_input) -> None
Locks or unlocks look input, consecutive calls stack up and require the same amount of calls to undo, or can all be undone using ResetIgnoreLookInput.

Args:
    new_look_input (bool): If true, look input is ignored. If false, input is not ignored.

<a id="unreal.Controller.set_control_rotation"></a>

#### set_control_rotation

```python
def set_control_rotation(new_rotation: Rotator) -> None
```

x.set_control_rotation(new_rotation) -> None
Set the control rotation.

Args:
    new_rotation (Rotator):

<a id="unreal.Controller.reset_ignore_move_input"></a>

#### reset_ignore_move_input

```python
def reset_ignore_move_input() -> None
```

x.reset_ignore_move_input() -> None
Stops ignoring move input by resetting the ignore move input state.

<a id="unreal.Controller.reset_ignore_look_input"></a>

#### reset_ignore_look_input

```python
def reset_ignore_look_input() -> None
```

x.reset_ignore_look_input() -> None
Stops ignoring look input by resetting the ignore look input state.

<a id="unreal.Controller.reset_ignore_input_flags"></a>

#### reset_ignore_input_flags

```python
def reset_ignore_input_flags() -> None
```

x.reset_ignore_input_flags() -> None
Reset move and look input ignore flags.

<a id="unreal.Controller.receive_un_possess"></a>

#### receive_un_possess

```python
def receive_un_possess(unpossessed_pawn: Pawn) -> None
```

x.receive_un_possess(unpossessed_pawn) -> None
Blueprint implementable event to react to the controller unpossessing a pawn

Args:
    unpossessed_pawn (Pawn):

<a id="unreal.Controller.on_un_possess"></a>

#### on_un_possess

```python
def on_un_possess(unpossessed_pawn: Pawn) -> None
```

deprecated: 'on_un_possess' was renamed to 'receive_un_possess'.

<a id="unreal.Controller.receive_possess"></a>

#### receive_possess

```python
def receive_possess(possessed_pawn: Pawn) -> None
```

x.receive_possess(possessed_pawn) -> None
Blueprint implementable event to react to the controller possessing a pawn

Args:
    possessed_pawn (Pawn):

<a id="unreal.Controller.on_possess"></a>

#### on_possess

```python
def on_possess(possessed_pawn: Pawn) -> None
```

deprecated: 'on_possess' was renamed to 'receive_possess'.

<a id="unreal.Controller.receive_instigated_any_damage"></a>

#### receive_instigated_any_damage

```python
def receive_instigated_any_damage(damage: float, damage_type: DamageType,
                                  damaged_actor: Actor,
                                  damage_causer: Actor) -> None
```

x.receive_instigated_any_damage(damage, damage_type, damaged_actor, damage_causer) -> None
Event when this controller instigates ANY damage

Args:
    damage (float): 
    damage_type (DamageType): 
    damaged_actor (Actor): 
    damage_causer (Actor):

<a id="unreal.Controller.possess"></a>

#### possess

```python
def possess(pawn: Pawn) -> None
```

x.possess(pawn) -> None
Handles attaching this controller to the specified pawn.
Only runs on the network authority (where HasAuthority() returns true).
Derived native classes can override OnPossess to filter the specified pawn.
When possessed pawn changed, blueprint class gets notified by ReceivePossess
and OnNewPawn delegate is broadcasted.
see: HasAuthority, OnPossess, ReceivePossess

Args:
    pawn (Pawn): The Pawn to be possessed.

<a id="unreal.Controller.line_of_sight_to"></a>

#### line_of_sight_to

```python
def line_of_sight_to(other: Actor,
                     view_point: Vector = [0.000000, 0.000000, 0.000000],
                     alternate_checks: bool = False) -> bool
```

x.line_of_sight_to(other, view_point=[0.000000, 0.000000, 0.000000], alternate_checks=False) -> bool
Checks line to center and top of other actor

Args:
    other (Actor): is the actor whose visibility is being checked.
    view_point (Vector): is eye position visibility is being checked from.  If vect(0,0,0) passed in, uses current viewtarget's eye position.
    alternate_checks (bool): used only in AIController implementation

Returns:
    bool: true if controller's pawn can see Other actor.

<a id="unreal.Controller.get_controlled_pawn"></a>

#### get_controlled_pawn

```python
def get_controlled_pawn() -> Pawn
```

x.get_controlled_pawn() -> Pawn
Return the Pawn that is currently 'controlled' by this PlayerController

Returns:
    Pawn:

<a id="unreal.Controller.is_player_controller"></a>

#### is_player_controller

```python
def is_player_controller() -> bool
```

x.is_player_controller() -> bool
Returns whether this Controller is a PlayerController.

Returns:
    bool:

<a id="unreal.Controller.is_move_input_ignored"></a>

#### is_move_input_ignored

```python
def is_move_input_ignored() -> bool
```

x.is_move_input_ignored() -> bool
Returns true if movement input is ignored.

Returns:
    bool:

<a id="unreal.Controller.is_look_input_ignored"></a>

#### is_look_input_ignored

```python
def is_look_input_ignored() -> bool
```

x.is_look_input_ignored() -> bool
Returns true if look input is ignored.

Returns:
    bool:

<a id="unreal.Controller.is_local_player_controller"></a>

#### is_local_player_controller

```python
def is_local_player_controller() -> bool
```

x.is_local_player_controller() -> bool
Returns whether this Controller is a locally controlled PlayerController.

Returns:
    bool:

<a id="unreal.Controller.is_local_controller"></a>

#### is_local_controller

```python
def is_local_controller() -> bool
```

x.is_local_controller() -> bool
Returns whether this Controller is a local controller.

Returns:
    bool:

<a id="unreal.Controller.get_view_target"></a>

#### get_view_target

```python
def get_view_target() -> Actor
```

x.get_view_target() -> Actor
Get the actor the controller is looking at

Returns:
    Actor:

<a id="unreal.Controller.get_player_view_point"></a>

#### get_player_view_point

```python
def get_player_view_point() -> Tuple[Vector, Rotator]
```

x.get_player_view_point() -> (location=Vector, rotation=Rotator)
Returns Player's Point of View
For the AI this means the Pawn's 'Eyes' ViewPoint
For a Human player, this means the Camera's ViewPoint
output: out_Location, view location of player
output: out_rotation, view rotation of player

Returns:
    tuple: 

    location (Vector): 

    rotation (Rotator):

<a id="unreal.Controller.get_desired_rotation"></a>

#### get_desired_rotation

```python
def get_desired_rotation() -> Rotator
```

x.get_desired_rotation() -> Rotator
Get the desired pawn target rotation

Returns:
    Rotator:

<a id="unreal.Controller.get_control_rotation"></a>

#### get_control_rotation

```python
def get_control_rotation() -> Rotator
```

x.get_control_rotation() -> Rotator
Get the control rotation. This is the full aim rotation, which may be different than a camera orientation (for example in a third person view),
and may differ from the rotation of the controlled Pawn (which may choose not to visually pitch or roll, for example).

Returns:
    Rotator:

<a id="unreal.AIController"></a>