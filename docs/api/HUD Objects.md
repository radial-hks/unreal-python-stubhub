## HUD Objects

```python
class HUD(Actor)
```

Base class of the heads-up display. This has a canvas and a debug canvas on which primitives can be drawn.
It also contains a list of simple hit boxes that can be used for simple item click detection.
A method of rendering debug text is also included.
Provides some simple methods for rendering text, textures, rectangles and materials which can also be accessed from blueprints.
see: UCanvas
see: FHUDHitBox
see: FDebugTextInfo

**C++ Source:**

- **Module**: Engine
- **File**: HUD.h

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
- ``enable_debug_text_shadow`` (bool):  [Read-Write] Put shadow on debug strings
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
- ``lost_focus_paused`` (bool):  [Read-Write] Tells whether the game was paused due to lost focus
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
- ``player_owner`` (PlayerController):  [Read-Write] PlayerController which owns this HUD.
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
- ``show_debug_info`` (bool):  [Read-Write] If true, current ViewTarget shows debug information using its DisplayDebug().
- ``show_hit_box_debug_info`` (bool):  [Read-Write] If true, show hitbox debugging info.
- ``show_hud`` (bool):  [Read-Write] Whether or not the HUD should be drawn.
- ``show_overlays`` (bool):  [Read-Write] If true, render actor overlays.
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

<a id="unreal.HUD.player_owner"></a>

#### player_owner

```python
@property
def player_owner() -> PlayerController
```

(PlayerController):  [Read-Only] PlayerController which owns this HUD.

<a id="unreal.HUD.lost_focus_paused"></a>

#### lost_focus_paused

```python
@property
def lost_focus_paused() -> bool
```

(bool):  [Read-Only] Tells whether the game was paused due to lost focus

<a id="unreal.HUD.show_hud"></a>

#### show_hud

```python
@property
def show_hud() -> bool
```

(bool):  [Read-Write] Whether or not the HUD should be drawn.

<a id="unreal.HUD.show_hud"></a>

#### show_hud

```python
@show_hud.setter
def show_hud(value: bool) -> None
```

<a id="unreal.HUD.show_debug_info"></a>

#### show_debug_info

```python
@property
def show_debug_info() -> bool
```

(bool):  [Read-Write] If true, current ViewTarget shows debug information using its DisplayDebug().

<a id="unreal.HUD.show_debug_info"></a>

#### show_debug_info

```python
@show_debug_info.setter
def show_debug_info(value: bool) -> None
```

<a id="unreal.HUD.show_hit_box_debug_info"></a>

#### show_hit_box_debug_info

```python
@property
def show_hit_box_debug_info() -> bool
```

(bool):  [Read-Write] If true, show hitbox debugging info.

<a id="unreal.HUD.show_hit_box_debug_info"></a>

#### show_hit_box_debug_info

```python
@show_hit_box_debug_info.setter
def show_hit_box_debug_info(value: bool) -> None
```

<a id="unreal.HUD.show_overlays"></a>

#### show_overlays

```python
@property
def show_overlays() -> bool
```

(bool):  [Read-Write] If true, render actor overlays.

<a id="unreal.HUD.show_overlays"></a>

#### show_overlays

```python
@show_overlays.setter
def show_overlays(value: bool) -> None
```

<a id="unreal.HUD.enable_debug_text_shadow"></a>

#### enable_debug_text_shadow

```python
@property
def enable_debug_text_shadow() -> bool
```

(bool):  [Read-Write] Put shadow on debug strings

<a id="unreal.HUD.enable_debug_text_shadow"></a>

#### enable_debug_text_shadow

```python
@enable_debug_text_shadow.setter
def enable_debug_text_shadow(value: bool) -> None
```

<a id="unreal.HUD.receive_hit_box_release"></a>

#### receive_hit_box_release

```python
def receive_hit_box_release(box_name: Name) -> None
```

x.receive_hit_box_release(box_name) -> None
Called when a hit box is unclicked. Provides the name associated with that box.

