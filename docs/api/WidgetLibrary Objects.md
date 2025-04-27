## WidgetLibrary Objects

```python
class WidgetLibrary(BlueprintFunctionLibrary)
```

Widget Blueprint Library

**C++ Source:**

- **Module**: UMG
- **File**: WidgetBlueprintLibrary.h

<a id="unreal.WidgetLibrary.unlock_mouse"></a>

#### unlock_mouse

```python
@classmethod
def unlock_mouse(cls, reply: EventReply) -> Tuple[EventReply, EventReply]
```

X.unlock_mouse(reply) -> (EventReply, reply=EventReply)
Unlock Mouse

Args:
    reply (EventReply): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.unhandled"></a>

#### unhandled

```python
@classmethod
def unhandled(cls) -> EventReply
```

X.unhandled() -> EventReply
The event reply to use when you choose not to handle an event.

Returns:
    EventReply:

<a id="unreal.WidgetLibrary.set_window_title_bar_state"></a>

#### set_window_title_bar_state

```python
@classmethod
def set_window_title_bar_state(cls, title_bar_content: Widget,
                               mode: WindowTitleBarMode,
                               title_bar_drag_enabled: bool,
                               window_buttons_visible: bool,
                               title_bar_visible: bool) -> None
```

X.set_window_title_bar_state(title_bar_content, mode, title_bar_drag_enabled, window_buttons_visible, title_bar_visible) -> None
Set Window Title Bar State

Args:
    title_bar_content (Widget): 
    mode (WindowTitleBarMode): 
    title_bar_drag_enabled (bool): 
    window_buttons_visible (bool): 
    title_bar_visible (bool):

<a id="unreal.WidgetLibrary.set_window_title_bar_on_close_clicked_delegate"></a>

#### set_window_title_bar_on_close_clicked_delegate

```python
@classmethod
def set_window_title_bar_on_close_clicked_delegate(
        cls, delegate: OnGameWindowCloseButtonClickedDelegate) -> None
```

X.set_window_title_bar_on_close_clicked_delegate(delegate) -> None
Set Window Title Bar on Close Clicked Delegate

Args:
    delegate (OnGameWindowCloseButtonClickedDelegate):

<a id="unreal.WidgetLibrary.set_window_title_bar_close_button_active"></a>

#### set_window_title_bar_close_button_active

```python
@classmethod
def set_window_title_bar_close_button_active(cls, active: bool) -> None
```

X.set_window_title_bar_close_button_active(active) -> None
Set Window Title Bar Close Button Active

Args:
    active (bool):

<a id="unreal.WidgetLibrary.set_user_focus"></a>

#### set_user_focus

```python
@classmethod
def set_user_focus(cls,
                   reply: EventReply,
                   focus_widget: Widget,
                   all_users: bool = False) -> Tuple[EventReply, EventReply]
```

X.set_user_focus(reply, focus_widget, all_users=False) -> (EventReply, reply=EventReply)
Set User Focus

Args:
    reply (EventReply): 
    focus_widget (Widget): 
    all_users (bool): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.set_mouse_position"></a>

#### set_mouse_position

```python
@classmethod
def set_mouse_position(
        cls, reply: EventReply,
        new_mouse_position: Vector2D) -> Tuple[EventReply, EventReply]
```

X.set_mouse_position(reply, new_mouse_position) -> (EventReply, reply=EventReply)
Set Mouse Position

Args:
    reply (EventReply): 
    new_mouse_position (Vector2D): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.set_input_mode_ui_only_ex"></a>

#### set_input_mode_ui_only_ex

```python
@classmethod
def set_input_mode_ui_only_ex(
        cls,
        player_controller: PlayerController,
        widget_to_focus: Widget = None,
        mouse_lock_mode: MouseLockMode = MouseLockMode.DO_NOT_LOCK,
        flush_input: bool = False) -> None
```

X.set_input_mode_ui_only_ex(player_controller, widget_to_focus=None, mouse_lock_mode=MouseLockMode.DO_NOT_LOCK, flush_input=False) -> None
Setup an input mode that allows only the UI to respond to user input.

