## MovieSceneSection Objects

```python
class MovieSceneSection(MovieSceneSignedObject)
```

Base class for movie scene sections

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneSection.set_row_index"></a>

#### set_row_index

```python
def set_row_index(new_row_index: int) -> None
```

x.set_row_index(new_row_index) -> None
Sets this section's new row index

Args:
    new_row_index (int32):

<a id="unreal.MovieSceneSection.set_pre_roll_frames"></a>

#### set_pre_roll_frames

```python
def set_pre_roll_frames(pre_roll_frames: int) -> None
```

x.set_pre_roll_frames(pre_roll_frames) -> None
Gets the number of frames to prepare this section for evaluation before it actually starts.

Args:
    pre_roll_frames (int32):

<a id="unreal.MovieSceneSection.set_post_roll_frames"></a>

#### set_post_roll_frames

```python
def set_post_roll_frames(post_roll_frames: int) -> None
```

x.set_post_roll_frames(post_roll_frames) -> None
Gets/sets the number of frames to continue 'postrolling' this section for after evaluation has ended.

Args:
    post_roll_frames (int32):

<a id="unreal.MovieSceneSection.set_overlap_priority"></a>

#### set_overlap_priority

```python
def set_overlap_priority(new_priority: int) -> None
```

x.set_overlap_priority(new_priority) -> None
Sets this section's priority over overlapping sections (higher wins)

Args:
    new_priority (int32):

<a id="unreal.MovieSceneSection.set_is_locked"></a>

#### set_is_locked

```python
def set_is_locked(is_locked: bool) -> None
```

x.set_is_locked(is_locked) -> None
Whether or not this section is locked.

Args:
    is_locked (bool):

<a id="unreal.MovieSceneSection.set_is_active"></a>

#### set_is_active

```python
def set_is_active(is_active: bool) -> None
```

x.set_is_active(is_active) -> None
Whether or not this section is active.

Args:
    is_active (bool):

<a id="unreal.MovieSceneSection.set_completion_mode"></a>

#### set_completion_mode

```python
def set_completion_mode(completion_mode: MovieSceneCompletionMode) -> None
```

x.set_completion_mode(completion_mode) -> None
* Sets this section's completion mode

Args:
    completion_mode (MovieSceneCompletionMode):

<a id="unreal.MovieSceneSection.set_color_tint"></a>

#### set_color_tint

```python
def set_color_tint(color_tint: Color) -> None
```

x.set_color_tint(color_tint) -> None
Set this section's color tint.

Args:
    color_tint (Color):

<a id="unreal.MovieSceneSection.set_blend_type"></a>

#### set_blend_type

```python
def set_blend_type(blend_type: MovieSceneBlendType) -> None
```

x.set_blend_type(blend_type) -> None
Sets this section's blend type

Args:
    blend_type (MovieSceneBlendType):

<a id="unreal.MovieSceneSection.is_locked"></a>

#### is_locked

```python
def is_locked() -> bool
```

x.is_locked() -> bool
Is Locked

Returns:
    bool:

<a id="unreal.MovieSceneSection.is_active"></a>

#### is_active

```python
def is_active() -> bool
```

x.is_active() -> bool
Is Active

Returns:
    bool:

<a id="unreal.MovieSceneSection.get_row_index"></a>

#### get_row_index

```python
def get_row_index() -> int
```

x.get_row_index() -> int32
Gets the row index for this section

Returns:
    int32:

<a id="unreal.MovieSceneSection.get_pre_roll_frames"></a>

#### get_pre_roll_frames

```python
def get_pre_roll_frames() -> int
```

x.get_pre_roll_frames() -> int32
Get Pre Roll Frames

Returns:
    int32:

<a id="unreal.MovieSceneSection.get_post_roll_frames"></a>

#### get_post_roll_frames

```python
def get_post_roll_frames() -> int
```

x.get_post_roll_frames() -> int32
Get Post Roll Frames

Returns:
    int32:

<a id="unreal.MovieSceneSection.get_overlap_priority"></a>

#### get_overlap_priority

```python
def get_overlap_priority() -> int
```

x.get_overlap_priority() -> int32
Gets this section's priority over overlapping sections (higher wins)

Returns:
    int32:

<a id="unreal.MovieSceneSection.get_completion_mode"></a>

#### get_completion_mode

```python
def get_completion_mode() -> MovieSceneCompletionMode
```

x.get_completion_mode() -> MovieSceneCompletionMode
Gets this section's completion mode

