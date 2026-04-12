## PoiWidgetBase Objects

```python
class PoiWidgetBase(CoveringWidgetBase)
```

Poi Widget Base

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: PoiWidgetBase.h

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
- ``on_button_clicked`` (MyButtonClickedDelegate):  [Read-Write]
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
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``stop_action`` (bool):  [Read-Write]
- ``tick_frequency`` (WidgetTickFrequency):  [Read-Write] This widget is allowed to tick. If this is unchecked tick will never be called, animations will not play correctly, and latent actions will not execute.
  Uncheck this for performance reasons only
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.PoiWidgetBase.on_button_clicked"></a>

#### on\_button\_clicked

```python
@property
def on_button_clicked() -> MyButtonClickedDelegate
```

(MyButtonClickedDelegate):  [Read-Write]

<a id="unreal.PoiWidgetBase.on_button_clicked"></a>

#### on\_button\_clicked

```python
@on_button_clicked.setter
def on_button_clicked(value: MyButtonClickedDelegate) -> None
```

<a id="unreal.PoiWidgetBase.parent_widget_component"></a>

#### parent\_widget\_component

```python
@property
def parent_widget_component() -> CoveringWidgetComponent
```

(CoveringWidgetComponent):  [Read-Write]

<a id="unreal.PoiWidgetBase.parent_widget_component"></a>

#### parent\_widget\_component

```python
@parent_widget_component.setter
def parent_widget_component(value: CoveringWidgetComponent) -> None
```

<a id="unreal.PoiWidgetBase.parent_widget_class"></a>

#### parent\_widget\_class

```python
@property
def parent_widget_class() -> Class
```

(Class):  [Read-Write]

<a id="unreal.PoiWidgetBase.parent_widget_class"></a>

#### parent\_widget\_class

```python
@parent_widget_class.setter
def parent_widget_class(value: Class) -> None
```

<a id="unreal.PoiWidgetBase.parent_visble2d_atom"></a>

#### parent\_visble2d\_atom

```python
@property
def parent_visble2d_atom() -> Visible2DAtom
```

(Visible2DAtom):  [Read-Write]

<a id="unreal.PoiWidgetBase.parent_visble2d_atom"></a>

#### parent\_visble2d\_atom

```python
@parent_visble2d_atom.setter
def parent_visble2d_atom(value: Visible2DAtom) -> None
```

<a id="unreal.PoiWidgetBase.set_z_order"></a>

#### set\_z\_order

```python
def set_z_order(z_order: int) -> None
```

x.set_z_order(z_order) -> None
Set ZOrder

Args:
    z_order (int32):

<a id="unreal.PoiWidgetBase.settext_box_width"></a>

#### settext\_box\_width

```python
def settext_box_width(box_width: float) -> bool
```

x.settext_box_width(box_width) -> bool
Settext Box Width

Args:
    box_width (float): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setspecific_label_style"></a>

#### setspecific\_label\_style

```python
def setspecific_label_style(
        newspecific_label_style: Map[str, PoiLabelContentStyle]) -> bool
```

x.setspecific_label_style(newspecific_label_style) -> bool
Setspecific Label Style

Args:
    newspecific_label_style (Map[str, PoiLabelContentStyle]): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setscroll_speed"></a>

#### setscroll\_speed

```python
def setscroll_speed(speed: float) -> bool
```

x.setscroll_speed(speed) -> bool
Setscroll Speed

Args:
    speed (float): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setscroll_policy"></a>

#### setscroll\_policy

```python
def setscroll_policy(policy: str) -> bool
```

x.setscroll_policy(policy) -> bool
Setscroll Policy