Note: This means that any bound Input Events in the widget will not be called!

Args:
    player_controller (PlayerController): 
    widget_to_focus (Widget): 
    mouse_lock_mode (MouseLockMode): 
    flush_input (bool):

<a id="unreal.WidgetLibrary.set_input_mode_game_only"></a>

#### set_input_mode_game_only

```python
@classmethod
def set_input_mode_game_only(cls,
                             player_controller: PlayerController,
                             flush_input: bool = False) -> None
```

X.set_input_mode_game_only(player_controller, flush_input=False) -> None
Setup an input mode that allows only player input / player controller to respond to user input.

Note: Any bound Input Events in this widget will be called.

Args:
    player_controller (PlayerController): 
    flush_input (bool):

<a id="unreal.WidgetLibrary.set_input_mode_game_and_ui_ex"></a>

#### set_input_mode_game_and_ui_ex

```python
@classmethod
def set_input_mode_game_and_ui_ex(
        cls,
        player_controller: PlayerController,
        widget_to_focus: Widget = None,
        mouse_lock_mode: MouseLockMode = MouseLockMode.DO_NOT_LOCK,
        hide_cursor_during_capture: bool = True,
        flush_input: bool = False) -> None
```

X.set_input_mode_game_and_ui_ex(player_controller, widget_to_focus=None, mouse_lock_mode=MouseLockMode.DO_NOT_LOCK, hide_cursor_during_capture=True, flush_input=False) -> None
Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input / player controller gets a chance.

Note: This means that any bound Input events in the widget will be called.

Args:
    player_controller (PlayerController): 
    widget_to_focus (Widget): 
    mouse_lock_mode (MouseLockMode): 
    hide_cursor_during_capture (bool): 
    flush_input (bool):

<a id="unreal.WidgetLibrary.set_hardware_cursor"></a>

#### set_hardware_cursor

```python
@classmethod
def set_hardware_cursor(cls, world_context_object: Object,
                        cursor_shape: MouseCursor, cursor_name: Name,
                        hot_spot: Vector2D) -> bool
```

X.set_hardware_cursor(world_context_object, cursor_shape, cursor_name, hot_spot) -> bool
Loads or sets a hardware cursor from the content directory in the game.

Args:
    world_context_object (Object): 
    cursor_shape (MouseCursor): 
    cursor_name (Name): 
    hot_spot (Vector2D): 

Returns:
    bool:

<a id="unreal.WidgetLibrary.set_focus_to_game_viewport"></a>

#### set_focus_to_game_viewport

```python
@classmethod
def set_focus_to_game_viewport(cls) -> None
```

X.set_focus_to_game_viewport() -> None
Set Focus to Game Viewport

<a id="unreal.WidgetLibrary.set_color_vision_deficiency_type"></a>

#### set_color_vision_deficiency_type

```python
@classmethod
def set_color_vision_deficiency_type(
        cls, type: ColorVisionDeficiency, severity: float,
        correct_deficiency: bool,
        show_correction_with_deficiency: bool) -> None
```

X.set_color_vision_deficiency_type(type, severity, correct_deficiency, show_correction_with_deficiency) -> None
Apply color deficiency correction settings to the game window

Args:
    type (ColorVisionDeficiency): The type of color deficiency correction to apply.
    severity (float): Intensity of the color deficiency correction effect, from 0 to 1.
    correct_deficiency (bool): Shifts the color spectrum to the visible range based on the current deficiency type.
    show_correction_with_deficiency (bool): If you're correcting the color deficiency, you can use this to visualize what the correction looks like with the deficiency.

<a id="unreal.WidgetLibrary.set_brush_resource_to_texture"></a>

#### set_brush_resource_to_texture

```python
@classmethod
def set_brush_resource_to_texture(cls, brush: SlateBrush,
                                  texture: Texture2D) -> SlateBrush
```

X.set_brush_resource_to_texture(brush, texture) -> SlateBrush
Sets the resource on a brush to be a UTexture2D.

Args:
    brush (SlateBrush): 
    texture (Texture2D): 

Returns:
    SlateBrush: 

    brush (SlateBrush):

