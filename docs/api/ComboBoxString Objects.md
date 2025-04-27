## ComboBoxString Objects

```python
class ComboBoxString(Widget)
```

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.

**C++ Source:**

- **Module**: UMG
- **File**: ComboBoxString.h

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
- ``content_padding`` (Margin):  [Read-Write]
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``default_options`` (Array[str]):  [Read-Write] The default list of items to be displayed on the combobox.
- ``enable_gamepad_navigation_mode`` (bool):  [Read-Write] When false, directional keys will change the selection. When true, ComboBox
  must be activated and will only capture arrow input while activated.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``font`` (SlateFontInfo):  [Read-Write] The default font to use in the combobox, only applies if you're not implementing OnGenerateWidgetEvent
  to factory each new entry.
- ``foreground_color`` (SlateColor):  [Read-Write] The foreground color to pass through the hierarchy.
- ``has_down_arrow`` (bool):  [Read-Write] When false, the down arrow is not generated and it is up to the API consumer
  to make their own visual hint that this is a drop down.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write]
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``item_style`` (TableRowStyle):  [Read-Write] The item row style.
- ``max_list_height`` (float):  [Read-Write] The max height of the combobox list that opens
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``on_generate_widget_event`` (GenerateWidgetForString):  [Read-Write] Called when the widget is needed for the item.
- ``on_opening`` (OnOpeningEvent):  [Read-Write] Called when the combobox is opening
- ``on_selection_changed`` (OnSelectionChangedEvent):  [Read-Write] Called when a new item is selected in the combobox.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``scroll_bar_style`` (ScrollBarStyle):  [Read-Write] The scroll bar style.
- ``selected_option`` (str):  [Read-Write] The item in the combobox to select by default
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``widget_style`` (ComboBoxStyle):  [Read-Write] The style.

<a id="unreal.ComboBoxString.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> ComboBoxStyle
```

(ComboBoxStyle):  [Read-Write] The style.

<a id="unreal.ComboBoxString.widget_style"></a>

#### widget_style

```python
@widget_style.setter
def widget_style(value: ComboBoxStyle) -> None
```

<a id="unreal.ComboBoxString.item_style"></a>

#### item_style

```python
@property
def item_style() -> TableRowStyle
```

(TableRowStyle):  [Read-Write] The item row style.

<a id="unreal.ComboBoxString.item_style"></a>

#### item_style

```python
@item_style.setter
def item_style(value: TableRowStyle) -> None
```

<a id="unreal.ComboBoxString.scroll_bar_style"></a>

#### scroll_bar_style

```python
@property
def scroll_bar_style() -> ScrollBarStyle
```

(ScrollBarStyle):  [Read-Only] The scroll bar style.

<a id="unreal.ComboBoxString.content_padding"></a>

#### content_padding

```python
@property
def content_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ComboBoxString.content_padding"></a>

#### content_padding

```python
@content_padding.setter
def content_padding(value: Margin) -> None
```

<a id="unreal.ComboBoxString.max_list_height"></a>

#### max_list_height

```python
@property
def max_list_height() -> float
```

(float):  [Read-Write] The max height of the combobox list that opens

<a id="unreal.ComboBoxString.max_list_height"></a>

#### max_list_height

```python
@max_list_height.setter
def max_list_height(value: float) -> None
```

<a id="unreal.ComboBoxString.has_down_arrow"></a>

#### has_down_arrow

```python
@property
def has_down_arrow() -> bool
```

(bool):  [Read-Write] When false, the down arrow is not generated and it is up to the API consumer
to make their own visual hint that this is a drop down.

<a id="unreal.ComboBoxString.has_down_arrow"></a>

#### has_down_arrow

```python
@has_down_arrow.setter
def has_down_arrow(value: bool) -> None
```

<a id="unreal.ComboBoxString.enable_gamepad_navigation_mode"></a>

#### enable_gamepad_navigation_mode

```python
@property
def enable_gamepad_navigation_mode() -> bool
```

(bool):  [Read-Write] When false, directional keys will change the selection. When true, ComboBox
must be activated and will only capture arrow input while activated.

<a id="unreal.ComboBoxString.enable_gamepad_navigation_mode"></a>

#### enable_gamepad_navigation_mode