Args:
    box_name (Name):

<a id="unreal.HUD.receive_hit_box_end_cursor_over"></a>

#### receive_hit_box_end_cursor_over

```python
def receive_hit_box_end_cursor_over(box_name: Name) -> None
```

x.receive_hit_box_end_cursor_over(box_name) -> None
Called when a hit box no longer has the mouse over it.

Args:
    box_name (Name):

<a id="unreal.HUD.receive_hit_box_click"></a>

#### receive_hit_box_click

```python
def receive_hit_box_click(box_name: Name) -> None
```

x.receive_hit_box_click(box_name) -> None
Called when a hit box is clicked on. Provides the name associated with that box.

Args:
    box_name (Name):

<a id="unreal.HUD.receive_hit_box_begin_cursor_over"></a>

#### receive_hit_box_begin_cursor_over

```python
def receive_hit_box_begin_cursor_over(box_name: Name) -> None
```

x.receive_hit_box_begin_cursor_over(box_name) -> None
Called when a hit box is moused over.

Args:
    box_name (Name):

<a id="unreal.HUD.receive_draw_hud"></a>

#### receive_draw_hud

```python
def receive_draw_hud(size_x: int, size_y: int) -> None
```

x.receive_draw_hud(size_x, size_y) -> None
Hook to allow blueprints to do custom HUD drawing.
see: bSuppressNativeHUD to control HUD drawing in base class. Note:  the canvas resource used for drawing is only valid during this event, it will not be valid if drawing functions are called later (e.g. after a Delay node).

Args:
    size_x (int32): 
    size_y (int32):

<a id="unreal.HUD.project"></a>

#### project

```python
def project(location: Vector, clamp_to_zero_plane: bool = True) -> Vector
```

x.project(location, clamp_to_zero_plane=True) -> Vector
Transforms a 3D world-space vector into 2D screen coordinates

Args:
    location (Vector): The world-space position to transform
    clamp_to_zero_plane (bool): If true, 2D screen coordinates behind the viewing plane (-Z) will have Z set to 0 (leaving X and Y alone)

Returns:
    Vector: The transformed vector

<a id="unreal.HUD.get_text_size"></a>

#### get_text_size

```python
def get_text_size(text: str,
                  font: Font = None,
                  scale: float = 1.000000) -> Tuple[float, float]
```

x.get_text_size(text, font=None, scale=1.000000) -> (out_width=float, out_height=float)
Returns the width and height of a string.

Args:
    text (str): String to draw
    font (Font): Font to draw text.  If NULL, default font is chosen.
    scale (float): Scale multiplier to control size of the text.

Returns:
    tuple: 

    out_width (float): Returns the width in pixels of the string.

    out_height (float): Returns the height in pixels of the string.

<a id="unreal.HUD.get_owning_player_controller"></a>

#### get_owning_player_controller

```python
def get_owning_player_controller() -> PlayerController
```

x.get_owning_player_controller() -> PlayerController
Returns the PlayerController for this HUD's player.

Returns:
    PlayerController:

<a id="unreal.HUD.get_owning_pawn"></a>

#### get_owning_pawn

```python
def get_owning_pawn() -> Pawn
```

x.get_owning_pawn() -> Pawn
Returns the Pawn for this HUD's player.

Returns:
    Pawn:

<a id="unreal.HUD.get_actors_in_selection_rectangle"></a>

#### get_actors_in_selection_rectangle

```python
def get_actors_in_selection_rectangle(
        class_filter: Class,
        first_point: Vector2D,
        second_point: Vector2D,
        include_non_colliding_components: bool = True,
        actor_must_be_fully_enclosed: bool = False) -> Array[Actor]
```

x.get_actors_in_selection_rectangle(class_filter, first_point, second_point, include_non_colliding_components=True, actor_must_be_fully_enclosed=False) -> Array[Actor]
Returns the array of actors inside a selection rectangle, with a class filter.

