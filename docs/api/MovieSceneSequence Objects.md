## MovieSceneSequence Objects

```python
class MovieSceneSequence(MovieSceneSignedObject)
```

Abstract base class for movie scene animations (C++ version).

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSequence.h

<a id="unreal.MovieSceneSequence.get_earliest_timecode_source"></a>

#### get_earliest_timecode_source

```python
def get_earliest_timecode_source() -> MovieSceneTimecodeSource
```

x.get_earliest_timecode_source() -> MovieSceneTimecodeSource
Get the earliest timecode source out of all of the movie scene sections contained within this sequence's movie scene.

Returns:
    MovieSceneTimecodeSource:

<a id="unreal.MovieSceneSequence.find_bindings_by_tag"></a>

#### find_bindings_by_tag

```python
def find_bindings_by_tag(
        binding_name: Name) -> Array[MovieSceneObjectBindingID]
```

x.find_bindings_by_tag(binding_name) -> Array[MovieSceneObjectBindingID]
Find all object binding IDs associated with the specified tag name (set up through RMB->Expose on Object bindings from within sequencer)

Args:
    binding_name (Name): 

Returns:
    Array[MovieSceneObjectBindingID]:

<a id="unreal.MovieSceneSequence.find_binding_by_tag"></a>

#### find_binding_by_tag

```python
def find_binding_by_tag(binding_name: Name) -> MovieSceneObjectBindingID
```

x.find_binding_by_tag(binding_name) -> MovieSceneObjectBindingID
Find the first object binding ID associated with the specified tag name (set up through RMB->Expose on Object bindings from within sequencer)

Args:
    binding_name (Name): 

Returns:
    MovieSceneObjectBindingID:

<a id="unreal.MovieSceneSequence.sort_marked_frames"></a>

#### sort_marked_frames

```python
def sort_marked_frames() -> None
```

x.sort_marked_frames() -> None
* Sort the marked frames in chronological order

<a id="unreal.MovieSceneSequence.set_work_range_start"></a>

#### set_work_range_start

```python
def set_work_range_start(start_time_in_seconds: float) -> None
```

x.set_work_range_start(start_time_in_seconds) -> None
Set the sequence work range start in seconds

Args:
    start_time_in_seconds (double): The desired work range start time in seconds for this sequence

<a id="unreal.MovieSceneSequence.set_work_range_end"></a>

#### set_work_range_end

```python
def set_work_range_end(end_time_in_seconds: float) -> None
```

x.set_work_range_end(end_time_in_seconds) -> None
Set the sequence work range end in seconds

Args:
    end_time_in_seconds (double):

<a id="unreal.MovieSceneSequence.set_view_range_start"></a>

#### set_view_range_start

```python
def set_view_range_start(start_time_in_seconds: float) -> None
```

x.set_view_range_start(start_time_in_seconds) -> None
Set the sequence view range start in seconds

Args:
    start_time_in_seconds (double): The desired view range start time in seconds for this sequence

<a id="unreal.MovieSceneSequence.set_view_range_end"></a>

#### set_view_range_end

```python
def set_view_range_end(end_time_in_seconds: float) -> None
```

x.set_view_range_end(end_time_in_seconds) -> None
Set the sequence view range end in seconds

Args:
    end_time_in_seconds (double):

<a id="unreal.MovieSceneSequence.set_tick_resolution_directly"></a>

#### set_tick_resolution_directly

```python
def set_tick_resolution_directly(tick_resolution: FrameRate) -> None
```

x.set_tick_resolution_directly(tick_resolution) -> None
Sets this sequence's tick resolution directly without migrating frame times

Args:
    tick_resolution (FrameRate): The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

<a id="unreal.MovieSceneSequence.set_tick_resolution"></a>

#### set_tick_resolution

```python
def set_tick_resolution(tick_resolution: FrameRate) -> None
```

x.set_tick_resolution(tick_resolution) -> None
Sets this sequence's tick resolution and migrates frame times

Args:
    tick_resolution (FrameRate): The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

<a id="unreal.MovieSceneSequence.set_read_only"></a>

#### set_read_only

```python
def set_read_only(read_only: bool) -> None
```

