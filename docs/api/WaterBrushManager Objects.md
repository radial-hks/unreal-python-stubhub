## WaterBrushManager Objects

```python
class WaterBrushManager(WaterLandscapeBrush)
```

Water Brush Manager

**C++ Source:**

- **Plugin**: Water
- **Module**: WaterEditor
- **File**: WaterBrushManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``affect_heightmap`` (bool):  [Read-Write]
- ``affect_visibility_layer`` (bool):  [Read-Write]
- ``affect_weightmap`` (bool):  [Read-Write]
- ``affected_weightmap_layers`` (Array[Name]):  [Read-Write]
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``blur_edges_material`` (MaterialInterface):  [Read-Write]
- ``brush_angle_falloff_material`` (MaterialInterface):  [Read-Write] Brush materials
- ``brush_angle_falloff_mid`` (MaterialInstanceDynamic):  [Read-Write] MIDs
- ``brush_curve_rt_cache`` (Map[CurveFloat, WaterBodyBrushCache]):  [Read-Only] MIDs End
- ``brush_width_falloff_material`` (MaterialInterface):  [Read-Write]
- ``brush_width_falloff_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``cache`` (Map[Actor, Object]):  [Read-Only]
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``canvas_segment_size`` (float):  [Read-Write]
- ``combined_velocity_and_height_rta`` (TextureRenderTarget2D):  [Read-Only]
- ``combined_velocity_and_height_rtb`` (TextureRenderTarget2D):  [Read-Only]
- ``composite_water_body_texture_material`` (MaterialInterface):  [Read-Write]
- ``composite_water_body_texture_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``debug_distance_field_material`` (MaterialInterface):  [Read-Write] TODO [jonathan.bard] : rename to DebugDistanceFieldMaterial and make it work :
- ``debug_distance_field_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``depth_and_shape_rt`` (TextureRenderTarget2D):  [Read-Only]
- ``disable_brush_texture_effects`` (bool):  [Read-Write]
- ``distance_divisor`` (float):  [Read-Write]
- ``distance_field_cache_material`` (MaterialInterface):  [Read-Write]
- ``distance_field_cache_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``draw_canvas_material`` (MaterialInterface):  [Read-Write]
- ``draw_canvas_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``find_edges_material`` (MaterialInterface):  [Read-Write]
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``heightmap_rta`` (TextureRenderTarget2D):  [Read-Only] RTs
- ``heightmap_rtb`` (TextureRenderTarget2D):  [Read-Only]
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
- ``island_falloff_material`` (MaterialInterface):  [Read-Write]
- ``island_falloff_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``jump_flood_rta`` (TextureRenderTarget2D):  [Read-Only]
- ``jump_flood_rtb`` (TextureRenderTarget2D):  [Read-Only]
- ``jump_step_material`` (MaterialInterface):  [Read-Write]
- ``landscape_quads`` (IntPoint):  [Read-Only]
- ``landscape_rt_ref`` (TextureRenderTarget2D):  [Read-Only]
- ``landscape_rt_res`` (IntPoint):  [Read-Only]
- ``landscape_transform`` (Transform):  [Read-Only]
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
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``relevant_for_level_bounds`` (bool):  [Read-Write] If true, this actor's component's bounds will be included in the level's
  bounding box unless the Actor's class has overridden IsLevelBoundsRelevant
- ``remote_role`` (NetRole):  [Read-Only] Describes how much control the remote machine has over the actor.
- ``render_river_spline_depth_material`` (MaterialInterface):  [Read-Write]
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
- ``river_spline_mi_ds`` (Array[MaterialInstanceDynamic]):  [Read-Write]
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``show_distance`` (bool):  [Read-Write]
- ``show_gradient`` (bool):  [Read-Write]
- ``show_grid`` (bool):  [Read-Write]
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``spline_mesh_extension`` (float):  [Read-Write]
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``update_on_property_change`` (bool):  [Read-Write]
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
- ``use_dynamic_preview_rt`` (bool):  [Read-Write]
- ``water_clear_height`` (float):  [Read-Write]
- ``water_depth_and_velocity_rt`` (TextureRenderTarget2D):  [Read-Only]
- ``weightmap_material`` (MaterialInterface):  [Read-Write]
- ``weightmap_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``weightmap_rta`` (TextureRenderTarget2D):  [Read-Only]
- ``weightmap_rtb`` (TextureRenderTarget2D):  [Read-Only]
- ``world_size`` (Vector):  [Read-Only]