Sample usage:

      TArray<AStaticMeshActor*> ActorsInSelectionRect;
             Canvas->GetActorsInSelectionRectangle<AStaticMeshActor>(FirstPoint,SecondPoint,ActorsInSelectionRect);

Args:
    class_filter (type(Class)): 
    first_point (Vector2D): The first point, or anchor of the marquee box. Where the dragging of the marquee started in screen space.
    second_point (Vector2D): The second point, where the mouse cursor currently is / the other point of the box selection, in screen space.
    include_non_colliding_components (bool): Whether to include even non-colliding components of the actor when determining its bounds
    actor_must_be_fully_enclosed (bool): The Selection rule: whether the selection box can partially intersect Actor, or must fully enclose the Actor.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]):

<a id="unreal.HUD.draw_texture_simple"></a>

#### draw_texture_simple

```python
def draw_texture_simple(texture: Texture,
                        screen_x: float,
                        screen_y: float,
                        scale: float = 1.000000,
                        scale_position: bool = False) -> None
```

x.draw_texture_simple(texture, screen_x, screen_y, scale=1.000000, scale_position=False) -> None
Draws a textured quad on the HUD. Assumes 1:1 texel density.

Args:
    texture (Texture): Texture to draw.
    screen_x (float): Screen-space X coordinate of upper left corner of the quad.
    screen_y (float): Screen-space Y coordinate of upper left corner of the quad.
    scale (float): Scale multiplier to control size of the text.
    scale_position (bool): Whether the "Scale" parameter should also scale the position of this draw call.

<a id="unreal.HUD.draw_texture"></a>

#### draw_texture

```python
def draw_texture(texture: Texture,
                 screen_x: float,
                 screen_y: float,
                 screen_w: float,
                 screen_h: float,
                 texture_u: float,
                 texture_v: float,
                 texture_u_width: float,
                 texture_v_height: float,
                 tint_color: LinearColor = [
                     1.000000, 1.000000, 1.000000, 1.000000
                 ],
                 blend_mode: BlendMode = BlendMode.BLEND_TRANSLUCENT,
                 scale: float = 1.000000,
                 scale_position: bool = False,
                 rotation: float = 0.000000,
                 rot_pivot: Vector2D = [0.000000, 0.000000]) -> None
```

x.draw_texture(texture, screen_x, screen_y, screen_w, screen_h, texture_u, texture_v, texture_u_width, texture_v_height, tint_color=[1.000000, 1.000000, 1.000000, 1.000000], blend_mode=BlendMode.BLEND_TRANSLUCENT, scale=1.000000, scale_position=False, rotation=0.000000, rot_pivot=[0.000000, 0.000000]) -> None
Draws a textured quad on the HUD.

Args:
    texture (Texture): Texture to draw.
    screen_x (float): Screen-space X coordinate of upper left corner of the quad.
    screen_y (float): Screen-space Y coordinate of upper left corner of the quad.
    screen_w (float): Screen-space width of the quad (in pixels).
    screen_h (float): Screen-space height of the quad (in pixels).
    texture_u (float): Texture-space U coordinate of upper left corner of the quad
    texture_v (float): Texture-space V coordinate of upper left corner of the quad.
    texture_u_width (float): Texture-space width of the quad (in normalized UV distance).
    texture_v_height (float): Texture-space height of the quad (in normalized UV distance).
    tint_color (LinearColor): Vertex color for the quad.
    blend_mode (BlendMode): Controls how to blend this quad with the scene. Translucent by default.
    scale (float): Amount to scale the entire texture (horizontally and vertically)
    scale_position (bool): Whether the "Scale" parameter should also scale the position of this draw call.
    rotation (float): Amount to rotate this quad
    rot_pivot (Vector2D): Location (as proportion of quad, 0-1) to rotate about

<a id="unreal.HUD.draw_text"></a>

#### draw_text

