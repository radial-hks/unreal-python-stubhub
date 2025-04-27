## LevelSequenceEditorBlueprintLibrary Objects

```python
class LevelSequenceEditorBlueprintLibrary(BlueprintFunctionLibrary)
```

Level Sequence Editor Blueprint Library

**C++ Source:**

- **Plugin**: LevelSequenceEditor
- **Module**: LevelSequenceEditor
- **File**: LevelSequenceEditorBlueprintLibrary.h

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_track_filter_enabled"></a>

#### set_track_filter_enabled

```python
@classmethod
def set_track_filter_enabled(cls, track_filter_name: Text,
                             enabled: bool) -> None
```

X.set_track_filter_enabled(track_filter_name, enabled) -> None
Set Track Filter Enabled

Args:
    track_filter_name (Text): 
    enabled (bool):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_track_filter_active"></a>

#### set_track_filter_active

```python
@classmethod
def set_track_filter_active(cls, track_filter_name: Text,
                            active: bool) -> None
```

X.set_track_filter_active(track_filter_name, active) -> None
Sets the specified track filter to be on or off

Args:
    track_filter_name (Text): 
    active (bool):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_selection_range_start"></a>

#### set_selection_range_start

```python
@classmethod
def set_selection_range_start(cls, new_frame: int) -> None
```

X.set_selection_range_start(new_frame) -> None
Set the selection range start frame.

Args:
    new_frame (int32):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_selection_range_end"></a>

#### set_selection_range_end

```python
@classmethod
def set_selection_range_end(cls, new_frame: int) -> None
```

X.set_selection_range_end(new_frame) -> None
Set the selection range end frame.

Args:
    new_frame (int32):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_random_color_for_channels"></a>

#### set_random_color_for_channels

```python
@classmethod
def set_random_color_for_channels(cls, class_: Class,
                                  identifiers: Array[str]) -> None
```

X.set_random_color_for_channels(class_, identifiers) -> None
Set Random Color for Channels
deprecated: Use USequencerCurveEditorObject::SetRandomColorForChannels

Args:
    class_ (type(Class)): 
    identifiers (Array[str]):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_playback_speed"></a>

#### set_playback_speed

```python
@classmethod
def set_playback_speed(cls, new_playback_speed: float) -> None
```

X.set_playback_speed(new_playback_speed) -> None
Set playback speed of the current level sequence

Args:
    new_playback_speed (float):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_loop_mode"></a>

#### set_loop_mode

```python
@classmethod
def set_loop_mode(cls, new_loop_mode: SequencerLoopMode) -> None
```

X.set_loop_mode(new_loop_mode) -> None
Set loop mode (note this is a per user preference)

Args:
    new_loop_mode (SequencerLoopMode):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_lock_level_sequence"></a>

#### set_lock_level_sequence

```python
@classmethod
def set_lock_level_sequence(cls, lock: bool) -> None
```

X.set_lock_level_sequence(lock) -> None
Sets the lock for the current level sequence and its descendants for editing.

Args:
    lock (bool):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_lock_camera_cut_to_viewport"></a>

#### set_lock_camera_cut_to_viewport

```python
@classmethod
def set_lock_camera_cut_to_viewport(cls, lock: bool) -> None
```

X.set_lock_camera_cut_to_viewport(lock) -> None
Sets the lock for the viewport to the camera cuts.

Args:
    lock (bool):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_local_position"></a>

#### set_local_position

