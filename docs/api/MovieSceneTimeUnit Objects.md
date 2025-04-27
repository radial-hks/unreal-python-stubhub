## MovieSceneTimeUnit Objects

```python
class MovieSceneTimeUnit(EnumBase)
```

Specifies which frame of reference you want to set/get time values in. This allows users to work
in reference space without having to manually convert back and forth all of the time.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneTimeUnit.h

<a id="unreal.MovieSceneTimeUnit.DISPLAY_RATE"></a>

#### DISPLAY_RATE

0: Display Rate matches the values shown in the UI such as 30fps giving you 30 frames per second. Supports sub-frame values (precision limited to Tick Resolution)

<a id="unreal.MovieSceneTimeUnit.TICK_RESOLUTION"></a>

#### TICK_RESOLUTION

1: Tick Resolution is the internal resolution that data is actually stored in, such as 24000 giving you 24,000 frames per second. This is the smallest interval that data can be stored on.

<a id="unreal.MovieSceneBlendType"></a>