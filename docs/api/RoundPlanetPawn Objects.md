## RoundPlanetPawn Objects

```python
class RoundPlanetPawn(DefaultPawn)
```

This pawn can be used to easily move around the globe while maintaining a
sensible orientation. As the pawn moves across the horizon, it automatically
changes its own up direction such that the world always looks right-side up.

**C++ Source:**

- **Plugin**: GeoReferencing
- **Module**: GeoReferencing
- **File**: RoundPlanetPawn.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``add_default_movement_bindings`` (bool):  [Read-Write] If true, adds default input bindings for movement and camera look.
- ``ai_controller_class`` (type(Class)):  [Read-Write] Default class to use when pawn is controlled by AI.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``altitude`` (float):  [Read-Only] The distance between the geographic ellipsoid surface and the pawn
- ``altitude_profile_curve`` (CurveFloat):  [Read-Write] This curve dictates what percentage of the max altitude the pawn should take at a given time on the curve.
  Depending on the total distance to Fly, a constant maximum altitude is computed from FlyToLocationMaximumAltitudeCurve
  Then during the fly, the actual pawn altitude is computed from this profile and the reference maximum altitude.
  This allows to have nice movements whenever you FlyTo near or far from your actual location.
  This curve must be kept in the 0 to 1 range on both axes.
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
- ``base_look_up_rate`` (float):  [Read-Only] Base lookup rate, in deg/sec. Other scaling may affect final lookup rate.
- ``base_speed_kmh`` (float):  [Read-Write] The Reference maximum speed for the pawn, before being altered by any Scalar modifier or by altitude curve
  ActualMaxSpeed = BaseSpeedKmh * SpeedScalar * AltitudeSpeedModifierCurve(Altitude)
- ``base_turn_rate`` (float):  [Read-Only] Base turn rate, in deg/sec. Other scaling may affect final turn rate.
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
- ``collision_component`` (SphereComponent):  [Read-Only] DefaultPawn collision component
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
- ``fly_duration`` (float):  [Read-Write] Fly to Location duration (in seconds)
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``granularity_degrees`` (float):  [Read-Write] The granularity in degrees with which keypoints should be generated for the Fly to Location interpolation.
  Lower values means smoother motion.
  ROM : 1 degree latitude ~110km on earth. => 0.1 ~10km
- ``hat`` (float):  [Read-Only] Height Above Terrain. The distance between the ground and the pawn
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
- ``maximum_altitude_curve`` (CurveFloat):  [Read-Write] This curve is used to pick up a reference the maximum altitude when flying to a location.
  This maximum altitude will be moderated by the FlyToLocationAltitudeProfileCurve
  X Axis is the distance of the flight (meters)
  Y Axis is the maximum altitude to be used for this flight (meters)
- ``maximum_altitude_value`` (float):  [Read-Write] In case MaximumAltitudeCurve is not defined, the AltitudeProfileCurve will use this Maximum altitude value for the flight, whatever the travel distance.
  In meters
- ``maximum_step_count`` (int32):  [Read-Write] Make sure we don't get crazy in case of large flights with small granularity
- ``mesh_component`` (StaticMeshComponent):  [Read-Only] The mesh associated with this Pawn.
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``minimum_step_count`` (int32):  [Read-Write] The minimum linear steps for the FlyTolocation motion.
  GranularityDegrees is not sufficient in case of short travels. Eg if 0.1, any jump shorter than 10km will have only one step.
  Make sure we have at least this number of steps in the trajectory.
- ``movement_component`` (PawnMovementComponent):  [Read-Only] DefaultPawn movement component
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
- ``orbital_motion`` (bool):  [Read-Write] if True, the motion Forward/Right motion of the pawn are relative to Planet tangent,
  meaning the altitude will approximately be kept, whatever the pawn camera orientation
- ``override_input_component_class`` (type(Class)):  [Read-Write] If set, then this InputComponent class will be used instead of the Input Settings' DefaultInputComponentClass
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``player_state`` (PlayerState):  [Read-Write] If Pawn is possessed by a player, points to its Player State.  Needed for network play as controllers are not replicated to clients.
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``progress_curve`` (CurveFloat):  [Read-Write] This curve is used to ease in an out the Fly to Location speed.
  It must be kept in the 0 to 1 range on both axes.
  X axis is the normalized time of travel
  Y axis is the progress on the flight motion.
  A linear curve will give a constant progress speed whereas a easein//easeout one will slow down the speed at beginning/end of motion.
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
- ``speed_by_hat_modifier_curve`` (CurveFloat):  [Read-Write] When being very high and moving around the planet, we have to dynamically increase the speed based on Height above terrain to accelerate movement
  This curve adds a multiplying factor to the maximum speed depending on HAT.
  ActualMaxSpeed = BaseSpeedKmh * SpeedScalar * AltitudeSpeedModifierCurve(Altitude)
- ``speed_scalar`` (float):  [Read-Write] Scalar modifier for the base speed
  ActualMaxSpeed = BaseSpeedKmh * SpeedScalar * AltitudeSpeedModifierCurve(Altitude)
- ``speed_scalar_increment`` (float):  [Read-Write] Multiplier/Divider for increasing/decreasing the speed scalar
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

<a id="unreal.RoundPlanetPawn.orbital_motion"></a>

#### orbital_motion

```python
@property
def orbital_motion() -> bool
```

(bool):  [Read-Write] if True, the motion Forward/Right motion of the pawn are relative to Planet tangent,
meaning the altitude will approximately be kept, whatever the pawn camera orientation

<a id="unreal.RoundPlanetPawn.orbital_motion"></a>

#### orbital_motion

```python
@orbital_motion.setter
def orbital_motion(value: bool) -> None
```

