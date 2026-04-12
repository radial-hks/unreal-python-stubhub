## WindowWidgetBase Objects

```python
class WindowWidgetBase(CoveringWidgetBase)
```

Window Widget Base

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: WindowWidgetBase.h

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
- ``parent_visble2d_atom`` (Visible2DAtom):  [Read-Write]
- ``parent_widget_class`` (Class):  [Read-Write]
- ``parent_widget_component`` (CoveringWidgetComponent):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``preview_background`` (Texture2D):  [Read-Write] A preview background that you can use when designing the UI to get a sense of scale on the screen.  Use
  a texture with a screenshot of your game in it, for example if you were designing a HUD.
- ``priority`` (int32):  [Read-Write]
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``set_visible`` (bool):  [Read-Write]
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``stop_action`` (bool):  [Read-Write]
- ``tick_frequency`` (WidgetTickFrequency):  [Read-Write] This widget is allowed to tick. If this is unchecked tick will never be called, animations will not play correctly, and latent actions will not execute.
  Uncheck this for performance reasons only
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``visible`` (bool):  [Read-Write]
- ``visible2d_atom`` (Visible2DAtom):  [Read-Write]

<a id="unreal.WindowWidgetBase.parent_widget_component"></a>

#### parent\_widget\_component

```python
@property
def parent_widget_component() -> CoveringWidgetComponent
```

(CoveringWidgetComponent):  [Read-Write]

<a id="unreal.WindowWidgetBase.parent_widget_component"></a>

#### parent\_widget\_component

```python
@parent_widget_component.setter
def parent_widget_component(value: CoveringWidgetComponent) -> None
```

<a id="unreal.WindowWidgetBase.parent_widget_class"></a>

#### parent\_widget\_class

```python
@property
def parent_widget_class() -> Class
```

(Class):  [Read-Write]

<a id="unreal.WindowWidgetBase.parent_widget_class"></a>

#### parent\_widget\_class

```python
@parent_widget_class.setter
def parent_widget_class(value: Class) -> None
```

<a id="unreal.WindowWidgetBase.parent_visble2d_atom"></a>

#### parent\_visble2d\_atom

```python
@property
def parent_visble2d_atom() -> Visible2DAtom
```

(Visible2DAtom):  [Read-Write]

<a id="unreal.WindowWidgetBase.parent_visble2d_atom"></a>

#### parent\_visble2d\_atom

```python
@parent_visble2d_atom.setter
def parent_visble2d_atom(value: Visible2DAtom) -> None
```

<a id="unreal.WindowWidgetBase.visible2d_atom"></a>

#### visible2d\_atom

```python
@property
def visible2d_atom() -> Visible2DAtom
```

(Visible2DAtom):  [Read-Write]

<a id="unreal.WindowWidgetBase.visible2d_atom"></a>

#### visible2d\_atom

```python
@visible2d_atom.setter
def visible2d_atom(value: Visible2DAtom) -> None
```

<a id="unreal.WindowWidgetBase.set_visible"></a>

#### set\_visible

```python
@property
def set_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WindowWidgetBase.set_visible"></a>

#### set\_visible

```python
@set_visible.setter
def set_visible(value: bool) -> None
```

<a id="unreal.WindowWidgetBase.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WindowWidgetBase.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.WindowWidgetBase.show_hide_window"></a>

#### show\_hide\_window

```python
def show_hide_window(show: bool) -> None
```

x.show_hide_window(show) -> None
Show Hide Window

Args:
    show (bool):

<a id="unreal.WindowWidgetBase.set_window_entity_actor"></a>

#### set\_window\_entity\_actor

```python
def set_window_entity_actor(p_entity: WindowEntity) -> None
```

x.set_window_entity_actor(p_entity) -> None
Set Window Entity Actor

Args:
    p_entity (WindowEntity):

<a id="unreal.WindowWidgetBase.set_url"></a>

#### set\_url

```python
def set_url(new_url: str) -> bool
```

x.set_url(new_url) -> bool
Set Url

Args:
    new_url (str): 

Returns:
    bool:

<a id="unreal.WindowWidgetBase.set_size"></a>

#### set\_size

```python
def set_size(new_size: Vector2D) -> bool
```

x.set_size(new_size) -> bool
Set Size

Args:
    new_size (Vector2D): 

Returns:
    bool:

<a id="unreal.WindowWidgetBase.set_point"></a>

#### set\_point

```python
def set_point(point: Vector) -> bool
```

x.set_point(point) -> bool
Set Point

Args:
    point (Vector): 

Returns:
    bool:

<a id="unreal.WindowWidgetBase.set_offset"></a>

#### set\_offset

```python
def set_offset(new_offset: Vector2D) -> bool
```

x.set_offset(new_offset) -> bool
Set Offset

Args:
    new_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.WindowWidgetBase.notify_window_load_finished"></a>

#### notify\_window\_load\_finished

```python
def notify_window_load_finished(sucees: bool) -> None
```

x.notify_window_load_finished(sucees) -> None
Notify Window Load Finished

Args:
    sucees (bool):

<a id="unreal.WindowWidgetBase.notify_button_clicked"></a>

#### notify\_button\_clicked

```python
def notify_button_clicked(select: bool) -> None
```

x.notify_button_clicked(select) -> None
Notify Button Clicked

Args:
    select (bool):

<a id="unreal.WindowWidgetBase.execute_scale_mode"></a>

#### execute\_scale\_mode

```python
def execute_scale_mode(scale_mode: str, location: Vector,
                       threshold: float) -> None
```

x.execute_scale_mode(scale_mode, location, threshold) -> None
Execute Scale Mode

Args:
    scale_mode (str): 
    location (Vector): 
    threshold (float):

<a id="unreal.WindowWidgetBase.do_wdp_pick_action"></a>

#### do\_wdp\_pick\_action

```python
def do_wdp_pick_action(pick: bool) -> None
```

x.do_wdp_pick_action(pick) -> None
Do Wdp Pick Action

Args:
    pick (bool):

<a id="unreal.WindowWidgetBase.create_window"></a>

#### create\_window

```python
def create_window(p_widget_component: CoveringWidgetComponent, point: Vector,
                  enity_name: Name,
                  window_entity_atom: WindowEntityAtom) -> bool
```

x.create_window(p_widget_component, point, enity_name, window_entity_atom) -> bool
Create Window

Args:
    p_widget_component (CoveringWidgetComponent): 
    point (Vector): 
    enity_name (Name): 
    window_entity_atom (WindowEntityAtom): 

Returns:
    bool:

<a id="unreal.WindowWidgetBase.all_hide"></a>

#### all\_hide

```python
def all_hide() -> None
```

x.all_hide() -> None
All Hide

<a id="unreal.WdpButton"></a>