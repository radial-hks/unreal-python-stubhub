## WidgetLayoutLibrary Objects

```python
class WidgetLayoutLibrary(BlueprintFunctionLibrary)
```

Widget Layout Library

**C++ Source:**

- **Module**: UMG
- **File**: WidgetLayoutLibrary.h

<a id="unreal.WidgetLayoutLibrary.slot_as_wrap_box_slot"></a>

#### slot_as_wrap_box_slot

```python
@classmethod
def slot_as_wrap_box_slot(cls, widget: Widget) -> WrapBoxSlot
```

X.slot_as_wrap_box_slot(widget) -> WrapBoxSlot
Gets the slot object on the child widget as a Wrap Box Slot, allowing you to manipulate its information.

Args:
    widget (Widget): The child widget of a Wrap Box.

Returns:
    WrapBoxSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_widget_switcher_slot"></a>

#### slot_as_widget_switcher_slot

```python
@classmethod
def slot_as_widget_switcher_slot(cls, widget: Widget) -> WidgetSwitcherSlot
```

X.slot_as_widget_switcher_slot(widget) -> WidgetSwitcherSlot
Gets the slot object on the child widget as a Widget Switcher Slot, allowing you to manipulate its information.

Args:
    widget (Widget): The child widget of a Widget Switcher Slot.

Returns:
    WidgetSwitcherSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_vertical_box_slot"></a>

#### slot_as_vertical_box_slot

```python
@classmethod
def slot_as_vertical_box_slot(cls, widget: Widget) -> VerticalBoxSlot
```

X.slot_as_vertical_box_slot(widget) -> VerticalBoxSlot
Gets the slot object on the child widget as a Vertical Box Slot, allowing you to manipulate its information.

Args:
    widget (Widget): The child widget of a Vertical Box.

Returns:
    VerticalBoxSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_uniform_grid_slot"></a>

#### slot_as_uniform_grid_slot

```python
@classmethod
def slot_as_uniform_grid_slot(cls, widget: Widget) -> UniformGridSlot
```

X.slot_as_uniform_grid_slot(widget) -> UniformGridSlot
Gets the slot object on the child widget as a Uniform Grid Slot, allowing you to manipulate layout information.

Args:
    widget (Widget): The child widget of a uniform grid panel.

Returns:
    UniformGridSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_size_box_slot"></a>

#### slot_as_size_box_slot

```python
@classmethod
def slot_as_size_box_slot(cls, widget: Widget) -> SizeBoxSlot
```

X.slot_as_size_box_slot(widget) -> SizeBoxSlot
Gets the slot object on the child widget as a Size Box Slot, allowing you to manipulate its information.

Args:
    widget (Widget): The child widget of a Size Box.

Returns:
    SizeBoxSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_scroll_box_slot"></a>

#### slot_as_scroll_box_slot

```python
@classmethod
def slot_as_scroll_box_slot(cls, widget: Widget) -> ScrollBoxSlot
```

X.slot_as_scroll_box_slot(widget) -> ScrollBoxSlot
Gets the slot object on the child widget as a Scroll Box Slot, allowing you to manipulate its information.

Args:
    widget (Widget): The child widget of a Scroll Box.

Returns:
    ScrollBoxSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_scale_box_slot"></a>

#### slot_as_scale_box_slot

```python
@classmethod
def slot_as_scale_box_slot(cls, widget: Widget) -> ScaleBoxSlot
```

X.slot_as_scale_box_slot(widget) -> ScaleBoxSlot
Gets the slot object on the child widget as a Scale Box Slot, allowing you to manipulate its information.

Args:
    widget (Widget): The child widget of a Scale Box.

Returns:
    ScaleBoxSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_safe_box_slot"></a>

#### slot_as_safe_box_slot

```python
@classmethod
def slot_as_safe_box_slot(cls, widget: Widget) -> SafeZoneSlot
```

X.slot_as_safe_box_slot(widget) -> SafeZoneSlot
Gets the slot object on the child widget as a Safe Box Slot, allowing you to manipulate its information.

Args:
    widget (Widget): The child widget of a Safe Box.

Returns:
    SafeZoneSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_overlay_slot"></a>

#### slot_as_overlay_slot

```python
@classmethod
def slot_as_overlay_slot(cls, widget: Widget) -> OverlaySlot
```

X.slot_as_overlay_slot(widget) -> OverlaySlot
Gets the slot object on the child widget as a Overlay Slot, allowing you to manipulate layout information.

Args:
    widget (Widget): The child widget of a overlay panel.

Returns:
    OverlaySlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_horizontal_box_slot"></a>

#### slot_as_horizontal_box_slot

```python
@classmethod
def slot_as_horizontal_box_slot(cls, widget: Widget) -> HorizontalBoxSlot
```

X.slot_as_horizontal_box_slot(widget) -> HorizontalBoxSlot
Gets the slot object on the child widget as a Horizontal Box Slot, allowing you to manipulate its information.

Args:
    widget (Widget): The child widget of a Horizontal Box.

Returns:
    HorizontalBoxSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_grid_slot"></a>

#### slot_as_grid_slot

```python
@classmethod
def slot_as_grid_slot(cls, widget: Widget) -> GridSlot
```

X.slot_as_grid_slot(widget) -> GridSlot
Gets the slot object on the child widget as a Grid Slot, allowing you to manipulate layout information.

Args:
    widget (Widget): The child widget of a grid panel.

Returns:
    GridSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_canvas_slot"></a>

#### slot_as_canvas_slot

```python
@classmethod
def slot_as_canvas_slot(cls, widget: Widget) -> CanvasPanelSlot
```

X.slot_as_canvas_slot(widget) -> CanvasPanelSlot
Gets the slot object on the child widget as a Canvas Slot, allowing you to manipulate layout information.

