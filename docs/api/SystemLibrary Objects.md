## SystemLibrary Objects

```python
class SystemLibrary(BlueprintFunctionLibrary)
```

Kismet System Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetSystemLibrary.h

<a id="unreal.SystemLibrary.unregister_for_remote_notifications"></a>

#### unregister_for_remote_notifications

```python
@classmethod
def unregister_for_remote_notifications(cls) -> None
```

X.unregister_for_remote_notifications() -> None
Requests Requests unregistering from receiving remote notifications to the user's device.
(Android only)

<a id="unreal.SystemLibrary.unload_primary_asset_list"></a>

#### unload_primary_asset_list

```python
@classmethod
def unload_primary_asset_list(
        cls, primary_asset_id_list: Array[PrimaryAssetId]) -> None
```

X.unload_primary_asset_list(primary_asset_id_list) -> None
Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

Args:
    primary_asset_id_list (Array[PrimaryAssetId]):

<a id="unreal.SystemLibrary.unload_primary_asset"></a>

#### unload_primary_asset

```python
@classmethod
def unload_primary_asset(cls, primary_asset_id: PrimaryAssetId) -> None
```

X.unload_primary_asset(primary_asset_id) -> None
Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

Args:
    primary_asset_id (PrimaryAssetId):

<a id="unreal.SystemLibrary.transact_object"></a>

#### transact_object

```python
@classmethod
def transact_object(cls, object: Object) -> None
```

X.transact_object(object) -> None
Notify the current transaction (if any) that this object is about to be modified and should be placed into the undo buffer.
note: Internally this calls Modify on the given object, so will also mark the owner package dirty.
note: Only available in the editor.

Args:
    object (Object): The object that is about to be modified.

<a id="unreal.SystemLibrary.sphere_trace_single_for_objects"></a>

#### sphere_trace_single_for_objects

