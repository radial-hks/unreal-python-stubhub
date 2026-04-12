## UserWidget Objects

```python
class UserWidget(Widget)
```

A widget that enables UI extensibility through WidgetBlueprint.

**C++ Source:**

- **Module**: UMG
- **File**: UserWidget.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``color_and_opacity`` (LinearColor):  [Read-Write] The color and opacity of this widget.  Tints all child widgets.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``desired_focus_widget`` (WidgetChild):  [Read-Write]
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``foreground_color`` (SlateColor):  [Read-Write] The foreground color of the widget, this is inherited by sub widgets.  Any color property
  that is marked as inherit will use this color.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write] Setting this flag to true, allows this widget to accept focus when clicked, or when navigated to.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_visibility_changed`` (OnVisibilityChangedEvent):  [Read-Write] Called when the visibility has changed
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``padding`` (Margin):  [Read-Write] The padding area around the content.
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``preview_background`` (Texture2D):  [Read-Write] A preview background that you can use when designing the UI to get a sense of scale on the screen.  Use
  a texture with a screenshot of your game in it, for example if you were designing a HUD.
- ``priority`` (int32):  [Read-Write]
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``stop_action`` (bool):  [Read-Write]
- ``tick_frequency`` (WidgetTickFrequency):  [Read-Write] This widget is allowed to tick. If this is unchecked tick will never be called, animations will not play correctly, and latent actions will not execute.
  Uncheck this for performance reasons only
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.UserWidget.color_and_opacity"></a>

#### color\_and\_opacity

```python
@property
def color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write] The color and opacity of this widget.  Tints all child widgets.

<a id="unreal.UserWidget.color_and_opacity"></a>

#### color\_and\_opacity

```python
@color_and_opacity.setter
def color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.UserWidget.foreground_color"></a>

#### foreground\_color

```python
@property
def foreground_color() -> SlateColor
```

(SlateColor):  [Read-Write] The foreground color of the widget, this is inherited by sub widgets.  Any color property
that is marked as inherit will use this color.

<a id="unreal.UserWidget.foreground_color"></a>

#### foreground\_color

```python
@foreground_color.setter
def foreground_color(value: SlateColor) -> None
```

<a id="unreal.UserWidget.on_visibility_changed"></a>

#### on\_visibility\_changed

```python
@property
def on_visibility_changed() -> OnVisibilityChangedEvent
```

(OnVisibilityChangedEvent):  [Read-Write] Called when the visibility has changed

<a id="unreal.UserWidget.on_visibility_changed"></a>

#### on\_visibility\_changed

```python
@on_visibility_changed.setter
def on_visibility_changed(value: OnVisibilityChangedEvent) -> None
```

<a id="unreal.UserWidget.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area around the content.

<a id="unreal.UserWidget.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.UserWidget.priority"></a>

#### priority

```python
@property
def priority() -> int
```

(int32):  [Read-Write]

<a id="unreal.UserWidget.priority"></a>

#### priority

```python
@priority.setter
def priority(value: int) -> None
```

<a id="unreal.UserWidget.is_focusable"></a>

#### is\_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Write] Setting this flag to true, allows this widget to accept focus when clicked, or when navigated to.

<a id="unreal.UserWidget.is_focusable"></a>

#### is\_focusable

```python
@is_focusable.setter
def is_focusable(value: bool) -> None
```

<a id="unreal.UserWidget.stop_action"></a>

#### stop\_action

```python
@property
def stop_action() -> bool
```

(bool):  [Read-Write]

<a id="unreal.UserWidget.stop_action"></a>

#### stop\_action

```python
@stop_action.setter
def stop_action(value: bool) -> None
```

<a id="unreal.UserWidget.tick_frequency"></a>

#### tick\_frequency

```python
@property
def tick_frequency() -> WidgetTickFrequency
```

(WidgetTickFrequency):  [Read-Only] This widget is allowed to tick. If this is unchecked tick will never be called, animations will not play correctly, and latent actions will not execute.
Uncheck this for performance reasons only

<a id="unreal.UserWidget.unregister_input_component"></a>

#### unregister\_input\_component

```python
def unregister_input_component() -> None
```

x.unregister_input_component() -> None
StopListeningForAllInputActions will automatically Register an Input Component with the player input system.
If you however, want to Pause and Resume, listening for a set of actions, the best way is to use
UnregisterInputComponent to pause, and RegisterInputComponent to resume listening.

<a id="unreal.UserWidget.unbind_from_animation_started"></a>

#### unbind\_from\_animation\_started

```python
def unbind_from_animation_started(
        animation: WidgetAnimation,
        delegate: WidgetAnimationDynamicEvent) -> None
```

x.unbind_from_animation_started(animation, delegate) -> None
Unbind an animation started delegate.

Args:
    animation (WidgetAnimation): the animation to listen for starting or finishing.
    delegate (WidgetAnimationDynamicEvent): the delegate to call when the animation's state changes

<a id="unreal.UserWidget.unbind_from_animation_finished"></a>

#### unbind\_from\_animation\_finished

```python
def unbind_from_animation_finished(
        animation: WidgetAnimation,
        delegate: WidgetAnimationDynamicEvent) -> None
```

x.unbind_from_animation_finished(animation, delegate) -> None
Unbind an animation finished delegate.

Args:
    animation (WidgetAnimation): the animation to listen for starting or finishing.
    delegate (WidgetAnimationDynamicEvent): the delegate to call when the animation's state changes

<a id="unreal.UserWidget.unbind_all_from_animation_started"></a>

#### unbind\_all\_from\_animation\_started

```python
def unbind_all_from_animation_started(animation: WidgetAnimation) -> None
```

x.unbind_all_from_animation_started(animation) -> None
Unbind All from Animation Started

Args:
    animation (WidgetAnimation):

<a id="unreal.UserWidget.unbind_all_from_animation_finished"></a>

#### unbind\_all\_from\_animation\_finished

```python
def unbind_all_from_animation_finished(animation: WidgetAnimation) -> None
```

x.unbind_all_from_animation_finished(animation) -> None
Unbind All from Animation Finished

Args:
    animation (WidgetAnimation):

<a id="unreal.UserWidget.tick"></a>