<a id="unreal.WidgetLibrary.set_brush_resource_to_material"></a>

#### set_brush_resource_to_material

```python
@classmethod
def set_brush_resource_to_material(cls, brush: SlateBrush,
                                   material: MaterialInterface) -> SlateBrush
```

X.set_brush_resource_to_material(brush, material) -> SlateBrush
Sets the resource on a brush to be a Material.

Args:
    brush (SlateBrush): 
    material (MaterialInterface): 

Returns:
    SlateBrush: 

    brush (SlateBrush):

<a id="unreal.WidgetLibrary.restore_previous_window_title_bar_state"></a>

#### restore_previous_window_title_bar_state

```python
@classmethod
def restore_previous_window_title_bar_state(cls) -> None
```

X.restore_previous_window_title_bar_state() -> None
Restore Previous Window Title Bar State

<a id="unreal.WidgetLibrary.release_mouse_capture"></a>

#### release_mouse_capture

```python
@classmethod
def release_mouse_capture(cls,
                          reply: EventReply) -> Tuple[EventReply, EventReply]
```

X.release_mouse_capture(reply) -> (EventReply, reply=EventReply)
Release Mouse Capture

Args:
    reply (EventReply): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.release_joystick_capture"></a>

#### release_joystick_capture

```python
@classmethod
def release_joystick_capture(
        cls,
        reply: EventReply,
        all_joysticks: bool = False) -> Tuple[EventReply, EventReply]
```

X.release_joystick_capture(reply, all_joysticks=False) -> (EventReply, reply=EventReply)
Release Joystick Capture
deprecated: Use ClearUserFocus() instead

Args:
    reply (EventReply): 
    all_joysticks (bool): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.no_resource_brush"></a>

#### no_resource_brush

```python
@classmethod
def no_resource_brush(cls) -> SlateBrush
```

X.no_resource_brush() -> SlateBrush
Creates a Slate Brush that wont draw anything, the "Null Brush".

Returns:
    SlateBrush: A new slate brush that wont draw anything.

<a id="unreal.WidgetLibrary.make_brush_from_texture"></a>

#### make_brush_from_texture

```python
@classmethod
def make_brush_from_texture(cls,
                            texture: Texture2D,
                            width: int = 0,
                            height: int = 0) -> SlateBrush
```

X.make_brush_from_texture(texture, width=0, height=0) -> SlateBrush
Creates a Slate Brush from a Texture2D

Args:
    texture (Texture2D): 
    width (int32): When less than or equal to zero, the Width of the brush will default to the Width of the Texture
    height (int32): When less than or equal to zero, the Height of the brush will default to the Height of the Texture

Returns:
    SlateBrush: A new slate brush using the texture.

<a id="unreal.WidgetLibrary.make_brush_from_material"></a>

#### make_brush_from_material

```python
@classmethod
def make_brush_from_material(cls,
                             material: MaterialInterface,
                             width: int = 32,
                             height: int = 32) -> SlateBrush
```

X.make_brush_from_material(material, width=32, height=32) -> SlateBrush
Creates a Slate Brush from a Material.  Materials don't have an implicit size, so providing a widget and height
is required to hint slate with how large the image wants to be by default.

Args:
    material (MaterialInterface): 
    width (int32): 
    height (int32): 

Returns:
    SlateBrush: A new slate brush using the material.

<a id="unreal.WidgetLibrary.make_brush_from_asset"></a>

#### make_brush_from_asset

```python
@classmethod
def make_brush_from_asset(cls, brush_asset: SlateBrushAsset) -> SlateBrush
```

X.make_brush_from_asset(brush_asset) -> SlateBrush
Creates a Slate Brush from a Slate Brush Asset

Args:
    brush_asset (SlateBrushAsset): 

Returns:
    SlateBrush: A new slate brush using the asset's brush.

<a id="unreal.WidgetLibrary.lock_mouse"></a>

#### lock_mouse

```python
@classmethod
def lock_mouse(cls, reply: EventReply,
               capturing_widget: Widget) -> Tuple[EventReply, EventReply]
```

