## DynamicEntryBoxBase Objects

```python
class DynamicEntryBoxBase(Widget)
```

Base for widgets that support a dynamic number of auto-generated entries at both design- and run-time.
Contains all functionality needed to create, construct, and cache an arbitrary number of entry widgets, but exposes no means of entry creation or removal
It's up to child classes to decide how they want to perform the population (some may do so entirely on their own without exposing a thing)
see: UDynamicEntryBox for a ready-to-use version

**C++ Source:**

- **Module**: UMG
- **File**: DynamicEntryBoxBase.h

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

<a id="unreal.DynamicEntryBoxBase.entry_spacing"></a>

#### entry_spacing

```python
@property
def entry_spacing() -> Vector2D
```

(Vector2D):  [Read-Write] The padding to apply between entries in the box.
Note horizontal boxes only use the X and vertical boxes only use Y. Value is also ignored for the first entry in the box.
Wrap and Overlay types use both X and Y for spacing.

<a id="unreal.DynamicEntryBoxBase.entry_spacing"></a>

#### entry_spacing

```python
@entry_spacing.setter
def entry_spacing(value: Vector2D) -> None
```

<a id="unreal.DynamicEntryBoxBase.spacing_pattern"></a>

#### spacing_pattern

```python
@property
def spacing_pattern() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Only] The looping sequence of entry paddings to apply as entries are created. Overlay boxes only. Ignores EntrySpacing if not empty.

<a id="unreal.DynamicEntryBoxBase.entry_box_type"></a>

#### entry_box_type

```python
@property
def entry_box_type() -> DynamicBoxType
```

(DynamicBoxType):  [Read-Only] The type of box panel into which created entries are added. Some differences in functionality exist between each type.

<a id="unreal.DynamicEntryBoxBase.entry_size_rule"></a>

#### entry_size_rule

```python
@property
def entry_size_rule() -> SlateChildSize
```

(SlateChildSize):  [Read-Only] Sizing rule to apply to generated entries. Horizontal/Vertical boxes only.

<a id="unreal.DynamicEntryBoxBase.entry_horizontal_alignment"></a>

#### entry_horizontal_alignment

```python
@property
def entry_horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Only] Horizontal alignment of generated entries. Horizontal/Vertical/Wrap boxes only.

<a id="unreal.DynamicEntryBoxBase.entry_vertical_alignment"></a>

#### entry_vertical_alignment

```python
@property
def entry_vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Only] Vertical alignment of generated entries. Horizontal/Vertical/Wrap boxes only.

<a id="unreal.DynamicEntryBoxBase.max_element_size"></a>

#### max_element_size

```python
@property
def max_element_size() -> int
```

(int32):  [Read-Only] The maximum size of each entry in the dominant axis of the box. Vertical/Horizontal boxes only.

<a id="unreal.DynamicEntryBoxBase.radial_box_settings"></a>

#### radial_box_settings

```python
@property
def radial_box_settings() -> RadialBoxSettings
```

(RadialBoxSettings):  [Read-Write] Settings only relevant to RadialBox

<a id="unreal.DynamicEntryBoxBase.radial_box_settings"></a>

#### radial_box_settings

```python
@radial_box_settings.setter
def radial_box_settings(value: RadialBoxSettings) -> None
```

<a id="unreal.DynamicEntryBoxBase.set_radial_settings"></a>

#### set_radial_settings

```python
def set_radial_settings(settings: RadialBoxSettings) -> None
```

x.set_radial_settings(settings) -> None
Set Radial Settings

Args:
    settings (RadialBoxSettings):

<a id="unreal.DynamicEntryBoxBase.set_entry_spacing"></a>

#### set_entry_spacing

```python
def set_entry_spacing(entry_spacing: Vector2D) -> None
```

x.set_entry_spacing(entry_spacing) -> None
Set Entry Spacing

Args:
    entry_spacing (Vector2D):

<a id="unreal.DynamicEntryBoxBase.get_num_entries"></a>

#### get_num_entries

```python
def get_num_entries() -> int
```

x.get_num_entries() -> int32
Get Num Entries

Returns:
    int32:

<a id="unreal.DynamicEntryBoxBase.get_all_entries"></a>

#### get_all_entries

```python
def get_all_entries() -> Array[UserWidget]
```

x.get_all_entries() -> Array[UserWidget]
Get All Entries

Returns:
    Array[UserWidget]:

<a id="unreal.DynamicEntryBox"></a>