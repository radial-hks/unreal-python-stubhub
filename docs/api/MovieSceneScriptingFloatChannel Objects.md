## MovieSceneScriptingFloatChannel Objects

```python
class MovieSceneScriptingFloatChannel(MovieSceneScriptingChannel)
```

Movie Scene Scripting Float Channel

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneScriptingFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_name`` (Name):  [Read-Write]

<a id="unreal.MovieSceneScriptingFloatChannel.set_pre_infinity_extrapolation"></a>

#### set_pre_infinity_extrapolation

```python
def set_pre_infinity_extrapolation(
        extrapolation: RichCurveExtrapolation) -> None
```

x.set_pre_infinity_extrapolation(extrapolation) -> None
Sets the Pre-infinity extrapolation state. See ERichCurveExtrapolation for more detail.

Args:
    extrapolation (RichCurveExtrapolation): The new extrapolation mode this key should use for evaluating before this key.

<a id="unreal.MovieSceneScriptingFloatChannel.set_post_infinity_extrapolation"></a>

#### set_post_infinity_extrapolation

```python
def set_post_infinity_extrapolation(
        extrapolation: RichCurveExtrapolation) -> None
```

x.set_post_infinity_extrapolation(extrapolation) -> None
Sets the Post-infinity extrapolation state. See ERichCurveExtrapolation for more detail.

Args:
    extrapolation (RichCurveExtrapolation): The new extrapolation mode this key should use for evaluating after this key.

<a id="unreal.MovieSceneScriptingFloatChannel.set_default"></a>

#### set_default

```python
def set_default(default_value: float) -> None
```

x.set_default(default_value) -> None
Set this channel's default value that should be used when no keys are present.
Sets bHasDefaultValue to true automatically.

Args:
    default_value (float):

<a id="unreal.MovieSceneScriptingFloatChannel.remove_key"></a>

#### remove_key

```python
def remove_key(key: MovieSceneScriptingKey) -> None
```

x.remove_key(key) -> None
Removes the specified key. Does nothing if the key is not specified or the key belongs to another channel.

Args:
    key (MovieSceneScriptingKey):

<a id="unreal.MovieSceneScriptingFloatChannel.remove_default"></a>

#### remove_default

```python
def remove_default() -> None
```

x.remove_default() -> None
Remove this channel's default value causing the channel to have no effect where no keys are present

<a id="unreal.MovieSceneScriptingFloatChannel.has_default"></a>

#### has_default

```python
def has_default() -> bool
```

x.has_default() -> bool


Returns:
    bool: Does this channel have a default value set?

<a id="unreal.MovieSceneScriptingFloatChannel.get_pre_infinity_extrapolation"></a>

#### get_pre_infinity_extrapolation

```python
def get_pre_infinity_extrapolation() -> RichCurveExtrapolation
```

x.get_pre_infinity_extrapolation() -> RichCurveExtrapolation


Returns:
    RichCurveExtrapolation: Gets the Pre-infinity extrapolation state. See ERichCurveExtrapolation for more detail.

<a id="unreal.MovieSceneScriptingFloatChannel.get_post_infinity_extrapolation"></a>

#### get_post_infinity_extrapolation

```python
def get_post_infinity_extrapolation() -> RichCurveExtrapolation
```

x.get_post_infinity_extrapolation() -> RichCurveExtrapolation


Returns:
    RichCurveExtrapolation: Gets the Post-infinity extrapolation state. See ERichCurveExtrapolation for more detail.

<a id="unreal.MovieSceneScriptingFloatChannel.get_num_keys"></a>

#### get_num_keys

```python
def get_num_keys() -> int
```

x.get_num_keys() -> int32
Returns number of keys in this channel.

Returns:
    int32:

<a id="unreal.MovieSceneScriptingFloatChannel.get_keys_by_index"></a>

#### get_keys_by_index

```python
def get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
```

x.get_keys_by_index(indices) -> Array[MovieSceneScriptingKey]
Gets the keys in this channel specified by the specific index
Indices: The indices from which to get the keys from

Args:
    indices (Array[int32]): 

Returns:
    Array[MovieSceneScriptingKey]: An array of UMovieSceneScriptingKey's contained by this channel. Returns all keys specified by the indices, even if out of range.

<a id="unreal.MovieSceneScriptingFloatChannel.get_keys"></a>

#### get_keys

```python
def get_keys() -> Array[MovieSceneScriptingKey]
```

x.get_keys() -> Array[MovieSceneScriptingKey]
Gets all of the keys in this channel.

Returns:
    Array[MovieSceneScriptingKey]: An array of UMovieSceneScriptingFloatKey's contained by this channel. Returns all keys even if clipped by the owning section's boundaries or outside of the current sequence play range.

<a id="unreal.MovieSceneScriptingFloatChannel.get_default"></a>

#### get_default

```python
def get_default() -> float
```

x.get_default() -> float
Get this channel's default value that will be used when no keys are present. Only a valid
value when HasDefault() returns true.

Returns:
    float:

<a id="unreal.MovieSceneScriptingFloatChannel.evaluate_keys"></a>

#### evaluate_keys

```python
def evaluate_keys(range: SequencerScriptingRange,
                  frame_rate: FrameRate) -> Array[float]
```

x.evaluate_keys(range, frame_rate) -> Array[float]
Gets baked keys in this channel.

Args:
    range (SequencerScriptingRange): 
    frame_rate (FrameRate): 

Returns:
    Array[float]: An array of float's contained by this channel. Returns baked keys in the specified range.

<a id="unreal.MovieSceneScriptingFloatChannel.compute_effective_range"></a>

#### compute_effective_range

```python
def compute_effective_range() -> SequencerScriptingRange
```

x.compute_effective_range() -> SequencerScriptingRange
Compute the effective range of this channel, for example, the extents of its key times

Returns:
    SequencerScriptingRange: A range that represents the greatest range of times occupied by this channel, in the sequence's frame resolution

<a id="unreal.MovieSceneScriptingFloatChannel.add_key"></a>

#### add_key

```python
def add_key(
    time: FrameNumber,
    new_value: float,
    sub_frame: float = 0.000000,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
    interpolation: MovieSceneKeyInterpolation = MovieSceneKeyInterpolation.AUTO
) -> MovieSceneScriptingFloatKey
```

x.add_key(time, new_value, sub_frame=0.000000, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, interpolation=MovieSceneKeyInterpolation.AUTO) -> MovieSceneScriptingFloatKey
Add a key to this channel. This initializes a new key and returns a reference to it.

Args:
    time (FrameNumber): The frame this key should go on. Respects TimeUnit to determine if it is a display rate frame or a tick resolution frame.
    new_value (float): The value that this key should be created with.
    sub_frame (float): Optional [0-1) clamped sub-frame to put this key on. Ignored if TimeUnit is set to Tick Resolution.
    time_unit (MovieSceneTimeUnit): Is the specified InTime in Display Rate frames or Tick Resolution.
    interpolation (MovieSceneKeyInterpolation): Interpolation method the key should use.

Returns:
    MovieSceneScriptingFloatKey: The key that was created with the specified values at the specified time.

<a id="unreal.MovieSceneScriptingIntegerKey"></a>