## MediaCaptureState Objects

```python
class MediaCaptureState(EnumBase)
```

Possible states of media capture.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaCapture.h

<a id="unreal.MediaCaptureState.ERROR"></a>

#### ERROR

0: Unrecoverable error occurred during capture.

<a id="unreal.MediaCaptureState.CAPTURING"></a>

#### CAPTURING

1: Media is currently capturing.

<a id="unreal.MediaCaptureState.PREPARING"></a>

#### PREPARING

2: Media is being prepared for capturing.

<a id="unreal.MediaCaptureState.STOP_REQUESTED"></a>

#### STOP_REQUESTED

3: Capture has been stopped but some frames may need to be process.

<a id="unreal.MediaCaptureState.STOPPED"></a>

#### STOPPED

4: Capture has been stopped.

<a id="unreal.MediaCaptureCroppingType"></a>