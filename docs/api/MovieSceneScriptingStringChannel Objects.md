## MovieSceneScriptingStringChannel Objects

```python
class MovieSceneScriptingStringChannel(MovieSceneScriptingChannel)
```

Movie Scene Scripting String Channel

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneScriptingString.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_name`` (Name):  [Read-Write]

<a id="unreal.MovieSceneScriptingStringChannel.set_default"></a>

#### set_default

```python
def set_default(default_value: str) -> None
```

x.set_default(default_value) -> None
Set this channel's default value that should be used when no keys are present.
Sets bHasDefaultValue to true automatically.

Args:
    default_value (str):

<a id="unreal.MovieSceneScriptingStringChannel.remove_key"></a>

#### remove_key

```python
def remove_key(key: MovieSceneScriptingKey) -> None
```

x.remove_key(key) -> None
Removes the specified key. Does nothing if the key is not specified or the key belongs to another channel.

Args:
    key (MovieSceneScriptingKey):

<a id="unreal.MovieSceneScriptingStringChannel.remove_default"></a>

#### remove_default

```python
def remove_default() -> None
```

x.remove_default() -> None
Remove this channel's default value causing the channel to have no effect where no keys are present

<a id="unreal.MovieSceneScriptingStringChannel.has_default"></a>

#### has_default

```python
def has_default() -> bool
```

x.has_default() -> bool


Returns:
    bool: Does this channel have a default value set?

<a id="unreal.MovieSceneScriptingStringChannel.get_keys_by_index"></a>

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

<a id="unreal.MovieSceneScriptingStringChannel.get_keys"></a>

#### get_keys

```python
def get_keys() -> Array[MovieSceneScriptingKey]
```

x.get_keys() -> Array[MovieSceneScriptingKey]
Gets all of the keys in this channel.

Returns:
    Array[MovieSceneScriptingKey]: An array of UMovieSceneScriptingStringKey's contained by this channel. Returns all keys even if clipped by the owning section's boundaries or outside of the current sequence play range.

<a id="unreal.MovieSceneScriptingStringChannel.get_default"></a>

#### get_default

```python
def get_default() -> str
```

x.get_default() -> str
Get this channel's default value that will be used when no keys are present. Only a valid
value when HasDefault() returns true.

Returns:
    str:

<a id="unreal.MovieSceneScriptingStringChannel.add_key"></a>

#### add_key

```python
def add_key(
    time: FrameNumber,
    new_value: str,
    sub_frame: float = 0.000000,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> MovieSceneScriptingStringKey
```

x.add_key(time, new_value, sub_frame=0.000000, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingStringKey
Add a key to this channel. This initializes a new key and returns a reference to it.

Args:
    time (FrameNumber): The frame this key should go on. Respects TimeUnit to determine if it is a display rate frame or a tick resolution frame.
    new_value (str): The value that this key should be created with.
    sub_frame (float): Optional [0-1) clamped sub-frame to put this key on. Ignored if TimeUnit is set to Tick Resolution.
    time_unit (MovieSceneTimeUnit): Is the specified InTime in Display Rate frames or Tick Resolution.

Returns:
    MovieSceneScriptingStringKey: The key that was created with the specified values at the specified time.

<a id="unreal.MovieSceneBindingExtensions"></a>