#### tick

```python
def tick(my_geometry: Geometry, delta_time: float) -> None
```

x.tick(my_geometry, delta_time) -> None
Ticks this widget.  Override in derived classes, but always call the parent implementation.

Args:
    my_geometry (Geometry): The space allotted for this widget
    delta_time (float): Real time passed since last tick

<a id="unreal.UserWidget.stop_listening_for_input_action"></a>

#### stop\_listening\_for\_input\_action

```python
def stop_listening_for_input_action(action_name: Name,
                                    event_type: InputEventType) -> None
```

x.stop_listening_for_input_action(action_name, event_type) -> None
Removes the binding for a particular action's callback.

Args:
    action_name (Name): 
    event_type (InputEventType):

<a id="unreal.UserWidget.stop_listening_for_all_input_actions"></a>

#### stop\_listening\_for\_all\_input\_actions

```python
def stop_listening_for_all_input_actions() -> None
```

x.stop_listening_for_all_input_actions() -> None
Stops listening to all input actions, and unregisters the input component with the player controller.

<a id="unreal.UserWidget.stop_animations_and_latent_actions"></a>

#### stop\_animations\_and\_latent\_actions

```python
def stop_animations_and_latent_actions() -> None
```

x.stop_animations_and_latent_actions() -> None
Cancels any pending Delays or timer callbacks for this widget, and stops all active animations on the widget.

<a id="unreal.UserWidget.stop_animation"></a>

#### stop\_animation

```python
def stop_animation(animation: WidgetAnimation) -> None
```

x.stop_animation(animation) -> None
Stops an already running animation in this widget

Args:
    animation (WidgetAnimation):

<a id="unreal.UserWidget.stop_all_animations"></a>

#### stop\_all\_animations

```python
def stop_all_animations() -> None
```

x.stop_all_animations() -> None
Stop All actively running animations.

<a id="unreal.UserWidget.set_position_in_viewport"></a>

#### set\_position\_in\_viewport

```python
def set_position_in_viewport(position: Vector2D,
                             remove_dpi_scale: bool = True) -> None
```

x.set_position_in_viewport(position, remove_dpi_scale=True) -> None
Sets the widgets position in the viewport.

Args:
    position (Vector2D): The 2D position to set the widget to in the viewport.
    remove_dpi_scale (bool): If you've already calculated inverse DPI, set this to false. Otherwise inverse DPI is applied to the position so that when the location is scaled by DPI, it ends up in the expected position.

<a id="unreal.UserWidget.set_playback_speed"></a>

#### set\_playback\_speed

```python
def set_playback_speed(animation: WidgetAnimation,
                       playback_speed: float = 1.000000) -> None
```

x.set_playback_speed(animation, playback_speed=1.000000) -> None
Changes the playback rate of a playing animation

Args:
    animation (WidgetAnimation): The animation that is already playing
    playback_speed (float):

<a id="unreal.UserWidget.set_padding"></a>

#### set\_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Sets the padding for the user widget, putting a larger gap between the widget border and it's root widget.

Args:
    padding (Margin):

<a id="unreal.UserWidget.set_owning_player"></a>

#### set\_owning\_player

```python
def set_owning_player(local_player_controller: PlayerController) -> None
```

x.set_owning_player(local_player_controller) -> None
Sets the local player associated with this UI via PlayerController reference.

Args:
    local_player_controller (PlayerController): The PlayerController of the local player you want to be the conceptual owner of this UI.

<a id="unreal.UserWidget.set_num_loops_to_play"></a>

#### set\_num\_loops\_to\_play

```python
def set_num_loops_to_play(animation: WidgetAnimation,
                          num_loops_to_play: int) -> None
```

x.set_num_loops_to_play(animation, num_loops_to_play) -> None
Changes the number of loops to play given a playing animation

Args:
    animation (WidgetAnimation): The animation that is already playing
    num_loops_to_play (int32): The number of loops to play. (0 to loop indefinitely)

<a id="unreal.UserWidget.set_input_action_priority"></a>

#### set\_input\_action\_priority

```python
def set_input_action_priority(new_priority: int) -> None
```

x.set_input_action_priority(new_priority) -> None
Set Input Action Priority

Args:
    new_priority (int32):

<a id="unreal.UserWidget.set_input_action_blocking"></a>

#### set\_input\_action\_blocking

```python
def set_input_action_blocking(should_block: bool) -> None
```

x.set_input_action_blocking(should_block) -> None
Set Input Action Blocking

Args:
    should_block (bool):

<a id="unreal.UserWidget.set_foreground_color"></a>

#### set\_foreground\_color

```python
def set_foreground_color(foreground_color: SlateColor) -> None
```

x.set_foreground_color(foreground_color) -> None
Sets the foreground color of the widget, this is inherited by sub widgets.  Any color property
that is marked as inherit will use this color.

Args:
    foreground_color (SlateColor): The foreground color.

<a id="unreal.UserWidget.set_desired_size_in_viewport"></a>

#### set\_desired\_size\_in\_viewport

```python
def set_desired_size_in_viewport(size: Vector2D) -> None
```

x.set_desired_size_in_viewport(size) -> None
Set Desired Size in Viewport

Args:
    size (Vector2D):

<a id="unreal.UserWidget.set_color_and_opacity"></a>

#### set\_color\_and\_opacity

```python
def set_color_and_opacity(color_and_opacity: LinearColor) -> None
```

x.set_color_and_opacity(color_and_opacity) -> None
Sets the tint of the widget, this affects all child widgets.

Args:
    color_and_opacity (LinearColor): The tint to apply to all child widgets.

<a id="unreal.UserWidget.set_animation_current_time"></a>

#### set\_animation\_current\_time

```python
def set_animation_current_time(animation: WidgetAnimation,
                               time: float) -> None
```

x.set_animation_current_time(animation, time) -> None
Sets the current time of the animation in this widget. Does not change state.

Args:
    animation (WidgetAnimation): 
    time (float):

<a id="unreal.UserWidget.set_anchors_in_viewport"></a>

#### set\_anchors\_in\_viewport

```python
def set_anchors_in_viewport(anchors: Anchors) -> None
```

