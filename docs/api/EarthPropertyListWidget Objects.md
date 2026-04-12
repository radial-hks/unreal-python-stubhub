## EarthPropertyListWidget Objects

```python
class EarthPropertyListWidget(EarthTabContentWidget)
```

Earth Property List Widget

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorUI
- **File**: EarthPropertyList.h

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
- ``content_data`` (DataTable):  [Read-Write]
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``customized_item_class`` (Map[Name, type(Class)]):  [Read-Write]
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
- ``typed_item_class`` (Map[EarthPropertyType, type(Class)]):  [Read-Write]
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.EarthPropertyListWidget.typed_item_class"></a>

#### typed\_item\_class

```python
@property
def typed_item_class() -> Map[EarthPropertyType, Class]
```

(Map[EarthPropertyType, type(Class)]):  [Read-Write]

<a id="unreal.EarthPropertyListWidget.typed_item_class"></a>

#### typed\_item\_class

```python
@typed_item_class.setter
def typed_item_class(value: Map[EarthPropertyType, Class]) -> None
```

<a id="unreal.EarthPropertyListWidget.customized_item_class"></a>

#### customized\_item\_class

```python
@property
def customized_item_class() -> Map[Name, Class]
```

(Map[Name, type(Class)]):  [Read-Write]

<a id="unreal.EarthPropertyListWidget.customized_item_class"></a>

#### customized\_item\_class

```python
@customized_item_class.setter
def customized_item_class(value: Map[Name, Class]) -> None
```

<a id="unreal.EarthPropertyListWidget.set_entity_name"></a>

#### set\_entity\_name

```python
def set_entity_name(entity_name: str) -> None
```

x.set_entity_name(entity_name) -> None
Set Entity Name

Args:
    entity_name (str):

<a id="unreal.EarthPropertyListWidget.set_entity_count"></a>

#### set\_entity\_count

```python
def set_entity_count(entity_count: int) -> None
```

x.set_entity_count(entity_count) -> None
Set Entity Count

Args:
    entity_count (int32):

<a id="unreal.EarthPropertyListWidget.refresh_list"></a>

#### refresh\_list

```python
def refresh_list() -> None
```

x.refresh_list() -> None
Refresh List

<a id="unreal.EarthPropertyListWidget.get_all_children"></a>

#### get\_all\_children

```python
def get_all_children() -> Array[Widget]
```

x.get_all_children() -> Array[Widget]
Get All Children

Returns:
    Array[Widget]:

<a id="unreal.EarthPropertyListWidget.clear_children"></a>

#### clear\_children

```python
def clear_children() -> None
```

x.clear_children() -> None
Clear Children

<a id="unreal.EarthPropertyListWidget.add_child"></a>

#### add\_child

```python
def add_child(child: Widget, flags: AesEditorPropertyFlags) -> None
```

x.add_child(child, flags) -> None
Add Child

Args:
    child (Widget): 
    flags (AesEditorPropertyFlags):

<a id="unreal.EarthPropertyListUtils"></a>