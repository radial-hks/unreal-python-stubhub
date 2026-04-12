## MouseCaptureMode Objects

```python
class MouseCaptureMode(EnumBase)
```

EMouse Capture Mode

**C++ Source:**

- **Module**: Engine
- **File**: EngineBaseTypes.h

<a id="unreal.MouseCaptureMode.NO_CAPTURE"></a>

#### NO\_CAPTURE

0: Do not capture the mouse at all

<a id="unreal.MouseCaptureMode.CAPTURE_PERMANENTLY"></a>

#### CAPTURE\_PERMANENTLY

1: Capture the mouse permanently when the viewport is clicked, and consume the initial mouse down that caused the capture so it isn't processed by player input

<a id="unreal.MouseCaptureMode.CAPTURE_PERMANENTLY_INCLUDING_INITIAL_MOUSE_DOWN"></a>

#### CAPTURE\_PERMANENTLY\_INCLUDING\_INITIAL\_MOUSE\_DOWN

2: Capture the mouse permanently when the viewport is clicked, and allow player input to process the mouse down that caused the capture

<a id="unreal.MouseCaptureMode.CAPTURE_DURING_MOUSE_DOWN"></a>

#### CAPTURE\_DURING\_MOUSE\_DOWN

3: Capture the mouse during a mouse down, releases on mouse up

<a id="unreal.MouseCaptureMode.CAPTURE_DURING_RIGHT_MOUSE_DOWN"></a>

#### CAPTURE\_DURING\_RIGHT\_MOUSE\_DOWN

4: Capture only when the right mouse button is down, not any of the other mouse buttons

<a id="unreal.SuggestProjVelocityTraceOption"></a>