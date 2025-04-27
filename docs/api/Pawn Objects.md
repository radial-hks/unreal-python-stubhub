## Pawn Objects

```python
class Pawn(Actor)
```

Pawn is the base class of all actors that can be possessed by players or AI.
They are the physical representations of players and creatures in a level.
see: https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Pawn/

**C++ Source:**

- **Module**: Engine
- **File**: Pawn.h

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
- ``last_hit_by`` (Controller):  [Read-Write] Controller of the last Actor that caused us damage.
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
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
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

<a id="unreal.Pawn.use_controller_rotation_pitch"></a>

#### use_controller_rotation_pitch

```python
@property
def use_controller_rotation_pitch() -> bool
```

(bool):  [Read-Write] If true, this Pawn's pitch will be updated to match the Controller's ControlRotation pitch, if controlled by a PlayerController.

<a id="unreal.Pawn.use_controller_rotation_pitch"></a>

#### use_controller_rotation_pitch

```python
@use_controller_rotation_pitch.setter
def use_controller_rotation_pitch(value: bool) -> None
```

<a id="unreal.Pawn.use_controller_rotation_yaw"></a>

#### use_controller_rotation_yaw

```python
@property
def use_controller_rotation_yaw() -> bool
```

(bool):  [Read-Write] If true, this Pawn's yaw will be updated to match the Controller's ControlRotation yaw, if controlled by a PlayerController.

<a id="unreal.Pawn.use_controller_rotation_yaw"></a>

#### use_controller_rotation_yaw

```python
@use_controller_rotation_yaw.setter
def use_controller_rotation_yaw(value: bool) -> None
```

<a id="unreal.Pawn.use_controller_rotation_roll"></a>

#### use_controller_rotation_roll

```python
@property
def use_controller_rotation_roll() -> bool
```

(bool):  [Read-Write] If true, this Pawn's roll will be updated to match the Controller's ControlRotation roll, if controlled by a PlayerController.

<a id="unreal.Pawn.use_controller_rotation_roll"></a>

#### use_controller_rotation_roll

```python
@use_controller_rotation_roll.setter
def use_controller_rotation_roll(value: bool) -> None
```

<a id="unreal.Pawn.can_affect_navigation_generation"></a>

#### can_affect_navigation_generation

```python
@property
def can_affect_navigation_generation() -> bool
```

(bool):  [Read-Only] If set to false (default) given pawn instance will never affect navigation generation (but components could).
Setting it to true will result in using regular AActor's navigation relevancy
calculation to check if this pawn instance should affect navigation generation.
note: Use SetCanAffectNavigationGeneration() to change this value at runtime.
note: Modifying this value at runtime will result in any navigation change only if runtime navigation generation is enabled.
note: Override UpdateNavigationRelevance() to propagate the flag to the desired components.
see: SetCanAffectNavigationGeneration(), UpdateNavigationRelevance()

<a id="unreal.Pawn.base_eye_height"></a>

#### base_eye_height

```python
@property
def base_eye_height() -> float
```

(float):  [Read-Write] Base eye height above collision center.

<a id="unreal.Pawn.base_eye_height"></a>

#### base_eye_height

```python
@base_eye_height.setter
def base_eye_height(value: float) -> None
```

<a id="unreal.Pawn.ai_controller_class"></a>

#### ai_controller_class

```python
@property
def ai_controller_class() -> Class
```

(type(Class)):  [Read-Write] Default class to use when pawn is controlled by AI.

<a id="unreal.Pawn.ai_controller_class"></a>

#### ai_controller_class

```python
@ai_controller_class.setter
def ai_controller_class(value: Class) -> None
```

<a id="unreal.Pawn.controller_class"></a>

#### controller_class

```python
@property
def controller_class() -> Class
```

deprecated: 'controller_class' was renamed to 'ai_controller_class'.

<a id="unreal.Pawn.controller_class"></a>

#### controller_class

```python
@controller_class.setter
def controller_class(value: Class) -> None
```

<a id="unreal.Pawn.player_state"></a>

