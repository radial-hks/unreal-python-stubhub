## LevelCapture Objects

```python
class LevelCapture(MovieSceneCapture)
```

Level Capture

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: LevelCapture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_command_line_arguments`` (str):  [Read-Write] Additional command line arguments to pass to the external process when capturing
- ``audio_capture_protocol`` (MovieSceneAudioCaptureProtocolBase):  [Read-Only]
- ``audio_capture_protocol_type`` (SoftClassPath):  [Read-Write] The type of capture protocol to use for audio data.
- ``auto_start_capture`` (bool):  [Read-Write] Specifies whether the capture should start immediately, or whether it will be invoked externally (through StartMovieCapture/StopMovieCapture exec commands)
- ``close_editor_when_capture_starts`` (bool):  [Read-Write] When enabled, the editor will shutdown when the capture starts
- ``image_capture_protocol`` (MovieSceneImageCaptureProtocolBase):  [Read-Only] Capture protocol responsible for actually capturing frame data
- ``image_capture_protocol_type`` (SoftClassPath):  [Read-Write] The type of capture protocol to use for image data
- ``inherited_command_line_arguments`` (str):  [Read-Write] Command line arguments inherited from this process
- ``settings`` (MovieSceneCaptureSettings):  [Read-Write] Settings that define how to capture
- ``use_separate_process`` (bool):  [Read-Write] Whether to capture the movie in a separate process or not

<a id="unreal.MovieSceneCaptureEnvironment"></a>