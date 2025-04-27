## LandmassActor Objects

```python
class LandmassActor(Actor)
```

Landmass Actor

**C++ Source:**

- **Plugin**: Landmass
- **Module**: LandmassEditor
- **File**: LandmassActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``affects_heightmap`` (bool):  [Read-Write]
- ``affects_visibility`` (bool):  [Read-Write]
- ``affects_weightmaps`` (bool):  [Read-Write]
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``brush_extents`` (Vector4):  [Read-Write]
- ``brush_manager`` (LandmassManagerBase):  [Read-Write]
- ``brush_render_parameters`` (LandscapeBrushParameters):  [Read-Write]
- ``brush_size`` (float):  [Read-Write]
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
- ``draw_to_entire_landscape`` (bool):  [Read-Write]
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``extents_preview_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``height_blend_mode`` (BrushBlendMode):  [Read-Write]
- ``height_material`` (MaterialInterface):  [Read-Write]
- ``heightmap_render_mid`` (MaterialInstanceDynamic):  [Read-Write]
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
- ``on_brush_updated`` (OnBrushUpdatedDelegate):  [Read-Write]
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
- ``weight_map_blend_mode`` (BrushBlendMode):  [Read-Write]
- ``weightmap_layers`` (Array[Name]):  [Read-Write]
- ``weightmap_material`` (MaterialInterface):  [Read-Write]
- ``weightmap_render_mid`` (MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.LandmassActor.brush_size"></a>

#### brush_size

```python
@property
def brush_size() -> float
```

(float):  [Read-Write]

<a id="unreal.LandmassActor.brush_size"></a>

#### brush_size

```python
@brush_size.setter
def brush_size(value: float) -> None
```

<a id="unreal.LandmassActor.draw_to_entire_landscape"></a>

#### draw_to_entire_landscape

```python
@property
def draw_to_entire_landscape() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LandmassActor.draw_to_entire_landscape"></a>

#### draw_to_entire_landscape

```python
@draw_to_entire_landscape.setter
def draw_to_entire_landscape(value: bool) -> None
```

<a id="unreal.LandmassActor.affects_heightmap"></a>

#### affects_heightmap

```python
@property
def affects_heightmap() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LandmassActor.affects_heightmap"></a>

#### affects_heightmap

```python
@affects_heightmap.setter
def affects_heightmap(value: bool) -> None
```

<a id="unreal.LandmassActor.affects_weightmaps"></a>

#### affects_weightmaps

```python
@property
def affects_weightmaps() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LandmassActor.affects_weightmaps"></a>

#### affects_weightmaps

```python
@affects_weightmaps.setter
def affects_weightmaps(value: bool) -> None
```

<a id="unreal.LandmassActor.affects_visibility"></a>

#### affects_visibility

```python
@property
def affects_visibility() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LandmassActor.affects_visibility"></a>

#### affects_visibility

```python
@affects_visibility.setter
def affects_visibility(value: bool) -> None
```

<a id="unreal.LandmassActor.height_blend_mode"></a>

#### height_blend_mode

```python
@property
def height_blend_mode() -> BrushBlendMode
```

(BrushBlendMode):  [Read-Write]

<a id="unreal.LandmassActor.height_blend_mode"></a>

#### height_blend_mode

```python
@height_blend_mode.setter
def height_blend_mode(value: BrushBlendMode) -> None
```

<a id="unreal.LandmassActor.height_material"></a>

#### height_material

```python
@property
def height_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.LandmassActor.height_material"></a>

#### height_material

```python
@height_material.setter
def height_material(value: MaterialInterface) -> None
```

<a id="unreal.LandmassActor.weight_map_blend_mode"></a>

#### weight_map_blend_mode

```python
@property
def weight_map_blend_mode() -> BrushBlendMode
```

(BrushBlendMode):  [Read-Write]

<a id="unreal.LandmassActor.weight_map_blend_mode"></a>

#### weight_map_blend_mode

```python
@weight_map_blend_mode.setter
def weight_map_blend_mode(value: BrushBlendMode) -> None
```

<a id="unreal.LandmassActor.weightmap_material"></a>

#### weightmap_material

```python
@property
def weightmap_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.LandmassActor.weightmap_material"></a>

#### weightmap_material

```python
@weightmap_material.setter
def weightmap_material(value: MaterialInterface) -> None
```

<a id="unreal.LandmassActor.brush_extents"></a>

#### brush_extents

```python
@property
def brush_extents() -> Vector4
```

(Vector4):  [Read-Only]

<a id="unreal.LandmassActor.weightmap_layers"></a>

#### weightmap_layers

```python
@property
def weightmap_layers() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.LandmassActor.weightmap_layers"></a>

#### weightmap_layers

```python
@weightmap_layers.setter
def weightmap_layers(value: Array[Name]) -> None
```

<a id="unreal.LandmassActor.brush_render_parameters"></a>

#### brush_render_parameters

```python
@property
def brush_render_parameters() -> LandscapeBrushParameters
```

(LandscapeBrushParameters):  [Read-Write]

<a id="unreal.LandmassActor.brush_render_parameters"></a>

#### brush_render_parameters

```python
@brush_render_parameters.setter
def brush_render_parameters(value: LandscapeBrushParameters) -> None
```

<a id="unreal.LandmassActor.brush_manager"></a>

#### brush_manager

```python
@property
def brush_manager() -> LandmassManagerBase
```

(LandmassManagerBase):  [Read-Write]

<a id="unreal.LandmassActor.brush_manager"></a>

#### brush_manager

```python
@brush_manager.setter
def brush_manager(value: LandmassManagerBase) -> None
```

<a id="unreal.LandmassActor.on_brush_updated"></a>

#### on_brush_updated

```python
@property
def on_brush_updated() -> OnBrushUpdatedDelegate
```

(OnBrushUpdatedDelegate):  [Read-Write]

<a id="unreal.LandmassActor.on_brush_updated"></a>

#### on_brush_updated

```python
@on_brush_updated.setter
def on_brush_updated(value: OnBrushUpdatedDelegate) -> None
```

<a id="unreal.LandmassActor.extents_preview_mid"></a>

#### extents_preview_mid

```python
@property
def extents_preview_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.LandmassActor.extents_preview_mid"></a>

#### extents_preview_mid

```python
@extents_preview_mid.setter
def extents_preview_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.LandmassActor.heightmap_render_mid"></a>

#### heightmap_render_mid

```python
@property
def heightmap_render_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.LandmassActor.heightmap_render_mid"></a>

#### heightmap_render_mid

```python
@heightmap_render_mid.setter
def heightmap_render_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.LandmassActor.weightmap_render_mid"></a>

#### weightmap_render_mid

```python
@property
def weightmap_render_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.LandmassActor.weightmap_render_mid"></a>

#### weightmap_render_mid

```python
@weightmap_render_mid.setter
def weightmap_render_mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.LandmassActor.update_brush_extents"></a>

#### update_brush_extents

```python
def update_brush_extents() -> None
```

x.update_brush_extents() -> None
Update Brush Extents

<a id="unreal.LandmassActor.set_mesh_exents_material"></a>

#### set_mesh_exents_material

```python
def set_mesh_exents_material(material: MaterialInterface) -> None
```

x.set_mesh_exents_material(material) -> None
Set Mesh Exents Material

Args:
    material (MaterialInterface):

<a id="unreal.LandmassActor.set_editor_tick_enabled"></a>

#### set_editor_tick_enabled

```python
def set_editor_tick_enabled(enabled: bool) -> None
```

x.set_editor_tick_enabled(enabled) -> None
Set Editor Tick Enabled

Args:
    enabled (bool):

<a id="unreal.LandmassActor.restore_landscape_editing"></a>

#### restore_landscape_editing

```python
def restore_landscape_editing() -> None
```

x.restore_landscape_editing() -> None
Restore Landscape Editing

<a id="unreal.LandmassActor.render_layer_native"></a>

#### render_layer_native

```python
def render_layer_native(parameters: LandscapeBrushParameters) -> None
```

x.render_layer_native(parameters) -> None
Render Layer Native

Args:
    parameters (LandscapeBrushParameters):

<a id="unreal.LandmassActor.render_layer"></a>

#### render_layer

```python
def render_layer(parameters: LandscapeBrushParameters) -> None
```

x.render_layer(parameters) -> None
Render Layer

Args:
    parameters (LandscapeBrushParameters):

<a id="unreal.LandmassActor.move_to_top"></a>

#### move_to_top

```python
def move_to_top() -> None
```

x.move_to_top() -> None
Move to Top

<a id="unreal.LandmassActor.move_to_bottom"></a>

#### move_to_bottom

```python
def move_to_bottom() -> None
```

x.move_to_bottom() -> None
Move to Bottom

<a id="unreal.LandmassActor.move_brush_up"></a>

#### move_brush_up

```python
def move_brush_up() -> None
```

x.move_brush_up() -> None
Move Brush Up

<a id="unreal.LandmassActor.move_brush_down"></a>

#### move_brush_down

```python
def move_brush_down() -> None
```

x.move_brush_down() -> None
Move Brush Down

<a id="unreal.LandmassActor.fast_preview_mode"></a>

#### fast_preview_mode

```python
def fast_preview_mode() -> None
```

x.fast_preview_mode() -> None
Fast Preview Mode

<a id="unreal.LandmassActor.draw_brush_material"></a>

#### draw_brush_material

```python
def draw_brush_material(material: MaterialInterface) -> None
```

x.draw_brush_material(material) -> None
Draw Brush Material

Args:
    material (MaterialInterface):

<a id="unreal.LandmassActor.custom_tick"></a>

#### custom_tick

```python
def custom_tick(delta_seconds: float) -> None
```

x.custom_tick(delta_seconds) -> None
Custom Tick

Args:
    delta_seconds (float):

<a id="unreal.LandmassActor.actor_selection_changed"></a>

#### actor_selection_changed

```python
def actor_selection_changed(selected: bool) -> None
```

x.actor_selection_changed(selected) -> None
Actor Selection Changed

Args:
    selected (bool):

<a id="unreal.LandmassBlueprintFunctionLibrary"></a>