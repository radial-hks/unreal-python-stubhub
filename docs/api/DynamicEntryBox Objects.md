## DynamicEntryBox Objects

```python
class DynamicEntryBox(DynamicEntryBoxBase)
```

A special box panel that auto-generates its entries at both design-time and runtime.
Useful for cases where you can have a varying number of entries, but it isn't worth the effort or conceptual overhead to set up a list/tile view.
Note that entries here are *not* virtualized as they are in the list views, so generally this should be avoided if you intend to scroll through lots of items.

No children can be manually added in the designer - all are auto-generated based on the given entry class.

**C++ Source:**

- **Module**: UMG
- **File**: DynamicEntryBox.h

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
- ``entry_box_type`` (DynamicBoxType):  [Read-Write] The type of box panel into which created entries are added. Some differences in functionality exist between each type.
- ``entry_horizontal_alignment`` (HorizontalAlignment):  [Read-Write] Horizontal alignment of generated entries. Horizontal/Vertical/Wrap boxes only.
- ``entry_size_rule`` (SlateChildSize):  [Read-Write] Sizing rule to apply to generated entries. Horizontal/Vertical boxes only.
- ``entry_spacing`` (Vector2D):  [Read-Write] The padding to apply between entries in the box.
  Note horizontal boxes only use the X and vertical boxes only use Y. Value is also ignored for the first entry in the box.
  Wrap and Overlay types use both X and Y for spacing.
- ``entry_vertical_alignment`` (VerticalAlignment):  [Read-Write] Vertical alignment of generated entries. Horizontal/Vertical/Wrap boxes only.
- ``entry_widget_class`` (type(Class)):  [Read-Write] The class of widget to create entries of.
  If natively binding this widget, use the EntryClass UPROPERTY metadata to specify the desired entry widget base class.
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``max_element_size`` (int32):  [Read-Write] The maximum size of each entry in the dominant axis of the box. Vertical/Horizontal boxes only.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``num_designer_preview_entries`` (int32):  [Read-Write]
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``radial_box_settings`` (RadialBoxSettings):  [Read-Write] Settings only relevant to RadialBox
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``spacing_pattern`` (Array[Vector2D]):  [Read-Write] The looping sequence of entry paddings to apply as entries are created. Overlay boxes only. Ignores EntrySpacing if not empty.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.DynamicEntryBox.entry_widget_class"></a>

#### entry_widget_class

```python
@property
def entry_widget_class() -> Class
```

(type(Class)):  [Read-Only] The class of widget to create entries of.
If natively binding this widget, use the EntryClass UPROPERTY metadata to specify the desired entry widget base class.

<a id="unreal.DynamicEntryBox.reset"></a>

#### reset

```python
def reset(delete_widgets: bool = False) -> None
```

x.reset(delete_widgets=False) -> None
Clear out the box entries, optionally deleting the underlying Slate widgets entirely as well.

Args:
    delete_widgets (bool):

<a id="unreal.DynamicEntryBox.remove_entry"></a>

#### remove_entry

```python
def remove_entry(entry_widget: UserWidget) -> None
```

x.remove_entry(entry_widget) -> None
Remove Entry

Args:
    entry_widget (UserWidget):

<a id="unreal.DynamicEntryBox.bp_create_entry_of_class"></a>

#### bp_create_entry_of_class

```python
def bp_create_entry_of_class(entry_class: Class) -> UserWidget
```

x.bp_create_entry_of_class(entry_class) -> UserWidget
Creates and establishes a new dynamic entry in the box using the specified class instead of the default.

Args:
    entry_class (type(Class)): 

Returns:
    UserWidget:

<a id="unreal.DynamicEntryBox.bp_create_entry"></a>

#### bp_create_entry

```python
def bp_create_entry() -> UserWidget
```

x.bp_create_entry() -> UserWidget
Creates and establishes a new dynamic entry in the box

Returns:
    UserWidget:

<a id="unreal.EditableText"></a>