## ScaleBox Objects

```python
class ScaleBox(ContentWidget)
```

Allows you to place content with a desired size and have it scale to meet the constraints placed on this box's alloted area.  If
you needed to have a background image scale to fill an area but not become distorted with different aspect ratios, or if you need
to auto fit some text to an area, this is the control for you.

* Single Child
* Aspect Ratio

**C++ Source:**

- **Module**: UMG
- **File**: ScaleBox.h

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
- ``flow_direction_preference`` (FlowDirectionPreference):  [Read-Write] Allows you to set a new flow direction
- ``ignore_inherited_scale`` (bool):  [Read-Write] Optional bool to ignore the inherited scale. Applies inverse scaling to counteract parents before applying the local scale operation.
- ``is_enabled`` (bool):  [Read-Write] Sets whether this widget can be modified interactively by the user
- ``is_volatile`` (bool):  [Read-Write] If true prevents the widget or its child's geometry or layout information from being cached.  If this widget
  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile
  instead of invalidating it every frame, which would prevent the invalidation panel from actually
  ever caching anything.
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
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``stretch`` (Stretch):  [Read-Write] The stretching rule to apply when content is stretched
- ``stretch_direction`` (StretchDirection):  [Read-Write] Controls in what direction content can be scaled
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``user_specified_scale`` (float):  [Read-Write] Optional scale that can be specified by the User. Used only for UserSpecified stretching.
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.ScaleBox.stretch"></a>

#### stretch

```python
@property
def stretch() -> Stretch
```

(Stretch):  [Read-Write] The stretching rule to apply when content is stretched

<a id="unreal.ScaleBox.stretch"></a>

#### stretch

```python
@stretch.setter
def stretch(value: Stretch) -> None
```

<a id="unreal.ScaleBox.stretch_direction"></a>

#### stretch_direction

```python
@property
def stretch_direction() -> StretchDirection
```

(StretchDirection):  [Read-Write] Controls in what direction content can be scaled

<a id="unreal.ScaleBox.stretch_direction"></a>

#### stretch_direction

```python
@stretch_direction.setter
def stretch_direction(value: StretchDirection) -> None
```

<a id="unreal.ScaleBox.user_specified_scale"></a>

#### user_specified_scale

```python
@property
def user_specified_scale() -> float
```

(float):  [Read-Write] Optional scale that can be specified by the User. Used only for UserSpecified stretching.

<a id="unreal.ScaleBox.user_specified_scale"></a>

#### user_specified_scale

```python
@user_specified_scale.setter
def user_specified_scale(value: float) -> None
```

<a id="unreal.ScaleBox.ignore_inherited_scale"></a>

#### ignore_inherited_scale

```python
@property
def ignore_inherited_scale() -> bool
```

(bool):  [Read-Write] Optional bool to ignore the inherited scale. Applies inverse scaling to counteract parents before applying the local scale operation.

<a id="unreal.ScaleBox.ignore_inherited_scale"></a>

#### ignore_inherited_scale

```python
@ignore_inherited_scale.setter
def ignore_inherited_scale(value: bool) -> None
```

<a id="unreal.ScaleBox.set_user_specified_scale"></a>

#### set_user_specified_scale

```python
def set_user_specified_scale(user_specified_scale: float) -> None
```

x.set_user_specified_scale(user_specified_scale) -> None
Set User Specified Scale

Args:
    user_specified_scale (float):

<a id="unreal.ScaleBox.set_stretch_direction"></a>

#### set_stretch_direction

```python
def set_stretch_direction(stretch_direction: StretchDirection) -> None
```

x.set_stretch_direction(stretch_direction) -> None
Set Stretch Direction

Args:
    stretch_direction (StretchDirection):

<a id="unreal.ScaleBox.set_stretch"></a>

#### set_stretch

```python
def set_stretch(stretch: Stretch) -> None
```

x.set_stretch(stretch) -> None
Set Stretch

Args:
    stretch (Stretch):

<a id="unreal.ScaleBox.set_ignore_inherited_scale"></a>

#### set_ignore_inherited_scale

```python
def set_ignore_inherited_scale(ignore_inherited_scale: bool) -> None
```

x.set_ignore_inherited_scale(ignore_inherited_scale) -> None
Set Ignore Inherited Scale

Args:
    ignore_inherited_scale (bool):

<a id="unreal.ScaleBoxSlot"></a>