Returns:
    MovieSceneCompletionMode:

<a id="unreal.MovieSceneSection.get_color_tint"></a>

#### get_color_tint

```python
def get_color_tint() -> Color
```

x.get_color_tint() -> Color
Get this section's color tint.

Returns:
    Color:

<a id="unreal.MovieSceneSection.get_blend_type"></a>

#### get_blend_type

```python
def get_blend_type() -> OptionalMovieSceneBlendType
```

x.get_blend_type() -> OptionalMovieSceneBlendType
Gets this section's blend type

Returns:
    OptionalMovieSceneBlendType:

<a id="unreal.MovieSceneSection.set_start_frame_seconds"></a>

#### set_start_frame_seconds

```python
def set_start_frame_seconds(start_time: float) -> None
```

x.set_start_frame_seconds(start_time) -> None
Set start time in seconds

Args:
    start_time (float): The desired start time for this section

<a id="unreal.MovieSceneSection.set_start_frame_bounded"></a>

#### set_start_frame_bounded

```python
def set_start_frame_bounded(is_bounded: bool) -> None
```

x.set_start_frame_bounded(is_bounded) -> None
Set start frame bounded

Args:
    is_bounded (bool):

<a id="unreal.MovieSceneSection.set_start_frame"></a>

#### set_start_frame

```python
def set_start_frame(start_frame: int) -> None
```

x.set_start_frame(start_frame) -> None
Set start frame

Args:
    start_frame (int32): The desired start frame for this section

<a id="unreal.MovieSceneSection.set_range_seconds"></a>

#### set_range_seconds

```python
def set_range_seconds(start_time: float, end_time: float) -> None
```

x.set_range_seconds(start_time, end_time) -> None
Set range in seconds

Args:
    start_time (float): The desired start frame for this section
    end_time (float): The desired end frame for this section

<a id="unreal.MovieSceneSection.set_range"></a>

#### set_range

```python
def set_range(start_frame: int, end_frame: int) -> None
```

x.set_range(start_frame, end_frame) -> None
Set range

Args:
    start_frame (int32): The desired start frame for this section
    end_frame (int32): The desired end frame for this section

<a id="unreal.MovieSceneSection.set_end_frame_seconds"></a>

#### set_end_frame_seconds

```python
def set_end_frame_seconds(end_time: float) -> None
```

x.set_end_frame_seconds(end_time) -> None
Set end time in seconds

Args:
    end_time (float): The desired end time for this section

<a id="unreal.MovieSceneSection.set_end_frame_bounded"></a>

#### set_end_frame_bounded

```python
def set_end_frame_bounded(is_bounded: bool) -> None
```

x.set_end_frame_bounded(is_bounded) -> None
Set end frame bounded

Args:
    is_bounded (bool):

<a id="unreal.MovieSceneSection.set_end_frame"></a>

#### set_end_frame

```python
def set_end_frame(end_frame: int) -> None
```

x.set_end_frame(end_frame) -> None
Set end frame

Args:
    end_frame (int32): The desired start frame for this section

<a id="unreal.MovieSceneSection.has_start_frame"></a>

#### has_start_frame

```python
def has_start_frame() -> bool
```

x.has_start_frame() -> bool
Has start frame

Returns:
    bool: Whether this section has a valid start frame (else infinite)

<a id="unreal.MovieSceneSection.has_end_frame"></a>

#### has_end_frame

```python
def has_end_frame() -> bool
```

x.has_end_frame() -> bool
Has end frame

Returns:
    bool: Whether this section has a valid end frame (else infinite)

<a id="unreal.MovieSceneSection.get_start_frame_seconds"></a>

#### get_start_frame_seconds

```python
def get_start_frame_seconds() -> float
```

x.get_start_frame_seconds() -> float
Get start time in seconds. Will throw an exception if section has no start frame, use HasStartFrame to check first.

Returns:
    float: Start time of this section

<a id="unreal.MovieSceneSection.get_start_frame"></a>

#### get_start_frame

```python
def get_start_frame() -> int
```

x.get_start_frame() -> int32
Get start frame. Will throw an exception if section has no start frame, use HasStartFrame to check first.

Returns:
    int32: Start frame of this section

<a id="unreal.MovieSceneSection.get_end_frame_seconds"></a>

#### get_end_frame_seconds

```python
def get_end_frame_seconds() -> float
```

x.get_end_frame_seconds() -> float
Get end time in seconds. Will throw an exception if section has no end frame, use HasEndFrame to check first.