X.lock_mouse(reply, capturing_widget) -> (EventReply, reply=EventReply)
Lock Mouse

Args:
    reply (EventReply): 
    capturing_widget (Widget): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.is_drag_dropping"></a>

#### is_drag_dropping

```python
@classmethod
def is_drag_dropping(cls) -> bool
```

X.is_drag_dropping() -> bool
Returns true if a drag/drop event is occurring that a widget can handle.

Returns:
    bool:

<a id="unreal.WidgetLibrary.handled"></a>

#### handled

```python
@classmethod
def handled(cls) -> EventReply
```

X.handled() -> EventReply
The event reply to use when you choose to handle an event.  This will prevent the event
from continuing to bubble up / down the widget hierarchy.

Returns:
    EventReply:

<a id="unreal.WidgetLibrary.get_safe_zone_padding"></a>

#### get_safe_zone_padding

```python
@classmethod
def get_safe_zone_padding(
        cls,
        world_context_object: Object) -> Tuple[Vector4, Vector2D, Vector4]
```

X.get_safe_zone_padding(world_context_object) -> (safe_padding=Vector4, safe_padding_scale=Vector2D, spill_over_padding=Vector4)
Gets the amount of padding that needs to be added when accounting for the safe zone on TVs.

Args:
    world_context_object (Object): 

Returns:
    tuple: 

    safe_padding (Vector4): 

    safe_padding_scale (Vector2D): 

    spill_over_padding (Vector4):

<a id="unreal.WidgetLibrary.get_key_event_from_analog_input_event"></a>

#### get_key_event_from_analog_input_event

```python
@classmethod
def get_key_event_from_analog_input_event(cls,
                                          event: AnalogInputEvent) -> KeyEvent
```

X.get_key_event_from_analog_input_event(event) -> KeyEvent
Get Key Event from Analog Input Event

Args:
    event (AnalogInputEvent): 

Returns:
    KeyEvent:

<a id="unreal.WidgetLibrary.get_input_event_from_pointer_event"></a>

#### get_input_event_from_pointer_event

```python
@classmethod
def get_input_event_from_pointer_event(cls, event: PointerEvent) -> InputEvent
```

X.get_input_event_from_pointer_event(event) -> InputEvent
Get Input Event from Pointer Event

Args:
    event (PointerEvent): 

Returns:
    InputEvent:

<a id="unreal.WidgetLibrary.get_input_event_from_navigation_event"></a>

#### get_input_event_from_navigation_event

```python
@classmethod
def get_input_event_from_navigation_event(
        cls, event: NavigationEvent) -> InputEvent
```

X.get_input_event_from_navigation_event(event) -> InputEvent
Get Input Event from Navigation Event

Args:
    event (NavigationEvent): 

Returns:
    InputEvent:

<a id="unreal.WidgetLibrary.get_input_event_from_key_event"></a>

#### get_input_event_from_key_event

```python
@classmethod
def get_input_event_from_key_event(cls, event: KeyEvent) -> InputEvent
```

X.get_input_event_from_key_event(event) -> InputEvent
Get Input Event from Key Event

Args:
    event (KeyEvent): 

Returns:
    InputEvent:

<a id="unreal.WidgetLibrary.get_input_event_from_character_event"></a>

#### get_input_event_from_character_event

```python
@classmethod
def get_input_event_from_character_event(cls,
                                         event: CharacterEvent) -> InputEvent
```

X.get_input_event_from_character_event(event) -> InputEvent
Get Input Event from Character Event

Args:
    event (CharacterEvent): 

Returns:
    InputEvent:

<a id="unreal.WidgetLibrary.get_dynamic_material"></a>

#### get_dynamic_material

```python
@classmethod
def get_dynamic_material(
        cls, brush: SlateBrush) -> Tuple[MaterialInstanceDynamic, SlateBrush]
```

X.get_dynamic_material(brush) -> (MaterialInstanceDynamic, brush=SlateBrush)
Gets the material that allows changes to parameters at runtime.  The brush must already have a material assigned to it,
if it does it will automatically be converted to a MID.

Args:
    brush (SlateBrush): 

