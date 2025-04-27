## MovieSceneEvaluationType Objects

```python
class MovieSceneEvaluationType(EnumBase)
```

EMovie Scene Evaluation Type

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneFwd.h

<a id="unreal.MovieSceneEvaluationType.FRAME_LOCKED"></a>

#### FRAME_LOCKED

0: Play the sequence frame-locked to its playback rate (snapped to the tick resolution - no sub-frames)

<a id="unreal.MovieSceneEvaluationType.WITH_SUB_FRAMES"></a>

#### WITH_SUB_FRAMES

1: Play the sequence in real-time, with sub-frame interpolation if necessary

<a id="unreal.UpdateClockSource"></a>