#### player_state

```python
@property
def player_state() -> PlayerState
```

(PlayerState):  [Read-Only] If Pawn is possessed by a player, points to its Player State.  Needed for network play as controllers are not replicated to clients.

<a id="unreal.Pawn.player_replication_info"></a>

#### player_replication_info

```python
@property
def player_replication_info() -> PlayerState
```

deprecated: 'player_replication_info' was renamed to 'player_state'.

<a id="unreal.Pawn.last_hit_by"></a>

#### last_hit_by

```python
@property
def last_hit_by() -> Controller
```

(Controller):  [Read-Only] Controller of the last Actor that caused us damage.

<a id="unreal.Pawn.receive_controller_changed_delegate"></a>

#### receive_controller_changed_delegate

```python
@property
def receive_controller_changed_delegate() -> PawnControllerChangedSignature
```

(PawnControllerChangedSignature):  [Read-Write] Event called after a pawn's controller has changed, on the server and owning client. This will happen at the same time as the delegate on GameInstance

<a id="unreal.Pawn.receive_controller_changed_delegate"></a>

#### receive_controller_changed_delegate

```python
@receive_controller_changed_delegate.setter
def receive_controller_changed_delegate(
        value: PawnControllerChangedSignature) -> None
```

<a id="unreal.Pawn.receive_restarted_delegate"></a>

#### receive_restarted_delegate

```python
@property
def receive_restarted_delegate() -> PawnRestartedSignature
```

(PawnRestartedSignature):  [Read-Write] Event called after a pawn has been restarted, usually by a possession change. This is called on the server for all pawns and the owning client for player pawns

<a id="unreal.Pawn.receive_restarted_delegate"></a>

#### receive_restarted_delegate

```python
@receive_restarted_delegate.setter
def receive_restarted_delegate(value: PawnRestartedSignature) -> None
```

<a id="unreal.Pawn.spawn_default_controller"></a>

#### spawn_default_controller

```python
def spawn_default_controller() -> None
```

x.spawn_default_controller() -> None
Spawn default controller for this Pawn, and get possessed by it.

<a id="unreal.Pawn.set_can_affect_navigation_generation"></a>

#### set_can_affect_navigation_generation

```python
def set_can_affect_navigation_generation(new_value: bool,
                                         force_update: bool = False) -> None
```

x.set_can_affect_navigation_generation(new_value, force_update=False) -> None
Use SetCanAffectNavigationGeneration to change this value at runtime.
Note that calling this function at runtime will result in any navigation change only if runtime navigation generation is enabled.

Args:
    new_value (bool): 
    force_update (bool):

<a id="unreal.Pawn.receive_unpossessed"></a>

#### receive_unpossessed

```python
def receive_unpossessed(old_controller: Controller) -> None
```

x.receive_unpossessed(old_controller) -> None
Event called when the Pawn is no longer possessed by a Controller. Only called on the server (or in standalone)

Args:
    old_controller (Controller):

<a id="unreal.Pawn.receive_restarted"></a>

#### receive_restarted

```python
def receive_restarted() -> None
```

x.receive_restarted() -> None
Event called after a pawn has been restarted, usually by a possession change. This is called on the server for all pawns and the owning client for player pawns

<a id="unreal.Pawn.receive_possessed"></a>

#### receive_possessed

```python
def receive_possessed(new_controller: Controller) -> None
```

x.receive_possessed(new_controller) -> None
Event called when the Pawn is possessed by a Controller. Only called on the server (or in standalone)

Args:
    new_controller (Controller):

<a id="unreal.Pawn.receive_controller_changed"></a>

#### receive_controller_changed

```python
def receive_controller_changed(old_controller: Controller,
                               new_controller: Controller) -> None
```

x.receive_controller_changed(old_controller, new_controller) -> None
Event called after a pawn's controller has changed, on the server and owning client. This will happen at the same time as the delegate on GameInstance

Args:
    old_controller (Controller): 
    new_controller (Controller):

<a id="unreal.Pawn.pawn_make_noise"></a>

