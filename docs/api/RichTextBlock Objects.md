## RichTextBlock Objects

```python
class RichTextBlock(TextLayoutWidget)
```

The rich text block

* Fancy Text
* No Children

**C++ Source:**

- **Module**: UMG
- **File**: RichTextBlock.h

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
- ``decorator_classes`` (Array[type(Class)]):  [Read-Write]
- ``default_text_style_override`` (TextBlockStyle):  [Read-Write] Text style to apply by default to text in this block
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
- ``justification`` (TextJustify):  [Read-Write] How the text should be aligned with the margin.
- ``line_height_percentage`` (float):  [Read-Write] The amount to scale each lines height by.
- ``margin`` (Margin):  [Read-Write] The amount of blank space left around the edges of text area.
- ``min_desired_width`` (float):  [Read-Write] The minimum desired size for the text
- ``navigation`` (WidgetNavigation):  [Read-Write] The navigation object for this widget is optionally created if the user has configured custom
  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions
  can occur between widgets.
- ``override_accessible_defaults`` (bool):  [Read-Write] Override all of the default accessibility behavior and text for this widget.
- ``override_cursor`` (bool):  [Read-Write]
- ``override_default_style`` (bool):  [Read-Write] True to specify the default text style for this rich text inline, overriding any default provided in the style set table
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``shaped_text_options`` (ShapedTextOptions):  [Read-Write] Controls how the text within this widget should be shaped.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``text`` (Text):  [Read-Write] The text to display
- ``text_overflow_policy`` (TextOverflowPolicy):  [Read-Write] Sets what happens to text that is clipped and doesn't fit within the clip rect for this widget
- ``text_style_set`` (DataTable):  [Read-Write]
- ``text_transform_policy`` (TextTransformPolicy):  [Read-Write] The text transformation policy to apply to this text block
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget
- ``wrap_text_at`` (float):  [Read-Write] Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs.
- ``wrapping_policy`` (TextWrappingPolicy):  [Read-Write] The wrapping policy to use.

<a id="unreal.RichTextBlock.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write] The text to display

<a id="unreal.RichTextBlock.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.RichTextBlock.text_style_set"></a>

#### text_style_set

```python
@property
def text_style_set() -> DataTable
```

(DataTable):  [Read-Write]

<a id="unreal.RichTextBlock.text_style_set"></a>

#### text_style_set

```python
@text_style_set.setter
def text_style_set(value: DataTable) -> None
```

<a id="unreal.RichTextBlock.default_text_style_override"></a>

#### default_text_style_override

```python
@property
def default_text_style_override() -> TextBlockStyle
```

(TextBlockStyle):  [Read-Write] Text style to apply by default to text in this block

<a id="unreal.RichTextBlock.default_text_style_override"></a>

#### default_text_style_override

```python
@default_text_style_override.setter
def default_text_style_override(value: TextBlockStyle) -> None
```

<a id="unreal.RichTextBlock.min_desired_width"></a>

#### min_desired_width

```python
@property
def min_desired_width() -> float
```

(float):  [Read-Write] The minimum desired size for the text

<a id="unreal.RichTextBlock.min_desired_width"></a>

#### min_desired_width

```python
@min_desired_width.setter
def min_desired_width(value: float) -> None
```

<a id="unreal.RichTextBlock.text_transform_policy"></a>

#### text_transform_policy

```python
@property
def text_transform_policy() -> TextTransformPolicy
```

(TextTransformPolicy):  [Read-Write] The text transformation policy to apply to this text block

<a id="unreal.RichTextBlock.text_transform_policy"></a>

#### text_transform_policy

```python
@text_transform_policy.setter
def text_transform_policy(value: TextTransformPolicy) -> None
```

<a id="unreal.RichTextBlock.text_overflow_policy"></a>

#### text_overflow_policy

```python
@property
def text_overflow_policy() -> TextOverflowPolicy
```

(TextOverflowPolicy):  [Read-Write] Sets what happens to text that is clipped and doesn't fit within the clip rect for this widget

<a id="unreal.RichTextBlock.text_overflow_policy"></a>

#### text_overflow_policy

```python
@text_overflow_policy.setter
def text_overflow_policy(value: TextOverflowPolicy) -> None
```

<a id="unreal.RichTextBlock.set_text_transform_policy"></a>

#### set_text_transform_policy

```python
def set_text_transform_policy(transform_policy: TextTransformPolicy) -> None
```

x.set_text_transform_policy(transform_policy) -> None
Set the text transformation policy for this text block.

Args:
    transform_policy (TextTransformPolicy): the new text transformation policy.

<a id="unreal.RichTextBlock.set_text_style_set"></a>

#### set_text_style_set

```python
def set_text_style_set(new_text_style_set: DataTable) -> None
```

x.set_text_style_set(new_text_style_set) -> None
Set Text Style Set

Args:
    new_text_style_set (DataTable):

<a id="unreal.RichTextBlock.set_text_overflow_policy"></a>

#### set_text_overflow_policy

```python
def set_text_overflow_policy(overflow_policy: TextOverflowPolicy) -> None
```

x.set_text_overflow_policy(overflow_policy) -> None
Set the text overflow policy for this text block.

Args:
    overflow_policy (TextOverflowPolicy): the new text overflow policy.

<a id="unreal.RichTextBlock.set_text"></a>

#### set_text

```python
def set_text(text: Text) -> None
```

x.set_text(text) -> None
Directly sets the widget text.
Warning: This will wipe any binding created for the Text property!

