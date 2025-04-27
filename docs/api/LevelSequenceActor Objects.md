## LevelSequenceActor Objects

```python
class LevelSequenceActor(Actor)
```

Actor responsible for controlling a specific level sequence in the world.

**C++ Source:**

- **Module**: LevelSequence
- **File**: LevelSequenceActor.h

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
- ``binding_overrides`` (MovieSceneBindingOverrides):  [Read-Write] Mapping of actors to override the sequence bindings with
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``burn_in_options`` (LevelSequenceBurnInOptions):  [Read-Write]
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``camera_settings`` (LevelSequenceCameraSettings):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_instance_data`` (Object):  [Read-Write] Instance data that can be used to dynamically control sequence evaluation at runtime
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
- ``level_sequence_asset`` (LevelSequence):  [Read-Write]
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
- ``override_instance_data`` (bool):  [Read-Write] Enable specification of dynamic instance data to be supplied to the sequence during playback
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``playback_settings`` (MovieSceneSequencePlaybackSettings):  [Read-Write]
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
- ``replicate_playback`` (bool):  [Read-Write] If true, playback of this level sequence on the server will be synchronized across other clients
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects and the replicated actor components list
  When false the replication system will instead call the virtual ReplicateSubobjects() function where the subobjects and actor components need to be manually replicated.
- ``replicated_movement`` (RepMovement):  [Read-Write] Used for replication of our RootComponent's position and velocity
- ``replicates`` (bool):  [Read-Write] If true, this actor will replicate to remote machines
  see: SetReplicates()
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``sequence_player`` (LevelSequencePlayer):  [Read-Write]
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

<a id="unreal.LevelSequenceActor.playback_settings"></a>

#### playback_settings

```python
@property
def playback_settings() -> MovieSceneSequencePlaybackSettings
```

(MovieSceneSequencePlaybackSettings):  [Read-Only]

<a id="unreal.LevelSequenceActor.sequence_player"></a>

#### sequence_player

```python
@property
def sequence_player() -> LevelSequencePlayer
```

(LevelSequencePlayer):  [Read-Only]

<a id="unreal.LevelSequenceActor.level_sequence_asset"></a>

#### level_sequence_asset

```python
@property
def level_sequence_asset() -> LevelSequence
```

(LevelSequence):  [Read-Only]

<a id="unreal.LevelSequenceActor.camera_settings"></a>

#### camera_settings

```python
@property
def camera_settings() -> LevelSequenceCameraSettings
```

(LevelSequenceCameraSettings):  [Read-Write]

<a id="unreal.LevelSequenceActor.camera_settings"></a>

#### camera_settings

```python
@camera_settings.setter
def camera_settings(value: LevelSequenceCameraSettings) -> None
```

<a id="unreal.LevelSequenceActor.burn_in_options"></a>

#### burn_in_options

```python
@property
def burn_in_options() -> LevelSequenceBurnInOptions
```

(LevelSequenceBurnInOptions):  [Read-Only]

<a id="unreal.LevelSequenceActor.binding_overrides"></a>

#### binding_overrides

```python
@property
def binding_overrides() -> MovieSceneBindingOverrides
```

(MovieSceneBindingOverrides):  [Read-Only] Mapping of actors to override the sequence bindings with

<a id="unreal.LevelSequenceActor.override_instance_data"></a>

#### override_instance_data

```python
@property
def override_instance_data() -> bool
```

(bool):  [Read-Write] Enable specification of dynamic instance data to be supplied to the sequence during playback

<a id="unreal.LevelSequenceActor.override_instance_data"></a>

#### override_instance_data

```python
@override_instance_data.setter
def override_instance_data(value: bool) -> None
```

<a id="unreal.LevelSequenceActor.replicate_playback"></a>

#### replicate_playback

```python
@property
def replicate_playback() -> bool
```

(bool):  [Read-Write] If true, playback of this level sequence on the server will be synchronized across other clients

