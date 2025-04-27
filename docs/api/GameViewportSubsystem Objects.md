## GameViewportSubsystem Objects

```python
class GameViewportSubsystem(EngineSubsystem)
```

Game Viewport Subsystem

**C++ Source:**

- **Module**: UMG
- **File**: GameViewportSubsystem.h

<a id="unreal.GameViewportSubsystem.set_widget_slot_position"></a>

#### set_widget_slot_position

```python
@classmethod
def set_widget_slot_position(cls, slot: GameViewportWidgetSlot, widget: Widget,
                             position: Vector2D,
                             remove_dpi_scale: bool) -> GameViewportWidgetSlot
```

X.set_widget_slot_position(slot, widget, position, remove_dpi_scale) -> GameViewportWidgetSlot
Helper function to set the position in the viewport for the Slot.

Args:
    slot (GameViewportWidgetSlot): 
    widget (Widget): 
    position (Vector2D): The 2D position to set the widget to in the viewport.
    remove_dpi_scale (bool): If you've already calculated inverse DPI, set this to false. Otherwise inverse DPI is applied to the position so that when the location is scaled by DPI, it ends up in the expected position.

Returns:
    GameViewportWidgetSlot:

<a id="unreal.GameViewportSubsystem.set_widget_slot_desired_size"></a>

#### set_widget_slot_desired_size

```python
@classmethod
def set_widget_slot_desired_size(cls, slot: GameViewportWidgetSlot,
                                 size: Vector2D) -> GameViewportWidgetSlot
```

X.set_widget_slot_desired_size(slot, size) -> GameViewportWidgetSlot
Helper function to set the desired size in the viewport for the Slot.

Args:
    slot (GameViewportWidgetSlot): 
    size (Vector2D): 

Returns:
    GameViewportWidgetSlot:

<a id="unreal.GameViewportSubsystem.set_widget_slot"></a>

#### set_widget_slot

```python
def set_widget_slot(widget: Widget, slot: GameViewportWidgetSlot) -> None
```

x.set_widget_slot(widget, slot) -> None
Update the slot info of a previously added widget or Store the slot info for later use.

Args:
    widget (Widget): 
    slot (GameViewportWidgetSlot):

<a id="unreal.GameViewportSubsystem.remove_widget"></a>

#### remove_widget

```python
def remove_widget(widget: Widget) -> None
```

x.remove_widget(widget) -> None
Removes the widget from the viewport.

Args:
    widget (Widget):

<a id="unreal.GameViewportSubsystem.is_widget_added"></a>

#### is_widget_added

```python
def is_widget_added(widget: Widget) -> bool
```

x.is_widget_added(widget) -> bool


Args:
    widget (Widget): 

Returns:
    bool: true if the widget was added to the viewport using AddWidget or AddWidgetForPlayer.

<a id="unreal.GameViewportSubsystem.get_widget_slot"></a>

#### get_widget_slot

```python
def get_widget_slot(widget: Widget) -> GameViewportWidgetSlot
```

x.get_widget_slot(widget) -> GameViewportWidgetSlot
The slot info from previously added widget or info that is store for later.

Args:
    widget (Widget): 

Returns:
    GameViewportWidgetSlot:

<a id="unreal.GameViewportSubsystem.add_widget_for_player"></a>

#### add_widget_for_player

```python
def add_widget_for_player(widget: Widget, player: LocalPlayer,
                          slot: GameViewportWidgetSlot) -> bool
```

x.add_widget_for_player(widget, player, slot) -> bool
Adds the widget to the game's viewport in the section dedicated to the player. This is valuable in a split screen
game where you need to only show a widget over a player's portion of the viewport.

Args:
    widget (Widget): 
    player (LocalPlayer): 
    slot (GameViewportWidgetSlot): 

Returns:
    bool:

<a id="unreal.GameViewportSubsystem.add_widget"></a>

#### add_widget

```python
def add_widget(widget: Widget, slot: GameViewportWidgetSlot) -> bool
```

x.add_widget(widget, slot) -> bool
Adds it to the game's viewport.

Args:
    widget (Widget): 
    slot (GameViewportWidgetSlot): 

Returns:
    bool:

<a id="unreal.UserListEntry"></a>