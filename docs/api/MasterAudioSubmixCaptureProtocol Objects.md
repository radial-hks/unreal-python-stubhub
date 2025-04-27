## MasterAudioSubmixCaptureProtocol Objects

```python
class MasterAudioSubmixCaptureProtocol(MovieSceneAudioCaptureProtocolBase)
```

This is an experimental audio capture implementation which captures the final output from the master submix.
This requires that your sequence can be played back in real-time (when rendering is disabled).
If the sequence evaluation hitches the audio will become desynchronized due to their being more time passed
in real time (platform time) than in the sequence itself.

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: AudioCaptureProtocol.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``file_name`` (str):  [Read-Write]

<a id="unreal.MasterAudioSubmixCaptureProtocol.file_name"></a>

#### file_name

```python
@property
def file_name() -> str
```

(str):  [Read-Write]

<a id="unreal.MasterAudioSubmixCaptureProtocol.file_name"></a>

#### file_name

```python
@file_name.setter
def file_name(value: str) -> None
```

<a id="unreal.MovieSceneImageCaptureProtocolBase"></a>