<a id="unreal.LevelSequenceActor.replicate_playback"></a>

#### replicate_playback

```python
@replicate_playback.setter
def replicate_playback(value: bool) -> None
```

<a id="unreal.LevelSequenceActor.default_instance_data"></a>

#### default_instance_data

```python
@property
def default_instance_data() -> Object
```

(Object):  [Read-Write] Instance data that can be used to dynamically control sequence evaluation at runtime

<a id="unreal.LevelSequenceActor.default_instance_data"></a>

#### default_instance_data

```python
@default_instance_data.setter
def default_instance_data(value: Object) -> None
```

<a id="unreal.LevelSequenceActor.show_burnin"></a>

#### show_burnin

```python
def show_burnin() -> None
```

x.show_burnin() -> None
Show burnin

<a id="unreal.LevelSequenceActor.set_sequence"></a>

#### set_sequence

```python
def set_sequence(sequence: LevelSequence) -> None
```

x.set_sequence(sequence) -> None
Set the level sequence being played by this actor.
see: GetSequence

Args:
    sequence (LevelSequence): The sequence object to set.

<a id="unreal.LevelSequenceActor.set_binding_by_tag"></a>

#### set_binding_by_tag

```python
def set_binding_by_tag(binding_tag: Name,
                       actors: Array[Actor],
                       allow_bindings_from_asset: bool = False) -> None
```

x.set_binding_by_tag(binding_tag, actors, allow_bindings_from_asset=False) -> None
Assigns an set of actors to all the bindings tagged with the specified name in this sequence. Object Bindings can be tagged within the sequence UI by RMB -> Tags... on the object binding in the tree.

Args:
    binding_tag (Name): The unique tag name to lookup bindings with
    actors (Array[Actor]): The actors to assign to all the tagged bindings
    allow_bindings_from_asset (bool): If false the new bindings being supplied here will replace the bindings set in the level sequence asset, meaning the original object animated by Sequencer will no longer be animated. Bindings set to spawnables will not spawn if false. If true, new bindings will be in addition to ones set set in Sequencer UI. This function will not modify the original asset.

<a id="unreal.LevelSequenceActor.set_binding"></a>

#### set_binding

```python
def set_binding(binding: MovieSceneObjectBindingID,
                actors: Array[Actor],
                allow_bindings_from_asset: bool = False) -> None
```

x.set_binding(binding, actors, allow_bindings_from_asset=False) -> None
Overrides the specified binding with the specified actors, optionally still allowing the bindings defined in the Level Sequence asset

Args:
    binding (MovieSceneObjectBindingID): Binding to modify
    actors (Array[Actor]): Actors to bind
    allow_bindings_from_asset (bool): If false the new bindings being supplied here will replace the bindings set in the level sequence asset, meaning the original object animated by Sequencer will no longer be animated. Bindings set to spawnables will not spawn if false. If true, new bindings will be in addition to ones set set in Sequencer UI. This function will not modify the original asset.

<a id="unreal.LevelSequenceActor.reset_bindings"></a>

#### reset_bindings

```python
def reset_bindings() -> None
```

x.reset_bindings() -> None
Resets all overridden bindings back to the defaults defined by the Level Sequence asset

<a id="unreal.LevelSequenceActor.reset_binding"></a>

#### reset_binding

```python
def reset_binding(binding: MovieSceneObjectBindingID) -> None
```

x.reset_binding(binding) -> None
Resets the specified binding back to the defaults defined by the Level Sequence asset

Args:
    binding (MovieSceneObjectBindingID):

<a id="unreal.LevelSequenceActor.remove_binding_by_tag"></a>

#### remove_binding_by_tag

```python
def remove_binding_by_tag(tag: Name, actor: Actor) -> None
```

x.remove_binding_by_tag(tag, actor) -> None
Removes the specified actor from the specified binding's actor array

Args:
    tag (Name): 
    actor (Actor):

