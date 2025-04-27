## Actor Objects

```python
class Actor(Object)
```

Actor is the base class for an Object that can be placed or spawned in a level.
Actors may contain a collection of ActorComponents, which can be used to control how actors move, how they are rendered, etc.
The other main function of an Actor is the replication of properties and function calls across the network during play.


Actor initialization has multiple steps, here's the order of important virtual functions that get called:
- UObject::PostLoad: For actors statically placed in a level, the normal UObject PostLoad gets called both in the editor and during gameplay.
                     This is not called for newly spawned actors.
- UActorComponent::OnComponentCreated: When an actor is spawned in the editor or during gameplay, this gets called for any native components.
                                       For blueprint-created components, this gets called during construction for that component.
                                       This is not called for components loaded from a level.
- AActor::PreRegisterAllComponents: For statically placed actors and spawned actors that have native root components, this gets called now.
                                    For blueprint actors without a native root component, these registration functions get called later during construction.
- UActorComponent::RegisterComponent: All components are registered in editor and at runtime, this creates their physical/visual representation.
                                      These calls may be distributed over multiple frames, but are always after PreRegisterAllComponents.
                                      This may also get called later on after an UnregisterComponent call removes it from the world.
- AActor::PostRegisterAllComponents: Called for all actors both in the editor and in gameplay, this is the last function that is called in all cases.
- AActor::PostActorCreated: When an actor is created in the editor or during gameplay, this gets called right before construction.
                            This is not called for components loaded from a level.
- AActor::UserConstructionScript: Called for blueprints that implement a construction script.
- AActor::OnConstruction: Called at the end of ExecuteConstruction, which calls the blueprint construction script.
                          This is called after all blueprint-created components are fully created and registered.
                          This is only called during gameplay for spawned actors, and may get rerun in the editor when changing blueprints.
- AActor::PreInitializeComponents: Called before InitializeComponent is called on the actor's components.
                                   This is only called during gameplay and in certain editor preview windows.
- UActorComponent::Activate: This will be called only if the component has bAutoActivate set.
                             It will also got called later on if a component is manually activated.
- UActorComponent::InitializeComponent: This will be called only if the component has bWantsInitializeComponentSet.
                                        This only happens once per gameplay session.
- AActor::PostInitializeComponents: Called after the actor's components have been initialized, only during gameplay and some editor previews.
- AActor::BeginPlay: Called when the level starts ticking, only during actual gameplay.
                     This normally happens right after PostInitializeComponents but can be delayed for networked or child actors.
see: https://docs.unrealengine.com/Programming/UnrealArchitecture/Actors
see: https://docs.unrealengine.com/Programming/UnrealArchitecture/Actors/ActorLifecycle
see: UActorComponent

**C++ Source:**

- **Module**: Engine
- **File**: Actor.h

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
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
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

<a id="unreal.Actor.only_relevant_to_owner"></a>

#### only_relevant_to_owner

```python
@property
def only_relevant_to_owner() -> bool
```

(bool):  [Read-Only] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.

<a id="unreal.Actor.always_relevant"></a>

#### always_relevant

```python
@property
def always_relevant() -> bool
```

(bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).

<a id="unreal.Actor.always_relevant"></a>

#### always_relevant

```python
@always_relevant.setter
def always_relevant(value: bool) -> None
```

<a id="unreal.Actor.hidden"></a>

#### hidden

```python
@property
def hidden() -> bool
```

(bool):  [Read-Only] Allows us to only see this Actor in the Editor, and not in the actual game.
see: SetActorHiddenInGame()

<a id="unreal.Actor.net_use_owner_relevancy"></a>

#### net_use_owner_relevancy

```python
@property
def net_use_owner_relevancy() -> bool
```

(bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority

<a id="unreal.Actor.net_use_owner_relevancy"></a>

#### net_use_owner_relevancy

```python
@net_use_owner_relevancy.setter
def net_use_owner_relevancy(value: bool) -> None
```

<a id="unreal.Actor.auto_destroy_when_finished"></a>

#### auto_destroy_when_finished

```python
@property
def auto_destroy_when_finished() -> bool
```

(bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.

<a id="unreal.Actor.auto_destroy_when_finished"></a>

#### auto_destroy_when_finished

```python
@auto_destroy_when_finished.setter
def auto_destroy_when_finished(value: bool) -> None
```

<a id="unreal.Actor.can_be_damaged"></a>

#### can_be_damaged

```python
@property
def can_be_damaged() -> bool
```

(bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
see: https://www.unrealengine.com/blog/damage-in-ue4
see: TakeDamage(), ReceiveDamage()

<a id="unreal.Actor.can_be_damaged"></a>

#### can_be_damaged

```python
@can_be_damaged.setter
def can_be_damaged(value: bool) -> None
```

<a id="unreal.Actor.find_camera_component_when_view_target"></a>

#### find_camera_component_when_view_target

```python
@property
def find_camera_component_when_view_target() -> bool
```

(bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.

<a id="unreal.Actor.find_camera_component_when_view_target"></a>

#### find_camera_component_when_view_target

```python
@find_camera_component_when_view_target.setter
def find_camera_component_when_view_target(value: bool) -> None
```

<a id="unreal.Actor.generate_overlap_events_during_level_streaming"></a>

#### generate_overlap_events_during_level_streaming

```python
@property
def generate_overlap_events_during_level_streaming() -> bool
```

(bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
see: UpdateOverlapsMethodDuringLevelStreaming

<a id="unreal.Actor.generate_overlap_events_during_level_streaming"></a>

#### generate_overlap_events_during_level_streaming

```python
@generate_overlap_events_during_level_streaming.setter
def generate_overlap_events_during_level_streaming(value: bool) -> None
```

<a id="unreal.Actor.enable_auto_lod_generation"></a>

#### enable_auto_lod_generation

```python
@property
def enable_auto_lod_generation() -> bool
```

(bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.

<a id="unreal.Actor.enable_auto_lod_generation"></a>

#### enable_auto_lod_generation

```python
@enable_auto_lod_generation.setter
def enable_auto_lod_generation(value: bool) -> None
```

<a id="unreal.Actor.replicates"></a>

#### replicates

```python
@property
def replicates() -> bool
```

(bool):  [Read-Only] If true, this actor will replicate to remote machines
see: SetReplicates()

<a id="unreal.Actor.replicate_using_registered_sub_object_list"></a>

#### replicate_using_registered_sub_object_list

```python
@property
def replicate_using_registered_sub_object_list() -> bool
```

(bool):  [Read-Only] When true the replication system will only replicate the registered subobjects and the replicated actor components list
When false the replication system will instead call the virtual ReplicateSubobjects() function where the subobjects and actor components need to be manually replicated.

<a id="unreal.Actor.initial_life_span"></a>

#### initial_life_span

```python
@property
def initial_life_span() -> float
```

(float):  [Read-Only] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.

<a id="unreal.Actor.life_span"></a>

#### life_span

```python
@property
def life_span() -> float
```

deprecated: 'life_span' was renamed to 'initial_life_span'.

<a id="unreal.Actor.custom_time_dilation"></a>

#### custom_time_dilation

```python
@property
def custom_time_dilation() -> float
```

(float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.

<a id="unreal.Actor.custom_time_dilation"></a>

#### custom_time_dilation

```python
@custom_time_dilation.setter
def custom_time_dilation(value: float) -> None
```

<a id="unreal.Actor.net_dormancy"></a>

#### net_dormancy

```python
@property
def net_dormancy() -> NetDormancy
```

(NetDormancy):  [Read-Only] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.

<a id="unreal.Actor.spawn_collision_handling_method"></a>

#### spawn_collision_handling_method

```python
@property
def spawn_collision_handling_method() -> SpawnActorCollisionHandlingMethod
```

(SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.

<a id="unreal.Actor.spawn_collision_handling_method"></a>

#### spawn_collision_handling_method

```python
@spawn_collision_handling_method.setter
def spawn_collision_handling_method(
        value: SpawnActorCollisionHandlingMethod) -> None
```

<a id="unreal.Actor.net_cull_distance_squared"></a>

#### net_cull_distance_squared

```python
@property
def net_cull_distance_squared() -> float
```

(float):  [Read-Write]

<a id="unreal.Actor.net_cull_distance_squared"></a>

#### net_cull_distance_squared

```python
@net_cull_distance_squared.setter
def net_cull_distance_squared(value: float) -> None
```

<a id="unreal.Actor.net_update_frequency"></a>

#### net_update_frequency

```python
@property
def net_update_frequency() -> float
```

(float):  [Read-Write]

<a id="unreal.Actor.net_update_frequency"></a>

#### net_update_frequency

```python
@net_update_frequency.setter
def net_update_frequency(value: float) -> None
```

<a id="unreal.Actor.min_net_update_frequency"></a>

#### min_net_update_frequency

```python
@property
def min_net_update_frequency() -> float
```

(float):  [Read-Write]

<a id="unreal.Actor.min_net_update_frequency"></a>

#### min_net_update_frequency

```python
@min_net_update_frequency.setter
def min_net_update_frequency(value: float) -> None
```

<a id="unreal.Actor.net_priority"></a>

#### net_priority

```python
@property
def net_priority() -> float
```

(float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate

<a id="unreal.Actor.net_priority"></a>

#### net_priority

```python
@net_priority.setter
def net_priority(value: float) -> None
```

<a id="unreal.Actor.instigator"></a>

#### instigator

```python
@property
def instigator() -> Pawn
```

(Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.

<a id="unreal.Actor.instigator"></a>

#### instigator

```python
@instigator.setter
def instigator(value: Pawn) -> None
```

<a id="unreal.Actor.root_component"></a>

#### root_component

```python
@property
def root_component() -> SceneComponent
```

(SceneComponent):  [Read-Only] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow

<a id="unreal.Actor.pivot_offset"></a>

#### pivot_offset

```python
@property
def pivot_offset() -> Vector
```

(Vector):  [Read-Only] Local space pivot offset for the actor, only used in the editor

<a id="unreal.Actor.actor_guid"></a>

#### actor_guid

```python
@property
def actor_guid() -> Guid
```

(Guid):  [Read-Only] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
see: ActorInstanceGuid, FActorInstanceGuidMapper
note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.

<a id="unreal.Actor.actor_instance_guid"></a>

#### actor_instance_guid

```python
@property
def actor_instance_guid() -> Guid
```

(Guid):  [Read-Only] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
see: ActorGuid
note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.

<a id="unreal.Actor.content_bundle_guid"></a>

#### content_bundle_guid

```python
@property
def content_bundle_guid() -> Guid
```

(Guid):  [Read-Only] The GUID for this actor's content bundle.

<a id="unreal.Actor.sprite_scale"></a>

#### sprite_scale

```python
@property
def sprite_scale() -> float
```

(float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).

<a id="unreal.Actor.sprite_scale"></a>

#### sprite_scale

```python
@sprite_scale.setter
def sprite_scale(value: float) -> None
```

<a id="unreal.Actor.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.

<a id="unreal.Actor.tags"></a>

#### tags

```python
@tags.setter
def tags(value: Array[Name]) -> None
```

<a id="unreal.Actor.on_take_any_damage"></a>

#### on_take_any_damage

```python
@property
def on_take_any_damage() -> TakeAnyDamageSignature
```

(TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.

<a id="unreal.Actor.on_take_any_damage"></a>

#### on_take_any_damage

```python
@on_take_any_damage.setter
def on_take_any_damage(value: TakeAnyDamageSignature) -> None
```

<a id="unreal.Actor.on_take_point_damage"></a>

#### on_take_point_damage

```python
@property
def on_take_point_damage() -> TakePointDamageSignature
```

(TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.

<a id="unreal.Actor.on_take_point_damage"></a>

#### on_take_point_damage

```python
@on_take_point_damage.setter
def on_take_point_damage(value: TakePointDamageSignature) -> None
```

<a id="unreal.Actor.on_take_radial_damage"></a>

#### on_take_radial_damage

```python
@property
def on_take_radial_damage() -> TakeRadialDamageSignature
```

(TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.

<a id="unreal.Actor.on_take_radial_damage"></a>

#### on_take_radial_damage

```python
@on_take_radial_damage.setter
def on_take_radial_damage(value: TakeRadialDamageSignature) -> None
```

<a id="unreal.Actor.on_actor_begin_overlap"></a>

#### on_actor_begin_overlap

```python
@property
def on_actor_begin_overlap() -> ActorBeginOverlapSignature
```

(ActorBeginOverlapSignature):  [Read-Write] Called when another actor begins to overlap this actor, for example a player walking into a trigger.
For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.

<a id="unreal.Actor.on_actor_begin_overlap"></a>

#### on_actor_begin_overlap

```python
@on_actor_begin_overlap.setter
def on_actor_begin_overlap(value: ActorBeginOverlapSignature) -> None
```

<a id="unreal.Actor.on_actor_touch"></a>

#### on_actor_touch

```python
@property
def on_actor_touch() -> ActorBeginOverlapSignature
```

deprecated: 'on_actor_touch' was renamed to 'on_actor_begin_overlap'.

<a id="unreal.Actor.on_actor_touch"></a>

#### on_actor_touch

```python
@on_actor_touch.setter
def on_actor_touch(value: ActorBeginOverlapSignature) -> None
```

<a id="unreal.Actor.on_actor_end_overlap"></a>

#### on_actor_end_overlap

```python
@property
def on_actor_end_overlap() -> ActorEndOverlapSignature
```

(ActorEndOverlapSignature):  [Read-Write] Called when another actor stops overlapping this actor.
note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.

<a id="unreal.Actor.on_actor_end_overlap"></a>

#### on_actor_end_overlap

```python
@on_actor_end_overlap.setter
def on_actor_end_overlap(value: ActorEndOverlapSignature) -> None
```

<a id="unreal.Actor.on_actor_un_touch"></a>

#### on_actor_un_touch

```python
@property
def on_actor_un_touch() -> ActorEndOverlapSignature
```

deprecated: 'on_actor_un_touch' was renamed to 'on_actor_end_overlap'.

<a id="unreal.Actor.on_actor_un_touch"></a>

#### on_actor_un_touch

```python
@on_actor_un_touch.setter
def on_actor_un_touch(value: ActorEndOverlapSignature) -> None
```

<a id="unreal.Actor.on_begin_cursor_over"></a>

#### on_begin_cursor_over

```python
@property
def on_begin_cursor_over() -> ActorBeginCursorOverSignature
```

(ActorBeginCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved over this actor if mouse over events are enabled in the player controller.

<a id="unreal.Actor.on_begin_cursor_over"></a>

#### on_begin_cursor_over

```python
@on_begin_cursor_over.setter
def on_begin_cursor_over(value: ActorBeginCursorOverSignature) -> None
```

<a id="unreal.Actor.on_end_cursor_over"></a>

#### on_end_cursor_over

```python
@property
def on_end_cursor_over() -> ActorEndCursorOverSignature
```

(ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.

<a id="unreal.Actor.on_end_cursor_over"></a>

#### on_end_cursor_over

```python
@on_end_cursor_over.setter
def on_end_cursor_over(value: ActorEndCursorOverSignature) -> None
```

<a id="unreal.Actor.on_clicked"></a>

#### on_clicked

```python
@property
def on_clicked() -> ActorOnClickedSignature
```

(ActorOnClickedSignature):  [Read-Write] Called when the left mouse button is clicked while the mouse is over this actor and click events are enabled in the player controller.

<a id="unreal.Actor.on_clicked"></a>

#### on_clicked

```python
@on_clicked.setter
def on_clicked(value: ActorOnClickedSignature) -> None
```

<a id="unreal.Actor.on_released"></a>

#### on_released

```python
@property
def on_released() -> ActorOnReleasedSignature
```

(ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.

<a id="unreal.Actor.on_released"></a>

#### on_released

```python
@on_released.setter
def on_released(value: ActorOnReleasedSignature) -> None
```

<a id="unreal.Actor.on_input_touch_begin"></a>

#### on_input_touch_begin

```python
@property
def on_input_touch_begin() -> ActorOnInputTouchBeginSignature
```

(ActorOnInputTouchBeginSignature):  [Read-Write] Called when a touch input is received over this actor when touch events are enabled in the player controller.

<a id="unreal.Actor.on_input_touch_begin"></a>

#### on_input_touch_begin

```python
@on_input_touch_begin.setter
def on_input_touch_begin(value: ActorOnInputTouchBeginSignature) -> None
```

<a id="unreal.Actor.on_input_touch_end"></a>

#### on_input_touch_end

```python
@property
def on_input_touch_end() -> ActorOnInputTouchEndSignature
```

(ActorOnInputTouchEndSignature):  [Read-Write] Called when a touch input is received over this component when touch events are enabled in the player controller.

<a id="unreal.Actor.on_input_touch_end"></a>

#### on_input_touch_end

```python
@on_input_touch_end.setter
def on_input_touch_end(value: ActorOnInputTouchEndSignature) -> None
```

<a id="unreal.Actor.on_input_touch_enter"></a>

#### on_input_touch_enter

```python
@property
def on_input_touch_enter() -> ActorBeginTouchOverSignature
```

(ActorBeginTouchOverSignature):  [Read-Write] Called when a finger is moved over this actor when touch over events are enabled in the player controller.

<a id="unreal.Actor.on_input_touch_enter"></a>

#### on_input_touch_enter

```python
@on_input_touch_enter.setter
def on_input_touch_enter(value: ActorBeginTouchOverSignature) -> None
```

<a id="unreal.Actor.on_input_touch_leave"></a>

#### on_input_touch_leave

```python
@property
def on_input_touch_leave() -> ActorEndTouchOverSignature
```

(ActorEndTouchOverSignature):  [Read-Write] Called when a finger is moved off this actor when touch over events are enabled in the player controller.

<a id="unreal.Actor.on_input_touch_leave"></a>

#### on_input_touch_leave

```python
@on_input_touch_leave.setter
def on_input_touch_leave(value: ActorEndTouchOverSignature) -> None
```

<a id="unreal.Actor.on_actor_hit"></a>

#### on_actor_hit

```python
@property
def on_actor_hit() -> ActorHitSignature
```

(ActorHitSignature):  [Read-Write] Called when this Actor hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.
note: For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled.

<a id="unreal.Actor.on_actor_hit"></a>

#### on_actor_hit

```python
@on_actor_hit.setter
def on_actor_hit(value: ActorHitSignature) -> None
```

<a id="unreal.Actor.on_destroyed"></a>

#### on_destroyed

```python
@property
def on_destroyed() -> ActorDestroyedSignature
```

(ActorDestroyedSignature):  [Read-Write] Event triggered when the actor has been explicitly destroyed.

<a id="unreal.Actor.on_destroyed"></a>

#### on_destroyed

```python
@on_destroyed.setter
def on_destroyed(value: ActorDestroyedSignature) -> None
```

<a id="unreal.Actor.on_end_play"></a>

#### on_end_play

```python
@property
def on_end_play() -> ActorEndPlaySignature
```

(ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.

<a id="unreal.Actor.on_end_play"></a>

#### on_end_play

```python
@on_end_play.setter
def on_end_play(value: ActorEndPlaySignature) -> None
```

<a id="unreal.Actor.was_recently_rendered"></a>

#### was_recently_rendered

```python
def was_recently_rendered(tolerance: float = 0.200000) -> bool
```

x.was_recently_rendered(tolerance=0.200000) -> bool
Returns true if this actor has been rendered "recently", with a tolerance in seconds to define what "recent" means.
e.g.: If a tolerance of 0.1 is used, this function will return true only if the actor was rendered in the last 0.1 seconds of game time.

Args:
    tolerance (float): How many seconds ago the actor last render time can be and still count as having been "recently" rendered.

Returns:
    bool: Whether this actor was recently rendered.

<a id="unreal.Actor.tear_off"></a>

#### tear_off

```python
def tear_off() -> None
```

x.tear_off() -> None
Networking - Server - TearOff this actor to stop replication to clients. Will set bTearOff to true.

<a id="unreal.Actor.set_tick_group"></a>

#### set_tick_group

```python
def set_tick_group(new_tick_group: TickingGroup) -> None
```

x.set_tick_group(new_tick_group) -> None
Sets the ticking group for this actor.

Args:
    new_tick_group (TickingGroup): the new value to assign

<a id="unreal.Actor.set_tickable_when_paused"></a>

#### set_tickable_when_paused

```python
def set_tickable_when_paused(tickable_when_paused: bool) -> None
```

x.set_tickable_when_paused(tickable_when_paused) -> None
Sets whether this actor can tick when paused.

Args:
    tickable_when_paused (bool):

<a id="unreal.Actor.set_replicates"></a>

#### set_replicates

```python
def set_replicates(replicates: bool) -> None
```

x.set_replicates(replicates) -> None
Set whether this actor replicates to network clients. When this actor is spawned on the server it will be sent to clients as well.
Properties flagged for replication will update on clients if they change on the server.
Internally changes the RemoteRole property and handles the cases where the actor needs to be added to the network actor list.
see: https://docs.unrealengine.com/InteractiveExperiences/Networking/Actors

Args:
    replicates (bool): Whether this Actor replicates to network clients.

<a id="unreal.Actor.set_replicate_movement"></a>

#### set_replicate_movement

```python
def set_replicate_movement(replicate_movement: bool) -> None
```

x.set_replicate_movement(replicate_movement) -> None
Set whether this actor's movement replicates to network clients.

Args:
    replicate_movement (bool): Whether this Actor's movement replicates to clients.

<a id="unreal.Actor.set_ray_tracing_group_id"></a>

#### set_ray_tracing_group_id

```python
def set_ray_tracing_group_id(raytracing_group_id: int) -> None
```

x.set_ray_tracing_group_id(raytracing_group_id) -> None
Specify a RayTracingGroupId for this actors. Components with invalid RayTracingGroupId will inherit the actors.

Args:
    raytracing_group_id (int32):

<a id="unreal.Actor.set_physics_replication_mode"></a>

#### set_physics_replication_mode

```python
def set_physics_replication_mode(
        replication_mode: PhysicsReplicationMode) -> None
```

x.set_physics_replication_mode(replication_mode) -> None
Set the physics replication mode of this body, via EPhysicsReplicationMode

Args:
    replication_mode (PhysicsReplicationMode):

<a id="unreal.Actor.set_owner"></a>

#### set_owner

```python
def set_owner(new_owner: Actor) -> None
```

x.set_owner(new_owner) -> None
Set the owner of this Actor, used primarily for network replication.

Args:
    new_owner (Actor): The Actor who takes over ownership of this Actor

<a id="unreal.Actor.set_net_dormancy"></a>

#### set_net_dormancy

```python
def set_net_dormancy(new_dormancy: NetDormancy) -> None
```

x.set_net_dormancy(new_dormancy) -> None
Puts actor in dormant networking state

Args:
    new_dormancy (NetDormancy):

<a id="unreal.Actor.set_life_span"></a>

#### set_life_span

```python
def set_life_span(lifespan: float) -> None
```

x.set_life_span(lifespan) -> None
Set the lifespan of this actor. When it expires the object will be destroyed. If requested lifespan is 0, the timer is cleared and the actor will not be destroyed.

Args:
    lifespan (float):

<a id="unreal.Actor.set_is_temporarily_hidden_in_editor"></a>

#### set_is_temporarily_hidden_in_editor

```python
def set_is_temporarily_hidden_in_editor(is_hidden: bool) -> None
```

x.set_is_temporarily_hidden_in_editor(is_hidden) -> None
Explicitly sets whether or not this actor is hidden in the editor for the duration of the current editor session

Args:
    is_hidden (bool): True if the actor is hidden

<a id="unreal.Actor.set_folder_path"></a>

#### set_folder_path

```python
def set_folder_path(new_folder_path: Name) -> None
```

x.set_folder_path(new_folder_path) -> None
Assigns a new folder to this actor. Actor folder paths are only available in development builds.

Args:
    new_folder_path (Name): The new folder to assign to the actor.

<a id="unreal.Actor.set_actor_tick_interval"></a>

#### set_actor_tick_interval

```python
def set_actor_tick_interval(tick_interval: float) -> None
```

x.set_actor_tick_interval(tick_interval) -> None
Sets the tick interval of this actor's primary tick function. Will not enable a disabled tick function. Takes effect on next tick.

Args:
    tick_interval (float): The rate at which this actor should be ticking

<a id="unreal.Actor.set_actor_tick_enabled"></a>

#### set_actor_tick_enabled

```python
def set_actor_tick_enabled(enabled: bool) -> None
```

x.set_actor_tick_enabled(enabled) -> None
Set this actor's tick functions to be enabled or disabled. Only has an effect if the function is registered
This only modifies the tick function on actor itself

Args:
    enabled (bool): Whether it should be enabled or not

<a id="unreal.Actor.set_tick_enabled"></a>

#### set_tick_enabled

```python
def set_tick_enabled(enabled: bool) -> None
```

deprecated: 'set_tick_enabled' was renamed to 'set_actor_tick_enabled'.

<a id="unreal.Actor.set_actor_scale3d"></a>

#### set_actor_scale3d

```python
def set_actor_scale3d(new_scale3d: Vector) -> None
```

x.set_actor_scale3d(new_scale3d) -> None
Set the Actor's world-space scale.

Args:
    new_scale3d (Vector):

<a id="unreal.Actor.set_actor_relative_scale3d"></a>

#### set_actor_relative_scale3d

```python
def set_actor_relative_scale3d(new_relative_scale: Vector) -> None
```

x.set_actor_relative_scale3d(new_relative_scale) -> None
Set the actor's RootComponent to the specified relative scale 3d

Args:
    new_relative_scale (Vector): New scale to set the actor's RootComponent to

<a id="unreal.Actor.set_actor_label"></a>

#### set_actor_label

```python
def set_actor_label(new_actor_label: str, mark_dirty: bool = True) -> None
```

x.set_actor_label(new_actor_label, mark_dirty=True) -> None
Assigns a new label to this actor.  Actor labels are only available in development builds.

Args:
    new_actor_label (str): The new label string to assign to the actor.  If empty, the actor will have a default label.
    mark_dirty (bool): If true the actor's package will be marked dirty for saving.  Otherwise it will not be.  You should pass false for this parameter if dirtying is not allowed (like during loads)

<a id="unreal.Actor.set_actor_hidden_in_game"></a>

#### set_actor_hidden_in_game

```python
def set_actor_hidden_in_game(new_hidden: bool) -> None
```

x.set_actor_hidden_in_game(new_hidden) -> None
Sets the actor to be hidden in the game

Args:
    new_hidden (bool): Whether or not to hide the actor and all its components

<a id="unreal.Actor.set_actor_hidden"></a>

#### set_actor_hidden

```python
def set_actor_hidden(new_hidden: bool) -> None
```

deprecated: 'set_actor_hidden' was renamed to 'set_actor_hidden_in_game'.

<a id="unreal.Actor.set_actor_enable_collision"></a>

#### set_actor_enable_collision

```python
def set_actor_enable_collision(new_actor_enable_collision: bool) -> None
```

x.set_actor_enable_collision(new_actor_enable_collision) -> None
Allows enabling/disabling collision for the whole actor

Args:
    new_actor_enable_collision (bool):

<a id="unreal.Actor.remove_tick_prerequisite_component"></a>

#### remove_tick_prerequisite_component

```python
def remove_tick_prerequisite_component(
        prerequisite_component: ActorComponent) -> None
```

x.remove_tick_prerequisite_component(prerequisite_component) -> None
Remove tick dependency on PrerequisiteComponent.

Args:
    prerequisite_component (ActorComponent):

<a id="unreal.Actor.remove_tick_prerequisite_actor"></a>

#### remove_tick_prerequisite_actor

```python
def remove_tick_prerequisite_actor(prerequisite_actor: Actor) -> None
```

x.remove_tick_prerequisite_actor(prerequisite_actor) -> None
Remove tick dependency on PrerequisiteActor.

Args:
    prerequisite_actor (Actor):

<a id="unreal.Actor.receive_tick"></a>

#### receive_tick

```python
def receive_tick(delta_seconds: float) -> None
```

x.receive_tick(delta_seconds) -> None
Event called every frame, if ticking is enabled

Args:
    delta_seconds (float):

<a id="unreal.Actor.receive_radial_damage"></a>

#### receive_radial_damage

```python
def receive_radial_damage(damage_received: float, damage_type: DamageType,
                          origin: Vector, hit_info: HitResult,
                          instigated_by: Controller,
                          damage_causer: Actor) -> None
```

x.receive_radial_damage(damage_received, damage_type, origin, hit_info, instigated_by, damage_causer) -> None
Event when this actor takes RADIAL damage

Args:
    damage_received (float): 
    damage_type (DamageType): 
    origin (Vector): 
    hit_info (HitResult): 
    instigated_by (Controller): 
    damage_causer (Actor):

<a id="unreal.Actor.receive_point_damage"></a>

#### receive_point_damage

```python
def receive_point_damage(damage: float, damage_type: DamageType,
                         hit_location: Vector, hit_normal: Vector,
                         hit_component: PrimitiveComponent, bone_name: Name,
                         shot_from_direction: Vector,
                         instigated_by: Controller, damage_causer: Actor,
                         hit_info: HitResult) -> None
```

x.receive_point_damage(damage, damage_type, hit_location, hit_normal, hit_component, bone_name, shot_from_direction, instigated_by, damage_causer, hit_info) -> None
Event when this actor takes POINT damage

Args:
    damage (float): 
    damage_type (DamageType): 
    hit_location (Vector): 
    hit_normal (Vector): 
    hit_component (PrimitiveComponent): 
    bone_name (Name): 
    shot_from_direction (Vector): 
    instigated_by (Controller): 
    damage_causer (Actor): 
    hit_info (HitResult):

<a id="unreal.Actor.receive_hit"></a>

#### receive_hit

```python
def receive_hit(my_comp: PrimitiveComponent, other: Actor,
                other_comp: PrimitiveComponent, self_moved: bool,
                hit_location: Vector, hit_normal: Vector,
                normal_impulse: Vector, hit: HitResult) -> None
```

x.receive_hit(my_comp, other, other_comp, self_moved, hit_location, hit_normal, normal_impulse, hit) -> None
Event when this actor bumps into a blocking object, or blocks another actor that bumps into it.
This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.
note: For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled.
note: When receiving a hit from another object's movement (bSelfMoved is false), the directions of 'Hit.Normal' and 'Hit.ImpactNormal' will be adjusted to indicate force from the other object against this object.
note: NormalImpulse will be filled in for physics-simulating bodies, but will be zero for swept-component blocking collisions.

Args:
    my_comp (PrimitiveComponent): 
    other (Actor): 
    other_comp (PrimitiveComponent): 
    self_moved (bool): 
    hit_location (Vector): 
    hit_normal (Vector): 
    normal_impulse (Vector): 
    hit (HitResult):

<a id="unreal.Actor.receive_end_play"></a>

#### receive_end_play

```python
def receive_end_play(end_play_reason: EndPlayReason) -> None
```

x.receive_end_play(end_play_reason) -> None
Event to notify blueprints this actor is being deleted or removed from a level.

Args:
    end_play_reason (EndPlayReason):

<a id="unreal.Actor.receive_destroyed"></a>

#### receive_destroyed

```python
def receive_destroyed() -> None
```

x.receive_destroyed() -> None
Called when the actor has been explicitly destroyed.

<a id="unreal.Actor.receive_begin_play"></a>

#### receive_begin_play

```python
def receive_begin_play() -> None
```

x.receive_begin_play() -> None
Event when play begins for this actor.

<a id="unreal.Actor.receive_async_physics_tick"></a>

#### receive_async_physics_tick

```python
def receive_async_physics_tick(delta_seconds: float,
                               sim_seconds: float) -> None
```

x.receive_async_physics_tick(delta_seconds, sim_seconds) -> None
Event called every physics tick if bAsyncPhysicsTickEnabled is true

Args:
    delta_seconds (float): 
    sim_seconds (float):

<a id="unreal.Actor.receive_any_damage"></a>

#### receive_any_damage

```python
def receive_any_damage(damage: float, damage_type: DamageType,
                       instigated_by: Controller,
                       damage_causer: Actor) -> None
```

x.receive_any_damage(damage, damage_type, instigated_by, damage_causer) -> None
Event when this actor takes ANY damage

Args:
    damage (float): 
    damage_type (DamageType): 
    instigated_by (Controller): 
    damage_causer (Actor):

<a id="unreal.Actor.receive_actor_on_released"></a>

#### receive_actor_on_released

```python
def receive_actor_on_released(button_released: Key) -> None
```

x.receive_actor_on_released(button_released) -> None
Event when this actor is under the mouse when left mouse button is released while using the clickable interface.

Args:
    button_released (Key):

<a id="unreal.Actor.receive_actor_on_input_touch_leave"></a>

#### receive_actor_on_input_touch_leave

```python
def receive_actor_on_input_touch_leave(finger_index: TouchIndex) -> None
```

x.receive_actor_on_input_touch_leave(finger_index) -> None
Event when this actor has a finger moved off of it with the clickable interface.

Args:
    finger_index (TouchIndex):

<a id="unreal.Actor.receive_actor_on_input_touch_enter"></a>

#### receive_actor_on_input_touch_enter

```python
def receive_actor_on_input_touch_enter(finger_index: TouchIndex) -> None
```

x.receive_actor_on_input_touch_enter(finger_index) -> None
Event when this actor has a finger moved over it with the clickable interface.

Args:
    finger_index (TouchIndex):

<a id="unreal.Actor.receive_actor_on_input_touch_end"></a>

#### receive_actor_on_input_touch_end

```python
def receive_actor_on_input_touch_end(finger_index: TouchIndex) -> None
```

x.receive_actor_on_input_touch_end(finger_index) -> None
Event when this actor is under the finger when untouched when click events are enabled.

Args:
    finger_index (TouchIndex):

<a id="unreal.Actor.receive_actor_on_input_touch_begin"></a>

#### receive_actor_on_input_touch_begin

```python
def receive_actor_on_input_touch_begin(finger_index: TouchIndex) -> None
```

x.receive_actor_on_input_touch_begin(finger_index) -> None
Event when this actor is touched when click events are enabled.

Args:
    finger_index (TouchIndex):

<a id="unreal.Actor.receive_actor_on_clicked"></a>

#### receive_actor_on_clicked

```python
def receive_actor_on_clicked(button_pressed: Key) -> None
```

x.receive_actor_on_clicked(button_pressed) -> None
Event when this actor is clicked by the mouse when using the clickable interface.

Args:
    button_pressed (Key):

<a id="unreal.Actor.receive_actor_end_overlap"></a>

#### receive_actor_end_overlap

```python
def receive_actor_end_overlap(other_actor: Actor) -> None
```

x.receive_actor_end_overlap(other_actor) -> None
Event when an actor no longer overlaps another actor, and they have separated.
note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.

Args:
    other_actor (Actor):

<a id="unreal.Actor.receive_actor_untouch"></a>

#### receive_actor_untouch

```python
def receive_actor_untouch(other_actor: Actor) -> None
```

deprecated: 'receive_actor_untouch' was renamed to 'receive_actor_end_overlap'.

<a id="unreal.Actor.receive_actor_end_cursor_over"></a>

#### receive_actor_end_cursor_over

```python
def receive_actor_end_cursor_over() -> None
```

x.receive_actor_end_cursor_over() -> None
Event when this actor has the mouse moved off of it with the clickable interface.

<a id="unreal.Actor.receive_actor_begin_overlap"></a>

#### receive_actor_begin_overlap

```python
def receive_actor_begin_overlap(other_actor: Actor) -> None
```

x.receive_actor_begin_overlap(other_actor) -> None
Event when this actor overlaps another actor, for example a player walking into a trigger.
For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.

Args:
    other_actor (Actor):

<a id="unreal.Actor.receive_actor_touch"></a>

#### receive_actor_touch

```python
def receive_actor_touch(other_actor: Actor) -> None
```

deprecated: 'receive_actor_touch' was renamed to 'receive_actor_begin_overlap'.

<a id="unreal.Actor.receive_actor_begin_cursor_over"></a>

#### receive_actor_begin_cursor_over

```python
def receive_actor_begin_cursor_over() -> None
```

x.receive_actor_begin_cursor_over() -> None
Event when this actor has the mouse moved over it with the clickable interface.

<a id="unreal.Actor.prestream_textures"></a>

#### prestream_textures

```python
def prestream_textures(seconds: float,
                       enable_streaming: bool,
                       cinematic_texture_groups: int = 0) -> None
```

x.prestream_textures(seconds, enable_streaming, cinematic_texture_groups=0) -> None
Calls PrestreamTextures() for all the actor's meshcomponents.

Args:
    seconds (float): Number of seconds to force all mip-levels to be resident
    enable_streaming (bool): Whether to start (true) or stop (false) streaming
    cinematic_texture_groups (int32): Bitfield indicating which texture groups that use extra high-resolution mips

<a id="unreal.Actor.make_noise"></a>

#### make_noise

```python
def make_noise(loudness: float = 1.000000,
               noise_instigator: Pawn = None,
               noise_location: Vector = [0.000000, 0.000000, 0.000000],
               max_range: float = 0.000000,
               tag: Name = "None") -> None
```

x.make_noise(loudness=1.000000, noise_instigator=None, noise_location=[0.000000, 0.000000, 0.000000], max_range=0.000000, tag="None") -> None
Trigger a noise caused by a given Pawn, at a given location.
Note that the NoiseInstigator Pawn MUST have a PawnNoiseEmitterComponent for the noise to be detected by a PawnSensingComponent.
Senders of MakeNoise should have an Instigator if they are not pawns, or pass a NoiseInstigator.

Args:
    loudness (float): The relative loudness of this noise. Usual range is 0 (no noise) to 1 (full volume). If MaxRange is used, this scales the max range, otherwise it affects the hearing range specified by the sensor.
    noise_instigator (Pawn): Pawn responsible for this noise.  Uses the actor's Instigator if NoiseInstigator is null
    noise_location (Vector): Position of noise source.  If zero vector, use the actor's location.
    max_range (float): Max range at which the sound may be heard. A value of 0 indicates no max range (though perception may have its own range). Loudness scales the range. (Note: not supported for legacy PawnSensingComponent, only for AIPerception)
    tag (Name): Identifier for the noise.

<a id="unreal.Actor.teleport"></a>

#### teleport

```python
def teleport(dest_location: Vector, dest_rotation: Rotator) -> bool
```

x.teleport(dest_location, dest_rotation) -> bool
Teleport this actor to a new location. If the actor doesn't fit exactly at the location specified, tries to slightly move it out of walls and such.

Args:
    dest_location (Vector): The target destination point
    dest_rotation (Rotator): The target rotation at the destination

Returns:
    bool: true if the actor has been successfully moved, or false if it couldn't fit.

<a id="unreal.Actor.set_actor_transform"></a>

#### set_actor_transform

```python
def set_actor_transform(new_transform: Transform, sweep: bool,
                        teleport: bool) -> Optional[HitResult]
```

x.set_actor_transform(new_transform, sweep, teleport) -> HitResult or None
Set the Actors transform to the specified one.

Args:
    new_transform (Transform): The new transform.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the transform without teleporting will not update the transform of simulated child/attached components.

Returns:
    HitResult or None: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.set_actor_rotation"></a>

#### set_actor_rotation

```python
def set_actor_rotation(new_rotation: Rotator, teleport_physics: bool) -> bool
```

x.set_actor_rotation(new_rotation, teleport_physics) -> bool
Set the Actor's rotation instantly to the specified rotation.

Args:
    new_rotation (Rotator): The new rotation for the Actor.
    teleport_physics (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the rotation without teleporting will not update the rotation of simulated child/attached components.

Returns:
    bool: Whether the rotation was successfully set.

<a id="unreal.Actor.set_actor_relative_transform"></a>

#### set_actor_relative_transform

```python
def set_actor_relative_transform(new_relative_transform: Transform,
                                 sweep: bool, teleport: bool) -> HitResult
```

x.set_actor_relative_transform(new_relative_transform, sweep, teleport) -> HitResult
Set the actor's RootComponent to the specified relative transform

Args:
    new_relative_transform (Transform): New relative transform of the actor's root component
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the transform without teleporting will not update the transform of simulated child/attached components.

Returns:
    HitResult: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.set_actor_relative_rotation"></a>

#### set_actor_relative_rotation

```python
def set_actor_relative_rotation(new_relative_rotation: Rotator, sweep: bool,
                                teleport: bool) -> HitResult
```

x.set_actor_relative_rotation(new_relative_rotation, sweep, teleport) -> HitResult
Set the actor's RootComponent to the specified relative rotation

Args:
    new_relative_rotation (Rotator): New relative rotation of the actor's root component
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the rotation without teleporting will not update the rotation of simulated child/attached components.

Returns:
    HitResult: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.set_actor_relative_location"></a>

#### set_actor_relative_location

```python
def set_actor_relative_location(new_relative_location: Vector, sweep: bool,
                                teleport: bool) -> HitResult
```

x.set_actor_relative_location(new_relative_location, sweep, teleport) -> HitResult
Set the actor's RootComponent to the specified relative location.

Args:
    new_relative_location (Vector): New relative location of the actor's root component
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the location without teleporting will not update the location of simulated child/attached components.

Returns:
    HitResult: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.set_actor_location_and_rotation"></a>

#### set_actor_location_and_rotation

```python
def set_actor_location_and_rotation(new_location: Vector,
                                    new_rotation: Rotator, sweep: bool,
                                    teleport: bool) -> Optional[HitResult]
```

x.set_actor_location_and_rotation(new_location, new_rotation, sweep, teleport) -> HitResult or None
Move the actor instantly to the specified location and rotation.

Args:
    new_location (Vector): The new location to teleport the Actor to.
    new_rotation (Rotator): The new rotation for the Actor.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the location without teleporting will not update the location of simulated child/attached components.

Returns:
    HitResult or None: Whether the rotation was successfully set.

    sweep_hit_result (HitResult): The hit result from the move if swept.

<a id="unreal.Actor.set_actor_location"></a>

#### set_actor_location

```python
def set_actor_location(new_location: Vector, sweep: bool,
                       teleport: bool) -> Optional[HitResult]
```

x.set_actor_location(new_location, sweep, teleport) -> HitResult or None
Move the Actor to the specified location.

Args:
    new_location (Vector): The new location to move the Actor to.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the location without teleporting will not update the location of simulated child/attached components.

Returns:
    HitResult or None: Whether the location was successfully set (if not swept), or whether movement occurred at all (if swept).

    sweep_hit_result (HitResult): The hit result from the move if swept.

<a id="unreal.Actor.on_reset"></a>

#### on_reset

```python
def on_reset() -> None
```

x.on_reset() -> None
Event called when this Actor is reset to its initial state - used when restarting level without reloading.

<a id="unreal.Actor.on_end_view_target"></a>

#### on_end_view_target

```python
def on_end_view_target(pc: PlayerController) -> None
```

x.on_end_view_target(pc) -> None
Event called when this Actor is no longer the view target for the given PlayerController.

Args:
    pc (PlayerController):

<a id="unreal.Actor.on_become_view_target"></a>

#### on_become_view_target

```python
def on_become_view_target(pc: PlayerController) -> None
```

x.on_become_view_target(pc) -> None
Event called when this Actor becomes the view target for the given PlayerController.

Args:
    pc (PlayerController):

<a id="unreal.Actor.get_components_by_class"></a>

#### get_components_by_class

```python
def get_components_by_class(
        component_class: Class = None) -> Array[ActorComponent]
```

x.get_components_by_class(component_class=None) -> Array[ActorComponent]
Gets all the components that inherit from the given class.
Currently returns an array of UActorComponent which must be cast to the correct type.
This intended to only be used by blueprints. Use GetComponents() in C++.

Args:
    component_class (type(Class)): 

Returns:
    Array[ActorComponent]:

<a id="unreal.Actor.get_actor_rotation"></a>

#### get_actor_rotation

```python
def get_actor_rotation() -> Rotator
```

x.get_actor_rotation() -> Rotator
Returns rotation of the RootComponent of this Actor.

Returns:
    Rotator:

<a id="unreal.Actor.get_actor_location"></a>

#### get_actor_location

```python
def get_actor_location() -> Vector
```

x.get_actor_location() -> Vector
Returns the location of the RootComponent of this Actor

Returns:
    Vector:

<a id="unreal.Actor.detach_from_actor"></a>

#### detach_from_actor

```python
def detach_from_actor(
        location_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE,
        rotation_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE,
        scale_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE) -> None
```

x.detach_from_actor(location_rule=DetachmentRule.KEEP_RELATIVE, rotation_rule=DetachmentRule.KEEP_RELATIVE, scale_rule=DetachmentRule.KEEP_RELATIVE) -> None
Detaches the RootComponent of this Actor from any SceneComponent it is currently attached to.

Args:
    location_rule (DetachmentRule): How to handle translation when detaching.
    rotation_rule (DetachmentRule): How to handle rotation when detaching.
    scale_rule (DetachmentRule): How to handle scale when detaching.

<a id="unreal.Actor.destroy_actor"></a>

#### destroy_actor

```python
def destroy_actor() -> None
```

x.destroy_actor() -> None
Destroy the actor

<a id="unreal.Actor.attach_to_component"></a>

#### attach_to_component

```python
def attach_to_component(parent: SceneComponent,
                        socket_name: Name,
                        location_rule: AttachmentRule,
                        rotation_rule: AttachmentRule,
                        scale_rule: AttachmentRule,
                        weld_simulated_bodies: bool = True) -> bool
```

x.attach_to_component(parent, socket_name, location_rule, rotation_rule, scale_rule, weld_simulated_bodies=True) -> bool
Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

Args:
    parent (SceneComponent): Parent to attach to.
    socket_name (Name): Optional socket to attach to on the parent.
    location_rule (AttachmentRule): How to handle translation when attaching.
    rotation_rule (AttachmentRule): How to handle rotation when attaching.
    scale_rule (AttachmentRule): How to handle scale when attaching.
    weld_simulated_bodies (bool): Whether to weld together simulated physics bodies. This transfers the shapes in the welded object into the parent (if simulated), which can result in permanent changes that persist even after subsequently detaching.

Returns:
    bool: Whether the attachment was successful or not

<a id="unreal.Actor.attach_to_actor"></a>

#### attach_to_actor

```python
def attach_to_actor(parent_actor: Actor,
                    socket_name: Name,
                    location_rule: AttachmentRule,
                    rotation_rule: AttachmentRule,
                    scale_rule: AttachmentRule,
                    weld_simulated_bodies: bool = True) -> bool
```

x.attach_to_actor(parent_actor, socket_name, location_rule, rotation_rule, scale_rule, weld_simulated_bodies=True) -> bool
Attaches the RootComponent of this Actor to the supplied actor, optionally at a named socket.

Args:
    parent_actor (Actor): Actor to attach this actor's RootComponent to
    socket_name (Name): Socket name to attach to, if any
    location_rule (AttachmentRule): How to handle translation when attaching.
    rotation_rule (AttachmentRule): How to handle rotation when attaching.
    scale_rule (AttachmentRule): How to handle scale when attaching.
    weld_simulated_bodies (bool): Whether to weld together simulated physics bodies.This transfers the shapes in the welded object into the parent (if simulated), which can result in permanent changes that persist even after subsequently detaching.

Returns:
    bool: Whether the attachment was successful or not

<a id="unreal.Actor.add_actor_world_transform_keep_scale"></a>

#### add_actor_world_transform_keep_scale

```python
def add_actor_world_transform_keep_scale(delta_transform: Transform,
                                         sweep: bool,
                                         teleport: bool) -> HitResult
```

x.add_actor_world_transform_keep_scale(delta_transform, sweep, teleport) -> HitResult
Adds a delta to the transform of this actor in world space. Scale is unchanged.

Args:
    delta_transform (Transform): 
    sweep (bool): 
    teleport (bool): 

Returns:
    HitResult: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.add_actor_world_transform"></a>

#### add_actor_world_transform

```python
def add_actor_world_transform(delta_transform: Transform, sweep: bool,
                              teleport: bool) -> HitResult
```

x.add_actor_world_transform(delta_transform, sweep, teleport) -> HitResult
Adds a delta to the transform of this actor in world space. Ignores scale and sets it to (1,1,1).

Args:
    delta_transform (Transform): 
    sweep (bool): 
    teleport (bool): 

Returns:
    HitResult: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.add_actor_world_rotation"></a>

#### add_actor_world_rotation

```python
def add_actor_world_rotation(delta_rotation: Rotator, sweep: bool,
                             teleport: bool) -> HitResult
```

x.add_actor_world_rotation(delta_rotation, sweep, teleport) -> HitResult
Adds a delta to the rotation of this actor in world space.

Args:
    delta_rotation (Rotator): The change in rotation.
    sweep (bool): Whether to sweep to the target rotation (not currently supported for rotation).
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the rotation without teleporting will not update the rotation of simulated child/attached components.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): The hit result from the move if swept.

<a id="unreal.Actor.add_actor_world_offset"></a>

#### add_actor_world_offset

```python
def add_actor_world_offset(delta_location: Vector, sweep: bool,
                           teleport: bool) -> HitResult
```

x.add_actor_world_offset(delta_location, sweep, teleport) -> HitResult
Adds a delta to the location of this actor in world space.

Args:
    delta_location (Vector): The change in location.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the location without teleporting will not update the location of simulated child/attached components.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): The hit result from the move if swept.

<a id="unreal.Actor.add_actor_local_transform"></a>

#### add_actor_local_transform

```python
def add_actor_local_transform(new_transform: Transform, sweep: bool,
                              teleport: bool) -> HitResult
```

x.add_actor_local_transform(new_transform, sweep, teleport) -> HitResult
Adds a delta to the transform of this component in its local reference frame

Args:
    new_transform (Transform): The change in transform in local space.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the transform without teleporting will not update the transform of simulated child/attached components.

Returns:
    HitResult: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.add_actor_local_rotation"></a>

#### add_actor_local_rotation

```python
def add_actor_local_rotation(delta_rotation: Rotator, sweep: bool,
                             teleport: bool) -> HitResult
```

x.add_actor_local_rotation(delta_rotation, sweep, teleport) -> HitResult
Adds a delta to the rotation of this component in its local reference frame

Args:
    delta_rotation (Rotator): The change in rotation in local space.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the rotation without teleporting will not update the rotation of simulated child/attached components.

Returns:
    HitResult: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.add_actor_local_offset"></a>

#### add_actor_local_offset

```python
def add_actor_local_offset(delta_location: Vector, sweep: bool,
                           teleport: bool) -> HitResult
```

x.add_actor_local_offset(delta_location, sweep, teleport) -> HitResult
Adds a delta to the location of this component in its local reference frame.

Args:
    delta_location (Vector): 
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire swept volume. Note that when teleporting, any child/attached components will be teleported too, maintaining their current offset even if they are being simulated. Setting the location without teleporting will not update the location of simulated child/attached components.

Returns:
    HitResult: 

    sweep_hit_result (HitResult):

<a id="unreal.Actor.is_temporarily_hidden_in_editor"></a>

#### is_temporarily_hidden_in_editor

```python
def is_temporarily_hidden_in_editor(include_parent: bool = False) -> bool
```

x.is_temporarily_hidden_in_editor(include_parent=False) -> bool
Returns whether or not this actor was explicitly hidden in the editor for the duration of the current editor session

Args:
    include_parent (bool): Whether to recurse up child actor hierarchy or not

Returns:
    bool:

<a id="unreal.Actor.is_selectable"></a>

#### is_selectable

```python
def is_selectable() -> bool
```

x.is_selectable() -> bool
Returns true if this actor can EVER be selected in a level in the editor.  Can be overridden by specific actors to make them unselectable.

Returns:
    bool:

<a id="unreal.Actor.is_overlapping_actor"></a>

#### is_overlapping_actor

```python
def is_overlapping_actor(other: Actor) -> bool
```

x.is_overlapping_actor(other) -> bool
Check whether any component of this Actor is overlapping any component of another Actor.

Args:
    other (Actor): The other Actor to test against

Returns:
    bool: Whether any component of this Actor is overlapping any component of another Actor.

<a id="unreal.Actor.is_hidden_ed_at_startup"></a>

#### is_hidden_ed_at_startup

```python
def is_hidden_ed_at_startup() -> bool
```

x.is_hidden_ed_at_startup() -> bool
Returns true if the actor is hidden upon editor startup/by default, false if it is not

Returns:
    bool:

<a id="unreal.Actor.is_hidden_ed"></a>

#### is_hidden_ed

```python
def is_hidden_ed() -> bool
```

x.is_hidden_ed() -> bool
Returns true if this actor is hidden in the editor viewports, also checking temporary flags.

Returns:
    bool:

<a id="unreal.Actor.is_editable"></a>

#### is_editable

```python
def is_editable() -> bool
```

x.is_editable() -> bool
Returns true if this actor is allowed to be displayed, selected and manipulated by the editor.

Returns:
    bool:

<a id="unreal.Actor.is_child_actor"></a>

#### is_child_actor

```python
def is_child_actor() -> bool
```

x.is_child_actor() -> bool
Returns whether this Actor was spawned by a child actor component

Returns:
    bool:

<a id="unreal.Actor.is_actor_tick_enabled"></a>

#### is_actor_tick_enabled

```python
def is_actor_tick_enabled() -> bool
```

x.is_actor_tick_enabled() -> bool
Returns whether this actor has tick enabled or not

Returns:
    bool:

<a id="unreal.Actor.is_actor_being_destroyed"></a>

#### is_actor_being_destroyed

```python
def is_actor_being_destroyed() -> bool
```

x.is_actor_being_destroyed() -> bool
Returns true if this actor is currently being destroyed, some gameplay events may be unsafe

Returns:
    bool:

<a id="unreal.Actor.has_authority"></a>

#### has_authority

```python
def has_authority() -> bool
```

x.has_authority() -> bool
Returns whether this actor has network authority

Returns:
    bool:

<a id="unreal.Actor.get_vertical_distance_to"></a>

#### get_vertical_distance_to

```python
def get_vertical_distance_to(other_actor: Actor) -> float
```

x.get_vertical_distance_to(other_actor) -> float
Returns the distance from this Actor to OtherActor, ignoring XY.

Args:
    other_actor (Actor): 

Returns:
    float:

<a id="unreal.Actor.get_velocity"></a>

#### get_velocity

```python
def get_velocity() -> Vector
```

x.get_velocity() -> Vector
Returns velocity (in cm/s (Unreal Units/second) of the rootcomponent if it is either using physics or has an associated MovementComponent

Returns:
    Vector:

<a id="unreal.Actor.get_actor_transform"></a>

#### get_actor_transform

```python
def get_actor_transform() -> Transform
```

x.get_actor_transform() -> Transform
Get the actor-to-world transform.

Returns:
    Transform: The transform that transforms from actor space to world space.

<a id="unreal.Actor.get_tickable_when_paused"></a>

#### get_tickable_when_paused

```python
def get_tickable_when_paused() -> bool
```

x.get_tickable_when_paused() -> bool
Gets whether this actor can tick when paused.

Returns:
    bool:

<a id="unreal.Actor.get_squared_horizontal_distance_to"></a>

#### get_squared_horizontal_distance_to

```python
def get_squared_horizontal_distance_to(other_actor: Actor) -> float
```

x.get_squared_horizontal_distance_to(other_actor) -> float
Returns the squared distance from this Actor to OtherActor, ignoring Z.

Args:
    other_actor (Actor): 

Returns:
    float:

<a id="unreal.Actor.get_squared_distance_to"></a>

#### get_squared_distance_to

```python
def get_squared_distance_to(other_actor: Actor) -> float
```

x.get_squared_distance_to(other_actor) -> float
Returns the squared distance from this Actor to OtherActor.

Args:
    other_actor (Actor): 

Returns:
    float:

<a id="unreal.Actor.get_resimulation_threshold"></a>

#### get_resimulation_threshold

```python
def get_resimulation_threshold() -> float
```

x.get_resimulation_threshold() -> float
Get the error threshold in centimeters before this object should enforce a resimulation to trigger.

Returns:
    float:

<a id="unreal.Actor.get_remote_role"></a>

#### get_remote_role

```python
def get_remote_role() -> NetRole
```

x.get_remote_role() -> NetRole
Returns how much control the remote machine has over this actor.

Returns:
    NetRole:

<a id="unreal.Actor.get_ray_tracing_group_id"></a>

#### get_ray_tracing_group_id

```python
def get_ray_tracing_group_id() -> int
```

x.get_ray_tracing_group_id() -> int32
Return the RayTracingGroupId for this actor.

Returns:
    int32:

<a id="unreal.Actor.get_physics_replication_mode"></a>

#### get_physics_replication_mode

```python
def get_physics_replication_mode() -> PhysicsReplicationMode
```

x.get_physics_replication_mode() -> PhysicsReplicationMode
Get the physics replication mode of this body, via EPhysicsReplicationMode

Returns:
    PhysicsReplicationMode:

<a id="unreal.Actor.get_parent_component"></a>

#### get_parent_component

```python
def get_parent_component() -> ChildActorComponent
```

x.get_parent_component() -> ChildActorComponent
If this Actor was created by a Child Actor Component returns that Child Actor Component

Returns:
    ChildActorComponent:

<a id="unreal.Actor.get_parent_actor"></a>

#### get_parent_actor

```python
def get_parent_actor() -> Actor
```

x.get_parent_actor() -> Actor
If this Actor was created by a Child Actor Component returns the Actor that owns that Child Actor Component

Returns:
    Actor:

<a id="unreal.Actor.get_owner"></a>

#### get_owner

```python
def get_owner() -> Actor
```

x.get_owner() -> Actor
Get the owner of this Actor, used primarily for network replication.

Returns:
    Actor:

<a id="unreal.Actor.get_overlapping_components"></a>

#### get_overlapping_components

```python
def get_overlapping_components() -> Array[PrimitiveComponent]
```

x.get_overlapping_components() -> Array[PrimitiveComponent]
Returns list of components this actor is overlapping.

Returns:
    Array[PrimitiveComponent]: 

    overlapping_components (Array[PrimitiveComponent]):

<a id="unreal.Actor.get_touching_components"></a>

#### get_touching_components

```python
def get_touching_components() -> Array[PrimitiveComponent]
```

deprecated: 'get_touching_components' was renamed to 'get_overlapping_components'.

<a id="unreal.Actor.get_overlapping_actors"></a>

#### get_overlapping_actors

```python
def get_overlapping_actors(class_filter: Class = None) -> Array[Actor]
```

x.get_overlapping_actors(class_filter=None) -> Array[Actor]
Returns list of actors this actor is overlapping (any component overlapping any component). Does not return itself.

Args:
    class_filter (type(Class)): [optional] If set, only returns actors of this class or subclasses

Returns:
    Array[Actor]: 

    overlapping_actors (Array[Actor]): [out] Returned list of overlapping actors

<a id="unreal.Actor.get_touching_actors"></a>

#### get_touching_actors

```python
def get_touching_actors(class_filter: Class = None) -> Array[Actor]
```

deprecated: 'get_touching_actors' was renamed to 'get_overlapping_actors'.

<a id="unreal.Actor.get_local_role"></a>

#### get_local_role

```python
def get_local_role() -> NetRole
```

x.get_local_role() -> NetRole
Returns how much control the local machine has over this actor.

Returns:
    NetRole:

<a id="unreal.Actor.get_life_span"></a>

#### get_life_span

```python
def get_life_span() -> float
```

x.get_life_span() -> float
Get the remaining lifespan of this actor. If zero is returned the actor lives forever.

Returns:
    float:

<a id="unreal.Actor.get_level_transform"></a>

#### get_level_transform

```python
def get_level_transform() -> Transform
```

x.get_level_transform() -> Transform
Return the FTransform of the level this actor is a part of.

Returns:
    Transform:

<a id="unreal.Actor.get_level"></a>

#### get_level

```python
def get_level() -> Level
```

x.get_level() -> Level
Return the ULevel that this Actor is part of.

Returns:
    Level:

<a id="unreal.Actor.get_instigator_controller"></a>

#### get_instigator_controller

```python
def get_instigator_controller() -> Controller
```

x.get_instigator_controller() -> Controller
Returns the instigator's controller for this actor, or nullptr if there is none.

Returns:
    Controller:

<a id="unreal.Actor.get_instigator"></a>

#### get_instigator

```python
def get_instigator() -> Pawn
```

x.get_instigator() -> Pawn
Returns the instigator for this actor, or nullptr if there is none.

Returns:
    Pawn:

<a id="unreal.Actor.get_horizontal_dot_product_to"></a>

#### get_horizontal_dot_product_to

```python
def get_horizontal_dot_product_to(other_actor: Actor) -> float
```

x.get_horizontal_dot_product_to(other_actor) -> float
Returns the dot product from this Actor to OtherActor, ignoring Z. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

Args:
    other_actor (Actor): 

Returns:
    float:

<a id="unreal.Actor.get_horizontal_distance_to"></a>

#### get_horizontal_distance_to

```python
def get_horizontal_distance_to(other_actor: Actor) -> float
```

x.get_horizontal_distance_to(other_actor) -> float
Returns the distance from this Actor to OtherActor, ignoring Z.

Args:
    other_actor (Actor): 

Returns:
    float:

<a id="unreal.Actor.get_game_time_since_creation"></a>

#### get_game_time_since_creation

```python
def get_game_time_since_creation() -> float
```

x.get_game_time_since_creation() -> float
The number of seconds (in game time) since this Actor was created, relative to Get Game Time In Seconds.

Returns:
    float:

<a id="unreal.Actor.get_folder_path"></a>

#### get_folder_path

```python
def get_folder_path() -> Name
```

x.get_folder_path() -> Name
Returns this actor's folder path. Actor folder paths are only available in development builds.

Returns:
    Name:

<a id="unreal.Actor.get_dot_product_to"></a>

#### get_dot_product_to

```python
def get_dot_product_to(other_actor: Actor) -> float
```

x.get_dot_product_to(other_actor) -> float
Returns the dot product from this Actor to OtherActor. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

Args:
    other_actor (Actor): 

Returns:
    float:

<a id="unreal.Actor.get_distance_to"></a>

#### get_distance_to

```python
def get_distance_to(other_actor: Actor) -> float
```

x.get_distance_to(other_actor) -> float
Returns the distance from this Actor to OtherActor.

Args:
    other_actor (Actor): 

Returns:
    float:

<a id="unreal.Actor.get_default_actor_label"></a>

#### get_default_actor_label

```python
def get_default_actor_label() -> str
```

x.get_default_actor_label() -> str
Returns this actor's default label (does not include any numeric suffix).  Actor labels are only available in development builds.

Returns:
    str:

<a id="unreal.Actor.get_components_by_tag"></a>

#### get_components_by_tag

```python
def get_components_by_tag(component_class: Class = None,
                          tag: Name = ...) -> Array[ActorComponent]
```

x.get_components_by_tag(component_class=None, tag) -> Array[ActorComponent]
Gets all the components that inherit from the given class with a given tag.

Args:
    component_class (type(Class)): 
    tag (Name): 

Returns:
    Array[ActorComponent]:

<a id="unreal.Actor.get_components_by_interface"></a>

#### get_components_by_interface

```python
def get_components_by_interface(interface: Class) -> Array[ActorComponent]
```

x.get_components_by_interface(interface) -> Array[ActorComponent]
Gets all the components that implements the given interface.

Args:
    interface (type(Class)): 

Returns:
    Array[ActorComponent]:

<a id="unreal.Actor.get_component_by_class"></a>

#### get_component_by_class

```python
def get_component_by_class(component_class: Class = None) -> ActorComponent
```

x.get_component_by_class(component_class=None) -> ActorComponent
Searches components array and returns first encountered component of the specified class

Args:
    component_class (type(Class)): 

Returns:
    ActorComponent:

<a id="unreal.Actor.get_attach_parent_socket_name"></a>

#### get_attach_parent_socket_name

```python
def get_attach_parent_socket_name() -> Name
```

x.get_attach_parent_socket_name() -> Name
Walk up the attachment chain from RootComponent until we encounter a different actor, and return the socket name in the component. If we are not attached to a component in a different actor, returns NAME_None

Returns:
    Name:

<a id="unreal.Actor.get_attach_parent_actor"></a>

#### get_attach_parent_actor

```python
def get_attach_parent_actor() -> Actor
```

x.get_attach_parent_actor() -> Actor
Walk up the attachment chain from RootComponent until we encounter a different actor, and return it. If we are not attached to a component in a different actor, returns nullptr

Returns:
    Actor:

<a id="unreal.Actor.get_attached_actors"></a>

#### get_attached_actors

```python
def get_attached_actors(
        reset_array: bool = True,
        recursively_include_attached_actors: bool = False) -> Array[Actor]
```

x.get_attached_actors(reset_array=True, recursively_include_attached_actors=False) -> Array[Actor]
Find all Actors which are attached directly to a component in this actor

Args:
    reset_array (bool): 
    recursively_include_attached_actors (bool): 

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]):

<a id="unreal.Actor.get_all_child_actors"></a>

#### get_all_child_actors

```python
def get_all_child_actors(include_descendants: bool = True) -> Array[Actor]
```

x.get_all_child_actors(include_descendants=True) -> Array[Actor]
Returns a list of all actors spawned by our Child Actor Components, including children of children.
This does not return the contents of the Children array

Args:
    include_descendants (bool): 

Returns:
    Array[Actor]: 

    child_actors (Array[Actor]):

<a id="unreal.Actor.get_actor_up_vector"></a>

#### get_actor_up_vector

```python
def get_actor_up_vector() -> Vector
```

x.get_actor_up_vector() -> Vector
Get the up (Z) vector (length 1.0) from this Actor, in world space.

Returns:
    Vector:

<a id="unreal.Actor.get_actor_time_dilation"></a>

#### get_actor_time_dilation

```python
def get_actor_time_dilation() -> float
```

x.get_actor_time_dilation() -> float
Get ActorTimeDilation - this can be used for input control or speed control for slomo.
We don't want to scale input globally because input can be used for UI, which do not care for TimeDilation.

Returns:
    float:

<a id="unreal.Actor.get_actor_tick_interval"></a>

#### get_actor_tick_interval

```python
def get_actor_tick_interval() -> float
```

x.get_actor_tick_interval() -> float
Returns the tick interval of this actor's primary tick function

Returns:
    float:

<a id="unreal.Actor.get_actor_scale3d"></a>

#### get_actor_scale3d

```python
def get_actor_scale3d() -> Vector
```

x.get_actor_scale3d() -> Vector
Returns the Actor's world-space scale.

Returns:
    Vector:

<a id="unreal.Actor.get_actor_right_vector"></a>

#### get_actor_right_vector

```python
def get_actor_right_vector() -> Vector
```

x.get_actor_right_vector() -> Vector
Get the right (Y) vector (length 1.0) from this Actor, in world space.

Returns:
    Vector:

<a id="unreal.Actor.get_actor_relative_scale3d"></a>

#### get_actor_relative_scale3d

```python
def get_actor_relative_scale3d() -> Vector
```

x.get_actor_relative_scale3d() -> Vector
Return the actor's relative scale 3d

Returns:
    Vector:

<a id="unreal.Actor.get_actor_label"></a>

#### get_actor_label

```python
def get_actor_label(create_if_none: bool = True) -> str
```

x.get_actor_label(create_if_none=True) -> str
Returns this actor's current label.  Actor labels are only available in development builds.

Args:
    create_if_none (bool): 

Returns:
    str:

<a id="unreal.Actor.get_actor_forward_vector"></a>

#### get_actor_forward_vector

```python
def get_actor_forward_vector() -> Vector
```

x.get_actor_forward_vector() -> Vector
Get the forward (X) vector (length 1.0) from this Actor, in world space.

Returns:
    Vector:

<a id="unreal.Actor.get_actor_eyes_view_point"></a>

#### get_actor_eyes_view_point

```python
def get_actor_eyes_view_point() -> Tuple[Vector, Rotator]
```

x.get_actor_eyes_view_point() -> (out_location=Vector, out_rotation=Rotator)
Returns the point of view of the actor.
Note that this doesn't mean the camera, but the 'eyes' of the actor.
For example, for a Pawn, this would define the eye height location,
and view rotation (which is different from the pawn rotation which has a zeroed pitch component).
A camera first person view will typically use this view point. Most traces (weapon, AI) will be done from this view point.

Returns:
    tuple: 

    out_location (Vector): location of view point

    out_rotation (Rotator): view rotation of actor.

<a id="unreal.Actor.get_actor_enable_collision"></a>

#### get_actor_enable_collision

```python
def get_actor_enable_collision() -> bool
```

x.get_actor_enable_collision() -> bool
Get current state of collision for the whole actor

Returns:
    bool:

<a id="unreal.Actor.get_actor_bounds"></a>

#### get_actor_bounds

```python
def get_actor_bounds(
        only_colliding_components: bool,
        include_from_child_actors: bool = False) -> Tuple[Vector, Vector]
```

x.get_actor_bounds(only_colliding_components, include_from_child_actors=False) -> (origin=Vector, box_extent=Vector)
Returns the bounding box of all components that make up this Actor (excluding ChildActorComponents).

Args:
    only_colliding_components (bool): If true, will only return the bounding box for components with collision enabled.
    include_from_child_actors (bool): If true then recurse in to ChildActor components

Returns:
    tuple: 

    origin (Vector): Set to the center of the actor in world space

    box_extent (Vector): Set to half the actor's size in 3d space

<a id="unreal.Actor.force_net_update"></a>

#### force_net_update

```python
def force_net_update() -> None
```

x.force_net_update() -> None
Force actor to be updated to clients/demo net drivers

<a id="unreal.Actor.flush_net_dormancy"></a>

#### flush_net_dormancy

```python
def flush_net_dormancy() -> None
```

x.flush_net_dormancy() -> None
Forces dormant actor to replicate but doesn't change NetDormancy state (i.e., they will go dormant again if left dormant)

<a id="unreal.Actor.find_component_by_tag"></a>

#### find_component_by_tag

```python
def find_component_by_tag(component_class: Class = None,
                          tag: Name = ...) -> ActorComponent
```

x.find_component_by_tag(component_class=None, tag) -> ActorComponent
Searches components array and returns first encountered component with a given tag.

Args:
    component_class (type(Class)): 
    tag (Name): 

Returns:
    ActorComponent:

<a id="unreal.Actor.enable_input"></a>

#### enable_input

```python
def enable_input(player_controller: PlayerController) -> None
```

x.enable_input(player_controller) -> None
Pushes this actor on to the stack of input being handled by a PlayerController.

Args:
    player_controller (PlayerController): The PlayerController whose input events we want to receive.

<a id="unreal.Actor.disable_input"></a>

#### disable_input

```python
def disable_input(player_controller: PlayerController) -> None
```

x.disable_input(player_controller) -> None
Removes this actor from the stack of input being handled by a PlayerController.

Args:
    player_controller (PlayerController): The PlayerController whose input events we no longer want to receive. If null, this actor will stop receiving input from all PlayerControllers.

<a id="unreal.Actor.create_input_component"></a>

#### create_input_component

```python
def create_input_component(input_component_to_create: Class) -> None
```

x.create_input_component(input_component_to_create) -> None
Creates an input component from the input component passed in

Args:
    input_component_to_create (type(Class)): The UInputComponent to create.

<a id="unreal.Actor.can_trigger_resimulation"></a>

#### can_trigger_resimulation

```python
def can_trigger_resimulation() -> bool
```

x.can_trigger_resimulation() -> bool
Can this body trigger a resimulation when Physics Prediction is enabled

Returns:
    bool:

<a id="unreal.Actor.add_tick_prerequisite_component"></a>

#### add_tick_prerequisite_component

```python
def add_tick_prerequisite_component(
        prerequisite_component: ActorComponent) -> None
```

x.add_tick_prerequisite_component(prerequisite_component) -> None
Make this actor tick after PrerequisiteComponent. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

Args:
    prerequisite_component (ActorComponent):

<a id="unreal.Actor.add_tick_prerequisite_actor"></a>

#### add_tick_prerequisite_actor

```python
def add_tick_prerequisite_actor(prerequisite_actor: Actor) -> None
```

x.add_tick_prerequisite_actor(prerequisite_actor) -> None
Make this actor tick after PrerequisiteActor. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

Args:
    prerequisite_actor (Actor):

<a id="unreal.Actor.set_tick_prerequisite"></a>

#### set_tick_prerequisite

```python
def set_tick_prerequisite(prerequisite_actor: Actor) -> None
```

deprecated: 'set_tick_prerequisite' was renamed to 'add_tick_prerequisite_actor'.

<a id="unreal.Actor.actor_has_tag"></a>

#### actor_has_tag

```python
def actor_has_tag(tag: Name) -> bool
```

x.actor_has_tag(tag) -> bool
See if this actor's Tags array contains the supplied name tag

Args:
    tag (Name): 

Returns:
    bool:

<a id="unreal.Actor.has_tag"></a>

#### has_tag

```python
def has_tag(tag: Name) -> bool
```

deprecated: 'has_tag' was renamed to 'actor_has_tag'.

<a id="unreal.Actor.acquire_editor_element_handle"></a>

#### acquire_editor_element_handle

```python
def acquire_editor_element_handle(
        allow_create: bool = True) -> ScriptTypedElementHandle
```

x.acquire_editor_element_handle(allow_create=True) -> ScriptTypedElementHandle
K2 Acquire Editor Actor Element Handle

Args:
    allow_create (bool): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.Actor.get_actor_local_bounds_pcg"></a>

#### get_actor_local_bounds_pcg

```python
def get_actor_local_bounds_pcg(
        ignore_pcg_created_components: bool = True) -> Box
```

x.get_actor_local_bounds_pcg(ignore_pcg_created_components=True) -> Box
Get Actor Local Bounds PCG

Args:
    ignore_pcg_created_components (bool): 

Returns:
    Box:

<a id="unreal.Actor.get_actor_bounds_pcg"></a>

#### get_actor_bounds_pcg

```python
def get_actor_bounds_pcg(ignore_pcg_created_components: bool = True) -> Box
```

x.get_actor_bounds_pcg(ignore_pcg_created_components=True) -> Box
Get Actor Bounds PCG

Args:
    ignore_pcg_created_components (bool): 

Returns:
    Box:

<a id="unreal.Actor.create_pcg_data_from_actor"></a>

#### create_pcg_data_from_actor

```python
def create_pcg_data_from_actor(parse_actor: bool = True) -> PCGData
```

x.create_pcg_data_from_actor(parse_actor=True) -> PCGData
Create PCGData from Actor

Args:
    parse_actor (bool): 

Returns:
    PCGData:

<a id="unreal.VREditorAvatarActor"></a>