```python
def draw_text(text: str,
              text_color: LinearColor = [
                  0.000000, 0.000000, 0.000000, 1.000000
              ],
              screen_x: float = ...,
              screen_y: float = ...,
              font: Font = None,
              scale: float = 1.000000,
              scale_position: bool = False) -> None
```

x.draw_text(text, text_color=[0.000000, 0.000000, 0.000000, 1.000000], screen_x, screen_y, font=None, scale=1.000000, scale_position=False) -> None
Draws a string on the HUD.

Args:
    text (str): String to draw
    text_color (LinearColor): Color to draw string
    screen_x (float): Screen-space X coordinate of upper left corner of the string.
    screen_y (float): Screen-space Y coordinate of upper left corner of the string.
    font (Font): Font to draw text.  If NULL, default font is chosen.
    scale (float): Scale multiplier to control size of the text.
    scale_position (bool): Whether the "Scale" parameter should also scale the position of this draw call.

<a id="unreal.HUD.draw_rect"></a>

#### draw_rect

```python
def draw_rect(rect_color: LinearColor = [
    0.000000, 0.000000, 0.000000, 1.000000
],
              screen_x: float = ...,
              screen_y: float = ...,
              screen_w: float = ...,
              screen_h: float = ...) -> None
```

x.draw_rect(rect_color=[0.000000, 0.000000, 0.000000, 1.000000], screen_x, screen_y, screen_w, screen_h) -> None
Draws a colored untextured quad on the HUD.

Args:
    rect_color (LinearColor): Color of the rect. Can be translucent.
    screen_x (float): Screen-space X coordinate of upper left corner of the quad.
    screen_y (float): Screen-space Y coordinate of upper left corner of the quad.
    screen_w (float): Screen-space width of the quad (in pixels).
    screen_h (float): Screen-space height of the quad (in pixels).

<a id="unreal.HUD.draw_material_triangle"></a>

#### draw_material_triangle

```python
def draw_material_triangle(
        material: MaterialInterface,
        v0_pos: Vector2D,
        v1_pos: Vector2D,
        v2_pos: Vector2D,
        v0_uv: Vector2D,
        v1_uv: Vector2D,
        v2_uv: Vector2D,
        v0_color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        v1_color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        v2_color: LinearColor = [1.000000, 1.000000, 1.000000,
                                 1.000000]) -> None
```

x.draw_material_triangle(material, v0_pos, v1_pos, v2_pos, v0_uv, v1_uv, v2_uv, v0_color=[1.000000, 1.000000, 1.000000, 1.000000], v1_color=[1.000000, 1.000000, 1.000000, 1.000000], v2_color=[1.000000, 1.000000, 1.000000, 1.000000]) -> None
Draw Material Triangle

Args:
    material (MaterialInterface): 
    v0_pos (Vector2D): 
    v1_pos (Vector2D): 
    v2_pos (Vector2D): 
    v0_uv (Vector2D): 
    v1_uv (Vector2D): 
    v2_uv (Vector2D): 
    v0_color (LinearColor): 
    v1_color (LinearColor): 
    v2_color (LinearColor):

<a id="unreal.HUD.draw_material_simple"></a>

#### draw_material_simple

```python
def draw_material_simple(material: MaterialInterface,
                         screen_x: float,
                         screen_y: float,
                         screen_w: float,
                         screen_h: float,
                         scale: float = 1.000000,
                         scale_position: bool = False) -> None
```

x.draw_material_simple(material, screen_x, screen_y, screen_w, screen_h, scale=1.000000, scale_position=False) -> None
Draws a material-textured quad on the HUD.  Assumes UVs such that the entire material is shown.

Args:
    material (MaterialInterface): Material to use
    screen_x (float): Screen-space X coordinate of upper left corner of the quad.
    screen_y (float): Screen-space Y coordinate of upper left corner of the quad.
    screen_w (float): Screen-space width of the quad (in pixels).
    screen_h (float): Screen-space height of the quad (in pixels).
    scale (float): Amount to scale the entire texture (horizontally and vertically)
    scale_position (bool): Whether the "Scale" parameter should also scale the position of this draw call.