<a id="unreal.LevelSequenceActor.remove_binding"></a>

#### remove_binding

```python
def remove_binding(binding: MovieSceneObjectBindingID, actor: Actor) -> None
```

x.remove_binding(binding, actor) -> None
Removes the specified actor from the specified binding's actor array

Args:
    binding (MovieSceneObjectBindingID): 
    actor (Actor):

<a id="unreal.LevelSequenceActor.hide_burnin"></a>

#### hide_burnin

```python
def hide_burnin() -> None
```

x.hide_burnin() -> None
Hide burnin

<a id="unreal.LevelSequenceActor.get_sequence"></a>

#### get_sequence

```python
def get_sequence() -> LevelSequence
```

x.get_sequence() -> LevelSequence
Get the level sequence being played by this actor.
see: SetSequence

Returns:
    LevelSequence: Level sequence, or nullptr if not assigned or if it cannot be loaded.

<a id="unreal.LevelSequenceActor.find_named_bindings"></a>

#### find_named_bindings

```python
def find_named_bindings(tag: Name) -> Array[MovieSceneObjectBindingID]
```

x.find_named_bindings(tag) -> Array[MovieSceneObjectBindingID]
Retrieve all the bindings that have been tagged with the specified name

Args:
    tag (Name): The unique tag name to lookup bindings with. Object Bindings can be tagged within the sequence UI by RMB -> Tags... on the object binding in the tree.

Returns:
    Array[MovieSceneObjectBindingID]: An array containing all the bindings that are tagged with this name, potentially empty.

<a id="unreal.LevelSequenceActor.find_named_binding"></a>

#### find_named_binding

```python
def find_named_binding(tag: Name) -> MovieSceneObjectBindingID
```

x.find_named_binding(tag) -> MovieSceneObjectBindingID
Retrieve the first object binding that has been tagged with the specified name

Args:
    tag (Name): 

Returns:
    MovieSceneObjectBindingID:

<a id="unreal.LevelSequenceActor.add_binding_by_tag"></a>

#### add_binding_by_tag

```python
def add_binding_by_tag(binding_tag: Name,
                       actor: Actor,
                       allow_bindings_from_asset: bool = False) -> None
```

x.add_binding_by_tag(binding_tag, actor, allow_bindings_from_asset=False) -> None
Binds an actor to all the bindings tagged with the specified name in this sequence. Does not remove any exising bindings that have been set up through this API. Object Bindings can be tagged within the sequence UI by RMB -> Tags... on the object binding in the tree.

Args:
    binding_tag (Name): The unique tag name to lookup bindings with
    actor (Actor): The actor to assign to all the tagged bindings
    allow_bindings_from_asset (bool): If false the new bindings being supplied here will replace the bindings set in the level sequence asset, meaning the original object animated by Sequencer will no longer be animated. Bindings set to spawnables will not spawn if false. If true, new bindings will be in addition to ones set set in Sequencer UI. This function will not modify the original asset.

<a id="unreal.LevelSequenceActor.add_binding"></a>

#### add_binding

```python
def add_binding(binding: MovieSceneObjectBindingID,
                actor: Actor,
                allow_bindings_from_asset: bool = False) -> None
```

x.add_binding(binding, actor, allow_bindings_from_asset=False) -> None
Adds the specified actor to the overridden bindings for the specified binding ID, optionally still allowing the bindings defined in the Level Sequence asset

Args:
    binding (MovieSceneObjectBindingID): Binding to modify
    actor (Actor): Actor to bind
    allow_bindings_from_asset (bool): If false the new bindings being supplied here will replace the bindings set in the level sequence asset, meaning the original object animated by Sequencer will no longer be animated. Bindings set to spawnables will not spawn if false. If true, new bindings will be in addition to ones set set in Sequencer UI. This function will not modify the original asset.

<a id="unreal.ReplicatedLevelSequenceActor"></a>