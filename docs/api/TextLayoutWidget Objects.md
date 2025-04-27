## TextLayoutWidget Objects

```python
class TextLayoutWidget(Widget)
```

Base class for all widgets that use a text layout.
Contains the common options that should be exposed for the underlying Slate widget.

**C++ Source:**

- **Module**: UMG
- **File**: TextWidgetTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``apply_line_height_to_bottom_line`` (bool):  [Read-Write] Whether to leave extra space below the last line due to line height.
- ``auto_wrap_text`` (bool):  [Read-Write] True if we're wrapping text automatically based on the computed horizontal space for this widget.
- ``can_children_be_accessible`` (bool):  [Read-Write] Whether or not children of this widget can appear as distinct accessible widgets.
- ``clipping`` (WidgetClipping):  [Read-Write] Controls how the clipping behavior of this widget.  Normally content that overflows the
  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content
  from being seen.

  NOTE: Elements in different clipping spaces can not be batched together, and so there is a
  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent
  content from showing up outside its bounds.
- ``cursor`` (MouseCursor):  [Read-Write] The cursor to show when the mouse is over the widget
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``justification`` (TextJustify):  [Read-Write] How the text should be aligned with the margin.
- ``line_height_percentage`` (float):  [Read-Write] The amount to scale each lines height by.
- ``margin`` (Margin):  [Read-Write] The amount of blank space left around the edges of text area.
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``shaped_text_options`` (ShapedTextOptions):  [Read-Write] Controls how the text within this widget should be shaped.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``wrap_text_at`` (float):  [Read-Write] Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs.
- ``wrapping_policy`` (TextWrappingPolicy):  [Read-Write] The wrapping policy to use.

<a id="unreal.TextLayoutWidget.shaped_text_options"></a>

#### shaped_text_options

```python
@property
def shaped_text_options() -> ShapedTextOptions
```

(ShapedTextOptions):  [Read-Write] Controls how the text within this widget should be shaped.

<a id="unreal.TextLayoutWidget.shaped_text_options"></a>

#### shaped_text_options

```python
@shaped_text_options.setter
def shaped_text_options(value: ShapedTextOptions) -> None
```

<a id="unreal.TextLayoutWidget.justification"></a>

#### justification

```python
@property
def justification() -> TextJustify
```

(TextJustify):  [Read-Write] How the text should be aligned with the margin.

<a id="unreal.TextLayoutWidget.justification"></a>

#### justification

```python
@justification.setter
def justification(value: TextJustify) -> None
```

<a id="unreal.TextLayoutWidget.wrapping_policy"></a>

#### wrapping_policy

```python
@property
def wrapping_policy() -> TextWrappingPolicy
```

(TextWrappingPolicy):  [Read-Write] The wrapping policy to use.

<a id="unreal.TextLayoutWidget.wrapping_policy"></a>

#### wrapping_policy

```python
@wrapping_policy.setter
def wrapping_policy(value: TextWrappingPolicy) -> None
```

<a id="unreal.TextLayoutWidget.auto_wrap_text"></a>

#### auto_wrap_text

```python
@property
def auto_wrap_text() -> bool
```

(bool):  [Read-Write] True if we're wrapping text automatically based on the computed horizontal space for this widget.

<a id="unreal.TextLayoutWidget.auto_wrap_text"></a>

#### auto_wrap_text

```python
@auto_wrap_text.setter
def auto_wrap_text(value: bool) -> None
```

<a id="unreal.TextLayoutWidget.apply_line_height_to_bottom_line"></a>

#### apply_line_height_to_bottom_line

```python
@property
def apply_line_height_to_bottom_line() -> bool
```

(bool):  [Read-Write] Whether to leave extra space below the last line due to line height.

<a id="unreal.TextLayoutWidget.apply_line_height_to_bottom_line"></a>

#### apply_line_height_to_bottom_line

```python
@apply_line_height_to_bottom_line.setter
def apply_line_height_to_bottom_line(value: bool) -> None
```

<a id="unreal.TextLayoutWidget.wrap_text_at"></a>

#### wrap_text_at

```python
@property
def wrap_text_at() -> float
```

(float):  [Read-Write] Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs.

<a id="unreal.TextLayoutWidget.wrap_text_at"></a>

#### wrap_text_at

```python
@wrap_text_at.setter
def wrap_text_at(value: float) -> None
```

<a id="unreal.TextLayoutWidget.margin"></a>

#### margin

```python
@property
def margin() -> Margin
```

(Margin):  [Read-Write] The amount of blank space left around the edges of text area.

<a id="unreal.TextLayoutWidget.margin"></a>

#### margin

```python
@margin.setter
def margin(value: Margin) -> None
```

<a id="unreal.TextLayoutWidget.line_height_percentage"></a>

#### line_height_percentage

```python
@property
def line_height_percentage() -> float
```

(float):  [Read-Write] The amount to scale each lines height by.

<a id="unreal.TextLayoutWidget.line_height_percentage"></a>

#### line_height_percentage

```python
@line_height_percentage.setter
def line_height_percentage(value: float) -> None
```

<a id="unreal.MultiLineEditableText"></a>