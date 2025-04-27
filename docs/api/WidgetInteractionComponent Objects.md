## WidgetInteractionComponent Objects

```python
class WidgetInteractionComponent(SceneComponent)
```

This is a component to allow interaction with the Widget Component.  This class allows you to
simulate a sort of laser pointer device, when it hovers over widgets it will send the basic signals
to show as if the mouse were moving on top of it.  You'll then tell the component to simulate key presses,
like Left Mouse, down and up, to simulate a mouse click.

**C++ Source:**

- **Module**: UMG
- **File**: WidgetInteractionComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``debug_color`` (LinearColor):  [Read-Write] Determines the color of the debug lines.
- ``debug_line_thickness`` (float):  [Read-Write] Determines the thickness of the debug lines.
- ``debug_sphere_line_thickness`` (float):  [Read-Write] Determines the line thickness of the debug sphere.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_hit_testing`` (bool):  [Read-Write] Should the interaction component perform hit testing (Automatic or Custom) and attempt to
  simulate hover - if you were going to emulate a keyboard you would want to turn this option off
  if the virtual keyboard was separate from the virtual pointer device and used a second interaction
  component.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``interaction_distance`` (float):  [Read-Write] The distance in game units the component should be able to interact with a widget component.
- ``interaction_source`` (WidgetInteractionSource):  [Read-Write] Should we project from the world location of the component?  If you set this to false, you'll
  need to call SetCustomHitResult(), and provide the result of a custom hit test form whatever
  location you wish.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_hovered_widget_changed`` (OnHoveredWidgetChanged):  [Read-Write] Called when the hovered Widget Component changes.  The interaction component functions at the Slate
  level - so it's unable to report anything about what UWidget is under the hit result.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``pointer_index`` (int32):  [Read-Write] Each user virtual controller or virtual finger tips being simulated should use a different pointer index.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``show_debug`` (bool):  [Read-Write] Shows some debugging lines and a hit sphere to help you debug interactions.
- ``trace_channel`` (CollisionChannel):  [Read-Write] The trace channel to use when tracing for widget components in the world.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``virtual_user_index`` (int32):  [Read-Write] Represents the Virtual User Index.  Each virtual user should be represented by a different
  index number, this will maintain separate capture and focus states for them.  Each
  controller or finger-tip should get a unique PointerIndex.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.WidgetInteractionComponent.on_hovered_widget_changed"></a>

#### on_hovered_widget_changed

```python
@property
def on_hovered_widget_changed() -> OnHoveredWidgetChanged
```

(OnHoveredWidgetChanged):  [Read-Write] Called when the hovered Widget Component changes.  The interaction component functions at the Slate
level - so it's unable to report anything about what UWidget is under the hit result.

<a id="unreal.WidgetInteractionComponent.on_hovered_widget_changed"></a>

#### on_hovered_widget_changed

```python
@on_hovered_widget_changed.setter
def on_hovered_widget_changed(value: OnHoveredWidgetChanged) -> None
```

<a id="unreal.WidgetInteractionComponent.virtual_user_index"></a>

#### virtual_user_index

```python
@property
def virtual_user_index() -> int
```

(int32):  [Read-Write] Represents the Virtual User Index.  Each virtual user should be represented by a different
index number, this will maintain separate capture and focus states for them.  Each
controller or finger-tip should get a unique PointerIndex.

<a id="unreal.WidgetInteractionComponent.virtual_user_index"></a>

#### virtual_user_index

```python
@virtual_user_index.setter
def virtual_user_index(value: int) -> None
```

<a id="unreal.WidgetInteractionComponent.pointer_index"></a>

#### pointer_index

```python
@property
def pointer_index() -> int
```

(int32):  [Read-Write] Each user virtual controller or virtual finger tips being simulated should use a different pointer index.

<a id="unreal.WidgetInteractionComponent.pointer_index"></a>

#### pointer_index

```python
@pointer_index.setter
def pointer_index(value: int) -> None
```

<a id="unreal.WidgetInteractionComponent.trace_channel"></a>

#### trace_channel

