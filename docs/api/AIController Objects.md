## AIController Objects

```python
class AIController(Controller)
```

AIController is the base class of controllers for AI-controlled Pawns.

Controllers are non-physical actors that can be attached to a pawn to control its actions.
AIControllers manage the artificial intelligence for the pawns they control.
In networked games, they only exist on the server.
see: https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Controller/

**C++ Source:**

- **Module**: AIModule
- **File**: AIController.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actions_comp`` (PawnActionsComponent):  [Read-Write]
- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``allow_strafe`` (bool):  [Read-Write] Is strafing allowed during movement?
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
- ``blackboard`` (BlackboardComponent):  [Read-Write] blackboard
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``brain_component`` (BrainComponent):  [Read-Write] Component responsible for behaviors.
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
- ``default_navigation_filter_class`` (type(Class)):  [Read-Write]
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
- ``path_following_component`` (PathFollowingComponent):  [Read-Only] Component used for moving along a path.
- ``perception_component`` (AIPerceptionComponent):  [Read-Only]
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``player_state`` (PlayerState):  [Read-Write] PlayerState containing replicated information about the player using this controller (only exists for players, not NPCs).
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``receive_move_completed`` (AIMoveCompletedSignature):  [Read-Write] Blueprint notification that we've completed the current movement request
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
- ``set_control_rotation_from_pawn_orientation`` (bool):  [Read-Write] Copy Pawn rotation to ControlRotation, if there is no focus point.
- ``skip_extra_los_checks`` (bool):  [Read-Write] Skip extra line of sight traces to extremities of target being checked.
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``start_ai_logic_on_possess`` (bool):  [Read-Write] By default AI's logic does not start when controlled Pawn is possessed. Setting this flag to true
      will make AI logic start when pawn is possessed
- ``stop_ai_logic_on_unposses`` (bool):  [Read-Write] By default AI's logic gets stopped when controlled Pawn is unpossessed. Setting this flag to false
      will make AI logic persist past losing control over a pawn
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
- ``wants_player_state`` (bool):  [Read-Write] Specifies if this AI wants its own PlayerState.

<a id="unreal.AIController.start_ai_logic_on_possess"></a>

#### start_ai_logic_on_possess

```python
@property
def start_ai_logic_on_possess() -> bool
```

(bool):  [Read-Write] By default AI's logic does not start when controlled Pawn is possessed. Setting this flag to true
    will make AI logic start when pawn is possessed

<a id="unreal.AIController.start_ai_logic_on_possess"></a>

#### start_ai_logic_on_possess

```python
@start_ai_logic_on_possess.setter
def start_ai_logic_on_possess(value: bool) -> None
```

<a id="unreal.AIController.stop_ai_logic_on_unposses"></a>

#### stop_ai_logic_on_unposses

```python
@property
def stop_ai_logic_on_unposses() -> bool
```

(bool):  [Read-Write] By default AI's logic gets stopped when controlled Pawn is unpossessed. Setting this flag to false
    will make AI logic persist past losing control over a pawn

<a id="unreal.AIController.stop_ai_logic_on_unposses"></a>

#### stop_ai_logic_on_unposses

```python
@stop_ai_logic_on_unposses.setter
def stop_ai_logic_on_unposses(value: bool) -> None
```

<a id="unreal.AIController.skip_extra_los_checks"></a>

#### skip_extra_los_checks

```python
@property
def skip_extra_los_checks() -> bool
```

(bool):  [Read-Write] Skip extra line of sight traces to extremities of target being checked.

<a id="unreal.AIController.skip_extra_los_checks"></a>

#### skip_extra_los_checks

```python
@skip_extra_los_checks.setter
def skip_extra_los_checks(value: bool) -> None
```

<a id="unreal.AIController.allow_strafe"></a>

#### allow_strafe

```python
@property
def allow_strafe() -> bool
```

(bool):  [Read-Write] Is strafing allowed during movement?

<a id="unreal.AIController.allow_strafe"></a>

#### allow_strafe

```python
@allow_strafe.setter
def allow_strafe(value: bool) -> None
```

<a id="unreal.AIController.wants_player_state"></a>

#### wants_player_state

```python
@property
def wants_player_state() -> bool
```

(bool):  [Read-Write] Specifies if this AI wants its own PlayerState.

<a id="unreal.AIController.wants_player_state"></a>

#### wants_player_state

```python
@wants_player_state.setter
def wants_player_state(value: bool) -> None
```

<a id="unreal.AIController.set_control_rotation_from_pawn_orientation"></a>

#### set_control_rotation_from_pawn_orientation

```python
@property
def set_control_rotation_from_pawn_orientation() -> bool
```

(bool):  [Read-Write] Copy Pawn rotation to ControlRotation, if there is no focus point.

<a id="unreal.AIController.set_control_rotation_from_pawn_orientation"></a>

#### set_control_rotation_from_pawn_orientation

```python
@set_control_rotation_from_pawn_orientation.setter
def set_control_rotation_from_pawn_orientation(value: bool) -> None
```

