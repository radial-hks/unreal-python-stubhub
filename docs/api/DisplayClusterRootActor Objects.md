## DisplayClusterRootActor Objects

```python
class DisplayClusterRootActor(Actor)
```

VR root. This contains nDisplay VR hierarchy in the game.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterRootActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``all_viewport_color_configuration_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``basic_display_device_component`` (DisplayClusterDisplayDeviceBaseComponent):  [Read-Only] The included display device nDisplay provides by default
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``cluster_color_grading_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``cluster_hide_list_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``current_config_data`` (DisplayClusterConfigurationData):  [Read-Only] If set from the DisplayCluster BP Compiler it will be loaded from the class default subobjects in run-time.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_display_device_name`` (Name):  [Read-Write] Select the default display device class to use when a viewport doesn't have one assigned
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``default_view_point`` (DisplayClusterCameraComponent):  [Read-Only] Default camera component. It's an outer camera in VP/ICVFX terminology. Always exists on a DCRA instance.
- ``display_cluster_root_component`` (SceneComponent):  [Read-Write] The root component for our hierarchy.
  Must have CPF_Edit(such as VisibleDefaultsOnly) on property for Live Link.
  nDisplay details panel will hide this from actually being visible.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enable_inner_frustum_chromakey_overlap_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``enable_inner_frustums_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``enable_lightcards_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``enable_preview_techvis`` (bool):  [Read-Write] Configure the root actor for Techvis rendering with preview components.
- ``enable_viewport_ocio_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``freeze_preview_render`` (bool):  [Read-Write] Freeze preview render.  This will impact editor performance.
- ``freeze_render_outer_viewports_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``global_chromakey_color_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``global_chromakey_markers_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``inner_frustum_priority`` (Array[DisplayClusterComponentRef]):  [Read-Write] Set the priority for inner frustum rendering if there is any overlap when enabling multiple ICVFX cameras.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``light_card_blending_mode_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``light_card_content_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``lightcard_all_viewport_color_configuration_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``lightcard_ocio_mode_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``lightcard_per_viewport_ocio_profiles_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``media_settings_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write] Media
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
- ``outer_hide_list_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``per_viewport_color_grading_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``per_viewport_ocio_profiles_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``preview_enable`` (bool):  [Read-Write] Render the scene and display it as a preview on the nDisplay root actor in the editor.  This will impact editor performance.
- ``preview_enable_overlay_material`` (bool):  [Read-Write] Show overlay material on the preview mesh when preview rendering is enabled (UMeshComponent::OverlayMaterial).
- ``preview_enable_post_process`` (bool):  [Read-Write] Enable PostProcess for preview.
- ``preview_icvfx_frustums`` (bool):  [Read-Write] Render ICVFX Frustums
- ``preview_icvfx_frustums_far_distance`` (float):  [Read-Write] Render ICVFX Frustums
- ``preview_in_game_enable`` (bool):  [Read-Write] Render this DCRA in game for Standalone/Package builds.
- ``preview_max_texture_dimension`` (int32):  [Read-Write] The maximum dimension of any internal texture for preview. Use less memory for large preview viewports
- ``preview_node_id`` (str):  [Read-Write] Selectively preview a specific viewport or show all/none.
- ``preview_render_target_ratio_mult`` (float):  [Read-Write] Adjust resolution scaling for the editor preview.
- ``preview_stage_geometry_mesh`` (bool):  [Read-Write] Toggles the visibility of the stage's geometry mesh, a smooth, continuous mesh generated and processed from the stage's geometry
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``relevant_for_level_bounds`` (bool):  [Read-Write] If true, this actor's component's bounds will be included in the level's
  bounding box unless the Actor's class has overridden IsLevelBoundsRelevant