```python
@classmethod
def sphere_trace_single_for_objects(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.sphere_trace_single_for_objects(world_context_object, start, end, radius, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweeps a sphere along the given line and returns the first hit encountered.
This only finds objects that are of a type specified by ObjectTypes.

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the sphere to sweep
    object_types (Array[ObjectTypeQuery]): Array of Object Types to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.sphere_trace_single_by_profile"></a>

#### sphere_trace_single_by_profile

```python
@classmethod
def sphere_trace_single_by_profile(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.sphere_trace_single_by_profile(world_context_object, start, end, radius, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweep a sphere against the world and return the first blocking hit using a specific profile

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the sphere to sweep
    profile_name (Name): The 'profile' used to determine which components to hit
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.sphere_trace_single"></a>

#### sphere_trace_single

```python
@classmethod
def sphere_trace_single(cls,
                        world_context_object: Object,
                        start: Vector,
                        end: Vector,
                        radius: float,
                        trace_channel: TraceTypeQuery,
                        trace_complex: bool,
                        actors_to_ignore: Array[Actor],
                        draw_debug_type: DrawDebugTrace,
                        ignore_self: bool = True,
                        trace_color: LinearColor = [
                            1.000000, 0.000000, 0.000000, 1.000000
                        ],
                        trace_hit_color: LinearColor = [
                            0.000000, 1.000000, 0.000000, 1.000000
                        ],
                        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.sphere_trace_single(world_context_object, start, end, radius, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweeps a sphere along the given line and returns the first blocking hit encountered.
This trace finds the objects that RESPONDS to the given TraceChannel

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the sphere to sweep
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.sphere_trace_single_new"></a>

#### sphere_trace_single_new

```python
@classmethod
def sphere_trace_single_new(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        trace_channel: TraceTypeQuery,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

deprecated: 'sphere_trace_single_new' was renamed to 'sphere_trace_single'.

<a id="unreal.SystemLibrary.sphere_trace_multi_for_objects"></a>

#### sphere_trace_multi_for_objects

```python
@classmethod
def sphere_trace_multi_for_objects(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.sphere_trace_multi_for_objects(world_context_object, start, end, radius, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweeps a sphere along the given line and returns all hits encountered.
This only finds objects that are of a type specified by ObjectTypes.

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the sphere to sweep
    object_types (Array[ObjectTypeQuery]): Array of Object Types to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.sphere_trace_multi_by_profile"></a>

#### sphere_trace_multi_by_profile

```python
@classmethod
def sphere_trace_multi_by_profile(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.sphere_trace_multi_by_profile(world_context_object, start, end, radius, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweep a sphere against the world and return all initial overlaps using a specific profile, then overlapping hits and then first blocking hit
Results are sorted, so a blocking hit (if found) will be the last element of the array
Only the single closest blocking result will be generated, no tests will be done after that

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the sphere to sweep
    profile_name (Name): The 'profile' used to determine which components to hit
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a blocking hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.sphere_trace_multi"></a>

#### sphere_trace_multi

```python
@classmethod
def sphere_trace_multi(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        trace_channel: TraceTypeQuery,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.sphere_trace_multi(world_context_object, start, end, radius, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweeps a sphere along the given line and returns all hits encountered up to and including the first blocking hit.
This trace finds the objects that RESPOND to the given TraceChannel

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the sphere to sweep
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a blocking hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.sphere_trace_multi_new"></a>

#### sphere_trace_multi_new

```python
@classmethod
def sphere_trace_multi_new(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        trace_channel: TraceTypeQuery,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

deprecated: 'sphere_trace_multi_new' was renamed to 'sphere_trace_multi'.

<a id="unreal.SystemLibrary.sphere_overlap_components"></a>

#### sphere_overlap_components

```python
@classmethod
def sphere_overlap_components(
        cls, world_context_object: Object, sphere_pos: Vector,
        sphere_radius: float, object_types: Array[ObjectTypeQuery],
        component_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[PrimitiveComponent]]
```

X.sphere_overlap_components(world_context_object, sphere_pos, sphere_radius, object_types, component_class_filter, actors_to_ignore) -> Array[PrimitiveComponent] or None
Returns an array of components that overlap the given sphere.

Args:
    world_context_object (Object): 
    sphere_pos (Vector): Center of sphere.
    sphere_radius (float): Size of sphere.
    object_types (Array[ObjectTypeQuery]): 
    component_class_filter (type(Class)): 
    actors_to_ignore (Array[Actor]): Ignore these actors in the list

Returns:
    Array[PrimitiveComponent] or None: true if there was an overlap that passed the filters, false otherwise.

    out_components (Array[PrimitiveComponent]):

<a id="unreal.SystemLibrary.sphere_overlap_components_new"></a>

#### sphere_overlap_components_new

```python
@classmethod
def sphere_overlap_components_new(
        cls, world_context_object: Object, sphere_pos: Vector,
        sphere_radius: float, object_types: Array[ObjectTypeQuery],
        component_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[PrimitiveComponent]]
```

deprecated: 'sphere_overlap_components_new' was renamed to 'sphere_overlap_components'.

<a id="unreal.SystemLibrary.sphere_overlap_actors"></a>

#### sphere_overlap_actors

```python
@classmethod
def sphere_overlap_actors(
        cls, world_context_object: Object, sphere_pos: Vector,
        sphere_radius: float, object_types: Array[ObjectTypeQuery],
        actor_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[Actor]]
```

X.sphere_overlap_actors(world_context_object, sphere_pos, sphere_radius, object_types, actor_class_filter, actors_to_ignore) -> Array[Actor] or None
Returns an array of actors that overlap the given sphere.

Args:
    world_context_object (Object): 
    sphere_pos (Vector): Center of sphere.
    sphere_radius (float): Size of sphere.
    object_types (Array[ObjectTypeQuery]): 
    actor_class_filter (type(Class)): 
    actors_to_ignore (Array[Actor]): Ignore these actors in the list

Returns:
    Array[Actor] or None: true if there was an overlap that passed the filters, false otherwise.

    out_actors (Array[Actor]): Returned array of actors. Unsorted.

<a id="unreal.SystemLibrary.sphere_overlap_actors_new"></a>

#### sphere_overlap_actors_new

```python
@classmethod
def sphere_overlap_actors_new(
        cls, world_context_object: Object, sphere_pos: Vector,
        sphere_radius: float, object_types: Array[ObjectTypeQuery],
        actor_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[Actor]]
```

deprecated: 'sphere_overlap_actors_new' was renamed to 'sphere_overlap_actors'.

<a id="unreal.SystemLibrary.snapshot_object"></a>

#### snapshot_object

```python
@classmethod
def snapshot_object(cls, object: Object) -> None
```

X.snapshot_object(object) -> None
Notify the current transaction (if any) that this object is about to be modified and should be snapshot for intermediate update.
note: Internally this calls SnapshotTransactionBuffer on the given object.
note: Only available in the editor.

Args:
    object (Object): The object that is about to be modified.

<a id="unreal.SystemLibrary.show_platform_specific_leaderboard_screen"></a>

#### show_platform_specific_leaderboard_screen

```python
@classmethod
def show_platform_specific_leaderboard_screen(cls, category_name: str) -> None
```

X.show_platform_specific_leaderboard_screen(category_name) -> None
Displays the built-in leaderboard GUI (iOS and Android only; this function may be renamed or moved in a future release)

Args:
    category_name (str):

<a id="unreal.SystemLibrary.experimental_show_game_center_leaderboard"></a>

#### experimental_show_game_center_leaderboard

```python
@classmethod
def experimental_show_game_center_leaderboard(cls, category_name: str) -> None
```

deprecated: 'experimental_show_game_center_leaderboard' was renamed to 'show_platform_specific_leaderboard_screen'.

<a id="unreal.SystemLibrary.show_platform_specific_achievements_screen"></a>

#### show_platform_specific_achievements_screen

```python
@classmethod
def show_platform_specific_achievements_screen(
        cls, specific_player: PlayerController) -> None
```

X.show_platform_specific_achievements_screen(specific_player) -> None
Displays the built-in achievements GUI (iOS and Android only; this function may be renamed or moved in a future release)

Args:
    specific_player (PlayerController): Specific player's achievements to show. May not be supported on all platforms. If null, defaults to the player with ControllerId 0

<a id="unreal.SystemLibrary.show_interstitial_ad"></a>

#### show_interstitial_ad

```python
@classmethod
def show_interstitial_ad(cls) -> None
```

X.show_interstitial_ad() -> None
Shows the loaded interstitial ad (loaded with LoadInterstitialAd)
(Android only)

<a id="unreal.SystemLibrary.show_ad_banner"></a>

#### show_ad_banner

```python
@classmethod
def show_ad_banner(cls, ad_id_index: int,
                   show_on_bottom_of_screen: bool) -> None
```

X.show_ad_banner(ad_id_index, show_on_bottom_of_screen) -> None
Will show an ad banner (iAd on iOS, or AdMob on Android) on the top or bottom of screen, on top of the GL view (doesn't resize the view)
(iOS and Android only)

Args:
    ad_id_index (int32): The index of the ID to select for the ad to show
    show_on_bottom_of_screen (bool): If true, the iAd will be shown at the bottom of the screen, top otherwise

<a id="unreal.SystemLibrary.experimental_show_ad_banner"></a>

#### experimental_show_ad_banner

```python
@classmethod
def experimental_show_ad_banner(cls, ad_id_index: int,
                                show_on_bottom_of_screen: bool) -> None
```

deprecated: 'experimental_show_ad_banner' was renamed to 'show_ad_banner'.

<a id="unreal.SystemLibrary.set_window_title"></a>

#### set_window_title

```python
@classmethod
def set_window_title(cls, title: Text) -> None
```

X.set_window_title(title) -> None
Sets the game window title

Args:
    title (Text):

<a id="unreal.SystemLibrary.set_volume_buttons_handled_by_system"></a>

#### set_volume_buttons_handled_by_system

```python
@classmethod
def set_volume_buttons_handled_by_system(cls, enabled: bool) -> None
```

X.set_volume_buttons_handled_by_system(enabled) -> None
Allows or inhibits system default handling of volume up and volume down buttons (Android only)

Args:
    enabled (bool): If true, allow Android to handle volume up and down events

<a id="unreal.SystemLibrary.set_user_activity"></a>

#### set_user_activity

```python
@classmethod
def set_user_activity(cls, user_activity: UserActivity) -> None
```

X.set_user_activity(user_activity) -> None
Tells the engine what the user is doing for debug, analytics, etc.

Args:
    user_activity (UserActivity):

<a id="unreal.SystemLibrary.set_suppress_viewport_transition_message"></a>

#### set_suppress_viewport_transition_message

```python
@classmethod
def set_suppress_viewport_transition_message(cls, world_context_object: Object,
                                             state: bool) -> None
```

X.set_suppress_viewport_transition_message(world_context_object, state) -> None
Sets the state of the transition message rendered by the viewport. (The blue text displayed when the game is paused and so forth.)

Args:
    world_context_object (Object): World context
    state (bool):

<a id="unreal.SystemLibrary.set_supress_viewport_transition_message"></a>

#### set_supress_viewport_transition_message

```python
@classmethod
def set_supress_viewport_transition_message(cls, world_context_object: Object,
                                            state: bool) -> None
```

deprecated: 'set_supress_viewport_transition_message' was renamed to 'set_suppress_viewport_transition_message'.

<a id="unreal.SystemLibrary.set_gamepads_block_device_feedback"></a>

#### set_gamepads_block_device_feedback

```python
@classmethod
def set_gamepads_block_device_feedback(cls, block: bool) -> None
```

X.set_gamepads_block_device_feedback(block) -> None
Sets whether attached gamepads will block feedback from the device itself (Mobile only).

Args:
    block (bool):

<a id="unreal.SystemLibrary.retriggerable_delay"></a>

#### retriggerable_delay

```python
@classmethod
def retriggerable_delay(cls,
                        world_context_object: Object,
                        duration: float = 0.200000,
                        latent_info: LatentActionInfo = ...) -> None
```

X.retriggerable_delay(world_context_object, duration=0.200000, latent_info) -> None
Perform a latent action with a retriggerable delay (specified in seconds).  Calling again while it is counting down will reset the countdown to Duration.

Args:
    world_context_object (Object): 
    duration (float): length of delay (in seconds).
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.SystemLibrary.reset_gamepad_assignment_to_controller"></a>

#### reset_gamepad_assignment_to_controller

```python
@classmethod
def reset_gamepad_assignment_to_controller(cls, controller_id: int) -> None
```

X.reset_gamepad_assignment_to_controller(controller_id) -> None
* Resets the gamepad assignment to player controller id (Android and iOS only)

Args:
    controller_id (int32):

<a id="unreal.SystemLibrary.reset_gamepad_assignments"></a>

#### reset_gamepad_assignments

```python
@classmethod
def reset_gamepad_assignments(cls) -> None
```

X.reset_gamepad_assignments() -> None
Resets the gamepad to player controller id assignments (Android and iOS only)

<a id="unreal.SystemLibrary.reset_editor_property"></a>

#### reset_editor_property

```python
@classmethod
def reset_editor_property(
    cls,
    object: Object,
    property_name: Name,
    change_notify_mode:
    PropertyAccessChangeNotifyMode = PropertyAccessChangeNotifyMode.DEFAULT
) -> bool
```

X.reset_editor_property(object, property_name, change_notify_mode=PropertyAccessChangeNotifyMode.DEFAULT) -> bool
Attempts to reset the value of a named property on the given object so that it matches the value of the archetype.

Args:
    object (Object): The object you want to reset a property value on.
    property_name (Name): The name of the object property to reset the value of.
    change_notify_mode (PropertyAccessChangeNotifyMode): When to emit property change notifications.

Returns:
    bool: Whether the property value was found and correctly reset.

<a id="unreal.SystemLibrary.register_for_remote_notifications"></a>

#### register_for_remote_notifications

```python
@classmethod
def register_for_remote_notifications(cls) -> None
```

X.register_for_remote_notifications() -> None
Requests permission to send remote notifications to the user's device.
(Android and iOS only)

<a id="unreal.SystemLibrary.quit_game"></a>

#### quit_game

```python
@classmethod
def quit_game(cls, world_context_object: Object,
              specific_player: PlayerController,
              quit_preference: QuitPreference,
              ignore_platform_restrictions: bool) -> None
```

X.quit_game(world_context_object, specific_player, quit_preference, ignore_platform_restrictions) -> None
Exit the current game

Args:
    world_context_object (Object): 
    specific_player (PlayerController): The specific player to quit the game. If not specified, player 0 will quit.
    quit_preference (QuitPreference): Form of quitting.
    ignore_platform_restrictions (bool): Ignores and best-practices based on platform (e.g on some consoles, games should never quit). Non-shipping only

<a id="unreal.SystemLibrary.quit_editor"></a>

#### quit_editor

```python
@classmethod
def quit_editor(cls) -> None
```

X.quit_editor() -> None
Exit the editor

<a id="unreal.SystemLibrary.print_text"></a>

#### print_text

```python
@classmethod
def print_text(cls,
               world_context_object: Object,
               text: Text = "Hello",
               print_to_screen: bool = True,
               print_to_log: bool = True,
               text_color: LinearColor = [
                   0.000000, 0.660000, 1.000000, 1.000000
               ],
               duration: float = 2.000000,
               key: Name = "None") -> None
```

X.print_text(world_context_object, text="Hello", print_to_screen=True, print_to_log=True, text_color=[0.000000, 0.660000, 1.000000, 1.000000], duration=2.000000, key="None") -> None
Prints text to the log, and optionally, to the screen
If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

Args:
    world_context_object (Object): 
    text (Text): The text to log out
    print_to_screen (bool): Whether or not to print the output to the screen
    print_to_log (bool): Whether or not to print the output to the log
    text_color (LinearColor): The color of the text to display
    duration (float): The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config.
    key (Name): If a non-empty key is provided, the message will replace any existing on-screen messages with the same key.

<a id="unreal.SystemLibrary.print_string"></a>

#### print_string

```python
@classmethod
def print_string(cls,
                 world_context_object: Object,
                 string: str = "Hello",
                 print_to_screen: bool = True,
                 print_to_log: bool = True,
                 text_color: LinearColor = [
                     0.000000, 0.660000, 1.000000, 1.000000
                 ],
                 duration: float = 2.000000,
                 key: Name = "None") -> None
```

X.print_string(world_context_object, string="Hello", print_to_screen=True, print_to_log=True, text_color=[0.000000, 0.660000, 1.000000, 1.000000], duration=2.000000, key="None") -> None
Prints a string to the log, and optionally, to the screen
If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

Args:
    world_context_object (Object): 
    string (str): The string to log out
    print_to_screen (bool): Whether or not to print the output to the screen
    print_to_log (bool): Whether or not to print the output to the log
    text_color (LinearColor): The color of the text to display
    duration (float): The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config.
    key (Name): If a non-empty key is provided, the message will replace any existing on-screen messages with the same key.

<a id="unreal.SystemLibrary.parse_param_value"></a>

#### parse_param_value

```python
@classmethod
def parse_param_value(cls, string: str, param: str) -> Optional[str]
```

X.parse_param_value(string, param) -> str or None
Returns 'value' if -option=value is in the string

Args:
    string (str): 
    param (str): 

Returns:
    str or None: 

    out_value (str):

<a id="unreal.SystemLibrary.parse_param"></a>

#### parse_param

```python
@classmethod
def parse_param(cls, string: str, param: str) -> bool
```

X.parse_param(string, param) -> bool
Returns true if the string has -param in it (do not specify the leading -)

Args:
    string (str): 
    param (str): 

Returns:
    bool:

<a id="unreal.SystemLibrary.parse_command_line"></a>

#### parse_command_line

```python
@classmethod
def parse_command_line(
        cls, cmd_line: str) -> Tuple[Array[str], Array[str], Map[str, str]]
```

X.parse_command_line(cmd_line) -> (out_tokens=Array[str], out_switches=Array[str], out_params=Map[str, str])
* Parses the given string into loose tokens, switches (arguments that begin with - or /) and parameters (-mySwitch=myVar)
*
*

Args:
    cmd_line (str): The the string to parse (ie '-foo -bar=/game/baz testtoken' ) *

Returns:
    tuple: 

    out_tokens (Array[str]): 

    out_switches (Array[str]): 

    out_params (Map[str, str]):

<a id="unreal.SystemLibrary.not_equal_soft_object_reference"></a>

#### not_equal_soft_object_reference

```python
@classmethod
def not_equal_soft_object_reference(cls, a: Object, b: Object) -> bool
```

X.not_equal_soft_object_reference(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (Object): 
    b (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.not_equal_soft_class_reference"></a>

#### not_equal_soft_class_reference

```python
@classmethod
def not_equal_soft_class_reference(cls, a: Class, b: Class) -> bool
```

X.not_equal_soft_class_reference(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (Class): 
    b (Class): 

Returns:
    bool:

<a id="unreal.SystemLibrary.not_equal_primary_asset_type"></a>

#### not_equal_primary_asset_type

```python
@classmethod
def not_equal_primary_asset_type(cls, a: PrimaryAssetType,
                                 b: PrimaryAssetType) -> bool
```

X.not_equal_primary_asset_type(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (PrimaryAssetType): 
    b (PrimaryAssetType): 

Returns:
    bool:

<a id="unreal.SystemLibrary.not_equal_primary_asset_id"></a>

#### not_equal_primary_asset_id

```python
@classmethod
def not_equal_primary_asset_id(cls, a: PrimaryAssetId,
                               b: PrimaryAssetId) -> bool
```

X.not_equal_primary_asset_id(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (PrimaryAssetId): 
    b (PrimaryAssetId): 

Returns:
    bool:

<a id="unreal.SystemLibrary.normalize_filename"></a>

#### normalize_filename

```python
@classmethod
def normalize_filename(cls, filename: str) -> str
```

X.normalize_filename(filename) -> str
Convert all / and \ to TEXT("/")

Args:
    filename (str): 

Returns:
    str:

<a id="unreal.SystemLibrary.move_component_to"></a>

#### move_component_to

```python
@classmethod
def move_component_to(cls,
                      component: SceneComponent,
                      target_relative_location: Vector,
                      target_relative_rotation: Rotator,
                      ease_out: bool,
                      ease_in: bool,
                      over_time: float = 0.200000,
                      force_shortest_rotation_path: bool = ...,
                      move_action: MoveComponentAction = ...,
                      latent_info: LatentActionInfo = ...) -> None
```

X.move_component_to(component, target_relative_location, target_relative_rotation, ease_out, ease_in, over_time=0.200000, force_shortest_rotation_path, move_action, latent_info) -> None
* Interpolate a component to the specified relative location and rotation over the course of OverTime seconds.
*
see: EMoveComponentAction *

Args:
    component (SceneComponent): Component to interpolate *
    target_relative_location (Vector): Relative target location *
    target_relative_rotation (Rotator): Relative target rotation *
    ease_out (bool): if true we will ease out (ie end slowly) during interpolation *
    ease_in (bool): if true we will ease in (ie start slowly) during interpolation *
    over_time (float): duration of interpolation *
    force_shortest_rotation_path (bool): if true we will always use the shortest path for rotation *
    move_action (MoveComponentAction): required movement behavior
    latent_info (LatentActionInfo): The latent action

<a id="unreal.SystemLibrary.make_literal_text"></a>

#### make_literal_text

```python
@classmethod
def make_literal_text(cls, value: Text) -> Text
```

X.make_literal_text(value) -> Text
Creates a literal FText

Args:
    value (Text): value to set the FText to

Returns:
    Text: The literal FText

<a id="unreal.SystemLibrary.make_literal_string"></a>

#### make_literal_string

```python
@classmethod
def make_literal_string(cls, value: str) -> str
```

X.make_literal_string(value) -> str
Creates a literal string

Args:
    value (str): value to set the string to

Returns:
    str: The literal string

<a id="unreal.SystemLibrary.make_literal_name"></a>

#### make_literal_name

```python
@classmethod
def make_literal_name(cls, value: Name) -> Name
```

X.make_literal_name(value) -> Name
Creates a literal name

Args:
    value (Name): value to set the name to

Returns:
    Name: The literal name

<a id="unreal.SystemLibrary.make_literal_int64"></a>

#### make_literal_int64

```python
@classmethod
def make_literal_int64(cls, value: int) -> int
```

X.make_literal_int64(value) -> int64
Creates a literal 64-bit integer

Args:
    value (int64): value to set the 64-bit integer to

Returns:
    int64: The literal 64-bit integer

<a id="unreal.SystemLibrary.make_literal_int"></a>

#### make_literal_int

```python
@classmethod
def make_literal_int(cls, value: int) -> int
```

X.make_literal_int(value) -> int32
Creates a literal integer

Args:
    value (int32): value to set the integer to

Returns:
    int32: The literal integer

<a id="unreal.SystemLibrary.make_literal_double"></a>

#### make_literal_double

```python
@classmethod
def make_literal_double(cls, value: float) -> float
```

X.make_literal_double(value) -> double
Creates a literal float (double-precision)

Args:
    value (double): value to set the float (double-precision) to

Returns:
    double: The literal float (double-precision)

<a id="unreal.SystemLibrary.make_literal_float"></a>

#### make_literal_float

```python
@classmethod
def make_literal_float(cls, value: float) -> float
```

deprecated: 'make_literal_float' was renamed to 'make_literal_double'.

<a id="unreal.SystemLibrary.make_literal_byte"></a>

#### make_literal_byte

```python
@classmethod
def make_literal_byte(cls, value: int) -> int
```

X.make_literal_byte(value) -> uint8
Creates a literal byte

Args:
    value (uint8): value to set the byte to

Returns:
    uint8: The literal byte

<a id="unreal.SystemLibrary.make_literal_bool"></a>

#### make_literal_bool

```python
@classmethod
def make_literal_bool(cls, value: bool) -> bool
```

X.make_literal_bool(value) -> bool
Creates a literal bool

Args:
    value (bool): value to set the bool to

Returns:
    bool: The literal bool

<a id="unreal.SystemLibrary.log_string"></a>

#### log_string

```python
@classmethod
def log_string(cls, string: str = "Hello", print_to_log: bool = True) -> None
```

X.log_string(string="Hello", print_to_log=True) -> None
Prints a string to the log
If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

Args:
    string (str): The string to log out
    print_to_log (bool): Whether or not to print the output to the log

<a id="unreal.SystemLibrary.load_interstitial_ad"></a>

#### load_interstitial_ad

```python
@classmethod
def load_interstitial_ad(cls, ad_id_index: int) -> None
```

X.load_interstitial_ad(ad_id_index) -> None
Will load a fullscreen interstitial AdMob ad. Call this before using ShowInterstitialAd
(Android only)

Args:
    ad_id_index (int32): The index of the ID to select for the ad to show

<a id="unreal.SystemLibrary.load_class_asset_blocking"></a>

#### load_class_asset_blocking

```python
@classmethod
def load_class_asset_blocking(cls, asset_class: Class) -> Class
```

X.load_class_asset_blocking(asset_class) -> type(Class)
Resolves or loads a Soft Class Reference immediately, this will cause hitches and Async Load Class Asset should be used if possible

Args:
    asset_class (Class): 

Returns:
    type(Class):

<a id="unreal.SystemLibrary.load_asset_blocking"></a>

#### load_asset_blocking

```python
@classmethod
def load_asset_blocking(cls, asset: Object) -> Object
```

X.load_asset_blocking(asset) -> Object
Resolves or loads a Soft Object Reference immediately, this will cause hitches and Async Load Asset should be used if possible

Args:
    asset (Object): 

Returns:
    Object:

<a id="unreal.SystemLibrary.line_trace_single_for_objects"></a>

#### line_trace_single_for_objects

```python
@classmethod
def line_trace_single_for_objects(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.line_trace_single_for_objects(world_context_object, start, end, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Does a collision trace along the given line and returns the first hit encountered.
This only finds objects that are of a type specified by ObjectTypes.

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    object_types (Array[ObjectTypeQuery]): Array of Object Types to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.line_trace_single_by_profile"></a>

#### line_trace_single_by_profile

```python
@classmethod
def line_trace_single_by_profile(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.line_trace_single_by_profile(world_context_object, start, end, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Trace a ray against the world using a specific profile and return the first blocking hit

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    profile_name (Name): The 'profile' used to determine which components to hit
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.line_trace_single"></a>

#### line_trace_single

```python
@classmethod
def line_trace_single(cls,
                      world_context_object: Object,
                      start: Vector,
                      end: Vector,
                      trace_channel: TraceTypeQuery,
                      trace_complex: bool,
                      actors_to_ignore: Array[Actor],
                      draw_debug_type: DrawDebugTrace,
                      ignore_self: bool = True,
                      trace_color: LinearColor = [
                          1.000000, 0.000000, 0.000000, 1.000000
                      ],
                      trace_hit_color: LinearColor = [
                          0.000000, 1.000000, 0.000000, 1.000000
                      ],
                      draw_time: float = 5.000000) -> Optional[HitResult]
```

X.line_trace_single(world_context_object, start, end, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Does a collision trace along the given line and returns the first blocking hit encountered.
This trace finds the objects that RESPONDS to the given TraceChannel

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.line_trace_single_new"></a>

#### line_trace_single_new

```python
@classmethod
def line_trace_single_new(cls,
                          world_context_object: Object,
                          start: Vector,
                          end: Vector,
                          trace_channel: TraceTypeQuery,
                          trace_complex: bool,
                          actors_to_ignore: Array[Actor],
                          draw_debug_type: DrawDebugTrace,
                          ignore_self: bool = True,
                          trace_color: LinearColor = [
                              1.000000, 0.000000, 0.000000, 1.000000
                          ],
                          trace_hit_color: LinearColor = [
                              0.000000, 1.000000, 0.000000, 1.000000
                          ],
                          draw_time: float = 5.000000) -> Optional[HitResult]
```

deprecated: 'line_trace_single_new' was renamed to 'line_trace_single'.

<a id="unreal.SystemLibrary.line_trace_multi_for_objects"></a>

#### line_trace_multi_for_objects

```python
@classmethod
def line_trace_multi_for_objects(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.line_trace_multi_for_objects(world_context_object, start, end, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Does a collision trace along the given line and returns all hits encountered.
This only finds objects that are of a type specified by ObjectTypes.

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    object_types (Array[ObjectTypeQuery]): Array of Object Types to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a hit, false otherwise.

    out_hits (Array[HitResult]):

<a id="unreal.SystemLibrary.line_trace_multi_by_profile"></a>

#### line_trace_multi_by_profile

```python
@classmethod
def line_trace_multi_by_profile(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.line_trace_multi_by_profile(world_context_object, start, end, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Trace a ray against the world using a specific profile and return overlapping hits and then first blocking hit
Results are sorted, so a blocking hit (if found) will be the last element of the array
Only the single closest blocking result will be generated, no tests will be done after that

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    profile_name (Name): The 'profile' used to determine which components to hit
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a blocking hit, false otherwise.

    out_hits (Array[HitResult]):

<a id="unreal.SystemLibrary.line_trace_multi"></a>

#### line_trace_multi

```python
@classmethod
def line_trace_multi(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        trace_channel: TraceTypeQuery,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.line_trace_multi(world_context_object, start, end, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Does a collision trace along the given line and returns all hits encountered up to and including the first blocking hit.
This trace finds the objects that RESPOND to the given TraceChannel

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    trace_channel (TraceTypeQuery): The channel to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a blocking hit, false otherwise.

    out_hits (Array[HitResult]):

<a id="unreal.SystemLibrary.line_trace_multi_new"></a>

#### line_trace_multi_new

```python
@classmethod
def line_trace_multi_new(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        trace_channel: TraceTypeQuery,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

deprecated: 'line_trace_multi_new' was renamed to 'line_trace_multi'.

<a id="unreal.SystemLibrary.launch_url"></a>

#### launch_url

```python
@classmethod
def launch_url(cls, url: str) -> None
```

X.launch_url(url) -> None
Opens the specified URL in the platform's web browser of choice

Args:
    url (str):

<a id="unreal.SystemLibrary.launch_external_url"></a>

#### launch_external_url

```python
@classmethod
def launch_external_url(cls, domain_strings: Array[str], url: str) -> None
```

X.launch_external_url(domain_strings, url) -> None
Opens an external URL in the platform's web browser of choice if it meets the allowlist of passed in domains

Args:
    domain_strings (Array[str]): 
    url (str):

<a id="unreal.SystemLibrary.un_pause_timer_handle"></a>

#### un_pause_timer_handle

```python
@classmethod
def un_pause_timer_handle(cls, world_context_object: Object,
                          handle: TimerHandle) -> None
```

X.un_pause_timer_handle(world_context_object, handle) -> None
Resumes a paused timer from its current elapsed time.

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle of the timer to unpause.

<a id="unreal.SystemLibrary.un_pause_timer_delegate"></a>

#### un_pause_timer_delegate

```python
@classmethod
def un_pause_timer_delegate(cls, delegate: TimerDynamicDelegate) -> None
```

X.un_pause_timer_delegate(delegate) -> None
Resumes a paused timer from its current elapsed time.
deprecated: Use Unpause Timer by Handle

Args:
    delegate (TimerDynamicDelegate):

<a id="unreal.SystemLibrary.un_pause_timer"></a>

#### un_pause_timer

```python
@classmethod
def un_pause_timer(cls, object: Object, function_name: str) -> None
```

X.un_pause_timer(object, function_name) -> None
Resumes a paused timer from its current elapsed time.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

<a id="unreal.SystemLibrary.timer_exists_handle"></a>

#### timer_exists_handle

```python
@classmethod
def timer_exists_handle(cls, world_context_object: Object,
                        handle: TimerHandle) -> bool
```

X.timer_exists_handle(world_context_object, handle) -> bool
Returns true is a timer for the given handle exists, false otherwise.

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle to check whether it exists.

Returns:
    bool: True if the timer exists.

<a id="unreal.SystemLibrary.timer_exists_delegate"></a>

#### timer_exists_delegate

```python
@classmethod
def timer_exists_delegate(cls, delegate: TimerDynamicDelegate) -> bool
```

X.timer_exists_delegate(delegate) -> bool
Returns true is a timer for the given delegate exists, false otherwise.
deprecated: Use Does Timer Exist by Handle

Args:
    delegate (TimerDynamicDelegate): 

Returns:
    bool: True if the timer exists.

<a id="unreal.SystemLibrary.timer_exists"></a>

#### timer_exists

```python
@classmethod
def timer_exists(cls, object: Object, function_name: str) -> bool
```

X.timer_exists(object, function_name) -> bool
Returns true is a timer for the given delegate exists, false otherwise.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

Returns:
    bool: True if the timer exists.

<a id="unreal.SystemLibrary.set_timer_for_next_tick_delegate"></a>

#### set_timer_for_next_tick_delegate

```python
@classmethod
def set_timer_for_next_tick_delegate(
        cls, delegate: TimerDynamicDelegate) -> TimerHandle
```

X.set_timer_for_next_tick_delegate(delegate) -> TimerHandle
Set a timer to execute a delegate next tick.

Args:
    delegate (TimerDynamicDelegate): 

Returns:
    TimerHandle: The timer handle to pass to other timer functions to manipulate this timer.

<a id="unreal.SystemLibrary.set_timer_for_next_tick"></a>

#### set_timer_for_next_tick

```python
@classmethod
def set_timer_for_next_tick(cls, object: Object,
                            function_name: str) -> TimerHandle
```

X.set_timer_for_next_tick(object, function_name) -> TimerHandle
Set a timer to execute a delegate on the next tick.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

Returns:
    TimerHandle: The timer handle to pass to other timer functions to manipulate this timer.

<a id="unreal.SystemLibrary.set_timer_delegate"></a>

#### set_timer_delegate

```python
@classmethod
def set_timer_delegate(
        cls,
        delegate: TimerDynamicDelegate,
        time: float,
        looping: bool,
        max_once_per_frame: bool = False,
        initial_start_delay: float = 0.000000,
        initial_start_delay_variance: float = 0.000000) -> TimerHandle
```

X.set_timer_delegate(delegate, time, looping, max_once_per_frame=False, initial_start_delay=0.000000, initial_start_delay_variance=0.000000) -> TimerHandle
Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

Args:
    delegate (TimerDynamicDelegate): 
    time (float): How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set.
    looping (bool): True to keep executing the delegate every Time seconds, false to execute delegate only once.
    max_once_per_frame (bool): For looping timers, whether to execute only once when the timer would otherwise expires multiple times in the current frame.
    initial_start_delay (float): Initial delay passed to the timer manager, in seconds.
    initial_start_delay_variance (float): Use this to add some variance to when the timer starts in lieu of doing a random range on the InitialStartDelay input, in seconds.

Returns:
    TimerHandle: The timer handle to pass to other timer functions to manipulate this timer.

<a id="unreal.SystemLibrary.set_timer"></a>

#### set_timer

```python
@classmethod
def set_timer(cls,
              object: Object,
              function_name: str,
              time: float,
              looping: bool,
              max_once_per_frame: bool = False,
              initial_start_delay: float = 0.000000,
              initial_start_delay_variance: float = 0.000000) -> TimerHandle
```

X.set_timer(object, function_name, time, looping, max_once_per_frame=False, initial_start_delay=0.000000, initial_start_delay_variance=0.000000) -> TimerHandle
Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.
    time (float): How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set.
    looping (bool): True to keep executing the delegate every Time seconds, false to execute delegate only once.
    max_once_per_frame (bool): For looping timers, whether to execute only once when the timer would otherwise expires multiple times in the current frame.
    initial_start_delay (float): Initial delay passed to the timer manager to allow some variance in when the timer starts, in seconds.
    initial_start_delay_variance (float): Use this to add some variance to when the timer starts in lieu of doing a random range on the InitialStartDelay input, in seconds.

Returns:
    TimerHandle: The timer handle to pass to other timer functions to manipulate this timer.

<a id="unreal.SystemLibrary.pause_timer_handle"></a>

#### pause_timer_handle

```python
@classmethod
def pause_timer_handle(cls, world_context_object: Object,
                       handle: TimerHandle) -> None
```

X.pause_timer_handle(world_context_object, handle) -> None
Pauses a set timer at its current elapsed time.

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle of the timer to pause.

<a id="unreal.SystemLibrary.pause_timer_delegate"></a>

#### pause_timer_delegate

```python
@classmethod
def pause_timer_delegate(cls, delegate: TimerDynamicDelegate) -> None
```

X.pause_timer_delegate(delegate) -> None
Pauses a set timer at its current elapsed time.
deprecated: Use Pause Timer by Handle

Args:
    delegate (TimerDynamicDelegate):

<a id="unreal.SystemLibrary.pause_timer"></a>

#### pause_timer

```python
@classmethod
def pause_timer(cls, object: Object, function_name: str) -> None
```

X.pause_timer(object, function_name) -> None
Pauses a set timer at its current elapsed time.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

<a id="unreal.SystemLibrary.is_valid_timer_handle"></a>

#### is_valid_timer_handle

```python
@classmethod
def is_valid_timer_handle(cls, handle: TimerHandle) -> bool
```

X.is_valid_timer_handle(handle) -> bool
Returns whether the timer handle is valid. This does not indicate that there is an active timer that this handle references, but rather that it once referenced a valid timer.

Args:
    handle (TimerHandle): The handle of the timer to check validity of.

Returns:
    bool: Whether the timer handle is valid.

<a id="unreal.SystemLibrary.is_timer_paused_handle"></a>

#### is_timer_paused_handle

```python
@classmethod
def is_timer_paused_handle(cls, world_context_object: Object,
                           handle: TimerHandle) -> bool
```

X.is_timer_paused_handle(world_context_object, handle) -> bool
Returns true if a timer exists and is paused for the given handle, false otherwise.

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle of the timer to check whether it is paused.

Returns:
    bool: True if the timer exists and is paused.

<a id="unreal.SystemLibrary.is_timer_paused_delegate"></a>

#### is_timer_paused_delegate

```python
@classmethod
def is_timer_paused_delegate(cls, delegate: TimerDynamicDelegate) -> bool
```

X.is_timer_paused_delegate(delegate) -> bool
Returns true if a timer exists and is paused for the given delegate, false otherwise.
deprecated: Use Is Timer Paused by Handle

Args:
    delegate (TimerDynamicDelegate): 

Returns:
    bool: True if the timer exists and is paused.

<a id="unreal.SystemLibrary.is_timer_paused"></a>

#### is_timer_paused

```python
@classmethod
def is_timer_paused(cls, object: Object, function_name: str) -> bool
```

X.is_timer_paused(object, function_name) -> bool
Returns true if a timer exists and is paused for the given delegate, false otherwise.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

Returns:
    bool: True if the timer exists and is paused.

<a id="unreal.SystemLibrary.is_timer_active_handle"></a>

#### is_timer_active_handle

```python
@classmethod
def is_timer_active_handle(cls, world_context_object: Object,
                           handle: TimerHandle) -> bool
```

X.is_timer_active_handle(world_context_object, handle) -> bool
Returns true if a timer exists and is active for the given handle, false otherwise.

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle of the timer to check whether it is active.

Returns:
    bool: True if the timer exists and is active.

<a id="unreal.SystemLibrary.is_timer_active_delegate"></a>

#### is_timer_active_delegate

```python
@classmethod
def is_timer_active_delegate(cls, delegate: TimerDynamicDelegate) -> bool
```

X.is_timer_active_delegate(delegate) -> bool
Returns true if a timer exists and is active for the given delegate, false otherwise.
deprecated: Use Is Timer Active by Handle

Args:
    delegate (TimerDynamicDelegate): 

Returns:
    bool: True if the timer exists and is active.

<a id="unreal.SystemLibrary.is_timer_active"></a>

#### is_timer_active

```python
@classmethod
def is_timer_active(cls, object: Object, function_name: str) -> bool
```

X.is_timer_active(object, function_name) -> bool
Returns true if a timer exists and is active for the given delegate, false otherwise.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

Returns:
    bool: True if the timer exists and is active.

<a id="unreal.SystemLibrary.invalidate_timer_handle"></a>

#### invalidate_timer_handle

```python
@classmethod
def invalidate_timer_handle(
        cls, handle: TimerHandle) -> Tuple[TimerHandle, TimerHandle]
```

X.invalidate_timer_handle(handle) -> (TimerHandle, handle=TimerHandle)
Invalidate the supplied TimerHandle and return it.

Args:
    handle (TimerHandle): The handle of the timer to invalidate.

Returns:
    TimerHandle: Return the invalidated timer handle for convenience.

    handle (TimerHandle): The handle of the timer to invalidate.

<a id="unreal.SystemLibrary.get_timer_remaining_time_handle"></a>

#### get_timer_remaining_time_handle

```python
@classmethod
def get_timer_remaining_time_handle(cls, world_context_object: Object,
                                    handle: TimerHandle) -> float
```

X.get_timer_remaining_time_handle(world_context_object, handle) -> float
Returns time until the timer will next execute its handle.

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle of the timer to time remaining of.

Returns:
    float: How long is remaining in the current iteration of the timer.

<a id="unreal.SystemLibrary.get_timer_remaining_time_delegate"></a>

#### get_timer_remaining_time_delegate

```python
@classmethod
def get_timer_remaining_time_delegate(cls,
                                      delegate: TimerDynamicDelegate) -> float
```

X.get_timer_remaining_time_delegate(delegate) -> float
Returns time until the timer will next execute its delegate.
deprecated: Use Get Timer Remaining Time by Handle

Args:
    delegate (TimerDynamicDelegate): 

Returns:
    float: How long is remaining in the current iteration of the timer.

<a id="unreal.SystemLibrary.get_timer_remaining_time"></a>

#### get_timer_remaining_time

```python
@classmethod
def get_timer_remaining_time(cls, object: Object, function_name: str) -> float
```

X.get_timer_remaining_time(object, function_name) -> float
Returns time until the timer will next execute its delegate.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

Returns:
    float: How long is remaining in the current iteration of the timer.

<a id="unreal.SystemLibrary.get_timer_elapsed_time_handle"></a>

#### get_timer_elapsed_time_handle

```python
@classmethod
def get_timer_elapsed_time_handle(cls, world_context_object: Object,
                                  handle: TimerHandle) -> float
```

X.get_timer_elapsed_time_handle(world_context_object, handle) -> float
Returns elapsed time for the given handle (time since current countdown iteration began).

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle of the timer to get the elapsed time of.

Returns:
    float: How long has elapsed since the current iteration of the timer began.

<a id="unreal.SystemLibrary.get_timer_elapsed_time_delegate"></a>

#### get_timer_elapsed_time_delegate

```python
@classmethod
def get_timer_elapsed_time_delegate(cls,
                                    delegate: TimerDynamicDelegate) -> float
```

X.get_timer_elapsed_time_delegate(delegate) -> float
Returns elapsed time for the given delegate (time since current countdown iteration began).
deprecated: Use Get Timer Elapsed Time by Handle

Args:
    delegate (TimerDynamicDelegate): 

Returns:
    float: How long has elapsed since the current iteration of the timer began.

<a id="unreal.SystemLibrary.get_timer_elapsed_time"></a>

#### get_timer_elapsed_time

```python
@classmethod
def get_timer_elapsed_time(cls, object: Object, function_name: str) -> float
```

X.get_timer_elapsed_time(object, function_name) -> float
Returns elapsed time for the given delegate (time since current countdown iteration began).

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

Returns:
    float: How long has elapsed since the current iteration of the timer began.

<a id="unreal.SystemLibrary.clear_timer_handle"></a>

#### clear_timer_handle

```python
@classmethod
def clear_timer_handle(cls, world_context_object: Object,
                       handle: TimerHandle) -> None
```

X.clear_timer_handle(world_context_object, handle) -> None
Clears a set timer.
deprecated: Use Clear and Invalidate Timer by Handle. Note: you no longer need to reset your handle yourself after switching to the new function.

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle of the timer to clear.

<a id="unreal.SystemLibrary.clear_timer_delegate"></a>

#### clear_timer_delegate

```python
@classmethod
def clear_timer_delegate(cls, delegate: TimerDynamicDelegate) -> None
```

X.clear_timer_delegate(delegate) -> None
Clears a set timer.
deprecated: Use Clear Timer by Handle

Args:
    delegate (TimerDynamicDelegate):

<a id="unreal.SystemLibrary.clear_timer"></a>

#### clear_timer

```python
@classmethod
def clear_timer(cls, object: Object, function_name: str) -> None
```

X.clear_timer(object, function_name) -> None
Clears a set timer.

Args:
    object (Object): Object that implements the delegate function. Defaults to self (this blueprint)
    function_name (str): Delegate function name. Can be a K2 function or a Custom Event.

<a id="unreal.SystemLibrary.clear_and_invalidate_timer_handle"></a>

#### clear_and_invalidate_timer_handle

```python
@classmethod
def clear_and_invalidate_timer_handle(cls, world_context_object: Object,
                                      handle: TimerHandle) -> TimerHandle
```

X.clear_and_invalidate_timer_handle(world_context_object, handle) -> TimerHandle
Clears a set timer.

Args:
    world_context_object (Object): 
    handle (TimerHandle): The handle of the timer to clear.

Returns:
    TimerHandle: 

    handle (TimerHandle): The handle of the timer to clear.

<a id="unreal.SystemLibrary.is_valid_soft_object_reference"></a>

#### is_valid_soft_object_reference

```python
@classmethod
def is_valid_soft_object_reference(cls, soft_object_reference: Object) -> bool
```

X.is_valid_soft_object_reference(soft_object_reference) -> bool
Returns true if the Soft Object Reference is not null

Args:
    soft_object_reference (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_valid_soft_class_reference"></a>

#### is_valid_soft_class_reference

```python
@classmethod
def is_valid_soft_class_reference(cls, soft_class_reference: Class) -> bool
```

X.is_valid_soft_class_reference(soft_class_reference) -> bool
Returns true if the Soft Class Reference is not null

Args:
    soft_class_reference (Class): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_valid_primary_asset_type"></a>

#### is_valid_primary_asset_type

```python
@classmethod
def is_valid_primary_asset_type(cls,
                                primary_asset_type: PrimaryAssetType) -> bool
```

X.is_valid_primary_asset_type(primary_asset_type) -> bool
Returns list of Primary Asset Ids for a PrimaryAssetType

Args:
    primary_asset_type (PrimaryAssetType): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_valid_primary_asset_id"></a>

#### is_valid_primary_asset_id

```python
@classmethod
def is_valid_primary_asset_id(cls, primary_asset_id: PrimaryAssetId) -> bool
```

X.is_valid_primary_asset_id(primary_asset_id) -> bool
Returns true if the Primary Asset Id is valid

Args:
    primary_asset_id (PrimaryAssetId): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_valid_interface"></a>

#### is_valid_interface

```python
@classmethod
def is_valid_interface(cls, interface: Interface) -> bool
```

X.is_valid_interface(interface) -> bool
Checks if the interface instance has a valid object for blueprint interface functions.
This will return true for both natively implemented and blueprint implemented interfaces.

Args:
    interface (Interface): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_valid_class"></a>

#### is_valid_class

```python
@classmethod
def is_valid_class(cls, class_: Class) -> bool
```

X.is_valid_class(class_) -> bool
Return true if the class is usable : non-null and not pending kill

Args:
    class_ (type(Class)): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_valid"></a>

#### is_valid

```python
@classmethod
def is_valid(cls, object: Object) -> bool
```

X.is_valid(object) -> bool
Return true if the object is usable : non-null and not pending kill

Args:
    object (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_unattended"></a>

#### is_unattended

```python
@classmethod
def is_unattended(cls) -> bool
```

X.is_unattended() -> bool
Returns true if running unattended (-unattended is on the command line)

Returns:
    bool: Unattended state

<a id="unreal.SystemLibrary.is_standalone"></a>

#### is_standalone

```python
@classmethod
def is_standalone(cls, world_context_object: Object) -> bool
```

X.is_standalone(world_context_object) -> bool
Returns whether this game instance is stand alone (no networking).

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_split_screen"></a>

#### is_split_screen

```python
@classmethod
def is_split_screen(cls, world_context_object: Object) -> bool
```

X.is_split_screen(world_context_object) -> bool
Is Split Screen
deprecated: Use HasMultipleLocalPlayers instead

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_server"></a>

#### is_server

```python
@classmethod
def is_server(cls, world_context_object: Object) -> bool
```

X.is_server(world_context_object) -> bool
Returns whether the world this object is in is the host or not

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_screensaver_enabled"></a>

#### is_screensaver_enabled

```python
@classmethod
def is_screensaver_enabled(cls) -> bool
```

X.is_screensaver_enabled() -> bool
Returns true if screen saver is enabled.

Returns:
    bool:

<a id="unreal.SystemLibrary.is_packaged_for_distribution"></a>

#### is_packaged_for_distribution

```python
@classmethod
def is_packaged_for_distribution(cls) -> bool
```

X.is_packaged_for_distribution() -> bool
Returns whether this is a build that is packaged for distribution

Returns:
    bool:

<a id="unreal.SystemLibrary.is_object_of_soft_class"></a>

#### is_object_of_soft_class

```python
@classmethod
def is_object_of_soft_class(cls, object: Object, soft_class: Class) -> bool
```

X.is_object_of_soft_class(object, soft_class) -> bool
Returns true if Object is of type SoftClass - either an instance of the class or child class, or implements the interface. Alternative to Cast - slower but without adding a hard reference.

Args:
    object (Object): 
    soft_class (Class): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_logged_in"></a>

#### is_logged_in

```python
@classmethod
def is_logged_in(cls, specific_player: PlayerController) -> bool
```

X.is_logged_in(specific_player) -> bool
Returns whether the player is logged in to the currently active online subsystem.

Args:
    specific_player (PlayerController): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_interstitial_ad_requested"></a>

#### is_interstitial_ad_requested

```python
@classmethod
def is_interstitial_ad_requested(cls) -> bool
```

X.is_interstitial_ad_requested() -> bool
Returns true if the requested interstitial ad has been successfully requested (false if load request fails)
(Android only)

Returns:
    bool:

<a id="unreal.SystemLibrary.is_interstitial_ad_available"></a>

#### is_interstitial_ad_available

```python
@classmethod
def is_interstitial_ad_available(cls) -> bool
```

X.is_interstitial_ad_available() -> bool
Returns true if the requested interstitial ad is loaded and ready
(Android only)

Returns:
    bool:

<a id="unreal.SystemLibrary.is_editor_property_overridden"></a>

#### is_editor_property_overridden

```python
@classmethod
def is_editor_property_overridden(
        cls, object: Object, property_name: Name) -> EditorPropertyValueState
```

X.is_editor_property_overridden(object, property_name) -> EditorPropertyValueState
Attempts to query whether the value of a named property on the given object overrides the value of its archetype (ie, would ResetEditorProperty do anything?).

Args:
    object (Object): The object you want to query a property value on.
    property_name (Name): The name of the object property to query the value of.

Returns:
    EditorPropertyValueState: What state the requested property is in.

<a id="unreal.SystemLibrary.is_dedicated_server"></a>

#### is_dedicated_server

```python
@classmethod
def is_dedicated_server(cls, world_context_object: Object) -> bool
```

X.is_dedicated_server(world_context_object) -> bool
Returns whether this is running on a dedicated server

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.is_controller_assigned_to_gamepad"></a>

#### is_controller_assigned_to_gamepad

```python
@classmethod
def is_controller_assigned_to_gamepad(cls, controller_id: int) -> bool
```

X.is_controller_assigned_to_gamepad(controller_id) -> bool
Returns true if controller id assigned to a gamepad (Android and iOS only)

Args:
    controller_id (int32): 

Returns:
    bool:

<a id="unreal.SystemLibrary.hide_ad_banner"></a>

#### hide_ad_banner

```python
@classmethod
def hide_ad_banner(cls) -> None
```

X.hide_ad_banner() -> None
Hides the ad banner (iAd on iOS, or AdMob on Android). Will force close the ad if it's open
(iOS and Android only)

<a id="unreal.SystemLibrary.experimental_hide_ad_banner"></a>

#### experimental_hide_ad_banner

```python
@classmethod
def experimental_hide_ad_banner(cls) -> None
```

deprecated: 'experimental_hide_ad_banner' was renamed to 'hide_ad_banner'.

<a id="unreal.SystemLibrary.has_multiple_local_players"></a>

#### has_multiple_local_players

```python
@classmethod
def has_multiple_local_players(cls, world_context_object: Object) -> bool
```

X.has_multiple_local_players(world_context_object) -> bool
Returns whether there are currently multiple local players in the given world

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.get_volume_buttons_handled_by_system"></a>

#### get_volume_buttons_handled_by_system

```python
@classmethod
def get_volume_buttons_handled_by_system(cls) -> bool
```

X.get_volume_buttons_handled_by_system() -> bool
Returns true if system default handling of volume up and volume down buttons enabled (Android only)

Returns:
    bool:

<a id="unreal.SystemLibrary.get_unique_device_id"></a>

#### get_unique_device_id

```python
@classmethod
def get_unique_device_id(cls) -> str
```

X.get_unique_device_id() -> str
Returns the platform specific unique device id
deprecated: Use GetDeviceId instead

Returns:
    str:

<a id="unreal.SystemLibrary.get_system_path"></a>

#### get_system_path

```python
@classmethod
def get_system_path(cls, object: Object) -> str
```

X.get_system_path(object) -> str
Returns the full file system path to a UObject
If given a non-asset UObject, it will return an empty string

Args:
    object (Object): 

Returns:
    str:

<a id="unreal.SystemLibrary.get_supported_fullscreen_resolutions"></a>

#### get_supported_fullscreen_resolutions

```python
@classmethod
def get_supported_fullscreen_resolutions(cls) -> Optional[Array[IntPoint]]
```

X.get_supported_fullscreen_resolutions() -> Array[IntPoint] or None
Gets the list of support fullscreen resolutions.

Returns:
    Array[IntPoint] or None: true if successfully queried the device for available resolutions.

    resolutions (Array[IntPoint]):

<a id="unreal.SystemLibrary.get_struct_top_level_asset_path"></a>

#### get_struct_top_level_asset_path

```python
@classmethod
def get_struct_top_level_asset_path(cls,
                                    struct: ScriptStruct) -> TopLevelAssetPath
```

X.get_struct_top_level_asset_path(struct) -> TopLevelAssetPath
Returns the full path to the specified struct as a Top Level Asset Path used by asset utilities

Args:
    struct (ScriptStruct): 

Returns:
    TopLevelAssetPath:

<a id="unreal.SystemLibrary.get_soft_object_reference_from_primary_asset_id"></a>

#### get_soft_object_reference_from_primary_asset_id

```python
@classmethod
def get_soft_object_reference_from_primary_asset_id(
        cls, primary_asset_id: PrimaryAssetId) -> Object
```

X.get_soft_object_reference_from_primary_asset_id(primary_asset_id) -> Object
Returns the Object Id associated with a Primary Asset Id, this works even if the asset is not loaded

Args:
    primary_asset_id (PrimaryAssetId): 

Returns:
    Object:

<a id="unreal.SystemLibrary.get_soft_object_path"></a>

#### get_soft_object_path

```python
@classmethod
def get_soft_object_path(cls, object: Object) -> SoftObjectPath
```

X.get_soft_object_path(object) -> SoftObjectPath
Returns the full path to the specified object as a Soft Object Path

Args:
    object (Object): 

Returns:
    SoftObjectPath:

<a id="unreal.SystemLibrary.get_soft_class_top_level_asset_path"></a>

#### get_soft_class_top_level_asset_path

```python
@classmethod
def get_soft_class_top_level_asset_path(
        cls, soft_class_reference: Class) -> TopLevelAssetPath
```

X.get_soft_class_top_level_asset_path(soft_class_reference) -> TopLevelAssetPath
Converts a Soft Class Reference to a Top Level Asset Path used by asset utilities

Args:
    soft_class_reference (Class): 

Returns:
    TopLevelAssetPath:

<a id="unreal.SystemLibrary.get_soft_class_reference_from_primary_asset_id"></a>

#### get_soft_class_reference_from_primary_asset_id

```python
@classmethod
def get_soft_class_reference_from_primary_asset_id(
        cls, primary_asset_id: PrimaryAssetId) -> Class
```

X.get_soft_class_reference_from_primary_asset_id(primary_asset_id) -> Class
Returns the Blueprint Class Id associated with a Primary Asset Id, this works even if the asset is not loaded

Args:
    primary_asset_id (PrimaryAssetId): 

Returns:
    Class:

<a id="unreal.SystemLibrary.get_soft_class_path"></a>

#### get_soft_class_path

```python
@classmethod
def get_soft_class_path(cls, class_: Class) -> SoftClassPath
```

X.get_soft_class_path(class_) -> SoftClassPath
Returns the full path to the specified class as a Soft Class Path (that can be used as a Soft Object Path)

Args:
    class_ (type(Class)): 

Returns:
    SoftClassPath:

<a id="unreal.SystemLibrary.get_rendering_material_quality_level"></a>

#### get_rendering_material_quality_level

```python
@classmethod
def get_rendering_material_quality_level(cls) -> int
```

X.get_rendering_material_quality_level() -> int32
Get the clamped state of r.MaterialQualityLevel, see console variable help (allows for scalability, cannot be used in construction scripts)
0: low
1: high
2: medium

Returns:
    int32:

<a id="unreal.SystemLibrary.get_rendering_detail_mode"></a>

#### get_rendering_detail_mode

```python
@classmethod
def get_rendering_detail_mode(cls) -> int
```

X.get_rendering_detail_mode() -> int32
Get the clamped state of r.DetailMode, see console variable help (allows for scalability, cannot be used in construction scripts)
0: low, show objects with DetailMode low
1: medium, show objects with DetailMode medium or below
2: high, show objects with DetailMode high or below
3: epic, show all objects

Returns:
    int32:

<a id="unreal.SystemLibrary.get_project_saved_directory"></a>

#### get_project_saved_directory

```python
@classmethod
def get_project_saved_directory(cls) -> str
```

X.get_project_saved_directory() -> str
Get the saved directory of the current project

Returns:
    str:

<a id="unreal.SystemLibrary.get_project_directory"></a>

#### get_project_directory

```python
@classmethod
def get_project_directory(cls) -> str
```

X.get_project_directory() -> str
Get the directory of the current project

Returns:
    str:

<a id="unreal.SystemLibrary.get_project_content_directory"></a>

#### get_project_content_directory

```python
@classmethod
def get_project_content_directory(cls) -> str
```

X.get_project_content_directory() -> str
Get the content directory of the current project

Returns:
    str:

<a id="unreal.SystemLibrary.get_primary_assets_with_bundle_state"></a>

#### get_primary_assets_with_bundle_state

```python
@classmethod
def get_primary_assets_with_bundle_state(
        cls, required_bundles: Array[Name], excluded_bundles: Array[Name],
        valid_types: Array[PrimaryAssetType],
        force_current_state: bool) -> Array[PrimaryAssetId]
```

X.get_primary_assets_with_bundle_state(required_bundles, excluded_bundles, valid_types, force_current_state) -> Array[PrimaryAssetId]
Returns the list of assets that are in a given bundle state. Required Bundles must be specified
If ExcludedBundles is not empty, it will not return any assets in those bundle states
If ValidTypes is not empty, it will only return assets of those types
If ForceCurrentState is true it will use the current state even if a load is in process

Args:
    required_bundles (Array[Name]): 
    excluded_bundles (Array[Name]): 
    valid_types (Array[PrimaryAssetType]): 
    force_current_state (bool): 

Returns:
    Array[PrimaryAssetId]: 

    out_primary_asset_id_list (Array[PrimaryAssetId]):

<a id="unreal.SystemLibrary.get_primary_asset_id_list"></a>

#### get_primary_asset_id_list

```python
@classmethod
def get_primary_asset_id_list(
        cls, primary_asset_type: PrimaryAssetType) -> Array[PrimaryAssetId]
```

X.get_primary_asset_id_list(primary_asset_type) -> Array[PrimaryAssetId]
Returns list of PrimaryAssetIds for a PrimaryAssetType

Args:
    primary_asset_type (PrimaryAssetType): 

Returns:
    Array[PrimaryAssetId]: 

    out_primary_asset_id_list (Array[PrimaryAssetId]):

<a id="unreal.SystemLibrary.get_primary_asset_id_from_soft_object_reference"></a>

#### get_primary_asset_id_from_soft_object_reference

```python
@classmethod
def get_primary_asset_id_from_soft_object_reference(
        cls, soft_object_reference: Object) -> PrimaryAssetId
```

X.get_primary_asset_id_from_soft_object_reference(soft_object_reference) -> PrimaryAssetId
Returns the Primary Asset Id for a Soft Object Reference, this can return an invalid one if not registered

Args:
    soft_object_reference (Object): 

Returns:
    PrimaryAssetId:

<a id="unreal.SystemLibrary.get_primary_asset_id_from_soft_class_reference"></a>

#### get_primary_asset_id_from_soft_class_reference

```python
@classmethod
def get_primary_asset_id_from_soft_class_reference(
        cls, soft_class_reference: Class) -> PrimaryAssetId
```

X.get_primary_asset_id_from_soft_class_reference(soft_class_reference) -> PrimaryAssetId
Returns the Primary Asset Id for a Soft Class Reference, this can return an invalid one if not registered

Args:
    soft_class_reference (Class): 

Returns:
    PrimaryAssetId:

<a id="unreal.SystemLibrary.get_primary_asset_id_from_object"></a>

#### get_primary_asset_id_from_object

```python
@classmethod
def get_primary_asset_id_from_object(cls, object: Object) -> PrimaryAssetId
```

X.get_primary_asset_id_from_object(object) -> PrimaryAssetId
Returns the Primary Asset Id for an Object, this can return an invalid one if not registered

Args:
    object (Object): 

Returns:
    PrimaryAssetId:

<a id="unreal.SystemLibrary.get_primary_asset_id_from_class"></a>

#### get_primary_asset_id_from_class

```python
@classmethod
def get_primary_asset_id_from_class(cls, class_: Class) -> PrimaryAssetId
```

X.get_primary_asset_id_from_class(class_) -> PrimaryAssetId
Returns the Primary Asset Id for a Class, this can return an invalid one if not registered

Args:
    class_ (type(Class)): 

Returns:
    PrimaryAssetId:

<a id="unreal.SystemLibrary.get_preferred_languages"></a>

#### get_preferred_languages

```python
@classmethod
def get_preferred_languages(cls) -> Array[str]
```

X.get_preferred_languages() -> Array[str]
Returns an array of the user's preferred languages in order of preference

Returns:
    Array[str]: An array of language IDs ordered from most preferred to least

<a id="unreal.SystemLibrary.get_platform_user_name"></a>

#### get_platform_user_name

```python
@classmethod
def get_platform_user_name(cls) -> str
```

X.get_platform_user_name() -> str
Get the current user name from the OS

Returns:
    str:

<a id="unreal.SystemLibrary.get_platform_user_dir"></a>

#### get_platform_user_dir

```python
@classmethod
def get_platform_user_dir(cls) -> str
```

X.get_platform_user_dir() -> str
Get the current user dir from the OS

Returns:
    str:

<a id="unreal.SystemLibrary.get_platform_time_seconds"></a>

#### get_platform_time_seconds

```python
@classmethod
def get_platform_time_seconds(cls) -> float
```

X.get_platform_time_seconds() -> double
Returns the current platform time in seconds. Not coupled to any gameplay or other containerization logic - this
function is useful for timing execution time or timestamping data. Marked as callable rather than pure because
implicit evaluation may be confusing, both for blueprint authors and blueprint readers. For implicit execution
simply wrap it in a blueprint pure function.

Returns:
    double:

<a id="unreal.SystemLibrary.get_path_name"></a>

#### get_path_name

```python
@classmethod
def get_path_name(cls, object: Object) -> str
```

X.get_path_name(object) -> str
Returns the full path to the specified object as a string

Args:
    object (Object): 

Returns:
    str:

<a id="unreal.SystemLibrary.get_outer_object"></a>

#### get_outer_object

```python
@classmethod
def get_outer_object(cls, object: Object) -> Object
```

X.get_outer_object(object) -> Object
Returns the outer object of an object.

Args:
    object (Object): 

Returns:
    Object:

<a id="unreal.SystemLibrary.get_object_name"></a>

#### get_object_name

```python
@classmethod
def get_object_name(cls, object: Object) -> str
```

X.get_object_name(object) -> str
Returns the actual object name.

Args:
    object (Object): 

Returns:
    str:

<a id="unreal.SystemLibrary.get_object_from_primary_asset_id"></a>

#### get_object_from_primary_asset_id

```python
@classmethod
def get_object_from_primary_asset_id(
        cls, primary_asset_id: PrimaryAssetId) -> Object
```

X.get_object_from_primary_asset_id(primary_asset_id) -> Object
Returns the Object associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

Args:
    primary_asset_id (PrimaryAssetId): 

Returns:
    Object:

<a id="unreal.SystemLibrary.get_min_y_resolution_for_ui"></a>

#### get_min_y_resolution_for_ui

```python
@classmethod
def get_min_y_resolution_for_ui(cls) -> int
```

X.get_min_y_resolution_for_ui() -> int32
Gets the smallest Y resolution we want to support in the UI, clamped within reasons

Returns:
    int32: value in pixels

<a id="unreal.SystemLibrary.get_min_y_resolution_for3d_view"></a>

#### get_min_y_resolution_for3d_view

```python
@classmethod
def get_min_y_resolution_for3d_view(cls) -> int
```

X.get_min_y_resolution_for3d_view() -> int32
Gets the smallest Y resolution we want to support in the 3D view, clamped within reasons

Returns:
    int32: value in pixels

<a id="unreal.SystemLibrary.get_local_currency_symbol"></a>

#### get_local_currency_symbol

```python
@classmethod
def get_local_currency_symbol(cls) -> str
```

X.get_local_currency_symbol() -> str
Returns the currency symbol associated with the device's locale

Returns:
    str: the currency symbol associated with the device's locale

<a id="unreal.SystemLibrary.get_local_currency_code"></a>

#### get_local_currency_code

```python
@classmethod
def get_local_currency_code(cls) -> str
```

X.get_local_currency_code() -> str
Returns the currency code associated with the device's locale

Returns:
    str: the currency code associated with the device's locale

<a id="unreal.SystemLibrary.get_game_time_in_seconds"></a>

#### get_game_time_in_seconds

```python
@classmethod
def get_game_time_in_seconds(cls, world_context_object: Object) -> float
```

X.get_game_time_in_seconds(world_context_object) -> double
Get the current game time, in seconds. This stops when the game is paused and is affected by slomo.

Args:
    world_context_object (Object): World context

Returns:
    double:

<a id="unreal.SystemLibrary.get_gamepad_controller_name"></a>

#### get_gamepad_controller_name

```python
@classmethod
def get_gamepad_controller_name(cls, controller_id: int) -> str
```

X.get_gamepad_controller_name(controller_id) -> str
Returns name of controller if assigned to a gamepad (or None if not assigned) (Android and iOS only)

Args:
    controller_id (int32): 

Returns:
    str:

<a id="unreal.SystemLibrary.get_gamepad_button_glyph"></a>

#### get_gamepad_button_glyph

```python
@classmethod
def get_gamepad_button_glyph(cls, button_key: str,
                             controller_index: int) -> Texture2D
```

X.get_gamepad_button_glyph(button_key, controller_index) -> Texture2D
Returns glyph assigned to a gamepad button (or a null ptr if not assigned) (iOS and tvOS only)

Args:
    button_key (str): 
    controller_index (int32): 

Returns:
    Texture2D:

<a id="unreal.SystemLibrary.get_game_name"></a>

#### get_game_name

```python
@classmethod
def get_game_name(cls) -> str
```

X.get_game_name() -> str
Get the name of the current game

Returns:
    str:

<a id="unreal.SystemLibrary.get_game_bundle_id"></a>

#### get_game_bundle_id

```python
@classmethod
def get_game_bundle_id(cls) -> str
```

X.get_game_bundle_id() -> str
Retrieves the game's platform-specific bundle identifier or package name of the game

Returns:
    str: The game's bundle identifier or package name.

<a id="unreal.SystemLibrary.get_frame_count"></a>

#### get_frame_count

```python
@classmethod
def get_frame_count(cls) -> int
```

X.get_frame_count() -> int64
Returns the value of GFrameCounter, a running count of the number of frames that have occurred.

Returns:
    int64:

<a id="unreal.SystemLibrary.get_enum_top_level_asset_path"></a>

#### get_enum_top_level_asset_path

```python
@classmethod
def get_enum_top_level_asset_path(cls, enum: Enum) -> TopLevelAssetPath
```

X.get_enum_top_level_asset_path(enum) -> TopLevelAssetPath
Returns the full path to the specified enum as a Top Level Asset Path used by asset utilities

Args:
    enum (Enum): 

Returns:
    TopLevelAssetPath:

<a id="unreal.SystemLibrary.get_engine_version"></a>

#### get_engine_version

```python
@classmethod
def get_engine_version(cls) -> str
```

X.get_engine_version() -> str
Engine build number, for displaying to end users.

Returns:
    str:

<a id="unreal.SystemLibrary.get_display_name"></a>

#### get_display_name

```python
@classmethod
def get_display_name(cls, object: Object) -> str
```

X.get_display_name(object) -> str
Returns the display name (or actor label), for displaying as a debugging aid.
Note: In editor builds, this is the actor label.  In non-editor builds, this is the actual object name.  This function should not be used to uniquely identify actors!
It is not localized and should not be used for display to an end user of a game.

Args:
    object (Object): 

Returns:
    str:

<a id="unreal.SystemLibrary.get_device_id"></a>

#### get_device_id

```python
@classmethod
def get_device_id(cls) -> str
```

X.get_device_id() -> str
Returns the platform specific unique device id

Returns:
    str:

<a id="unreal.SystemLibrary.get_default_locale"></a>

#### get_default_locale

```python
@classmethod
def get_default_locale(cls) -> str
```

X.get_default_locale() -> str
Get the default locale (for internationalization) used by this platform
note: This should be returned in IETF language tag form: - A two-letter ISO 639-1 language code (eg, "zh") - An optional four-letter ISO 15924 script code (eg, "Hans") - An optional two-letter ISO 3166-1 country code (eg, "CN")

Returns:
    str: The locale as an IETF language tag (eg, "zh-Hans-CN")

<a id="unreal.SystemLibrary.get_default_language"></a>

#### get_default_language

```python
@classmethod
def get_default_language(cls) -> str
```

X.get_default_language() -> str
Get the default language (for localization) used by this platform
note: This is typically the same as GetDefaultLocale unless the platform distinguishes between the two
note: This should be returned in IETF language tag form: - A two-letter ISO 639-1 language code (eg, "zh") - An optional four-letter ISO 15924 script code (eg, "Hans") - An optional two-letter ISO 3166-1 country code (eg, "CN")

Returns:
    str: The language as an IETF language tag (eg, "zh-Hans-CN")

<a id="unreal.SystemLibrary.get_current_bundle_state"></a>

#### get_current_bundle_state

```python
@classmethod
def get_current_bundle_state(
        cls, primary_asset_id: PrimaryAssetId,
        force_current_state: bool) -> Optional[Array[Name]]
```

X.get_current_bundle_state(primary_asset_id, force_current_state) -> Array[Name] or None
Returns the list of loaded bundles for a given Primary Asset. This will return false if the asset is not loaded at all.
If ForceCurrentState is true it will return the current state even if a load is in process

Args:
    primary_asset_id (PrimaryAssetId): 
    force_current_state (bool): 

Returns:
    Array[Name] or None: 

    out_bundles (Array[Name]):

<a id="unreal.SystemLibrary.get_convenient_windowed_resolutions"></a>

#### get_convenient_windowed_resolutions

```python
@classmethod
def get_convenient_windowed_resolutions(cls) -> Optional[Array[IntPoint]]
```

X.get_convenient_windowed_resolutions() -> Array[IntPoint] or None
Gets the list of windowed resolutions which are convenient for the current primary display size.

Returns:
    Array[IntPoint] or None: true if successfully queried the device for available resolutions.

    resolutions (Array[IntPoint]):

<a id="unreal.SystemLibrary.get_console_variable_string_value"></a>

#### get_console_variable_string_value

```python
@classmethod
def get_console_variable_string_value(cls, variable_name: str) -> str
```

X.get_console_variable_string_value(variable_name) -> str
Attempts to retrieve the value of the specified string console variable, if it exists.

Args:
    variable_name (str): Name of the console variable to find.

Returns:
    str: The value if found, empty string otherwise.

<a id="unreal.SystemLibrary.get_console_variable_int_value"></a>

#### get_console_variable_int_value

```python
@classmethod
def get_console_variable_int_value(cls, variable_name: str) -> int
```

X.get_console_variable_int_value(variable_name) -> int32
Attempts to retrieve the value of the specified integer console variable, if it exists.

Args:
    variable_name (str): Name of the console variable to find.

Returns:
    int32: The value if found, 0 otherwise.

<a id="unreal.SystemLibrary.get_console_variable_float_value"></a>

#### get_console_variable_float_value

```python
@classmethod
def get_console_variable_float_value(cls, variable_name: str) -> float
```

X.get_console_variable_float_value(variable_name) -> float
Attempts to retrieve the value of the specified float console variable, if it exists.

Args:
    variable_name (str): Name of the console variable to find.

Returns:
    float: The value if found, 0 otherwise.

<a id="unreal.SystemLibrary.get_console_variable_bool_value"></a>

#### get_console_variable_bool_value

```python
@classmethod
def get_console_variable_bool_value(cls, variable_name: str) -> bool
```

X.get_console_variable_bool_value(variable_name) -> bool
Evaluates, if it exists, whether the specified integer console variable has a non-zero value (true) or not (false).

Args:
    variable_name (str): Name of the console variable to find.

Returns:
    bool: True if found and has a non-zero value, false otherwise.

<a id="unreal.SystemLibrary.get_component_bounds"></a>

#### get_component_bounds

```python
@classmethod
def get_component_bounds(
        cls, component: SceneComponent) -> Tuple[Vector, Vector, float]
```

X.get_component_bounds(component) -> (origin=Vector, box_extent=Vector, sphere_radius=float)
Get bounds

Args:
    component (SceneComponent): 

Returns:
    tuple: 

    origin (Vector): 

    box_extent (Vector): 

    sphere_radius (float):

<a id="unreal.SystemLibrary.get_command_line"></a>

#### get_command_line

```python
@classmethod
def get_command_line(cls) -> str
```

X.get_command_line() -> str
Returns the command line that the process was launched with.

Returns:
    str:

<a id="unreal.SystemLibrary.get_class_top_level_asset_path"></a>

#### get_class_top_level_asset_path

```python
@classmethod
def get_class_top_level_asset_path(cls, class_: Class) -> TopLevelAssetPath
```

X.get_class_top_level_asset_path(class_) -> TopLevelAssetPath
Returns the full path to the specified class as a Top Level Asset Path used by asset utilities

Args:
    class_ (type(Class)): 

Returns:
    TopLevelAssetPath:

<a id="unreal.SystemLibrary.get_class_from_primary_asset_id"></a>

#### get_class_from_primary_asset_id

```python
@classmethod
def get_class_from_primary_asset_id(cls,
                                    primary_asset_id: PrimaryAssetId) -> Class
```

X.get_class_from_primary_asset_id(primary_asset_id) -> type(Class)
Returns the Blueprint Class associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

Args:
    primary_asset_id (PrimaryAssetId): 

Returns:
    type(Class):

<a id="unreal.SystemLibrary.get_class_display_name"></a>

#### get_class_display_name

```python
@classmethod
def get_class_display_name(cls, class_: Class) -> str
```

X.get_class_display_name(class_) -> str
Returns the display name of a class

Args:
    class_ (type(Class)): 

Returns:
    str:

<a id="unreal.SystemLibrary.get_build_version"></a>

#### get_build_version

```python
@classmethod
def get_build_version(cls) -> str
```

X.get_build_version() -> str
Build version, for displaying to end users in diagnostics.

Returns:
    str:

<a id="unreal.SystemLibrary.get_build_configuration"></a>

#### get_build_configuration

```python
@classmethod
def get_build_configuration(cls) -> str
```

X.get_build_configuration() -> str
Build configuration, for displaying to end users in diagnostics.

Returns:
    str:

<a id="unreal.SystemLibrary.get_ad_id_count"></a>

#### get_ad_id_count

```python
@classmethod
def get_ad_id_count(cls) -> int
```

X.get_ad_id_count() -> int32
Retrieves the total number of Ad IDs that can be selected between

Returns:
    int32:

<a id="unreal.SystemLibrary.get_actor_list_from_component_list"></a>

#### get_actor_list_from_component_list

```python
@classmethod
def get_actor_list_from_component_list(
        cls, component_list: Array[PrimitiveComponent],
        actor_class_filter: Class) -> Array[Actor]
```

X.get_actor_list_from_component_list(component_list, actor_class_filter) -> Array[Actor]
Returns an array of unique actors represented by the given list of components.

Args:
    component_list (Array[PrimitiveComponent]): List of components.
    actor_class_filter (type(Class)): 

Returns:
    Array[Actor]: 

    out_actor_list (Array[Actor]): Start of line segment.

<a id="unreal.SystemLibrary.get_actor_bounds"></a>

#### get_actor_bounds

```python
@classmethod
def get_actor_bounds(cls, actor: Actor) -> Tuple[Vector, Vector]
```

X.get_actor_bounds(actor) -> (origin=Vector, box_extent=Vector)
Get Actor Bounds
deprecated: Function 'GetActorBounds' is deprecated.

Args:
    actor (Actor): 

Returns:
    tuple: 

    origin (Vector): 

    box_extent (Vector):

<a id="unreal.SystemLibrary.force_close_ad_banner"></a>

#### force_close_ad_banner

```python
@classmethod
def force_close_ad_banner(cls) -> None
```

X.force_close_ad_banner() -> None
Forces closed any displayed ad. Can lead to loss of revenue
(iOS and Android only)

<a id="unreal.SystemLibrary.experimental_close_ad_banner"></a>

#### experimental_close_ad_banner

```python
@classmethod
def experimental_close_ad_banner(cls) -> None
```

deprecated: 'experimental_close_ad_banner' was renamed to 'force_close_ad_banner'.

<a id="unreal.SystemLibrary.flush_persistent_debug_lines"></a>

#### flush_persistent_debug_lines

```python
@classmethod
def flush_persistent_debug_lines(cls, world_context_object: Object) -> None
```

X.flush_persistent_debug_lines(world_context_object) -> None
Flush all persistent debug lines and shapes.

Args:
    world_context_object (Object):

<a id="unreal.SystemLibrary.flush_debug_strings"></a>

#### flush_debug_strings

```python
@classmethod
def flush_debug_strings(cls, world_context_object: Object) -> None
```

X.flush_debug_strings(world_context_object) -> None
Removes all debug strings.

Args:
    world_context_object (Object):

<a id="unreal.SystemLibrary.execute_console_command"></a>

#### execute_console_command

```python
@classmethod
def execute_console_command(cls,
                            world_context_object: Object,
                            command: str,
                            specific_player: PlayerController = None) -> None
```

X.execute_console_command(world_context_object, command, specific_player=None) -> None
Executes a console command, optionally on a specific controller

Args:
    world_context_object (Object): 
    command (str): Command to send to the console
    specific_player (PlayerController): If specified, the console command will be routed through the specified player

<a id="unreal.SystemLibrary.equal_equal_soft_object_reference"></a>

#### equal_equal_soft_object_reference

```python
@classmethod
def equal_equal_soft_object_reference(cls, a: Object, b: Object) -> bool
```

X.equal_equal_soft_object_reference(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (Object): 
    b (Object): 

Returns:
    bool:

<a id="unreal.SystemLibrary.equal_equal_soft_class_reference"></a>

#### equal_equal_soft_class_reference

```python
@classmethod
def equal_equal_soft_class_reference(cls, a: Class, b: Class) -> bool
```

X.equal_equal_soft_class_reference(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (Class): 
    b (Class): 

Returns:
    bool:

<a id="unreal.SystemLibrary.equal_equal_primary_asset_type"></a>

#### equal_equal_primary_asset_type

```python
@classmethod
def equal_equal_primary_asset_type(cls, a: PrimaryAssetType,
                                   b: PrimaryAssetType) -> bool
```

X.equal_equal_primary_asset_type(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (PrimaryAssetType): 
    b (PrimaryAssetType): 

Returns:
    bool:

<a id="unreal.SystemLibrary.equal_equal_primary_asset_id"></a>

#### equal_equal_primary_asset_id

```python
@classmethod
def equal_equal_primary_asset_id(cls, a: PrimaryAssetId,
                                 b: PrimaryAssetId) -> bool
```

X.equal_equal_primary_asset_id(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (PrimaryAssetId): 
    b (PrimaryAssetId): 

Returns:
    bool:

<a id="unreal.SystemLibrary.end_transaction"></a>

#### end_transaction

```python
@classmethod
def end_transaction(cls) -> int
```

X.end_transaction() -> int32
Attempt to end the current undo transaction. Only successful if the transaction's action counter is 1.
note: Only available in the editor.

Returns:
    int32: The number of active actions when EndTransaction was called (a value of 1 indicates that the transaction was successfully closed), or -1 on failure.

<a id="unreal.SystemLibrary.draw_debug_string"></a>

#### draw_debug_string

```python
@classmethod
def draw_debug_string(cls,
                      world_context_object: Object,
                      text_location: Vector,
                      text: str,
                      test_base_actor: Actor = None,
                      text_color: LinearColor = [
                          1.000000, 1.000000, 1.000000, 1.000000
                      ],
                      duration: float = 0.000000) -> None
```

X.draw_debug_string(world_context_object, text_location, text, test_base_actor=None, text_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000) -> None
Draw a debug string at a 3d world location.

Args:
    world_context_object (Object): 
    text_location (Vector): 
    text (str): 
    test_base_actor (Actor): 
    text_color (LinearColor): 
    duration (float):

<a id="unreal.SystemLibrary.draw_debug_sphere"></a>

#### draw_debug_sphere

```python
@classmethod
def draw_debug_sphere(cls,
                      world_context_object: Object,
                      center: Vector,
                      radius: float = 100.000000,
                      segments: int = 12,
                      line_color: LinearColor = [
                          1.000000, 1.000000, 1.000000, 1.000000
                      ],
                      duration: float = 0.000000,
                      thickness: float = 0.000000) -> None
```

X.draw_debug_sphere(world_context_object, center, radius=100.000000, segments=12, line_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000, thickness=0.000000) -> None
Draw a debug sphere

Args:
    world_context_object (Object): 
    center (Vector): 
    radius (float): 
    segments (int32): 
    line_color (LinearColor): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_point"></a>

#### draw_debug_point

```python
@classmethod
def draw_debug_point(cls,
                     world_context_object: Object,
                     position: Vector,
                     size: float,
                     point_color: LinearColor,
                     duration: float = 0.000000) -> None
```

X.draw_debug_point(world_context_object, position, size, point_color, duration=0.000000) -> None
Draw a debug point

Args:
    world_context_object (Object): 
    position (Vector): 
    size (float): 
    point_color (LinearColor): 
    duration (float):

<a id="unreal.SystemLibrary.draw_debug_plane"></a>

#### draw_debug_plane

```python
@classmethod
def draw_debug_plane(cls,
                     world_context_object: Object,
                     plane_coordinates: Plane,
                     location: Vector,
                     size: float,
                     plane_color: LinearColor = [
                         1.000000, 1.000000, 1.000000, 1.000000
                     ],
                     duration: float = 0.000000) -> None
```

X.draw_debug_plane(world_context_object, plane_coordinates, location, size, plane_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000) -> None
Draws a debug plane.

Args:
    world_context_object (Object): 
    plane_coordinates (Plane): 
    location (Vector): 
    size (float): 
    plane_color (LinearColor): 
    duration (float):

<a id="unreal.SystemLibrary.draw_debug_line"></a>

#### draw_debug_line

```python
@classmethod
def draw_debug_line(cls,
                    world_context_object: Object,
                    line_start: Vector,
                    line_end: Vector,
                    line_color: LinearColor,
                    duration: float = 0.000000,
                    thickness: float = 0.000000) -> None
```

X.draw_debug_line(world_context_object, line_start, line_end, line_color, duration=0.000000, thickness=0.000000) -> None
Draw a debug line

Args:
    world_context_object (Object): 
    line_start (Vector): 
    line_end (Vector): 
    line_color (LinearColor): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_frustum"></a>

#### draw_debug_frustum

```python
@classmethod
def draw_debug_frustum(cls,
                       world_context_object: Object,
                       frustum_transform: Transform,
                       frustum_color: LinearColor = [
                           1.000000, 1.000000, 1.000000, 1.000000
                       ],
                       duration: float = 0.000000,
                       thickness: float = 0.000000) -> None
```

X.draw_debug_frustum(world_context_object, frustum_transform, frustum_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000, thickness=0.000000) -> None
Draws a debug frustum.

Args:
    world_context_object (Object): 
    frustum_transform (Transform): 
    frustum_color (LinearColor): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_float_history_transform"></a>

#### draw_debug_float_history_transform

```python
@classmethod
def draw_debug_float_history_transform(cls,
                                       world_context_object: Object,
                                       float_history: DebugFloatHistory,
                                       draw_transform: Transform,
                                       draw_size: Vector2D,
                                       draw_color: LinearColor = [
                                           1.000000, 1.000000, 1.000000,
                                           1.000000
                                       ],
                                       duration: float = 0.000000) -> None
```

X.draw_debug_float_history_transform(world_context_object, float_history, draw_transform, draw_size, draw_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000) -> None
Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawTransform for the position in the world.

Args:
    world_context_object (Object): 
    float_history (DebugFloatHistory): 
    draw_transform (Transform): 
    draw_size (Vector2D): 
    draw_color (LinearColor): 
    duration (float):

<a id="unreal.SystemLibrary.draw_debug_float_history_location"></a>

#### draw_debug_float_history_location

```python
@classmethod
def draw_debug_float_history_location(cls,
                                      world_context_object: Object,
                                      float_history: DebugFloatHistory,
                                      draw_location: Vector,
                                      draw_size: Vector2D,
                                      draw_color: LinearColor = [
                                          1.000000, 1.000000, 1.000000,
                                          1.000000
                                      ],
                                      duration: float = 0.000000) -> None
```

X.draw_debug_float_history_location(world_context_object, float_history, draw_location, draw_size, draw_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000) -> None
Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawLocation for the location in the world, rotation will face camera of first player.

Args:
    world_context_object (Object): 
    float_history (DebugFloatHistory): 
    draw_location (Vector): 
    draw_size (Vector2D): 
    draw_color (LinearColor): 
    duration (float):

<a id="unreal.SystemLibrary.draw_debug_cylinder"></a>

#### draw_debug_cylinder

```python
@classmethod
def draw_debug_cylinder(cls,
                        world_context_object: Object,
                        start: Vector,
                        end: Vector,
                        radius: float = 100.000000,
                        segments: int = 12,
                        line_color: LinearColor = [
                            1.000000, 1.000000, 1.000000, 1.000000
                        ],
                        duration: float = 0.000000,
                        thickness: float = 0.000000) -> None
```

X.draw_debug_cylinder(world_context_object, start, end, radius=100.000000, segments=12, line_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000, thickness=0.000000) -> None
Draw a debug cylinder

Args:
    world_context_object (Object): 
    start (Vector): 
    end (Vector): 
    radius (float): 
    segments (int32): 
    line_color (LinearColor): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_coordinate_system"></a>

#### draw_debug_coordinate_system

```python
@classmethod
def draw_debug_coordinate_system(cls,
                                 world_context_object: Object,
                                 axis_loc: Vector,
                                 axis_rot: Rotator,
                                 scale: float = 1.000000,
                                 duration: float = 0.000000,
                                 thickness: float = 0.000000) -> None
```

X.draw_debug_coordinate_system(world_context_object, axis_loc, axis_rot, scale=1.000000, duration=0.000000, thickness=0.000000) -> None
Draw a debug coordinate system.

Args:
    world_context_object (Object): 
    axis_loc (Vector): 
    axis_rot (Rotator): 
    scale (float): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_cone_in_degrees"></a>

#### draw_debug_cone_in_degrees

```python
@classmethod
def draw_debug_cone_in_degrees(cls,
                               world_context_object: Object,
                               origin: Vector,
                               direction: Vector,
                               length: float = 100.000000,
                               angle_width: float = 45.000000,
                               angle_height: float = 45.000000,
                               num_sides: int = 12,
                               line_color: LinearColor = [
                                   1.000000, 1.000000, 1.000000, 1.000000
                               ],
                               duration: float = 0.000000,
                               thickness: float = 0.000000) -> None
```

X.draw_debug_cone_in_degrees(world_context_object, origin, direction, length=100.000000, angle_width=45.000000, angle_height=45.000000, num_sides=12, line_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000, thickness=0.000000) -> None
Draw a debug cone
Angles are specified in degrees

Args:
    world_context_object (Object): 
    origin (Vector): 
    direction (Vector): 
    length (float): 
    angle_width (float): 
    angle_height (float): 
    num_sides (int32): 
    line_color (LinearColor): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_cone"></a>

#### draw_debug_cone

```python
@classmethod
def draw_debug_cone(cls,
                    world_context_object: Object,
                    origin: Vector,
                    direction: Vector,
                    length: float,
                    angle_width: float,
                    angle_height: float,
                    num_sides: int,
                    line_color: LinearColor,
                    duration: float = 0.000000,
                    thickness: float = 0.000000) -> None
```

X.draw_debug_cone(world_context_object, origin, direction, length, angle_width, angle_height, num_sides, line_color, duration=0.000000, thickness=0.000000) -> None
Draw a debug cone
deprecated: DrawDebugCone has been changed to use degrees for angles instead of radians. Place a new DrawDebugCone node and pass your angles as degrees.

Args:
    world_context_object (Object): 
    origin (Vector): 
    direction (Vector): 
    length (float): 
    angle_width (float): 
    angle_height (float): 
    num_sides (int32): 
    line_color (LinearColor): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_circle"></a>

#### draw_debug_circle

```python
@classmethod
def draw_debug_circle(cls,
                      world_context_object: Object,
                      center: Vector,
                      radius: float,
                      num_segments: int = 12,
                      line_color: LinearColor = [
                          1.000000, 1.000000, 1.000000, 1.000000
                      ],
                      duration: float = 0.000000,
                      thickness: float = 0.000000,
                      y_axis: Vector = [0.000000, 1.000000, 0.000000],
                      z_axis: Vector = [0.000000, 0.000000, 1.000000],
                      draw_axis: bool = False) -> None
```

X.draw_debug_circle(world_context_object, center, radius, num_segments=12, line_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000, thickness=0.000000, y_axis=[0.000000, 1.000000, 0.000000], z_axis=[0.000000, 0.000000, 1.000000], draw_axis=False) -> None
Draw a debug circle!

Args:
    world_context_object (Object): 
    center (Vector): 
    radius (float): 
    num_segments (int32): 
    line_color (LinearColor): 
    duration (float): 
    thickness (float): 
    y_axis (Vector): 
    z_axis (Vector): 
    draw_axis (bool):

<a id="unreal.SystemLibrary.draw_debug_capsule"></a>

#### draw_debug_capsule

```python
@classmethod
def draw_debug_capsule(cls,
                       world_context_object: Object,
                       center: Vector,
                       half_height: float,
                       radius: float,
                       rotation: Rotator,
                       line_color: LinearColor = [
                           1.000000, 1.000000, 1.000000, 1.000000
                       ],
                       duration: float = 0.000000,
                       thickness: float = 0.000000) -> None
```

X.draw_debug_capsule(world_context_object, center, half_height, radius, rotation, line_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000, thickness=0.000000) -> None
Draw a debug capsule

Args:
    world_context_object (Object): 
    center (Vector): 
    half_height (float): 
    radius (float): 
    rotation (Rotator): 
    line_color (LinearColor): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_camera"></a>

#### draw_debug_camera

```python
@classmethod
def draw_debug_camera(cls,
                      camera_actor: CameraActor,
                      camera_color: LinearColor = [
                          1.000000, 1.000000, 1.000000, 1.000000
                      ],
                      duration: float = 0.000000) -> None
```

X.draw_debug_camera(camera_actor, camera_color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000) -> None
Draw a debug camera shape.

Args:
    camera_actor (CameraActor): 
    camera_color (LinearColor): 
    duration (float):

<a id="unreal.SystemLibrary.draw_debug_box"></a>

#### draw_debug_box

```python
@classmethod
def draw_debug_box(cls,
                   world_context_object: Object,
                   center: Vector,
                   extent: Vector,
                   line_color: LinearColor,
                   rotation: Rotator = [0.000000, 0.000000, 0.000000],
                   duration: float = 0.000000,
                   thickness: float = 0.000000) -> None
```

X.draw_debug_box(world_context_object, center, extent, line_color, rotation=[0.000000, 0.000000, 0.000000], duration=0.000000, thickness=0.000000) -> None
Draw a debug box

Args:
    world_context_object (Object): 
    center (Vector): 
    extent (Vector): 
    line_color (LinearColor): 
    rotation (Rotator): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.draw_debug_arrow"></a>

#### draw_debug_arrow

```python
@classmethod
def draw_debug_arrow(cls,
                     world_context_object: Object,
                     line_start: Vector,
                     line_end: Vector,
                     arrow_size: float,
                     line_color: LinearColor,
                     duration: float = 0.000000,
                     thickness: float = 0.000000) -> None
```

X.draw_debug_arrow(world_context_object, line_start, line_end, arrow_size, line_color, duration=0.000000, thickness=0.000000) -> None
Draw directional arrow, pointing from LineStart to LineEnd.

Args:
    world_context_object (Object): 
    line_start (Vector): 
    line_end (Vector): 
    arrow_size (float): 
    line_color (LinearColor): 
    duration (float): 
    thickness (float):

<a id="unreal.SystemLibrary.does_implement_interface"></a>

#### does_implement_interface

```python
@classmethod
def does_implement_interface(cls, test_object: Object,
                             interface: Class) -> bool
```

X.does_implement_interface(test_object, interface) -> bool
Checks if the given object implements a specific interface, works for both native and blueprint interfacse

Args:
    test_object (Object): 
    interface (type(Class)): 

Returns:
    bool:

<a id="unreal.SystemLibrary.does_class_implement_interface"></a>

#### does_class_implement_interface

```python
@classmethod
def does_class_implement_interface(cls, test_class: Class,
                                   interface: Class) -> bool
```

X.does_class_implement_interface(test_class, interface) -> bool
Checks if the given class implements a specific interface, works for both native and blueprint interfacse

Args:
    test_class (type(Class)): 
    interface (type(Class)): 

Returns:
    bool:

<a id="unreal.SystemLibrary.delay_until_next_tick"></a>

#### delay_until_next_tick

```python
@classmethod
def delay_until_next_tick(cls, world_context_object: Object,
                          latent_info: LatentActionInfo) -> None
```

X.delay_until_next_tick(world_context_object, latent_info) -> None
Perform a latent action with a delay of one tick.  Calling again while it is counting down will be ignored.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.SystemLibrary.delay"></a>

#### delay

```python
@classmethod
def delay(cls,
          world_context_object: Object,
          duration: float = 0.200000,
          latent_info: LatentActionInfo = ...) -> None
```

X.delay(world_context_object, duration=0.200000, latent_info) -> None
Perform a latent action with a delay (specified in seconds).  Calling again while it is counting down will be ignored.

Args:
    world_context_object (Object): 
    duration (float): length of delay (in seconds).
    latent_info (LatentActionInfo): The latent action.

<a id="unreal.SystemLibrary.create_copy_for_undo_buffer"></a>

#### create_copy_for_undo_buffer

```python
@classmethod
def create_copy_for_undo_buffer(cls, object_to_modify: Object) -> None
```

X.create_copy_for_undo_buffer(object_to_modify) -> None
Mark as modified.

Args:
    object_to_modify (Object):

<a id="unreal.SystemLibrary.convert_to_relative_path"></a>

#### convert_to_relative_path

```python
@classmethod
def convert_to_relative_path(cls, filename: str) -> str
```

X.convert_to_relative_path(filename) -> str
Converts passed in filename to use a relative path

Args:
    filename (str): 

Returns:
    str:

<a id="unreal.SystemLibrary.convert_to_absolute_path"></a>

#### convert_to_absolute_path

```python
@classmethod
def convert_to_absolute_path(cls, filename: str) -> str
```

X.convert_to_absolute_path(filename) -> str
Converts passed in filename to use a absolute path

Args:
    filename (str): 

Returns:
    str:

<a id="unreal.SystemLibrary.conv_soft_obj_ref_to_soft_obj_path"></a>

#### conv_soft_obj_ref_to_soft_obj_path

```python
@classmethod
def conv_soft_obj_ref_to_soft_obj_path(
        cls, soft_object_reference: Object) -> SoftObjectPath
```

X.conv_soft_obj_ref_to_soft_obj_path(soft_object_reference) -> SoftObjectPath
Converts a Soft Object Reference into a Soft Object Path

Args:
    soft_object_reference (Object): 

Returns:
    SoftObjectPath:

<a id="unreal.SystemLibrary.conv_soft_obj_ref_to_soft_class_path"></a>

#### conv_soft_obj_ref_to_soft_class_path

```python
@classmethod
def conv_soft_obj_ref_to_soft_class_path(
        cls, soft_class_reference: Class) -> SoftClassPath
```

X.conv_soft_obj_ref_to_soft_class_path(soft_class_reference) -> SoftClassPath
Converts a Soft Class Reference into a Soft Class Path (which can be used like a Soft Object Path)

Args:
    soft_class_reference (Class): 

Returns:
    SoftClassPath:

<a id="unreal.SystemLibrary.conv_soft_obj_path_to_soft_obj_ref"></a>

#### conv_soft_obj_path_to_soft_obj_ref

```python
@classmethod
def conv_soft_obj_path_to_soft_obj_ref(
        cls, soft_object_path: SoftObjectPath) -> Object
```

X.conv_soft_obj_path_to_soft_obj_ref(soft_object_path) -> Object
Converts a Soft Object Path into a base Soft Object Reference, this is not guaranteed to be resolvable

Args:
    soft_object_path (SoftObjectPath): 

Returns:
    Object:

<a id="unreal.SystemLibrary.conv_soft_object_reference_to_string"></a>

#### conv_soft_object_reference_to_string

```python
@classmethod
def conv_soft_object_reference_to_string(cls,
                                         soft_object_reference: Object) -> str
```

X.conv_soft_object_reference_to_string(soft_object_reference) -> str
Converts a Soft Object Reference to a path string

Args:
    soft_object_reference (Object): 

Returns:
    str:

<a id="unreal.SystemLibrary.conv_soft_class_reference_to_string"></a>

#### conv_soft_class_reference_to_string

```python
@classmethod
def conv_soft_class_reference_to_string(cls,
                                        soft_class_reference: Class) -> str
```

X.conv_soft_class_reference_to_string(soft_class_reference) -> str
Converts a Soft Class Reference to a path string

Args:
    soft_class_reference (Class): 

Returns:
    str:

<a id="unreal.SystemLibrary.conv_soft_class_path_to_soft_class_ref"></a>

#### conv_soft_class_path_to_soft_class_ref

```python
@classmethod
def conv_soft_class_path_to_soft_class_ref(
        cls, soft_class_path: SoftClassPath) -> Class
```

X.conv_soft_class_path_to_soft_class_ref(soft_class_path) -> Class
Converts a Soft Class Path into a base Soft Class Reference, this is not guaranteed to be resolvable

Args:
    soft_class_path (SoftClassPath): 

Returns:
    Class:

<a id="unreal.SystemLibrary.conv_primary_asset_type_to_string"></a>

#### conv_primary_asset_type_to_string

```python
@classmethod
def conv_primary_asset_type_to_string(
        cls, primary_asset_type: PrimaryAssetType) -> str
```

X.conv_primary_asset_type_to_string(primary_asset_type) -> str
Converts a Primary Asset Type to a string. The other direction is not provided because it cannot be validated

Args:
    primary_asset_type (PrimaryAssetType): 

Returns:
    str:

<a id="unreal.SystemLibrary.conv_primary_asset_id_to_string"></a>

#### conv_primary_asset_id_to_string

```python
@classmethod
def conv_primary_asset_id_to_string(cls,
                                    primary_asset_id: PrimaryAssetId) -> str
```

X.conv_primary_asset_id_to_string(primary_asset_id) -> str
Converts a Primary Asset Id to a string. The other direction is not provided because it cannot be validated

Args:
    primary_asset_id (PrimaryAssetId): 

Returns:
    str:

<a id="unreal.SystemLibrary.conv_object_to_class"></a>

#### conv_object_to_class

```python
@classmethod
def conv_object_to_class(cls, object: Object, class_: Class) -> Class
```

X.conv_object_to_class(object, class_) -> type(Class)
Casts from an object to a class, this will only work if the object is already a class

Args:
    object (Object): 
    class_ (type(Class)): 

Returns:
    type(Class):

<a id="unreal.SystemLibrary.conv_interface_to_object"></a>

#### conv_interface_to_object

```python
@classmethod
def conv_interface_to_object(cls, interface: Interface) -> Object
```

X.conv_interface_to_object(interface) -> Object
Converts an interface instance into an object

Args:
    interface (Interface): 

Returns:
    Object:

<a id="unreal.SystemLibrary.conv_component_reference_to_soft_component_reference"></a>

#### conv_component_reference_to_soft_component_reference

```python
@classmethod
def conv_component_reference_to_soft_component_reference(
        cls,
        component_reference: ComponentReference) -> SoftComponentReference
```

X.conv_component_reference_to_soft_component_reference(component_reference) -> SoftComponentReference
Conv Component Reference to Soft Component Reference

Args:
    component_reference (ComponentReference): 

Returns:
    SoftComponentReference:

<a id="unreal.SystemLibrary.control_screensaver"></a>

#### control_screensaver

```python
@classmethod
def control_screensaver(cls, allow_screen_saver: bool) -> None
```

X.control_screensaver(allow_screen_saver) -> None
Allows or inhibits screensaver

Args:
    allow_screen_saver (bool): If false, don't allow screensaver if possible, otherwise allow default behavior

<a id="unreal.SystemLibrary.component_overlap_components"></a>

#### component_overlap_components

```python
@classmethod
def component_overlap_components(
        cls, component: PrimitiveComponent, component_transform: Transform,
        object_types: Array[ObjectTypeQuery], component_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[PrimitiveComponent]]
```

X.component_overlap_components(component, component_transform, object_types, component_class_filter, actors_to_ignore) -> Array[PrimitiveComponent] or None
Returns an array of components that overlap the given component.

Args:
    component (PrimitiveComponent): Component to test with.
    component_transform (Transform): Defines where to place the component for overlap testing.
    object_types (Array[ObjectTypeQuery]): 
    component_class_filter (type(Class)): 
    actors_to_ignore (Array[Actor]): Ignore these actors in the list

Returns:
    Array[PrimitiveComponent] or None: true if there was an overlap that passed the filters, false otherwise.

    out_components (Array[PrimitiveComponent]):

<a id="unreal.SystemLibrary.component_overlap_components_new"></a>

#### component_overlap_components_new

```python
@classmethod
def component_overlap_components_new(
        cls, component: PrimitiveComponent, component_transform: Transform,
        object_types: Array[ObjectTypeQuery], component_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[PrimitiveComponent]]
```

deprecated: 'component_overlap_components_new' was renamed to 'component_overlap_components'.

<a id="unreal.SystemLibrary.component_overlap_actors"></a>

#### component_overlap_actors

```python
@classmethod
def component_overlap_actors(
        cls, component: PrimitiveComponent, component_transform: Transform,
        object_types: Array[ObjectTypeQuery], actor_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[Actor]]
```

X.component_overlap_actors(component, component_transform, object_types, actor_class_filter, actors_to_ignore) -> Array[Actor] or None
Returns an array of actors that overlap the given component.

Args:
    component (PrimitiveComponent): Component to test with.
    component_transform (Transform): Defines where to place the component for overlap testing.
    object_types (Array[ObjectTypeQuery]): 
    actor_class_filter (type(Class)): 
    actors_to_ignore (Array[Actor]): Ignore these actors in the list

Returns:
    Array[Actor] or None: true if there was an overlap that passed the filters, false otherwise.

    out_actors (Array[Actor]): Returned array of actors. Unsorted.

<a id="unreal.SystemLibrary.component_overlap_actors_new"></a>

#### component_overlap_actors_new

```python
@classmethod
def component_overlap_actors_new(
        cls, component: PrimitiveComponent, component_transform: Transform,
        object_types: Array[ObjectTypeQuery], actor_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[Actor]]
```

deprecated: 'component_overlap_actors_new' was renamed to 'component_overlap_actors'.

<a id="unreal.SystemLibrary.collect_garbage"></a>

#### collect_garbage

```python
@classmethod
def collect_garbage(cls) -> None
```

X.collect_garbage() -> None
Deletes all unreferenced objects, keeping only referenced objects (this command will be queued and happen at the end of the frame)
Note: This can be a slow operation, and should only be performed where a hitch would be acceptable

<a id="unreal.SystemLibrary.capsule_trace_single_for_objects"></a>

#### capsule_trace_single_for_objects

```python
@classmethod
def capsule_trace_single_for_objects(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        half_height: float,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.capsule_trace_single_for_objects(world_context_object, start, end, radius, half_height, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweeps a capsule along the given line and returns the first hit encountered.
This only finds objects that are of a type specified by ObjectTypes.

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the capsule to sweep
    half_height (float): Distance from center of capsule to tip of hemisphere endcap.
    object_types (Array[ObjectTypeQuery]): Array of Object Types to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.capsule_trace_single_by_profile"></a>

#### capsule_trace_single_by_profile

```python
@classmethod
def capsule_trace_single_by_profile(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        half_height: float,
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.capsule_trace_single_by_profile(world_context_object, start, end, radius, half_height, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweep a capsule against the world and return the first blocking hit using a specific profile

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the capsule to sweep
    half_height (float): Distance from center of capsule to tip of hemisphere endcap.
    profile_name (Name): The 'profile' used to determine which components to hit
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.capsule_trace_single"></a>

#### capsule_trace_single

```python
@classmethod
def capsule_trace_single(cls,
                         world_context_object: Object,
                         start: Vector,
                         end: Vector,
                         radius: float,
                         half_height: float,
                         trace_channel: TraceTypeQuery,
                         trace_complex: bool,
                         actors_to_ignore: Array[Actor],
                         draw_debug_type: DrawDebugTrace,
                         ignore_self: bool = True,
                         trace_color: LinearColor = [
                             1.000000, 0.000000, 0.000000, 1.000000
                         ],
                         trace_hit_color: LinearColor = [
                             0.000000, 1.000000, 0.000000, 1.000000
                         ],
                         draw_time: float = 5.000000) -> Optional[HitResult]
```

X.capsule_trace_single(world_context_object, start, end, radius, half_height, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweeps a capsule along the given line and returns the first blocking hit encountered.
This trace finds the objects that RESPOND to the given TraceChannel

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the capsule to sweep
    half_height (float): Distance from center of capsule to tip of hemisphere endcap.
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.capsule_trace_single_new"></a>

#### capsule_trace_single_new

```python
@classmethod
def capsule_trace_single_new(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        half_height: float,
        trace_channel: TraceTypeQuery,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

deprecated: 'capsule_trace_single_new' was renamed to 'capsule_trace_single'.

<a id="unreal.SystemLibrary.capsule_trace_multi_for_objects"></a>

#### capsule_trace_multi_for_objects

```python
@classmethod
def capsule_trace_multi_for_objects(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        half_height: float,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.capsule_trace_multi_for_objects(world_context_object, start, end, radius, half_height, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweeps a capsule along the given line and returns all hits encountered.
This only finds objects that are of a type specified by ObjectTypes.

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the capsule to sweep
    half_height (float): Distance from center of capsule to tip of hemisphere endcap.
    object_types (Array[ObjectTypeQuery]): Array of Object Types to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.capsule_trace_multi_by_profile"></a>

#### capsule_trace_multi_by_profile

```python
@classmethod
def capsule_trace_multi_by_profile(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        half_height: float,
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.capsule_trace_multi_by_profile(world_context_object, start, end, radius, half_height, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweep a capsule against the world and return all initial overlaps using a specific profile, then overlapping hits and then first blocking hit
Results are sorted, so a blocking hit (if found) will be the last element of the array
Only the single closest blocking result will be generated, no tests will be done after that

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the capsule to sweep
    half_height (float): Distance from center of capsule to tip of hemisphere endcap.
    profile_name (Name): The 'profile' used to determine which components to hit
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a blocking hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.capsule_trace_multi"></a>

#### capsule_trace_multi

```python
@classmethod
def capsule_trace_multi(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        half_height: float,
        trace_channel: TraceTypeQuery,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.capsule_trace_multi(world_context_object, start, end, radius, half_height, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweeps a capsule along the given line and returns all hits encountered up to and including the first blocking hit.
This trace finds the objects that RESPOND to the given TraceChannel

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    radius (float): Radius of the capsule to sweep
    half_height (float): Distance from center of capsule to tip of hemisphere endcap.
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a blocking hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.capsule_trace_multi_new"></a>

#### capsule_trace_multi_new

```python
@classmethod
def capsule_trace_multi_new(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        radius: float,
        half_height: float,
        trace_channel: TraceTypeQuery,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

deprecated: 'capsule_trace_multi_new' was renamed to 'capsule_trace_multi'.

<a id="unreal.SystemLibrary.capsule_overlap_components"></a>

#### capsule_overlap_components

```python
@classmethod
def capsule_overlap_components(
        cls, world_context_object: Object, capsule_pos: Vector, radius: float,
        half_height: float, object_types: Array[ObjectTypeQuery],
        component_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[PrimitiveComponent]]
```

X.capsule_overlap_components(world_context_object, capsule_pos, radius, half_height, object_types, component_class_filter, actors_to_ignore) -> Array[PrimitiveComponent] or None
Returns an array of components that overlap the given capsule.

Args:
    world_context_object (Object): 
    capsule_pos (Vector): Center of the capsule.
    radius (float): Radius of capsule hemispheres and radius of center cylinder portion.
    half_height (float): Half-height of the capsule (from center of capsule to tip of hemisphere.
    object_types (Array[ObjectTypeQuery]): 
    component_class_filter (type(Class)): 
    actors_to_ignore (Array[Actor]): Ignore these actors in the list

Returns:
    Array[PrimitiveComponent] or None: true if there was an overlap that passed the filters, false otherwise.

    out_components (Array[PrimitiveComponent]):

<a id="unreal.SystemLibrary.capsule_overlap_components_new"></a>

#### capsule_overlap_components_new

```python
@classmethod
def capsule_overlap_components_new(
        cls, world_context_object: Object, capsule_pos: Vector, radius: float,
        half_height: float, object_types: Array[ObjectTypeQuery],
        component_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[PrimitiveComponent]]
```

deprecated: 'capsule_overlap_components_new' was renamed to 'capsule_overlap_components'.

<a id="unreal.SystemLibrary.capsule_overlap_actors"></a>

#### capsule_overlap_actors

```python
@classmethod
def capsule_overlap_actors(
        cls, world_context_object: Object, capsule_pos: Vector, radius: float,
        half_height: float, object_types: Array[ObjectTypeQuery],
        actor_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[Actor]]
```

X.capsule_overlap_actors(world_context_object, capsule_pos, radius, half_height, object_types, actor_class_filter, actors_to_ignore) -> Array[Actor] or None
Returns an array of actors that overlap the given capsule.

Args:
    world_context_object (Object): 
    capsule_pos (Vector): Center of the capsule.
    radius (float): Radius of capsule hemispheres and radius of center cylinder portion.
    half_height (float): Half-height of the capsule (from center of capsule to tip of hemisphere.
    object_types (Array[ObjectTypeQuery]): 
    actor_class_filter (type(Class)): 
    actors_to_ignore (Array[Actor]): Ignore these actors in the list

Returns:
    Array[Actor] or None: true if there was an overlap that passed the filters, false otherwise.

    out_actors (Array[Actor]): Returned array of actors. Unsorted.

<a id="unreal.SystemLibrary.capsule_overlap_actors_new"></a>

#### capsule_overlap_actors_new

```python
@classmethod
def capsule_overlap_actors_new(
        cls, world_context_object: Object, capsule_pos: Vector, radius: float,
        half_height: float, object_types: Array[ObjectTypeQuery],
        actor_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[Actor]]
```

deprecated: 'capsule_overlap_actors_new' was renamed to 'capsule_overlap_actors'.

<a id="unreal.SystemLibrary.can_launch_url"></a>

#### can_launch_url

```python
@classmethod
def can_launch_url(cls, url: str) -> bool
```

X.can_launch_url(url) -> bool
Can Launch URL

Args:
    url (str): 

Returns:
    bool:

<a id="unreal.SystemLibrary.cancel_transaction"></a>

#### cancel_transaction

```python
@classmethod
def cancel_transaction(cls, index: int) -> None
```

X.cancel_transaction(index) -> None
Cancel the current transaction, and no longer capture actions to be placed in the undo buffer.
note: Only available in the editor.

Args:
    index (int32): The action counter to cancel transactions from (as returned by a call to BeginTransaction).

<a id="unreal.SystemLibrary.box_trace_single_for_objects"></a>

#### box_trace_single_for_objects

```python
@classmethod
def box_trace_single_for_objects(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        half_size: Vector,
        orientation: Rotator,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.box_trace_single_for_objects(world_context_object, start, end, half_size, orientation, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweeps a box along the given line and returns the first hit encountered.
This only finds objects that are of a type specified by ObjectTypes.

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    half_size (Vector): Radius of the sphere to sweep
    orientation (Rotator): 
    object_types (Array[ObjectTypeQuery]): Array of Object Types to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.box_trace_single_by_profile"></a>

#### box_trace_single_by_profile

```python
@classmethod
def box_trace_single_by_profile(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        half_size: Vector,
        orientation: Rotator,
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[HitResult]
```

X.box_trace_single_by_profile(world_context_object, start, end, half_size, orientation, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweep a box against the world and return the first blocking hit using a specific profile

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    half_size (Vector): Distance from the center of box along each axis
    orientation (Rotator): Orientation of the box
    profile_name (Name): The 'profile' used to determine which components to hit
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.box_trace_single"></a>

#### box_trace_single

```python
@classmethod
def box_trace_single(cls,
                     world_context_object: Object,
                     start: Vector,
                     end: Vector,
                     half_size: Vector,
                     orientation: Rotator,
                     trace_channel: TraceTypeQuery,
                     trace_complex: bool,
                     actors_to_ignore: Array[Actor],
                     draw_debug_type: DrawDebugTrace,
                     ignore_self: bool = True,
                     trace_color: LinearColor = [
                         1.000000, 0.000000, 0.000000, 1.000000
                     ],
                     trace_hit_color: LinearColor = [
                         0.000000, 1.000000, 0.000000, 1.000000
                     ],
                     draw_time: float = 5.000000) -> Optional[HitResult]
```

X.box_trace_single(world_context_object, start, end, half_size, orientation, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> HitResult or None
Sweeps a box along the given line and returns the first blocking hit encountered.
This trace finds the objects that RESPONDS to the given TraceChannel

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    half_size (Vector): Distance from the center of box along each axis
    orientation (Rotator): Orientation of the box
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    HitResult or None: True if there was a hit, false otherwise.

    out_hit (HitResult): Properties of the trace hit.

<a id="unreal.SystemLibrary.box_trace_multi_for_objects"></a>

#### box_trace_multi_for_objects

```python
@classmethod
def box_trace_multi_for_objects(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        half_size: Vector,
        orientation: Rotator,
        object_types: Array[ObjectTypeQuery],
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.box_trace_multi_for_objects(world_context_object, start, end, half_size, orientation, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweeps a box along the given line and returns all hits encountered.
This only finds objects that are of a type specified by ObjectTypes.

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    half_size (Vector): Radius of the sphere to sweep
    orientation (Rotator): 
    object_types (Array[ObjectTypeQuery]): Array of Object Types to trace
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.box_trace_multi_by_profile"></a>

#### box_trace_multi_by_profile

```python
@classmethod
def box_trace_multi_by_profile(
        cls,
        world_context_object: Object,
        start: Vector,
        end: Vector,
        half_size: Vector,
        orientation: Rotator,
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        draw_debug_type: DrawDebugTrace,
        ignore_self: bool = True,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.box_trace_multi_by_profile(world_context_object, start, end, half_size, orientation, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweep a box against the world and return all initial overlaps using a specific profile, then overlapping hits and then first blocking hit
Results are sorted, so a blocking hit (if found) will be the last element of the array
Only the single closest blocking result will be generated, no tests will be done after that

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    half_size (Vector): Distance from the center of box along each axis
    orientation (Rotator): Orientation of the box
    profile_name (Name): The 'profile' used to determine which components to hit
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a blocking hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish. The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.box_trace_multi"></a>

#### box_trace_multi

```python
@classmethod
def box_trace_multi(cls,
                    world_context_object: Object,
                    start: Vector,
                    end: Vector,
                    half_size: Vector,
                    orientation: Rotator,
                    trace_channel: TraceTypeQuery,
                    trace_complex: bool,
                    actors_to_ignore: Array[Actor],
                    draw_debug_type: DrawDebugTrace,
                    ignore_self: bool = True,
                    trace_color: LinearColor = [
                        1.000000, 0.000000, 0.000000, 1.000000
                    ],
                    trace_hit_color: LinearColor = [
                        0.000000, 1.000000, 0.000000, 1.000000
                    ],
                    draw_time: float = 5.000000) -> Optional[Array[HitResult]]
```

X.box_trace_multi(world_context_object, start, end, half_size, orientation, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self=True, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> Array[HitResult] or None
Sweeps a box along the given line and returns all hits encountered.
This trace finds the objects that RESPONDS to the given TraceChannel

Args:
    world_context_object (Object): 
    start (Vector): Start of line segment.
    end (Vector): End of line segment.
    half_size (Vector): Distance from the center of box along each axis
    orientation (Rotator): Orientation of the box
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): True to test against complex collision, false to test against simplified collision.
    actors_to_ignore (Array[Actor]): 
    draw_debug_type (DrawDebugTrace): 
    ignore_self (bool): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    Array[HitResult] or None: True if there was a blocking hit, false otherwise.

    out_hits (Array[HitResult]): A list of hits, sorted along the trace from start to finish. The blocking hit will be the last hit, if there was one.

<a id="unreal.SystemLibrary.box_overlap_components"></a>

#### box_overlap_components

```python
@classmethod
def box_overlap_components(
        cls, world_context_object: Object, box_pos: Vector, extent: Vector,
        object_types: Array[ObjectTypeQuery], component_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[PrimitiveComponent]]
```

X.box_overlap_components(world_context_object, box_pos, extent, object_types, component_class_filter, actors_to_ignore) -> Array[PrimitiveComponent] or None
Returns an array of components that overlap the given axis-aligned box.

Args:
    world_context_object (Object): 
    box_pos (Vector): Center of box.
    extent (Vector): 
    object_types (Array[ObjectTypeQuery]): 
    component_class_filter (type(Class)): 
    actors_to_ignore (Array[Actor]): Ignore these actors in the list

Returns:
    Array[PrimitiveComponent] or None: true if there was an overlap that passed the filters, false otherwise.

    out_components (Array[PrimitiveComponent]):

<a id="unreal.SystemLibrary.box_overlap_components_new"></a>

#### box_overlap_components_new

```python
@classmethod
def box_overlap_components_new(
        cls, world_context_object: Object, box_pos: Vector, extent: Vector,
        object_types: Array[ObjectTypeQuery], component_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[PrimitiveComponent]]
```

deprecated: 'box_overlap_components_new' was renamed to 'box_overlap_components'.

<a id="unreal.SystemLibrary.box_overlap_actors"></a>

#### box_overlap_actors

```python
@classmethod
def box_overlap_actors(
        cls, world_context_object: Object, box_pos: Vector, box_extent: Vector,
        object_types: Array[ObjectTypeQuery], actor_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[Actor]]
```

X.box_overlap_actors(world_context_object, box_pos, box_extent, object_types, actor_class_filter, actors_to_ignore) -> Array[Actor] or None
Returns an array of actors that overlap the given axis-aligned box.

Args:
    world_context_object (Object): 
    box_pos (Vector): Center of box.
    box_extent (Vector): Extents of box.
    object_types (Array[ObjectTypeQuery]): 
    actor_class_filter (type(Class)): 
    actors_to_ignore (Array[Actor]): Ignore these actors in the list

Returns:
    Array[Actor] or None: true if there was an overlap that passed the filters, false otherwise.

    out_actors (Array[Actor]): Returned array of actors. Unsorted.

<a id="unreal.SystemLibrary.box_overlap_actors_new"></a>

#### box_overlap_actors_new

```python
@classmethod
def box_overlap_actors_new(
        cls, world_context_object: Object, box_pos: Vector, box_extent: Vector,
        object_types: Array[ObjectTypeQuery], actor_class_filter: Class,
        actors_to_ignore: Array[Actor]) -> Optional[Array[Actor]]
```

deprecated: 'box_overlap_actors_new' was renamed to 'box_overlap_actors'.

<a id="unreal.SystemLibrary.begin_transaction"></a>

#### begin_transaction

```python
@classmethod
def begin_transaction(cls, context: str, description: Text,
                      primary_object: Object) -> int
```

X.begin_transaction(context, description, primary_object) -> int32
Begin a new undo transaction. An undo transaction is defined as all actions which take place when the user selects "undo" a single time.
note: If there is already an active transaction in progress, then this increments that transaction's action counter instead of beginning a new transaction.
note: You must call TransactObject before modifying each object that should be included in this undo transaction.
note: Only available in the editor.

Args:
    context (str): The context for the undo session. Typically the tool/editor that caused the undo operation.
    description (Text): The description for the undo session. This is the text that will appear in the "Edit" menu next to the Undo item.
    primary_object (Object): The primary object that the undo session operators on (can be null, and mostly is).

Returns:
    int32: The number of active actions when BeginTransaction was called (values greater than 0 indicate that there was already an existing undo transaction in progress), or -1 on failure.

<a id="unreal.SystemLibrary.add_float_history_sample"></a>

#### add_float_history_sample

```python
@classmethod
def add_float_history_sample(
        cls, value: float,
        float_history: DebugFloatHistory) -> DebugFloatHistory
```

X.add_float_history_sample(value, float_history) -> DebugFloatHistory
Add Float History Sample

Args:
    value (float): 
    float_history (DebugFloatHistory): 

Returns:
    DebugFloatHistory:

<a id="unreal.Paths"></a>