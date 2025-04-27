## ListViewBase Objects

```python
class ListViewBase(Widget)
```

Bare-bones base class to make creating custom UListView widgets easier.
Child classes should also inherit from ITypedUMGListView<T> to get a basic public ListView API for free.

Child classes will own the actual SListView<T> widgets, but this provides some boilerplate functionality for generating entries.
To generate a row for the child list, use GenerateTypedRow with the appropriate SObjectTableRow<T> type for your list

Additionally, the entry widget class can be filtered for a particular class and interface with the EntryClass and EntryInterface metadata arguments
This can be specified either on the class directly (see below) or on any BindWidget FProperty

Example:
class UMyUserWidget : public UUserWidget
{
            UPROPERTY(BindWidget, meta = (EntryClass = MyListEntryWidget))
            UListView* ListView_InventoryItems;
}

**C++ Source:**

- **Module**: UMG
- **File**: ListViewBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``allow_dragging`` (bool):  [Read-Write] True to allow dragging of row widgets in the list
- ``allow_overscroll`` (bool):  [Read-Write] Disable to stop scrollbars from activating inertial overscrolling
- ``bp_on_entry_generated`` (OnListEntryGeneratedDynamic):  [Read-Write] Called when a row widget is generated for a list item
- ``bp_on_entry_released`` (OnListEntryReleasedDynamic):  [Read-Write] Called when a row widget is released by the list (i.e. when it no longer represents a list item)
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``enable_fixed_line_offset`` (bool):  [Read-Write]
- ``enable_right_click_scrolling`` (bool):  [Read-Write] True to allow right click drag scrolling.
- ``enable_scroll_animation`` (bool):  [Read-Write] True to enable lerped animation when scrolling through the list
- ``enable_touch_animated_scrolling`` (bool):  [Read-Write] True to enable lerped animation when scrolling through the list with touch
- ``enable_touch_scrolling`` (bool):  [Read-Write] True to allow scrolling using touch input.
- ``entry_widget_class`` (type(Class)):  [Read-Write] The type of widget to create for each entry displayed in the list.
- ``fixed_line_scroll_offset`` (float):  [Read-Write] Optional fixed offset (in lines) to always apply to the top/left (depending on orientation) of the list.
  If provided, all non-inertial means of scrolling will settle with exactly this offset of the topmost entry.
  Ex: A value of 0.25 would cause the topmost full entry to be offset down by a quarter length of the preceeding entry.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
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
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``scrolling_animation_interpolation_speed`` (float):  [Read-Write] The speed to apply when lerping in the scroll animation.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``wheel_scroll_multiplier`` (float):  [Read-Write] The multiplier to apply when wheel scrolling

<a id="unreal.ListViewBase.bp_on_entry_generated"></a>

#### bp_on_entry_generated

```python
@property
def bp_on_entry_generated() -> OnListEntryGeneratedDynamic
```

(OnListEntryGeneratedDynamic):  [Read-Write] Called when a row widget is generated for a list item

<a id="unreal.ListViewBase.bp_on_entry_generated"></a>

#### bp_on_entry_generated

```python
@bp_on_entry_generated.setter
def bp_on_entry_generated(value: OnListEntryGeneratedDynamic) -> None
```

<a id="unreal.ListViewBase.entry_widget_class"></a>

#### entry_widget_class

```python
@property
def entry_widget_class() -> Class
```

(type(Class)):  [Read-Only] The type of widget to create for each entry displayed in the list.

<a id="unreal.ListViewBase.wheel_scroll_multiplier"></a>

#### wheel_scroll_multiplier

```python
@property
def wheel_scroll_multiplier() -> float
```

(float):  [Read-Only] The multiplier to apply when wheel scrolling

<a id="unreal.ListViewBase.enable_scroll_animation"></a>

#### enable_scroll_animation

```python
@property
def enable_scroll_animation() -> bool
```

(bool):  [Read-Only] True to enable lerped animation when scrolling through the list

<a id="unreal.ListViewBase.scrolling_animation_interpolation_speed"></a>

#### scrolling_animation_interpolation_speed

```python
@property
def scrolling_animation_interpolation_speed() -> float
```

(float):  [Read-Only] The speed to apply when lerping in the scroll animation.

<a id="unreal.ListViewBase.enable_touch_animated_scrolling"></a>

#### enable_touch_animated_scrolling

```python
@property
def enable_touch_animated_scrolling() -> bool
```

(bool):  [Read-Only] True to enable lerped animation when scrolling through the list with touch

<a id="unreal.ListViewBase.allow_dragging"></a>

#### allow_dragging

```python
@property
def allow_dragging() -> bool
```

(bool):  [Read-Only] True to allow dragging of row widgets in the list

<a id="unreal.ListViewBase.bp_on_entry_released"></a>

#### bp_on_entry_released