Args:
    policy (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.set_point"></a>

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

<a id="unreal.PoiWidgetBase.set_poi_entity_actor"></a>

#### set\_poi\_entity\_actor

```python
def set_poi_entity_actor(p_entity: PoiEntity) -> None
```

x.set_poi_entity_actor(p_entity) -> None
Set Poi Entity Actor

Args:
    p_entity (PoiEntity):

<a id="unreal.PoiWidgetBase.setmarker_visible"></a>

#### setmarker\_visible

```python
def setmarker_visible(visible: bool) -> bool
```

x.setmarker_visible(visible) -> bool
Setmarker Visible

Args:
    visible (bool): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setmarker_ui"></a>

#### setmarker\_ui

```python
def setmarker_ui(marker_ui: str) -> bool
```

x.setmarker_ui(marker_ui) -> bool
Setmarker Ui

Args:
    marker_ui (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setmarker_size"></a>

#### setmarker\_size

```python
def setmarker_size(marker_size: str) -> bool
```

x.setmarker_size(marker_size) -> bool
Setmarker Size

Args:
    marker_size (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setmarker_offset"></a>

#### setmarker\_offset

```python
def setmarker_offset(marker_offset: Vector2D) -> bool
```

x.setmarker_offset(marker_offset) -> bool
Setmarker Offset

Args:
    marker_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setmarker_normal_url"></a>

#### setmarker\_normal\_url

```python
def setmarker_normal_url(marker_normal_url: str) -> bool
```

x.setmarker_normal_url(marker_normal_url) -> bool
Setmarker Normal Url

Args:
    marker_normal_url (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setmarker_activate_url"></a>

#### setmarker\_activate\_url

```python
def setmarker_activate_url(marker_activate_url: str) -> bool
```

x.setmarker_activate_url(marker_activate_url) -> bool
Setmarker Activate Url

Args:
    marker_activate_url (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_visible"></a>

#### setlabel\_visible

```python
def setlabel_visible(visible: bool) -> bool
```

x.setlabel_visible(visible) -> bool
Setlabel Visible

Args:
    visible (bool): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_top"></a>

#### setlabel\_top

```python
def setlabel_top(top: bool) -> None
```

x.setlabel_top(top) -> None
Setlabel Top

Args:
    top (bool):

<a id="unreal.PoiWidgetBase.setlabel_ui"></a>

#### setlabel\_ui

```python
def setlabel_ui(label_ui: str) -> bool
```

x.setlabel_ui(label_ui) -> bool
Setlabel Ui

Args:
    label_ui (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_contents"></a>

#### setlabel\_contents

```python
def setlabel_contents(label_contents: Array[str]) -> bool
```

x.setlabel_contents(label_contents) -> bool
Setlabel Contents

Args:
    label_contents (Array[str]): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_content_offset"></a>

#### setlabel\_content\_offset

```python
def setlabel_content_offset(label_content_offset: Vector2D) -> bool
```

x.setlabel_content_offset(label_content_offset) -> bool
Setlabel Content Offset

Args:
    label_content_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_content_justification"></a>

#### setlabel\_content\_justification

```python
def setlabel_content_justification(label_content_justification: str) -> bool
```

x.setlabel_content_justification(label_content_justification) -> bool
Setlabel Content Justification

Args:
    label_content_justification (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_content_autowrap"></a>

#### setlabel\_content\_autowrap

```python
def setlabel_content_autowrap(auto_wrap: bool) -> bool
```

x.setlabel_content_autowrap(auto_wrap) -> bool
Setlabel Content Autowrap

Args:
    auto_wrap (bool): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_content"></a>

#### setlabel\_content

```python
def setlabel_content(label_content: Array[str]) -> bool
```

x.setlabel_content(label_content) -> bool
Setlabel Content

Args:
    label_content (Array[str]): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_bg_size"></a>

#### setlabel\_bg\_size

```python
def setlabel_bg_size(label_bg_size: str) -> bool
```

x.setlabel_bg_size(label_bg_size) -> bool
Setlabel Bg Size

Args:
    label_bg_size (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_bg_offset"></a>

#### setlabel\_bg\_offset

```python
def setlabel_bg_offset(label_bg_offset: str) -> bool
```

x.setlabel_bg_offset(label_bg_offset) -> bool
Setlabel Bg Offset

Args:
    label_bg_offset (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setlabel_bg_image_url"></a>

#### setlabel\_bg\_image\_url

```python
def setlabel_bg_image_url(label_bg_image_url: str) -> bool
```

x.setlabel_bg_image_url(label_bg_image_url) -> bool
Setlabel Bg Image Url

Args:
    label_bg_image_url (str): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.setgeneral_label_style"></a>

#### setgeneral\_label\_style

```python
def setgeneral_label_style(
        newgeneral_label_style: PoiLabelContentStyle) -> bool
```

x.setgeneral_label_style(newgeneral_label_style) -> bool
Setgeneral Label Style

Args:
    newgeneral_label_style (PoiLabelContentStyle): 

Returns:
    bool:

<a id="unreal.PoiWidgetBase.reset_z_order"></a>

#### reset\_z\_order

```python
def reset_z_order() -> None
```

x.reset_z_order() -> None
Reset ZOrder

<a id="unreal.PoiWidgetBase.notify_poi_image_load_finished"></a>

#### notify\_poi\_image\_load\_finished

```python
def notify_poi_image_load_finished(sucees: bool) -> None
```

x.notify_poi_image_load_finished(sucees) -> None
Notify Poi Image Load Finished

Args:
    sucees (bool):

<a id="unreal.PoiWidgetBase.notify_button_clicked"></a>

#### notify\_button\_clicked

```python
def notify_button_clicked(select: bool) -> None
```

x.notify_button_clicked(select) -> None
Notify Button Clicked

Args:
    select (bool):

<a id="unreal.PoiWidgetBase.execute_scale_mode"></a>

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

<a id="unreal.PoiWidgetBase.enable_debugging"></a>

#### enable\_debugging

```python
def enable_debugging() -> None
```

x.enable_debugging() -> None
Enable Debugging

<a id="unreal.PoiWidgetBase.do_wdp_pick_action"></a>

#### do\_wdp\_pick\_action

```python
def do_wdp_pick_action(pick: bool) -> None
```

x.do_wdp_pick_action(pick) -> None
Do Wdp Pick Action

Args:
    pick (bool):

<a id="unreal.PoiWidgetBase.create_poi"></a>

#### create\_poi

```python
def create_poi(p_widget_component: CoveringWidgetComponent, point: Vector,
               enity_name: Name, poi_entity_atom: PoiEntityAtom) -> bool
```

x.create_poi(p_widget_component, point, enity_name, poi_entity_atom) -> bool
Create Poi

Args:
    p_widget_component (CoveringWidgetComponent): 
    point (Vector): 
    enity_name (Name): 
    poi_entity_atom (PoiEntityAtom): 

Returns:
    bool:

<a id="unreal.PolyganTriangle"></a>