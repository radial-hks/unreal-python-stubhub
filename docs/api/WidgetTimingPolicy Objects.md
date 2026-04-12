## WidgetTimingPolicy Objects

```python
class WidgetTimingPolicy(EnumBase)
```

EWidget Timing Policy

**C++ Source:**

- **Module**: UMG
- **File**: WidgetComponent.h

<a id="unreal.WidgetTimingPolicy.REAL_TIME"></a>

#### REAL\_TIME

0: The widget will tick using real time. When not ticking, real time will accumulate and be simulated on the next tick.

<a id="unreal.WidgetTimingPolicy.GAME_TIME"></a>

#### GAME\_TIME

1: The widget will tick using game time, respecting pausing and time dilation.

<a id="unreal.WidgetBlendMode"></a>