<a id="unreal.AIController.brain_component"></a>

#### brain_component

```python
@property
def brain_component() -> BrainComponent
```

(BrainComponent):  [Read-Write] Component responsible for behaviors.

<a id="unreal.AIController.brain_component"></a>

#### brain_component

```python
@brain_component.setter
def brain_component(value: BrainComponent) -> None
```

<a id="unreal.AIController.actions_comp"></a>

#### actions_comp

```python
@property
def actions_comp() -> PawnActionsComponent
```

(PawnActionsComponent):  [Read-Only]

<a id="unreal.AIController.blackboard"></a>

#### blackboard

```python
@property
def blackboard() -> BlackboardComponent
```

(BlackboardComponent):  [Read-Only] blackboard

<a id="unreal.AIController.default_navigation_filter_class"></a>

#### default_navigation_filter_class

```python
@property
def default_navigation_filter_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.AIController.default_navigation_filter_class"></a>

#### default_navigation_filter_class

```python
@default_navigation_filter_class.setter
def default_navigation_filter_class(value: Class) -> None
```

<a id="unreal.AIController.receive_move_completed"></a>

#### receive_move_completed

```python
@property
def receive_move_completed() -> AIMoveCompletedSignature
```

(AIMoveCompletedSignature):  [Read-Write] Blueprint notification that we've completed the current movement request

<a id="unreal.AIController.receive_move_completed"></a>

#### receive_move_completed

```python
@receive_move_completed.setter
def receive_move_completed(value: AIMoveCompletedSignature) -> None
```

<a id="unreal.AIController.use_blackboard"></a>

#### use_blackboard

```python
def use_blackboard(
        blackboard_asset: BlackboardData) -> Optional[BlackboardComponent]
```

x.use_blackboard(blackboard_asset) -> BlackboardComponent or None
Makes AI use the specified Blackboard asset & creates a Blackboard Component if one does not already exist.

Args:
    blackboard_asset (BlackboardData): The Blackboard asset to use.

Returns:
    BlackboardComponent or None: true if we successfully linked the blackboard asset to the blackboard component.

    blackboard_component (BlackboardComponent): The Blackboard component that was used or created to work with the passed-in Blackboard Asset.

<a id="unreal.AIController.unclaim_task_resource"></a>

#### unclaim_task_resource

```python
def unclaim_task_resource(resource_class: Class) -> None
```

x.unclaim_task_resource(resource_class) -> None
Unclaim Task Resource

Args:
    resource_class (type(Class)):

<a id="unreal.AIController.set_path_following_component"></a>

#### set_path_following_component

```python
def set_path_following_component(
        new_pf_component: PathFollowingComponent) -> None
```

x.set_path_following_component(new_pf_component) -> None
Note that this function does not do any pathfollowing state transfer.
    Intended to be called as part of initialization/setup process

Args:
    new_pf_component (PathFollowingComponent):

<a id="unreal.AIController.set_move_block_detection"></a>

#### set_move_block_detection

```python
def set_move_block_detection(enable: bool) -> None
```

x.set_move_block_detection(enable) -> None
Updates state of movement block detection.

Args:
    enable (bool):

<a id="unreal.AIController.run_behavior_tree"></a>

#### run_behavior_tree

```python
def run_behavior_tree(bt_asset: BehaviorTree) -> bool
```

x.run_behavior_tree(bt_asset) -> bool
Starts executing behavior tree.

Args:
    bt_asset (BehaviorTree): 

Returns:
    bool:

<a id="unreal.AIController.on_using_black_board"></a>

#### on_using_black_board

```python
def on_using_black_board(blackboard_comp: BlackboardComponent,
                         blackboard_asset: BlackboardData) -> None
```

x.on_using_black_board(blackboard_comp, blackboard_asset) -> None
On Using Black Board

Args:
    blackboard_comp (BlackboardComponent): 
    blackboard_asset (BlackboardData):

<a id="unreal.AIController.move_to_location"></a>

#### move_to_location

```python
def move_to_location(
        dest: Vector,
        acceptance_radius: float = -1.000000,
        stop_on_overlap: bool = True,
        use_pathfinding: bool = True,
        project_destination_to_navigation: bool = False,
        can_strafe: bool = True,
        filter_class: Class = None,
        allow_partial_path: bool = True) -> PathFollowingRequestResult