x.set_read_only(read_only) -> None
* Set read only
*
*
bInReadOnly: Whether the movie scene should be read only or not

Args:
    read_only (bool):

<a id="unreal.MovieSceneSequence.set_playback_start_seconds"></a>

#### set_playback_start_seconds

```python
def set_playback_start_seconds(start_time: float) -> None
```

x.set_playback_start_seconds(start_time) -> None
Set playback start of this sequence in seconds

Args:
    start_time (float): The desired start time in seconds for this sequence

<a id="unreal.MovieSceneSequence.set_playback_start"></a>

#### set_playback_start

```python
def set_playback_start(start_frame: int) -> None
```

x.set_playback_start(start_frame) -> None
Set playback start of this sequence

Args:
    start_frame (int32): The desired start frame for this sequence

<a id="unreal.MovieSceneSequence.set_playback_range_locked"></a>

#### set_playback_range_locked

```python
def set_playback_range_locked(locked: bool) -> None
```

x.set_playback_range_locked(locked) -> None
* Set playback range locked
*
*
bInLocked: Whether the movie scene playback range should be locked

Args:
    locked (bool):

<a id="unreal.MovieSceneSequence.set_playback_end_seconds"></a>

#### set_playback_end_seconds

```python
def set_playback_end_seconds(end_time: float) -> None
```

x.set_playback_end_seconds(end_time) -> None
Set playback end of this sequence in seconds

Args:
    end_time (float): The desired end time in seconds for this sequence

<a id="unreal.MovieSceneSequence.set_playback_end"></a>

#### set_playback_end

```python
def set_playback_end(end_frame: int) -> None
```

x.set_playback_end(end_frame) -> None
Set playback end of this sequence

Args:
    end_frame (int32): The desired end frame for this sequence

<a id="unreal.MovieSceneSequence.set_marked_frames_locked"></a>

#### set_marked_frames_locked

```python
def set_marked_frames_locked(locked: bool) -> None
```

x.set_marked_frames_locked(locked) -> None
* Set marked frames locked
*
*
bInLocked: Whether the movie scene marked frames should be locked

Args:
    locked (bool):

<a id="unreal.MovieSceneSequence.set_marked_frame_in_sequence"></a>

#### set_marked_frame_in_sequence

```python
def set_marked_frame_in_sequence(
        mark_index: int,
        frame_number: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

x.set_marked_frame_in_sequence(mark_index, frame_number, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
* Sets the frame number for the given marked frame index. Does not maintain sort. Call SortMarkedFrames
*
*
InMarkIndex: The given user marked frame index to edit *
InFrameNumber: The frame number to set

Args:
    mark_index (int32): 
    frame_number (FrameNumber): 
    time_unit (MovieSceneTimeUnit):

<a id="unreal.MovieSceneSequence.set_marked_frame"></a>

#### set_marked_frame

```python
def set_marked_frame(mark_index: int, frame_number: FrameNumber) -> None
```

x.set_marked_frame(mark_index, frame_number) -> None
Set Marked Frame
deprecated: SetMarkedFrame is deprecated. Please use SetMarkedFrame that takes a time unit instead

Args:
    mark_index (int32): 
    frame_number (FrameNumber):

<a id="unreal.MovieSceneSequence.set_evaluation_type"></a>

#### set_evaluation_type

```python
def set_evaluation_type(evaluation_type: MovieSceneEvaluationType) -> None
```

x.set_evaluation_type(evaluation_type) -> None
Set the evaluation type for this sequence

Args:
    evaluation_type (MovieSceneEvaluationType): The evaluation type to set for this sequence

<a id="unreal.MovieSceneSequence.set_display_rate"></a>

#### set_display_rate

```python
def set_display_rate(display_rate: FrameRate) -> None
```

x.set_display_rate(display_rate) -> None
Sets this sequence's display rate

Args:
    display_rate (FrameRate): The display rate that this sequence is displayed as

<a id="unreal.MovieSceneSequence.set_clock_source"></a>

#### set_clock_source

```python
def set_clock_source(clock_source: UpdateClockSource) -> None
```

x.set_clock_source(clock_source) -> None
Set the clock source for this sequence

Args:
    clock_source (UpdateClockSource): The clock source to set for this sequence

<a id="unreal.MovieSceneSequence.resolve_binding_id"></a>

#### resolve_binding_id

```python
def resolve_binding_id(
        object_binding_id: MovieSceneObjectBindingID
) -> MovieSceneBindingProxy
```

x.resolve_binding_id(object_binding_id) -> MovieSceneBindingProxy
Make a binding for the given binding ID

Args:
    object_binding_id (MovieSceneObjectBindingID): 

Returns:
    MovieSceneBindingProxy: The new binding proxy

<a id="unreal.MovieSceneSequence.remove_track"></a>

#### remove_track

```python
def remove_track(track: MovieSceneTrack) -> bool
```

x.remove_track(track) -> bool
Removes a track

Args:
    track (MovieSceneTrack): The track to remove

Returns:
    bool: Whether the track was successfully removed

<a id="unreal.MovieSceneSequence.remove_root_folder_from_sequence"></a>

#### remove_root_folder_from_sequence

```python
def remove_root_folder_from_sequence(folder: MovieSceneFolder) -> None
```

x.remove_root_folder_from_sequence(folder) -> None
Remove a root folder from the given sequence. Will throw an exception if the specified folder is not valid or not a root folder.

Args:
    folder (MovieSceneFolder): The folder to remove

<a id="unreal.MovieSceneSequence.make_range_seconds"></a>

#### make_range_seconds

```python
def make_range_seconds(start_time: float,
                       duration: float) -> SequencerScriptingRange
