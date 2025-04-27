## CompositingElement Objects

```python
class CompositingElement(ComposurePipelineBaseActor)
```

Compositing Element

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElement.h

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
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``auto_run`` (bool):  [Read-Write] When set, we'll call EnqueueRendering() each frame automatically. If left
  off, it is up to the user to manually call their composure rendering.
  Toggle this on/off at runtime to enable/disable this pipeline.
- ``auto_run_child_elements_and_self`` (bool):  [Read-Write] When set to false, all composure elements including itself's rendering will not automatically be called in the pipeline.
  When set to true, all of its children and its self's rendering will be called every frame.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``camera_source`` (SceneCameraLinkType):  [Read-Write] *****************************// Inputs
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``compositing_target`` (ComposureCompositingTargetComponent):  [Read-Write]
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_input_type`` (type(Class)):  [Read-Write]
- ``default_output_type`` (type(Class)):  [Read-Write]
- ``default_transform_type`` (type(Class)):  [Read-Write]
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
- ``inputs`` (Array[CompositingElementInput]):  [Read-Write] *****************************// Pipeline Passes
  //   - protected to prevent users from directly modifying these lists (use the accessor functions instead)
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
- ``on_final_pass_rendered_bp`` (DynamicOnFinalPassRendered):  [Read-Write] Called when the final output of this element is rendered
- ``on_input_touch_begin`` (ActorOnInputTouchBeginSignature):  [Read-Write] Called when a touch input is received over this actor when touch events are enabled in the player controller.
- ``on_input_touch_end`` (ActorOnInputTouchEndSignature):  [Read-Write] Called when a touch input is received over this component when touch events are enabled in the player controller.
- ``on_input_touch_enter`` (ActorBeginTouchOverSignature):  [Read-Write] Called when a finger is moved over this actor when touch over events are enabled in the player controller.
- ``on_input_touch_leave`` (ActorEndTouchOverSignature):  [Read-Write] Called when a finger is moved off this actor when touch over events are enabled in the player controller.
- ``on_released`` (ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``on_transform_pass_rendered_bp`` (DynamicOnTransformPassRendered):  [Read-Write] Called when a transform pass on this element is rendered
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``outputs`` (Array[CompositingElementOutput]):  [Read-Write]
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``post_process_proxy`` (ComposurePostProcessingPassProxy):  [Read-Write]
- ``preview_transform`` (CompositingElementTransform):  [Read-Write]
- ``preview_transform_source`` (InheritedSourceType):  [Read-Write]
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``relevant_for_level_bounds`` (bool):  [Read-Write] If true, this actor's component's bounds will be included in the level's
  bounding box unless the Actor's class has overridden IsLevelBoundsRelevant
- ``remote_role`` (NetRole):  [Read-Only] Describes how much control the remote machine has over the actor.
- ``render_format`` (TextureRenderTargetFormat):  [Read-Write]
- ``render_resolution`` (IntPoint):  [Read-Write]
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
- ``resolution_source`` (InheritedSourceType):  [Read-Write] *****************************// Outputs
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``run_in_editor`` (bool):  [Read-Write] With bAutoRun, this will run EnqueueRendering() in editor - enqueuing render calls along with Editor scene rendering.
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``target_camera_actor_ptr`` (CameraActor):  [Read-Write]
- ``transform_passes`` (Array[CompositingElementTransform]):  [Read-Write]
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
- ``use_shared_target_pool`` (bool):  [Read-Write]

<a id="unreal.CompositingElement.compositing_target"></a>

#### compositing_target

```python
@property
def compositing_target() -> ComposureCompositingTargetComponent
```

(ComposureCompositingTargetComponent):  [Read-Only]

<a id="unreal.CompositingElement.post_process_proxy"></a>

#### post_process_proxy

```python
@property
def post_process_proxy() -> ComposurePostProcessingPassProxy
```

(ComposurePostProcessingPassProxy):  [Read-Only]

<a id="unreal.CompositingElement.inputs"></a>

#### inputs

```python
@property
def inputs() -> Array[CompositingElementInput]
```

(Array[CompositingElementInput]):  [Read-Only] *****************************// Pipeline Passes
//   - protected to prevent users from directly modifying these lists (use the accessor functions instead)

<a id="unreal.CompositingElement.transform_passes"></a>

#### transform_passes

```python
@property
def transform_passes() -> Array[CompositingElementTransform]
```

(Array[CompositingElementTransform]):  [Read-Only]

<a id="unreal.CompositingElement.outputs"></a>

#### outputs

```python
@property
def outputs() -> Array[CompositingElementOutput]
```

(Array[CompositingElementOutput]):  [Read-Only]

<a id="unreal.CompositingElement.render_resolution"></a>

#### render_resolution

```python
@property
def render_resolution() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.CompositingElement.render_resolution"></a>

#### render_resolution

```python
@render_resolution.setter
def render_resolution(value: IntPoint) -> None
```

<a id="unreal.CompositingElement.render_format"></a>

#### render_format

```python
@property
def render_format() -> TextureRenderTargetFormat
```

(TextureRenderTargetFormat):  [Read-Write]

<a id="unreal.CompositingElement.render_format"></a>

#### render_format

```python
@render_format.setter
def render_format(value: TextureRenderTargetFormat) -> None
```

<a id="unreal.CompositingElement.on_transform_pass_rendered_bp"></a>

#### on_transform_pass_rendered_bp

```python
@property
def on_transform_pass_rendered_bp() -> DynamicOnTransformPassRendered
```

(DynamicOnTransformPassRendered):  [Read-Write] Called when a transform pass on this element is rendered

<a id="unreal.CompositingElement.on_transform_pass_rendered_bp"></a>

#### on_transform_pass_rendered_bp

```python
@on_transform_pass_rendered_bp.setter
def on_transform_pass_rendered_bp(
        value: DynamicOnTransformPassRendered) -> None
```

<a id="unreal.CompositingElement.on_final_pass_rendered_bp"></a>

#### on_final_pass_rendered_bp

```python
@property
def on_final_pass_rendered_bp() -> DynamicOnFinalPassRendered
```

(DynamicOnFinalPassRendered):  [Read-Write] Called when the final output of this element is rendered

<a id="unreal.CompositingElement.on_final_pass_rendered_bp"></a>

#### on_final_pass_rendered_bp

```python
@on_final_pass_rendered_bp.setter
def on_final_pass_rendered_bp(value: DynamicOnFinalPassRendered) -> None
```

<a id="unreal.CompositingElement.set_target_camera"></a>

#### set_target_camera

```python
def set_target_camera(new_camera_actor: CameraActor) -> None
```

x.set_target_camera(new_camera_actor) -> None
Set Target Camera

Args:
    new_camera_actor (CameraActor):

<a id="unreal.CompositingElement.set_opacity"></a>

#### set_opacity

```python
def set_opacity(new_opacity: float) -> None
```

x.set_opacity(new_opacity) -> None
Set the rendering opacity of current composure actor.

Args:
    new_opacity (float): The new opacity value set to the composure element.

<a id="unreal.CompositingElement.set_element_name"></a>

#### set_element_name

```python
def set_element_name(new_name: Name) -> None
```

x.set_element_name(new_name) -> None
Rename composure actor's name

Args:
    new_name (Name): New name for current composure element.

<a id="unreal.CompositingElement.set_editor_color_picking_target"></a>

#### set_editor_color_picking_target

```python
def set_editor_color_picking_target(
        picking_target: TextureRenderTarget2D) -> None
```

x.set_editor_color_picking_target(picking_target) -> None
EDITOR ONLY - Specifies which intermediate target to pick colors from (if left unset, we default to the display image)

Args:
    picking_target (TextureRenderTarget2D):

<a id="unreal.CompositingElement.set_editor_color_picker_display_image"></a>

#### set_editor_color_picker_display_image

```python
def set_editor_color_picker_display_image(
        picker_display_image: Texture) -> None
```

x.set_editor_color_picker_display_image(picker_display_image) -> None
EDITOR ONLY - Specifies an intermediate image to display when picking (if left unset, we default to the final output image)

Args:
    picker_display_image (Texture):

<a id="unreal.CompositingElement.request_named_render_target"></a>

#### request_named_render_target

```python
def request_named_render_target(
    reference_name: Name,
    render_percentage: float = 1.000000,
    usage_tag: TargetUsageFlags = TargetUsageFlags.USAGE_NONE
) -> TextureRenderTarget2D
```

x.request_named_render_target(reference_name, render_percentage=1.000000, usage_tag=TargetUsageFlags.USAGE_NONE) -> TextureRenderTarget2D
Request Named Render Target

Args:
    reference_name (Name): 
    render_percentage (float): 
    usage_tag (TargetUsageFlags): 

Returns:
    TextureRenderTarget2D:

<a id="unreal.CompositingElement.render_compositing_material_to_target"></a>

#### render_compositing_material_to_target

```python
def render_compositing_material_to_target(
    comp_material: CompositingMaterial,
    render_target: TextureRenderTarget2D,
    result_lookup_name: Name = "None"
) -> Tuple[TextureRenderTarget2D, CompositingMaterial]
```

x.render_compositing_material_to_target(comp_material, render_target, result_lookup_name="None") -> (TextureRenderTarget2D, comp_material=CompositingMaterial)
Render Compositing Material to Target

Args:
    comp_material (CompositingMaterial): 
    render_target (TextureRenderTarget2D): 
    result_lookup_name (Name): 

Returns:
    CompositingMaterial: 

    comp_material (CompositingMaterial):

<a id="unreal.CompositingElement.render_compositing_material"></a>

#### render_compositing_material

```python
def render_compositing_material(
    comp_material: CompositingMaterial,
    render_scale: float = 1.000000,
    result_lookup_name: Name = "None",
    usage_tag: TargetUsageFlags = TargetUsageFlags.USAGE_NONE
) -> Tuple[Texture, CompositingMaterial]
```

x.render_compositing_material(comp_material, render_scale=1.000000, result_lookup_name="None", usage_tag=TargetUsageFlags.USAGE_NONE) -> (Texture, comp_material=CompositingMaterial)
Render Compositing Material

Args:
    comp_material (CompositingMaterial): 
    render_scale (float): 
    result_lookup_name (Name): 
    usage_tag (TargetUsageFlags): 

Returns:
    CompositingMaterial: 

    comp_material (CompositingMaterial):

<a id="unreal.CompositingElement.render_comp_element"></a>

#### render_comp_element

```python
def render_comp_element(camera_cut_this_frame: bool) -> Texture
```

x.render_comp_element(camera_cut_this_frame) -> Texture
Render Comp Element

Args:
    camera_cut_this_frame (bool): 

Returns:
    Texture:

<a id="unreal.CompositingElement.release_owned_target"></a>

#### release_owned_target

```python
def release_owned_target(owned_target: TextureRenderTarget2D) -> bool
```

x.release_owned_target(owned_target) -> bool
Release Owned Target

Args:
    owned_target (TextureRenderTarget2D): 

Returns:
    bool:

<a id="unreal.CompositingElement.register_pass_result"></a>

#### register_pass_result

```python
def register_pass_result(reference_name: Name,
                         pass_result: Texture,
                         set_as_latest_render_result: bool = True) -> None
```

x.register_pass_result(reference_name, pass_result, set_as_latest_render_result=True) -> None
Register Pass Result

Args:
    reference_name (Name): 
    pass_result (Texture): 
    set_as_latest_render_result (bool):

<a id="unreal.CompositingElement.is_sub_element"></a>

#### is_sub_element

```python
def is_sub_element() -> bool
```

x.is_sub_element() -> bool
Determines whether current composure element is a child of another composure element or not.

Returns:
    bool: bool                Whether current composure actor is a child actor or not.

<a id="unreal.CompositingElement.get_render_priority"></a>

#### get_render_priority

```python
def get_render_priority() -> int
```

x.get_render_priority() -> int32
Get Render Priority

Returns:
    int32:

<a id="unreal.CompositingElement.get_opacity"></a>

#### get_opacity

```python
def get_opacity() -> float
```

x.get_opacity() -> float
Return the rendering opacity of current composure actor.

Returns:
    float: float                The rendering opacity of current composure element.

<a id="unreal.CompositingElement.get_latest_render_result"></a>

#### get_latest_render_result

```python
def get_latest_render_result() -> Texture
```

x.get_latest_render_result() -> Texture
const;

Returns:
    Texture:

<a id="unreal.CompositingElement.get_element_parent"></a>

#### get_element_parent

```python
def get_element_parent() -> CompositingElement
```

x.get_element_parent() -> CompositingElement
Get the parent composure element of current element.

Returns:
    CompositingElement: bool                Whether the function successfully finds the parent or not.

<a id="unreal.CompositingElement.get_comp_element_name"></a>

#### get_comp_element_name

```python
def get_comp_element_name() -> Name
```

x.get_comp_element_name() -> Name
Return the FName of the composure element object

Returns:
    Name:

<a id="unreal.CompositingElement.get_child_elements"></a>

#### get_child_elements

```python
def get_child_elements() -> Array[CompositingElement]
```

x.get_child_elements() -> Array[CompositingElement]
Get the first level of current element's child composure elements.

Returns:
    Array[CompositingElement]: TArray<ACompositingElement*>   The array containing all the first level children without any grandchildren.

<a id="unreal.CompositingElement.find_transform_pass"></a>

#### find_transform_pass

```python
def find_transform_pass(
    transform_type: Class,
    optional_pass_name: Name = "None"
) -> Tuple[CompositingElementTransform, Texture]
```

x.find_transform_pass(transform_type, optional_pass_name="None") -> (CompositingElementTransform, pass_result=Texture)
Find Transform Pass

Args:
    transform_type (type(Class)): 
    optional_pass_name (Name): 

Returns:
    Texture: 

    pass_result (Texture):

<a id="unreal.CompositingElement.find_target_camera"></a>

#### find_target_camera

```python
def find_target_camera() -> CameraActor
```

x.find_target_camera() -> CameraActor
Find Target Camera

Returns:
    CameraActor:

<a id="unreal.CompositingElement.find_output_pass"></a>

#### find_output_pass

```python
def find_output_pass(
        output_type: Class,
        optional_pass_name: Name = "None") -> CompositingElementOutput
```

x.find_output_pass(output_type, optional_pass_name="None") -> CompositingElementOutput
Find Output Pass

Args:
    output_type (type(Class)): 
    optional_pass_name (Name): 

Returns:
    CompositingElementOutput:

<a id="unreal.CompositingElement.find_named_render_result"></a>

#### find_named_render_result

```python
def find_named_render_result(pass_name: Name,
                             search_sub_elements: bool = True) -> Texture
```

x.find_named_render_result(pass_name, search_sub_elements=True) -> Texture
Find Named Render Result

Args:
    pass_name (Name): 
    search_sub_elements (bool): 

Returns:
    Texture:

<a id="unreal.CompositingElement.find_input_pass"></a>

#### find_input_pass

```python
def find_input_pass(
    input_type: Class,
    optional_pass_name: Name = "None"
) -> Tuple[CompositingElementInput, Texture]
```

x.find_input_pass(input_type, optional_pass_name="None") -> (CompositingElementInput, pass_result=Texture)
*****************************// Pass Management

Args:
    input_type (type(Class)): 
    optional_pass_name (Name): 

Returns:
    Texture: 

    pass_result (Texture):

<a id="unreal.CompositingElement.delete_pass"></a>

#### delete_pass

```python
def delete_pass(pass_to_delete: CompositingElementPass) -> bool
```

x.delete_pass(pass_to_delete) -> bool
Delete a specific pass. This function deals with the public list where deletion is directly reflected in the editor.

Args:
    pass_to_delete (CompositingElementPass): The pass that will be deleted.

Returns:
    bool: bool                   Whether the delete operation is successful or not

<a id="unreal.CompositingElement.create_new_transform_pass"></a>

#### create_new_transform_pass

```python
def create_new_transform_pass(
        pass_name: Name, transform_type: Class) -> CompositingElementTransform
```

x.create_new_transform_pass(pass_name, transform_type) -> CompositingElementTransform
Create a new Transform pass into the public list which directly shows in the editor.

Args:
    pass_name (Name): The name for the new pass.
    transform_type (type(Class)): The class type of the created pass.

Returns:
    CompositingElementTransform: CompositingElementTransform    The newly created transform pass object.

<a id="unreal.CompositingElement.create_new_output_pass"></a>

#### create_new_output_pass

```python
def create_new_output_pass(pass_name: Name,
                           output_type: Class) -> CompositingElementOutput
```

x.create_new_output_pass(pass_name, output_type) -> CompositingElementOutput
Create a new Output pass into the public list which directly shows in the editor.

Args:
    pass_name (Name): The name for the new pass.
    output_type (type(Class)): The class type of the created pass.

Returns:
    CompositingElementOutput: CompositingElementOutput       The newly created output pass object.

<a id="unreal.CompositingElement.create_new_input_pass"></a>

#### create_new_input_pass

```python
def create_new_input_pass(pass_name: Name,
                          input_type: Class) -> CompositingElementInput
```

x.create_new_input_pass(pass_name, input_type) -> CompositingElementInput
Create a new input pass into the public list which directly shows in the editor.

Args:
    pass_name (Name): The name for the new pass.
    input_type (type(Class)): The class type of the created pass.

Returns:
    CompositingElementInput: CompositingElementInput        The newly created input pass object.

<a id="unreal.CompositingElement.add_new_transform_pass"></a>

#### add_new_transform_pass

```python
def add_new_transform_pass(
        pass_name: Name, transform_type: Class) -> CompositingElementTransform
```

x.add_new_transform_pass(pass_name, transform_type) -> CompositingElementTransform
Add New Transform Pass

Args:
    pass_name (Name): 
    transform_type (type(Class)): 

Returns:
    CompositingElementTransform:

<a id="unreal.CompositingElement.add_new_output_pass"></a>

#### add_new_output_pass

```python
def add_new_output_pass(pass_name: Name,
                        output_type: Class) -> CompositingElementOutput
```

x.add_new_output_pass(pass_name, output_type) -> CompositingElementOutput
Add New Output Pass

Args:
    pass_name (Name): 
    output_type (type(Class)): 

Returns:
    CompositingElementOutput:

<a id="unreal.CompositingElement.add_new_input_pass"></a>

#### add_new_input_pass

```python
def add_new_input_pass(pass_name: Name,
                       input_type: Class) -> CompositingElementInput
```

x.add_new_input_pass(pass_name, input_type) -> CompositingElementInput
Add New Input Pass

Args:
    pass_name (Name): 
    input_type (type(Class)): 

Returns:
    CompositingElementInput:

<a id="unreal.ComposureCompShotElement"></a>