x.set_anchors_in_viewport(anchors) -> None
Set Anchors in Viewport

Args:
    anchors (Anchors):

<a id="unreal.UserWidget.set_alignment_in_viewport"></a>

#### set\_alignment\_in\_viewport

```python
def set_alignment_in_viewport(alignment: Vector2D) -> None
```

x.set_alignment_in_viewport(alignment) -> None
Set Alignment in Viewport

Args:
    alignment (Vector2D):

<a id="unreal.UserWidget.reverse_animation"></a>

#### reverse\_animation

```python
def reverse_animation(animation: WidgetAnimation) -> None
```

x.reverse_animation(animation) -> None
If an animation is playing, this function will reverse the playback.

Args:
    animation (WidgetAnimation): The playing animation that we want to reverse

<a id="unreal.UserWidget.remove_from_viewport"></a>

#### remove\_from\_viewport

```python
def remove_from_viewport() -> None
```

x.remove_from_viewport() -> None
Remove from Viewport
deprecated: Use RemoveFromParent instead

<a id="unreal.UserWidget.remove_extensions"></a>

#### remove\_extensions

```python
def remove_extensions(extension_type: Class) -> None
```

x.remove_extensions(extension_type) -> None
Remove all extensions of the requested type.

Args:
    extension_type (type(Class)):

<a id="unreal.UserWidget.remove_extension"></a>

#### remove\_extension

```python
def remove_extension(extension: UserWidgetExtension) -> None
```

x.remove_extension(extension) -> None
Remove the extension.

Args:
    extension (UserWidgetExtension):

<a id="unreal.UserWidget.register_input_component"></a>

#### register\_input\_component

```python
def register_input_component() -> None
```

x.register_input_component() -> None
ListenForInputAction will automatically Register an Input Component with the player input system.
If you however, want to Pause and Resume, listening for a set of actions, the best way is to use
UnregisterInputComponent to pause, and RegisterInputComponent to resume listening.

<a id="unreal.UserWidget.queue_stop_animation"></a>

#### queue\_stop\_animation

```python
def queue_stop_animation(animation: WidgetAnimation) -> None
```

x.queue_stop_animation(animation) -> None
Stops an already running animation in this widget

Args:
    animation (WidgetAnimation):

<a id="unreal.UserWidget.queue_stop_all_animations"></a>

#### queue\_stop\_all\_animations

```python
def queue_stop_all_animations() -> None
```

x.queue_stop_all_animations() -> None
Stop All actively running animations.

<a id="unreal.UserWidget.queue_play_animation_time_range"></a>

#### queue\_play\_animation\_time\_range

```python
def queue_play_animation_time_range(
        animation: WidgetAnimation,
        start_at_time: float = 0.000000,
        end_at_time: float = 0.000000,
        num_loops_to_play: int = 1,
        play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD,
        playback_speed: float = 1.000000,
        restore_state: bool = False) -> None
```

x.queue_play_animation_time_range(animation, start_at_time=0.000000, end_at_time=0.000000, num_loops_to_play=1, play_mode=UMGSequencePlayMode.FORWARD, playback_speed=1.000000, restore_state=False) -> None
Plays an animation in this widget a specified number of times stopping at a specified time

Args:
    animation (WidgetAnimation): The animation to play
    start_at_time (float): The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation.
    end_at_time (float): The absolute time in the animation where to stop, this is only considered in the last loop.
    num_loops_to_play (int32): The number of times to loop this animation (0 to loop indefinitely)
    play_mode (UMGSequencePlayMode): Specifies the playback mode
    playback_speed (float): The speed at which the animation should play
    restore_state (bool): Restores widgets to their pre-animated state when the animation stops

<a id="unreal.UserWidget.queue_play_animation_reverse"></a>

#### queue\_play\_animation\_reverse

```python
def queue_play_animation_reverse(animation: WidgetAnimation,
                                 playback_speed: float = 1.000000,
                                 restore_state: bool = False) -> None
```

x.queue_play_animation_reverse(animation, playback_speed=1.000000, restore_state=False) -> None
Plays an animation on this widget relative to it's current state in reverse.  You should use this version in situations where
say a user can click a button and that causes a panel to slide out, and you want to reverse that same animation to begin sliding
in the opposite direction.

Args:
    animation (WidgetAnimation): The animation to play
    playback_speed (float): The speed at which the animation should play
    restore_state (bool): Restores widgets to their pre-animated state when the animation stops

<a id="unreal.UserWidget.queue_play_animation_forward"></a>

#### queue\_play\_animation\_forward

```python
def queue_play_animation_forward(animation: WidgetAnimation,
                                 playback_speed: float = 1.000000,
                                 restore_state: bool = False) -> None
```

x.queue_play_animation_forward(animation, playback_speed=1.000000, restore_state=False) -> None
Plays an animation on this widget relative to it's current state forward.  You should use this version in situations where
say a user can click a button and that causes a panel to slide out, and you want to reverse that same animation to begin sliding
in the opposite direction.

Args:
    animation (WidgetAnimation): The animation to play
    playback_speed (float): The speed at which the animation should play
    restore_state (bool): Restores widgets to their pre-animated state when the animation stops

<a id="unreal.UserWidget.queue_play_animation"></a>

#### queue\_play\_animation

```python
def queue_play_animation(
        animation: WidgetAnimation,
        start_at_time: float = 0.000000,
        num_loops_to_play: int = 1,
        play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD,
        playback_speed: float = 1.000000,
        restore_state: bool = False) -> None
```

x.queue_play_animation(animation, start_at_time=0.000000, num_loops_to_play=1, play_mode=UMGSequencePlayMode.FORWARD, playback_speed=1.000000, restore_state=False) -> None
Plays an animation in this widget a specified number of times

Args:
    animation (WidgetAnimation): The animation to play
    start_at_time (float): The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation.
    num_loops_to_play (int32): The number of times to loop this animation (0 to loop indefinitely)
    play_mode (UMGSequencePlayMode): Specifies the playback mode
    playback_speed (float): The speed at which the animation should play
    restore_state (bool): Restores widgets to their pre-animated state when the animation stops

<a id="unreal.UserWidget.queue_pause_animation"></a>

#### queue\_pause\_animation

