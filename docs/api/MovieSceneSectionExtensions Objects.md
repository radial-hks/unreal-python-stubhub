## MovieSceneSectionExtensions Objects

```python
class MovieSceneSectionExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieSceneSections for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneSectionExtensions.h

<a id="unreal.MovieSceneSectionExtensions.set_start_frame_seconds"></a>

#### set_start_frame_seconds

```python
@classmethod
def set_start_frame_seconds(cls, section: MovieSceneSection,
                            start_time: float) -> None
```

X.set_start_frame_seconds(section, start_time) -> None
Set start time in seconds

Args:
    section (MovieSceneSection): The section within which to set the start time
    start_time (float): The desired start time for this section

<a id="unreal.MovieSceneSectionExtensions.set_start_frame_bounded"></a>

#### set_start_frame_bounded

```python
@classmethod
def set_start_frame_bounded(cls, section: MovieSceneSection,
                            is_bounded: bool) -> None
```

X.set_start_frame_bounded(section, is_bounded) -> None
Set start frame bounded

Args:
    section (MovieSceneSection): The section to set whether the start frame is bounded or not
    is_bounded (bool):

<a id="unreal.MovieSceneSectionExtensions.set_start_frame"></a>

#### set_start_frame

```python
@classmethod
def set_start_frame(cls, section: MovieSceneSection, start_frame: int) -> None
```

X.set_start_frame(section, start_frame) -> None
Set start frame

Args:
    section (MovieSceneSection): The section within which to set the start frame
    start_frame (int32): The desired start frame for this section

<a id="unreal.MovieSceneSectionExtensions.set_range_seconds"></a>

#### set_range_seconds

```python
@classmethod
def set_range_seconds(cls, section: MovieSceneSection, start_time: float,
                      end_time: float) -> None
```

X.set_range_seconds(section, start_time, end_time) -> None
Set range in seconds

Args:
    section (MovieSceneSection): The section within which to set the range
    start_time (float): The desired start frame for this section
    end_time (float): The desired end frame for this section

<a id="unreal.MovieSceneSectionExtensions.set_range"></a>

#### set_range

```python
@classmethod
def set_range(cls, section: MovieSceneSection, start_frame: int,
              end_frame: int) -> None
```

X.set_range(section, start_frame, end_frame) -> None
Set range

Args:
    section (MovieSceneSection): The section within which to set the range
    start_frame (int32): The desired start frame for this section
    end_frame (int32): The desired end frame for this section

<a id="unreal.MovieSceneSectionExtensions.set_end_frame_seconds"></a>

#### set_end_frame_seconds

```python
@classmethod
def set_end_frame_seconds(cls, section: MovieSceneSection,
                          end_time: float) -> None
```

X.set_end_frame_seconds(section, end_time) -> None
Set end time in seconds

Args:
    section (MovieSceneSection): The section within which to set the end time
    end_time (float): The desired end time for this section

<a id="unreal.MovieSceneSectionExtensions.set_end_frame_bounded"></a>

#### set_end_frame_bounded

```python
@classmethod
def set_end_frame_bounded(cls, section: MovieSceneSection,
                          is_bounded: bool) -> None
