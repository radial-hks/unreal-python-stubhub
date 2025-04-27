## DisplayClusterLightCardActor Objects

```python
class DisplayClusterLightCardActor(Actor)
```

Display Cluster Light Card Actor

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterLightCardActor.h

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
- ``alpha_gradient`` (LightCardAlphaGradientSettings):  [Read-Write] Settings related to an alpha gradient effect
- ``always_flush_to_wall`` (bool):  [Read-Write] Indicates whether the light card is always made to be flush to a stage wall or not
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
- ``color`` (LinearColor):  [Read-Write] Light card color, before any modifier is applied
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_scene_root_component`` (SceneComponent):  [Read-Write]
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``distance_from_center`` (double):  [Read-Write] Radius of light card polar coordinates. Does not include the effect of RadialOffset
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``exposure`` (float):  [Read-Write] 2^Exposure color value multiplier
- ``extender_name_to_component_map`` (Map[Name, ActorComponent]):  [Read-Only] Components added by the IDisplayLightCardActorExtender
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``feathering`` (float):  [Read-Write] Feathers in the alpha from the edges
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``gain`` (float):  [Read-Write] Linear color value multiplier
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
- ``label_component`` (DisplayClusterLabelComponent):  [Read-Write]
- ``latitude`` (double):  [Read-Write] Related to the Elevation of light card polar coordinates
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``light_card_component`` (StaticMeshComponent):  [Read-Write]
- ``light_card_transformer_component`` (SceneComponent):  [Read-Write]
- ``longitude`` (double):  [Read-Write] Related to the Azimuth of light card polar coordinates
- ``main_spring_arm_component`` (SpringArmComponent):  [Read-Write]
- ``mask`` (DisplayClusterLightCardMask):  [Read-Write]
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
- ``opacity`` (float):  [Read-Write] Linear alpha multiplier
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``per_lightcard_render_mode`` (DisplayClusterConfigurationICVFX_PerLightcardRenderMode):  [Read-Write] Specify how to render this Light Card Actor in relation to the inner frustum.
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pitch`` (double):  [Read-Write]
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``polygon`` (Array[Vector2D]):  [Read-Write] Polygon points when using this type of mask
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``radial_offset`` (double):  [Read-Write] Used by the flush constraint to offset the location of the light card form the wall
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
- ``scale`` (Vector2D):  [Read-Write]
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``spin`` (double):  [Read-Write] Roll rotation of light card around its plane axis
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``stage_actor_component`` (DisplayClusterStageActorComponent):  [Read-Only] Manages stage actor properties
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``temperature`` (float):  [Read-Write]
- ``texture`` (Texture):  [Read-Write]
- ``tint`` (float):  [Read-Write]
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
- ``uv_coordinates`` (Vector2D):  [Read-Write] The UV coordinates of the light card, if it is in UV space
- ``uv_indicator_component`` (StaticMeshComponent):  [Read-Write]
- ``yaw`` (double):  [Read-Write]

<a id="unreal.DisplayClusterLightCardActor.distance_from_center"></a>

#### distance_from_center

```python
@property
def distance_from_center() -> float
```

(double):  [Read-Write] Radius of light card polar coordinates. Does not include the effect of RadialOffset

<a id="unreal.DisplayClusterLightCardActor.distance_from_center"></a>

#### distance_from_center

