## MovieSceneCapture Objects

```python
class MovieSceneCapture(Object)
```

Class responsible for capturing scene data

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: MovieSceneCapture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_command_line_arguments`` (str):  [Read-Write] Additional command line arguments to pass to the external process when capturing
- ``audio_capture_protocol`` (MovieSceneAudioCaptureProtocolBase):  [Read-Only]
- ``audio_capture_protocol_type`` (SoftClassPath):  [Read-Write] The type of capture protocol to use for audio data.
- ``close_editor_when_capture_starts`` (bool):  [Read-Write] When enabled, the editor will shutdown when the capture starts
- ``image_capture_protocol`` (MovieSceneImageCaptureProtocolBase):  [Read-Only] Capture protocol responsible for actually capturing frame data
- ``image_capture_protocol_type`` (SoftClassPath):  [Read-Write] The type of capture protocol to use for image data
- ``inherited_command_line_arguments`` (str):  [Read-Write] Command line arguments inherited from this process
- ``settings`` (MovieSceneCaptureSettings):  [Read-Write] Settings that define how to capture
- ``use_separate_process`` (bool):  [Read-Write] Whether to capture the movie in a separate process or not

<a id="unreal.MovieSceneCapture.settings"></a>

#### settings

```python
@property
def settings() -> MovieSceneCaptureSettings
```

(MovieSceneCaptureSettings):  [Read-Write] Settings that define how to capture

<a id="unreal.MovieSceneCapture.settings"></a>

#### settings

```python
@settings.setter
def settings(value: MovieSceneCaptureSettings) -> None
```

<a id="unreal.MovieSceneCapture.use_separate_process"></a>

#### use_separate_process

```python
@property
def use_separate_process() -> bool
```

(bool):  [Read-Write] Whether to capture the movie in a separate process or not

<a id="unreal.MovieSceneCapture.use_separate_process"></a>

#### use_separate_process

```python
@use_separate_process.setter
def use_separate_process(value: bool) -> None
```

<a id="unreal.MovieSceneCapture.close_editor_when_capture_starts"></a>

#### close_editor_when_capture_starts

```python
@property
def close_editor_when_capture_starts() -> bool
```

(bool):  [Read-Write] When enabled, the editor will shutdown when the capture starts

<a id="unreal.MovieSceneCapture.close_editor_when_capture_starts"></a>

#### close_editor_when_capture_starts

```python
@close_editor_when_capture_starts.setter
def close_editor_when_capture_starts(value: bool) -> None
```

<a id="unreal.MovieSceneCapture.additional_command_line_arguments"></a>

#### additional_command_line_arguments

```python
@property
def additional_command_line_arguments() -> str
```

(str):  [Read-Write] Additional command line arguments to pass to the external process when capturing

<a id="unreal.MovieSceneCapture.additional_command_line_arguments"></a>

#### additional_command_line_arguments

```python
@additional_command_line_arguments.setter
def additional_command_line_arguments(value: str) -> None
```

<a id="unreal.MovieSceneCapture.inherited_command_line_arguments"></a>

#### inherited_command_line_arguments

```python
@property
def inherited_command_line_arguments() -> str
```

(str):  [Read-Write] Command line arguments inherited from this process

<a id="unreal.MovieSceneCapture.inherited_command_line_arguments"></a>

#### inherited_command_line_arguments

```python
@inherited_command_line_arguments.setter
def inherited_command_line_arguments(value: str) -> None
```

<a id="unreal.MovieSceneCapture.set_image_capture_protocol_type"></a>

#### set_image_capture_protocol_type

```python
def set_image_capture_protocol_type(protocol_type: Class) -> None
```

x.set_image_capture_protocol_type(protocol_type) -> None
Set Image Capture Protocol Type

Args:
    protocol_type (type(Class)):

<a id="unreal.MovieSceneCapture.set_audio_capture_protocol_type"></a>

#### set_audio_capture_protocol_type

```python
def set_audio_capture_protocol_type(protocol_type: Class) -> None
```

x.set_audio_capture_protocol_type(protocol_type) -> None
Set Audio Capture Protocol Type

Args:
    protocol_type (type(Class)):

<a id="unreal.MovieSceneCapture.get_image_capture_protocol"></a>

#### get_image_capture_protocol

```python
def get_image_capture_protocol() -> MovieSceneCaptureProtocolBase
```

x.get_image_capture_protocol() -> MovieSceneCaptureProtocolBase
Access the capture protocol we are using

Returns:
    MovieSceneCaptureProtocolBase:

<a id="unreal.MovieSceneCapture.get_audio_capture_protocol"></a>

#### get_audio_capture_protocol

```python
def get_audio_capture_protocol() -> MovieSceneCaptureProtocolBase
```

x.get_audio_capture_protocol() -> MovieSceneCaptureProtocolBase
Get Audio Capture Protocol

Returns:
    MovieSceneCaptureProtocolBase:

<a id="unreal.LevelCapture"></a>