```

X.set_end_frame_bounded(section, is_bounded) -> None
Set end frame bounded

Args:
    section (MovieSceneSection): The section to set whether the end frame is bounded or not
    is_bounded (bool):

<a id="unreal.MovieSceneSectionExtensions.set_end_frame"></a>

#### set_end_frame

```python
@classmethod
def set_end_frame(cls, section: MovieSceneSection, end_frame: int) -> None
```

X.set_end_frame(section, end_frame) -> None
Set end frame

Args:
    section (MovieSceneSection): The section within which to set the end frame
    end_frame (int32): The desired start frame for this section

<a id="unreal.MovieSceneSectionExtensions.has_start_frame"></a>

#### has_start_frame

```python
@classmethod
def has_start_frame(cls, section: MovieSceneSection) -> bool
```

X.has_start_frame(section) -> bool
Has start frame

Args:
    section (MovieSceneSection): The section being queried

Returns:
    bool: Whether this section has a valid start frame (else infinite)

<a id="unreal.MovieSceneSectionExtensions.has_end_frame"></a>

#### has_end_frame

```python
@classmethod
def has_end_frame(cls, section: MovieSceneSection) -> bool
```

X.has_end_frame(section) -> bool
Has end frame

Args:
    section (MovieSceneSection): The section being queried

Returns:
    bool: Whether this section has a valid end frame (else infinite)

<a id="unreal.MovieSceneSectionExtensions.get_start_frame_seconds"></a>

#### get_start_frame_seconds

```python
@classmethod
def get_start_frame_seconds(cls, section: MovieSceneSection) -> float
```

X.get_start_frame_seconds(section) -> float
Get start time in seconds. Will throw an exception if section has no start frame, use HasStartFrame to check first.

Args:
    section (MovieSceneSection): The section within which to get the start time

Returns:
    float: Start time of this section

<a id="unreal.MovieSceneSectionExtensions.get_start_frame"></a>

#### get_start_frame

```python
@classmethod
def get_start_frame(cls, section: MovieSceneSection) -> int
```

X.get_start_frame(section) -> int32
Get start frame. Will throw an exception if section has no start frame, use HasStartFrame to check first.

Args:
    section (MovieSceneSection): The section within which to get the start frame

Returns:
    int32: Start frame of this section

<a id="unreal.MovieSceneSectionExtensions.get_parent_sequence_frame"></a>

#### get_parent_sequence_frame

```python
@classmethod
def get_parent_sequence_frame(cls, section: MovieSceneSubSection, frame: int,
                              parent_sequence: MovieSceneSequence) -> int
```

X.get_parent_sequence_frame(section, frame, parent_sequence) -> int32
Get the frame in the space of its parent sequence

Args:
    section (MovieSceneSubSection): The section that the InFrame is local to
    frame (int32): The desired local frame
    parent_sequence (MovieSceneSequence): The parent sequence to traverse from

Returns:
    int32: The frame at the parent sequence

<a id="unreal.MovieSceneSectionExtensions.get_end_frame_seconds"></a>

#### get_end_frame_seconds

```python
@classmethod
def get_end_frame_seconds(cls, section: MovieSceneSection) -> float
```

X.get_end_frame_seconds(section) -> float
Get end time in seconds. Will throw an exception if section has no end frame, use HasEndFrame to check first.

Args:
    section (MovieSceneSection): The section within which to get the end time

Returns:
    float: End time of this section

<a id="unreal.MovieSceneSectionExtensions.get_end_frame"></a>

#### get_end_frame

```python
@classmethod
def get_end_frame(cls, section: MovieSceneSection) -> int
```

X.get_end_frame(section) -> int32
Get end frame. Will throw an exception if section has no end frame, use HasEndFrame to check first.

Args:
    section (MovieSceneSection): The section within which to get the end frame

Returns:
    int32: End frame of this section

<a id="unreal.MovieSceneSectionExtensions.get_channels_by_type"></a>

#### get_channels_by_type

```python
@classmethod
def get_channels_by_type(
        cls, section: MovieSceneSection,
        channel_type: Class) -> Array[MovieSceneScriptingChannel]
```

X.get_channels_by_type(section, channel_type) -> Array[MovieSceneScriptingChannel]
Find all channels that belong to the specified UMovieSceneSection that match the specific type. This will filter out any children who do not inherit
from the specified type for you.

Args:
    section (MovieSceneSection): The section to use.
    channel_type (type(Class)): The class type to look for.

Returns:
    Array[MovieSceneScriptingChannel]: An array containing any key channels that match the type specified

<a id="unreal.MovieSceneSectionExtensions.get_channel"></a>

#### get_channel

```python
@classmethod
def get_channel(cls, section: MovieSceneSection,
                channel_name: Name) -> MovieSceneScriptingChannel