Returns:
    SlateBrush: A material that supports dynamic input from the game.

    brush (SlateBrush):

<a id="unreal.WidgetLibrary.get_drag_dropping_content"></a>

#### get_drag_dropping_content

```python
@classmethod
def get_drag_dropping_content(cls) -> DragDropOperation
```

X.get_drag_dropping_content() -> DragDropOperation
Returns the drag and drop operation that is currently occurring if any, otherwise nothing.

Returns:
    DragDropOperation:

<a id="unreal.WidgetLibrary.get_brush_resource_as_texture2d"></a>

#### get_brush_resource_as_texture2d

```python
@classmethod
def get_brush_resource_as_texture2d(cls, brush: SlateBrush) -> Texture2D
```

X.get_brush_resource_as_texture2d(brush) -> Texture2D
Gets the brush resource as a texture 2D.

Args:
    brush (SlateBrush): 

Returns:
    Texture2D:

<a id="unreal.WidgetLibrary.get_brush_resource_as_material"></a>

#### get_brush_resource_as_material

```python
@classmethod
def get_brush_resource_as_material(cls,
                                   brush: SlateBrush) -> MaterialInterface
```

X.get_brush_resource_as_material(brush) -> MaterialInterface
Gets the brush resource as a material.

Args:
    brush (SlateBrush): 

Returns:
    MaterialInterface:

<a id="unreal.WidgetLibrary.get_brush_resource"></a>

#### get_brush_resource

```python
@classmethod
def get_brush_resource(cls, brush: SlateBrush) -> Object
```

X.get_brush_resource(brush) -> Object
Gets the resource object on a brush.  This could be a UTexture2D or a UMaterialInterface.

Args:
    brush (SlateBrush): 

Returns:
    Object:

<a id="unreal.WidgetLibrary.get_all_widgets_with_interface"></a>

#### get_all_widgets_with_interface

```python
@classmethod
def get_all_widgets_with_interface(cls, world_context_object: Object,
                                   interface: Class,
                                   top_level_only: bool) -> Array[UserWidget]
```

X.get_all_widgets_with_interface(world_context_object, interface, top_level_only) -> Array[UserWidget]
Find all widgets in the world with the specified interface.
This is a slow operation, use with caution e.g. do not use every frame.

Args:
    world_context_object (Object): 
    interface (type(Class)): The interface to find. Must be specified or result array will be empty.
    top_level_only (bool): Only the widgets that are direct children of the viewport will be returned.

Returns:
    Array[UserWidget]: 

    found_widgets (Array[UserWidget]): Output array of widgets that implement the specified interface.

<a id="unreal.WidgetLibrary.get_all_widgets_of_class"></a>

#### get_all_widgets_of_class

```python
@classmethod
def get_all_widgets_of_class(cls,
                             world_context_object: Object,
                             widget_class: Class,
                             top_level_only: bool = True) -> Array[UserWidget]
```

X.get_all_widgets_of_class(world_context_object, widget_class, top_level_only=True) -> Array[UserWidget]
Find all widgets of a certain class.

Args:
    world_context_object (Object): 
    widget_class (type(Class)): The widget class to filter by.
    top_level_only (bool): Only the widgets that are direct children of the viewport will be returned.

Returns:
    Array[UserWidget]: 

    found_widgets (Array[UserWidget]): The widgets that were found matching the filter.

<a id="unreal.WidgetLibrary.end_drag_drop"></a>

#### end_drag_drop

```python
@classmethod
def end_drag_drop(cls, reply: EventReply) -> Tuple[EventReply, EventReply]
```

X.end_drag_drop(reply) -> (EventReply, reply=EventReply)
An event should return FReply::Handled().EndDragDrop() to request that the current drag/drop operation be terminated.

Args:
    reply (EventReply): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.draw_text_formatted"></a>

#### draw_text_formatted

```python
@classmethod
def draw_text_formatted(
    cls,
    context: PaintContext,
    text: Text,
    position: Vector2D,
    font: Font,
    font_size: float = 16.000000,
    font_type_face: Name = "Regular",
    tint: LinearColor = [1.000000, 1.000000, 1.000000,
                         1.000000]) -> PaintContext
```