```python
@enable_gamepad_navigation_mode.setter
def enable_gamepad_navigation_mode(value: bool) -> None
```

<a id="unreal.ComboBoxString.font"></a>

#### font

```python
@property
def font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Only] The default font to use in the combobox, only applies if you're not implementing OnGenerateWidgetEvent
to factory each new entry.

<a id="unreal.ComboBoxString.foreground_color"></a>

#### foreground_color

```python
@property
def foreground_color() -> SlateColor
```

(SlateColor):  [Read-Only] The foreground color to pass through the hierarchy.

<a id="unreal.ComboBoxString.is_focusable"></a>

#### is_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ComboBoxString.on_selection_changed"></a>

#### on_selection_changed

```python
@property
def on_selection_changed() -> OnSelectionChangedEvent
```

(OnSelectionChangedEvent):  [Read-Write] Called when a new item is selected in the combobox.

<a id="unreal.ComboBoxString.on_selection_changed"></a>

#### on_selection_changed

```python
@on_selection_changed.setter
def on_selection_changed(value: OnSelectionChangedEvent) -> None
```

<a id="unreal.ComboBoxString.on_opening"></a>

#### on_opening

```python
@property
def on_opening() -> OnOpeningEvent
```

(OnOpeningEvent):  [Read-Write] Called when the combobox is opening

<a id="unreal.ComboBoxString.on_opening"></a>

#### on_opening

```python
@on_opening.setter
def on_opening(value: OnOpeningEvent) -> None
```

<a id="unreal.ComboBoxString.set_selected_option"></a>

#### set_selected_option

```python
def set_selected_option(option: str) -> None
```

x.set_selected_option(option) -> None
Set Selected Option

Args:
    option (str):

<a id="unreal.ComboBoxString.set_selected_index"></a>

#### set_selected_index

```python
def set_selected_index(index: int) -> None
```

x.set_selected_index(index) -> None
Set Selected Index

Args:
    index (int32):

<a id="unreal.ComboBoxString.remove_option"></a>

#### remove_option

```python
def remove_option(option: str) -> bool
```

x.remove_option(option) -> bool
Remove Option

Args:
    option (str): 

Returns:
    bool:

<a id="unreal.ComboBoxString.refresh_options"></a>

#### refresh_options

```python
def refresh_options() -> None
```

x.refresh_options() -> None
Refreshes the list of options.  If you added new ones, and want to update the list even if it's
currently being displayed use this.

<a id="unreal.ComboBoxString.is_open"></a>

#### is_open

```python
def is_open() -> bool
```

x.is_open() -> bool
Is Open

Returns:
    bool:

<a id="unreal.ComboBoxString.get_selected_option"></a>

#### get_selected_option

```python
def get_selected_option() -> str
```

x.get_selected_option() -> str
Get Selected Option

Returns:
    str:

<a id="unreal.ComboBoxString.get_selected_index"></a>

#### get_selected_index

```python
def get_selected_index() -> int
```

x.get_selected_index() -> int32
Get Selected Index

Returns:
    int32:

<a id="unreal.ComboBoxString.get_option_count"></a>

#### get_option_count

```python
def get_option_count() -> int
```

x.get_option_count() -> int32
Returns the number of options

Returns:
    int32:

<a id="unreal.ComboBoxString.get_option_at_index"></a>

#### get_option_at_index

```python
def get_option_at_index(index: int) -> str
```

x.get_option_at_index(index) -> str
Get Option at Index

Args:
    index (int32): 

Returns:
    str:

<a id="unreal.ComboBoxString.find_option_index"></a>

#### find_option_index

```python
def find_option_index(option: str) -> int
```

x.find_option_index(option) -> int32
Find Option Index

Args:
    option (str): 

Returns:
    int32:

<a id="unreal.ComboBoxString.clear_selection"></a>

#### clear_selection

```python
def clear_selection() -> None
```

x.clear_selection() -> None
Clear Selection

<a id="unreal.ComboBoxString.clear_options"></a>

#### clear_options

```python
def clear_options() -> None
```

x.clear_options() -> None
Clear Options

<a id="unreal.ComboBoxString.add_option"></a>

#### add_option

```python
def add_option(option: str) -> None
```

x.add_option(option) -> None
Add Option

Args:
    option (str):

<a id="unreal.DynamicEntryBoxBase"></a>