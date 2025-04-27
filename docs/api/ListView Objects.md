## ListView Objects

```python
class ListView(ListViewBase)
```

A virtualized list that allows up to thousands of items to be displayed.

An important distinction to keep in mind here is "Item" vs. "Entry"
The list itself is based on a list of n items, but only creates as many entry widgets as can fit on screen.
For example, a scrolling ListView of 200 items with 5 currently visible will only have created 5 entry widgets.

To make a widget usable as an entry in a ListView, it must inherit from the IUserObjectListEntry interface.

**C++ Source:**

- **Module**: UMG
- **File**: ListView.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``allow_dragging`` (bool):  [Read-Write] True to allow dragging of row widgets in the list
- ``allow_overscroll`` (bool):  [Read-Write] Disable to stop scrollbars from activating inertial overscrolling
- ``bp_on_entry_generated`` (OnListEntryGeneratedDynamic):  [Read-Write] Called when a row widget is generated for a list item
- ``bp_on_entry_initialized`` (OnListEntryInitializedDynamic):  [Read-Write] Called when a row widget is generated for a list item
- ``bp_on_entry_released`` (OnListEntryReleasedDynamic):  [Read-Write] Called when a row widget is released by the list (i.e. when it no longer represents a list item)
- ``bp_on_item_clicked`` (SimpleListItemEventDynamic):  [Read-Write]
- ``bp_on_item_double_clicked`` (SimpleListItemEventDynamic):  [Read-Write]
- ``bp_on_item_is_hovered_changed`` (OnItemIsHoveredChangedDynamic):  [Read-Write]
- ``bp_on_item_scrolled_into_view`` (OnListItemScrolledIntoViewDynamic):  [Read-Write]
- ``bp_on_item_selection_changed`` (OnListItemSelectionChangedDynamic):  [Read-Write]
- ``bp_on_list_view_scrolled`` (OnListViewScrolledDynamic):  [Read-Write]
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clear_selection_on_click`` (bool):  [Read-Write]
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``consume_mouse_wheel`` (ConsumeMouseWheel):  [Read-Write]
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``enable_fixed_line_offset`` (bool):  [Read-Write]
- ``enable_right_click_scrolling`` (bool):  [Read-Write] True to allow right click drag scrolling.
- ``enable_scroll_animation`` (bool):  [Read-Write] True to enable lerped animation when scrolling through the list
- ``enable_touch_animated_scrolling`` (bool):  [Read-Write] True to enable lerped animation when scrolling through the list with touch
- ``enable_touch_scrolling`` (bool):  [Read-Write] True to allow scrolling using touch input.
- ``entry_spacing`` (float):  [Read-Write] This deprecated property was originally BlueprintReadOnly. To satisfy the compiler requirment to have a BlueprintGetter for this property,
  it relies on the newly added UFunction GetHorizontalEntrySpacing() to act as its BlueprintGetter.
  deprecated: EntrySpacing has been deprecated. Please use HorizontalEntrySpacing and VerticalEntrySpacing.
- ``entry_widget_class`` (type(Class)):  [Read-Write] The type of widget to create for each entry displayed in the list.
- ``fixed_line_scroll_offset`` (float):  [Read-Write] Optional fixed offset (in lines) to always apply to the top/left (depending on orientation) of the list.
  If provided, all non-inertial means of scrolling will settle with exactly this offset of the topmost entry.
  Ex: A value of 0.25 would cause the topmost full entry to be offset down by a quarter length of the preceeding entry.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``horizontal_entry_spacing`` (float):  [Read-Write]
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_focusable`` (bool):  [Read-Write]
- ``is_gamepad_scrolling_enabled`` (bool):  [Read-Write] Enable/Disable scrolling using Gamepad.
- ``is_pointer_scrolling_enabled`` (bool):  [Read-Write] Enable/Disable scrolling using Touch or Mouse.
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``num_designer_preview_entries`` (int32):  [Read-Write] The number of dummy item entry widgets to preview in the widget designer
- ``orientation`` (Orientation):  [Read-Write] The scroll & layout orientation of the list. ListView and TileView only.
  Vertical will scroll vertically and arrange tiles into rows.
  Horizontal will scroll horizontally and arrange tiles into columns.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``return_focus_to_selection`` (bool):  [Read-Write]
- ``scroll_bar_padding`` (Margin):  [Read-Write]
- ``scroll_bar_style`` (ScrollBarStyle):  [Read-Write]
- ``scroll_into_view_alignment`` (ScrollIntoViewAlignment):  [Read-Write] Sets where to scroll a widget to when using explicit navigation
- ``scrolling_animation_interpolation_speed`` (float):  [Read-Write] The speed to apply when lerping in the scroll animation.
- ``selection_mode`` (SelectionMode):  [Read-Write]
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``vertical_entry_spacing`` (float):  [Read-Write]
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``wheel_scroll_multiplier`` (float):  [Read-Write] The multiplier to apply when wheel scrolling
- ``widget_style`` (TableViewStyle):  [Read-Write]

