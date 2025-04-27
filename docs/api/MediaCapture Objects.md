## MediaCapture Objects

```python
class MediaCapture(Object)
```

Abstract base class for media capture.

MediaCapture capture the texture of the Render target or the SceneViewport and sends it to an external media device.
MediaCapture should be created by a MediaOutput.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaCapture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_state_changed`` (MediaCaptureStateChangedSignature):  [Read-Write] Called when the state of the capture changed.

<a id="unreal.MediaCapture.on_state_changed"></a>

#### on_state_changed

```python
@property
def on_state_changed() -> MediaCaptureStateChangedSignature
```

(MediaCaptureStateChangedSignature):  [Read-Write] Called when the state of the capture changed.

<a id="unreal.MediaCapture.on_state_changed"></a>

#### on_state_changed

```python
@on_state_changed.setter
def on_state_changed(value: MediaCaptureStateChangedSignature) -> None
```

<a id="unreal.MediaCapture.update_texture_render_target2d"></a>

#### update_texture_render_target2d

```python
def update_texture_render_target2d(
        render_target: TextureRenderTarget2D) -> bool
```

x.update_texture_render_target2d(render_target) -> bool
Update the current capture with every frame for a TextureRenderTarget2D.
The TextureRenderTarget2D needs to be of the same size and have the same pixel format as requested by the media output.

Args:
    render_target (TextureRenderTarget2D): 

Returns:
    bool: Return true if the capture was successfully updated. If false is returned, the capture was stopped.

<a id="unreal.MediaCapture.stop_capture"></a>

#### stop_capture

```python
def stop_capture(allow_pending_frame_to_be_process: bool) -> None
```

x.stop_capture(allow_pending_frame_to_be_process) -> None
Stop the previous requested capture.

Args:
    allow_pending_frame_to_be_process (bool): Keep copying the pending frames asynchronously or stop immediately without copying the pending frames.

<a id="unreal.MediaCapture.set_media_output"></a>

#### set_media_output

```python
def set_media_output(media_output: MediaOutput) -> None
```

x.set_media_output(media_output) -> None
Set the media output. Can only be set when the capture is stopped.

Args:
    media_output (MediaOutput):

<a id="unreal.MediaCapture.get_state"></a>

#### get_state

```python
def get_state() -> MediaCaptureState
```

x.get_state() -> MediaCaptureState
Get the current state of the capture.

Returns:
    MediaCaptureState:

<a id="unreal.MediaCapture.get_desired_size"></a>

#### get_desired_size

```python
def get_desired_size() -> IntPoint
```

x.get_desired_size() -> IntPoint
Get the desired size of the current capture.

Returns:
    IntPoint:

<a id="unreal.MediaCapture.get_desired_pixel_format"></a>

#### get_desired_pixel_format

```python
def get_desired_pixel_format() -> PixelFormat
```

x.get_desired_pixel_format() -> PixelFormat
Get the desired pixel format of the current capture.

Returns:
    PixelFormat:

<a id="unreal.MediaCapture.capture_texture_render_target2d"></a>

#### capture_texture_render_target2d

```python
def capture_texture_render_target2d(
        render_target: TextureRenderTarget2D,
        capture_options: MediaCaptureOptions) -> bool
```

x.capture_texture_render_target2d(render_target, capture_options) -> bool
Stop the actual capture if there is one.
Then capture every frame for a TextureRenderTarget2D.
The TextureRenderTarget2D needs to be of the same size and have the same pixel format as requested by the media output.

Args:
    render_target (TextureRenderTarget2D): 
    capture_options (MediaCaptureOptions): 

Returns:
    bool: True if the capture was successfully started

<a id="unreal.MediaCapture.capture_active_scene_viewport"></a>

#### capture_active_scene_viewport

```python
def capture_active_scene_viewport(
        capture_options: MediaCaptureOptions) -> bool
```

x.capture_active_scene_viewport(capture_options) -> bool
Stop the current capture if there is one.
Then find and capture every frame from active SceneViewport.
It can only find a SceneViewport when you play in Standalone or in "New Editor Window PIE".
If the active SceneViewport is destroyed, the capture will stop.
The SceneViewport needs to be of the same size and have the same pixel format as requested by the media output.

Args:
    capture_options (MediaCaptureOptions): 

Returns:
    bool: True if the capture was successfully started

<a id="unreal.FileMediaCapture"></a>