## MovieSceneScriptingIntegerChannel Objects

```python
class MovieSceneScriptingIntegerChannel(MovieSceneScriptingChannel)
```

Movie Scene Scripting Integer Channel

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneScriptingInteger.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_name`` (Name):  [Read-Write]

<a id="unreal.MovieSceneScriptingIntegerChannel.set_interpolate_linear_keys"></a>

#### set_interpolate_linear_keys

```python
def set_interpolate_linear_keys(interpolate_linear_keys: bool) -> None
```

x.set_interpolate_linear_keys(interpolate_linear_keys) -> None
Set this channel to evaluate linear keys with interpolation.

Args:
    interpolate_linear_keys (bool):

<a id="unreal.MovieSceneScriptingIntegerChannel.set_default"></a>

#### set_default

```python
def set_default(default_value: int) -> None
```

x.set_default(default_value) -> None
Set this channel's default value that should be used when no keys are present.
Sets bHasDefaultValue to true automatically.

Args:
    default_value (int32):

<a id="unreal.MovieSceneScriptingIntegerChannel.remove_key"></a>

#### remove_key

```python
def remove_key(key: MovieSceneScriptingKey) -> None
```

x.remove_key(key) -> None
Removes the specified key. Does nothing if the key is not specified or the key belongs to another channel.

Args:
    key (MovieSceneScriptingKey):

<a id="unreal.MovieSceneScriptingIntegerChannel.remove_default"></a>

#### remove_default

```python
def remove_default() -> None
```

x.remove_default() -> None
Remove this channel's default value causing the channel to have no effect where no keys are present

<a id="unreal.MovieSceneScriptingIntegerChannel.has_default"></a>

#### has_default

```python
def has_default() -> bool
```

x.has_default() -> bool


Returns:
    bool: Does this channel have a default value set?

<a id="unreal.MovieSceneScriptingIntegerChannel.get_num_keys"></a>

#### get_num_keys

```python
def get_num_keys() -> int
```

x.get_num_keys() -> int32
Returns number of keys in this channel.

Returns:
    int32:

<a id="unreal.MovieSceneScriptingIntegerChannel.get_keys_by_index"></a>

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

<a id="unreal.MovieSceneScriptingIntegerChannel.get_keys"></a>

#### get_keys

```python
def get_keys() -> Array[MovieSceneScriptingKey]
```

x.get_keys() -> Array[MovieSceneScriptingKey]
Gets all of the keys in this channel.

Returns:
    Array[MovieSceneScriptingKey]: An array of UMovieSceneScriptingIntegerKey's contained by this channel. Returns all keys even if clipped by the owning section's boundaries or outside of the current sequence play range.

<a id="unreal.MovieSceneScriptingIntegerChannel.get_interpolate_linear_keys"></a>

#### get_interpolate_linear_keys

```python
def get_interpolate_linear_keys() -> bool
```

x.get_interpolate_linear_keys() -> bool
Get whether this channel will evaluate linear keys with interpolation.

Returns:
    bool:

<a id="unreal.MovieSceneScriptingIntegerChannel.get_default"></a>

#### get_default

```python
def get_default() -> int
```

x.get_default() -> int32
Get this channel's default value that will be used when no keys are present. Only a valid
value when HasDefault() returns true.

Returns:
    int32:

<a id="unreal.MovieSceneScriptingIntegerChannel.evaluate_keys"></a>

#### evaluate_keys

```python
def evaluate_keys(range: SequencerScriptingRange,
                  frame_rate: FrameRate) -> Array[int]
```

x.evaluate_keys(range, frame_rate) -> Array[int32]
Gets baked keys in this channel.

Args:
    range (SequencerScriptingRange): 
    frame_rate (FrameRate): 

Returns:
    Array[int32]: An array of values contained by this channel. Returns baked keys in the specified range.

<a id="unreal.MovieSceneScriptingIntegerChannel.add_key"></a>

#### add_key

```python
def add_key(
    time: FrameNumber,
    new_value: int,
    sub_frame: float = 0.000000,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> MovieSceneScriptingIntegerKey
```

x.add_key(time, new_value, sub_frame=0.000000, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingIntegerKey
Add a key to this channel. This initializes a new key and returns a reference to it.

Args:
    time (FrameNumber): The frame this key should go on. Respects TimeUnit to determine if it is a display rate frame or a tick resolution frame.
    new_value (int32): The value that this key should be created with.
    sub_frame (float): Optional [0-1) clamped sub-frame to put this key on. Ignored if TimeUnit is set to Tick Resolution.
    time_unit (MovieSceneTimeUnit): Is the specified InTime in Display Rate frames or Tick Resolution.

Returns:
    MovieSceneScriptingIntegerKey: The key that was created with the specified values at the specified time.

<a id="unreal.MovieSceneScriptingObjectPathKey"></a>