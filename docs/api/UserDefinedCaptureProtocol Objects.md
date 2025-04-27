## UserDefinedCaptureProtocol Objects

```python
class UserDefinedCaptureProtocol(MovieSceneImageCaptureProtocolBase)
```

A blueprintable capture protocol that defines how to capture frames from the engine

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: UserDefinedCaptureProtocol.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``world`` (World):  [Read-Write] World pointer assigned on Setup

<a id="unreal.UserDefinedCaptureProtocol.world"></a>

#### world

```python
@property
def world() -> World
```

(World):  [Read-Only] World pointer assigned on Setup

<a id="unreal.UserDefinedCaptureProtocol.stop_capturing_final_pixels"></a>

#### stop_capturing_final_pixels

```python
def stop_capturing_final_pixels() -> None
```

x.stop_capturing_final_pixels() -> None
Instruct this protocol to stop capturing LDR final pixels

<a id="unreal.UserDefinedCaptureProtocol.start_capturing_final_pixels"></a>

#### start_capturing_final_pixels

```python
def start_capturing_final_pixels(stream_id: CapturedPixelsID) -> None
```

x.start_capturing_final_pixels(stream_id) -> None
Instruct this protocol to start capturing LDR final pixels (including slate widgets and burn-ins)

Args:
    stream_id (CapturedPixelsID): The identifier to use for the final pixels buffer

<a id="unreal.UserDefinedCaptureProtocol.resolve_buffer"></a>

#### resolve_buffer

```python
def resolve_buffer(buffer: Texture, buffer_id: CapturedPixelsID) -> None
```

x.resolve_buffer(buffer, buffer_id) -> None
* Resolve the specified buffer and pass it directly to the specified handler when done (does not pass to any bound streams)
*
*

Args:
    buffer (Texture): The desired buffer to save *
    buffer_id (CapturedPixelsID): The ID of this buffer that is passed to the pixel handler (e.g. a composition pass name).

<a id="unreal.UserDefinedCaptureProtocol.on_warm_up"></a>

#### on_warm_up

```python
def on_warm_up() -> None
```

x.on_warm_up() -> None
Called when the capture process is warming up. Protocols may transition from either an initialized, or capturing state to warm-up

<a id="unreal.UserDefinedCaptureProtocol.on_tick"></a>

#### on_tick

```python
def on_tick() -> None
```

x.on_tick() -> None
Called after the capture process itself is ticked, after the frame is set up for capture, but before most actors have ticked

<a id="unreal.UserDefinedCaptureProtocol.on_start_capture"></a>

#### on_start_capture

```python
def on_start_capture() -> None
```

x.on_start_capture() -> None
Called when this protocol should start capturing frames

<a id="unreal.UserDefinedCaptureProtocol.on_setup"></a>

#### on_setup

```python
def on_setup() -> bool
```

x.on_setup() -> bool
Called once at the start of the capture process, but before any warmup frames

Returns:
    bool: true if this protocol set up successfully, false otherwise

<a id="unreal.UserDefinedCaptureProtocol.on_pre_tick"></a>

#### on_pre_tick

```python
def on_pre_tick() -> None
```

x.on_pre_tick() -> None
Called before the capture process itself is ticked, before each frame is set up for capture
Useful for any pre-frame set up or resetting the previous frame's state

<a id="unreal.UserDefinedCaptureProtocol.on_pixels_received"></a>

#### on_pixels_received

```python
def on_pixels_received(pixels: CapturedPixels, id: CapturedPixelsID,
                       frame_metrics: FrameMetrics) -> None
```

x.on_pixels_received(pixels, id, frame_metrics) -> None
Called when pixels have been received for the specified stream name

Args:
    pixels (CapturedPixels): 
    id (CapturedPixelsID): 
    frame_metrics (FrameMetrics):

<a id="unreal.UserDefinedCaptureProtocol.on_pause_capture"></a>

#### on_pause_capture

```python
def on_pause_capture() -> None
```

x.on_pause_capture() -> None
Called when this protocol should temporarily stop capturing frames

<a id="unreal.UserDefinedCaptureProtocol.on_finalize"></a>

#### on_finalize

```python
def on_finalize() -> None
```

x.on_finalize() -> None
Called to complete finalization of this protocol

<a id="unreal.UserDefinedCaptureProtocol.on_capture_frame"></a>

#### on_capture_frame

```python
def on_capture_frame() -> None
```

x.on_capture_frame() -> None
Called when this protocol should capture the current frame

<a id="unreal.UserDefinedCaptureProtocol.on_can_finalize"></a>

#### on_can_finalize

```python
def on_can_finalize() -> bool
```

x.on_can_finalize() -> bool
Called to check whether this protocol has finished any pending tasks, and can now be shut down

Returns:
    bool:

<a id="unreal.UserDefinedCaptureProtocol.on_begin_finalize"></a>

#### on_begin_finalize

```python
def on_begin_finalize() -> None
```

x.on_begin_finalize() -> None
Called when this protocol is going to be shut down - should not capture any more frames

<a id="unreal.UserDefinedCaptureProtocol.get_current_frame_metrics"></a>

#### get_current_frame_metrics

```python
def get_current_frame_metrics() -> FrameMetrics
```

x.get_current_frame_metrics() -> FrameMetrics
Access this protocol's current frame metrics

Returns:
    FrameMetrics:

<a id="unreal.UserDefinedCaptureProtocol.generate_filename"></a>

#### generate_filename

```python
def generate_filename(frame_metrics: FrameMetrics) -> str
```

x.generate_filename(frame_metrics) -> str
Generate a filename for the current frame

Args:
    frame_metrics (FrameMetrics): 

Returns:
    str:

<a id="unreal.UserDefinedImageCaptureProtocol"></a>