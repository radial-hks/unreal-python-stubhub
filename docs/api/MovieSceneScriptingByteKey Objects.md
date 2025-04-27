## MovieSceneScriptingByteKey Objects

```python
class MovieSceneScriptingByteKey(MovieSceneScriptingKey)
```

Exposes a Sequencer byte/enum type key to Python/Blueprints.
Stores a reference to the data so changes to this class are forwarded onto the underlying data structures.

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneScriptingByte.h

<a id="unreal.MovieSceneScriptingByteKey.set_value"></a>

#### set_value

```python
def set_value(new_value: int) -> None
```

x.set_value(new_value) -> None
Sets the value for this key, reflecting it in the owning channel.

Args:
    new_value (uint8): The new value for this key.

<a id="unreal.MovieSceneScriptingByteKey.set_time"></a>

#### set_time

```python
def set_time(
        new_frame_number: FrameNumber,
        sub_frame: float = 0.000000,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

x.set_time(new_frame_number, sub_frame=0.000000, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Sets the time for this key in the owning channel. Will replace any key that already exists at that frame number in this channel.

Args:
    new_frame_number (FrameNumber): What frame should this key be moved to? This should be in the time unit specified by TimeUnit.
    sub_frame (float): If using Display Rate time, what is the sub-frame this should go to? Clamped [0-1), and ignored with when TimeUnit is set to Tick Resolution.
    time_unit (MovieSceneTimeUnit): Should the NewFrameNumber be interpreted as Display Rate frames or in Tick Resolution?

<a id="unreal.MovieSceneScriptingByteKey.get_value"></a>

#### get_value

```python
def get_value() -> int
```

x.get_value() -> uint8
Gets the value for this key from the owning channel.

Returns:
    uint8: The value for this key.

<a id="unreal.MovieSceneScriptingByteKey.get_time"></a>

#### get_time

```python
def get_time(
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> FrameTime
```

x.get_time(time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
Gets the time for this key from the owning channel.

Args:
    time_unit (MovieSceneTimeUnit): Should the time be returned in Display Rate frames (possibly with a sub-frame value) or in Tick Resolution with no sub-frame values?

Returns:
    FrameTime: The time of this key which combines both the frame number and the sub-frame it is on. Sub-frame will be zero if you request Tick Resolution.

<a id="unreal.MovieSceneScriptingByteChannel"></a>