<a id="unreal.WaterBrushManager.brush_angle_falloff_material"></a>

#### brush_angle_falloff_material

```python
@property
def brush_angle_falloff_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] Brush materials

<a id="unreal.WaterBrushManager.brush_angle_falloff_material"></a>

#### brush_angle_falloff_material

```python
@brush_angle_falloff_material.setter
def brush_angle_falloff_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.brush_width_falloff_material"></a>

#### brush_width_falloff_material

```python
@property
def brush_width_falloff_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.brush_width_falloff_material"></a>

#### brush_width_falloff_material

```python
@brush_width_falloff_material.setter
def brush_width_falloff_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.distance_field_cache_material"></a>

#### distance_field_cache_material

```python
@property
def distance_field_cache_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.distance_field_cache_material"></a>

#### distance_field_cache_material

```python
@distance_field_cache_material.setter
def distance_field_cache_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.render_river_spline_depth_material"></a>

#### render_river_spline_depth_material

```python
@property
def render_river_spline_depth_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.render_river_spline_depth_material"></a>

#### render_river_spline_depth_material

```python
@render_river_spline_depth_material.setter
def render_river_spline_depth_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.debug_distance_field_material"></a>

#### debug_distance_field_material

```python
@property
def debug_distance_field_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] TODO [jonathan.bard] : rename to DebugDistanceFieldMaterial and make it work :

<a id="unreal.WaterBrushManager.debug_distance_field_material"></a>

#### debug_distance_field_material

```python
@debug_distance_field_material.setter
def debug_distance_field_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.weightmap_material"></a>

#### weightmap_material

```python
@property
def weightmap_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.weightmap_material"></a>

#### weightmap_material

```python
@weightmap_material.setter
def weightmap_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.draw_canvas_material"></a>

#### draw_canvas_material

```python
@property
def draw_canvas_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.draw_canvas_material"></a>

#### draw_canvas_material

```python
@draw_canvas_material.setter
def draw_canvas_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.composite_water_body_texture_material"></a>

#### composite_water_body_texture_material

```python
@property
def composite_water_body_texture_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.composite_water_body_texture_material"></a>

#### composite_water_body_texture_material

```python
@composite_water_body_texture_material.setter
def composite_water_body_texture_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.island_falloff_material"></a>

#### island_falloff_material

```python
@property
def island_falloff_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.island_falloff_material"></a>

#### island_falloff_material

```python
@island_falloff_material.setter
def island_falloff_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.jump_step_material"></a>

#### jump_step_material

```python
@property
def jump_step_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.jump_step_material"></a>

#### jump_step_material

```python
@jump_step_material.setter
def jump_step_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.find_edges_material"></a>

#### find_edges_material

```python
@property
def find_edges_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.find_edges_material"></a>

#### find_edges_material

```python
@find_edges_material.setter
def find_edges_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.blur_edges_material"></a>

#### blur_edges_material

```python
@property
def blur_edges_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.WaterBrushManager.blur_edges_material"></a>

#### blur_edges_material

```python
@blur_edges_material.setter
def blur_edges_material(value: MaterialInterface) -> None
```

<a id="unreal.WaterBrushManager.brush_angle_falloff_mid"></a>

#### brush_angle_falloff_mid

```python
@property
def brush_angle_falloff_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write] MIDs

<a id="unreal.WaterBrushManager.brush_angle_falloff_mid"></a>

#### brush_angle_falloff_mid

```python
@brush_angle_falloff_mid.setter
def brush_angle_falloff_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.WaterBrushManager.brush_width_falloff_mid"></a>

#### brush_width_falloff_mid

```python
@property
def brush_width_falloff_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.WaterBrushManager.brush_width_falloff_mid"></a>