```python
def queue_pause_animation(animation: WidgetAnimation) -> float
```

x.queue_pause_animation(animation) -> float
Pauses an already running animation in this widget

Args:
    animation (WidgetAnimation): 

Returns:
    float: the time point the animation was at when it was paused, relative to its start position.  Use this as the StartAtTime when you trigger PlayAnimation.

<a id="unreal.UserWidget.pre_construct"></a>

#### pre\_construct

```python
def pre_construct(is_design_time: bool) -> None
```

x.pre_construct(is_design_time) -> None
Called by both the game and the editor.  Allows users to run initial setup for their widgets to better preview
the setup in the designer and since generally that same setup code is required at runtime, it's called there
as well.

**WARNING**
This is intended purely for cosmetic updates using locally owned data, you can not safely access any game related
state, if you call something that doesn't expect to be run at editor time, you may crash the editor.

In the event you save the asset with blueprint code that causes a crash on evaluation.  You can turn off
PreConstruct evaluation in the Widget Designer settings in the Editor Preferences.

Args:
    is_design_time (bool):

<a id="unreal.UserWidget.play_sound"></a>

#### play\_sound

```python
def play_sound(sound_to_play: SoundBase) -> None
```

x.play_sound(sound_to_play) -> None
Plays a sound through the UI
deprecated: Use the UGameplayStatics::PlaySound2D instead.

Args:
    sound_to_play (SoundBase):

<a id="unreal.UserWidget.play_animation_time_range"></a>

#### play\_animation\_time\_range

```python
def play_animation_time_range(
        animation: WidgetAnimation,
        start_at_time: float = 0.000000,
        end_at_time: float = 0.000000,
        num_loops_to_play: int = 1,
        play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD,
        playback_speed: float = 1.000000,
        restore_state: bool = False) -> UMGSequencePlayer
```

x.play_animation_time_range(animation, start_at_time=0.000000, end_at_time=0.000000, num_loops_to_play=1, play_mode=UMGSequencePlayMode.FORWARD, playback_speed=1.000000, restore_state=False) -> UMGSequencePlayer
Plays an animation in this widget a specified number of times stopping at a specified time

Args:
    animation (WidgetAnimation): The animation to play
    start_at_time (float): The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation.
    end_at_time (float): The absolute time in the animation where to stop, this is only considered in the last loop.
    num_loops_to_play (int32): The number of times to loop this animation (0 to loop indefinitely)
    play_mode (UMGSequencePlayMode): Specifies the playback mode
    playback_speed (float): The speed at which the animation should play
    restore_state (bool): Restores widgets to their pre-animated state when the animation stops

Returns:
    UMGSequencePlayer:

<a id="unreal.UserWidget.play_animation_to"></a>

#### play\_animation\_to

```python
def play_animation_to(
        animation: WidgetAnimation,
        start_at_time: float = 0.000000,
        end_at_time: float = 0.000000,
        num_loops_to_play: int = 1,
        play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD,
        playback_speed: float = 1.000000,
        restore_state: bool = False) -> UMGSequencePlayer
```

deprecated: 'play_animation_to' was renamed to 'play_animation_time_range'.

<a id="unreal.UserWidget.play_animation_reverse"></a>

#### play\_animation\_reverse

```python
def play_animation_reverse(animation: WidgetAnimation,
                           playback_speed: float = 1.000000,
                           restore_state: bool = False) -> UMGSequencePlayer
```

x.play_animation_reverse(animation, playback_speed=1.000000, restore_state=False) -> UMGSequencePlayer
Plays an animation on this widget relative to it's current state in reverse.  You should use this version in situations where
say a user can click a button and that causes a panel to slide out, and you want to reverse that same animation to begin sliding
in the opposite direction.

Args:
    animation (WidgetAnimation): The animation to play
    playback_speed (float): The speed at which the animation should play
    restore_state (bool): Restores widgets to their pre-animated state when the animation stops

Returns:
    UMGSequencePlayer:

<a id="unreal.UserWidget.play_animation_forward"></a>

#### play\_animation\_forward

```python
def play_animation_forward(animation: WidgetAnimation,
                           playback_speed: float = 1.000000,
                           restore_state: bool = False) -> UMGSequencePlayer
```

x.play_animation_forward(animation, playback_speed=1.000000, restore_state=False) -> UMGSequencePlayer
Plays an animation on this widget relative to it's current state forward.  You should use this version in situations where
say a user can click a button and that causes a panel to slide out, and you want to reverse that same animation to begin sliding
in the opposite direction.

Args:
    animation (WidgetAnimation): The animation to play
    playback_speed (float): The speed at which the animation should play
    restore_state (bool): Restores widgets to their pre-animated state when the animation stops

Returns:
    UMGSequencePlayer:

<a id="unreal.UserWidget.play_animation"></a>

#### play\_animation

```python
def play_animation(
        animation: WidgetAnimation,
        start_at_time: float = 0.000000,
        num_loops_to_play: int = 1,
        play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD,
        playback_speed: float = 1.000000,
        restore_state: bool = False) -> UMGSequencePlayer
```

x.play_animation(animation, start_at_time=0.000000, num_loops_to_play=1, play_mode=UMGSequencePlayMode.FORWARD, playback_speed=1.000000, restore_state=False) -> UMGSequencePlayer
Plays an animation in this widget a specified number of times

Args:
    animation (WidgetAnimation): The animation to play
    start_at_time (float): The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation.
    num_loops_to_play (int32): The number of times to loop this animation (0 to loop indefinitely)
    play_mode (UMGSequencePlayMode): Specifies the playback mode
    playback_speed (float): The speed at which the animation should play
    restore_state (bool): Restores widgets to their pre-animated state when the animation stops

Returns:
    UMGSequencePlayer:

<a id="unreal.UserWidget.play_animation_at_time"></a>

#### play\_animation\_at\_time

```python
def play_animation_at_time(
        animation: WidgetAnimation,
        start_at_time: float = 0.000000,
        num_loops_to_play: int = 1,
        play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD,
        playback_speed: float = 1.000000,
        restore_state: bool = False) -> UMGSequencePlayer
```

deprecated: 'play_animation_at_time' was renamed to 'play_animation'.

