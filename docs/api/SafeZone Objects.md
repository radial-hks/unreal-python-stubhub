## SafeZone Objects

```python
class SafeZone(ContentWidget)
```

The Safe-Zone widget is an essential part of developing a game UI that can run on lots of different non-PC platforms.
While a modern flat panel computer monitor may not have over scan issues, this is a common occurrence for Consoles.
It's common for TVs to have extra pixels under the bezel, in addition to projectors and projection TVs having potentially
several vertical and horizontal columns of pixels hidden behind or against a black border of the projection screen.

Useful testing console commands to help, simulate the safe zone on PC,
  r.DebugSafeZone.TitleRatio 0.96
  r.DebugActionZone.ActionRatio 0.96

To enable a red band to visualize the safe zone, use this console command,
r.DebugSafeZone.Mode controls the debug visualization overlay (0..2, default 0).
  0: Do not display the safe zone overlay.
  1: Display the overlay for the title safe zone.
  2: Display the overlay for the action safe zone.

**C++ Source:**

- **Module**: UMG
- **File**: SafeZone.h

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
- ``pad_bottom`` (bool):  [Read-Write] If this safe zone should pad for the bottom side of the screen's safe zone
- ``pad_left`` (bool):  [Read-Write] If this safe zone should pad for the left side of the screen's safe zone
- ``pad_right`` (bool):  [Read-Write] If this safe zone should pad for the right side of the screen's safe zone
- ``pad_top`` (bool):  [Read-Write] If this safe zone should pad for the top side of the screen's safe zone
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.SafeZone.pad_left"></a>

#### pad_left

```python
@property
def pad_left() -> bool
```

(bool):  [Read-Write] If this safe zone should pad for the left side of the screen's safe zone

<a id="unreal.SafeZone.pad_left"></a>

#### pad_left

```python
@pad_left.setter
def pad_left(value: bool) -> None
```

<a id="unreal.SafeZone.pad_right"></a>

#### pad_right

```python
@property
def pad_right() -> bool
```

(bool):  [Read-Write] If this safe zone should pad for the right side of the screen's safe zone

<a id="unreal.SafeZone.pad_right"></a>

#### pad_right

```python
@pad_right.setter
def pad_right(value: bool) -> None
```

<a id="unreal.SafeZone.pad_top"></a>

#### pad_top

```python
@property
def pad_top() -> bool
```

(bool):  [Read-Write] If this safe zone should pad for the top side of the screen's safe zone

<a id="unreal.SafeZone.pad_top"></a>

#### pad_top

```python
@pad_top.setter
def pad_top(value: bool) -> None
```

<a id="unreal.SafeZone.pad_bottom"></a>

#### pad_bottom

```python
@property
def pad_bottom() -> bool
```

(bool):  [Read-Write] If this safe zone should pad for the bottom side of the screen's safe zone

<a id="unreal.SafeZone.pad_bottom"></a>

#### pad_bottom

```python
@pad_bottom.setter
def pad_bottom(value: bool) -> None
```

<a id="unreal.SafeZone.set_sides_to_pad"></a>

#### set_sides_to_pad

```python
def set_sides_to_pad(pad_left: bool, pad_right: bool, pad_top: bool,
                     pad_bottom: bool) -> None
```

x.set_sides_to_pad(pad_left, pad_right, pad_top, pad_bottom) -> None
Set Sides to Pad

Args:
    pad_left (bool): 
    pad_right (bool): 
    pad_top (bool): 
    pad_bottom (bool):

<a id="unreal.SafeZoneSlot"></a>