```python
@classmethod
def set_local_position(
        cls,
        playback_params: MovieSceneSequencePlaybackParams,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_position(playback_params, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set local playhead position for the current level sequence. If the requested time is the same as the current time, an evaluation will be forced.

Args:
    playback_params (MovieSceneSequencePlaybackParams): 
    time_unit (MovieSceneTimeUnit):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_global_position"></a>

#### set_global_position

```python
@classmethod
def set_global_position(
        cls,
        playback_params: MovieSceneSequencePlaybackParams,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_global_position(playback_params, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set global playhead position for the current level sequence. If the requested time is the same as the current time, an evaluation will be forced.

Args:
    playback_params (MovieSceneSequencePlaybackParams): 
    time_unit (MovieSceneTimeUnit):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_custom_color_for_channels"></a>

#### set_custom_color_for_channels

```python
@classmethod
def set_custom_color_for_channels(cls, class_: Class, identifiers: Array[str],
                                  new_colors: Array[LinearColor]) -> None
```

X.set_custom_color_for_channels(class_, identifiers, new_colors) -> None
Set Custom Color for Channels
deprecated: Use USequencerCurveEditorObject::DeleteColorForChannels

Args:
    class_ (type(Class)): 
    identifiers (Array[str]): 
    new_colors (Array[LinearColor]):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_custom_color_for_channel"></a>

#### set_custom_color_for_channel

```python
@classmethod
def set_custom_color_for_channel(cls, class_: Class, identifier: str,
                                 new_color: LinearColor) -> None
```

X.set_custom_color_for_channel(class_, identifier, new_color) -> None
Set Custom Color for Channel
deprecated: Use USequencerCurveEditorObject::SetCustomColorForChannel

Args:
    class_ (type(Class)): 
    identifier (str): 
    new_color (LinearColor):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_current_time"></a>

#### set_current_time

```python
@classmethod
def set_current_time(cls, new_frame: int) -> None
```

X.set_current_time(new_frame) -> None
Set Current Time
deprecated: Use SetCurrentTime that takes a FMovieSceneSequencePlaybackParams

Args:
    new_frame (int32):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.set_current_local_time"></a>

#### set_current_local_time

```python
@classmethod
def set_current_local_time(cls, new_frame: int) -> None
```

X.set_current_local_time(new_frame) -> None
Set Current Local Time
deprecated: Use SetCurrentLocalTime that takes a FMovieSceneSequencePlaybackParams

Args:
    new_frame (int32):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.select_tracks"></a>

#### select_tracks

```python
@classmethod
def select_tracks(cls, tracks: Array[MovieSceneTrack]) -> None
```

X.select_tracks(tracks) -> None
Select tracks

Args:
    tracks (Array[MovieSceneTrack]):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.select_sections"></a>

#### select_sections

```python
@classmethod
def select_sections(cls, sections: Array[MovieSceneSection]) -> None
```

X.select_sections(sections) -> None
Select sections

Args:
    sections (Array[MovieSceneSection]):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.select_keys"></a>

#### select_keys

```python
@classmethod
def select_keys(cls, channel: SequencerChannelProxy,
                indices: Array[int]) -> None
```

X.select_keys(channel, indices) -> None
Select keys from indices

Args:
    channel (SequencerChannelProxy): 
    indices (Array[int32]):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.select_folders"></a>

#### select_folders

```python
@classmethod
def select_folders(cls, folders: Array[MovieSceneFolder]) -> None
```

X.select_folders(folders) -> None
Select folders

Args:
    folders (Array[MovieSceneFolder]):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.select_channels"></a>

#### select_channels

```python
@classmethod
def select_channels(cls, channels: Array[SequencerChannelProxy]) -> None
```

X.select_channels(channels) -> None
Select channels

Args:
    channels (Array[SequencerChannelProxy]):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.select_bindings"></a>

#### select_bindings

```python
@classmethod
def select_bindings(cls,
                    object_bindings: Array[MovieSceneBindingProxy]) -> None
```

X.select_bindings(object_bindings) -> None
Select bindings

Args:
    object_bindings (Array[MovieSceneBindingProxy]):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.refresh_current_level_sequence"></a>

#### refresh_current_level_sequence

```python
@classmethod
def refresh_current_level_sequence(cls) -> None
```

X.refresh_current_level_sequence() -> None
Refresh Sequencer UI on next tick

<a id="unreal.LevelSequenceEditorBlueprintLibrary.play_to"></a>

#### play_to

```python
@classmethod
def play_to(
        cls,
        playback_params: MovieSceneSequencePlaybackParams,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.play_to(playback_params, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Play from the current time to the requested time in frames

Args:
    playback_params (MovieSceneSequencePlaybackParams): 
    time_unit (MovieSceneTimeUnit):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.play"></a>

#### play

```python
@classmethod
def play(cls) -> None
```

X.play() -> None
Play the current level sequence

<a id="unreal.LevelSequenceEditorBlueprintLibrary.pause"></a>

#### pause

```python
@classmethod
def pause(cls) -> None
```

X.pause() -> None
Pause the current level sequence

<a id="unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence"></a>

#### open_level_sequence

```python
@classmethod
def open_level_sequence(cls, level_sequence: LevelSequence) -> bool
```

X.open_level_sequence(level_sequence) -> bool
* Open a level sequence asset

Args:
    level_sequence (LevelSequence): 

Returns:
    bool:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.is_track_filter_enabled"></a>

#### is_track_filter_enabled

```python
@classmethod
def is_track_filter_enabled(cls, track_filter_name: Text) -> bool
```

X.is_track_filter_enabled(track_filter_name) -> bool
Is Track Filter Enabled

Args:
    track_filter_name (Text): 

Returns:
    bool:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.is_track_filter_active"></a>

#### is_track_filter_active

```python
@classmethod
def is_track_filter_active(cls, track_filter_name: Text) -> bool
```

X.is_track_filter_active(track_filter_name) -> bool
Gets whether the specified track filter is on/off

Args:
    track_filter_name (Text): 

Returns:
    bool:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.is_playing"></a>

#### is_playing

```python
@classmethod
def is_playing(cls) -> bool
```

X.is_playing() -> bool
Check whether the sequence is actively playing.

Returns:
    bool:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.is_level_sequence_locked"></a>

#### is_level_sequence_locked

```python
@classmethod
def is_level_sequence_locked(cls) -> bool
```

X.is_level_sequence_locked() -> bool
Check whether the current level sequence and its descendants are locked for editing.

Returns:
    bool:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.is_camera_cut_locked_to_viewport"></a>

#### is_camera_cut_locked_to_viewport

```python
@classmethod
def is_camera_cut_locked_to_viewport(cls) -> bool
```

X.is_camera_cut_locked_to_viewport() -> bool
Check whether the lock for the viewport to the camera cuts is enabled.

Returns:
    bool:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.has_custom_color_for_channel"></a>

#### has_custom_color_for_channel

```python
@classmethod
def has_custom_color_for_channel(cls, class_: Class, identifier: str) -> bool
```

X.has_custom_color_for_channel(class_, identifier) -> bool
Has Custom Color for Channel
deprecated: Use USequencerCurveEditorObject::HasCustomColorForChannel

Args:
    class_ (type(Class)): 
    identifier (str): 

Returns:
    bool:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_track_filter_names"></a>

#### get_track_filter_names

```python
@classmethod
def get_track_filter_names(cls) -> Array[Text]
```

X.get_track_filter_names() -> Array[Text]
Gets all the available track filter names

Returns:
    Array[Text]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_sub_sequence_hierarchy"></a>

#### get_sub_sequence_hierarchy

```python
@classmethod
def get_sub_sequence_hierarchy(cls) -> Array[MovieSceneSubSection]
```

X.get_sub_sequence_hierarchy() -> Array[MovieSceneSubSection]
* Get the current sub section hierarchy from the current sequence to the section associated with the focused sequence.

Returns:
    Array[MovieSceneSubSection]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_selection_range_start"></a>

#### get_selection_range_start

```python
@classmethod
def get_selection_range_start(cls) -> int
```

X.get_selection_range_start() -> int32
Get the selection range start frame.

Returns:
    int32:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_selection_range_end"></a>

#### get_selection_range_end

```python
@classmethod
def get_selection_range_end(cls) -> int
```

X.get_selection_range_end() -> int32
Get the selection range end frame.

Returns:
    int32:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_selected_tracks"></a>

#### get_selected_tracks

```python
@classmethod
def get_selected_tracks(cls) -> Array[MovieSceneTrack]
```

X.get_selected_tracks() -> Array[MovieSceneTrack]
Gets the currently selected tracks.

Returns:
    Array[MovieSceneTrack]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_selected_sections"></a>

#### get_selected_sections

```python
@classmethod
def get_selected_sections(cls) -> Array[MovieSceneSection]
```

X.get_selected_sections() -> Array[MovieSceneSection]
Gets the currently selected sections.

Returns:
    Array[MovieSceneSection]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_selected_keys"></a>

#### get_selected_keys

```python
@classmethod
def get_selected_keys(cls, channel_proxy: SequencerChannelProxy) -> Array[int]
```

X.get_selected_keys(channel_proxy) -> Array[int32]
Gets the selected key indices with this channel

Args:
    channel_proxy (SequencerChannelProxy): 

Returns:
    Array[int32]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_selected_folders"></a>

#### get_selected_folders

```python
@classmethod
def get_selected_folders(cls) -> Array[MovieSceneFolder]
```

X.get_selected_folders() -> Array[MovieSceneFolder]
Gets the currently selected folders.

Returns:
    Array[MovieSceneFolder]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_selected_channels"></a>

#### get_selected_channels

```python
@classmethod
def get_selected_channels(cls) -> Array[SequencerChannelProxy]
```

X.get_selected_channels() -> Array[SequencerChannelProxy]
Gets the currently selected channels.

Returns:
    Array[SequencerChannelProxy]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_selected_bindings"></a>

#### get_selected_bindings

```python
@classmethod
def get_selected_bindings(cls) -> Array[MovieSceneBindingProxy]
```

X.get_selected_bindings() -> Array[MovieSceneBindingProxy]
Gets the currently selected object bindings

Returns:
    Array[MovieSceneBindingProxy]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_playback_speed"></a>

#### get_playback_speed

```python
@classmethod
def get_playback_speed(cls) -> float
```

X.get_playback_speed() -> float
Get playback speed of the current level sequence

Returns:
    float:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_loop_mode"></a>

#### get_loop_mode

```python
@classmethod
def get_loop_mode(cls) -> SequencerLoopMode
```

X.get_loop_mode() -> SequencerLoopMode
Get loop mode (note this is a per user preference)

Returns:
    SequencerLoopMode:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_local_position"></a>

#### get_local_position

```python
@classmethod
def get_local_position(
    cls,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> MovieSceneSequencePlaybackParams
```

X.get_local_position(time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneSequencePlaybackParams
Get the current local playhead position

Args:
    time_unit (MovieSceneTimeUnit): 

Returns:
    MovieSceneSequencePlaybackParams:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_global_position"></a>

#### get_global_position

```python
@classmethod
def get_global_position(
    cls,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> MovieSceneSequencePlaybackParams
```

X.get_global_position(time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneSequencePlaybackParams
Get the current global playhead position

Args:
    time_unit (MovieSceneTimeUnit): 

Returns:
    MovieSceneSequencePlaybackParams:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_focused_level_sequence"></a>

#### get_focused_level_sequence

```python
@classmethod
def get_focused_level_sequence(cls) -> LevelSequence
```

X.get_focused_level_sequence() -> LevelSequence
* Get the currently focused/viewed level sequence asset if there is a hierarchy of sequences.

Returns:
    LevelSequence:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_custom_color_for_channel"></a>

#### get_custom_color_for_channel

```python
@classmethod
def get_custom_color_for_channel(cls, class_: Class,
                                 identifier: str) -> LinearColor
```

X.get_custom_color_for_channel(class_, identifier) -> LinearColor
Get Custom Color for Channel
deprecated: Use USequencerCurveEditorObject::HasCustomColorForChannel

Args:
    class_ (type(Class)): 
    identifier (str): 

Returns:
    LinearColor:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_current_time"></a>

#### get_current_time

```python
@classmethod
def get_current_time(cls) -> int
```

X.get_current_time() -> int32
Get Current Time
deprecated: Use GetCurrentTime that returns a FMovieSceneSequencePlaybackParams

Returns:
    int32:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_current_local_time"></a>

#### get_current_local_time

```python
@classmethod
def get_current_local_time(cls) -> int
```

X.get_current_local_time() -> int32
Get Current Local Time
deprecated: Use GetCurrentLocalTime that returns a FMovieSceneSequencePlaybackParams

Returns:
    int32:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_current_level_sequence"></a>

#### get_current_level_sequence

```python
@classmethod
def get_current_level_sequence(cls) -> LevelSequence
```

X.get_current_level_sequence() -> LevelSequence
* Get the currently opened root level sequence asset

Returns:
    LevelSequence:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_channels_with_selected_keys"></a>

#### get_channels_with_selected_keys

```python
@classmethod
def get_channels_with_selected_keys(cls) -> Array[SequencerChannelProxy]
```

X.get_channels_with_selected_keys() -> Array[SequencerChannelProxy]
Gets the channel with selected keys.

Returns:
    Array[SequencerChannelProxy]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.get_bound_objects"></a>

#### get_bound_objects

```python
@classmethod
def get_bound_objects(
        cls, object_binding: MovieSceneObjectBindingID) -> Array[Object]
```

X.get_bound_objects(object_binding) -> Array[Object]
Get the object bound to the given binding ID with the current level sequence editor

Args:
    object_binding (MovieSceneObjectBindingID): 

Returns:
    Array[Object]:

<a id="unreal.LevelSequenceEditorBlueprintLibrary.force_update"></a>

#### force_update

```python
@classmethod
def force_update(cls) -> None
```

X.force_update() -> None
Force sequencer evaluation and UI update immediately

<a id="unreal.LevelSequenceEditorBlueprintLibrary.focus_parent_sequence"></a>

#### focus_parent_sequence

```python
@classmethod
def focus_parent_sequence(cls) -> None
```

X.focus_parent_sequence() -> None
* Focus/view the parent sequence, popping out of the current sub sequence section.

<a id="unreal.LevelSequenceEditorBlueprintLibrary.focus_level_sequence"></a>

#### focus_level_sequence

```python
@classmethod
def focus_level_sequence(cls, sub_section: MovieSceneSubSection) -> None
```

X.focus_level_sequence(sub_section) -> None
* Focus/view the sequence associated to the given sub sequence section.

Args:
    sub_section (MovieSceneSubSection):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.empty_selection"></a>

#### empty_selection

```python
@classmethod
def empty_selection(cls) -> None
```

X.empty_selection() -> None
Empties the current selection.

<a id="unreal.LevelSequenceEditorBlueprintLibrary.delete_color_for_channels"></a>

#### delete_color_for_channels

```python
@classmethod
def delete_color_for_channels(cls, class_: Class) -> str
```

X.delete_color_for_channels(class_) -> str
Delete Color for Channels
deprecated: Use USequencerCurveEditorObject::DeleteColorForChannels

Args:
    class_ (type(Class)): 

Returns:
    str: 

    identifier (str):

<a id="unreal.LevelSequenceEditorBlueprintLibrary.close_level_sequence"></a>

#### close_level_sequence

```python
@classmethod
def close_level_sequence(cls) -> None
```

X.close_level_sequence() -> None
* Close

<a id="unreal.LevelSequenceEditorSubsystem"></a>