<a id="unreal.UserWidget.pause_animation"></a>

#### pause\_animation

```python
def pause_animation(animation: WidgetAnimation) -> float
```

x.pause_animation(animation) -> float
Pauses an already running animation in this widget

Args:
    animation (WidgetAnimation): 

Returns:
    float: the time point the animation was at when it was paused, relative to its start position.  Use this as the StartAtTime when you trigger PlayAnimation.

<a id="unreal.UserWidget.on_touch_started"></a>

#### on\_touch\_started

```python
def on_touch_started(my_geometry: Geometry,
                     touch_event: PointerEvent) -> EventReply
```

x.on_touch_started(my_geometry, touch_event) -> EventReply
Called when a touchpad touch is started (finger down)

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    touch_event (PointerEvent): The touch event generated

Returns:
    EventReply:

<a id="unreal.UserWidget.on_touch_moved"></a>

#### on\_touch\_moved

```python
def on_touch_moved(my_geometry: Geometry,
                   touch_event: PointerEvent) -> EventReply
```

x.on_touch_moved(my_geometry, touch_event) -> EventReply
Called when a touchpad touch is moved  (finger moved)

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    touch_event (PointerEvent): The touch event generated

Returns:
    EventReply:

<a id="unreal.UserWidget.on_touch_gesture"></a>

#### on\_touch\_gesture

```python
def on_touch_gesture(my_geometry: Geometry,
                     gesture_event: PointerEvent) -> EventReply
```

x.on_touch_gesture(my_geometry, gesture_event) -> EventReply
Called when the user performs a gesture on trackpad. This event is bubbled.

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    gesture_event (PointerEvent): gesture event

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_touch_force_changed"></a>

#### on\_touch\_force\_changed

```python
def on_touch_force_changed(my_geometry: Geometry,
                           touch_event: PointerEvent) -> EventReply
```

x.on_touch_force_changed(my_geometry, touch_event) -> EventReply
Called when a touchpad force has changed (user pressed down harder or let up)

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    touch_event (PointerEvent): The touch event generated

Returns:
    EventReply:

<a id="unreal.UserWidget.on_touch_ended"></a>

#### on\_touch\_ended

```python
def on_touch_ended(my_geometry: Geometry,
                   touch_event: PointerEvent) -> EventReply
```

x.on_touch_ended(my_geometry, touch_event) -> EventReply
Called when a touchpad touch is ended (finger lifted)

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    touch_event (PointerEvent): The touch event generated

Returns:
    EventReply:

<a id="unreal.UserWidget.on_removed_from_focus_path"></a>

#### on\_removed\_from\_focus\_path

```python
def on_removed_from_focus_path(focus_event: FocusEvent) -> None
```

x.on_removed_from_focus_path(focus_event) -> None
If focus is lost on on this widget or on a child widget and this widget is
no longer part of the focus path.

Args:
    focus_event (FocusEvent): FocusEvent

<a id="unreal.UserWidget.on_preview_mouse_button_down"></a>

#### on\_preview\_mouse\_button\_down

```python
def on_preview_mouse_button_down(my_geometry: Geometry,
                                 mouse_event: PointerEvent) -> EventReply
```

x.on_preview_mouse_button_down(my_geometry, mouse_event) -> EventReply
Just like OnMouseButtonDown, but tunnels instead of bubbling.
If this event is handled, OnMouseButtonDown will not be sent.

Use this event sparingly as preview events generally make UIs more
difficult to reason about.

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    mouse_event (PointerEvent): Information about the input event

Returns:
    EventReply: Whether the event was handled along with possible requests for the system to take action.

<a id="unreal.UserWidget.on_preview_key_down"></a>

#### on\_preview\_key\_down

```python
def on_preview_key_down(my_geometry: Geometry,
                        key_event: KeyEvent) -> EventReply
```

x.on_preview_key_down(my_geometry, key_event) -> EventReply
Called after a key (keyboard, controller, ...) is pressed when this widget or a child of this widget has focus
If a widget handles this event, OnKeyDown will *not* be passed to the focused widget.

This event is primarily to allow parent widgets to consume an event before a child widget processes
it and it should be used only when there is no better design alternative.

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    key_event (KeyEvent): Key event

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_paint"></a>

#### on\_paint

```python
def on_paint(context: PaintContext) -> PaintContext
```

x.on_paint(context) -> PaintContext
On Paint

Args:
    context (PaintContext): 

Returns:
    PaintContext: 

    context (PaintContext):

<a id="unreal.UserWidget.on_mouse_wheel"></a>

#### on\_mouse\_wheel

```python
def on_mouse_wheel(my_geometry: Geometry,
                   mouse_event: PointerEvent) -> EventReply
```

x.on_mouse_wheel(my_geometry, mouse_event) -> EventReply
Called when the mouse wheel is spun. This event is bubbled.

Args:
    my_geometry (Geometry): 
    mouse_event (PointerEvent): Mouse event

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_mouse_move"></a>

#### on\_mouse\_move

```python
def on_mouse_move(my_geometry: Geometry,
                  mouse_event: PointerEvent) -> EventReply
```

x.on_mouse_move(my_geometry, mouse_event) -> EventReply
The system calls this method to notify the widget that a mouse moved within it. This event is bubbled.

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    mouse_event (PointerEvent): Information about the input event

Returns:
    EventReply: Whether the event was handled along with possible requests for the system to take action.

<a id="unreal.UserWidget.on_mouse_leave"></a>

#### on\_mouse\_leave

```python
def on_mouse_leave(mouse_event: PointerEvent) -> None
```

x.on_mouse_leave(mouse_event) -> None
The system will use this event to notify a widget that the cursor has left it. This event is NOT bubbled.

Args:
    mouse_event (PointerEvent): Information about the input event

<a id="unreal.UserWidget.on_mouse_enter"></a>

#### on\_mouse\_enter

```python
def on_mouse_enter(my_geometry: Geometry, mouse_event: PointerEvent) -> None
```

x.on_mouse_enter(my_geometry, mouse_event) -> None
The system will use this event to notify a widget that the cursor has entered it. This event is NOT bubbled.

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    mouse_event (PointerEvent): Information about the input event