#### brush_width_falloff_mid

```python
@brush_width_falloff_mid.setter
def brush_width_falloff_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.WaterBrushManager.distance_field_cache_mid"></a>

#### distance_field_cache_mid

```python
@property
def distance_field_cache_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.WaterBrushManager.distance_field_cache_mid"></a>

#### distance_field_cache_mid

```python
@distance_field_cache_mid.setter
def distance_field_cache_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.WaterBrushManager.river_spline_mi_ds"></a>

#### river_spline_mi_ds

```python
@property
def river_spline_mi_ds() -> Array[MaterialInstanceDynamic]
```

(Array[MaterialInstanceDynamic]):  [Read-Write]

<a id="unreal.WaterBrushManager.river_spline_mi_ds"></a>

#### river_spline_mi_ds

```python
@river_spline_mi_ds.setter
def river_spline_mi_ds(value: Array[MaterialInstanceDynamic]) -> None
```

<a id="unreal.WaterBrushManager.debug_distance_field_mid"></a>

#### debug_distance_field_mid

```python
@property
def debug_distance_field_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.WaterBrushManager.debug_distance_field_mid"></a>

#### debug_distance_field_mid

```python
@debug_distance_field_mid.setter
def debug_distance_field_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.WaterBrushManager.weightmap_mid"></a>

#### weightmap_mid

```python
@property
def weightmap_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.WaterBrushManager.weightmap_mid"></a>

#### weightmap_mid

```python
@weightmap_mid.setter
def weightmap_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.WaterBrushManager.draw_canvas_mid"></a>

#### draw_canvas_mid

```python
@property
def draw_canvas_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.WaterBrushManager.draw_canvas_mid"></a>

#### draw_canvas_mid

```python
@draw_canvas_mid.setter
def draw_canvas_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.WaterBrushManager.composite_water_body_texture_mid"></a>

#### composite_water_body_texture_mid

```python
@property
def composite_water_body_texture_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.WaterBrushManager.composite_water_body_texture_mid"></a>

#### composite_water_body_texture_mid

```python
@composite_water_body_texture_mid.setter
def composite_water_body_texture_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.WaterBrushManager.island_falloff_mid"></a>

#### island_falloff_mid

```python
@property
def island_falloff_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.WaterBrushManager.island_falloff_mid"></a>

#### island_falloff_mid

```python
@island_falloff_mid.setter
def island_falloff_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.WaterBrushManager.brush_curve_rt_cache"></a>

#### brush_curve_rt_cache

```python
@property
def brush_curve_rt_cache() -> Map[CurveFloat, WaterBodyBrushCache]
```

(Map[CurveFloat, WaterBodyBrushCache]):  [Read-Only] MIDs End

<a id="unreal.WaterBrushManager.world_size"></a>

#### world_size

```python
@property
def world_size() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.WaterBrushManager.landscape_rt_res"></a>

#### landscape_rt_res

```python
@property
def landscape_rt_res() -> IntPoint
```

(IntPoint):  [Read-Only]

<a id="unreal.WaterBrushManager.landscape_quads"></a>

#### landscape_quads

```python
@property
def landscape_quads() -> IntPoint
```

(IntPoint):  [Read-Only]

<a id="unreal.WaterBrushManager.landscape_transform"></a>

#### landscape_transform

```python
@property
def landscape_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.WaterBrushManager.show_gradient"></a>

#### show_gradient

```python
@property
def show_gradient() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WaterBrushManager.show_gradient"></a>

#### show_gradient

```python
@show_gradient.setter
def show_gradient(value: bool) -> None
```

<a id="unreal.WaterBrushManager.distance_divisor"></a>

#### distance_divisor

```python
@property
def distance_divisor() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBrushManager.distance_divisor"></a>

#### distance_divisor

```python
@distance_divisor.setter
def distance_divisor(value: float) -> None
```

<a id="unreal.WaterBrushManager.show_distance"></a>

#### show_distance

```python
@property
def show_distance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WaterBrushManager.show_distance"></a>