```

x.make_range_seconds(start_time, duration) -> SequencerScriptingRange
Make a new range for this sequence in seconds

Args:
    start_time (float): The time in seconds at which to start the range
    duration (float): The length of the range in seconds

Returns:
    SequencerScriptingRange: Specified sequencer range

<a id="unreal.MovieSceneSequence.make_range"></a>

#### make_range

```python
def make_range(start_frame: int, duration: int) -> SequencerScriptingRange
```

x.make_range(start_frame, duration) -> SequencerScriptingRange
Make a new range for this sequence in its display rate

Args:
    start_frame (int32): The frame at which to start the range
    duration (int32): The length of the range

Returns:
    SequencerScriptingRange: Specified sequencer range

<a id="unreal.MovieSceneSequence.locate_bound_objects"></a>

#### locate_bound_objects

```python
def locate_bound_objects(binding: MovieSceneBindingProxy,
                         context: Object) -> Array[Object]
```

x.locate_bound_objects(binding, context) -> Array[Object]
Locate all the objects that correspond to the specified object ID, using the specified context

Args:
    binding (MovieSceneBindingProxy): The object binding
    context (Object): Optional context to use to find the required object

Returns:
    Array[Object]: An array of all bound objects

<a id="unreal.MovieSceneSequence.is_read_only"></a>

#### is_read_only

```python
def is_read_only() -> bool
```

x.is_read_only() -> bool
* Is read only
*
*

Returns:
    bool: Whether the movie scene is read only or not

<a id="unreal.MovieSceneSequence.is_playback_range_locked"></a>

#### is_playback_range_locked

```python
def is_playback_range_locked() -> bool
```

x.is_playback_range_locked() -> bool
* Is playback ranged locked
*
*

Returns:
    bool: Whether the movie scene playback range is locked

<a id="unreal.MovieSceneSequence.get_work_range_start"></a>

#### get_work_range_start

```python
def get_work_range_start() -> float
```

x.get_work_range_start() -> double
Get the sequence work range start in seconds

Returns:
    double: The work range start time in seconds for this sequence

<a id="unreal.MovieSceneSequence.get_work_range_end"></a>

#### get_work_range_end

```python
def get_work_range_end() -> float
```

x.get_work_range_end() -> double
Get the sequence work range end in seconds

Returns:
    double: The work range end time in seconds for this sequence

<a id="unreal.MovieSceneSequence.get_view_range_start"></a>

#### get_view_range_start

```python
def get_view_range_start() -> float
```

x.get_view_range_start() -> double
Get the sequence view range start in seconds

Returns:
    double: The view range start time in seconds for this sequence

<a id="unreal.MovieSceneSequence.get_view_range_end"></a>

#### get_view_range_end

```python
def get_view_range_end() -> float
```

x.get_view_range_end() -> double
Get the sequence view range end in seconds

Returns:
    double: The view range end time in seconds for this sequence

<a id="unreal.MovieSceneSequence.get_tracks"></a>

#### get_tracks

```python
def get_tracks() -> Array[MovieSceneTrack]
```

x.get_tracks() -> Array[MovieSceneTrack]
Get all tracks

Returns:
    Array[MovieSceneTrack]: An array containing all tracks in this sequence

<a id="unreal.MovieSceneSequence.get_tick_resolution"></a>

#### get_tick_resolution

```python
def get_tick_resolution() -> FrameRate
```

x.get_tick_resolution() -> FrameRate
Gets this sequence's tick resolution

Returns:
    FrameRate: The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

<a id="unreal.MovieSceneSequence.get_spawnables"></a>

#### get_spawnables

```python
def get_spawnables() -> Array[MovieSceneBindingProxy]
```

x.get_spawnables() -> Array[MovieSceneBindingProxy]
Get all the spawnables in this sequence. For Level Sequences, this includes bindings with binding type UMovieSceneSpawnableActorBinding.

Returns:
    Array[MovieSceneBindingProxy]: Spawnables in this sequence

<a id="unreal.MovieSceneSequence.get_root_folders_in_sequence"></a>

#### get_root_folders_in_sequence

```python
def get_root_folders_in_sequence() -> Array[MovieSceneFolder]
```

x.get_root_folders_in_sequence() -> Array[MovieSceneFolder]
Get the root folders in the provided sequence

Returns:
    Array[MovieSceneFolder]: The folders contained within the given sequence

<a id="unreal.MovieSceneSequence.get_possessables"></a>

#### get_possessables

```python
def get_possessables() -> Array[MovieSceneBindingProxy]
```

x.get_possessables() -> Array[MovieSceneBindingProxy]
Get all the possessables in this sequence. It is understood for the purpose of this function that this means the bindings are not custom.

Returns:
    Array[MovieSceneBindingProxy]: Possessables in this sequence

<a id="unreal.MovieSceneSequence.get_portable_binding_id"></a>

#### get_portable_binding_id

```python
def get_portable_binding_id(
        destination_sequence: MovieSceneSequence,
        binding: MovieSceneBindingProxy) -> MovieSceneObjectBindingID