```python
@property
def bp_on_entry_released() -> OnListEntryReleasedDynamic
```

(OnListEntryReleasedDynamic):  [Read-Write] Called when a row widget is released by the list (i.e. when it no longer represents a list item)

<a id="unreal.ListViewBase.bp_on_entry_released"></a>

#### bp_on_entry_released

```python
@bp_on_entry_released.setter
def bp_on_entry_released(value: OnListEntryReleasedDynamic) -> None
```

<a id="unreal.ListViewBase.set_wheel_scroll_multiplier"></a>

#### set_wheel_scroll_multiplier

```python
def set_wheel_scroll_multiplier(new_wheel_scroll_multiplier: float) -> None
```

x.set_wheel_scroll_multiplier(new_wheel_scroll_multiplier) -> None
Set Wheel Scroll Multiplier

Args:
    new_wheel_scroll_multiplier (float):

<a id="unreal.ListViewBase.set_scroll_offset"></a>

#### set_scroll_offset

```python
def set_scroll_offset(scroll_offset: float) -> None
```

x.set_scroll_offset(scroll_offset) -> None
Set the scroll offset of this view (in items)

Args:
    scroll_offset (float):

<a id="unreal.ListViewBase.set_scrollbar_visibility"></a>

#### set_scrollbar_visibility

```python
def set_scrollbar_visibility(visibility: SlateVisibility) -> None
```

x.set_scrollbar_visibility(visibility) -> None
Set Scrollbar Visibility

Args:
    visibility (SlateVisibility):

<a id="unreal.ListViewBase.set_is_pointer_scrolling_enabled"></a>

#### set_is_pointer_scrolling_enabled

```python
def set_is_pointer_scrolling_enabled(
        is_pointer_scrolling_enabled: bool) -> None
```

x.set_is_pointer_scrolling_enabled(is_pointer_scrolling_enabled) -> None
Enable/Disable the ability of the list to scroll. This should be use as a temporary disable.

Args:
    is_pointer_scrolling_enabled (bool):

<a id="unreal.ListViewBase.set_is_gamepad_scrolling_enabled"></a>

#### set_is_gamepad_scrolling_enabled

```python
def set_is_gamepad_scrolling_enabled(
        is_gamepad_scrolling_enabled: bool) -> None
```

x.set_is_gamepad_scrolling_enabled(is_gamepad_scrolling_enabled) -> None
Enable/Disable the ability of the list to scroll via gamepad.

Args:
    is_gamepad_scrolling_enabled (bool):

<a id="unreal.ListViewBase.scroll_to_top"></a>

#### scroll_to_top

```python
def scroll_to_top() -> None
```

x.scroll_to_top() -> None
Scroll the entire list up to the first item

<a id="unreal.ListViewBase.scroll_to_bottom"></a>

#### scroll_to_bottom

```python
def scroll_to_bottom() -> None
```

x.scroll_to_bottom() -> None
Scroll the entire list down to the bottom-most item

<a id="unreal.ListViewBase.request_refresh"></a>

#### request_refresh

```python
def request_refresh() -> None
```

x.request_refresh() -> None
Sets the list to refresh on the next tick.

Note that refreshing, from a list perspective, is limited to accounting for discrepancies between items and entries.
In other words, it will only release entries that no longer have items and generate entries for new items (or newly visible items).

It does NOT account for changes within existing items - that is up to the item to announce and an entry to listen to as needed.
This can be onerous to set up for simple cases, so it's also reasonable (though not ideal) to call RegenerateAllEntries when changes within N list items need to be reflected.

<a id="unreal.ListViewBase.regenerate_all_entries"></a>

#### regenerate_all_entries

```python
def regenerate_all_entries() -> None
```

x.regenerate_all_entries() -> None
Full regeneration of all entries in the list. Note that the entry UWidget instances will not be destroyed, but they will be released and re-generated.
In other words, entry widgets will not receive Destruct/Construct events. They will receive OnEntryReleased and IUserObjectListEntry implementations will receive OnListItemObjectSet.

<a id="unreal.ListViewBase.get_scroll_offset"></a>

#### get_scroll_offset

```python
def get_scroll_offset() -> float
```

x.get_scroll_offset() -> float
Get the scroll offset of this view (in items)

Returns:
    float:

<a id="unreal.ListViewBase.get_displayed_entry_widgets"></a>

#### get_displayed_entry_widgets

```python
def get_displayed_entry_widgets() -> Array[UserWidget]
```

x.get_displayed_entry_widgets() -> Array[UserWidget]
Gets all of the list entry widgets currently being displayed by the list

Returns:
    Array[UserWidget]:

<a id="unreal.ListViewBase.end_inertial_scrolling"></a>

#### end_inertial_scrolling

```python
def end_inertial_scrolling() -> None
```

x.end_inertial_scrolling() -> None
Stops the scroll inertia

<a id="unreal.ListView"></a>