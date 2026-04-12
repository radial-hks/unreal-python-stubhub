## CoveringWidgetTimingPolicy Objects

```python
class CoveringWidgetTimingPolicy(EnumBase)
```

ECovering Widget Timing Policy

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: Covering3DWidgetComponent.h

<a id="unreal.CoveringWidgetTimingPolicy.REAL_TIME"></a>

#### REAL\_TIME

0: The widget will tick using real time. When not ticking, real time will accumulate and be simulated on the next tick.

<a id="unreal.CoveringWidgetTimingPolicy.GAME_TIME"></a>

#### GAME\_TIME

1: The widget will tick using game time, respecting pausing and time dilation.

<a id="unreal.CoveringWidgetBlendMode"></a>