## MediaCaptureOptions Objects

```python
class MediaCaptureOptions(StructBase)
```

Base class of additional data that can be stored for each requested capture.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaCapture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_linear_to_srgb_conversion`` (bool):  [Read-Write] Whether to apply a linear to sRGB conversion to the texture before outputting.
- ``auto_restart_on_source_size_change`` (bool):  [Read-Write] If source texture's size change, auto restart capture to follow source resolution if implementation supports it.
- ``autostop_on_capture`` (bool):  [Read-Write] Automatically stop capturing after a predetermined number of images.
- ``capture_phase`` (MediaCapturePhase):  [Read-Write]
- ``color_conversion_settings`` (OpenColorIOColorConversionSettings):  [Read-Write] Color conversion settings used by the OCIO conversion pass.
- ``convert_to_desired_pixel_format`` (bool):  [Read-Write] Allows to enable/disable pixel format conversion for the cases where render target is not of the desired pixel format.
- ``crop`` (MediaCaptureCroppingType):  [Read-Write] Crop the captured SceneViewport or TextureRenderTarget2D to the desired size.
- ``custom_capture_point`` (IntPoint):  [Read-Write] Crop the captured SceneViewport or TextureRenderTarget2D to the desired size.
  note: Only valid when Crop is set to Custom.
- ``force_alpha_to_one_on_conversion`` (bool):  [Read-Write] In some cases when we want to stream irregular render targets containing limited number
  of channels (for example RG16f), we would like to force Alpha to 1.
- ``number_of_frames_to_capture`` (int32):  [Read-Write] The number of images to capture
- ``overrun_action`` (MediaCaptureOverrunAction):  [Read-Write] Action to do when game thread overruns render thread and all frames are in flights being captured / readback.
- ``resize_method`` (MediaCaptureResizeMethod):  [Read-Write] When the capture start, control if and how the source buffer should be resized to the desired size.
  note: Only valid when a size is specified by the MediaOutput.
- ``resize_source_buffer`` (bool):  [Read-Write]
  deprecated: bResizeSourceBuffer, please use ResizeMethod instead.
- ``skip_frame_when_running_expensive_tasks`` (bool):  [Read-Write] When the application enters responsive mode, skip the frame capture.
  The application can enter responsive mode on mouse down, viewport resize, ...
  That is to ensure responsiveness in low FPS situations.

<a id="unreal.MediaCaptureOptions.__init__"></a>

#### __init__

```python
def __init__(
    auto_restart_on_source_size_change: bool = False,
    overrun_action: MediaCaptureOverrunAction = MediaCaptureOverrunAction.
    FLUSH,
    crop: MediaCaptureCroppingType = MediaCaptureCroppingType.NONE,
    color_conversion_settings: OpenColorIOColorConversionSettings = [
        None, ["", -1, ""], ["", -1, ""], ["", ""],
        OpenColorIOViewTransformDirection.FORWARD
    ],
    custom_capture_point: IntPoint = [0, 0],
    resize_method: MediaCaptureResizeMethod = MediaCaptureResizeMethod.NONE,
    skip_frame_when_running_expensive_tasks: bool = False,
    convert_to_desired_pixel_format: bool = False,
    force_alpha_to_one_on_conversion: bool = False,
    apply_linear_to_srgb_conversion: bool = False,
    autostop_on_capture: bool = False,
    number_of_frames_to_capture: int = 0,
    capture_phase: MediaCapturePhase = MediaCapturePhase.BEFORE_POST_PROCESSING
) -> None
```

<a id="unreal.MediaCaptureOptions.auto_restart_on_source_size_change"></a>

#### auto_restart_on_source_size_change

```python
@property
def auto_restart_on_source_size_change() -> bool
```

(bool):  [Read-Write] If source texture's size change, auto restart capture to follow source resolution if implementation supports it.

<a id="unreal.MediaCaptureOptions.auto_restart_on_source_size_change"></a>

#### auto_restart_on_source_size_change

```python
@auto_restart_on_source_size_change.setter
def auto_restart_on_source_size_change(value: bool) -> None
```

<a id="unreal.MediaCaptureOptions.overrun_action"></a>

#### overrun_action

```python
@property
def overrun_action() -> MediaCaptureOverrunAction
```

(MediaCaptureOverrunAction):  [Read-Write] Action to do when game thread overruns render thread and all frames are in flights being captured / readback.

<a id="unreal.MediaCaptureOptions.overrun_action"></a>

#### overrun_action

```python
@overrun_action.setter
def overrun_action(value: MediaCaptureOverrunAction) -> None
```

<a id="unreal.MediaCaptureOptions.crop"></a>

#### crop

```python
@property
def crop() -> MediaCaptureCroppingType
```

(MediaCaptureCroppingType):  [Read-Write] Crop the captured SceneViewport or TextureRenderTarget2D to the desired size.

<a id="unreal.MediaCaptureOptions.crop"></a>

#### crop

```python
@crop.setter
def crop(value: MediaCaptureCroppingType) -> None
```

<a id="unreal.MediaCaptureOptions.color_conversion_settings"></a>

#### color_conversion_settings

```python
@property
def color_conversion_settings() -> OpenColorIOColorConversionSettings
```

(OpenColorIOColorConversionSettings):  [Read-Write] Color conversion settings used by the OCIO conversion pass.

<a id="unreal.MediaCaptureOptions.color_conversion_settings"></a>

#### color_conversion_settings