X.draw_text_formatted(context, text, position, font, font_size=16.000000, font_type_face="Regular", tint=[1.000000, 1.000000, 1.000000, 1.000000]) -> PaintContext
Draws text.

Args:
    context (PaintContext): 
    text (Text): The string to draw.
    position (Vector2D): The starting position where the text is drawn in local space.
    font (Font): 
    font_size (float): 
    font_type_face (Name): 
    tint (LinearColor): Color to render the line.

Returns:
    PaintContext: 

    context (PaintContext):

<a id="unreal.WidgetLibrary.draw_text"></a>

#### draw_text

```python
@classmethod
def draw_text(
    cls,
    context: PaintContext,
    string: str,
    position: Vector2D,
    tint: LinearColor = [1.000000, 1.000000, 1.000000,
                         1.000000]) -> PaintContext
```

X.draw_text(context, string, position, tint=[1.000000, 1.000000, 1.000000, 1.000000]) -> PaintContext
Draws text.
deprecated: Use Draw Text instead

Args:
    context (PaintContext): 
    string (str): The string to draw.
    position (Vector2D): The starting position where the text is drawn in local space.
    tint (LinearColor): Color to render the line.

Returns:
    PaintContext: 

    context (PaintContext):

<a id="unreal.WidgetLibrary.draw_spline"></a>

#### draw_spline

```python
@classmethod
def draw_spline(cls,
                context: PaintContext,
                start: Vector2D,
                start_dir: Vector2D,
                end: Vector2D,
                end_dir: Vector2D,
                tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
                thickness: float = 1.000000) -> PaintContext
```

X.draw_spline(context, start, start_dir, end, end_dir, tint=[1.000000, 1.000000, 1.000000, 1.000000], thickness=1.000000) -> PaintContext
Draws a hermite spline.

Args:
    context (PaintContext): 
    start (Vector2D): Starting position of the spline in local space.
    start_dir (Vector2D): The direction of the spline from the start point.
    end (Vector2D): Ending position of the spline in local space.
    end_dir (Vector2D): The direction of the spline to the end point.
    tint (LinearColor): Color to render the spline.
    thickness (float): How many pixels thick this spline should be.

Returns:
    PaintContext: 

    context (PaintContext):

<a id="unreal.WidgetLibrary.draw_lines"></a>

#### draw_lines

```python
@classmethod
def draw_lines(cls,
               context: PaintContext,
               points: Array[Vector2D],
               tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
               anti_alias: bool = True,
               thickness: float = 1.000000) -> PaintContext
```

X.draw_lines(context, points, tint=[1.000000, 1.000000, 1.000000, 1.000000], anti_alias=True, thickness=1.000000) -> PaintContext
Draws several line segments.

Args:
    context (PaintContext): 
    points (Array[Vector2D]): Line pairs, each line needs to be 2 separate points in the array.
    tint (LinearColor): Color to render the line.
    anti_alias (bool): Whether the line should be antialiased.
    thickness (float): How many pixels thick this line should be.

Returns:
    PaintContext: 

    context (PaintContext):

<a id="unreal.WidgetLibrary.draw_line"></a>

#### draw_line

```python
@classmethod
def draw_line(cls,
              context: PaintContext,
              position_a: Vector2D,
              position_b: Vector2D,
              tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
              anti_alias: bool = True,
              thickness: float = 1.000000) -> PaintContext
```

X.draw_line(context, position_a, position_b, tint=[1.000000, 1.000000, 1.000000, 1.000000], anti_alias=True, thickness=1.000000) -> PaintContext
Draws a line.

Args:
    context (PaintContext): 
    position_a (Vector2D): Starting position of the line in local space.
    position_b (Vector2D): Ending position of the line in local space.
    tint (LinearColor): Color to render the line.
    anti_alias (bool): Whether the line should be antialiased.
    thickness (float): How many pixels thick this line should be.

Returns:
    PaintContext: 

    context (PaintContext):

<a id="unreal.WidgetLibrary.draw_box"></a>

#### draw_box