#### pawn_make_noise

```python
def pawn_make_noise(loudness: float,
                    noise_location: Vector,
                    use_noise_maker_location: bool = True,
                    noise_maker: Actor = None) -> None
```

x.pawn_make_noise(loudness, noise_location, use_noise_maker_location=True, noise_maker=None) -> None
Inform AIControllers that you've made a noise they might hear (they are sent a HearNoise message if they have bHearNoises==true)
The instigator of this sound is the pawn which is used to call MakeNoise.

Args:
    loudness (float): is the relative loudness of this noise (range 0.0 to 1.0).  Directly affects the hearing range specified by the AI's HearingThreshold.
    noise_location (Vector): Position of noise source.  If zero vector, use the actor's location.
    use_noise_maker_location (bool): If true, use the location of the NoiseMaker rather than NoiseLocation.  If false, use NoiseLocation.
    noise_maker (Actor): Which actor is the source of the noise.  Not to be confused with the Noise Instigator, which is responsible for the noise (and is the pawn on which this function is called).  If not specified, the pawn instigating the noise will be used as the NoiseMaker

<a id="unreal.Pawn.is_player_controlled"></a>

#### is_player_controlled

```python
def is_player_controlled() -> bool
```

x.is_player_controlled() -> bool
Returns true if controlled by a human player (possessed by a PlayerController).        This returns true for players controlled by remote clients

Returns:
    bool:

<a id="unreal.Pawn.is_pawn_controlled"></a>

#### is_pawn_controlled

```python
def is_pawn_controlled() -> bool
```

x.is_pawn_controlled() -> bool
Check if this actor is currently being controlled at all (the actor has a valid Controller, which will be false for remote clients)

Returns:
    bool:

<a id="unreal.Pawn.is_move_input_ignored"></a>

#### is_move_input_ignored

```python
def is_move_input_ignored() -> bool
```

x.is_move_input_ignored() -> bool
Helper to see if move input is ignored. If our controller is a PlayerController, checks Controller->IsMoveInputIgnored().

Returns:
    bool:

<a id="unreal.Pawn.is_locally_viewed"></a>

#### is_locally_viewed

```python
def is_locally_viewed() -> bool
```

x.is_locally_viewed() -> bool
Is this pawn the ViewTarget of a local PlayerController?  Helpful for determining whether the pawn is
visible/critical for any VFX.  NOTE: Technically there may be some cases where locally controlled pawns return
false for this, such as if you are using a remote camera view of some sort.  But generally it will be true for
locally controlled pawns, and it will always be true for pawns that are being spectated in-game or in Replays.

Returns:
    bool:

<a id="unreal.Pawn.is_locally_controlled"></a>

#### is_locally_controlled

```python
def is_locally_controlled() -> bool
```

x.is_locally_controlled() -> bool
Returns true if controlled by a local (not network) Controller.

Returns:
    bool:

<a id="unreal.Pawn.is_controlled"></a>

#### is_controlled

```python
def is_controlled() -> bool
```

x.is_controlled() -> bool
Is Controlled

Returns:
    bool:

<a id="unreal.Pawn.is_bot_controlled"></a>

#### is_bot_controlled

```python
def is_bot_controlled() -> bool
```

x.is_bot_controlled() -> bool
Returns true if controlled by a bot.

Returns:
    bool:

<a id="unreal.Pawn.get_platform_user_id"></a>

#### get_platform_user_id

```python
def get_platform_user_id() -> PlatformUserId
```

x.get_platform_user_id() -> PlatformUserId
Returns the Platform User ID of the PlayerController that is controlling this character.

Returns an invalid Platform User ID if this character is not controlled by a local player.

Returns:
    PlatformUserId:

<a id="unreal.Pawn.get_pending_movement_input_vector"></a>

#### get_pending_movement_input_vector

```python
def get_pending_movement_input_vector() -> Vector
```

