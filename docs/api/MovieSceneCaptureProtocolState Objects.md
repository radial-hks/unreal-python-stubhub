## MovieSceneCaptureProtocolState Objects

```python
class MovieSceneCaptureProtocolState(EnumBase)
```

EMovie Scene Capture Protocol State

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: MovieSceneCaptureProtocolBase.h

<a id="unreal.MovieSceneCaptureProtocolState.IDLE"></a>

#### IDLE

0: The protocol is idle, and has not even been initialized

<a id="unreal.MovieSceneCaptureProtocolState.INITIALIZED"></a>

#### INITIALIZED

1: The protocol has been initialized (and bound to a viewport) but is not capturing frames yet

<a id="unreal.MovieSceneCaptureProtocolState.CAPTURING"></a>

#### CAPTURING

2: The protocol has been initialized, bound to a viewport and is capturing data

<a id="unreal.MovieSceneCaptureProtocolState.FINALIZING"></a>

#### FINALIZING

3: The protocol has finished capturing data, and is pending finalization

<a id="unreal.ShouldCookBlueprintPropertyGuids"></a>