Args:
    widget (Widget): The child widget of a canvas panel.

Returns:
    CanvasPanelSlot:

<a id="unreal.WidgetLayoutLibrary.slot_as_border_slot"></a>

#### slot_as_border_slot

```python
@classmethod
def slot_as_border_slot(cls, widget: Widget) -> BorderSlot
```

X.slot_as_border_slot(widget) -> BorderSlot
Gets the slot object on the child widget as a Border Slot, allowing you to manipulate layout information.

Args:
    widget (Widget): The child widget of a border panel.

Returns:
    BorderSlot:

<a id="unreal.WidgetLayoutLibrary.remove_all_widgets"></a>

#### remove_all_widgets

```python
@classmethod
def remove_all_widgets(cls, world_context_object: Object) -> None
```

X.remove_all_widgets(world_context_object) -> None
Removes all widgets from the viewport.

Args:
    world_context_object (Object):

<a id="unreal.WidgetLayoutLibrary.project_world_location_to_widget_position"></a>

#### project_world_location_to_widget_position

```python
@classmethod
def project_world_location_to_widget_position(
        cls, player_controller: PlayerController, world_location: Vector,
        player_viewport_relative: bool) -> Optional[Vector2D]
```

X.project_world_location_to_widget_position(player_controller, world_location, player_viewport_relative) -> Vector2D or None
Gets the projected world to screen position for a player, then converts it into a widget
position, which takes into account any quality scaling.

Args:
    player_controller (PlayerController): The player controller to project the position in the world to their screen.
    world_location (Vector): The world location to project from.
    player_viewport_relative (bool): Should this be relative to the player viewport subregion (useful when using player attached widgets in split screen or when aspect-ratio constrained)

Returns:
    Vector2D or None: true if the position projects onto the screen.

    screen_position (Vector2D): The position in the viewport with quality scale removed and DPI scale remove.

<a id="unreal.WidgetLayoutLibrary.get_viewport_widget_geometry"></a>

#### get_viewport_widget_geometry

```python
@classmethod
def get_viewport_widget_geometry(cls,
                                 world_context_object: Object) -> Geometry
```

X.get_viewport_widget_geometry(world_context_object) -> Geometry
Gets the geometry of the widget holding all widgets added to the "Viewport".  You
can use this geometry to convert between absolute and local space of widgets held on this
widget.

Args:
    world_context_object (Object): 

Returns:
    Geometry:

<a id="unreal.WidgetLayoutLibrary.get_viewport_size"></a>

#### get_viewport_size

```python
@classmethod
def get_viewport_size(cls, world_context_object: Object) -> Vector2D
```

X.get_viewport_size(world_context_object) -> Vector2D
Gets the size of the game viewport.

Args:
    world_context_object (Object): 

Returns:
    Vector2D:

<a id="unreal.WidgetLayoutLibrary.get_viewport_scale"></a>

#### get_viewport_scale

```python
@classmethod
def get_viewport_scale(cls, world_context_object: Object) -> float
```

X.get_viewport_scale(world_context_object) -> float
Gets the current DPI Scale being applied to the viewport and all the Widgets.

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.WidgetLayoutLibrary.get_player_screen_widget_geometry"></a>

#### get_player_screen_widget_geometry

```python
@classmethod
def get_player_screen_widget_geometry(
        cls, player_controller: PlayerController) -> Geometry
```

X.get_player_screen_widget_geometry(player_controller) -> Geometry
Gets the geometry of the widget holding all widgets added to the "Player Screen". You
can use this geometry to convert between absolute and local space of widgets held on this
widget.

Args:
    player_controller (PlayerController): 

Returns:
    Geometry:

<a id="unreal.WidgetLayoutLibrary.get_mouse_position_scaled_by_dpi"></a>

#### get_mouse_position_scaled_by_dpi

```python
@classmethod
def get_mouse_position_scaled_by_dpi(
        cls, player: PlayerController) -> Optional[Tuple[float, float]]
```

X.get_mouse_position_scaled_by_dpi(player) -> (location_x=float, location_y=float) or None
Gets the mouse position of the player controller, scaled by the DPI.  If you're trying to go from raw mouse screenspace coordinates
to fullscreen widget space, you'll need to transform the mouse into DPI Scaled space.  This function performs that scaling.

MousePositionScaledByDPI = MousePosition * (1 / ViewportScale).
        //UE_DEPRECATED(4.17, "Use GetMousePositionOnViewport() instead.  Optionally and for more options, you can use GetViewportWidgetGeometry and GetPlayerScreenWidgetGeometry are newly introduced to give you the geometry of the viewport and the player screen for widgets to help convert between spaces.")

Args:
    player (PlayerController): 

Returns:
    tuple or None: 

    location_x (float): 

    location_y (float):

<a id="unreal.WidgetLayoutLibrary.get_mouse_position_on_viewport"></a>

#### get_mouse_position_on_viewport

```python
@classmethod
def get_mouse_position_on_viewport(cls,
                                   world_context_object: Object) -> Vector2D
```

X.get_mouse_position_on_viewport(world_context_object) -> Vector2D
Gets the platform's mouse cursor position in the local space of the viewport widget.

Args:
    world_context_object (Object): 

Returns:
    Vector2D:

<a id="unreal.WidgetLayoutLibrary.get_mouse_position_on_platform"></a>

#### get_mouse_position_on_platform

```python
@classmethod
def get_mouse_position_on_platform(cls) -> Vector2D
```

X.get_mouse_position_on_platform() -> Vector2D
Gets the platform's mouse cursor position.  This is the 'absolute' desktop location of the mouse.

Returns:
    Vector2D:

<a id="unreal.ClothingAssetBase"></a>