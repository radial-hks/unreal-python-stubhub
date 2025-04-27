## MediaCaptureOverrunAction Objects

```python
class MediaCaptureOverrunAction(EnumBase)
```

Action when overrun occurs

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaCapture.h

<a id="unreal.MediaCaptureOverrunAction.FLUSH"></a>

#### FLUSH

0: Flush rendering thread such that all scheduled commands are executed.

<a id="unreal.MediaCaptureOverrunAction.SKIP"></a>

#### SKIP

1: Skip capturing a frame if readback is trailing too much.

<a id="unreal.MediaCapturePhase"></a>