```

x.get_portable_binding_id(destination_sequence, binding) -> MovieSceneObjectBindingID
Get a portable binding ID for a binding that resides in a different sequence to the one where this binding will be resolved.
note:: This function must be used over GetBindingID when the target binding resides in different shots or sub-sequences.
note:: Only unique instances of sequences within a root sequences are supported

Args:
    destination_sequence (MovieSceneSequence): The sequence that will own or resolve the resulting binding ID. For example, if the binding ID will be applied to a camera cut section pass the sequence that contains the camera cut track to this parameter.
    binding (MovieSceneBindingProxy): 

Returns:
    MovieSceneObjectBindingID: The binding's id

<a id="unreal.MovieSceneSequence.get_playback_start_seconds"></a>

#### get_playback_start_seconds

```python
def get_playback_start_seconds() -> float
```

x.get_playback_start_seconds() -> float
Get playback start of this sequence in seconds

Returns:
    float: Playback start of this sequence

<a id="unreal.MovieSceneSequence.get_playback_start"></a>

#### get_playback_start

```python
def get_playback_start() -> int
```

x.get_playback_start() -> int32
Get playback start of this sequence in display rate resolution

Returns:
    int32: Playback start of this sequence

<a id="unreal.MovieSceneSequence.get_playback_range"></a>

#### get_playback_range

```python
def get_playback_range() -> SequencerScriptingRange
```

x.get_playback_range() -> SequencerScriptingRange
Get playback range of this sequence in display rate resolution

Returns:
    SequencerScriptingRange: Playback range of this sequence

<a id="unreal.MovieSceneSequence.get_playback_end_seconds"></a>

#### get_playback_end_seconds

```python
def get_playback_end_seconds() -> float
```

x.get_playback_end_seconds() -> float
Get playback end of this sequence in seconds

Returns:
    float: Playback end of this sequence

<a id="unreal.MovieSceneSequence.get_playback_end"></a>

#### get_playback_end

```python
def get_playback_end() -> int
```

x.get_playback_end() -> int32
Get playback end of this sequence in display rate resolution

Returns:
    int32: Playback end of this sequence

<a id="unreal.MovieSceneSequence.get_movie_scene"></a>

#### get_movie_scene

```python
def get_movie_scene() -> MovieScene
```

x.get_movie_scene() -> MovieScene
Get this sequence's movie scene data

Returns:
    MovieScene: This sequence's movie scene data object

<a id="unreal.MovieSceneSequence.get_marked_frames_from_sequence"></a>

#### get_marked_frames_from_sequence

```python
def get_marked_frames_from_sequence(
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[MovieSceneMarkedFrame]
```

x.get_marked_frames_from_sequence(time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[MovieSceneMarkedFrame]
* Get the marked frames for this sequence
*
*

Args:
    time_unit (MovieSceneTimeUnit): 

Returns:
    Array[MovieSceneMarkedFrame]: Return the user marked frames

<a id="unreal.MovieSceneSequence.get_marked_frames"></a>

#### get_marked_frames

```python
def get_marked_frames() -> Array[MovieSceneMarkedFrame]
```

x.get_marked_frames() -> Array[MovieSceneMarkedFrame]
Get Marked Frames
deprecated: GetMarkedFrames is deprecated. Please use GetMarkedFrames that takes a time unit instead

Returns:
    Array[MovieSceneMarkedFrame]:

<a id="unreal.MovieSceneSequence.get_evaluation_type"></a>

#### get_evaluation_type

```python
def get_evaluation_type() -> MovieSceneEvaluationType
```

x.get_evaluation_type() -> MovieSceneEvaluationType
Get the evaluation type for this sequence

Returns:
    MovieSceneEvaluationType: The evaluation type for this sequence

<a id="unreal.MovieSceneSequence.get_display_rate"></a>

#### get_display_rate

```python
def get_display_rate() -> FrameRate
```

x.get_display_rate() -> FrameRate
Gets this sequence's display rate

Returns:
    FrameRate: The display rate that this sequence is displayed as

<a id="unreal.MovieSceneSequence.get_clock_source"></a>

#### get_clock_source

```python
def get_clock_source() -> UpdateClockSource
```

x.get_clock_source() -> UpdateClockSource
Get the clock source for this sequence

Returns:
    UpdateClockSource: The clock source for this sequence

<a id="unreal.MovieSceneSequence.get_bindings"></a>

#### get_bindings

```python
def get_bindings() -> Array[MovieSceneBindingProxy]
```

x.get_bindings() -> Array[MovieSceneBindingProxy]
Get all the bindings in this sequence

Returns:
    Array[MovieSceneBindingProxy]: An array of unique identifiers for all the bindings in this sequence

<a id="unreal.MovieSceneSequence.get_binding_id"></a>

#### get_binding_id

```python
def get_binding_id(
        binding: MovieSceneBindingProxy) -> MovieSceneObjectBindingID
```

x.get_binding_id(binding) -> MovieSceneObjectBindingID
Get the binding ID for a binding within a sequence.
note:: The resulting binding is only valid when applied to properties within the same sequence as this binding. Use GetPortableBindingID for bindings which live in different sub-sequences.

Args:
    binding (MovieSceneBindingProxy): 

Returns:
    MovieSceneObjectBindingID: The binding's id

<a id="unreal.MovieSceneSequence.find_tracks_by_type"></a>

#### find_tracks_by_type

```python
def find_tracks_by_type(track_type: Class) -> Array[MovieSceneTrack]
```

x.find_tracks_by_type(track_type) -> Array[MovieSceneTrack]
Find all tracks of the specified type

Args:
    track_type (type(Class)): A UMovieSceneTrack class type specifying which types of track to return

Returns:
    Array[MovieSceneTrack]: An array containing any tracks that match the type specified

<a id="unreal.MovieSceneSequence.find_tracks_by_exact_type"></a>

#### find_tracks_by_exact_type

```python
def find_tracks_by_exact_type(track_type: Class) -> Array[MovieSceneTrack]
```

x.find_tracks_by_exact_type(track_type) -> Array[MovieSceneTrack]
Find all tracks of the specified type, not allowing sub-classed types

Args:
    track_type (type(Class)): A UMovieSceneTrack class type specifying the exact types of track to return

Returns:
    Array[MovieSceneTrack]: An array containing any tracks that are exactly the same as the type specified

<a id="unreal.MovieSceneSequence.find_next_marked_frame_in_sequence"></a>

#### find_next_marked_frame_in_sequence

```python
def find_next_marked_frame_in_sequence(
        frame_number: FrameNumber,
        forward: bool,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> int
```

x.find_next_marked_frame_in_sequence(frame_number, forward, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> int32
* Find the next/previous user marked frame from the given frame number
*
*
InFrameNumber: The frame number to find the next/previous user marked frame from *
bForward: Find forward from the given frame number.

Args:
    frame_number (FrameNumber): 
    forward (bool): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    int32:

<a id="unreal.MovieSceneSequence.find_next_marked_frame"></a>

#### find_next_marked_frame

```python
def find_next_marked_frame(frame_number: FrameNumber, forward: bool) -> int
```

x.find_next_marked_frame(frame_number, forward) -> int32
Find Next Marked Frame
deprecated: FindNextMarkedFrame is deprecated. Please use FindNextMarkedFrame that takes a time unit and defaults to display rate instead

Args:
    frame_number (FrameNumber): 
    forward (bool): 

Returns:
    int32:

<a id="unreal.MovieSceneSequence.find_marked_frame_by_label"></a>

#### find_marked_frame_by_label

```python
def find_marked_frame_by_label(label: str) -> int
```

x.find_marked_frame_by_label(label) -> int32
* Find the user marked frame by label
*
*
InLabel: The label to the user marked frame to find

Args:
    label (str): 

Returns:
    int32:

<a id="unreal.MovieSceneSequence.find_marked_frame_by_frame_number_in_sequence"></a>

#### find_marked_frame_by_frame_number_in_sequence

```python
def find_marked_frame_by_frame_number_in_sequence(
        frame_number: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> int
```

x.find_marked_frame_by_frame_number_in_sequence(frame_number, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> int32
* Find the user marked frame by frame number
*
*
InFrameNumber: The frame number of the user marked frame to find

Args:
    frame_number (FrameNumber): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    int32:

<a id="unreal.MovieSceneSequence.find_marked_frame_by_frame_number"></a>

#### find_marked_frame_by_frame_number

```python
def find_marked_frame_by_frame_number(frame_number: FrameNumber) -> int
```

x.find_marked_frame_by_frame_number(frame_number) -> int32
Find Marked Frame by Frame Number
deprecated: FindMarkedFrameByFrameNumber is deprecated. Please use FindMarkedFrameByFrameNumber that takes a time unit instead

Args:
    frame_number (FrameNumber): 

Returns:
    int32:

<a id="unreal.MovieSceneSequence.find_binding_by_name"></a>

#### find_binding_by_name

```python
def find_binding_by_name(name: str) -> MovieSceneBindingProxy
```

x.find_binding_by_name(name) -> MovieSceneBindingProxy
Attempt to locate a binding in this sequence by its name

Args:
    name (str): The display name of the binding to look up

Returns:
    MovieSceneBindingProxy: A unique identifier for the binding, or invalid

<a id="unreal.MovieSceneSequence.find_binding_by_id"></a>

#### find_binding_by_id

```python
def find_binding_by_id(binding_id: Guid) -> MovieSceneBindingProxy
```

x.find_binding_by_id(binding_id) -> MovieSceneBindingProxy
Attempt to locate a binding in this sequence by its Id

Args:
    binding_id (Guid): The binding Id to look up

Returns:
    MovieSceneBindingProxy: A unique identifier for the binding, or invalid

<a id="unreal.MovieSceneSequence.delete_marked_frames"></a>

#### delete_marked_frames

```python
def delete_marked_frames() -> None
```

x.delete_marked_frames() -> None
* Delete all user marked frames

<a id="unreal.MovieSceneSequence.delete_marked_frame"></a>

#### delete_marked_frame

```python
def delete_marked_frame(delete_index: int) -> None
```

x.delete_marked_frame(delete_index) -> None
* Delete the user marked frame by index.
*
*
DeleteIndex: The index to the user marked frame to delete

Args:
    delete_index (int32):

<a id="unreal.MovieSceneSequence.are_marked_frames_locked"></a>

#### are_marked_frames_locked

```python
def are_marked_frames_locked() -> bool
```

x.are_marked_frames_locked() -> bool
* Are marked frames locked
*
*

Returns:
    bool: Whether the movie scene marked frames are locked

<a id="unreal.MovieSceneSequence.add_track"></a>

#### add_track

```python
def add_track(track_type: Class) -> MovieSceneTrack
```

x.add_track(track_type) -> MovieSceneTrack
Add a new track of the specified type

Args:
    track_type (type(Class)): A UMovieSceneTrack class type to create

Returns:
    MovieSceneTrack: The newly created track, if successful

<a id="unreal.MovieSceneSequence.add_spawnable_from_instance"></a>

#### add_spawnable_from_instance

```python
def add_spawnable_from_instance(
        object_to_spawn: Object) -> MovieSceneBindingProxy
```

x.add_spawnable_from_instance(object_to_spawn) -> MovieSceneBindingProxy
Add a new binding to this sequence that will spawn the specified object.
For level sequences this will make a custom binding of type UMovieSceneSpawnableActorBinding.

Args:
    object_to_spawn (Object): An object instance to use as a template for spawning

Returns:
    MovieSceneBindingProxy: A unique identifier for the new binding

<a id="unreal.MovieSceneSequence.add_spawnable_from_class"></a>

#### add_spawnable_from_class

```python
def add_spawnable_from_class(class_to_spawn: Class) -> MovieSceneBindingProxy
```

x.add_spawnable_from_class(class_to_spawn) -> MovieSceneBindingProxy
Add a new binding to this sequence that will spawn the specified object
For level sequences this will make a custom binding of type UMovieSceneSpawnableActorBinding.

Args:
    class_to_spawn (type(Class)): A class or blueprint type to spawn for this binding

Returns:
    MovieSceneBindingProxy: A unique identifier for the new binding

<a id="unreal.MovieSceneSequence.add_root_folder_to_sequence"></a>

#### add_root_folder_to_sequence

```python
def add_root_folder_to_sequence(new_folder_name: str) -> MovieSceneFolder
```

x.add_root_folder_to_sequence(new_folder_name) -> MovieSceneFolder
Add a root folder to the given sequence

Args:
    new_folder_name (str): The name to give the added folder

Returns:
    MovieSceneFolder: The newly created folder

<a id="unreal.MovieSceneSequence.add_possessable"></a>

#### add_possessable

```python
def add_possessable(object_to_possess: Object) -> MovieSceneBindingProxy
```

x.add_possessable(object_to_possess) -> MovieSceneBindingProxy
Add a new binding to this sequence that will possess the specified object

Args:
    object_to_possess (Object): The object that this sequence should possess when evaluating

Returns:
    MovieSceneBindingProxy: A unique identifier for the new binding

<a id="unreal.MovieSceneSequence.add_marked_frame_to_sequence"></a>

#### add_marked_frame_to_sequence

```python
def add_marked_frame_to_sequence(
        marked_frame: MovieSceneMarkedFrame,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> int
```

x.add_marked_frame_to_sequence(marked_frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> int32
* Add a given user marked frame.
* A unique label will be generated if the marked frame label is empty
*
*
InMarkedFrame: The given user marked frame to add *

Args:
    marked_frame (MovieSceneMarkedFrame): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    int32: The index to the newly added marked frame

<a id="unreal.MovieSceneSequence.add_marked_frame"></a>

#### add_marked_frame

```python
def add_marked_frame(marked_frame: MovieSceneMarkedFrame) -> int
```

x.add_marked_frame(marked_frame) -> int32
Add Marked Frame
deprecated: AddMarkedFrame is deprecated. Please use AddMarkedFrame that takes a time unit instead

Args:
    marked_frame (MovieSceneMarkedFrame): 

Returns:
    int32:

<a id="unreal.WidgetAnimation"></a>