<a id="unreal.UserWidget.on_mouse_capture_lost"></a>

#### on\_mouse\_capture\_lost

```python
def on_mouse_capture_lost() -> None
```

x.on_mouse_capture_lost() -> None
Called when mouse capture is lost if it was owned by this widget.

<a id="unreal.UserWidget.on_mouse_button_up"></a>

#### on\_mouse\_button\_up

```python
def on_mouse_button_up(my_geometry: Geometry,
                       mouse_event: PointerEvent) -> EventReply
```

x.on_mouse_button_up(my_geometry, mouse_event) -> EventReply
The system calls this method to notify the widget that a mouse button was release within it. This event is bubbled.

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    mouse_event (PointerEvent): Information about the input event

Returns:
    EventReply: Whether the event was handled along with possible requests for the system to take action.

<a id="unreal.UserWidget.on_mouse_button_down"></a>

#### on\_mouse\_button\_down

```python
def on_mouse_button_down(my_geometry: Geometry,
                         mouse_event: PointerEvent) -> EventReply
```

x.on_mouse_button_down(my_geometry, mouse_event) -> EventReply
The system calls this method to notify the widget that a mouse button was pressed within it. This event is bubbled.

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    mouse_event (PointerEvent): Information about the input event

Returns:
    EventReply: Whether the event was handled along with possible requests for the system to take action.

<a id="unreal.UserWidget.on_mouse_button_double_click"></a>

#### on\_mouse\_button\_double\_click

```python
def on_mouse_button_double_click(my_geometry: Geometry,
                                 mouse_event: PointerEvent) -> EventReply
```

x.on_mouse_button_double_click(my_geometry, mouse_event) -> EventReply
Called when a mouse button is double clicked.  Override this in derived classes.

Args:
    my_geometry (Geometry): Widget geometry
    mouse_event (PointerEvent): Mouse button event

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_motion_detected"></a>

#### on\_motion\_detected

```python
def on_motion_detected(my_geometry: Geometry,
                       motion_event: MotionEvent) -> EventReply
```

x.on_motion_detected(my_geometry, motion_event) -> EventReply
Called when motion is detected (controller or device)
e.g. Someone tilts or shakes their controller.

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    motion_event (MotionEvent): 

Returns:
    EventReply:

<a id="unreal.UserWidget.on_key_up"></a>

#### on\_key\_up

```python
def on_key_up(my_geometry: Geometry, key_event: KeyEvent) -> EventReply
```

x.on_key_up(my_geometry, key_event) -> EventReply
Called after a key (keyboard, controller, ...) is released when this widget has focus

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    key_event (KeyEvent): Key event

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_key_down"></a>

#### on\_key\_down

```python
def on_key_down(my_geometry: Geometry, key_event: KeyEvent) -> EventReply
```

x.on_key_down(my_geometry, key_event) -> EventReply
Called after a key (keyboard, controller, ...) is pressed when this widget has focus (this event bubbles if not handled)

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    key_event (KeyEvent): Key event

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_key_char"></a>

#### on\_key\_char

```python
def on_key_char(my_geometry: Geometry,
                character_event: CharacterEvent) -> EventReply
```

x.on_key_char(my_geometry, character_event) -> EventReply
Called after a character is entered while this widget has focus

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    character_event (CharacterEvent): Character event

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_initialized"></a>

#### on\_initialized

```python
def on_initialized() -> None
```

x.on_initialized() -> None
Called once only at game time on non-template instances.
While Construct/Destruct pertain to the underlying Slate, this is called only once for the UUserWidget.
If you have one-time things to establish up-front (like binding callbacks to events on BindWidget properties), do so here.

<a id="unreal.UserWidget.on_focus_received"></a>

#### on\_focus\_received

```python
def on_focus_received(my_geometry: Geometry,
                      focus_event: FocusEvent) -> EventReply
```

x.on_focus_received(my_geometry, focus_event) -> EventReply
Called when keyboard focus is given to this widget.  This event does not bubble.

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    focus_event (FocusEvent): FocusEvent

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_focus_lost"></a>

#### on\_focus\_lost

```python
def on_focus_lost(focus_event: FocusEvent) -> None
```

x.on_focus_lost(focus_event) -> None
Called when this widget loses focus.  This event does not bubble.

Args:
    focus_event (FocusEvent): FocusEvent

<a id="unreal.UserWidget.on_drop"></a>

#### on\_drop

```python
def on_drop(my_geometry: Geometry, pointer_event: PointerEvent,
            operation: DragDropOperation) -> bool
```

x.on_drop(my_geometry, pointer_event, operation) -> bool
Called when the user is dropping something onto a widget.  Ends the drag and drop operation, even if no widget handles this.

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    pointer_event (PointerEvent): The mouse event from when the drag occurred over the widget.
    operation (DragDropOperation): The drag operation over the widget.

Returns:
    bool: 'true' to indicate you handled the drop operation.

<a id="unreal.UserWidget.on_drag_over"></a>

#### on\_drag\_over

```python
def on_drag_over(my_geometry: Geometry, pointer_event: PointerEvent,
                 operation: DragDropOperation) -> bool
```

x.on_drag_over(my_geometry, pointer_event, operation) -> bool
Called during drag and drop when the the mouse is being dragged over a widget.

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    pointer_event (PointerEvent): The mouse event from when the drag occurred over the widget.
    operation (DragDropOperation): The drag operation over the widget.

Returns:
    bool: 'true' to indicate that you handled the drag over operation.  Returning 'false' will cause the operation to continue to bubble up.

<a id="unreal.UserWidget.on_drag_leave"></a>

#### on\_drag\_leave

```python
def on_drag_leave(pointer_event: PointerEvent,
                  operation: DragDropOperation) -> None
```

x.on_drag_leave(pointer_event, operation) -> None
Called during drag and drop when the drag leaves the widget.

Args:
    pointer_event (PointerEvent): The mouse event from when the drag left the widget.
    operation (DragDropOperation): The drag operation that entered the widget.

<a id="unreal.UserWidget.on_drag_enter"></a>

#### on\_drag\_enter

```python
def on_drag_enter(my_geometry: Geometry, pointer_event: PointerEvent,
                  operation: DragDropOperation) -> None
```

