## ViewportStatsSubsystem Objects

```python
class ViewportStatsSubsystem(WorldSubsystem)
```

The Viewport Stats Subsystem offers the ability to add messages to the current
viewport such as "LIGHTING NEEDS TO BE REBUILT" and "BLUEPRINT COMPILE ERROR".

Example usage:

     if (UViewportStatsSubsystem* ViewportSubsystem = GetWorld()->GetSubsystem<UViewportStatsSubsystem>())
     {
             // Bind a member function delegate to the subsystem...
             FViewportDisplayCallback Callback;
             Callback.BindDynamic(this, &UCustomClass::DisplayViewportMessage);
             ViewportSubsystem->AddDisplayDelegate(Callback);

             // ... or use inline lambda functions
             ViewportSubsystem->AddDisplayDelegate([](FText& OutText, FLinearColor& OutColor)
             {
                     // Some kind of state management
                     OutText = NSLOCTEXT("FooNamespace", "Blarg", "Display message here");
                     OutColor = FLinearColor::Red;
                     return bShouldDisplay;
             });
     }

**C++ Source:**

- **Module**: Engine
- **File**: ViewportStatsSubsystem.h

<a id="unreal.ViewportStatsSubsystem.remove_display_delegate"></a>

#### remove_display_delegate

```python
def remove_display_delegate(index_to_remove: int) -> None
```

x.remove_display_delegate(index_to_remove) -> None
Remove a callback function from the display subsystem

Args:
    index_to_remove (int32): The index in the DisplayDelegates array to remove. This is the value returned from AddDisplayDelegate.

<a id="unreal.ViewportStatsSubsystem.add_timed_display"></a>

#### add_timed_display

```python
def add_timed_display(text: Text,
                      color: LinearColor = [
                          1.000000, 1.000000, 1.000000, 1.000000
                      ],
                      duration: float = 0.000000,
                      display_offset: Vector2D = [0.000000, 0.000000]) -> None
```

x.add_timed_display(text, color=[1.000000, 1.000000, 1.000000, 1.000000], duration=0.000000, display_offset=[0.000000, 0.000000]) -> None
Add a message to be displayed on the viewport of this world

Args:
    text (Text): The text to be displayed
    color (LinearColor): Color of the text to be displayed
    duration (float): How long the text will be on screen, if 0 then it will stay indefinitely
    display_offset (Vector2D): A position offset that the message should use when displayed.

<a id="unreal.ViewportStatsSubsystem.add_display_delegate"></a>

#### add_display_delegate

```python
def add_display_delegate(delegate: ViewportDisplayCallback) -> int
```

x.add_display_delegate(delegate) -> int32
Add a dynamic delegate to the display subsystem.

Args:
    delegate (ViewportDisplayCallback): 

Returns:
    int32:

<a id="unreal.FloatingPawnMovement"></a>