- ``remote_role`` (NetRole):  [Read-Only] Describes how much control the remote machine has over the actor.
- ``render_mode`` (DisplayClusterConfigurationRenderMode):  [Read-Write] Render Mode
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
- ``show_inner_frustum_overlaps_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``tick_per_frame`` (int32):  [Read-Write] Tick Per Frame
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
- ``viewport_overscan_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write] Render a larger frame than specified in the configuration to achieve continuity across displays when using post-processing effects.
- ``viewport_screen_percentage_multiplier_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write]
- ``viewport_screen_percentage_ref`` (DisplayClusterEditorPropertyReference):  [Read-Write] Adjust resolution scaling for an individual viewport.  Viewport Screen Percentage Multiplier is applied to this value.
- ``viewports_per_frame`` (int32):  [Read-Write] Max amount of Viewports Per Frame

<a id="unreal.DisplayClusterRootActor.default_view_point"></a>

#### default_view_point

```python
@property
def default_view_point() -> DisplayClusterCameraComponent
```

(DisplayClusterCameraComponent):  [Read-Only] Default camera component. It's an outer camera in VP/ICVFX terminology. Always exists on a DCRA instance.

<a id="unreal.DisplayClusterRootActor.current_config_data"></a>

#### current_config_data

```python
@property
def current_config_data() -> DisplayClusterConfigurationData
```

(DisplayClusterConfigurationData):  [Read-Only] If set from the DisplayCluster BP Compiler it will be loaded from the class default subobjects in run-time.

<a id="unreal.DisplayClusterRootActor.preview_enable"></a>

#### preview_enable

```python
@property
def preview_enable() -> bool
```

(bool):  [Read-Write] Render the scene and display it as a preview on the nDisplay root actor in the editor.  This will impact editor performance.

<a id="unreal.DisplayClusterRootActor.preview_enable"></a>

#### preview_enable

```python
@preview_enable.setter
def preview_enable(value: bool) -> None
```

<a id="unreal.DisplayClusterRootActor.preview_in_game_enable"></a>

#### preview_in_game_enable

```python
@property
def preview_in_game_enable() -> bool
```

(bool):  [Read-Write] Render this DCRA in game for Standalone/Package builds.

<a id="unreal.DisplayClusterRootActor.preview_in_game_enable"></a>

#### preview_in_game_enable

```python
@preview_in_game_enable.setter
def preview_in_game_enable(value: bool) -> None
```

<a id="unreal.DisplayClusterRootActor.preview_render_target_ratio_mult"></a>

#### preview_render_target_ratio_mult

```python
@property
def preview_render_target_ratio_mult() -> float
```

(float):  [Read-Write] Adjust resolution scaling for the editor preview.

<a id="unreal.DisplayClusterRootActor.preview_render_target_ratio_mult"></a>

#### preview_render_target_ratio_mult

```python
@preview_render_target_ratio_mult.setter
def preview_render_target_ratio_mult(value: float) -> None
```

<a id="unreal.DisplayClusterRootActor.preview_enable_post_process"></a>

#### preview_enable_post_process

```python
@property
def preview_enable_post_process() -> bool
```

(bool):  [Read-Write] Enable PostProcess for preview.

<a id="unreal.DisplayClusterRootActor.preview_enable_post_process"></a>

#### preview_enable_post_process

```python
@preview_enable_post_process.setter
def preview_enable_post_process(value: bool) -> None
```

<a id="unreal.DisplayClusterRootActor.preview_enable_overlay_material"></a>

#### preview_enable_overlay_material

```python
@property
def preview_enable_overlay_material() -> bool
```

(bool):  [Read-Write] Show overlay material on the preview mesh when preview rendering is enabled (UMeshComponent::OverlayMaterial).

<a id="unreal.DisplayClusterRootActor.preview_enable_overlay_material"></a>

#### preview_enable_overlay_material

```python
@preview_enable_overlay_material.setter
def preview_enable_overlay_material(value: bool) -> None
```

<a id="unreal.DisplayClusterRootActor.enable_preview_techvis"></a>

