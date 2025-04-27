## MovieSceneCaptureEnvironment Objects

```python
class MovieSceneCaptureEnvironment(Object)
```

Movie Scene Capture Environment

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: MovieSceneCaptureEnvironment.h

<a id="unreal.MovieSceneCaptureEnvironment.is_capture_in_progress"></a>

#### is_capture_in_progress

```python
@classmethod
def is_capture_in_progress(cls) -> bool
```

X.is_capture_in_progress() -> bool
Return true if there is any capture currently active (even in a warm-up state).
Useful for checking whether to do certain operations in BeginPlay

Returns:
    bool:

<a id="unreal.MovieSceneCaptureEnvironment.get_capture_frame_number"></a>

#### get_capture_frame_number

```python
@classmethod
def get_capture_frame_number(cls) -> int
```

X.get_capture_frame_number() -> int32
Get the frame number of the current capture

Returns:
    int32:

<a id="unreal.MovieSceneCaptureEnvironment.get_capture_elapsed_time"></a>

#### get_capture_elapsed_time

```python
@classmethod
def get_capture_elapsed_time(cls) -> float
```

X.get_capture_elapsed_time() -> float
Get the total elapsed time of the current capture in seconds

Returns:
    float:

<a id="unreal.MovieSceneCaptureEnvironment.find_image_capture_protocol"></a>

#### find_image_capture_protocol

```python
@classmethod
def find_image_capture_protocol(cls) -> MovieSceneImageCaptureProtocolBase
```

X.find_image_capture_protocol() -> MovieSceneImageCaptureProtocolBase
Attempt to locate a capture protocol - may not be in a capturing state

Returns:
    MovieSceneImageCaptureProtocolBase:

<a id="unreal.MovieSceneCaptureEnvironment.find_audio_capture_protocol"></a>

#### find_audio_capture_protocol

```python
@classmethod
def find_audio_capture_protocol(cls) -> MovieSceneAudioCaptureProtocolBase
```

X.find_audio_capture_protocol() -> MovieSceneAudioCaptureProtocolBase
Attempt to locate a capture protocol - may not be in a capturing state

Returns:
    MovieSceneAudioCaptureProtocolBase:

<a id="unreal.UserDefinedCaptureProtocol"></a>