```python
@color_conversion_settings.setter
def color_conversion_settings(
        value: OpenColorIOColorConversionSettings) -> None
```

<a id="unreal.MediaCaptureOptions.custom_capture_point"></a>

#### custom_capture_point

```python
@property
def custom_capture_point() -> IntPoint
```

(IntPoint):  [Read-Write] Crop the captured SceneViewport or TextureRenderTarget2D to the desired size.
note: Only valid when Crop is set to Custom.

<a id="unreal.MediaCaptureOptions.custom_capture_point"></a>

#### custom_capture_point

```python
@custom_capture_point.setter
def custom_capture_point(value: IntPoint) -> None
```

<a id="unreal.MediaCaptureOptions.resize_method"></a>

#### resize_method

```python
@property
def resize_method() -> MediaCaptureResizeMethod
```

(MediaCaptureResizeMethod):  [Read-Write] When the capture start, control if and how the source buffer should be resized to the desired size.
note: Only valid when a size is specified by the MediaOutput.

<a id="unreal.MediaCaptureOptions.resize_method"></a>

#### resize_method

```python
@resize_method.setter
def resize_method(value: MediaCaptureResizeMethod) -> None
```

<a id="unreal.MediaCaptureOptions.skip_frame_when_running_expensive_tasks"></a>

#### skip_frame_when_running_expensive_tasks

```python
@property
def skip_frame_when_running_expensive_tasks() -> bool
```

(bool):  [Read-Write] When the application enters responsive mode, skip the frame capture.
The application can enter responsive mode on mouse down, viewport resize, ...
That is to ensure responsiveness in low FPS situations.

<a id="unreal.MediaCaptureOptions.skip_frame_when_running_expensive_tasks"></a>

#### skip_frame_when_running_expensive_tasks

```python
@skip_frame_when_running_expensive_tasks.setter
def skip_frame_when_running_expensive_tasks(value: bool) -> None
```

<a id="unreal.MediaCaptureOptions.convert_to_desired_pixel_format"></a>

#### convert_to_desired_pixel_format

```python
@property
def convert_to_desired_pixel_format() -> bool
```

(bool):  [Read-Write] Allows to enable/disable pixel format conversion for the cases where render target is not of the desired pixel format.

<a id="unreal.MediaCaptureOptions.convert_to_desired_pixel_format"></a>

#### convert_to_desired_pixel_format

```python
@convert_to_desired_pixel_format.setter
def convert_to_desired_pixel_format(value: bool) -> None
```

<a id="unreal.MediaCaptureOptions.force_alpha_to_one_on_conversion"></a>

#### force_alpha_to_one_on_conversion

```python
@property
def force_alpha_to_one_on_conversion() -> bool
```

(bool):  [Read-Write] In some cases when we want to stream irregular render targets containing limited number
of channels (for example RG16f), we would like to force Alpha to 1.

<a id="unreal.MediaCaptureOptions.force_alpha_to_one_on_conversion"></a>

#### force_alpha_to_one_on_conversion

```python
@force_alpha_to_one_on_conversion.setter
def force_alpha_to_one_on_conversion(value: bool) -> None
```

<a id="unreal.MediaCaptureOptions.apply_linear_to_srgb_conversion"></a>

#### apply_linear_to_srgb_conversion

```python
@property
def apply_linear_to_srgb_conversion() -> bool
```

(bool):  [Read-Write] Whether to apply a linear to sRGB conversion to the texture before outputting.

<a id="unreal.MediaCaptureOptions.apply_linear_to_srgb_conversion"></a>

#### apply_linear_to_srgb_conversion

```python
@apply_linear_to_srgb_conversion.setter
def apply_linear_to_srgb_conversion(value: bool) -> None
```

<a id="unreal.MediaCaptureOptions.autostop_on_capture"></a>

#### autostop_on_capture

```python
@property
def autostop_on_capture() -> bool
```

(bool):  [Read-Write] Automatically stop capturing after a predetermined number of images.

<a id="unreal.MediaCaptureOptions.autostop_on_capture"></a>

#### autostop_on_capture

```python
@autostop_on_capture.setter
def autostop_on_capture(value: bool) -> None
```

<a id="unreal.MediaCaptureOptions.number_of_frames_to_capture"></a>

#### number_of_frames_to_capture

```python
@property
def number_of_frames_to_capture() -> int
```

(int32):  [Read-Write] The number of images to capture

<a id="unreal.MediaCaptureOptions.number_of_frames_to_capture"></a>

#### number_of_frames_to_capture

```python
@number_of_frames_to_capture.setter
def number_of_frames_to_capture(value: int) -> None
```

<a id="unreal.MediaCaptureOptions.capture_phase"></a>

#### capture_phase

```python
@property
def capture_phase() -> MediaCapturePhase
```

(MediaCapturePhase):  [Read-Write]

<a id="unreal.MediaCaptureOptions.capture_phase"></a>

#### capture_phase

```python
@capture_phase.setter
def capture_phase(value: MediaCapturePhase) -> None
```

<a id="unreal.MediaCaptureOptions.resize_source_buffer"></a>

#### resize_source_buffer

```python
@property
def resize_source_buffer() -> bool
```

(bool):  [Read-Write]
deprecated: bResizeSourceBuffer, please use ResizeMethod instead.

<a id="unreal.MediaCaptureOptions.resize_source_buffer"></a>

#### resize_source_buffer

```python
@resize_source_buffer.setter
def resize_source_buffer(value: bool) -> None
```

<a id="unreal.AvaRundownPageListReference"></a>