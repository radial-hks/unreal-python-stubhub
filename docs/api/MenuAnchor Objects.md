## MenuAnchor Objects

```python
class MenuAnchor(ContentWidget)
```

The Menu Anchor allows you to specify an location that a popup menu should be anchored to,
and should be summoned from.
* Single Child
* Popup

**C++ Source:**

- **Module**: UMG
- **File**: MenuAnchor.h

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
- ``menu_class`` (type(Class)):  [Read-Write] The widget class to spawn when the menu is required.  Creates the widget freshly each time.
  If you want to customize the creation of the popup, you should bind a function to OnGetMenuContentEvent
  instead.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_get_menu_content_event`` (GetWidget):  [Read-Write]
- ``on_get_user_menu_content_event`` (GetUserWidget):  [Read-Write] Called when the menu content is requested to allow a more customized handling over what to display
- ``on_menu_open_changed`` (OnMenuOpenChangedEvent):  [Read-Write] Called when the opened state of the menu changes
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``placement`` (MenuPlacement):  [Read-Write] The placement location of the summoned widget.
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``should_defer_painting_after_window_content`` (bool):  [Read-Write]
- ``should_fit_in_window`` (bool):  [Read-Write] Should the menu anchor attempt to fit the menu inside the window.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``use_application_menu_stack`` (bool):  [Read-Write] Does this menu behave like a normal stacked menu? Set it to false to control the menu's lifetime yourself.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.MenuAnchor.menu_class"></a>

#### menu_class

```python
@property
def menu_class() -> Class
```

(type(Class)):  [Read-Only] The widget class to spawn when the menu is required.  Creates the widget freshly each time.
If you want to customize the creation of the popup, you should bind a function to OnGetMenuContentEvent
instead.

<a id="unreal.MenuAnchor.placement"></a>

#### placement

```python
@property
def placement() -> MenuPlacement
```

(MenuPlacement):  [Read-Write] The placement location of the summoned widget.

<a id="unreal.MenuAnchor.placement"></a>

#### placement

```python
@placement.setter
def placement(value: MenuPlacement) -> None
```

<a id="unreal.MenuAnchor.should_fit_in_window"></a>

#### should_fit_in_window

```python
@property
def should_fit_in_window() -> bool
```

(bool):  [Read-Write] Should the menu anchor attempt to fit the menu inside the window.

<a id="unreal.MenuAnchor.should_fit_in_window"></a>

#### should_fit_in_window

```python
@should_fit_in_window.setter
def should_fit_in_window(value: bool) -> None
```

<a id="unreal.MenuAnchor.should_defer_painting_after_window_content"></a>

#### should_defer_painting_after_window_content

```python
@property
def should_defer_painting_after_window_content() -> bool
```

(bool):  [Read-Only]

<a id="unreal.MenuAnchor.use_application_menu_stack"></a>

#### use_application_menu_stack

```python
@property
def use_application_menu_stack() -> bool
```

(bool):  [Read-Only] Does this menu behave like a normal stacked menu? Set it to false to control the menu's lifetime yourself.

<a id="unreal.MenuAnchor.on_menu_open_changed"></a>

#### on_menu_open_changed

```python
@property
def on_menu_open_changed() -> OnMenuOpenChangedEvent
```

(OnMenuOpenChangedEvent):  [Read-Write] Called when the opened state of the menu changes

<a id="unreal.MenuAnchor.on_menu_open_changed"></a>

#### on_menu_open_changed

```python
@on_menu_open_changed.setter
def on_menu_open_changed(value: OnMenuOpenChangedEvent) -> None
```

<a id="unreal.MenuAnchor.toggle_open"></a>

#### toggle_open

```python
def toggle_open(focus_on_open: bool) -> None
```

x.toggle_open(focus_on_open) -> None
Toggles the menus open state.

Args:
    focus_on_open (bool): Should we focus the popup as soon as it opens?

<a id="unreal.MenuAnchor.should_open_due_to_click"></a>

#### should_open_due_to_click

```python
def should_open_due_to_click() -> bool
```

x.should_open_due_to_click() -> bool
Returns true if we should open the menu due to a click. Sometimes we should not, if
the same MouseDownEvent that just closed the menu is about to re-open it because it
happens to land on the button.

Returns:
    bool:

<a id="unreal.MenuAnchor.set_placement"></a>

#### set_placement

```python
def set_placement(placement: MenuPlacement) -> None
```

x.set_placement(placement) -> None
TODO UMG Add Set MenuClass

Args:
    placement (MenuPlacement):

<a id="unreal.MenuAnchor.open"></a>

#### open

```python
def open(focus_menu: bool) -> None
```

x.open(focus_menu) -> None
Opens the menu if it is not already open

Args:
    focus_menu (bool):

<a id="unreal.MenuAnchor.is_open"></a>

#### is_open

```python
def is_open() -> bool
```

x.is_open() -> bool
Returns true if the popup is open; false otherwise.

Returns:
    bool:

<a id="unreal.MenuAnchor.has_open_sub_menus"></a>

#### has_open_sub_menus

```python
def has_open_sub_menus() -> bool
```

x.has_open_sub_menus() -> bool
Returns whether this menu has open submenus

Returns:
    bool:

<a id="unreal.MenuAnchor.get_menu_position"></a>

#### get_menu_position

```python
def get_menu_position() -> Vector2D
```

x.get_menu_position() -> Vector2D
Returns the current menu position

Returns:
    Vector2D:

<a id="unreal.MenuAnchor.fit_in_window"></a>

#### fit_in_window

```python
def fit_in_window(fit: bool) -> None
```

x.fit_in_window(fit) -> None
Fit in Window

Args:
    fit (bool):

<a id="unreal.MenuAnchor.close"></a>

#### close

```python
def close() -> None
```

x.close() -> None
Closes the menu if it is currently open.

<a id="unreal.TextLayoutWidget"></a>