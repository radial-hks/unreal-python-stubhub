## Widget Objects

```python
class Widget(Visual)
```

This is the base class for all wrapped Slate controls that are exposed to UObjects.

**C++ Source:**

- **Module**: UMG
- **File**: Widget.h

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
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.Widget.slot"></a>

#### slot

```python
@property
def slot() -> PanelSlot
```

(PanelSlot):  [Read-Only] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.

<a id="unreal.Widget.tool_tip_text"></a>

#### tool_tip_text

```python
@property
def tool_tip_text() -> Text
```

(Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse

<a id="unreal.Widget.tool_tip_text"></a>

#### tool_tip_text

```python
@tool_tip_text.setter
def tool_tip_text(value: Text) -> None
```

<a id="unreal.Widget.tool_tip_widget"></a>

#### tool_tip_widget

```python
@property
def tool_tip_widget() -> Widget
```

(Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse

<a id="unreal.Widget.render_transform"></a>

#### render_transform

```python
@property
def render_transform() -> WidgetTransform
```

(WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.

<a id="unreal.Widget.render_transform"></a>

#### render_transform

```python
@render_transform.setter
def render_transform(value: WidgetTransform) -> None
```

<a id="unreal.Widget.render_transform_pivot"></a>

#### render_transform_pivot

```python
@property
def render_transform_pivot() -> Vector2D
```

(Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
This value is a normalized coordinate about which things like rotations will occur.

<a id="unreal.Widget.render_transform_pivot"></a>

#### render_transform_pivot

```python
@render_transform_pivot.setter
def render_transform_pivot(value: Vector2D) -> None
```

<a id="unreal.Widget.flow_direction_preference"></a>

#### flow_direction_preference

```python
@property
def flow_direction_preference() -> FlowDirectionPreference
```

(FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction

<a id="unreal.Widget.flow_direction_preference"></a>

#### flow_direction_preference

```python
@flow_direction_preference.setter
def flow_direction_preference(value: FlowDirectionPreference) -> None
```

<a id="unreal.Widget.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Write] Sets whether this widget can be modified interactively by the user

<a id="unreal.Widget.is_enabled"></a>

#### is_enabled

```python
@is_enabled.setter
def is_enabled(value: bool) -> None
```

<a id="unreal.Widget.is_volatile"></a>

#### is_volatile

```python
@property
def is_volatile() -> bool
```

(bool):  [Read-Only] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
instead of invalidating it every frame, which would prevent the invalidation panel from actually
ever caching anything.

<a id="unreal.Widget.cursor"></a>

#### cursor

```python
@property
def cursor() -> MouseCursor
```

(MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget

<a id="unreal.Widget.cursor"></a>

#### cursor

```python
@cursor.setter
def cursor(value: MouseCursor) -> None
```

<a id="unreal.Widget.clipping"></a>

#### clipping

```python
@property
def clipping() -> WidgetClipping
```

(WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
from being seen.

NOTE: Elements in different clipping spaces can not be batched together, and so there is a
performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
content from showing up outside its bounds.

<a id="unreal.Widget.clipping"></a>

#### clipping

```python
@clipping.setter
def clipping(value: WidgetClipping) -> None
```

<a id="unreal.Widget.clip_to_bounds"></a>

#### clip_to_bounds

```python
@property
def clip_to_bounds() -> WidgetClipping
```

deprecated: 'clip_to_bounds' was renamed to 'clipping'.

<a id="unreal.Widget.clip_to_bounds"></a>

#### clip_to_bounds

```python
@clip_to_bounds.setter
def clip_to_bounds(value: WidgetClipping) -> None
```

<a id="unreal.Widget.visibility"></a>

#### visibility

```python
@property
def visibility() -> SlateVisibility
```

(SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.Widget.visibility"></a>

#### visibility

```python
@visibility.setter
def visibility(value: SlateVisibility) -> None
```

<a id="unreal.Widget.visiblity"></a>

#### visiblity

```python
@property
def visiblity() -> SlateVisibility
```

deprecated: 'visiblity' was renamed to 'visibility'.

<a id="unreal.Widget.visiblity"></a>

#### visiblity

```python
@visiblity.setter
def visiblity(value: SlateVisibility) -> None
```

<a id="unreal.Widget.pixel_snapping"></a>

#### pixel_snapping

```python
@property
def pixel_snapping() -> WidgetPixelSnapping
```

(WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation

<a id="unreal.Widget.pixel_snapping"></a>

#### pixel_snapping

```python
@pixel_snapping.setter
def pixel_snapping(value: WidgetPixelSnapping) -> None
```

<a id="unreal.Widget.render_opacity"></a>

#### render_opacity

```python
@property
def render_opacity() -> float
```

(float):  [Read-Write] The opacity of the widget

<a id="unreal.Widget.render_opacity"></a>

#### render_opacity

```python
@render_opacity.setter
def render_opacity(value: float) -> None
```

<a id="unreal.Widget.opacity"></a>

#### opacity

```python
@property
def opacity() -> float
```

deprecated: 'opacity' was renamed to 'render_opacity'.

<a id="unreal.Widget.opacity"></a>

#### opacity

```python
@opacity.setter
def opacity(value: float) -> None
```

<a id="unreal.Widget.navigation"></a>

#### navigation

```python
@property
def navigation() -> WidgetNavigation
```

(WidgetNavigation):  [Read-Only] The navigation object for this widget is optionally created if the user has configured custom
navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
can occur between widgets.

<a id="unreal.Widget.set_visibility"></a>

#### set_visibility

```python
def set_visibility(visibility: SlateVisibility) -> None
```

x.set_visibility(visibility) -> None
Sets the visibility of the widget.

Args:
    visibility (SlateVisibility):

<a id="unreal.Widget.set_user_focus"></a>

#### set_user_focus

```python
def set_user_focus(player_controller: PlayerController) -> None
```

x.set_user_focus(player_controller) -> None
Sets the focus to this widget for a specific user (if setting focus for the owning user, prefer SetFocus())

Args:
    player_controller (PlayerController):

<a id="unreal.Widget.set_tool_tip_text"></a>

#### set_tool_tip_text

```python
def set_tool_tip_text(tool_tip_text: Text) -> None
```

x.set_tool_tip_text(tool_tip_text) -> None
Sets the tooltip text for the widget.

Args:
    tool_tip_text (Text):

<a id="unreal.Widget.set_tool_tip"></a>

#### set_tool_tip

```python
def set_tool_tip(widget: Widget) -> None
```

x.set_tool_tip(widget) -> None
Sets a custom widget as the tooltip of the widget.

Args:
    widget (Widget):

<a id="unreal.Widget.set_render_translation"></a>

#### set_render_translation

```python
def set_render_translation(translation: Vector2D) -> None
```

x.set_render_translation(translation) -> None
Set Render Translation

Args:
    translation (Vector2D):

<a id="unreal.Widget.set_render_transform_pivot"></a>

#### set_render_transform_pivot

```python
def set_render_transform_pivot(pivot: Vector2D) -> None
```

x.set_render_transform_pivot(pivot) -> None
Set Render Transform Pivot

Args:
    pivot (Vector2D):

<a id="unreal.Widget.set_render_transform_angle"></a>

#### set_render_transform_angle

```python
def set_render_transform_angle(angle: float) -> None
```

x.set_render_transform_angle(angle) -> None
Set Render Transform Angle

Args:
    angle (float):

<a id="unreal.Widget.set_render_angle"></a>

#### set_render_angle

```python
def set_render_angle(angle: float) -> None
```

deprecated: 'set_render_angle' was renamed to 'set_render_transform_angle'.

<a id="unreal.Widget.set_render_transform"></a>

#### set_render_transform

```python
def set_render_transform(transform: WidgetTransform) -> None
```

x.set_render_transform(transform) -> None
Set Render Transform

Args:
    transform (WidgetTransform):

<a id="unreal.Widget.set_render_shear"></a>

#### set_render_shear

```python
def set_render_shear(shear: Vector2D) -> None
```

x.set_render_shear(shear) -> None
Set Render Shear

Args:
    shear (Vector2D):

<a id="unreal.Widget.set_render_scale"></a>

#### set_render_scale

```python
def set_render_scale(scale: Vector2D) -> None
```

x.set_render_scale(scale) -> None
Set Render Scale

Args:
    scale (Vector2D):

<a id="unreal.Widget.set_render_opacity"></a>

#### set_render_opacity

```python
def set_render_opacity(opacity: float) -> None
```

x.set_render_opacity(opacity) -> None
Sets the visibility of the widget.

Args:
    opacity (float):

<a id="unreal.Widget.set_opacity"></a>

#### set_opacity

```python
def set_opacity(opacity: float) -> None
```

deprecated: 'set_opacity' was renamed to 'set_render_opacity'.

<a id="unreal.Widget.set_navigation_rule_explicit"></a>

#### set_navigation_rule_explicit

```python
def set_navigation_rule_explicit(direction: UINavigation,
                                 widget: Widget) -> None
```

x.set_navigation_rule_explicit(direction, widget) -> None
Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree. This works only for Explicit Rule.

Args:
    direction (UINavigation): 
    widget (Widget): Focus on this widget instance

<a id="unreal.Widget.set_navigation_rule_custom_boundary"></a>

#### set_navigation_rule_custom_boundary

```python
def set_navigation_rule_custom_boundary(
        direction: UINavigation,
        custom_delegate: CustomWidgetNavigationDelegate) -> None
```

x.set_navigation_rule_custom_boundary(direction, custom_delegate) -> None
Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree. This works only for CustomBoundary Rule.

Args:
    direction (UINavigation): 
    custom_delegate (CustomWidgetNavigationDelegate): Custom Delegate that will be called

<a id="unreal.Widget.set_navigation_rule_custom"></a>

#### set_navigation_rule_custom

```python
def set_navigation_rule_custom(
        direction: UINavigation,
        custom_delegate: CustomWidgetNavigationDelegate) -> None
```

x.set_navigation_rule_custom(direction, custom_delegate) -> None
Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree. This works only for Custom Rule.

Args:
    direction (UINavigation): 
    custom_delegate (CustomWidgetNavigationDelegate): Custom Delegate that will be called

<a id="unreal.Widget.set_navigation_rule_base"></a>

#### set_navigation_rule_base

```python
def set_navigation_rule_base(direction: UINavigation,
                             rule: UINavigationRule) -> None
```

x.set_navigation_rule_base(direction, rule) -> None
Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree. This works only for non Explicit, non Custom and non CustomBoundary Rules.

Args:
    direction (UINavigation): 
    rule (UINavigationRule): The rule to use when navigation is taking place

<a id="unreal.Widget.set_navigation_rule"></a>

#### set_navigation_rule

```python
def set_navigation_rule(direction: UINavigation, rule: UINavigationRule,
                        widget_to_focus: Name) -> None
```

x.set_navigation_rule(direction, rule, widget_to_focus) -> None
Set Navigation Rule
deprecated: Function 'SetNavigationRule' is deprecated.

Args:
    direction (UINavigation): 
    rule (UINavigationRule): 
    widget_to_focus (Name):

<a id="unreal.Widget.set_keyboard_focus"></a>

#### set_keyboard_focus

```python
def set_keyboard_focus() -> None
```

x.set_keyboard_focus() -> None
Sets the focus to this widget.

<a id="unreal.Widget.set_is_enabled"></a>

#### set_is_enabled

```python
def set_is_enabled(is_enabled: bool) -> None
```

x.set_is_enabled(is_enabled) -> None
Sets the current enabled status of the widget

Args:
    is_enabled (bool):

<a id="unreal.Widget.set_focus"></a>

#### set_focus

```python
def set_focus() -> None
```

x.set_focus() -> None
Sets the focus to this widget for the owning user

<a id="unreal.Widget.set_cursor"></a>

#### set_cursor

```python
def set_cursor(cursor: MouseCursor) -> None
```

x.set_cursor(cursor) -> None
Sets the cursor to show over the widget.

Args:
    cursor (MouseCursor):

<a id="unreal.Widget.set_clipping"></a>

#### set_clipping

```python
def set_clipping(clipping: WidgetClipping) -> None
```

x.set_clipping(clipping) -> None
Sets the clipping state of this widget.

Args:
    clipping (WidgetClipping):

<a id="unreal.Widget.set_all_navigation_rules"></a>

#### set_all_navigation_rules

```python
def set_all_navigation_rules(rule: UINavigationRule,
                             widget_to_focus: Name) -> None
```

x.set_all_navigation_rules(rule, widget_to_focus) -> None
Sets the widget navigation rules for all directions. This can only be called on widgets that are in a widget tree.

Args:
    rule (UINavigationRule): The rule to use when navigation is taking place
    widget_to_focus (Name): When using the Explicit rule, focus on this widget

<a id="unreal.Widget.reset_cursor"></a>

#### reset_cursor

```python
def reset_cursor() -> None
```

x.reset_cursor() -> None
Resets the cursor to use on the widget, removing any customization for it.

<a id="unreal.Widget.remove_from_parent"></a>

#### remove_from_parent

```python
def remove_from_parent() -> None
```

x.remove_from_parent() -> None
Removes the widget from its parent widget.  If this widget was added to the player's screen or the viewport
it will also be removed from those containers.

<a id="unreal.Widget.remove_field_value_changed_delegate"></a>

#### remove_field_value_changed_delegate

```python
def remove_field_value_changed_delegate(
        field_id: FieldNotificationId,
        delegate: FieldValueChangedDynamicDelegate) -> None
```

x.remove_field_value_changed_delegate(field_id, delegate) -> None
K2 Remove Field Value Changed Delegate

Args:
    field_id (FieldNotificationId): 
    delegate (FieldValueChangedDynamicDelegate):

<a id="unreal.Widget.broadcast_field_value_changed"></a>

#### broadcast_field_value_changed

```python
def broadcast_field_value_changed(field_id: FieldNotificationId) -> None
```

x.broadcast_field_value_changed(field_id) -> None
K2 Broadcast Field Value Changed

Args:
    field_id (FieldNotificationId):

<a id="unreal.Widget.add_field_value_changed_delegate"></a>

#### add_field_value_changed_delegate

```python
def add_field_value_changed_delegate(
        field_id: FieldNotificationId,
        delegate: FieldValueChangedDynamicDelegate) -> None
```

x.add_field_value_changed_delegate(field_id, delegate) -> None
K2 Add Field Value Changed Delegate

Args:
    field_id (FieldNotificationId): 
    delegate (FieldValueChangedDynamicDelegate):

<a id="unreal.Widget.is_visible"></a>

#### is_visible

```python
def is_visible() -> bool
```

x.is_visible() -> bool
Returns true if the widget is Visible, HitTestInvisible or SelfHitTestInvisible.

Returns:
    bool:

<a id="unreal.Widget.is_rendered"></a>

#### is_rendered

```python
def is_rendered() -> bool
```

x.is_rendered() -> bool
Returns true if the widget is Visible, HitTestInvisible or SelfHitTestInvisible and the Render Opacity is greater than 0.

Returns:
    bool:

<a id="unreal.Widget.is_in_viewport"></a>

#### is_in_viewport

```python
def is_in_viewport() -> bool
```

x.is_in_viewport() -> bool


Returns:
    bool: true if the widget was added to the viewport using AddToViewport or AddToPlayerScreen.

<a id="unreal.Widget.is_hovered"></a>

#### is_hovered

```python
def is_hovered() -> bool
```

x.is_hovered() -> bool
Returns true if the widget is currently being hovered by a pointer device

Returns:
    bool:

<a id="unreal.Widget.invalidate_layout_and_volatility"></a>

#### invalidate_layout_and_volatility

```python
def invalidate_layout_and_volatility() -> None
```

x.invalidate_layout_and_volatility() -> None
Invalidates the widget from the view of a layout caching widget that may own this widget.
will force the owning widget to redraw and cache children on the next paint pass.

<a id="unreal.Widget.has_user_focused_descendants"></a>

#### has_user_focused_descendants

```python
def has_user_focused_descendants(player_controller: PlayerController) -> bool
```

x.has_user_focused_descendants(player_controller) -> bool
Returns true if any descendant widget is focused by a specific user.

Args:
    player_controller (PlayerController): 

Returns:
    bool:

<a id="unreal.Widget.has_user_focus"></a>

#### has_user_focus

```python
def has_user_focus(player_controller: PlayerController) -> bool
```

x.has_user_focus(player_controller) -> bool
Returns true if this widget is focused by a specific user.

Args:
    player_controller (PlayerController): 

Returns:
    bool:

<a id="unreal.Widget.has_mouse_capture_by_user"></a>

#### has_mouse_capture_by_user

```python
def has_mouse_capture_by_user(user_index: int,
                              pointer_index: int = -1) -> bool
```

x.has_mouse_capture_by_user(user_index, pointer_index=-1) -> bool
Checks to see if this widget is the current mouse captor

Args:
    user_index (int32): 
    pointer_index (int32): 

Returns:
    bool: True if this widget has captured the mouse with given user and pointer

<a id="unreal.Widget.has_mouse_capture"></a>

#### has_mouse_capture

```python
def has_mouse_capture() -> bool
```

x.has_mouse_capture() -> bool
Checks to see if this widget is the current mouse captor

Returns:
    bool: True if this widget has captured the mouse

<a id="unreal.Widget.has_keyboard_focus"></a>

#### has_keyboard_focus

```python
def has_keyboard_focus() -> bool
```

x.has_keyboard_focus() -> bool
Checks to see if this widget currently has the keyboard focus

Returns:
    bool: True if this widget has keyboard focus

<a id="unreal.Widget.has_focused_descendants"></a>

#### has_focused_descendants

```python
def has_focused_descendants() -> bool
```

x.has_focused_descendants() -> bool
Returns true if any descendant widget is focused by any user.

Returns:
    bool:

<a id="unreal.Widget.has_any_user_focus"></a>

#### has_any_user_focus

```python
def has_any_user_focus() -> bool
```

x.has_any_user_focus() -> bool
Returns true if this widget is focused by any user.

Returns:
    bool:

<a id="unreal.Widget.get_visibility"></a>

#### get_visibility

```python
def get_visibility() -> SlateVisibility
```

x.get_visibility() -> SlateVisibility
Gets the current visibility of the widget.

Returns:
    SlateVisibility:

<a id="unreal.Widget.get_tick_space_geometry"></a>

#### get_tick_space_geometry

```python
def get_tick_space_geometry() -> Geometry
```

x.get_tick_space_geometry() -> Geometry
Get Tick Space Geometry

Returns:
    Geometry:

<a id="unreal.Widget.get_render_transform_angle"></a>

#### get_render_transform_angle

```python
def get_render_transform_angle() -> float
```

x.get_render_transform_angle() -> float
Get Render Transform Angle

Returns:
    float:

<a id="unreal.Widget.get_render_opacity"></a>

#### get_render_opacity

```python
def get_render_opacity() -> float
```

x.get_render_opacity() -> float
Gets the current visibility of the widget.

Returns:
    float:

<a id="unreal.Widget.get_opacity"></a>

#### get_opacity

```python
def get_opacity() -> float
```

deprecated: 'get_opacity' was renamed to 'get_render_opacity'.

<a id="unreal.Widget.get_parent"></a>

#### get_parent

```python
def get_parent() -> PanelWidget
```

x.get_parent() -> PanelWidget
Gets the parent widget

Returns:
    PanelWidget:

<a id="unreal.Widget.get_paint_space_geometry"></a>

#### get_paint_space_geometry

```python
def get_paint_space_geometry() -> Geometry
```

x.get_paint_space_geometry() -> Geometry
Get Paint Space Geometry

Returns:
    Geometry:

<a id="unreal.Widget.get_owning_player"></a>

#### get_owning_player

```python
def get_owning_player() -> PlayerController
```

x.get_owning_player() -> PlayerController
Gets the player controller associated with this UI.

Returns:
    PlayerController: The player controller that owns the UI.

<a id="unreal.Widget.get_owning_local_player"></a>

#### get_owning_local_player

```python
def get_owning_local_player() -> LocalPlayer
```

x.get_owning_local_player() -> LocalPlayer
Gets the local player associated with this UI.

Returns:
    LocalPlayer: The owning local player.

<a id="unreal.Widget.get_is_enabled"></a>

#### get_is_enabled

```python
def get_is_enabled() -> bool
```

x.get_is_enabled() -> bool
Gets the current enabled status of the widget

Returns:
    bool:

<a id="unreal.Widget.get_game_instance"></a>

#### get_game_instance

```python
def get_game_instance() -> GameInstance
```

x.get_game_instance() -> GameInstance
Gets the game instance associated with this UI.

Returns:
    GameInstance: a pointer to the owning game instance

<a id="unreal.Widget.get_desired_size"></a>

#### get_desired_size

```python
def get_desired_size() -> Vector2D
```

x.get_desired_size() -> Vector2D
Gets the widgets desired size.
NOTE: The underlying Slate widget must exist and be valid, also at least one pre-pass must
      have occurred before this value will be of any use.

Returns:
    Vector2D: The widget's desired size

<a id="unreal.Widget.get_clipping"></a>

#### get_clipping

```python
def get_clipping() -> WidgetClipping
```

x.get_clipping() -> WidgetClipping
Gets the clipping state of this widget.

Returns:
    WidgetClipping:

<a id="unreal.Widget.get_cached_geometry"></a>

#### get_cached_geometry

```python
def get_cached_geometry() -> Geometry
```

x.get_cached_geometry() -> Geometry
Gets the last geometry used to Tick the widget.  This data may not exist yet if this call happens prior to
the widget having been ticked/painted, or it may be out of date, or a frame behind.

We recommend not to use this data unless there's no other way to solve your problem.  Normally in Slate we
try and handle these issues by making a dependent widget part of the hierarchy, as to avoid frame behind
or what are referred to as hysteresis problems, both caused by depending on geometry from the previous frame
being used to advise how to layout a dependent object the current frame.

Returns:
    Geometry:

<a id="unreal.Widget.get_accessible_text"></a>

#### get_accessible_text

```python
def get_accessible_text() -> Text
```

x.get_accessible_text() -> Text
Gets the accessible text from the underlying Slate accessible widget

Returns:
    Text: The accessible text of the underlying Slate accessible widget. Returns an empty text if accessibility is dsabled or the underlying accessible widget is invalid.

<a id="unreal.Widget.get_accessible_summary_text"></a>

#### get_accessible_summary_text

```python
def get_accessible_summary_text() -> Text
```

x.get_accessible_summary_text() -> Text
Gets the accessible summary text from the underlying Slate accessible widget.

Returns:
    Text: The accessible summary text of the underlying Slate accessible widget. Returns an empty text if accessibility is dsabled or the underlying accessible widget is invalid.

<a id="unreal.Widget.force_volatile"></a>

#### force_volatile

```python
def force_volatile(force: bool) -> None
```

x.force_volatile(force) -> None
Sets the forced volatility of the widget.

Args:
    force (bool):

<a id="unreal.Widget.force_layout_prepass"></a>

#### force_layout_prepass

```python
def force_layout_prepass() -> None
```

x.force_layout_prepass() -> None
Forces a pre-pass.  A pre-pass caches the desired size of the widget hierarchy owned by this widget.
One pre-pass already happens for every widget before Tick occurs.  You only need to perform another
pre-pass if you are adding child widgets this frame and want them to immediately be visible this frame.

<a id="unreal.UserWidget"></a>