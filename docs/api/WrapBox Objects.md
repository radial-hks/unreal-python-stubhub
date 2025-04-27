## WrapBox Objects

```python
class WrapBox(PanelWidget)
```

Arranges widgets left-to-right or top-to-bottom dependently of the orientation.  When the widgets exceed the wrapSize it will place widgets on the next line.

* Many Children
* Flows
* Wraps

**C++ Source:**

- **Module**: UMG
- **File**: WrapBox.h

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
- ``explicit_wrap_size`` (bool):  [Read-Write] Use explicit wrap size whenever possible. It greatly simplifies layout calculations and reduces likelihood of "wiggling UI"
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of each line of wrapped content.
- ``inner_slot_padding`` (Vector2D):  [Read-Write] The inner slot padding goes between slots sharing borders
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``orientation`` (Orientation):  [Read-Write] Determines if the Wrap Box should arranges the widgets left-to-right or top-to-bottom
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``wrap_size`` (float):  [Read-Write] When this size is exceeded, elements will start appearing on the next line.

<a id="unreal.WrapBox.inner_slot_padding"></a>

#### inner_slot_padding

```python
@property
def inner_slot_padding() -> Vector2D
```

(Vector2D):  [Read-Write] The inner slot padding goes between slots sharing borders

<a id="unreal.WrapBox.inner_slot_padding"></a>

#### inner_slot_padding

```python
@inner_slot_padding.setter
def inner_slot_padding(value: Vector2D) -> None
```

<a id="unreal.WrapBox.wrap_size"></a>

#### wrap_size

```python
@property
def wrap_size() -> float
```

(float):  [Read-Write] When this size is exceeded, elements will start appearing on the next line.

<a id="unreal.WrapBox.wrap_size"></a>

#### wrap_size

```python
@wrap_size.setter
def wrap_size(value: float) -> None
```

<a id="unreal.WrapBox.explicit_wrap_size"></a>

#### explicit_wrap_size

```python
@property
def explicit_wrap_size() -> bool
```

(bool):  [Read-Write] Use explicit wrap size whenever possible. It greatly simplifies layout calculations and reduces likelihood of "wiggling UI"

<a id="unreal.WrapBox.explicit_wrap_size"></a>

#### explicit_wrap_size

```python
@explicit_wrap_size.setter
def explicit_wrap_size(value: bool) -> None
```

<a id="unreal.WrapBox.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of each line of wrapped content.

<a id="unreal.WrapBox.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.WrapBox.orientation"></a>

#### orientation

```python
@property
def orientation() -> Orientation
```

(Orientation):  [Read-Write] Determines if the Wrap Box should arranges the widgets left-to-right or top-to-bottom

<a id="unreal.WrapBox.orientation"></a>

#### orientation

```python
@orientation.setter
def orientation(value: Orientation) -> None
```

<a id="unreal.WrapBox.set_inner_slot_padding"></a>

#### set_inner_slot_padding

```python
def set_inner_slot_padding(padding: Vector2D) -> None
```

x.set_inner_slot_padding(padding) -> None
Sets the inner slot padding goes between slots sharing borders

Args:
    padding (Vector2D):

<a id="unreal.WrapBox.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.WrapBox.add_child_to_wrap_box"></a>

#### add_child_to_wrap_box

```python
def add_child_to_wrap_box(content: Widget) -> WrapBoxSlot
```

x.add_child_to_wrap_box(content) -> WrapBoxSlot
Add Child to Wrap Box

Args:
    content (Widget): 

Returns:
    WrapBoxSlot:

<a id="unreal.WrapBox.add_child_wrap_box"></a>

#### add_child_wrap_box

```python
def add_child_wrap_box(content: Widget) -> WrapBoxSlot
```

deprecated: 'add_child_wrap_box' was renamed to 'add_child_to_wrap_box'.

<a id="unreal.WrapBoxSlot"></a>