<a id="unreal.HUD.draw_material"></a>

#### draw_material

```python
def draw_material(material: MaterialInterface,
                  screen_x: float,
                  screen_y: float,
                  screen_w: float,
                  screen_h: float,
                  material_u: float,
                  material_v: float,
                  material_u_width: float,
                  material_v_height: float,
                  scale: float = 1.000000,
                  scale_position: bool = False,
                  rotation: float = 0.000000,
                  rot_pivot: Vector2D = [0.000000, 0.000000]) -> None
```

x.draw_material(material, screen_x, screen_y, screen_w, screen_h, material_u, material_v, material_u_width, material_v_height, scale=1.000000, scale_position=False, rotation=0.000000, rot_pivot=[0.000000, 0.000000]) -> None
Draws a material-textured quad on the HUD.

Args:
    material (MaterialInterface): Material to use
    screen_x (float): Screen-space X coordinate of upper left corner of the quad.
    screen_y (float): Screen-space Y coordinate of upper left corner of the quad.
    screen_w (float): Screen-space width of the quad (in pixels).
    screen_h (float): Screen-space height of the quad (in pixels).
    material_u (float): Texture-space U coordinate of upper left corner of the quad
    material_v (float): Texture-space V coordinate of upper left corner of the quad.
    material_u_width (float): Texture-space width of the quad (in normalized UV distance).
    material_v_height (float): Texture-space height of the quad (in normalized UV distance).
    scale (float): Amount to scale the entire texture (horizontally and vertically)
    scale_position (bool): Whether the "Scale" parameter should also scale the position of this draw call.
    rotation (float): Amount to rotate this quad
    rot_pivot (Vector2D): Location (as proportion of quad, 0-1) to rotate about

<a id="unreal.HUD.draw_line"></a>

#### draw_line

```python
def draw_line(start_screen_x: float,
              start_screen_y: float,
              end_screen_x: float,
              end_screen_y: float,
              line_color: LinearColor = [
                  0.000000, 0.000000, 0.000000, 1.000000
              ],
              line_thickness: float = 0.000000) -> None
```

x.draw_line(start_screen_x, start_screen_y, end_screen_x, end_screen_y, line_color=[0.000000, 0.000000, 0.000000, 1.000000], line_thickness=0.000000) -> None
Draws a 2D line on the HUD.

Args:
    start_screen_x (float): Screen-space X coordinate of start of the line.
    start_screen_y (float): Screen-space Y coordinate of start of the line.
    end_screen_x (float): Screen-space X coordinate of end of the line.
    end_screen_y (float): Screen-space Y coordinate of end of the line.
    line_color (LinearColor): Color to draw line
    line_thickness (float): Thickness of the line to draw

<a id="unreal.HUD.deproject"></a>

#### deproject

```python
def deproject(screen_x: float, screen_y: float) -> Tuple[Vector, Vector]
```

x.deproject(screen_x, screen_y) -> (world_position=Vector, world_direction=Vector)
Transforms a 2D screen location into a 3D location and direction

Args:
    screen_x (float): 
    screen_y (float): 

Returns:
    tuple: 

    world_position (Vector): 

    world_direction (Vector):

<a id="unreal.HUD.add_hit_box"></a>

#### add_hit_box

```python
def add_hit_box(position: Vector2D,
                size: Vector2D,
                name: Name,
                consumes_input: bool,
                priority: int = 0) -> None
```

x.add_hit_box(position, size, name, consumes_input, priority=0) -> None
Add a hitbox to the hud

Args:
    position (Vector2D): Coordinates of the top left of the hit box.
    size (Vector2D): Size of the hit box.
    name (Name): 
    consumes_input (bool): Whether click processing should continue if this hit box is clicked.
    priority (int32): The priority of the box used for layering. Larger values are considered first.  Equal values are considered in the order they were added.

<a id="unreal.DebugCameraHUD"></a>