Args:
    text (Text): The text to assign to the widget

<a id="unreal.RichTextBlock.set_min_desired_width"></a>

#### set_min_desired_width

```python
def set_min_desired_width(min_desired_width: float) -> None
```

x.set_min_desired_width(min_desired_width) -> None
Set the minimum desired width for this rich text block

Args:
    min_desired_width (float): new minimum desired width

<a id="unreal.RichTextBlock.set_default_text_style"></a>

#### set_default_text_style

```python
def set_default_text_style(default_text_style: TextBlockStyle) -> None
```

x.set_default_text_style(default_text_style) -> None
Wholesale override of the currently established default text style

Args:
    default_text_style (TextBlockStyle): The new text style to apply to all default (i.e. undecorated) text in the block

<a id="unreal.RichTextBlock.set_default_strike_brush"></a>

#### set_default_strike_brush

```python
def set_default_strike_brush(strike_brush: SlateBrush) -> None
```

x.set_default_strike_brush(strike_brush) -> None
Dynamically set the default strike brush for this rich text block

Args:
    strike_brush (SlateBrush): The new brush to use to strike through text

<a id="unreal.RichTextBlock.set_default_shadow_offset"></a>

#### set_default_shadow_offset

```python
def set_default_shadow_offset(shadow_offset: Vector2D) -> None
```

x.set_default_shadow_offset(shadow_offset) -> None
Sets the offset that the default text drop shadow should be drawn at

Args:
    shadow_offset (Vector2D): The new offset

<a id="unreal.RichTextBlock.set_default_shadow_color_and_opacity"></a>

#### set_default_shadow_color_and_opacity

```python
def set_default_shadow_color_and_opacity(
        shadow_color_and_opacity: LinearColor) -> None
```

x.set_default_shadow_color_and_opacity(shadow_color_and_opacity) -> None
Sets the color and opacity of the default text drop shadow
Note: if opacity is zero no shadow will be drawn

Args:
    shadow_color_and_opacity (LinearColor): The new drop shadow color and opacity

<a id="unreal.RichTextBlock.set_default_material"></a>

#### set_default_material

```python
def set_default_material(material: MaterialInterface) -> None
```

x.set_default_material(material) -> None
Set Default Material

Args:
    material (MaterialInterface):

<a id="unreal.RichTextBlock.set_default_font"></a>

#### set_default_font

```python
def set_default_font(font_info: SlateFontInfo) -> None
```

x.set_default_font(font_info) -> None
Dynamically set the default font info for this rich text block

Args:
    font_info (SlateFontInfo): The new font info

<a id="unreal.RichTextBlock.set_default_color_and_opacity"></a>

#### set_default_color_and_opacity

```python
def set_default_color_and_opacity(color_and_opacity: SlateColor) -> None
```

x.set_default_color_and_opacity(color_and_opacity) -> None
Sets the color and opacity of the default text in this rich text block

Args:
    color_and_opacity (SlateColor): The new text color and opacity

<a id="unreal.RichTextBlock.set_decorators"></a>

#### set_decorators

```python
def set_decorators(decorator_classes: Array[Class]) -> None
```

x.set_decorators(decorator_classes) -> None
Replaces the existing decorators with the list provided

Args:
    decorator_classes (Array[type(Class)]):

<a id="unreal.RichTextBlock.set_auto_wrap_text"></a>

#### set_auto_wrap_text

```python
def set_auto_wrap_text(auto_text_wrap: bool) -> None
```

x.set_auto_wrap_text(auto_text_wrap) -> None
Set the auto wrap for this rich text block

Args:
    auto_text_wrap (bool): to turn wrap on or off

<a id="unreal.RichTextBlock.refresh_text_layout"></a>

#### refresh_text_layout

```python
def refresh_text_layout() -> None
```

x.refresh_text_layout() -> None
Causes the text to reflow it's layout and re-evaluate any decorators

<a id="unreal.RichTextBlock.get_text_style_set"></a>

#### get_text_style_set

```python
def get_text_style_set() -> DataTable
```

x.get_text_style_set() -> DataTable
Get Text Style Set

Returns:
    DataTable:

<a id="unreal.RichTextBlock.get_text"></a>

#### get_text

```python
def get_text() -> Text
```

x.get_text() -> Text
Returns widgets text.

Returns:
    Text:

<a id="unreal.RichTextBlock.get_default_dynamic_material"></a>

#### get_default_dynamic_material

```python
def get_default_dynamic_material() -> MaterialInstanceDynamic
```

x.get_default_dynamic_material() -> MaterialInstanceDynamic
Creates a dynamic material for the default font or returns it if it already
exists

Returns:
    MaterialInstanceDynamic:

<a id="unreal.RichTextBlock.get_decorator_by_class"></a>

#### get_decorator_by_class

```python
def get_decorator_by_class(decorator_class: Class) -> RichTextBlockDecorator
```

x.get_decorator_by_class(decorator_class) -> RichTextBlockDecorator
Get Decorator by Class

Args:
    decorator_class (type(Class)): 

Returns:
    RichTextBlockDecorator:

<a id="unreal.RichTextBlock.clear_all_default_style_overrides"></a>

#### clear_all_default_style_overrides

```python
def clear_all_default_style_overrides() -> None
```

x.clear_all_default_style_overrides() -> None
Remove all overrides made to the default text style and return to the style specified in the style set data table

<a id="unreal.RichTextBlockDecorator"></a>