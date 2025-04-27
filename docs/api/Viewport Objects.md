## Viewport Objects

```python
class Viewport(ContentWidget)
```

Viewport

**C++ Source:**

- **Module**: UMG
- **File**: Viewport.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accessible_behavior`` (SlateAccessibleBehavior):  [Read-Write] Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.
- ``accessible_summary_behavior`` (SlateAccessibleBehavior):  [Read-Write] How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.
- ``accessible_summary_text`` (Text):  [Read-Write] When AccessibleSummaryBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``accessible_text`` (Text):  [Read-Write] When AccessibleBehavior is set to Custom, this is the text that will be used to describe the widget.
- ``background_color`` (LinearColor):  [Read-Write]
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
- ``pixel_snapping`` (WidgetPixelSnapping):  [Read-Write] If the widget will draw snapped to the nearest pixel.  Improves clarity but might cause visibile stepping in animation
- ``render_opacity`` (float):  [Read-Write] The opacity of the widget
- ``render_transform`` (WidgetTransform):  [Read-Write] The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget.
- ``render_transform_pivot`` (Vector2D):  [Read-Write] The render transform pivot controls the location about which transforms are applied.
  This value is a normalized coordinate about which things like rotations will occur.
- ``slot`` (PanelSlot):  [Read-Write] The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget.
- ``tool_tip_text`` (Text):  [Read-Write] Tooltip text to show when the user hovers over the widget with the mouse
- ``tool_tip_widget`` (Widget):  [Read-Only] Tooltip widget to show when the user hovers over the widget with the mouse
- ``visibility`` (SlateVisibility):  [Read-Write] The visibility of the widget

<a id="unreal.Viewport.background_color"></a>

#### background_color

```python
@property
def background_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.Viewport.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: LinearColor) -> None
```

<a id="unreal.Viewport.spawn"></a>

#### spawn

```python
def spawn(actor_class: Class) -> Actor
```

x.spawn(actor_class) -> Actor
Spawn

Args:
    actor_class (type(Class)): 

Returns:
    Actor:

<a id="unreal.Viewport.set_view_rotation"></a>

#### set_view_rotation

```python
def set_view_rotation(rotation: Rotator) -> None
```

x.set_view_rotation(rotation) -> None
Set View Rotation

Args:
    rotation (Rotator):

<a id="unreal.Viewport.set_view_location"></a>

#### set_view_location

```python
def set_view_location(location: Vector) -> None
```

x.set_view_location(location) -> None
Set View Location

Args:
    location (Vector):

<a id="unreal.Viewport.set_sky_intensity"></a>

#### set_sky_intensity

```python
def set_sky_intensity(light_intensity: float) -> None
```

x.set_sky_intensity(light_intensity) -> None
Set Sky Intensity

Args:
    light_intensity (float):

<a id="unreal.Viewport.set_show_flag"></a>

#### set_show_flag

```python
def set_show_flag(show_flag_name: str, value: bool) -> None
```

x.set_show_flag(show_flag_name, value) -> None
Set Show Flag

Args:
    show_flag_name (str): 
    value (bool):

<a id="unreal.Viewport.set_light_intensity"></a>

#### set_light_intensity

```python
def set_light_intensity(light_intensity: float) -> None
```

x.set_light_intensity(light_intensity) -> None
Set Light Intensity

Args:
    light_intensity (float):

<a id="unreal.Viewport.set_enable_advanced_features"></a>

#### set_enable_advanced_features

```python
def set_enable_advanced_features(enable_advanced_features: bool) -> None
```

x.set_enable_advanced_features(enable_advanced_features) -> None
Set Enable Advanced Features

Args:
    enable_advanced_features (bool):

<a id="unreal.Viewport.get_view_rotation"></a>

#### get_view_rotation

```python
def get_view_rotation() -> Rotator
```

x.get_view_rotation() -> Rotator
Get View Rotation

Returns:
    Rotator:

<a id="unreal.Viewport.get_viewport_world"></a>

#### get_viewport_world

```python
def get_viewport_world() -> World
```

x.get_viewport_world() -> World
Get Viewport World

Returns:
    World:

<a id="unreal.Viewport.get_view_location"></a>

#### get_view_location

```python
def get_view_location() -> Vector
```

x.get_view_location() -> Vector
Get View Location

Returns:
    Vector:

<a id="unreal.WidgetInteractionComponent"></a>