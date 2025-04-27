## MovieSceneCaptureProtocolBase Objects

```python
class MovieSceneCaptureProtocolBase(Object)
```

A capture protocol responsible for dealing with captured frames using some custom method (writing out to disk, streaming, etc)

A typical process for capture consits of the following process:
    Setup -> [ Warm up -> [ Capture Frame ] ] -> Begin Finalize -> [ HasFinishedProcessing ] -> Finalize

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: MovieSceneCaptureProtocolBase.h

<a id="unreal.MovieSceneCaptureProtocolBase.is_capturing"></a>

#### is_capturing

```python
def is_capturing() -> bool
```

x.is_capturing() -> bool
Check whether we can capture a frame from this protocol

Returns:
    bool:

<a id="unreal.MovieSceneCaptureProtocolBase.get_state"></a>

#### get_state

```python
def get_state() -> MovieSceneCaptureProtocolState
```

x.get_state() -> MovieSceneCaptureProtocolState
Get the current state of this capture protocol

Returns:
    MovieSceneCaptureProtocolState:

<a id="unreal.MovieSceneAudioCaptureProtocolBase"></a>