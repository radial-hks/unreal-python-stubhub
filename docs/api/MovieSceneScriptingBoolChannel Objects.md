## MovieSceneScriptingBoolChannel Objects

```python
class MovieSceneScriptingBoolChannel(MovieSceneScriptingChannel)
```

Movie Scene Scripting Bool Channel

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneScriptingBool.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_name`` (Name):  [Read-Write]

<a id="unreal.MovieSceneScriptingBoolChannel.set_default"></a>

#### set_default

```python
def set_default(default_value: bool) -> None
```

x.set_default(default_value) -> None
Set this channel's default value that should be used when no keys are present.
Sets bHasDefaultValue to true automatically.

Args:
    default_value (bool):

<a id="unreal.MovieSceneScriptingBoolChannel.remove_key"></a>

#### remove_key

```python
def remove_key(key: MovieSceneScriptingKey) -> None
```

x.remove_key(key) -> None
Removes the specified key. Does nothing if the key is not specified or the key belongs to another channel.

Args:
    key (MovieSceneScriptingKey):

<a id="unreal.MovieSceneScriptingBoolChannel.remove_default"></a>

#### remove_default

```python
def remove_default() -> None
```

x.remove_default() -> None
Remove this channel's default value causing the channel to have no effect where no keys are present

<a id="unreal.MovieSceneScriptingBoolChannel.has_default"></a>

#### has_default

```python
def has_default() -> bool
```

x.has_default() -> bool


Returns:
    bool: Does this channel have a default value set?

<a id="unreal.MovieSceneScriptingBoolChannel.get_num_keys"></a>

#### get_num_keys

```python
def get_num_keys() -> int
```

x.get_num_keys() -> int32
Returns number of keys in this channel.

Returns:
    int32:

<a id="unreal.MovieSceneScriptingBoolChannel.get_keys_by_index"></a>

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

<a id="unreal.MovieSceneScriptingBoolChannel.get_keys"></a>

#### get_keys

```python
def get_keys() -> Array[MovieSceneScriptingKey]
```

x.get_keys() -> Array[MovieSceneScriptingKey]
Gets all of the keys in this channel.

Returns:
    Array[MovieSceneScriptingKey]: An array of UMovieSceneScriptingBoolKey's contained by this channel. Returns all keys even if clipped by the owning section's boundaries or outside of the current sequence play range.

<a id="unreal.MovieSceneScriptingBoolChannel.get_default"></a>

#### get_default

```python
def get_default() -> bool
```

x.get_default() -> bool
Get this channel's default value that will be used when no keys are present. Only a valid
value when HasDefault() returns true.

Returns:
    bool:

<a id="unreal.MovieSceneScriptingBoolChannel.evaluate_keys"></a>

#### evaluate_keys

```python
def evaluate_keys(range: SequencerScriptingRange,
                  frame_rate: FrameRate) -> Array[bool]
```

x.evaluate_keys(range, frame_rate) -> Array[bool]
Gets baked keys in this channel.

Args:
    range (SequencerScriptingRange): 
    frame_rate (FrameRate): 

Returns:
    Array[bool]: An array of values contained by this channel. Returns baked keys in the specified range.

<a id="unreal.MovieSceneScriptingBoolChannel.compute_effective_range"></a>

#### compute_effective_range

```python
def compute_effective_range() -> SequencerScriptingRange
```

x.compute_effective_range() -> SequencerScriptingRange
Compute the effective range of this channel, for example, the extents of its key times

Returns:
    SequencerScriptingRange: A range that represents the greatest range of times occupied by this channel, in the sequence's frame resolution

<a id="unreal.MovieSceneScriptingBoolChannel.add_key"></a>

#### add_key

```python
def add_key(
    time: FrameNumber,
    new_value: bool,
    sub_frame: float = 0.000000,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> MovieSceneScriptingBoolKey
```

x.add_key(time, new_value, sub_frame=0.000000, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingBoolKey
Add a key to this channel. This initializes a new key and returns a reference to it.

Args:
    time (FrameNumber): The frame this key should go on. Respects TimeUnit to determine if it is a display rate frame or a tick resolution frame.
    new_value (bool): The value that this key should be created with.
    sub_frame (float): Optional [0-1) clamped sub-frame to put this key on. Ignored if TimeUnit is set to Tick Resolution.
    time_unit (MovieSceneTimeUnit): Is the specified InTime in Display Rate frames or Tick Resolution.

Returns:
    MovieSceneScriptingBoolKey: The key that was created with the specified values at the specified time.

<a id="unreal.MovieSceneScriptingByteKey"></a>