```python
@distance_from_center.setter
def distance_from_center(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.longitude"></a>

#### longitude

```python
@property
def longitude() -> float
```

(double):  [Read-Write] Related to the Azimuth of light card polar coordinates

<a id="unreal.DisplayClusterLightCardActor.longitude"></a>

#### longitude

```python
@longitude.setter
def longitude(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.latitude"></a>

#### latitude

```python
@property
def latitude() -> float
```

(double):  [Read-Write] Related to the Elevation of light card polar coordinates

<a id="unreal.DisplayClusterLightCardActor.latitude"></a>

#### latitude

```python
@latitude.setter
def latitude(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.uv_coordinates"></a>

#### uv_coordinates

```python
@property
def uv_coordinates() -> Vector2D
```

(Vector2D):  [Read-Write] The UV coordinates of the light card, if it is in UV space

<a id="unreal.DisplayClusterLightCardActor.uv_coordinates"></a>

#### uv_coordinates

```python
@uv_coordinates.setter
def uv_coordinates(value: Vector2D) -> None
```

<a id="unreal.DisplayClusterLightCardActor.spin"></a>

#### spin

```python
@property
def spin() -> float
```

(double):  [Read-Write] Roll rotation of light card around its plane axis

<a id="unreal.DisplayClusterLightCardActor.spin"></a>

#### spin

```python
@spin.setter
def spin(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.pitch"></a>

#### pitch

```python
@property
def pitch() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterLightCardActor.pitch"></a>

#### pitch

```python
@pitch.setter
def pitch(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.yaw"></a>

#### yaw

```python
@property
def yaw() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterLightCardActor.yaw"></a>

#### yaw

```python
@yaw.setter
def yaw(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.scale"></a>

#### scale

```python
@property
def scale() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DisplayClusterLightCardActor.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector2D) -> None
```

<a id="unreal.DisplayClusterLightCardActor.radial_offset"></a>

#### radial_offset

```python
@property
def radial_offset() -> float
```

(double):  [Read-Write] Used by the flush constraint to offset the location of the light card form the wall

<a id="unreal.DisplayClusterLightCardActor.radial_offset"></a>

#### radial_offset

```python
@radial_offset.setter
def radial_offset(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.always_flush_to_wall"></a>

#### always_flush_to_wall

```python
@property
def always_flush_to_wall() -> bool
```

(bool):  [Read-Write] Indicates whether the light card is always made to be flush to a stage wall or not

<a id="unreal.DisplayClusterLightCardActor.always_flush_to_wall"></a>

#### always_flush_to_wall

```python
@always_flush_to_wall.setter
def always_flush_to_wall(value: bool) -> None
```

<a id="unreal.DisplayClusterLightCardActor.per_lightcard_render_mode"></a>

#### per_lightcard_render_mode

```python
@property
def per_lightcard_render_mode(
) -> DisplayClusterConfigurationICVFX_PerLightcardRenderMode
```

(DisplayClusterConfigurationICVFX_PerLightcardRenderMode):  [Read-Write] Specify how to render this Light Card Actor in relation to the inner frustum.

<a id="unreal.DisplayClusterLightCardActor.per_lightcard_render_mode"></a>

#### per_lightcard_render_mode

```python
@per_lightcard_render_mode.setter
def per_lightcard_render_mode(
        value: DisplayClusterConfigurationICVFX_PerLightcardRenderMode
) -> None
```

<a id="unreal.DisplayClusterLightCardActor.mask"></a>

#### mask

```python
@property
def mask() -> DisplayClusterLightCardMask
```

(DisplayClusterLightCardMask):  [Read-Write]

<a id="unreal.DisplayClusterLightCardActor.mask"></a>

#### mask

```python
@mask.setter
def mask(value: DisplayClusterLightCardMask) -> None
```

<a id="unreal.DisplayClusterLightCardActor.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.DisplayClusterLightCardActor.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture) -> None
```

<a id="unreal.DisplayClusterLightCardActor.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] Light card color, before any modifier is applied

<a id="unreal.DisplayClusterLightCardActor.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.DisplayClusterLightCardActor.temperature"></a>

#### temperature

```python
@property
def temperature() -> float
```

(float):  [Read-Write]

<a id="unreal.DisplayClusterLightCardActor.temperature"></a>

#### temperature

```python
@temperature.setter
def temperature(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.tint"></a>

#### tint

```python
@property
def tint() -> float
```

(float):  [Read-Write]

<a id="unreal.DisplayClusterLightCardActor.tint"></a>

#### tint

```python
@tint.setter
def tint(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.exposure"></a>

#### exposure

```python
@property
def exposure() -> float
```

(float):  [Read-Write] 2^Exposure color value multiplier

<a id="unreal.DisplayClusterLightCardActor.exposure"></a>

#### exposure

```python
@exposure.setter
def exposure(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.gain"></a>

#### gain

```python
@property
def gain() -> float
```

(float):  [Read-Write] Linear color value multiplier

<a id="unreal.DisplayClusterLightCardActor.gain"></a>

#### gain

```python
@gain.setter
def gain(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.opacity"></a>

#### opacity

```python
@property
def opacity() -> float
```

(float):  [Read-Write] Linear alpha multiplier

<a id="unreal.DisplayClusterLightCardActor.opacity"></a>

#### opacity

```python
@opacity.setter
def opacity(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.feathering"></a>

#### feathering

```python
@property
def feathering() -> float
```

(float):  [Read-Write] Feathers in the alpha from the edges

<a id="unreal.DisplayClusterLightCardActor.feathering"></a>

#### feathering

```python
@feathering.setter
def feathering(value: float) -> None
```

<a id="unreal.DisplayClusterLightCardActor.alpha_gradient"></a>

#### alpha_gradient

```python
@property
def alpha_gradient() -> LightCardAlphaGradientSettings
```

(LightCardAlphaGradientSettings):  [Read-Write] Settings related to an alpha gradient effect

<a id="unreal.DisplayClusterLightCardActor.alpha_gradient"></a>

#### alpha_gradient

```python
@alpha_gradient.setter
def alpha_gradient(value: LightCardAlphaGradientSettings) -> None
```

<a id="unreal.DisplayClusterLightCardActor.polygon"></a>

#### polygon

```python
@property
def polygon() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write] Polygon points when using this type of mask

<a id="unreal.DisplayClusterLightCardActor.polygon"></a>

#### polygon

```python
@polygon.setter
def polygon(value: Array[Vector2D]) -> None
```

<a id="unreal.DisplayClusterLightCardActor.default_scene_root_component"></a>

#### default_scene_root_component

```python
@property
def default_scene_root_component() -> SceneComponent
```

(SceneComponent):  [Read-Only]

<a id="unreal.DisplayClusterLightCardActor.main_spring_arm_component"></a>

#### main_spring_arm_component

```python
@property
def main_spring_arm_component() -> SpringArmComponent
```

(SpringArmComponent):  [Read-Only]

<a id="unreal.DisplayClusterLightCardActor.light_card_transformer_component"></a>

#### light_card_transformer_component

```python
@property
def light_card_transformer_component() -> SceneComponent
```

(SceneComponent):  [Read-Only]

<a id="unreal.DisplayClusterLightCardActor.light_card_component"></a>

#### light_card_component

```python
@property
def light_card_component() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Only]

<a id="unreal.DisplayClusterLightCardActor.label_component"></a>

#### label_component

```python
@property
def label_component() -> DisplayClusterLabelComponent
```

(DisplayClusterLabelComponent):  [Read-Only]

<a id="unreal.DisplayClusterLightCardActor.uv_indicator_component"></a>

#### uv_indicator_component

```python
@property
def uv_indicator_component() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Only]

<a id="unreal.DisplayClusterChromakeyCardActor"></a>