## PlayerCameraManager Objects

```python
class PlayerCameraManager(Actor)
```

A PlayerCameraManager is responsible for managing the camera for a particular
player. It defines the final view properties used by other systems (e.g. the renderer),
meaning you can think of it as your virtual eyeball in the world. It can compute the
final camera properties directly, or it can arbitrate/blend between other objects or
actors that influence the camera (e.g. blending from one CameraActor to another).

The PlayerCameraManagers primary external responsibility is to reliably respond to
various Get*() functions, such as GetCameraViewPoint. Most everything else is
implementation detail and overrideable by user projects.

By default, a PlayerCameraManager maintains a "view target", which is the primary actor
the camera is associated with. It can also apply various "post" effects to the final
view state, such as camera animations, shakes, post-process effects or special
effects such as dirt on the lens.
see: https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Camera/

**C++ Source:**

- **Module**: Engine
- **File**: PlayerCameraManager.h

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
- ``auto_calculate_ortho_planes`` (bool):  [Read-Write] True when this camera should automatically calculated the Near+Far planes
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_plane_shift`` (float):  [Read-Write] Manually adjusts the planes of this camera, maintaining the distance between them. Positive moves out to the farplane, negative towards the near plane
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``client_simulating_view_target`` (bool):  [Read-Write] True if clients are handling setting their own viewtarget and the server should not replicate it.
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_aspect_ratio`` (float):  [Read-Write] Default aspect ratio. Most of the time the value from a camera component will be used instead.
- ``default_constrain_aspect_ratio`` (bool):  [Read-Write] True if black bars should be added if the destination view has a different aspect ratio (only used when a view target doesn't specify whether or not to constrain the aspect ratio; most of the time the value from a camera component is used instead)
- ``default_fov`` (float):  [Read-Write] FOV to use by default.
- ``default_modifiers`` (Array[type(Class)]):  [Read-Write] List of modifiers to create by default for this camera
- ``default_ortho_width`` (float):  [Read-Write] The default desired width (in world units) of the orthographic view (ignored in Perspective mode)
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
- ``free_cam_distance`` (float):  [Read-Write] Distance to place free camera from view target (used in certain CameraStyles)
- ``free_cam_offset`` (Vector):  [Read-Write] Offset to Z free camera position (used in certain CameraStyles)
- ``game_camera_cut_this_frame`` (bool):  [Read-Write] True if we did a camera cut this frame. Automatically reset to false every frame.
  This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur).
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
- ``is_orthographic`` (bool):  [Read-Write] True when this camera should use an orthographic perspective instead of FOV
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
- ``on_audio_fade_change_event`` (OnAudioFadeChangeSignature):  [Read-Write] If bound, broadcast on fade start (with fade time) instead of manually altering audio device's primary volume directly
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
- ``transform_component`` (SceneComponent):  [Read-Only] Dummy component we can use to attach things to the camera.
- ``update_ortho_planes`` (bool):  [Read-Write] Adjusts the near/far planes and the view origin of the current camera automatically to avoid clipping and light artefacting
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
- ``use_camera_height_as_view_target`` (bool):  [Read-Write] If UpdateOrthoPlanes is enabled, this setting will use the cameras current height to compensate the distance to the general view (as a pseudo distance to view target when one isn't present)
- ``use_client_side_camera_updates`` (bool):  [Read-Write] True if server will use camera positions replicated from the client instead of calculating them locally.
- ``view_pitch_max`` (float):  [Read-Write] Maximum view pitch, in degrees.
- ``view_pitch_min`` (float):  [Read-Write] Minimum view pitch, in degrees.
- ``view_roll_max`` (float):  [Read-Write] Maximum view roll, in degrees.
- ``view_roll_min`` (float):  [Read-Write] Minimum view roll, in degrees.
- ``view_target_offset`` (Vector):  [Read-Write] Offset to view target (used in certain CameraStyles)
- ``view_yaw_max`` (float):  [Read-Write] Maximum view yaw, in degrees.
- ``view_yaw_min`` (float):  [Read-Write] Minimum view yaw, in degrees.

<a id="unreal.PlayerCameraManager.transform_component"></a>

#### transform_component

```python
@property
def transform_component() -> SceneComponent
```

(SceneComponent):  [Read-Only] Dummy component we can use to attach things to the camera.

<a id="unreal.PlayerCameraManager.default_fov"></a>

#### default_fov

```python
@property
def default_fov() -> float
```

(float):  [Read-Write] FOV to use by default.

<a id="unreal.PlayerCameraManager.default_fov"></a>

#### default_fov

```python
@default_fov.setter
def default_fov(value: float) -> None
```

<a id="unreal.PlayerCameraManager.default_ortho_width"></a>

#### default_ortho_width

```python
@property
def default_ortho_width() -> float
```

(float):  [Read-Write] The default desired width (in world units) of the orthographic view (ignored in Perspective mode)

<a id="unreal.PlayerCameraManager.default_ortho_width"></a>

#### default_ortho_width

```python
@default_ortho_width.setter
def default_ortho_width(value: float) -> None
```

<a id="unreal.PlayerCameraManager.default_aspect_ratio"></a>

#### default_aspect_ratio

```python
@property
def default_aspect_ratio() -> float
```

(float):  [Read-Write] Default aspect ratio. Most of the time the value from a camera component will be used instead.

<a id="unreal.PlayerCameraManager.default_aspect_ratio"></a>

#### default_aspect_ratio

```python
@default_aspect_ratio.setter
def default_aspect_ratio(value: float) -> None
```

<a id="unreal.PlayerCameraManager.default_modifiers"></a>

#### default_modifiers

```python
@property
def default_modifiers() -> Array[Class]
```

(Array[type(Class)]):  [Read-Only] List of modifiers to create by default for this camera

<a id="unreal.PlayerCameraManager.free_cam_distance"></a>

#### free_cam_distance

```python
@property
def free_cam_distance() -> float
```

(float):  [Read-Write] Distance to place free camera from view target (used in certain CameraStyles)

<a id="unreal.PlayerCameraManager.free_cam_distance"></a>

#### free_cam_distance

```python
@free_cam_distance.setter
def free_cam_distance(value: float) -> None
```

<a id="unreal.PlayerCameraManager.free_cam_offset"></a>

#### free_cam_offset

```python
@property
def free_cam_offset() -> Vector
```

(Vector):  [Read-Write] Offset to Z free camera position (used in certain CameraStyles)

<a id="unreal.PlayerCameraManager.free_cam_offset"></a>

#### free_cam_offset

```python
@free_cam_offset.setter
def free_cam_offset(value: Vector) -> None
```

<a id="unreal.PlayerCameraManager.view_target_offset"></a>

#### view_target_offset

```python
@property
def view_target_offset() -> Vector
```

(Vector):  [Read-Write] Offset to view target (used in certain CameraStyles)

<a id="unreal.PlayerCameraManager.view_target_offset"></a>

#### view_target_offset

```python
@view_target_offset.setter
def view_target_offset(value: Vector) -> None
```

<a id="unreal.PlayerCameraManager.on_audio_fade_change_event"></a>

#### on_audio_fade_change_event

```python
@property
def on_audio_fade_change_event() -> OnAudioFadeChangeSignature
```

(OnAudioFadeChangeSignature):  [Read-Write] If bound, broadcast on fade start (with fade time) instead of manually altering audio device's primary volume directly

<a id="unreal.PlayerCameraManager.on_audio_fade_change_event"></a>

#### on_audio_fade_change_event

```python
@on_audio_fade_change_event.setter
def on_audio_fade_change_event(value: OnAudioFadeChangeSignature) -> None
```

<a id="unreal.PlayerCameraManager.is_orthographic"></a>

#### is_orthographic

```python
@property
def is_orthographic() -> bool
```

(bool):  [Read-Write] True when this camera should use an orthographic perspective instead of FOV

<a id="unreal.PlayerCameraManager.is_orthographic"></a>

#### is_orthographic

```python
@is_orthographic.setter
def is_orthographic(value: bool) -> None
```

<a id="unreal.PlayerCameraManager.auto_calculate_ortho_planes"></a>

#### auto_calculate_ortho_planes

```python
@property
def auto_calculate_ortho_planes() -> bool
```

(bool):  [Read-Write] True when this camera should automatically calculated the Near+Far planes

<a id="unreal.PlayerCameraManager.auto_calculate_ortho_planes"></a>

#### auto_calculate_ortho_planes

```python
@auto_calculate_ortho_planes.setter
def auto_calculate_ortho_planes(value: bool) -> None
```

<a id="unreal.PlayerCameraManager.auto_plane_shift"></a>

#### auto_plane_shift

```python
@property
def auto_plane_shift() -> float
```

(float):  [Read-Write] Manually adjusts the planes of this camera, maintaining the distance between them. Positive moves out to the farplane, negative towards the near plane

<a id="unreal.PlayerCameraManager.auto_plane_shift"></a>

#### auto_plane_shift

```python
@auto_plane_shift.setter
def auto_plane_shift(value: float) -> None
```

<a id="unreal.PlayerCameraManager.update_ortho_planes"></a>

#### update_ortho_planes

```python
@property
def update_ortho_planes() -> bool
```

(bool):  [Read-Write] Adjusts the near/far planes and the view origin of the current camera automatically to avoid clipping and light artefacting

<a id="unreal.PlayerCameraManager.update_ortho_planes"></a>

#### update_ortho_planes

```python
@update_ortho_planes.setter
def update_ortho_planes(value: bool) -> None
```

<a id="unreal.PlayerCameraManager.use_camera_height_as_view_target"></a>

#### use_camera_height_as_view_target

```python
@property
def use_camera_height_as_view_target() -> bool
```

(bool):  [Read-Write] If UpdateOrthoPlanes is enabled, this setting will use the cameras current height to compensate the distance to the general view (as a pseudo distance to view target when one isn't present)

<a id="unreal.PlayerCameraManager.use_camera_height_as_view_target"></a>

#### use_camera_height_as_view_target

```python
@use_camera_height_as_view_target.setter
def use_camera_height_as_view_target(value: bool) -> None
```

<a id="unreal.PlayerCameraManager.default_constrain_aspect_ratio"></a>

#### default_constrain_aspect_ratio

```python
@property
def default_constrain_aspect_ratio() -> bool
```

(bool):  [Read-Write] True if black bars should be added if the destination view has a different aspect ratio (only used when a view target doesn't specify whether or not to constrain the aspect ratio; most of the time the value from a camera component is used instead)

<a id="unreal.PlayerCameraManager.default_constrain_aspect_ratio"></a>

#### default_constrain_aspect_ratio

```python
@default_constrain_aspect_ratio.setter
def default_constrain_aspect_ratio(value: bool) -> None
```

<a id="unreal.PlayerCameraManager.client_simulating_view_target"></a>

#### client_simulating_view_target

```python
@property
def client_simulating_view_target() -> bool
```

(bool):  [Read-Write] True if clients are handling setting their own viewtarget and the server should not replicate it.

<a id="unreal.PlayerCameraManager.client_simulating_view_target"></a>

#### client_simulating_view_target

```python
@client_simulating_view_target.setter
def client_simulating_view_target(value: bool) -> None
```

<a id="unreal.PlayerCameraManager.use_client_side_camera_updates"></a>

#### use_client_side_camera_updates

```python
@property
def use_client_side_camera_updates() -> bool
```

(bool):  [Read-Only] True if server will use camera positions replicated from the client instead of calculating them locally.

<a id="unreal.PlayerCameraManager.game_camera_cut_this_frame"></a>

#### game_camera_cut_this_frame

```python
@property
def game_camera_cut_this_frame() -> bool
```

(bool):  [Read-Only] True if we did a camera cut this frame. Automatically reset to false every frame.
This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur).

<a id="unreal.PlayerCameraManager.view_pitch_min"></a>

#### view_pitch_min

```python
@property
def view_pitch_min() -> float
```

(float):  [Read-Write] Minimum view pitch, in degrees.

<a id="unreal.PlayerCameraManager.view_pitch_min"></a>

#### view_pitch_min

```python
@view_pitch_min.setter
def view_pitch_min(value: float) -> None
```

<a id="unreal.PlayerCameraManager.view_pitch_max"></a>

#### view_pitch_max

```python
@property
def view_pitch_max() -> float
```

(float):  [Read-Write] Maximum view pitch, in degrees.

<a id="unreal.PlayerCameraManager.view_pitch_max"></a>

#### view_pitch_max

```python
@view_pitch_max.setter
def view_pitch_max(value: float) -> None
```

<a id="unreal.PlayerCameraManager.view_yaw_min"></a>

#### view_yaw_min

```python
@property
def view_yaw_min() -> float
```

(float):  [Read-Write] Minimum view yaw, in degrees.

<a id="unreal.PlayerCameraManager.view_yaw_min"></a>

#### view_yaw_min

```python
@view_yaw_min.setter
def view_yaw_min(value: float) -> None
```

<a id="unreal.PlayerCameraManager.view_yaw_max"></a>

#### view_yaw_max

```python
@property
def view_yaw_max() -> float
```

(float):  [Read-Write] Maximum view yaw, in degrees.

<a id="unreal.PlayerCameraManager.view_yaw_max"></a>

#### view_yaw_max

```python
@view_yaw_max.setter
def view_yaw_max(value: float) -> None
```

<a id="unreal.PlayerCameraManager.view_roll_min"></a>

#### view_roll_min

```python
@property
def view_roll_min() -> float
```

(float):  [Read-Write] Minimum view roll, in degrees.

<a id="unreal.PlayerCameraManager.view_roll_min"></a>

#### view_roll_min

```python
@view_roll_min.setter
def view_roll_min(value: float) -> None
```

<a id="unreal.PlayerCameraManager.view_roll_max"></a>

#### view_roll_max

```python
@property
def view_roll_max() -> float
```

(float):  [Read-Write] Maximum view roll, in degrees.

<a id="unreal.PlayerCameraManager.view_roll_max"></a>

#### view_roll_max

```python
@view_roll_max.setter
def view_roll_max(value: float) -> None
```

<a id="unreal.PlayerCameraManager.stop_camera_shake"></a>

#### stop_camera_shake

```python
def stop_camera_shake(shake_instance: CameraShakeBase,
                      immediately: bool = True) -> None
```

x.stop_camera_shake(shake_instance, immediately=True) -> None
Immediately stops the given shake instance and invalidates it.

Args:
    shake_instance (CameraShakeBase): 
    immediately (bool):

<a id="unreal.PlayerCameraManager.stop_camera_fade"></a>

#### stop_camera_fade

```python
def stop_camera_fade() -> None
```

x.stop_camera_fade() -> None
Stops camera fading.

<a id="unreal.PlayerCameraManager.stop_all_instances_of_camera_shake_from_source"></a>

#### stop_all_instances_of_camera_shake_from_source

```python
def stop_all_instances_of_camera_shake_from_source(
        shake: Class,
        source_component: CameraShakeSourceComponent,
        immediately: bool = True) -> None
```

x.stop_all_instances_of_camera_shake_from_source(shake, source_component, immediately=True) -> None
Stops playing all shakes of the given class originating from the given source.

Args:
    shake (type(Class)): 
    source_component (CameraShakeSourceComponent): 
    immediately (bool):

<a id="unreal.PlayerCameraManager.stop_all_instances_of_camera_shake"></a>

#### stop_all_instances_of_camera_shake

```python
def stop_all_instances_of_camera_shake(shake: Class,
                                       immediately: bool = True) -> None
```

x.stop_all_instances_of_camera_shake(shake, immediately=True) -> None
Stops playing all shakes of the given class.

Args:
    shake (type(Class)): 
    immediately (bool):

<a id="unreal.PlayerCameraManager.stop_all_camera_shakes_from_source"></a>

#### stop_all_camera_shakes_from_source

```python
def stop_all_camera_shakes_from_source(
        source_component: CameraShakeSourceComponent,
        immediately: bool = True) -> None
```

x.stop_all_camera_shakes_from_source(source_component, immediately=True) -> None
Stops playing all shakes originating from the given source.

Args:
    source_component (CameraShakeSourceComponent): 
    immediately (bool):

<a id="unreal.PlayerCameraManager.stop_all_camera_shakes"></a>

#### stop_all_camera_shakes

```python
def stop_all_camera_shakes(immediately: bool = True) -> None
```

x.stop_all_camera_shakes(immediately=True) -> None
Stops all active camera shakes on this camera.

Args:
    immediately (bool):

<a id="unreal.PlayerCameraManager.start_camera_shake_from_source"></a>

#### start_camera_shake_from_source

```python
def start_camera_shake_from_source(
    shake_class: Class,
    source_component: CameraShakeSourceComponent,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> CameraShakeBase
```

x.start_camera_shake_from_source(shake_class, source_component, scale=1.000000, play_space=CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot=[0.000000, 0.000000, 0.000000]) -> CameraShakeBase
Plays a camera shake on this camera.

Args:
    shake_class (type(Class)): 
    source_component (CameraShakeSourceComponent): The source from which the camera shake originates.
    scale (float): Applies an additional constant scale on top of the dynamic scale computed with the distance to the source
    play_space (CameraShakePlaySpace): Which coordinate system to play the shake in (affects oscillations and camera anims)
    user_play_space_rot (Rotator): Coordinate system to play shake when PlaySpace == CAPS_UserDefined.

Returns:
    CameraShakeBase:

<a id="unreal.PlayerCameraManager.play_camera_shake_from_source"></a>

#### play_camera_shake_from_source

```python
def play_camera_shake_from_source(
    shake_class: Class,
    source_component: CameraShakeSourceComponent,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> CameraShakeBase
```

deprecated: 'play_camera_shake_from_source' was renamed to 'start_camera_shake_from_source'.

<a id="unreal.PlayerCameraManager.start_matinee_camera_shake_from_source"></a>

#### start_matinee_camera_shake_from_source

```python
def start_matinee_camera_shake_from_source(
    shake_class: Class,
    source_component: CameraShakeSourceComponent,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> CameraShakeBase
```

deprecated: 'start_matinee_camera_shake_from_source' was renamed to 'start_camera_shake_from_source'.

<a id="unreal.PlayerCameraManager.start_camera_shake"></a>

#### start_camera_shake

```python
def start_camera_shake(
    shake_class: Class,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> CameraShakeBase
```

x.start_camera_shake(shake_class, scale=1.000000, play_space=CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot=[0.000000, 0.000000, 0.000000]) -> CameraShakeBase
Plays a camera shake on this camera.

Args:
    shake_class (type(Class)): 
    scale (float): Scalar defining how "intense" to play the shake. 1.0 is normal (as authored).
    play_space (CameraShakePlaySpace): Which coordinate system to play the shake in (affects oscillations and camera anims)
    user_play_space_rot (Rotator): Coordinate system to play shake when PlaySpace == CAPS_UserDefined.

Returns:
    CameraShakeBase:

<a id="unreal.PlayerCameraManager.play_camera_shake"></a>

#### play_camera_shake

```python
def play_camera_shake(
    shake_class: Class,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> CameraShakeBase
```

deprecated: 'play_camera_shake' was renamed to 'start_camera_shake'.

<a id="unreal.PlayerCameraManager.start_matinee_camera_shake"></a>

#### start_matinee_camera_shake

```python
def start_matinee_camera_shake(
    shake_class: Class,
    scale: float = 1.000000,
    play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
    user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]
) -> CameraShakeBase
```

deprecated: 'start_matinee_camera_shake' was renamed to 'start_camera_shake'.

<a id="unreal.PlayerCameraManager.start_camera_fade"></a>

#### start_camera_fade

```python
def start_camera_fade(from_alpha: float,
                      to_alpha: float,
                      duration: float,
                      color: LinearColor,
                      should_fade_audio: bool = False,
                      hold_when_finished: bool = False) -> None
```

x.start_camera_fade(from_alpha, to_alpha, duration, color, should_fade_audio=False, hold_when_finished=False) -> None
Does a camera fade to/from a solid color.  Animates automatically.

Args:
    from_alpha (float): Alpha at which to begin the fade. Range [0..1], where 0 is fully transparent and 1 is fully opaque solid color.
    to_alpha (float): Alpha at which to finish the fade.
    duration (float): How long the fade should take, in seconds.
    color (LinearColor): Color to fade to/from.
    should_fade_audio (bool): True to fade audio volume along with the alpha of the solid color.
    hold_when_finished (bool): True for fade to hold at the ToAlpha until explicitly stopped (e.g. with StopCameraFade)

<a id="unreal.PlayerCameraManager.set_manual_camera_fade"></a>

#### set_manual_camera_fade

```python
def set_manual_camera_fade(fade_amount: float, color: LinearColor,
                           fade_audio: bool) -> None
```

x.set_manual_camera_fade(fade_amount, color, fade_audio) -> None
Turns on camera fading at the given opacity. Does not auto-animate, allowing user to animate themselves.
Call StopCameraFade to turn fading back off.

Args:
    fade_amount (float): 
    color (LinearColor): 
    fade_audio (bool):

<a id="unreal.PlayerCameraManager.set_game_camera_cut_this_frame"></a>

#### set_game_camera_cut_this_frame

```python
def set_game_camera_cut_this_frame() -> None
```

x.set_game_camera_cut_this_frame() -> None
Sets the bGameCameraCutThisFrame flag to true (indicating we did a camera cut this frame; useful for game code to call, e.g., when performing a teleport that should be seamless)

<a id="unreal.PlayerCameraManager.remove_generic_camera_lens_effect"></a>

#### remove_generic_camera_lens_effect

```python
def remove_generic_camera_lens_effect(
        emitter: CameraLensEffectInterface) -> None
```

x.remove_generic_camera_lens_effect(emitter) -> None
Removes the given lens effect from the camera.

Args:
    emitter (CameraLensEffectInterface): the emitter actor to remove from the camera

<a id="unreal.PlayerCameraManager.remove_camera_modifier"></a>

#### remove_camera_modifier

```python
def remove_camera_modifier(modifier_to_remove: CameraModifier) -> bool
```

x.remove_camera_modifier(modifier_to_remove) -> bool
Removes the given camera modifier from this camera (if it's on the camera in the first place) and discards it.

Args:
    modifier_to_remove (CameraModifier): 

Returns:
    bool: True if successfully removed, false otherwise.

<a id="unreal.PlayerCameraManager.photography_camera_modify"></a>

#### photography_camera_modify

```python
def photography_camera_modify(new_camera_location: Vector,
                              previous_camera_location: Vector,
                              original_camera_location: Vector) -> Vector
```

x.photography_camera_modify(new_camera_location, previous_camera_location, original_camera_location) -> Vector
Implementable blueprint hook to allow a PlayerCameraManager subclass to
constrain or otherwise modify the camera during free-camera photography.
For example, a blueprint may wish to limit the distance from the camera's
original point, or forbid the camera from passing through walls.
NewCameraLocation contains the proposed new camera location.
PreviousCameraLocation contains the camera location in the previous frame.
OriginalCameraLocation contains the camera location before the game was put
into photography mode.
Return ResultCameraLocation as modified according to your constraints.

Args:
    new_camera_location (Vector): 
    previous_camera_location (Vector): 
    original_camera_location (Vector): 

Returns:
    Vector: 

    result_camera_location (Vector):

<a id="unreal.PlayerCameraManager.on_photography_session_start"></a>

#### on_photography_session_start

```python
def on_photography_session_start() -> None
```

x.on_photography_session_start() -> None
Event triggered upon entering Photography mode (before pausing, if
r.Photography.AutoPause is 1).

<a id="unreal.PlayerCameraManager.on_photography_session_end"></a>

#### on_photography_session_end

```python
def on_photography_session_end() -> None
```

x.on_photography_session_end() -> None
Event triggered upon leaving Photography mode (after unpausing, if
r.Photography.AutoPause is 1).

<a id="unreal.PlayerCameraManager.on_photography_multi_part_capture_start"></a>

#### on_photography_multi_part_capture_start

```python
def on_photography_multi_part_capture_start() -> None
```

x.on_photography_multi_part_capture_start() -> None
Event triggered upon the start of a multi-part photograph capture (i.e. a
stereoscopic or 360-degree shot).  This is an ideal time to turn off
rendering effects that tile badly (UI, subtitles, vignette, very aggressive
bloom, etc; most of these are automatically disabled when
r.Photography.AutoPostprocess is 1).

<a id="unreal.PlayerCameraManager.on_photography_multi_part_capture_end"></a>

#### on_photography_multi_part_capture_end

```python
def on_photography_multi_part_capture_end() -> None
```

x.on_photography_multi_part_capture_end() -> None
Event triggered upon the end of a multi-part photograph capture, when manual
free-roaming photographic camera control is about to be returned to the user.
Here you may re-enable whatever was turned off within
OnPhotographyMultiPartCaptureStart.

<a id="unreal.PlayerCameraManager.get_owning_player_controller"></a>

#### get_owning_player_controller

```python
def get_owning_player_controller() -> PlayerController
```

x.get_owning_player_controller() -> PlayerController
Returns the PlayerController that owns this camera.

Returns:
    PlayerController:

<a id="unreal.PlayerCameraManager.get_fov_angle"></a>

#### get_fov_angle

```python
def get_fov_angle() -> float
```

x.get_fov_angle() -> float
Returns the camera's current full FOV angle, in degrees.

Returns:
    float:

<a id="unreal.PlayerCameraManager.get_camera_rotation"></a>

#### get_camera_rotation

```python
def get_camera_rotation() -> Rotator
```

x.get_camera_rotation() -> Rotator
Returns camera's current rotation.

Returns:
    Rotator:

<a id="unreal.PlayerCameraManager.get_camera_location"></a>

#### get_camera_location

```python
def get_camera_location() -> Vector
```

x.get_camera_location() -> Vector
Returns camera's current location.

Returns:
    Vector:

<a id="unreal.PlayerCameraManager.find_camera_modifier_by_class"></a>

#### find_camera_modifier_by_class

```python
def find_camera_modifier_by_class(modifier_class: Class) -> CameraModifier
```

x.find_camera_modifier_by_class(modifier_class) -> CameraModifier
Returns camera modifier for this camera of the given class, if it exists.
Exact class match only. If there are multiple modifiers of the same class, the first one is returned.

Args:
    modifier_class (type(Class)): 

Returns:
    CameraModifier:

<a id="unreal.PlayerCameraManager.clear_camera_lens_effects"></a>

#### clear_camera_lens_effects

```python
def clear_camera_lens_effects() -> None
```

x.clear_camera_lens_effects() -> None
Removes all camera lens effects.

<a id="unreal.PlayerCameraManager.blueprint_update_camera"></a>

#### blueprint_update_camera

```python
def blueprint_update_camera(
        camera_target: Actor) -> Optional[Tuple[Vector, Rotator, float]]
```

x.blueprint_update_camera(camera_target) -> (new_camera_location=Vector, new_camera_rotation=Rotator, new_camera_fov=float) or None
Blueprint hook to allow blueprints to override existing camera behavior or implement custom cameras.
If this function returns true, we will use the given returned values and skip further calculations to determine
final camera POV.

Args:
    camera_target (Actor): 

Returns:
    tuple or None: 

    new_camera_location (Vector): 

    new_camera_rotation (Rotator): 

    new_camera_fov (float):

<a id="unreal.PlayerCameraManager.kismet_update_camera"></a>

#### kismet_update_camera

```python
def kismet_update_camera(
        camera_target: Actor) -> Optional[Tuple[Vector, Rotator, float]]
```

deprecated: 'kismet_update_camera' was renamed to 'blueprint_update_camera'.

<a id="unreal.PlayerCameraManager.add_new_camera_modifier"></a>

#### add_new_camera_modifier

```python
def add_new_camera_modifier(modifier_class: Class) -> CameraModifier
```

x.add_new_camera_modifier(modifier_class) -> CameraModifier
Creates and initializes a new camera modifier of the specified class.

Args:
    modifier_class (type(Class)): The class of camera modifier to create.

Returns:
    CameraModifier: Returns the newly created camera modifier.

<a id="unreal.PlayerCameraManager.add_generic_camera_lens_effect"></a>

#### add_generic_camera_lens_effect

```python
def add_generic_camera_lens_effect(
        lens_effect_emitter_class: Class) -> CameraLensEffectInterface
```

x.add_generic_camera_lens_effect(lens_effect_emitter_class) -> CameraLensEffectInterface
Creates a camera lens effect of the given class on this camera.

Args:
    lens_effect_emitter_class (type(Class)): Class of lens effect emitter to create.

Returns:
    CameraLensEffectInterface: Returns the new emitter actor.

<a id="unreal.PluginBlueprintLibrary"></a>