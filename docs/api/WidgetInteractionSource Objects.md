## WidgetInteractionSource Objects

```python
class WidgetInteractionSource(EnumBase)
```

The interaction source for the widget interaction component, e.g. where do we try and
trace from to try to find a widget under a virtual pointer device.

**C++ Source:**

- **Module**: UMG
- **File**: WidgetInteractionComponent.h

<a id="unreal.WidgetInteractionSource.WORLD"></a>

#### WORLD

0: Sends traces from the world location and orientation of the interaction component.

<a id="unreal.WidgetInteractionSource.MOUSE"></a>

#### MOUSE

1: Sends traces from the mouse location of the first local player controller.

<a id="unreal.WidgetInteractionSource.CENTER_SCREEN"></a>

#### CENTER_SCREEN

2: Sends trace from the center of the first local player's screen.

<a id="unreal.WidgetInteractionSource.CUSTOM"></a>

#### CUSTOM

3: Sends traces from a custom location determined by the user.  Will use whatever
FHitResult is set by the call to SetCustomHitResult.

<a id="unreal.DragPivot"></a>