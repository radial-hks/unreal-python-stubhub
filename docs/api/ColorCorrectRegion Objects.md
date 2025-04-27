## ColorCorrectRegion Objects

```python
class ColorCorrectRegion(Actor)
```

An instance of Color Correction Region. Used to aggregate all active regions.
This actor is aggregated by ColorCorrectRegionsSubsystem on Tick.
AActor class itself is not aware of when it is added/removed, Undo/Redo etc in the Editor.
More information in ColorCorrectRegionsSubsytem.h

**C++ Source:**

- **Plugin**: ColorCorrectRegions
- **Module**: ColorCorrectRegions
- **File**: ColorCorrectRegion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``affected_actors`` (Set[Actor]):  [Read-Write] List of actors that get affected or ignored by Per actor CC. Effect depends on the above option.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``color_grading_settings`` (ColorGradingSettings):  [Read-Write] Color correction settings.
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
- ``enable_per_actor_cc`` (bool):  [Read-Write] Enables or disabled per actor color correction.
- ``enabled`` (bool):  [Read-Write] Enable/Disable color correction provided by this region.
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``falloff`` (float):  [Read-Write] Falloff. Softening the region.
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``inner`` (float):  [Read-Write] Inner of the region. Swapped with Outer in case it is higher than Outer.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``intensity`` (float):  [Read-Write] Color correction intensity. Clamped to 0-1 range.
- ``invert`` (bool):  [Read-Write] Invert region.
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
- ``on_released`` (ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``origin`` (Transform):  [Read-Only] The origin when used in the ICVFX panel.
- ``outer`` (float):  [Read-Write] Outer of the region.
- ``per_actor_color_correction`` (ColorCorrectRegionStencilType):  [Read-Write] Controls in which way the below targets will be affected by color correction.
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``positional_params`` (DisplayClusterPositionalParams):  [Read-Write] Spherical coordinates in relation to the origin, primarily used with the ICVFX panel.
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``priority`` (int32):  [Read-Write] Render priority/order. The higher the number the later region will be applied.
  A region with Priority 1 will be rendered before a region with Priority 10.
  This property is hidden if priority is determined by distance from the camera (When Window CCR is being used).
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
- ``temperature`` (float):  [Read-Write] Color correction temperature.
- ``temperature_type`` (ColorCorrectRegionTemperatureType):  [Read-Write] Type of algorithm to be used to control color temperature or white balance.
- ``tint`` (float):  [Read-Write] Color temperature tint.
- ``type`` (ColorCorrectRegionsType):  [Read-Write] Region type.
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

<a id="unreal.ColorCorrectRegion.type"></a>

#### type

```python
@property
def type() -> ColorCorrectRegionsType
```

(ColorCorrectRegionsType):  [Read-Write] Region type.

<a id="unreal.ColorCorrectRegion.type"></a>

#### type

```python
@type.setter
def type(value: ColorCorrectRegionsType) -> None
```

<a id="unreal.ColorCorrectRegion.priority"></a>

#### priority

```python
@property
def priority() -> int
```

(int32):  [Read-Write] Render priority/order. The higher the number the later region will be applied.
A region with Priority 1 will be rendered before a region with Priority 10.
This property is hidden if priority is determined by distance from the camera (When Window CCR is being used).

<a id="unreal.ColorCorrectRegion.priority"></a>

#### priority

```python
@priority.setter
def priority(value: int) -> None
```

<a id="unreal.ColorCorrectRegion.intensity"></a>

#### intensity

```python
@property
def intensity() -> float
```

(float):  [Read-Write] Color correction intensity. Clamped to 0-1 range.

<a id="unreal.ColorCorrectRegion.intensity"></a>

#### intensity

```python
@intensity.setter
def intensity(value: float) -> None
```

<a id="unreal.ColorCorrectRegion.inner"></a>

#### inner

```python
@property
def inner() -> float
```

(float):  [Read-Write] Inner of the region. Swapped with Outer in case it is higher than Outer.

<a id="unreal.ColorCorrectRegion.inner"></a>

#### inner

```python
@inner.setter
def inner(value: float) -> None
```

<a id="unreal.ColorCorrectRegion.outer"></a>

#### outer

```python
@property
def outer() -> float
```

(float):  [Read-Write] Outer of the region.

<a id="unreal.ColorCorrectRegion.outer"></a>

#### outer

```python
@outer.setter
def outer(value: float) -> None
```

<a id="unreal.ColorCorrectRegion.falloff"></a>

#### falloff

```python
@property
def falloff() -> float
```

(float):  [Read-Write] Falloff. Softening the region.

<a id="unreal.ColorCorrectRegion.falloff"></a>

#### falloff

```python
@falloff.setter
def falloff(value: float) -> None
```

<a id="unreal.ColorCorrectRegion.invert"></a>

#### invert

```python
@property
def invert() -> bool
```

(bool):  [Read-Write] Invert region.

<a id="unreal.ColorCorrectRegion.invert"></a>

#### invert

```python
@invert.setter
def invert(value: bool) -> None
```

<a id="unreal.ColorCorrectRegion.temperature_type"></a>

#### temperature_type

```python
@property
def temperature_type() -> ColorCorrectRegionTemperatureType
```

(ColorCorrectRegionTemperatureType):  [Read-Write] Type of algorithm to be used to control color temperature or white balance.

<a id="unreal.ColorCorrectRegion.temperature_type"></a>

#### temperature_type

```python
@temperature_type.setter
def temperature_type(value: ColorCorrectRegionTemperatureType) -> None
```

<a id="unreal.ColorCorrectRegion.temperature"></a>

#### temperature

```python
@property
def temperature() -> float
```

(float):  [Read-Write] Color correction temperature.

<a id="unreal.ColorCorrectRegion.temperature"></a>

#### temperature

```python
@temperature.setter
def temperature(value: float) -> None
```

<a id="unreal.ColorCorrectRegion.tint"></a>

#### tint

```python
@property
def tint() -> float
```

(float):  [Read-Write] Color temperature tint.

<a id="unreal.ColorCorrectRegion.tint"></a>

#### tint

```python
@tint.setter
def tint(value: float) -> None
```

<a id="unreal.ColorCorrectRegion.color_grading_settings"></a>

#### color_grading_settings

```python
@property
def color_grading_settings() -> ColorGradingSettings
```

(ColorGradingSettings):  [Read-Write] Color correction settings.

<a id="unreal.ColorCorrectRegion.color_grading_settings"></a>

#### color_grading_settings

```python
@color_grading_settings.setter
def color_grading_settings(value: ColorGradingSettings) -> None
```

<a id="unreal.ColorCorrectRegion.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Enable/Disable color correction provided by this region.

<a id="unreal.ColorCorrectRegion.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.ColorCorrectRegion.enable_per_actor_cc"></a>

#### enable_per_actor_cc

```python
@property
def enable_per_actor_cc() -> bool
```

(bool):  [Read-Write] Enables or disabled per actor color correction.

<a id="unreal.ColorCorrectRegion.enable_per_actor_cc"></a>

#### enable_per_actor_cc

```python
@enable_per_actor_cc.setter
def enable_per_actor_cc(value: bool) -> None
```

<a id="unreal.ColorCorrectRegion.per_actor_color_correction"></a>

#### per_actor_color_correction

```python
@property
def per_actor_color_correction() -> ColorCorrectRegionStencilType
```

(ColorCorrectRegionStencilType):  [Read-Write] Controls in which way the below targets will be affected by color correction.

<a id="unreal.ColorCorrectRegion.per_actor_color_correction"></a>

#### per_actor_color_correction

```python
@per_actor_color_correction.setter
def per_actor_color_correction(value: ColorCorrectRegionStencilType) -> None
```

<a id="unreal.ColorCorrectRegion.affected_actors"></a>

#### affected_actors

```python
@property
def affected_actors() -> Set[Actor]
```

(Set[Actor]):  [Read-Write] List of actors that get affected or ignored by Per actor CC. Effect depends on the above option.

<a id="unreal.ColorCorrectRegion.affected_actors"></a>

#### affected_actors

```python
@affected_actors.setter
def affected_actors(value: Set[Actor]) -> None
```

<a id="unreal.ColorCorrectRegion.origin"></a>

#### origin

```python
@property
def origin() -> Transform
```

(Transform):  [Read-Only] The origin when used in the ICVFX panel.

<a id="unreal.ColorCorrectRegion.set_yaw"></a>

#### set_yaw

```python
def set_yaw(value: float) -> None
```

x.set_yaw(value) -> None
Set Yaw

Args:
    value (double):

<a id="unreal.ColorCorrectRegion.set_spin"></a>

#### set_spin

```python
def set_spin(value: float) -> None
```

x.set_spin(value) -> None
Set Spin

Args:
    value (double):

<a id="unreal.ColorCorrectRegion.set_scale"></a>

#### set_scale

```python
def set_scale(scale: Vector2D) -> None
```

x.set_scale(scale) -> None
Set Scale

Args:
    scale (Vector2D):

<a id="unreal.ColorCorrectRegion.set_radial_offset"></a>

#### set_radial_offset

```python
def set_radial_offset(value: float) -> None
```

x.set_radial_offset(value) -> None
Set Radial Offset

Args:
    value (double):

<a id="unreal.ColorCorrectRegion.set_positional_params"></a>

#### set_positional_params

```python
def set_positional_params(params: DisplayClusterPositionalParams) -> None
```

x.set_positional_params(params) -> None
Set Positional Params

Args:
    params (DisplayClusterPositionalParams):

<a id="unreal.ColorCorrectRegion.set_pitch"></a>

#### set_pitch

```python
def set_pitch(value: float) -> None
```

x.set_pitch(value) -> None
Set Pitch

Args:
    value (double):

<a id="unreal.ColorCorrectRegion.set_longitude"></a>

#### set_longitude

```python
def set_longitude(value: float) -> None
```

x.set_longitude(value) -> None
~Begin IDisplayClusterStageActor interface

Args:
    value (double):

<a id="unreal.ColorCorrectRegion.set_latitude"></a>

#### set_latitude

```python
def set_latitude(value: float) -> None
```

x.set_latitude(value) -> None
Set Latitude

Args:
    value (double):

<a id="unreal.ColorCorrectRegion.set_distance_from_center"></a>

#### set_distance_from_center

```python
def set_distance_from_center(value: float) -> None
```

x.set_distance_from_center(value) -> None
Set Distance from Center

Args:
    value (double):

<a id="unreal.ColorCorrectRegion.get_yaw"></a>

#### get_yaw

```python
def get_yaw() -> float
```

x.get_yaw() -> double
Get Yaw

Returns:
    double:

<a id="unreal.ColorCorrectRegion.get_spin"></a>

#### get_spin

```python
def get_spin() -> float
```

x.get_spin() -> double
Get Spin

Returns:
    double:

<a id="unreal.ColorCorrectRegion.get_scale"></a>

#### get_scale

```python
def get_scale() -> Vector2D
```

x.get_scale() -> Vector2D
Get Scale

Returns:
    Vector2D:

<a id="unreal.ColorCorrectRegion.get_radial_offset"></a>

#### get_radial_offset

```python
def get_radial_offset() -> float
```

x.get_radial_offset() -> double
Get Radial Offset

Returns:
    double:

<a id="unreal.ColorCorrectRegion.get_positional_params"></a>

#### get_positional_params

```python
def get_positional_params() -> DisplayClusterPositionalParams
```

x.get_positional_params() -> DisplayClusterPositionalParams
Get Positional Params

Returns:
    DisplayClusterPositionalParams:

<a id="unreal.ColorCorrectRegion.get_pitch"></a>

#### get_pitch

```python
def get_pitch() -> float
```

x.get_pitch() -> double
Get Pitch

Returns:
    double:

<a id="unreal.ColorCorrectRegion.get_longitude"></a>

#### get_longitude

```python
def get_longitude() -> float
```

x.get_longitude() -> double
Get Longitude

Returns:
    double:

<a id="unreal.ColorCorrectRegion.get_latitude"></a>

#### get_latitude

```python
def get_latitude() -> float
```

x.get_latitude() -> double
Get Latitude

Returns:
    double:

<a id="unreal.ColorCorrectRegion.get_distance_from_center"></a>

#### get_distance_from_center

```python
def get_distance_from_center() -> float
```

x.get_distance_from_center() -> double
Get Distance from Center

Returns:
    double:

<a id="unreal.ColorCorrectionRegion"></a>