```python
@property
def trace_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write] The trace channel to use when tracing for widget components in the world.

<a id="unreal.WidgetInteractionComponent.trace_channel"></a>

#### trace_channel

```python
@trace_channel.setter
def trace_channel(value: CollisionChannel) -> None
```

<a id="unreal.WidgetInteractionComponent.interaction_distance"></a>

#### interaction_distance

```python
@property
def interaction_distance() -> float
```

(float):  [Read-Write] The distance in game units the component should be able to interact with a widget component.

<a id="unreal.WidgetInteractionComponent.interaction_distance"></a>

#### interaction_distance

```python
@interaction_distance.setter
def interaction_distance(value: float) -> None
```

<a id="unreal.WidgetInteractionComponent.interaction_source"></a>

#### interaction_source

```python
@property
def interaction_source() -> WidgetInteractionSource
```

(WidgetInteractionSource):  [Read-Write] Should we project from the world location of the component?  If you set this to false, you'll
need to call SetCustomHitResult(), and provide the result of a custom hit test form whatever
location you wish.

<a id="unreal.WidgetInteractionComponent.interaction_source"></a>

#### interaction_source

```python
@interaction_source.setter
def interaction_source(value: WidgetInteractionSource) -> None
```

<a id="unreal.WidgetInteractionComponent.enable_hit_testing"></a>

#### enable_hit_testing

```python
@property
def enable_hit_testing() -> bool
```

(bool):  [Read-Write] Should the interaction component perform hit testing (Automatic or Custom) and attempt to
simulate hover - if you were going to emulate a keyboard you would want to turn this option off
if the virtual keyboard was separate from the virtual pointer device and used a second interaction
component.

<a id="unreal.WidgetInteractionComponent.enable_hit_testing"></a>

#### enable_hit_testing

```python
@enable_hit_testing.setter
def enable_hit_testing(value: bool) -> None
```

<a id="unreal.WidgetInteractionComponent.show_debug"></a>

#### show_debug

```python
@property
def show_debug() -> bool
```

(bool):  [Read-Write] Shows some debugging lines and a hit sphere to help you debug interactions.

<a id="unreal.WidgetInteractionComponent.show_debug"></a>

#### show_debug

```python
@show_debug.setter
def show_debug(value: bool) -> None
```

<a id="unreal.WidgetInteractionComponent.debug_sphere_line_thickness"></a>

#### debug_sphere_line_thickness

```python
@property
def debug_sphere_line_thickness() -> float
```

(float):  [Read-Write] Determines the line thickness of the debug sphere.

<a id="unreal.WidgetInteractionComponent.debug_sphere_line_thickness"></a>

#### debug_sphere_line_thickness

```python
@debug_sphere_line_thickness.setter
def debug_sphere_line_thickness(value: float) -> None
```

<a id="unreal.WidgetInteractionComponent.debug_line_thickness"></a>

#### debug_line_thickness

```python
@property
def debug_line_thickness() -> float
```

(float):  [Read-Write] Determines the thickness of the debug lines.

<a id="unreal.WidgetInteractionComponent.debug_line_thickness"></a>

#### debug_line_thickness

```python
@debug_line_thickness.setter
def debug_line_thickness(value: float) -> None
```

<a id="unreal.WidgetInteractionComponent.debug_color"></a>

#### debug_color

```python
@property
def debug_color() -> LinearColor
```

(LinearColor):  [Read-Write] Determines the color of the debug lines.

<a id="unreal.WidgetInteractionComponent.debug_color"></a>

#### debug_color

```python
@debug_color.setter
def debug_color(value: LinearColor) -> None
```

<a id="unreal.WidgetInteractionComponent.set_focus"></a>

#### set_focus

```python
def set_focus(focus_widget: Widget) -> None
```

x.set_focus(focus_widget) -> None
Set the focus target of the virtual user managed by this component

Args:
    focus_widget (Widget):

<a id="unreal.WidgetInteractionComponent.set_custom_hit_result"></a>

#### set_custom_hit_result

```python
def set_custom_hit_result(hit_result: HitResult) -> None
```

x.set_custom_hit_result(hit_result) -> None
Set custom hit result.  This is only taken into account if InteractionSource is set to EWidgetInteractionSource::Custom.

Args:
    hit_result (HitResult):

<a id="unreal.WidgetInteractionComponent.send_key_char"></a>

#### send_key_char

```python
def send_key_char(characters: str, repeat: bool = False) -> bool
```

x.send_key_char(characters, repeat=False) -> bool
Transmits a list of characters to a widget by simulating a OnKeyChar event for each key listed in
the string.

Args:
    characters (str): 
    repeat (bool): 

Returns:
    bool:

<a id="unreal.WidgetInteractionComponent.scroll_wheel"></a>

#### scroll_wheel

```python
def scroll_wheel(scroll_delta: float) -> None
```

x.scroll_wheel(scroll_delta) -> None
Sends a scroll wheel event to the widget under the last hit result.

Args:
    scroll_delta (float):

<a id="unreal.WidgetInteractionComponent.release_pointer_key"></a>

#### release_pointer_key

```python
def release_pointer_key(key: Key) -> None
```

x.release_pointer_key(key) -> None
Releases a key as if the mouse/pointer were the source of it.  Normally you would just use
Left/Right mouse button for the Key.  However - advanced uses could also be imagined where you
send other keys to signal widgets to take special actions if they're under the cursor.

Args:
    key (Key):

<a id="unreal.WidgetInteractionComponent.release_key"></a>

#### release_key

```python
def release_key(key: Key) -> bool
```

x.release_key(key) -> bool
Releases a key as if it had been released by the keyboard.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.WidgetInteractionComponent.press_pointer_key"></a>

#### press_pointer_key

```python
def press_pointer_key(key: Key) -> None
```

x.press_pointer_key(key) -> None
Presses a key as if the mouse/pointer were the source of it.  Normally you would just use
Left/Right mouse button for the Key.  However - advanced uses could also be imagined where you
send other keys to signal widgets to take special actions if they're under the cursor.

Args:
    key (Key):

<a id="unreal.WidgetInteractionComponent.press_key"></a>

#### press_key

```python
def press_key(key: Key, repeat: bool = False) -> bool
```

x.press_key(key, repeat=False) -> bool
Press a key as if it had come from the keyboard.  Avoid using this for 'a-z|A-Z', things like
the Editable Textbox in Slate expect OnKeyChar to be called to signal a specific character being
send to the widget.  So for those cases you should use SendKeyChar.

Args:
    key (Key): 
    repeat (bool): 

Returns:
    bool:

<a id="unreal.WidgetInteractionComponent.press_and_release_key"></a>

#### press_and_release_key

```python
def press_and_release_key(key: Key) -> bool
```

x.press_and_release_key(key) -> bool
Does both the press and release of a simulated keyboard key.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.WidgetInteractionComponent.is_over_interactable_widget"></a>

#### is_over_interactable_widget

```python
def is_over_interactable_widget() -> bool
```

x.is_over_interactable_widget() -> bool
Returns true if a widget under the hit result is interactive.  e.g. Slate widgets
that return true for IsInteractable().

Returns:
    bool:

<a id="unreal.WidgetInteractionComponent.is_over_hit_test_visible_widget"></a>

#### is_over_hit_test_visible_widget

```python
def is_over_hit_test_visible_widget() -> bool
```

x.is_over_hit_test_visible_widget() -> bool
Returns true if a widget under the hit result is has a visibility that makes it hit test
visible.  e.g. Slate widgets that return true for GetVisibility().IsHitTestVisible().

Returns:
    bool:

<a id="unreal.WidgetInteractionComponent.is_over_focusable_widget"></a>

#### is_over_focusable_widget

```python
def is_over_focusable_widget() -> bool
```

x.is_over_focusable_widget() -> bool
Returns true if a widget under the hit result is focusable.  e.g. Slate widgets that
return true for SupportsKeyboardFocus().

Returns:
    bool:

<a id="unreal.WidgetInteractionComponent.get_last_hit_result"></a>

#### get_last_hit_result

```python
def get_last_hit_result() -> HitResult
```

x.get_last_hit_result() -> HitResult
Gets the last hit result generated by the component.  Returns the custom hit result if that was set.

Returns:
    HitResult:

<a id="unreal.WidgetInteractionComponent.get_hovered_widget_component"></a>

#### get_hovered_widget_component

```python
def get_hovered_widget_component() -> WidgetComponent
```

x.get_hovered_widget_component() -> WidgetComponent
Get the currently hovered widget component.

Returns:
    WidgetComponent:

<a id="unreal.WidgetInteractionComponent.get2d_hit_location"></a>

#### get2d_hit_location

```python
def get2d_hit_location() -> Vector2D
```

x.get2d_hit_location() -> Vector2D
Gets the last hit location on the widget in 2D, local pixel units of the render target.

Returns:
    Vector2D:

<a id="unreal.WidgetSwitcher"></a>