<a id="unreal.ListView.widget_style"></a>

#### widget_style

```python
@property
def widget_style() -> TableViewStyle
```

(TableViewStyle):  [Read-Only]

<a id="unreal.ListView.scroll_bar_style"></a>

#### scroll_bar_style

```python
@property
def scroll_bar_style() -> ScrollBarStyle
```

(ScrollBarStyle):  [Read-Only]

<a id="unreal.ListView.orientation"></a>

#### orientation

```python
@property
def orientation() -> Orientation
```

(Orientation):  [Read-Only] The scroll & layout orientation of the list. ListView and TileView only.
Vertical will scroll vertically and arrange tiles into rows.
Horizontal will scroll horizontally and arrange tiles into columns.

<a id="unreal.ListView.selection_mode"></a>

#### selection_mode

```python
@property
def selection_mode() -> SelectionMode
```

(SelectionMode):  [Read-Only]

<a id="unreal.ListView.consume_mouse_wheel"></a>

#### consume_mouse_wheel

```python
@property
def consume_mouse_wheel() -> ConsumeMouseWheel
```

(ConsumeMouseWheel):  [Read-Only]

<a id="unreal.ListView.clear_selection_on_click"></a>

#### clear_selection_on_click

```python
@property
def clear_selection_on_click() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ListView.is_focusable"></a>

#### is_focusable

```python
@property
def is_focusable() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ListView.return_focus_to_selection"></a>

#### return_focus_to_selection

```python
@property
def return_focus_to_selection() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ListView.scroll_into_view_alignment"></a>

#### scroll_into_view_alignment

```python
@property
def scroll_into_view_alignment() -> ScrollIntoViewAlignment
```

(ScrollIntoViewAlignment):  [Read-Only] Sets where to scroll a widget to when using explicit navigation

<a id="unreal.ListView.entry_spacing"></a>

#### entry_spacing

```python
@property
def entry_spacing() -> float
```

(float):  [Read-Only] This deprecated property was originally BlueprintReadOnly. To satisfy the compiler requirment to have a BlueprintGetter for this property,
it relies on the newly added UFunction GetHorizontalEntrySpacing() to act as its BlueprintGetter.
deprecated: EntrySpacing has been deprecated. Please use HorizontalEntrySpacing and VerticalEntrySpacing.

<a id="unreal.ListView.horizontal_entry_spacing"></a>

#### horizontal_entry_spacing

```python
@property
def horizontal_entry_spacing() -> float
```

(float):  [Read-Only]

<a id="unreal.ListView.vertical_entry_spacing"></a>

#### vertical_entry_spacing

```python
@property
def vertical_entry_spacing() -> float
```

(float):  [Read-Only]

<a id="unreal.ListView.scroll_bar_padding"></a>

#### scroll_bar_padding

```python
@property
def scroll_bar_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ListView.scroll_bar_padding"></a>

#### scroll_bar_padding

```python
@scroll_bar_padding.setter
def scroll_bar_padding(value: Margin) -> None
```

<a id="unreal.ListView.bp_on_entry_initialized"></a>

#### bp_on_entry_initialized

```python
@property
def bp_on_entry_initialized() -> OnListEntryInitializedDynamic
```

(OnListEntryInitializedDynamic):  [Read-Write] Called when a row widget is generated for a list item

<a id="unreal.ListView.bp_on_entry_initialized"></a>

#### bp_on_entry_initialized

```python
@bp_on_entry_initialized.setter
def bp_on_entry_initialized(value: OnListEntryInitializedDynamic) -> None
```

<a id="unreal.ListView.bp_on_item_clicked"></a>

#### bp_on_item_clicked

```python
@property
def bp_on_item_clicked() -> SimpleListItemEventDynamic
```

(SimpleListItemEventDynamic):  [Read-Write]

<a id="unreal.ListView.bp_on_item_clicked"></a>

#### bp_on_item_clicked

```python
@bp_on_item_clicked.setter
def bp_on_item_clicked(value: SimpleListItemEventDynamic) -> None
```

<a id="unreal.ListView.bp_on_item_double_clicked"></a>

#### bp_on_item_double_clicked

```python
@property
def bp_on_item_double_clicked() -> SimpleListItemEventDynamic
```

(SimpleListItemEventDynamic):  [Read-Write]

<a id="unreal.ListView.bp_on_item_double_clicked"></a>

#### bp_on_item_double_clicked

```python
@bp_on_item_double_clicked.setter
def bp_on_item_double_clicked(value: SimpleListItemEventDynamic) -> None
```

<a id="unreal.ListView.bp_on_item_is_hovered_changed"></a>