Returns:
    float: End time of this section

<a id="unreal.MovieSceneSection.get_end_frame"></a>

#### get_end_frame

```python
def get_end_frame() -> int
```

x.get_end_frame() -> int32
Get end frame. Will throw an exception if section has no end frame, use HasEndFrame to check first.

Returns:
    int32: End frame of this section

<a id="unreal.MovieSceneSection.get_channels_by_type"></a>

#### get_channels_by_type

```python
def get_channels_by_type(
        channel_type: Class) -> Array[MovieSceneScriptingChannel]
```

x.get_channels_by_type(channel_type) -> Array[MovieSceneScriptingChannel]
Find all channels that belong to the specified UMovieSceneSection that match the specific type. This will filter out any children who do not inherit
from the specified type for you.

Args:
    channel_type (type(Class)): The class type to look for.

Returns:
    Array[MovieSceneScriptingChannel]: An array containing any key channels that match the type specified

<a id="unreal.MovieSceneSection.get_channel"></a>

#### get_channel

```python
def get_channel(channel_name: Name) -> MovieSceneScriptingChannel
```

x.get_channel(channel_name) -> MovieSceneScriptingChannel
Get channel from specified section and channel name

Args:
    channel_name (Name): The name of the channel.

Returns:
    MovieSceneScriptingChannel: The channel if it exists

<a id="unreal.MovieSceneSection.get_auto_size_start_frame_seconds"></a>

#### get_auto_size_start_frame_seconds

```python
def get_auto_size_start_frame_seconds() -> float
```

x.get_auto_size_start_frame_seconds() -> float
Get start time of the AutoSize in seconds. Will throw an exception if section has no start frame, use GetAutoSizeHasStartFrame to check first.

Returns:
    float: The start frame of the AutoSize data in seconds.

<a id="unreal.MovieSceneSection.get_auto_size_start_frame"></a>

#### get_auto_size_start_frame

```python
def get_auto_size_start_frame() -> int
```

x.get_auto_size_start_frame() -> int32
Get start frame of the AutoSize. Will throw an exception if section has no start frame, use GetAutoSizeHasStartFrame to check first.

Returns:
    int32: The start frame of the AutoSize data.

<a id="unreal.MovieSceneSection.get_auto_size_has_start_frame"></a>

#### get_auto_size_has_start_frame

```python
def get_auto_size_has_start_frame() -> bool
```

x.get_auto_size_has_start_frame() -> bool
Checks to see if this section has an AutoSize implementation, and if so, if that implementation has a start frame.

Returns:
    bool: Whether this section has a valid autosize range, and a valid start frame

<a id="unreal.MovieSceneSection.get_auto_size_has_end_frame"></a>

#### get_auto_size_has_end_frame

```python
def get_auto_size_has_end_frame() -> bool
```

x.get_auto_size_has_end_frame() -> bool
Checks to see if this section has an AutoSize implementation, and if so, if that implementation has a end frame.

Returns:
    bool: Whether this section has a valid autosize range, and a valid end frame

<a id="unreal.MovieSceneSection.get_auto_size_end_frame_seconds"></a>

#### get_auto_size_end_frame_seconds

```python
def get_auto_size_end_frame_seconds() -> float
```

x.get_auto_size_end_frame_seconds() -> float
Get end time of the AutoSize seconds. Will throw an exception if section has no end frame, use GetAutoSizeHasEndFrame to check first.

Returns:
    float: The end frame of the AutoSize data in seconds.

<a id="unreal.MovieSceneSection.get_auto_size_end_frame"></a>

#### get_auto_size_end_frame

```python
def get_auto_size_end_frame() -> int
```

x.get_auto_size_end_frame() -> int32
Get end frame of the AutoSize. Will throw an exception if section has no end frame, use GetAutoSizeHasEndFrame to check first.

Returns:
    int32: The end frame of the AutoSize data.

<a id="unreal.MovieSceneSection.get_all_channels"></a>

#### get_all_channels

```python
def get_all_channels() -> Array[MovieSceneScriptingChannel]
```

x.get_all_channels() -> Array[MovieSceneScriptingChannel]
Find all channels that belong to the specified UMovieSceneSection. Some sections have many channels (such as
Transforms containing 9 double channels to represent Translation/Rotation/Scale), and a section may have mixed
channel types.

Returns:
    Array[MovieSceneScriptingChannel]: An array containing any key channels that match the type specified

<a id="unreal.MovieScene2DTransformSection"></a>