<a id="unreal.RoundPlanetPawn.base_speed_kmh"></a>

#### base_speed_kmh

```python
@property
def base_speed_kmh() -> float
```

(float):  [Read-Write] The Reference maximum speed for the pawn, before being altered by any Scalar modifier or by altitude curve
ActualMaxSpeed = BaseSpeedKmh * SpeedScalar * AltitudeSpeedModifierCurve(Altitude)

<a id="unreal.RoundPlanetPawn.base_speed_kmh"></a>

#### base_speed_kmh

```python
@base_speed_kmh.setter
def base_speed_kmh(value: float) -> None
```

<a id="unreal.RoundPlanetPawn.speed_scalar"></a>

#### speed_scalar

```python
@property
def speed_scalar() -> float
```

(float):  [Read-Write] Scalar modifier for the base speed
ActualMaxSpeed = BaseSpeedKmh * SpeedScalar * AltitudeSpeedModifierCurve(Altitude)

<a id="unreal.RoundPlanetPawn.speed_scalar"></a>

#### speed_scalar

```python
@speed_scalar.setter
def speed_scalar(value: float) -> None
```

<a id="unreal.RoundPlanetPawn.speed_scalar_increment"></a>

#### speed_scalar_increment

```python
@property
def speed_scalar_increment() -> float
```

(float):  [Read-Write] Multiplier/Divider for increasing/decreasing the speed scalar

<a id="unreal.RoundPlanetPawn.speed_scalar_increment"></a>

#### speed_scalar_increment

```python
@speed_scalar_increment.setter
def speed_scalar_increment(value: float) -> None
```

<a id="unreal.RoundPlanetPawn.hat"></a>

#### hat

```python
@property
def hat() -> float
```

(float):  [Read-Only] Height Above Terrain. The distance between the ground and the pawn

<a id="unreal.RoundPlanetPawn.altitude"></a>

#### altitude

```python
@property
def altitude() -> float
```

(float):  [Read-Only] The distance between the geographic ellipsoid surface and the pawn

<a id="unreal.RoundPlanetPawn.reset_speed_scalar"></a>

#### reset_speed_scalar

```python
def reset_speed_scalar() -> None
```

x.reset_speed_scalar() -> None
Reset the Speed Scalar to its default value - Middle-mouse button click equivalent

<a id="unreal.RoundPlanetPawn.interrupt_fly_to_location"></a>

#### interrupt_fly_to_location

```python
def interrupt_fly_to_location() -> None
```

x.interrupt_fly_to_location() -> None
Stop the current Fly To Location motion

<a id="unreal.RoundPlanetPawn.increase_speed_scalar"></a>

#### increase_speed_scalar

```python
def increase_speed_scalar() -> None
```

x.increase_speed_scalar() -> None
Increase the Speed Scalar - MouseWheel Up equivalent

<a id="unreal.RoundPlanetPawn.fly_to_location_latitude_longitude_altitude"></a>

#### fly_to_location_latitude_longitude_altitude

```python
def fly_to_location_latitude_longitude_altitude(
        latitude: float, longitude: float, altitude: float,
        yaw_at_destination: float, pitch_at_destination: float,
        can_interrupt_by_moving: bool) -> None
```

x.fly_to_location_latitude_longitude_altitude(latitude, longitude, altitude, yaw_at_destination, pitch_at_destination, can_interrupt_by_moving) -> None
Begin a smooth camera flight to the given Latitude/Longitude destination such that the camera ends at the specified yaw and pitch.
The flight can be enforced or canceled if the user moves the pawn

Args:
    latitude (double): 
    longitude (double): 
    altitude (double): 
    yaw_at_destination (double): 
    pitch_at_destination (double): 
    can_interrupt_by_moving (bool):

<a id="unreal.RoundPlanetPawn.fly_to_location_geographic"></a>

#### fly_to_location_geographic

```python
def fly_to_location_geographic(geographic_destination: GeographicCoordinates,
                               yaw_at_destination: float,
                               pitch_at_destination: float,
                               can_interrupt_by_moving: bool) -> None
```

x.fly_to_location_geographic(geographic_destination, yaw_at_destination, pitch_at_destination, can_interrupt_by_moving) -> None
Begin a smooth camera flight to the given Latitude/Longitude destination such that the camera ends at the specified yaw and pitch.
The flight can be enforced or canceled if the user moves the pawn

Args:
    geographic_destination (GeographicCoordinates): 
    yaw_at_destination (double): 
    pitch_at_destination (double): 
    can_interrupt_by_moving (bool):

<a id="unreal.RoundPlanetPawn.fly_to_location_ecef"></a>

#### fly_to_location_ecef

```python
def fly_to_location_ecef(ecef_destination: Vector, yaw_at_destination: float,
                         pitch_at_destination: float,
                         can_interrupt_by_moving: bool) -> None
```

x.fly_to_location_ecef(ecef_destination, yaw_at_destination, pitch_at_destination, can_interrupt_by_moving) -> None
Begin a smooth camera flight to the given ECEF destination such that the camera ends at the specified yaw and pitch.
The flight can be enforced or canceled if the user moves the pawn

Args:
    ecef_destination (Vector): 
    yaw_at_destination (double): 
    pitch_at_destination (double): 
    can_interrupt_by_moving (bool):

<a id="unreal.RoundPlanetPawn.decrease_speed_scalar"></a>

#### decrease_speed_scalar

```python
def decrease_speed_scalar() -> None
```

x.decrease_speed_scalar() -> None
Decrease the Speed Scalar - MouseWheel Down equivalent

<a id="unreal.GeoReferencingEditorBPLibrary"></a>