```python
@classmethod
def draw_box(
    cls,
    context: PaintContext,
    position: Vector2D,
    size: Vector2D,
    brush: SlateBrushAsset,
    tint: LinearColor = [1.000000, 1.000000, 1.000000,
                         1.000000]) -> PaintContext
```

X.draw_box(context, position, size, brush, tint=[1.000000, 1.000000, 1.000000, 1.000000]) -> PaintContext
Draws a box

Args:
    context (PaintContext): 
    position (Vector2D): 
    size (Vector2D): 
    brush (SlateBrushAsset): 
    tint (LinearColor): 

Returns:
    PaintContext: 

    context (PaintContext):

<a id="unreal.WidgetLibrary.dismiss_all_menus"></a>

#### dismiss_all_menus

```python
@classmethod
def dismiss_all_menus(cls) -> None
```

X.dismiss_all_menus() -> None
Closes any popup menu

<a id="unreal.WidgetLibrary.detect_drag_if_pressed"></a>

#### detect_drag_if_pressed

```python
@classmethod
def detect_drag_if_pressed(cls, pointer_event: PointerEvent,
                           widget_detecting_drag: Widget,
                           drag_key: Key) -> EventReply
```

X.detect_drag_if_pressed(pointer_event, widget_detecting_drag, drag_key) -> EventReply
Given the pointer event, emit the DetectDrag reply if the provided key was pressed.
If the DragKey is a touch key, that will also automatically work.

Args:
    pointer_event (PointerEvent): The pointer device event coming in.
    widget_detecting_drag (Widget): Detect dragging in this widget.
    drag_key (Key): This button should be pressed to detect the drag, won't emit the DetectDrag FEventReply unless this is pressed.

Returns:
    EventReply:

<a id="unreal.WidgetLibrary.detect_drag"></a>

#### detect_drag

```python
@classmethod
def detect_drag(cls, reply: EventReply, widget_detecting_drag: Widget,
                drag_key: Key) -> Tuple[EventReply, EventReply]
```

X.detect_drag(reply, widget_detecting_drag, drag_key) -> (EventReply, reply=EventReply)
Ask Slate to detect if a user starts dragging in this widget later.  Slate internally tracks the movement
and if it surpasses the drag threshold, Slate will send an OnDragDetected event to the widget.

Args:
    reply (EventReply): 
    widget_detecting_drag (Widget): Detect dragging in this widget
    drag_key (Key): This button should be pressed to detect the drag

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.clear_user_focus"></a>

#### clear_user_focus

```python
@classmethod
def clear_user_focus(cls,
                     reply: EventReply,
                     all_users: bool = False) -> Tuple[EventReply, EventReply]
```

X.clear_user_focus(reply, all_users=False) -> (EventReply, reply=EventReply)
Clear User Focus

Args:
    reply (EventReply): 
    all_users (bool): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.capture_mouse"></a>

#### capture_mouse

```python
@classmethod
def capture_mouse(cls, reply: EventReply,
                  capturing_widget: Widget) -> Tuple[EventReply, EventReply]
```

X.capture_mouse(reply, capturing_widget) -> (EventReply, reply=EventReply)
Capture Mouse

Args:
    reply (EventReply): 
    capturing_widget (Widget): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.capture_joystick"></a>

#### capture_joystick

```python
@classmethod
def capture_joystick(
        cls,
        reply: EventReply,
        capturing_widget: Widget,
        all_joysticks: bool = False) -> Tuple[EventReply, EventReply]
```

X.capture_joystick(reply, capturing_widget, all_joysticks=False) -> (EventReply, reply=EventReply)
Capture Joystick
deprecated: Use SetUserFocus() instead

Args:
    reply (EventReply): 
    capturing_widget (Widget): 
    all_joysticks (bool): 

Returns:
    EventReply: 

    reply (EventReply):

<a id="unreal.WidgetLibrary.cancel_drag_drop"></a>

#### cancel_drag_drop

```python
@classmethod
def cancel_drag_drop(cls) -> None
```

X.cancel_drag_drop() -> None
Cancels any current drag drop operation.

<a id="unreal.WidgetLayoutLibrary"></a>