#### enable_preview_techvis

```python
@property
def enable_preview_techvis() -> bool
```

(bool):  [Read-Write] Configure the root actor for Techvis rendering with preview components.

<a id="unreal.DisplayClusterRootActor.enable_preview_techvis"></a>

#### enable_preview_techvis

```python
@enable_preview_techvis.setter
def enable_preview_techvis(value: bool) -> None
```

<a id="unreal.DisplayClusterRootActor.freeze_preview_render"></a>

#### freeze_preview_render

```python
@property
def freeze_preview_render() -> bool
```

(bool):  [Read-Write] Freeze preview render.  This will impact editor performance.

<a id="unreal.DisplayClusterRootActor.freeze_preview_render"></a>

#### freeze_preview_render

```python
@freeze_preview_render.setter
def freeze_preview_render(value: bool) -> None
```

<a id="unreal.DisplayClusterRootActor.preview_icvfx_frustums"></a>

#### preview_icvfx_frustums

```python
@property
def preview_icvfx_frustums() -> bool
```

(bool):  [Read-Write] Render ICVFX Frustums

<a id="unreal.DisplayClusterRootActor.preview_icvfx_frustums"></a>

#### preview_icvfx_frustums

```python
@preview_icvfx_frustums.setter
def preview_icvfx_frustums(value: bool) -> None
```

<a id="unreal.DisplayClusterRootActor.preview_icvfx_frustums_far_distance"></a>

#### preview_icvfx_frustums_far_distance

```python
@property
def preview_icvfx_frustums_far_distance() -> float
```

(float):  [Read-Write] Render ICVFX Frustums

<a id="unreal.DisplayClusterRootActor.preview_icvfx_frustums_far_distance"></a>

#### preview_icvfx_frustums_far_distance

```python
@preview_icvfx_frustums_far_distance.setter
def preview_icvfx_frustums_far_distance(value: float) -> None
```

<a id="unreal.DisplayClusterRootActor.preview_node_id"></a>

#### preview_node_id

```python
@property
def preview_node_id() -> str
```

(str):  [Read-Write] Selectively preview a specific viewport or show all/none.

<a id="unreal.DisplayClusterRootActor.preview_node_id"></a>

#### preview_node_id

```python
@preview_node_id.setter
def preview_node_id(value: str) -> None
```

<a id="unreal.DisplayClusterRootActor.render_mode"></a>

#### render_mode

```python
@property
def render_mode() -> DisplayClusterConfigurationRenderMode
```

(DisplayClusterConfigurationRenderMode):  [Read-Write] Render Mode

<a id="unreal.DisplayClusterRootActor.render_mode"></a>

#### render_mode

```python
@render_mode.setter
def render_mode(value: DisplayClusterConfigurationRenderMode) -> None
```

<a id="unreal.DisplayClusterRootActor.tick_per_frame"></a>

#### tick_per_frame

```python
@property
def tick_per_frame() -> int
```

(int32):  [Read-Write] Tick Per Frame

<a id="unreal.DisplayClusterRootActor.tick_per_frame"></a>

#### tick_per_frame

```python
@tick_per_frame.setter
def tick_per_frame(value: int) -> None
```

<a id="unreal.DisplayClusterRootActor.viewports_per_frame"></a>

#### viewports_per_frame

```python
@property
def viewports_per_frame() -> int
```

(int32):  [Read-Write] Max amount of Viewports Per Frame

<a id="unreal.DisplayClusterRootActor.viewports_per_frame"></a>

#### viewports_per_frame

```python
@viewports_per_frame.setter
def viewports_per_frame(value: int) -> None
```

<a id="unreal.DisplayClusterRootActor.preview_max_texture_dimension"></a>

#### preview_max_texture_dimension

```python
@property
def preview_max_texture_dimension() -> int
```

(int32):  [Read-Write] The maximum dimension of any internal texture for preview. Use less memory for large preview viewports

