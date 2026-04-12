## CesiumSunSky Objects

```python
class CesiumSunSky(Actor)
```

A globe-aware sun sky actor. If the georeference is set to CartographicOrigin
(aka Longitude/Latitude/Height) mode, then this actor will automatically
sync its longitude and latitude properties with the georeference's, and
recalculate the sun position whenever those properties change.

Note: because we use `Planet Center at Component Transform`
for the SkyAtmosphere transform mode, this actor's location will be forced
to the Earth's center if the georeference is set to CartographicOrigin.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumSunSky.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``aerial_perspective_view_distance_scale`` (float):  [Read-Write] Makes the aerial perspective look thicker by scaling distances from view
  to surfaces (opaque and translucent). This value is automatically scaled
  according to the CesiumGeoreference Scale and the Actor scale.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``atmosphere_height`` (float):  [Read-Write] The height of the atmosphere layer above the ground, in kilometers. This
  value is automatically scaled according to the CesiumGeoreference Scale and
  the Actor scale. However, Unreal Engine's SkyAtmosphere has a hard-coded
  minimum effective value of 0.1, so the atmosphere will look too thick when
  the globe is scaled down drastically.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``azimuth`` (double):  [Read-Write] The current sun azimuth in degrees clockwise from North toward East, as
  viewed from the Georeference origin.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``circumscribed_ground_height`` (double):  [Read-Write] The height at which to place the bottom of the atmosphere when the player
  pawn is above the CircumscribedGroundThreshold. This is expressed as a
  height in kilometers above the maximum radius of the ellipsoid (usually
  WGS84). To avoid dark splotchy artifacts in the atmosphere when zoomed out
  far from the globe, this value must be above the greatest height achieved
  by any part of the tileset.
- ``circumscribed_ground_threshold`` (double):  [Read-Write] When the player pawn is above this height, which is expressed in kilometers
  above the ellipsoid, this Actor will use an atmosphere ground radius that
  is guaranteed to be above the terrain surface anywhere on Earth. This
  avoids artifacts caused by terrain poking through the atmosphere when
  viewing the Earth from far away.

  Below InscribedGroundThreshold, this Actor will use an atmosphere
  ground radius that is calculated to be at or below the terrain surface at
  the player pawn's current location. This avoids a gap between the bottom of
  the atmosphere and the top of the terrain when zoomed in close to the
  terrain surface.

  At heights in between InscribedGroundThreshold and
  CircumscribedGroundThreshold, this Actor uses a linear interpolation
  between the two ground radii.

  This value is automatically scaled according to the CesiumGeoreference
  Scale and the Actor scale.
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``corrected_elevation`` (double):  [Read-Write] The current sun elevation, corrected for atmospheric diffraction, in
  degrees above the horizontal, as viewed from the Georeference origin.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``day`` (int32):  [Read-Write] The day of the month.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``directional_light`` (DirectionalLightComponent):  [Read-Write]
- ``dst_end_day`` (int32):  [Read-Write] Set the Date at which DST ends in the current year.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``dst_end_month`` (int32):  [Read-Write] Set the Date at which DST ends in the current year.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``dst_start_day`` (int32):  [Read-Write] Set the Date at which DST starts in the current year.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``dst_start_month`` (int32):  [Read-Write] Set the Date at which DST starts in the current year.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``dst_switch_hour`` (int32):  [Read-Write] Hour of the DST Switch for both beginning and end.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``elevation`` (double):  [Read-Write] The current sun elevation in degrees above the horizontal, as viewed from
  the Georeference origin.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``georeference`` (CesiumGeoreference):  [Read-Write] THIS PROPERTY IS DEPRECATED.

  Get the Georeference instance from the Globe Anchor Component instead.
  deprecated: Get the Georeference instance from the Globe Anchor Component instead.
