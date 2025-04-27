## UpdatePositionMethod Objects

```python
class UpdatePositionMethod(EnumBase)
```

Enum used to define how to update to a particular time

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSequencePlayer.h

<a id="unreal.UpdatePositionMethod.PLAY"></a>

#### PLAY

0: Update from the current position to a specified position (including triggering events), using the current player status

<a id="unreal.UpdatePositionMethod.JUMP"></a>

#### JUMP

1: Jump to a specified position (without triggering events in between), using the current player status

<a id="unreal.UpdatePositionMethod.SCRUB"></a>

#### SCRUB

2: Jump to a specified position, temporarily using EMovieScenePlayerStatus::Scrubbing

<a id="unreal.MovieScenePositionType"></a>