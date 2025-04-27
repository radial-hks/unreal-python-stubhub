## MediaOutput Objects

```python
class MediaOutput(Object)
```

Abstract base class for media output.

Media output describe the location and/or settings of media objects that can
be used to output the content of Unreal Engine to a target device via a MediaCapture.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``number_of_texture_buffers`` (int32):  [Read-Write] Number of texture used to transfer the texture from the GPU to the system memory.
  A smaller number is most likely to block the GPU (wait for the transfer to complete).
  A bigger number is most likely to increase latency.
  note: Some Capture are not are executed on the GPU. If it's the case then no buffer will be needed and no buffer will be created.

<a id="unreal.MediaOutput.validate"></a>

#### validate

```python
def validate() -> Optional[str]
```

x.validate() -> str or None
Validate the media output settings (must be implemented in child classes).

Returns:
    str or None: true if validation passed, false otherwise.

    out_failure_reason (str):

<a id="unreal.MediaOutput.create_media_capture"></a>

#### create_media_capture

```python
def create_media_capture() -> MediaCapture
```

x.create_media_capture() -> MediaCapture
Creates the specific implementation of the MediaCapture for the MediaOutput.

Returns:
    MediaCapture:

<a id="unreal.FileMediaOutput"></a>