x.on_drag_enter(my_geometry, pointer_event, operation) -> None
Called during drag and drop when the drag enters the widget.

Args:
    my_geometry (Geometry): The geometry of the widget receiving the event.
    pointer_event (PointerEvent): The mouse event from when the drag entered the widget.
    operation (DragDropOperation): The drag operation that entered the widget.

<a id="unreal.UserWidget.on_drag_detected"></a>

#### on\_drag\_detected

```python
def on_drag_detected(my_geometry: Geometry,
                     pointer_event: PointerEvent) -> DragDropOperation
```

x.on_drag_detected(my_geometry, pointer_event) -> DragDropOperation
Called when Slate detects that a widget started to be dragged.

Args:
    my_geometry (Geometry): 
    pointer_event (PointerEvent): MouseMove that triggered the drag

Returns:
    DragDropOperation: 

    operation (DragDropOperation): The drag operation that was detected.

<a id="unreal.UserWidget.on_drag_cancelled"></a>

#### on\_drag\_cancelled

```python
def on_drag_cancelled(pointer_event: PointerEvent,
                      operation: DragDropOperation) -> None
```

x.on_drag_cancelled(pointer_event, operation) -> None
Called when the user cancels the drag operation, typically when they simply release the mouse button after
beginning a drag operation, but failing to complete the drag.

Args:
    pointer_event (PointerEvent): Last mouse event from when the drag was canceled.
    operation (DragDropOperation): The drag operation that was canceled.

<a id="unreal.UserWidget.on_animation_started"></a>

#### on\_animation\_started

```python
def on_animation_started(animation: WidgetAnimation) -> None
```

x.on_animation_started(animation) -> None
Called when an animation is started.

Args:
    animation (WidgetAnimation): the animation that started

<a id="unreal.UserWidget.on_animation_finished"></a>

#### on\_animation\_finished

```python
def on_animation_finished(animation: WidgetAnimation) -> None
```

x.on_animation_finished(animation) -> None
Called when an animation has either played all the way through or is stopped

Args:
    animation (WidgetAnimation): The animation that has finished playing

<a id="unreal.UserWidget.on_analog_value_changed"></a>

#### on\_analog\_value\_changed

```python
def on_analog_value_changed(
        my_geometry: Geometry,
        analog_input_event: AnalogInputEvent) -> EventReply
```

x.on_analog_value_changed(my_geometry, analog_input_event) -> EventReply
Called when an analog value changes on a button that supports analog

Args:
    my_geometry (Geometry): The Geometry of the widget receiving the event
    analog_input_event (AnalogInputEvent): Analog Event

Returns:
    EventReply: Returns whether the event was handled, along with other possible actions

<a id="unreal.UserWidget.on_added_to_focus_path"></a>

#### on\_added\_to\_focus\_path

```python
def on_added_to_focus_path(focus_event: FocusEvent) -> None
```

x.on_added_to_focus_path(focus_event) -> None
If focus is gained on on this widget or on a child widget and this widget is added
to the focus path, and wasn't previously part of it, this event is called.

Args:
    focus_event (FocusEvent): FocusEvent

<a id="unreal.UserWidget.listen_for_input_action"></a>

#### listen\_for\_input\_action

```python
def listen_for_input_action(action_name: Name, event_type: InputEventType,
                            consume: bool, callback: OnInputAction) -> None
```

x.listen_for_input_action(action_name, event_type, consume, callback) -> None
Listens for a particular Player Input Action by name.  This requires that those actions are being executed, and
that we're not currently in UI-Only Input Mode.

Args:
    action_name (Name): 
    event_type (InputEventType): 
    consume (bool): 
    callback (OnInputAction):

<a id="unreal.UserWidget.is_playing_animation"></a>

#### is\_playing\_animation

```python
def is_playing_animation() -> bool
```

x.is_playing_animation() -> bool
Are we currently playing any animations?

Returns:
    bool:

<a id="unreal.UserWidget.is_listening_for_input_action"></a>

#### is\_listening\_for\_input\_action

```python
def is_listening_for_input_action(action_name: Name) -> bool
```

x.is_listening_for_input_action(action_name) -> bool
Checks if the action has a registered callback with the input component.

Args:
    action_name (Name): 

Returns:
    bool:

<a id="unreal.UserWidget.is_interactable"></a>

#### is\_interactable

```python
def is_interactable() -> bool
```

x.is_interactable() -> bool
Gets a value indicating if the widget is interactive.

Returns:
    bool:

<a id="unreal.UserWidget.is_any_animation_playing"></a>

#### is\_any\_animation\_playing

```python
def is_any_animation_playing() -> bool
```

x.is_any_animation_playing() -> bool


Returns:
    bool: True if any animation is currently playing

<a id="unreal.UserWidget.is_animation_playing_forward"></a>

#### is\_animation\_playing\_forward

```python
def is_animation_playing_forward(animation: WidgetAnimation) -> bool
```

x.is_animation_playing_forward(animation) -> bool
returns true if the animation is currently playing forward, false otherwise.

Args:
    animation (WidgetAnimation): The playing animation that we want to know about

Returns:
    bool:

<a id="unreal.UserWidget.is_animation_playing"></a>

#### is\_animation\_playing

```python
def is_animation_playing(animation: WidgetAnimation) -> bool
```

x.is_animation_playing(animation) -> bool
Gets whether an animation is currently playing on this widget.

Args:
    animation (WidgetAnimation): The animation to check the playback status of

Returns:
    bool: True if the animation is currently playing

<a id="unreal.UserWidget.get_owning_player_pawn"></a>

#### get\_owning\_player\_pawn

```python
def get_owning_player_pawn() -> Pawn
```

x.get_owning_player_pawn() -> Pawn
Gets the player pawn associated with this UI.

Returns:
    Pawn: Gets the owning player pawn that's owned by the player controller assigned to this widget.

<a id="unreal.UserWidget.get_owning_player_camera_manager"></a>

#### get\_owning\_player\_camera\_manager

```python
def get_owning_player_camera_manager() -> PlayerCameraManager
```

x.get_owning_player_camera_manager() -> PlayerCameraManager
Gets the player camera manager associated with this UI.