#### show_distance

```python
@show_distance.setter
def show_distance(value: bool) -> None
```

<a id="unreal.WaterBrushManager.show_grid"></a>

#### show_grid

```python
@property
def show_grid() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WaterBrushManager.show_grid"></a>

#### show_grid

```python
@show_grid.setter
def show_grid(value: bool) -> None
```

<a id="unreal.WaterBrushManager.canvas_segment_size"></a>

#### canvas_segment_size

```python
@property
def canvas_segment_size() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBrushManager.canvas_segment_size"></a>

#### canvas_segment_size

```python
@canvas_segment_size.setter
def canvas_segment_size(value: float) -> None
```

<a id="unreal.WaterBrushManager.water_clear_height"></a>

#### water_clear_height

```python
@property
def water_clear_height() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBrushManager.water_clear_height"></a>

#### water_clear_height

```python
@water_clear_height.setter
def water_clear_height(value: float) -> None
```

<a id="unreal.WaterBrushManager.spline_mesh_extension"></a>

#### spline_mesh_extension

```python
@property
def spline_mesh_extension() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterBrushManager.spline_mesh_extension"></a>

#### spline_mesh_extension

```python
@spline_mesh_extension.setter
def spline_mesh_extension(value: float) -> None
```

<a id="unreal.WaterBrushManager.use_dynamic_preview_rt"></a>

#### use_dynamic_preview_rt

```python
@property
def use_dynamic_preview_rt() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WaterBrushManager.use_dynamic_preview_rt"></a>

#### use_dynamic_preview_rt

```python
@use_dynamic_preview_rt.setter
def use_dynamic_preview_rt(value: bool) -> None
```

<a id="unreal.WaterBrushManager.disable_brush_texture_effects"></a>

#### disable_brush_texture_effects

```python
@property
def disable_brush_texture_effects() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WaterBrushManager.disable_brush_texture_effects"></a>

#### disable_brush_texture_effects

```python
@disable_brush_texture_effects.setter
def disable_brush_texture_effects(value: bool) -> None
```

<a id="unreal.WaterBrushManager.sort_water_bodies_for_brush_render"></a>

#### sort_water_bodies_for_brush_render

```python
def sort_water_bodies_for_brush_render() -> Array[WaterBody]
```

x.sort_water_bodies_for_brush_render() -> Array[WaterBody]
Sorts the water bodies in the order they should be rendered when rendering the water brush

Returns:
    Array[WaterBody]: 

    out_water_bodies (Array[WaterBody]): : list of water bodies that needs sorting

<a id="unreal.WaterBrushManager.single_jump_step"></a>

#### single_jump_step

```python
def single_jump_step() -> None
```

x.single_jump_step() -> None
Single Jump Step

<a id="unreal.WaterBrushManager.single_blur_step"></a>

#### single_blur_step

```python
def single_blur_step() -> None
```

x.single_blur_step() -> None
Single Blur Step

<a id="unreal.WaterBrushManager.setup_default_materials"></a>

#### setup_default_materials

```python
def setup_default_materials() -> None
```

x.setup_default_materials() -> None
Setup Default Materials

<a id="unreal.WaterBrushManager.get_water_cache_key"></a>

#### get_water_cache_key

```python
def get_water_cache_key(
    water_brush: Actor
) -> Tuple[WaterBodyBrushCacheContainer, WaterBodyBrushCache]
```

x.get_water_cache_key(water_brush) -> (container_object=WaterBodyBrushCacheContainer, value=WaterBodyBrushCache)
out

Args:
    water_brush (Actor): 

Returns:
    tuple: 

    container_object (WaterBodyBrushCacheContainer): 

    value (WaterBodyBrushCache):

<a id="unreal.WaterBrushManager.force_update"></a>

#### force_update

```python
def force_update() -> None
```

x.force_update() -> None
Debug Buttons

<a id="unreal.WaterBrushManager.find_edges"></a>

#### find_edges

```python
def find_edges() -> None
```

x.find_edges() -> None
Find Edges

<a id="unreal.WaterWavesAssetFactory"></a>