```

X.get_channel(section, channel_name) -> MovieSceneScriptingChannel
Get channel from specified section and channel name

Args:
    section (MovieSceneSection): The section to use.
    channel_name (Name): The name of the channel.

Returns:
    MovieSceneScriptingChannel: The channel if it exists

<a id="unreal.MovieSceneSectionExtensions.get_auto_size_start_frame_seconds"></a>

#### get_auto_size_start_frame_seconds

```python
@classmethod
def get_auto_size_start_frame_seconds(cls,
                                      section: MovieSceneSection) -> float
```

X.get_auto_size_start_frame_seconds(section) -> float
Get start time of the AutoSize in seconds. Will throw an exception if section has no start frame, use GetAutoSizeHasStartFrame to check first.

Args:
    section (MovieSceneSection): The section being queried

Returns:
    float: The start frame of the AutoSize data in seconds.

<a id="unreal.MovieSceneSectionExtensions.get_auto_size_start_frame"></a>

#### get_auto_size_start_frame

```python
@classmethod
def get_auto_size_start_frame(cls, section: MovieSceneSection) -> int
```

X.get_auto_size_start_frame(section) -> int32
Get start frame of the AutoSize. Will throw an exception if section has no start frame, use GetAutoSizeHasStartFrame to check first.

Args:
    section (MovieSceneSection): The section being queried

Returns:
    int32: The start frame of the AutoSize data.

<a id="unreal.MovieSceneSectionExtensions.get_auto_size_has_start_frame"></a>

#### get_auto_size_has_start_frame

```python
@classmethod
def get_auto_size_has_start_frame(cls, section: MovieSceneSection) -> bool
```

X.get_auto_size_has_start_frame(section) -> bool
Checks to see if this section has an AutoSize implementation, and if so, if that implementation has a start frame.

Args:
    section (MovieSceneSection): The section being queried

Returns:
    bool: Whether this section has a valid autosize range, and a valid start frame

<a id="unreal.MovieSceneSectionExtensions.get_auto_size_has_end_frame"></a>

#### get_auto_size_has_end_frame

```python
@classmethod
def get_auto_size_has_end_frame(cls, section: MovieSceneSection) -> bool
```

X.get_auto_size_has_end_frame(section) -> bool
Checks to see if this section has an AutoSize implementation, and if so, if that implementation has a end frame.

Args:
    section (MovieSceneSection): The section being queried

Returns:
    bool: Whether this section has a valid autosize range, and a valid end frame

<a id="unreal.MovieSceneSectionExtensions.get_auto_size_end_frame_seconds"></a>

#### get_auto_size_end_frame_seconds

```python
@classmethod
def get_auto_size_end_frame_seconds(cls, section: MovieSceneSection) -> float
```

X.get_auto_size_end_frame_seconds(section) -> float
Get end time of the AutoSize seconds. Will throw an exception if section has no end frame, use GetAutoSizeHasEndFrame to check first.

Args:
    section (MovieSceneSection): The section being queried

Returns:
    float: The end frame of the AutoSize data in seconds.

<a id="unreal.MovieSceneSectionExtensions.get_auto_size_end_frame"></a>

#### get_auto_size_end_frame

```python
@classmethod
def get_auto_size_end_frame(cls, section: MovieSceneSection) -> int
```

X.get_auto_size_end_frame(section) -> int32
Get end frame of the AutoSize. Will throw an exception if section has no end frame, use GetAutoSizeHasEndFrame to check first.

Args:
    section (MovieSceneSection): The section being queried

Returns:
    int32: The end frame of the AutoSize data.

<a id="unreal.MovieSceneSectionExtensions.get_all_channels"></a>

#### get_all_channels

```python
@classmethod
def get_all_channels(
        cls, section: MovieSceneSection) -> Array[MovieSceneScriptingChannel]
```

X.get_all_channels(section) -> Array[MovieSceneScriptingChannel]
Find all channels that belong to the specified UMovieSceneSection. Some sections have many channels (such as
Transforms containing 9 double channels to represent Translation/Rotation/Scale), and a section may have mixed
channel types.

Args:
    section (MovieSceneSection): The section to use.

Returns:
    Array[MovieSceneScriptingChannel]: An array containing any key channels that match the type specified

<a id="unreal.MovieSceneSequenceExtensions"></a>