x.get_pending_movement_input_vector() -> Vector
Return the pending input vector in world space. This is the most up-to-date value of the input vector, pending ConsumeMovementInputVector() which clears it,
Usually only a PawnMovementComponent will want to read this value, or the Pawn itself if it is responsible for movement.
see: AddMovementInput(), GetLastMovementInputVector(), ConsumeMovementInputVector()

Returns:
    Vector: The pending input vector in world space.

<a id="unreal.Pawn.get_override_input_component_class"></a>

#### get_override_input_component_class

```python
def get_override_input_component_class() -> Class
```

x.get_override_input_component_class() -> type(Class)
Get Override Input Component Class

Returns:
    type(Class):

<a id="unreal.Pawn.get_nav_agent_location"></a>

#### get_nav_agent_location

```python
def get_nav_agent_location() -> Vector
```

x.get_nav_agent_location() -> Vector
Basically retrieved pawn's location on navmesh

Returns:
    Vector:

<a id="unreal.Pawn.get_movement_component"></a>

#### get_movement_component

```python
def get_movement_component() -> PawnMovementComponent
```

x.get_movement_component() -> PawnMovementComponent
Return our PawnMovementComponent, if we have one.

Returns:
    PawnMovementComponent:

<a id="unreal.Pawn.get_movement_base_actor"></a>

#### get_movement_base_actor

```python
@classmethod
def get_movement_base_actor(cls, pawn: Pawn) -> Actor
```

X.get_movement_base_actor(pawn) -> Actor
Gets the owning actor of the Movement Base Component on which the pawn is standing.

Args:
    pawn (Pawn): 

Returns:
    Actor:

<a id="unreal.Pawn.get_local_viewing_player_controller"></a>

#### get_local_viewing_player_controller

```python
def get_local_viewing_player_controller() -> PlayerController
```

x.get_local_viewing_player_controller() -> PlayerController
Returns local Player Controller viewing this pawn, whether it is controlling or spectating

Returns:
    PlayerController:

<a id="unreal.Pawn.get_last_movement_input_vector"></a>

#### get_last_movement_input_vector

```python
def get_last_movement_input_vector() -> Vector
```

x.get_last_movement_input_vector() -> Vector
Return the last input vector in world space that was processed by ConsumeMovementInputVector(), which is usually done by the Pawn or PawnMovementComponent.
Any user that needs to know about the input that last affected movement should use this function.
For example an animation update would want to use this, since by default the order of updates in a frame is:
PlayerController (device input) -> MovementComponent -> Pawn -> Mesh (animations)
see: AddMovementInput(), GetPendingMovementInputVector(), ConsumeMovementInputVector()

Returns:
    Vector: The last input vector in world space that was processed by ConsumeMovementInputVector().

<a id="unreal.Pawn.get_control_rotation"></a>

#### get_control_rotation

```python
def get_control_rotation() -> Rotator
```

x.get_control_rotation() -> Rotator
Get the rotation of the Controller, often the 'view' rotation of this Pawn.

Returns:
    Rotator:

<a id="unreal.Pawn.get_controller"></a>

#### get_controller

```python
def get_controller() -> Controller
```

x.get_controller() -> Controller
Returns controller for this actor.

Returns:
    Controller:

<a id="unreal.Pawn.get_base_aim_rotation"></a>

#### get_base_aim_rotation

```python
def get_base_aim_rotation() -> Rotator
```

x.get_base_aim_rotation() -> Rotator
Return the aim rotation for the Pawn.
If we have a controller, by default we aim at the player's 'eyes' direction
that is by default the Pawn rotation for AI, and camera (crosshair) rotation for human players.

Returns:
    Rotator:

<a id="unreal.Pawn.detach_from_controller_pending_destroy"></a>

#### detach_from_controller_pending_destroy

```python
def detach_from_controller_pending_destroy() -> None
```

x.detach_from_controller_pending_destroy() -> None
Call this function to detach safely pawn from its controller, knowing that we will be destroyed soon.

<a id="unreal.Pawn.consume_movement_input_vector"></a>

#### consume_movement_input_vector

```python
def consume_movement_input_vector() -> Vector
```

