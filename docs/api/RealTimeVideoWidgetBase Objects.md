## RealTimeVideoWidgetBase Objects

```python
class RealTimeVideoWidgetBase(CoveringWidgetBase)
```

Real Time Video Widget Base

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: RealTimeVideoWidgetBase.h

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

<a id="unreal.RealTimeVideoWidgetBase.set_url"></a>

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

<a id="unreal.RealTimeVideoWidgetBase.set_state"></a>

#### set\_state

```python
def set_state(new_state: str) -> bool
```

x.set_state(new_state) -> bool
Set State

Args:
    new_state (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_resolution"></a>

#### set\_resolution

```python
def set_resolution(new_resolution: Vector2D) -> bool
```

x.set_resolution(new_resolution) -> bool
Set Resolution

Args:
    new_resolution (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_real_time_video_entity_actor"></a>

#### set\_real\_time\_video\_entity\_actor

```python
def set_real_time_video_entity_actor(p_entity: RealTimeVideoEntity) -> None
```

x.set_real_time_video_entity_actor(p_entity) -> None
Set Real Time Video Entity Actor

Args:
    p_entity (RealTimeVideoEntity):

<a id="unreal.RealTimeVideoWidgetBase.set_point"></a>

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

<a id="unreal.RealTimeVideoWidgetBase.set_offset"></a>

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

<a id="unreal.RealTimeVideoWidgetBase.set_label_size"></a>

#### set\_label\_size

```python
def set_label_size(new_label_size: Vector2D) -> bool
```

x.set_label_size(new_label_size) -> bool
Set Label Size

Args:
    new_label_size (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_label_offset"></a>

#### set\_label\_offset

```python
def set_label_offset(new_label_offset: Vector2D) -> bool
```

x.set_label_offset(new_label_offset) -> bool
Set Label Offset

Args:
    new_label_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_label_content_justification"></a>

#### set\_label\_content\_justification

```python
def set_label_content_justification(
        new_label_content_justification: str) -> bool
```

x.set_label_content_justification(new_label_content_justification) -> bool
Set Label Content Justification

Args:
    new_label_content_justification (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_label_content_auto_wrap"></a>

#### set\_label\_content\_auto\_wrap

```python
def set_label_content_auto_wrap(new_label_content_auto_wrap: bool) -> bool
```

x.set_label_content_auto_wrap(new_label_content_auto_wrap) -> bool
Set Label Content Auto Wrap

Args:
    new_label_content_auto_wrap (bool): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_label_content"></a>

#### set\_label\_content

```python
def set_label_content(new_label_content: Array[str]) -> bool
```

x.set_label_content(new_label_content) -> bool
Set Label Content

Args:
    new_label_content (Array[str]): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_conrner_shift"></a>

#### set\_conrner\_shift

```python
def set_conrner_shift(new_conrner_shift: Array[Vector2D]) -> bool
```

x.set_conrner_shift(new_conrner_shift) -> bool
Set Conrner Shift

Args:
    new_conrner_shift (Array[Vector2D]): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_btn_size"></a>

#### set\_btn\_size

```python
def set_btn_size(new_btn_size: Vector2D) -> bool
```

x.set_btn_size(new_btn_size) -> bool
Set Btn Size

Args:
    new_btn_size (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_btn_offset"></a>

#### set\_btn\_offset

```python
def set_btn_offset(new_btn_offset: Vector2D) -> bool
```

x.set_btn_offset(new_btn_offset) -> bool
Set Btn Offset

Args:
    new_btn_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_btn_normal_url"></a>

#### set\_btn\_normal\_url

```python
def set_btn_normal_url(new_btn_normal_url: str) -> bool
```

x.set_btn_normal_url(new_btn_normal_url) -> bool
Set Btn Normal Url

Args:
    new_btn_normal_url (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_btn_activate_url"></a>

#### set\_btn\_activate\_url

```python
def set_btn_activate_url(new_btn_activate_url: str) -> bool
```

x.set_btn_activate_url(new_btn_activate_url) -> bool
Set Btn Activate Url

Args:
    new_btn_activate_url (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_bokeh"></a>

#### set\_bokeh

```python
def set_bokeh(new_bokeh: float) -> bool
```

x.set_bokeh(new_bokeh) -> bool
Set Bokeh

Args:
    new_bokeh (float): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_bg_url"></a>

#### set\_bg\_url

```python
def set_bg_url(new_bg_url: str) -> bool
```

x.set_bg_url(new_bg_url) -> bool
Set Bg Url

Args:
    new_bg_url (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_bg_padding"></a>

#### set\_bg\_padding

```python
def set_bg_padding(new_bg_padding: Array[int]) -> bool
```

x.set_bg_padding(new_bg_padding) -> bool
Set Bg Padding

Args:
    new_bg_padding (Array[int32]): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.set_bg_overlap"></a>

#### set\_bg\_overlap

```python
def set_bg_overlap(new_bg_overlap: str) -> bool
```

x.set_bg_overlap(new_bg_overlap) -> bool
Set Bg Overlap

Args:
    new_bg_overlap (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoWidgetBase.notify_real_time_video_load_finished"></a>

#### notify\_real\_time\_video\_load\_finished

```python
def notify_real_time_video_load_finished(sucees: bool) -> None
```

x.notify_real_time_video_load_finished(sucees) -> None
Notify Real Time Video Load Finished

Args:
    sucees (bool):

<a id="unreal.RealTimeVideoWidgetBase.create_real_time_video"></a>

#### create\_real\_time\_video

```python
def create_real_time_video(
        p_widget_component: CoveringWidgetComponent, point: Vector,
        enity_name: Name,
        real_time_video_entity_atom: RealTimeVideoEntityAtom) -> bool
```

x.create_real_time_video(p_widget_component, point, enity_name, real_time_video_entity_atom) -> bool
Create Real Time Video

Args:
    p_widget_component (CoveringWidgetComponent): 
    point (Vector): 
    enity_name (Name): 
    real_time_video_entity_atom (RealTimeVideoEntityAtom): 

Returns:
    bool:

<a id="unreal.RichTextBlockInlineDecorator"></a>