<a id="unreal.DisplayClusterRootActor.preview_max_texture_dimension"></a>

#### preview_max_texture_dimension

```python
@preview_max_texture_dimension.setter
def preview_max_texture_dimension(value: int) -> None
```

<a id="unreal.DisplayClusterRootActor.update_procedural_mesh_component_data"></a>

#### update_procedural_mesh_component_data

```python
def update_procedural_mesh_component_data(
        procedural_mesh_component: ProceduralMeshComponent = None) -> None
```

x.update_procedural_mesh_component_data(procedural_mesh_component=None) -> None
Update the geometry of the procedural mesh component(s) referenced inside nDisplay

Args:
    procedural_mesh_component (ProceduralMeshComponent): (optional) Mark the specified procedural mesh component, not all

<a id="unreal.DisplayClusterRootActor.set_replace_texture_flag_for_all_viewports"></a>

#### set_replace_texture_flag_for_all_viewports

```python
def set_replace_texture_flag_for_all_viewports(replace: bool) -> bool
```

x.set_replace_texture_flag_for_all_viewports(replace) -> bool
Set Replace Texture Flag for All Viewports

Args:
    replace (bool): 

Returns:
    bool:

<a id="unreal.DisplayClusterRootActor.set_freeze_outer_viewports"></a>

#### set_freeze_outer_viewports

```python
def set_freeze_outer_viewports(enable: bool) -> bool
```

x.set_freeze_outer_viewports(enable) -> bool
Set Freeze Outer Viewports

Args:
    enable (bool): 

Returns:
    bool:

<a id="unreal.DisplayClusterRootActor.make_stage_actor_flush_to_wall"></a>

#### make_stage_actor_flush_to_wall

```python
def make_stage_actor_flush_to_wall(
        stage_actor: DisplayClusterStageActor,
        desired_offset_from_flush: float = 0.000000) -> bool
```

x.make_stage_actor_flush_to_wall(stage_actor, desired_offset_from_flush=0.000000) -> bool
Make Stage Actor Flush to Wall

Args:
    stage_actor (DisplayClusterStageActor): 
    desired_offset_from_flush (double): 

Returns:
    bool:

<a id="unreal.DisplayClusterRootActor.get_flush_position_and_normal"></a>

#### get_flush_position_and_normal

```python
def get_flush_position_and_normal(
        world_position: Vector) -> Optional[Tuple[Vector, Vector]]
```

x.get_flush_position_and_normal(world_position) -> (out_position=Vector, out_normal=Vector) or None
Get Flush Position and Normal

Args:
    world_position (Vector): 

Returns:
    tuple or None: 

    out_position (Vector): 

    out_normal (Vector):

<a id="unreal.DisplayClusterRootActor.get_distance_to_stage_geometry"></a>

#### get_distance_to_stage_geometry

```python
def get_distance_to_stage_geometry(world_position: Vector,
                                   world_direction: Vector) -> Optional[float]
```

x.get_distance_to_stage_geometry(world_position, world_direction) -> float or None
Gets the distance from a world position to the stage's geometry along the specified direction, if there is an intersection

Args:
    world_position (Vector): The world position to measure the distance from
    world_direction (Vector): The direction to find the distance to the geometry along

Returns:
    float or None: True if an intersection point from WorldPosition along WorldDirection was found, false if not

    out_distance (float): The distance to the stage geometry from the specified point

<a id="unreal.DisplayClusterRootActor.get_common_view_point"></a>

#### get_common_view_point

```python
def get_common_view_point() -> SceneComponent
```

x.get_common_view_point() -> SceneComponent
Get the view point most commonly used by viewports in this cluster.
If no viewports override the camera, this returns the default camera, or if there isn't one, the actor's root component.

Returns:
    SceneComponent:

<a id="unreal.DisplayClusterSceneComponentSync"></a>