x.consume_movement_input_vector() -> Vector
Returns the pending input vector and resets it to zero.
This should be used during a movement update (by the Pawn or PawnMovementComponent) to prevent accumulation of control input between frames.
Copies the pending input vector to the saved input vector (GetLastMovementInputVector()).

Returns:
    Vector: The pending input vector.

<a id="unreal.Pawn.add_movement_input"></a>

#### add_movement_input

```python
def add_movement_input(world_direction: Vector,
                       scale_value: float = 1.000000,
                       force: bool = False) -> None
```

x.add_movement_input(world_direction, scale_value=1.000000, force=False) -> None
Add movement input along the given world direction vector (usually normalized) scaled by 'ScaleValue'. If ScaleValue < 0, movement will be in the opposite direction.
Base Pawn classes won't automatically apply movement, it's up to the user to do so in a Tick event. Subclasses such as Character and DefaultPawn automatically handle this input and move.
see: GetPendingMovementInputVector(), GetLastMovementInputVector(), ConsumeMovementInputVector()

Args:
    world_direction (Vector): Direction in world space to apply input
    scale_value (float): Scale to apply to input. This can be used for analog input, ie a value of 0.5 applies half the normal value, while -1.0 would reverse the direction.
    force (bool): If true always add the input, ignoring the result of IsMoveInputIgnored().

<a id="unreal.Pawn.add_controller_yaw_input"></a>

#### add_controller_yaw_input

```python
def add_controller_yaw_input(val: float) -> None
```

x.add_controller_yaw_input(val) -> None
Add input (affecting Yaw) to the Controller's ControlRotation, if it is a local PlayerController.
This value is multiplied by the PlayerController's InputYawScale value.
see: PlayerController::InputYawScale

Args:
    val (float): Amount to add to Yaw. This value is multiplied by the PlayerController's InputYawScale value.

<a id="unreal.Pawn.add_turn_input"></a>

#### add_turn_input

```python
def add_turn_input(val: float) -> None
```

deprecated: 'add_turn_input' was renamed to 'add_controller_yaw_input'.

<a id="unreal.Pawn.add_yaw_input"></a>

#### add_yaw_input

```python
def add_yaw_input(val: float) -> None
```

deprecated: 'add_yaw_input' was renamed to 'add_controller_yaw_input'.

<a id="unreal.Pawn.add_controller_roll_input"></a>

#### add_controller_roll_input

```python
def add_controller_roll_input(val: float) -> None
```

x.add_controller_roll_input(val) -> None
Add input (affecting Roll) to the Controller's ControlRotation, if it is a local PlayerController.
This value is multiplied by the PlayerController's InputRollScale value.
see: PlayerController::InputRollScale

Args:
    val (float): Amount to add to Roll. This value is multiplied by the PlayerController's InputRollScale value.

<a id="unreal.Pawn.add_roll_input"></a>

#### add_roll_input

```python
def add_roll_input(val: float) -> None
```

deprecated: 'add_roll_input' was renamed to 'add_controller_roll_input'.

<a id="unreal.Pawn.add_controller_pitch_input"></a>

#### add_controller_pitch_input

```python
def add_controller_pitch_input(val: float) -> None
```

x.add_controller_pitch_input(val) -> None
Add input (affecting Pitch) to the Controller's ControlRotation, if it is a local PlayerController.
This value is multiplied by the PlayerController's InputPitchScale value.
see: PlayerController::InputPitchScale

Args:
    val (float): Amount to add to Pitch. This value is multiplied by the PlayerController's InputPitchScale value.

<a id="unreal.Pawn.add_look_up_input"></a>

#### add_look_up_input

```python
def add_look_up_input(val: float) -> None
```

deprecated: 'add_look_up_input' was renamed to 'add_controller_pitch_input'.

<a id="unreal.Pawn.add_pitch_input"></a>

#### add_pitch_input

```python
def add_pitch_input(val: float) -> None
```

deprecated: 'add_pitch_input' was renamed to 'add_controller_pitch_input'.

<a id="unreal.Character"></a>