```

x.move_to_location(dest, acceptance_radius=-1.000000, stop_on_overlap=True, use_pathfinding=True, project_destination_to_navigation=False, can_strafe=True, filter_class=None, allow_partial_path=True) -> PathFollowingRequestResult
Makes AI go toward specified Dest location, aborts any active path following
note: AcceptanceRadius has default value or -1 due to Header Parser not being able to recognize UPathFollowingComponent::DefaultAcceptanceRadius

Args:
    dest (Vector): 
    acceptance_radius (float): finish move if pawn gets close enough
    stop_on_overlap (bool): add pawn's radius to AcceptanceRadius
    use_pathfinding (bool): use navigation data to calculate path (otherwise it will go in straight line)
    project_destination_to_navigation (bool): project location on navigation data before using it
    can_strafe (bool): set focus related flag: bAllowStrafe
    filter_class (type(Class)): navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used
    allow_partial_path (bool): use incomplete path when goal can't be reached

Returns:
    PathFollowingRequestResult:

<a id="unreal.AIController.move_to_actor"></a>

#### move_to_actor

```python
def move_to_actor(
        goal: Actor,
        acceptance_radius: float = -1.000000,
        stop_on_overlap: bool = True,
        use_pathfinding: bool = True,
        can_strafe: bool = True,
        filter_class: Class = None,
        allow_partial_path: bool = True) -> PathFollowingRequestResult
```

x.move_to_actor(goal, acceptance_radius=-1.000000, stop_on_overlap=True, use_pathfinding=True, can_strafe=True, filter_class=None, allow_partial_path=True) -> PathFollowingRequestResult
Makes AI go toward specified Goal actor (destination will be continuously updated), aborts any active path following
note: AcceptanceRadius has default value or -1 due to Header Parser not being able to recognize UPathFollowingComponent::DefaultAcceptanceRadius

Args:
    goal (Actor): 
    acceptance_radius (float): finish move if pawn gets close enough
    stop_on_overlap (bool): add pawn's radius to AcceptanceRadius
    use_pathfinding (bool): use navigation data to calculate path (otherwise it will go in straight line)
    can_strafe (bool): set focus related flag: bAllowStrafe
    filter_class (type(Class)): navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used
    allow_partial_path (bool): use incomplete path when goal can't be reached

Returns:
    PathFollowingRequestResult:

<a id="unreal.AIController.set_focus"></a>

#### set_focus

```python
def set_focus(new_focus: Actor) -> None
```

x.set_focus(new_focus) -> None
Set Focus for actor, will set FocalPoint as a result.

Args:
    new_focus (Actor):

<a id="unreal.AIController.set_focal_point"></a>

#### set_focal_point

```python
def set_focal_point(fp: Vector) -> None
```

x.set_focal_point(fp) -> None
Set the position that controller should be looking at.

Args:
    fp (Vector):

<a id="unreal.AIController.clear_focus"></a>

#### clear_focus

```python
def clear_focus() -> None
```

x.clear_focus() -> None
Clears Focus, will also clear FocalPoint as a result

<a id="unreal.AIController.has_partial_path"></a>

#### has_partial_path

```python
def has_partial_path() -> bool
```

x.has_partial_path() -> bool
Returns true if the current PathFollowingComponent's path is partial (does not reach desired destination).

Returns:
    bool:

<a id="unreal.AIController.get_path_following_component"></a>

#### get_path_following_component

```python
def get_path_following_component() -> PathFollowingComponent
```

x.get_path_following_component() -> PathFollowingComponent
Returns PathFollowingComponent subobject *

Returns:
    PathFollowingComponent:

<a id="unreal.AIController.get_move_status"></a>

#### get_move_status

```python
def get_move_status() -> PathFollowingStatus
```

x.get_move_status() -> PathFollowingStatus
Returns status of path following

Returns:
    PathFollowingStatus:

<a id="unreal.AIController.get_immediate_move_destination"></a>

#### get_immediate_move_destination

```python
def get_immediate_move_destination() -> Vector
```

x.get_immediate_move_destination() -> Vector
Returns position of current path segment's end.

Returns:
    Vector:

<a id="unreal.AIController.get_focus_actor"></a>

#### get_focus_actor

```python
def get_focus_actor() -> Actor
```

x.get_focus_actor() -> Actor
Get the focused actor.

Returns:
    Actor:

<a id="unreal.AIController.get_focal_point_on_actor"></a>

#### get_focal_point_on_actor

```python
def get_focal_point_on_actor(actor: Actor) -> Vector
```

x.get_focal_point_on_actor(actor) -> Vector
Retrieve the focal point this controller should focus to on given actor.

Args:
    actor (Actor): 

Returns:
    Vector:

<a id="unreal.AIController.get_focal_point"></a>

#### get_focal_point

```python
def get_focal_point() -> Vector
```

x.get_focal_point() -> Vector
Retrieve the final position that controller should be looking at.

Returns:
    Vector:

<a id="unreal.AIController.get_ai_perception_component"></a>

#### get_ai_perception_component

```python
def get_ai_perception_component() -> AIPerceptionComponent
```

x.get_ai_perception_component() -> AIPerceptionComponent
Get AIPerception Component

Returns:
    AIPerceptionComponent:

<a id="unreal.AIController.claim_task_resource"></a>

#### claim_task_resource

```python
def claim_task_resource(resource_class: Class) -> None
```

x.claim_task_resource(resource_class) -> None
Claim Task Resource

Args:
    resource_class (type(Class)):

<a id="unreal.AIResource_Movement"></a>