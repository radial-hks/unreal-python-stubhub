## WidgetPixelSnapping Objects

```python
class WidgetPixelSnapping(EnumBase)
```

The different states of pixel snapping a widget can be in.

**C++ Source:**

- **Module**: SlateCore
- **File**: WidgetPixelSnapping.h

<a id="unreal.WidgetPixelSnapping.INHERIT"></a>

#### INHERIT

0: Inherits the snapping method set by the parent widget.

<a id="unreal.WidgetPixelSnapping.DISABLED"></a>

#### DISABLED

1: Draws the widget without snapping. Useful during animations or moving indicators.

<a id="unreal.WidgetPixelSnapping.SNAP_TO_PIXEL"></a>

#### SNAP_TO_PIXEL

2: Draws the widget at the nearest pixel. Improves sharpness of widgets.

<a id="unreal.WidgetTickFrequency"></a>