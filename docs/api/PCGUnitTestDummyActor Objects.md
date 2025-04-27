## PCGUnitTestDummyActor Objects

```python
class PCGUnitTestDummyActor(Actor)
```

PCGUnit Test Dummy Actor

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGetActorPropertyTest.h

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
- ``array_of_ints_property`` (Array[int32]):  [Read-Write]
- ``array_of_objects_property`` (Array[PCGDummyGetPropertyTest]):  [Read-Write]
- ``array_of_structs_property`` (Array[PCGTestMyColorStruct]):  [Read-Write]
- ``array_of_vectors_property`` (Array[Vector]):  [Read-Write]
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``bool_property`` (bool):  [Read-Write]
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``class_property`` (type(Class)):  [Read-Write]
- ``color_property`` (Color):  [Read-Write]
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
- ``double_property`` (double):  [Read-Write]
- ``dummy_struct`` (PCGDummyGetPropertyStruct):  [Read-Write]
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enum_property`` (PCGUnitTestDummyEnum):  [Read-Write]
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``float_property`` (float):  [Read-Write]
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
- ``int64_property`` (int64):  [Read-Write]
- ``int_property`` (int32):  [Read-Write]
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``linear_color_property`` (LinearColor):  [Read-Write]
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``name_property`` (Name):  [Read-Write]
- ``net_cull_distance_squared`` (float):  [Read-Write]
- ``net_dormancy`` (NetDormancy):  [Read-Write] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.
- ``net_load_on_client`` (bool):  [Read-Write] This actor will be loaded on network clients during map load
- ``net_priority`` (float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate
- ``net_update_frequency`` (float):  [Read-Write]
- ``net_use_owner_relevancy`` (bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority
- ``object_property`` (PCGDummyGetPropertyTest):  [Read-Write]
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
- ``pcg_color_property`` (PCGTestMyColorStruct):  [Read-Write]
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``quat_property`` (Quat):  [Read-Write]
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
- ``rotator_property`` (Rotator):  [Read-Write]
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``set_of_ints_property`` (Array[int32]):  [Read-Write]
- ``soft_class_path_property`` (SoftClassPath):  [Read-Write]
- ``soft_object_path_property`` (SoftObjectPath):  [Read-Write]
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``string_property`` (str):  [Read-Write]
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``transform_property`` (Transform):  [Read-Write]
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
- ``vector2_property`` (Vector2D):  [Read-Write]
- ``vector4_property`` (Vector4):  [Read-Write]
- ``vector_property`` (Vector):  [Read-Write]

<a id="unreal.PCGUnitTestDummyActor.int_property"></a>

#### int_property

```python
@property
def int_property() -> int
```

(int32):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.float_property"></a>

#### float_property

```python
@property
def float_property() -> float
```

(float):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.int64_property"></a>

#### int64_property

```python
@property
def int64_property() -> int
```

(int64):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.double_property"></a>

#### double_property

```python
@property
def double_property() -> float
```

(double):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.bool_property"></a>

#### bool_property

```python
@property
def bool_property() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.name_property"></a>

#### name_property

```python
@property
def name_property() -> Name
```

(Name):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.string_property"></a>

#### string_property

```python
@property
def string_property() -> str
```

(str):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.enum_property"></a>

#### enum_property

```python
@property
def enum_property() -> PCGUnitTestDummyEnum
```

(PCGUnitTestDummyEnum):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.vector_property"></a>

#### vector_property

```python
@property
def vector_property() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.vector4_property"></a>

#### vector4_property

```python
@property
def vector4_property() -> Vector4
```

(Vector4):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.transform_property"></a>

#### transform_property

```python
@property
def transform_property() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.rotator_property"></a>

#### rotator_property

```python
@property
def rotator_property() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.quat_property"></a>

#### quat_property

```python
@property
def quat_property() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.soft_object_path_property"></a>

#### soft_object_path_property

```python
@property
def soft_object_path_property() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.soft_class_path_property"></a>

#### soft_class_path_property

```python
@property
def soft_class_path_property() -> SoftClassPath
```

(SoftClassPath):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.class_property"></a>

#### class_property

```python
@property
def class_property() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.object_property"></a>

#### object_property

```python
@property
def object_property() -> PCGDummyGetPropertyTest
```

(PCGDummyGetPropertyTest):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.vector2_property"></a>

#### vector2_property

```python
@property
def vector2_property() -> Vector2D
```

(Vector2D):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.color_property"></a>

#### color_property

```python
@property
def color_property() -> Color
```

(Color):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.linear_color_property"></a>

#### linear_color_property

```python
@property
def linear_color_property() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.pcg_color_property"></a>

#### pcg_color_property

```python
@property
def pcg_color_property() -> PCGTestMyColorStruct
```

(PCGTestMyColorStruct):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.array_of_ints_property"></a>

#### array_of_ints_property

```python
@property
def array_of_ints_property() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.array_of_vectors_property"></a>

#### array_of_vectors_property

```python
@property
def array_of_vectors_property() -> Array[Vector]
```

(Array[Vector]):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.array_of_structs_property"></a>

#### array_of_structs_property

```python
@property
def array_of_structs_property() -> Array[PCGTestMyColorStruct]
```

(Array[PCGTestMyColorStruct]):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.array_of_objects_property"></a>

#### array_of_objects_property

```python
@property
def array_of_objects_property() -> Array[PCGDummyGetPropertyTest]
```

(Array[PCGDummyGetPropertyTest]):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.dummy_struct"></a>

#### dummy_struct

```python
@property
def dummy_struct() -> PCGDummyGetPropertyStruct
```

(PCGDummyGetPropertyStruct):  [Read-Only]

<a id="unreal.PCGUnitTestDummyActor.set_of_ints_property"></a>

#### set_of_ints_property

```python
@property
def set_of_ints_property() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.PCGUnitTestDummyComponent"></a>