#### bp_on_item_is_hovered_changed

```python
@property
def bp_on_item_is_hovered_changed() -> OnItemIsHoveredChangedDynamic
```

(OnItemIsHoveredChangedDynamic):  [Read-Write]

<a id="unreal.ListView.bp_on_item_is_hovered_changed"></a>

#### bp_on_item_is_hovered_changed

```python
@bp_on_item_is_hovered_changed.setter
def bp_on_item_is_hovered_changed(
        value: OnItemIsHoveredChangedDynamic) -> None
```

<a id="unreal.ListView.bp_on_item_selection_changed"></a>

#### bp_on_item_selection_changed

```python
@property
def bp_on_item_selection_changed() -> OnListItemSelectionChangedDynamic
```

(OnListItemSelectionChangedDynamic):  [Read-Write]

<a id="unreal.ListView.bp_on_item_selection_changed"></a>

#### bp_on_item_selection_changed

```python
@bp_on_item_selection_changed.setter
def bp_on_item_selection_changed(
        value: OnListItemSelectionChangedDynamic) -> None
```

<a id="unreal.ListView.bp_on_item_scrolled_into_view"></a>

#### bp_on_item_scrolled_into_view

```python
@property
def bp_on_item_scrolled_into_view() -> OnListItemScrolledIntoViewDynamic
```

(OnListItemScrolledIntoViewDynamic):  [Read-Write]

<a id="unreal.ListView.bp_on_item_scrolled_into_view"></a>

#### bp_on_item_scrolled_into_view

```python
@bp_on_item_scrolled_into_view.setter
def bp_on_item_scrolled_into_view(
        value: OnListItemScrolledIntoViewDynamic) -> None
```

<a id="unreal.ListView.bp_on_list_view_scrolled"></a>

#### bp_on_list_view_scrolled

```python
@property
def bp_on_list_view_scrolled() -> OnListViewScrolledDynamic
```

(OnListViewScrolledDynamic):  [Read-Write]

<a id="unreal.ListView.bp_on_list_view_scrolled"></a>

#### bp_on_list_view_scrolled

```python
@bp_on_list_view_scrolled.setter
def bp_on_list_view_scrolled(value: OnListViewScrolledDynamic) -> None
```

<a id="unreal.ListView.set_selection_mode"></a>

#### set_selection_mode

```python
def set_selection_mode(selection_mode: SelectionMode) -> None
```

x.set_selection_mode(selection_mode) -> None
Sets the new selection mode, preserving the current selection where possible.

Args:
    selection_mode (SelectionMode):

<a id="unreal.ListView.set_selected_index"></a>

#### set_selected_index

```python
def set_selected_index(index: int) -> None
```

x.set_selected_index(index) -> None
Sets the item at the given index as the sole selected item.

Args:
    index (int32):

<a id="unreal.ListView.set_scroll_into_view_alignment"></a>

#### set_scroll_into_view_alignment

```python
def set_scroll_into_view_alignment(
        new_scroll_into_view_alignment: ScrollIntoViewAlignment) -> None
```

x.set_scroll_into_view_alignment(new_scroll_into_view_alignment) -> None
Sets ScrollIntoViewAlignment which allows to stick the selected item to either side or center

Args:
    new_scroll_into_view_alignment (ScrollIntoViewAlignment):

<a id="unreal.ListView.scroll_index_into_view"></a>

#### scroll_index_into_view

```python
def scroll_index_into_view(index: int) -> None
```

x.scroll_index_into_view(index) -> None
Requests that the item at the given index is scrolled into view

Args:
    index (int32):

<a id="unreal.ListView.remove_item"></a>

#### remove_item

```python
def remove_item(item: Object) -> None
```

x.remove_item(item) -> None
Removes an the item from the list

Args:
    item (Object):

<a id="unreal.ListView.navigate_to_index"></a>

#### navigate_to_index

```python
def navigate_to_index(index: int) -> None
```

x.navigate_to_index(index) -> None
Requests that the item at the given index navigated to, scrolling it into view if needed.

Args:
    index (int32):

<a id="unreal.ListView.is_refresh_pending"></a>

#### is_refresh_pending

```python
def is_refresh_pending() -> bool
```

x.is_refresh_pending() -> bool
Returns true if a refresh is pending and the list will be rebuilt on the next tick

Returns:
    bool:

<a id="unreal.ListView.get_vertical_entry_spacing"></a>

#### get_vertical_entry_spacing

```python
def get_vertical_entry_spacing() -> float
```

x.get_vertical_entry_spacing() -> float
Get the vertical spacing between entries.

Returns:
    float:

<a id="unreal.ListView.get_num_items"></a>

#### get_num_items

```python
def get_num_items() -> int
```

x.get_num_items() -> int32
Returns the total number of items

Returns:
    int32:

<a id="unreal.ListView.get_list_items"></a>

#### get_list_items

```python
def get_list_items() -> Array[Object]
```

x.get_list_items() -> Array[Object]
Gets the list of all items in the list.
Note that each of these items only has a corresponding entry widget when visible. Use GetDisplayedEntryWidgets to get the currently displayed widgets.

Returns:
    Array[Object]:

<a id="unreal.ListView.get_item_at"></a>

#### get_item_at

```python
def get_item_at(index: int) -> Object
```

x.get_item_at(index) -> Object
Returns the item at the given index

Args:
    index (int32): 

Returns:
    Object:

<a id="unreal.ListView.get_index_for_item"></a>

#### get_index_for_item

```python
def get_index_for_item(item: Object) -> int
```

x.get_index_for_item(item) -> int32
Returns the index that the specified item is at. Will return the first found, or -1 for not found

Args:
    item (Object): 

Returns:
    int32:

<a id="unreal.ListView.get_horizontal_entry_spacing"></a>

#### get_horizontal_entry_spacing

```python
def get_horizontal_entry_spacing() -> float
```

x.get_horizontal_entry_spacing() -> float
Get the horizontal spacing between entries.

Returns:
    float:

<a id="unreal.ListView.clear_list_items"></a>

#### clear_list_items

```python
def clear_list_items() -> None
```

x.clear_list_items() -> None
Removes all items from the list

<a id="unreal.ListView.bp_set_selected_item"></a>

#### bp_set_selected_item

```python
def bp_set_selected_item(item: Object) -> None
```

x.bp_set_selected_item(item) -> None
Sets the given item as the sole selected item.

Args:
    item (Object):

<a id="unreal.ListView.bp_set_list_items"></a>

#### bp_set_list_items

```python
def bp_set_list_items(list_items: Array[Object]) -> None
```

x.bp_set_list_items(list_items) -> None
Sets the array of objects to display rows for in the list

Args:
    list_items (Array[Object]):

<a id="unreal.ListView.bp_set_item_selection"></a>

#### bp_set_item_selection

```python
def bp_set_item_selection(item: Object, selected: bool) -> None
```

x.bp_set_item_selection(item, selected) -> None
Sets whether the given item is selected.

Args:
    item (Object): 
    selected (bool):

<a id="unreal.ListView.bp_scroll_item_into_view"></a>

#### bp_scroll_item_into_view

```python
def bp_scroll_item_into_view(item: Object) -> None
```

x.bp_scroll_item_into_view(item) -> None
Requests that the given item is scrolled into view

Args:
    item (Object):

<a id="unreal.ListView.bp_navigate_to_item"></a>

#### bp_navigate_to_item

```python
def bp_navigate_to_item(item: Object) -> None
```

x.bp_navigate_to_item(item) -> None
Requests that the given item is navigated to, scrolling it into view if needed.

Args:
    item (Object):

<a id="unreal.ListView.bp_is_item_visible"></a>

#### bp_is_item_visible

```python
def bp_is_item_visible(item: Object) -> bool
```

x.bp_is_item_visible(item) -> bool
Gets whether the entry for the given object is currently visible in the list

Args:
    item (Object): 

Returns:
    bool:

<a id="unreal.ListView.bp_get_selected_items"></a>

#### bp_get_selected_items

```python
def bp_get_selected_items() -> Optional[Array[Object]]
```

x.bp_get_selected_items() -> Array[Object] or None
Gets a list of all the currently selected items

Returns:
    Array[Object] or None: 

    items (Array[Object]):

<a id="unreal.ListView.bp_get_selected_item"></a>

#### bp_get_selected_item

```python
def bp_get_selected_item() -> Object
```

x.bp_get_selected_item() -> Object
Gets the first selected item, if any; recommended that you only use this for single selection lists.

Returns:
    Object:

<a id="unreal.ListView.bp_get_num_items_selected"></a>

#### bp_get_num_items_selected

```python
def bp_get_num_items_selected() -> int
```

x.bp_get_num_items_selected() -> int32
Gets the number of items currently selected in the list

Returns:
    int32:

<a id="unreal.ListView.bp_clear_selection"></a>

#### bp_clear_selection

```python
def bp_clear_selection() -> None
```

x.bp_clear_selection() -> None
Clear selection

<a id="unreal.ListView.bp_cancel_scroll_into_view"></a>

#### bp_cancel_scroll_into_view

```python
def bp_cancel_scroll_into_view() -> None
```

x.bp_cancel_scroll_into_view() -> None
Cancels a previous request to scroll and item into view.

<a id="unreal.ListView.add_item"></a>

#### add_item

```python
def add_item(item: Object) -> None
```

x.add_item(item) -> None
Adds an the item to the list

Args:
    item (Object):

<a id="unreal.WidgetNavigation"></a>