- ``globe_anchor`` (CesiumGlobeAnchorComponent):  [Read-Write] The Globe Anchor Component that precisely ties this Actor to the Globe.
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``inscribed_ground_threshold`` (double):  [Read-Write] When the player pawn is below this height, which is expressed in kilometers
  above the ellipsoid, this Actor will use an atmosphere ground radius that
  is calculated to be at or below the terrain surface at the player pawn's
  current location. This avoids a gap between the bottom of the atmosphere
  and the top of the terrain when zoomed in close to the terrain surface.

  Above CircumscribedGroundThreshold, this Actor will use an atmosphere
  ground radius that is guaranteed to be above the terrain surface anywhere
  on Earth. This avoids artifacts caused by terrain poking through the
  atmosphere when viewing the Earth from far away.

  At player pawn heights in between InscribedGroundThreshold and
  CircumscribedGroundThreshold, this Actor uses a linear interpolation
  between the two ground radii.

  This value is automatically scaled according to the CesiumGeoreference
  Scale and the Actor scale.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``level_directional_light`` (DirectionalLight):  [Read-Write] Reference to a manually assigned Directional Light in the level.
- ``mie_exponential_distribution`` (float):  [Read-Write] The altitude in kilometers at which Mie effects are reduced to 40%. This
  value is automatically scaled according to the CesiumGeoreference Scale and
  the Actor scale.
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``mobile_directional_light_intensity`` (double):  [Read-Write] Default intensity of directional light that's spawned for mobile rendering.
- ``month`` (int32):  [Read-Write] The month of the year, where 1 is January and 12 is December.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``net_cull_distance_squared`` (float):  [Read-Write]
- ``net_dormancy`` (NetDormancy):  [Read-Write] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.
- ``net_load_on_client`` (bool):  [Read-Write] This actor will be loaded on network clients during map load
- ``net_priority`` (float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate
- ``net_update_frequency`` (float):  [Read-Write]
- ``net_use_owner_relevancy`` (bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority
- ``north_offset`` (double):  [Read-Write] Offset in the sun's position. Should be set to -90 for the sun's position
  to be accurate in the Unreal reference frame.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
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
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``rayleigh_exponential_distribution`` (float):  [Read-Write] The altitude in kilometers at which Rayleigh scattering effect is reduced
  to 40%. This value is automatically scaled according to the
  CesiumGeoreference Scale and the Actor scale.
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
- ``scene`` (SceneComponent):  [Read-Write]
- ``sky_atmosphere`` (SkyAtmosphereComponent):  [Read-Write]
- ``sky_light`` (SkyLightComponent):  [Read-Write]
- ``sky_sphere_actor`` (Actor):  [Read-Only] Reference to BP_Sky_Sphere or similar actor (mobile only)
- ``sky_sphere_class`` (type(Class)):  [Read-Write] Mobile platforms currently do not support the SkyAtmosphereComponent.
  In lieu of that, use the engine BP_Sky_Sphere class, or a derived class.
- ``solar_time`` (double):  [Read-Write] The current solar time represented as hours from midnight.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``time_zone`` (double):  [Read-Write] Gets the time zone, represented as hours offset from GMT.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``update_atmosphere_at_runtime`` (bool):  [Read-Write] Updates the atmosphere automatically given current player pawn's longitude,
  latitude, and height. Fixes artifacts seen with the atmosphere rendering
  when flying high above the surface, or low to the ground in high latitudes.
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
- ``use_daylight_saving_time`` (bool):  [Read-Write] Enables adjustment of the Solar Time for Daylight Saving Time (DST).

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.
- ``use_level_directional_light`` (bool):  [Read-Write] False: Use Directional Light component inside CesiumSunSky.
  True: Use the assigned Directional Light in the level.
- ``use_mobile_rendering`` (bool):  [Read-Write] A switch to toggle between desktop and mobile rendering code paths.
  This will NOT be automatically set when running on mobile, so make sure
  to check this setting before building on mobile platforms.
- ``year`` (int32):  [Read-Write] The year.

  After changing this value from Blueprints or C++, you must call UpdateSun
  for it to take effect.

<a id="unreal.CesiumSunSky.scene"></a>

#### scene

```python
@property
def scene() -> SceneComponent
```

(SceneComponent):  [Read-Only]

<a id="unreal.CesiumSunSky.sky_light"></a>

#### sky\_light

```python
@property
def sky_light() -> SkyLightComponent
```

(SkyLightComponent):  [Read-Only]

<a id="unreal.CesiumSunSky.directional_light"></a>

#### directional\_light

```python
@property
def directional_light() -> DirectionalLightComponent
```

(DirectionalLightComponent):  [Read-Only]

<a id="unreal.CesiumSunSky.sky_atmosphere"></a>

#### sky\_atmosphere

```python
@property
def sky_atmosphere() -> SkyAtmosphereComponent
```

(SkyAtmosphereComponent):  [Read-Only]

<a id="unreal.CesiumSunSky.globe_anchor"></a>

#### globe\_anchor

```python
@property
def globe_anchor() -> CesiumGlobeAnchorComponent
```

(CesiumGlobeAnchorComponent):  [Read-Only] The Globe Anchor Component that precisely ties this Actor to the Globe.

<a id="unreal.CesiumSunSky.time_zone"></a>

#### time\_zone

```python
@property
def time_zone() -> float
```

(double):  [Read-Write] Gets the time zone, represented as hours offset from GMT.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.time_zone"></a>

#### time\_zone

```python
@time_zone.setter
def time_zone(value: float) -> None
```

<a id="unreal.CesiumSunSky.solar_time"></a>

#### solar\_time

```python
@property
def solar_time() -> float
```

(double):  [Read-Write] The current solar time represented as hours from midnight.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.solar_time"></a>

#### solar\_time

```python
@solar_time.setter
def solar_time(value: float) -> None
```

<a id="unreal.CesiumSunSky.day"></a>

#### day

```python
@property
def day() -> int
```

(int32):  [Read-Write] The day of the month.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.day"></a>

#### day

```python
@day.setter
def day(value: int) -> None
```

<a id="unreal.CesiumSunSky.month"></a>

#### month

```python
@property
def month() -> int
```

(int32):  [Read-Write] The month of the year, where 1 is January and 12 is December.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.month"></a>

#### month

```python
@month.setter
def month(value: int) -> None
```

<a id="unreal.CesiumSunSky.year"></a>

#### year

```python
@property
def year() -> int
```

(int32):  [Read-Write] The year.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.year"></a>

#### year

```python
@year.setter
def year(value: int) -> None
```

<a id="unreal.CesiumSunSky.north_offset"></a>

#### north\_offset

```python
@property
def north_offset() -> float
```

(double):  [Read-Write] Offset in the sun's position. Should be set to -90 for the sun's position
to be accurate in the Unreal reference frame.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.north_offset"></a>

#### north\_offset

```python
@north_offset.setter
def north_offset(value: float) -> None
```

<a id="unreal.CesiumSunSky.use_daylight_saving_time"></a>

#### use\_daylight\_saving\_time

```python
@property
def use_daylight_saving_time() -> bool
```

(bool):  [Read-Write] Enables adjustment of the Solar Time for Daylight Saving Time (DST).

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.use_daylight_saving_time"></a>

#### use\_daylight\_saving\_time

```python
@use_daylight_saving_time.setter
def use_daylight_saving_time(value: bool) -> None
```

<a id="unreal.CesiumSunSky.georeference"></a>

#### georeference

```python
@property
def georeference() -> CesiumGeoreference
```

(CesiumGeoreference):  [Read-Only] THIS PROPERTY IS DEPRECATED.

Get the Georeference instance from the Globe Anchor Component instead.
deprecated: Get the Georeference instance from the Globe Anchor Component instead.

<a id="unreal.CesiumSunSky.dst_start_month"></a>

#### dst\_start\_month

```python
@property
def dst_start_month() -> int
```

(int32):  [Read-Write] Set the Date at which DST starts in the current year.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.dst_start_month"></a>

#### dst\_start\_month

```python
@dst_start_month.setter
def dst_start_month(value: int) -> None
```

<a id="unreal.CesiumSunSky.dst_start_day"></a>

#### dst\_start\_day

```python
@property
def dst_start_day() -> int
```

(int32):  [Read-Write] Set the Date at which DST starts in the current year.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.dst_start_day"></a>

#### dst\_start\_day

```python
@dst_start_day.setter
def dst_start_day(value: int) -> None
```

<a id="unreal.CesiumSunSky.dst_end_month"></a>

#### dst\_end\_month

```python
@property
def dst_end_month() -> int
```

(int32):  [Read-Write] Set the Date at which DST ends in the current year.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.dst_end_month"></a>

#### dst\_end\_month

```python
@dst_end_month.setter
def dst_end_month(value: int) -> None
```

<a id="unreal.CesiumSunSky.dst_end_day"></a>

#### dst\_end\_day

```python
@property
def dst_end_day() -> int
```

(int32):  [Read-Write] Set the Date at which DST ends in the current year.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.dst_end_day"></a>

#### dst\_end\_day

```python
@dst_end_day.setter
def dst_end_day(value: int) -> None
```

<a id="unreal.CesiumSunSky.dst_switch_hour"></a>

#### dst\_switch\_hour

```python
@property
def dst_switch_hour() -> int
```

(int32):  [Read-Write] Hour of the DST Switch for both beginning and end.

After changing this value from Blueprints or C++, you must call UpdateSun
for it to take effect.

<a id="unreal.CesiumSunSky.dst_switch_hour"></a>

#### dst\_switch\_hour

```python
@dst_switch_hour.setter
def dst_switch_hour(value: int) -> None
```

<a id="unreal.CesiumSunSky.update_atmosphere_at_runtime"></a>

#### update\_atmosphere\_at\_runtime

```python
@property
def update_atmosphere_at_runtime() -> bool
```

(bool):  [Read-Write] Updates the atmosphere automatically given current player pawn's longitude,
latitude, and height. Fixes artifacts seen with the atmosphere rendering
when flying high above the surface, or low to the ground in high latitudes.

<a id="unreal.CesiumSunSky.update_atmosphere_at_runtime"></a>

#### update\_atmosphere\_at\_runtime

```python
@update_atmosphere_at_runtime.setter
def update_atmosphere_at_runtime(value: bool) -> None
```

<a id="unreal.CesiumSunSky.inscribed_ground_threshold"></a>

#### inscribed\_ground\_threshold

```python
@property
def inscribed_ground_threshold() -> float
```

(double):  [Read-Write] When the player pawn is below this height, which is expressed in kilometers
above the ellipsoid, this Actor will use an atmosphere ground radius that
is calculated to be at or below the terrain surface at the player pawn's
current location. This avoids a gap between the bottom of the atmosphere
and the top of the terrain when zoomed in close to the terrain surface.

Above CircumscribedGroundThreshold, this Actor will use an atmosphere
ground radius that is guaranteed to be above the terrain surface anywhere
on Earth. This avoids artifacts caused by terrain poking through the
atmosphere when viewing the Earth from far away.

At player pawn heights in between InscribedGroundThreshold and
CircumscribedGroundThreshold, this Actor uses a linear interpolation
between the two ground radii.

This value is automatically scaled according to the CesiumGeoreference
Scale and the Actor scale.

<a id="unreal.CesiumSunSky.inscribed_ground_threshold"></a>

#### inscribed\_ground\_threshold

```python
@inscribed_ground_threshold.setter
def inscribed_ground_threshold(value: float) -> None
```

<a id="unreal.CesiumSunSky.circumscribed_ground_threshold"></a>

#### circumscribed\_ground\_threshold

```python
@property
def circumscribed_ground_threshold() -> float
```

(double):  [Read-Write] When the player pawn is above this height, which is expressed in kilometers
above the ellipsoid, this Actor will use an atmosphere ground radius that
is guaranteed to be above the terrain surface anywhere on Earth. This
avoids artifacts caused by terrain poking through the atmosphere when
viewing the Earth from far away.

Below InscribedGroundThreshold, this Actor will use an atmosphere
ground radius that is calculated to be at or below the terrain surface at
the player pawn's current location. This avoids a gap between the bottom of
the atmosphere and the top of the terrain when zoomed in close to the
terrain surface.

At heights in between InscribedGroundThreshold and
CircumscribedGroundThreshold, this Actor uses a linear interpolation
between the two ground radii.

This value is automatically scaled according to the CesiumGeoreference
Scale and the Actor scale.

<a id="unreal.CesiumSunSky.circumscribed_ground_threshold"></a>

#### circumscribed\_ground\_threshold

```python
@circumscribed_ground_threshold.setter
def circumscribed_ground_threshold(value: float) -> None
```

<a id="unreal.CesiumSunSky.circumscribed_ground_height"></a>

#### circumscribed\_ground\_height

```python
@property
def circumscribed_ground_height() -> float
```

(double):  [Read-Write] The height at which to place the bottom of the atmosphere when the player
pawn is above the CircumscribedGroundThreshold. This is expressed as a
height in kilometers above the maximum radius of the ellipsoid (usually
WGS84). To avoid dark splotchy artifacts in the atmosphere when zoomed out
far from the globe, this value must be above the greatest height achieved
by any part of the tileset.

<a id="unreal.CesiumSunSky.circumscribed_ground_height"></a>

#### circumscribed\_ground\_height

```python
@circumscribed_ground_height.setter
def circumscribed_ground_height(value: float) -> None
```

<a id="unreal.CesiumSunSky.atmosphere_height"></a>

#### atmosphere\_height

```python
@property
def atmosphere_height() -> float
```

(float):  [Read-Only] The height of the atmosphere layer above the ground, in kilometers. This
value is automatically scaled according to the CesiumGeoreference Scale and
the Actor scale. However, Unreal Engine's SkyAtmosphere has a hard-coded
minimum effective value of 0.1, so the atmosphere will look too thick when
the globe is scaled down drastically.

<a id="unreal.CesiumSunSky.aerial_perspective_view_distance_scale"></a>

#### aerial\_perspective\_view\_distance\_scale

```python
@property
def aerial_perspective_view_distance_scale() -> float
```

(float):  [Read-Only] Makes the aerial perspective look thicker by scaling distances from view
to surfaces (opaque and translucent). This value is automatically scaled
according to the CesiumGeoreference Scale and the Actor scale.

<a id="unreal.CesiumSunSky.rayleigh_exponential_distribution"></a>

#### rayleigh\_exponential\_distribution

```python
@property
def rayleigh_exponential_distribution() -> float
```

(float):  [Read-Only] The altitude in kilometers at which Rayleigh scattering effect is reduced
to 40%. This value is automatically scaled according to the
CesiumGeoreference Scale and the Actor scale.

<a id="unreal.CesiumSunSky.mie_exponential_distribution"></a>

#### mie\_exponential\_distribution

```python
@property
def mie_exponential_distribution() -> float
```

(float):  [Read-Only] The altitude in kilometers at which Mie effects are reduced to 40%. This
value is automatically scaled according to the CesiumGeoreference Scale and
the Actor scale.

<a id="unreal.CesiumSunSky.use_level_directional_light"></a>

#### use\_level\_directional\_light

```python
@property
def use_level_directional_light() -> bool
```

(bool):  [Read-Write] False: Use Directional Light component inside CesiumSunSky.
True: Use the assigned Directional Light in the level.

<a id="unreal.CesiumSunSky.use_level_directional_light"></a>

#### use\_level\_directional\_light

```python
@use_level_directional_light.setter
def use_level_directional_light(value: bool) -> None
```

<a id="unreal.CesiumSunSky.level_directional_light"></a>

#### level\_directional\_light

```python
@property
def level_directional_light() -> DirectionalLight
```

(DirectionalLight):  [Read-Write] Reference to a manually assigned Directional Light in the level.

<a id="unreal.CesiumSunSky.level_directional_light"></a>

#### level\_directional\_light

```python
@level_directional_light.setter
def level_directional_light(value: DirectionalLight) -> None
```

<a id="unreal.CesiumSunSky.elevation"></a>

#### elevation

```python
@property
def elevation() -> float
```

(double):  [Read-Only] The current sun elevation in degrees above the horizontal, as viewed from
the Georeference origin.

<a id="unreal.CesiumSunSky.corrected_elevation"></a>

#### corrected\_elevation

```python
@property
def corrected_elevation() -> float
```

(double):  [Read-Only] The current sun elevation, corrected for atmospheric diffraction, in
degrees above the horizontal, as viewed from the Georeference origin.

<a id="unreal.CesiumSunSky.azimuth"></a>

#### azimuth

```python
@property
def azimuth() -> float
```

(double):  [Read-Only] The current sun azimuth in degrees clockwise from North toward East, as
viewed from the Georeference origin.

<a id="unreal.CesiumSunSky.use_mobile_rendering"></a>

#### use\_mobile\_rendering

```python
@property
def use_mobile_rendering() -> bool
```

(bool):  [Read-Only] A switch to toggle between desktop and mobile rendering code paths.
This will NOT be automatically set when running on mobile, so make sure
to check this setting before building on mobile platforms.

<a id="unreal.CesiumSunSky.enable_mobile_rendering"></a>

#### enable\_mobile\_rendering

```python
@property
def enable_mobile_rendering() -> bool
```

deprecated: 'enable_mobile_rendering' was renamed to 'use_mobile_rendering'.

<a id="unreal.CesiumSunSky.sky_sphere_class"></a>

#### sky\_sphere\_class

```python
@property
def sky_sphere_class() -> Class
```

(type(Class)):  [Read-Write] Mobile platforms currently do not support the SkyAtmosphereComponent.
In lieu of that, use the engine BP_Sky_Sphere class, or a derived class.

<a id="unreal.CesiumSunSky.sky_sphere_class"></a>

#### sky\_sphere\_class

```python
@sky_sphere_class.setter
def sky_sphere_class(value: Class) -> None
```

<a id="unreal.CesiumSunSky.sky_sphere_actor"></a>

#### sky\_sphere\_actor

```python
@property
def sky_sphere_actor() -> Actor
```

(Actor):  [Read-Only] Reference to BP_Sky_Sphere or similar actor (mobile only)

<a id="unreal.CesiumSunSky.mobile_directional_light_intensity"></a>

#### mobile\_directional\_light\_intensity

```python
@property
def mobile_directional_light_intensity() -> float
```

(double):  [Read-Only] Default intensity of directional light that's spawned for mobile rendering.

<a id="unreal.CesiumSunSky.update_sun"></a>

#### update\_sun

```python
def update_sun() -> None
```

x.update_sun() -> None
Update Sun

<a id="unreal.CesiumSunSky.update_sky_sphere"></a>

#### update\_sky\_sphere

```python
def update_sky_sphere() -> None
```

x.update_sky_sphere() -> None
Update MobileSkySphere by calling its RefreshMaterial function

<a id="unreal.CesiumSunSky.update_atmosphere_radius"></a>

#### update\_atmosphere\_radius

```python
def update_atmosphere_radius() -> None
```

x.update_atmosphere_radius() -> None
Update Atmosphere Radius

<a id="unreal.CesiumSunSky.adjust_atmosphere_radius"></a>

#### adjust\_atmosphere\_radius

```python
def adjust_atmosphere_radius() -> None
```

deprecated: 'adjust_atmosphere_radius' was renamed to 'update_atmosphere_radius'.

<a id="unreal.CesiumSunSky.set_sky_atmosphere_ground_radius"></a>

#### set\_sky\_atmosphere\_ground\_radius

```python
def set_sky_atmosphere_ground_radius(sky: SkyAtmosphereComponent,
                                     radius: float) -> None
```

x.set_sky_atmosphere_ground_radius(sky, radius) -> None
Modifies the sky atmosphere's ground radius, which represents the Earth's
radius in the SkyAtmosphere rendering model. Only changes if there's a >0.1
difference, to reduce redraws.

Args:
    sky (SkyAtmosphereComponent): A pointer to the SkyAtmosphereComponent
    radius (double): The radius in kilometers.

<a id="unreal.CesiumSunSky.is_dst"></a>

#### is\_dst

```python
def is_dst(dst_enable: bool, dst_start_month: int, dst_start_day: int,
           dst_end_month: int, dst_end_day: int, dst_switch_hour: int) -> bool
```

x.is_dst(dst_enable, dst_start_month, dst_start_day, dst_end_month, dst_end_day, dst_switch_hour) -> bool
Check whether the current time and date (based on this class instance's
properties) falls within Daylight Savings Time. Copied the implementation
from the engine SunSkyBP class.

Args:
    dst_enable (bool): 
    dst_start_month (int32): 
    dst_start_day (int32): 
    dst_end_month (int32): 
    dst_end_day (int32): 
    dst_switch_hour (int32): 

Returns:
    bool:

<a id="unreal.CesiumSunSky.get_hms_from_solar_time"></a>

#### get\_hms\_from\_solar\_time

```python
@classmethod
def get_hms_from_solar_time(cls, solar_time: float) -> Tuple[int, int, int]
```

X.get_hms_from_solar_time(solar_time) -> (hour=int32, minute=int32, second=int32)
Convert solar time to Hours:Minutes:Seconds. Copied the implementation
from the engine SunSkyBP class.

Args:
    solar_time (double): 

Returns:
    tuple: 

    hour (int32): 

    minute (int32): 

    second (int32):

<a id="unreal.CesiumSunSky_C"></a>