Returns:
    PlayerCameraManager: Gets the owning player camera manager that's owned by the player controller assigned to this widget.

<a id="unreal.UserWidget.get_is_visible"></a>

#### get\_is\_visible

```python
def get_is_visible() -> bool
```

x.get_is_visible() -> bool
Get Is Visible
deprecated: Use IsInViewport instead

Returns:
    bool:

<a id="unreal.UserWidget.get_extensions"></a>

#### get\_extensions

```python
def get_extensions(extension_type: Class) -> Array[UserWidgetExtension]
```

x.get_extensions(extension_type) -> Array[UserWidgetExtension]
Find the extensions of the requested type.

Args:
    extension_type (type(Class)): 

Returns:
    Array[UserWidgetExtension]:

<a id="unreal.UserWidget.get_extension"></a>

#### get\_extension

```python
def get_extension(extension_type: Class) -> UserWidgetExtension
```

x.get_extension(extension_type) -> UserWidgetExtension
Find the first extension of the requested type.

Args:
    extension_type (type(Class)): 

Returns:
    UserWidgetExtension:

<a id="unreal.UserWidget.get_animation_current_time"></a>

#### get\_animation\_current\_time

```python
def get_animation_current_time(animation: WidgetAnimation) -> float
```

x.get_animation_current_time(animation) -> float
Gets the current time of the animation in this widget

Args:
    animation (WidgetAnimation): 

Returns:
    float: the current time of the animation.

<a id="unreal.UserWidget.get_anchors_in_viewport"></a>

#### get\_anchors\_in\_viewport

```python
def get_anchors_in_viewport() -> Anchors
```

x.get_anchors_in_viewport() -> Anchors
Get Anchors in Viewport

Returns:
    Anchors:

<a id="unreal.UserWidget.get_alignment_in_viewport"></a>

#### get\_alignment\_in\_viewport

```python
def get_alignment_in_viewport() -> Vector2D
```

x.get_alignment_in_viewport() -> Vector2D
Get Alignment in Viewport

Returns:
    Vector2D:

<a id="unreal.UserWidget.flush_animations"></a>

#### flush\_animations

```python
def flush_animations() -> None
```

x.flush_animations() -> None
Flushes all animations on all widgets to guarantee that any queued updates are processed before this call returns

<a id="unreal.UserWidget.destruct"></a>

#### destruct

```python
def destruct() -> None
```

x.destruct() -> None
Called when a widget is no longer referenced causing the slate resource to destroyed.  Just like
Construct this event can be called multiple times.

<a id="unreal.UserWidget.construct"></a>

#### construct

```python
def construct() -> None
```

x.construct() -> None
Called after the underlying slate widget is constructed.  Depending on how the slate object is used
this event may be called multiple times due to adding and removing from the hierarchy.
If you need a true called-once-when-created event, use OnInitialized.

<a id="unreal.UserWidget.cancel_latent_actions"></a>

#### cancel\_latent\_actions

```python
def cancel_latent_actions() -> None
```

x.cancel_latent_actions() -> None
Cancels any pending Delays or timer callbacks for this widget.

<a id="unreal.UserWidget.bind_to_animation_started"></a>

#### bind\_to\_animation\_started

```python
def bind_to_animation_started(animation: WidgetAnimation,
                              delegate: WidgetAnimationDynamicEvent) -> None
```

x.bind_to_animation_started(animation, delegate) -> None
Bind an animation started delegate.

Args:
    animation (WidgetAnimation): the animation to listen for starting or finishing.
    delegate (WidgetAnimationDynamicEvent): the delegate to call when the animation's state changes

<a id="unreal.UserWidget.bind_to_animation_finished"></a>

#### bind\_to\_animation\_finished

```python
def bind_to_animation_finished(animation: WidgetAnimation,
                               delegate: WidgetAnimationDynamicEvent) -> None
```

x.bind_to_animation_finished(animation, delegate) -> None
Bind an animation finished delegate.

Args:
    animation (WidgetAnimation): the animation to listen for starting or finishing.
    delegate (WidgetAnimationDynamicEvent): the delegate to call when the animation's state changes

<a id="unreal.UserWidget.bind_to_animation_event"></a>

#### bind\_to\_animation\_event

```python
def bind_to_animation_event(animation: WidgetAnimation,
                            delegate: WidgetAnimationDynamicEvent,
                            animation_event: WidgetAnimationEvent,
                            user_tag: Name = "None") -> None
```

x.bind_to_animation_event(animation, delegate, animation_event, user_tag="None") -> None
Allows binding to a specific animation's event.

Args:
    animation (WidgetAnimation): the animation to listen for starting or finishing.
    delegate (WidgetAnimationDynamicEvent): the delegate to call when the animation's state changes
    animation_event (WidgetAnimationEvent): the event to watch for.
    user_tag (Name): Scopes the delegate to only be called when the animation completes with a specific tag set on it when it was played.

<a id="unreal.UserWidget.add_to_viewport"></a>

#### add\_to\_viewport

```python
def add_to_viewport(z_order: int = 0) -> None
```

x.add_to_viewport(z_order=0) -> None
Adds it to the game's viewport and fills the entire screen, unless SetDesiredSizeInViewport is called
to explicitly set the size.

Args:
    z_order (int32): The higher the number, the more on top this widget will be.

<a id="unreal.UserWidget.add_to_player_screen"></a>

#### add\_to\_player\_screen

```python
def add_to_player_screen(z_order: int = 0) -> bool
```

x.add_to_player_screen(z_order=0) -> bool
Adds the widget to the game's viewport in a section dedicated to the player.  This is valuable in a split screen
game where you need to only show a widget over a player's portion of the viewport.

Args:
    z_order (int32): The higher the number, the more on top this widget will be.

Returns:
    bool:

<a id="unreal.UserWidget.add_extension"></a>

#### add\_extension

```python
def add_extension(extension_type: Class) -> UserWidgetExtension
```

x.add_extension(extension_type) -> UserWidgetExtension
Add the extension of the requested type.

Args:
    extension_type (type(Class)): 

Returns:
    UserWidgetExtension:

<a id="unreal.VREditorBaseUserWidget"></a>