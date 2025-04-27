## WidgetTickFrequency Objects

```python
class WidgetTickFrequency(EnumBase)
```

Determines what strategy we use to determine when and if the widget ticks.

**C++ Source:**

- **Module**: UMG
- **File**: UserWidget.h

<a id="unreal.WidgetTickFrequency.NEVER"></a>

#### NEVER

0: This widget never ticks

<a id="unreal.WidgetTickFrequency.AUTO"></a>

#### AUTO

1: This widget will tick if a blueprint tick function is implemented, any latent actions are found or animations need to play
If the widget inherits from something other than UserWidget it will also tick so that native C++ or inherited ticks function
To disable native ticking use add the class metadata flag "DisableNativeTick".  I.E: meta=(DisableNativeTick)

<a id="unreal.DetailMode"></a>