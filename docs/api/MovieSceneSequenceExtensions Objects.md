## MovieSceneSequenceExtensions Objects

```python
class MovieSceneSequenceExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieSceneSequences for scripting purposes

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneSequenceExtensions.h

<a id="unreal.MovieSceneSequenceExtensions.sort_marked_frames"></a>

#### sort_marked_frames

```python
@classmethod
def sort_marked_frames(cls, sequence: MovieSceneSequence) -> None
```

X.sort_marked_frames(sequence) -> None
* Sort the marked frames in chronological order

Args:
    sequence (MovieSceneSequence):

<a id="unreal.MovieSceneSequenceExtensions.set_work_range_start"></a>

#### set_work_range_start

```python
@classmethod
def set_work_range_start(cls, sequence: MovieSceneSequence,
                         start_time_in_seconds: float) -> None
```

X.set_work_range_start(sequence, start_time_in_seconds) -> None
Set the sequence work range start in seconds

Args:
    sequence (MovieSceneSequence): 
    start_time_in_seconds (double): The desired work range start time in seconds for this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_work_range_end"></a>

#### set_work_range_end

```python
@classmethod
def set_work_range_end(cls, sequence: MovieSceneSequence,
                       end_time_in_seconds: float) -> None
```

X.set_work_range_end(sequence, end_time_in_seconds) -> None
Set the sequence work range end in seconds

Args:
    sequence (MovieSceneSequence): 
    end_time_in_seconds (double):

<a id="unreal.MovieSceneSequenceExtensions.set_view_range_start"></a>

#### set_view_range_start

```python
@classmethod
def set_view_range_start(cls, sequence: MovieSceneSequence,
                         start_time_in_seconds: float) -> None
```

X.set_view_range_start(sequence, start_time_in_seconds) -> None
Set the sequence view range start in seconds

Args:
    sequence (MovieSceneSequence): 
    start_time_in_seconds (double): The desired view range start time in seconds for this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_view_range_end"></a>

#### set_view_range_end

```python
@classmethod
def set_view_range_end(cls, sequence: MovieSceneSequence,
                       end_time_in_seconds: float) -> None
```

X.set_view_range_end(sequence, end_time_in_seconds) -> None
Set the sequence view range end in seconds

Args:
    sequence (MovieSceneSequence): 
    end_time_in_seconds (double):

<a id="unreal.MovieSceneSequenceExtensions.set_tick_resolution_directly"></a>

#### set_tick_resolution_directly

```python
@classmethod
def set_tick_resolution_directly(cls, sequence: MovieSceneSequence,
                                 tick_resolution: FrameRate) -> None
```

X.set_tick_resolution_directly(sequence, tick_resolution) -> None
Sets this sequence's tick resolution directly without migrating frame times

Args:
    sequence (MovieSceneSequence): The sequence to use
    tick_resolution (FrameRate): The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_tick_resolution"></a>

#### set_tick_resolution

```python
@classmethod
def set_tick_resolution(cls, sequence: MovieSceneSequence,
                        tick_resolution: FrameRate) -> None
```

X.set_tick_resolution(sequence, tick_resolution) -> None
Sets this sequence's tick resolution and migrates frame times

Args:
    sequence (MovieSceneSequence): The sequence to use
    tick_resolution (FrameRate): The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_read_only"></a>

#### set_read_only

```python
@classmethod
def set_read_only(cls, sequence: MovieSceneSequence, read_only: bool) -> None
```

X.set_read_only(sequence, read_only) -> None
* Set read only
*
*
bInReadOnly: Whether the movie scene should be read only or not

Args:
    sequence (MovieSceneSequence): 
    read_only (bool):

<a id="unreal.MovieSceneSequenceExtensions.set_playback_start_seconds"></a>

#### set_playback_start_seconds

```python
@classmethod
def set_playback_start_seconds(cls, sequence: MovieSceneSequence,
                               start_time: float) -> None
```

X.set_playback_start_seconds(sequence, start_time) -> None
Set playback start of this sequence in seconds

Args:
    sequence (MovieSceneSequence): The sequence within which to set the playback start
    start_time (float): The desired start time in seconds for this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_playback_start"></a>

#### set_playback_start

```python
@classmethod
def set_playback_start(cls, sequence: MovieSceneSequence,
                       start_frame: int) -> None
```

X.set_playback_start(sequence, start_frame) -> None
Set playback start of this sequence

Args:
    sequence (MovieSceneSequence): The sequence within which to set the playback start
    start_frame (int32): The desired start frame for this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_playback_range_locked"></a>

#### set_playback_range_locked

```python
@classmethod
def set_playback_range_locked(cls, sequence: MovieSceneSequence,
                              locked: bool) -> None
```

X.set_playback_range_locked(sequence, locked) -> None
* Set playback range locked
*
*
bInLocked: Whether the movie scene playback range should be locked

Args:
    sequence (MovieSceneSequence): 
    locked (bool):

<a id="unreal.MovieSceneSequenceExtensions.set_playback_end_seconds"></a>

#### set_playback_end_seconds

```python
@classmethod
def set_playback_end_seconds(cls, sequence: MovieSceneSequence,
                             end_time: float) -> None
```

X.set_playback_end_seconds(sequence, end_time) -> None
Set playback end of this sequence in seconds

Args:
    sequence (MovieSceneSequence): The sequence within which to set the playback end
    end_time (float): The desired end time in seconds for this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_playback_end"></a>

#### set_playback_end

```python
@classmethod
def set_playback_end(cls, sequence: MovieSceneSequence,
                     end_frame: int) -> None
```

X.set_playback_end(sequence, end_frame) -> None
Set playback end of this sequence

Args:
    sequence (MovieSceneSequence): The sequence within which to set the playback end
    end_frame (int32): The desired end frame for this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_marked_frames_locked"></a>

#### set_marked_frames_locked

```python
@classmethod
def set_marked_frames_locked(cls, sequence: MovieSceneSequence,
                             locked: bool) -> None
```

X.set_marked_frames_locked(sequence, locked) -> None
* Set marked frames locked
*
*
bInLocked: Whether the movie scene marked frames should be locked

Args:
    sequence (MovieSceneSequence): 
    locked (bool):

<a id="unreal.MovieSceneSequenceExtensions.set_marked_frame_in_sequence"></a>

#### set_marked_frame_in_sequence

```python
@classmethod
def set_marked_frame_in_sequence(
        cls,
        sequence: MovieSceneSequence,
        mark_index: int,
        frame_number: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_marked_frame_in_sequence(sequence, mark_index, frame_number, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
* Sets the frame number for the given marked frame index. Does not maintain sort. Call SortMarkedFrames
*
*
InMarkIndex: The given user marked frame index to edit *
InFrameNumber: The frame number to set

Args:
    sequence (MovieSceneSequence): 
    mark_index (int32): 
    frame_number (FrameNumber): 
    time_unit (MovieSceneTimeUnit):

<a id="unreal.MovieSceneSequenceExtensions.set_marked_frame"></a>

#### set_marked_frame

```python
@classmethod
def set_marked_frame(cls, sequence: MovieSceneSequence, mark_index: int,
                     frame_number: FrameNumber) -> None
```

X.set_marked_frame(sequence, mark_index, frame_number) -> None
Set Marked Frame
deprecated: SetMarkedFrame is deprecated. Please use SetMarkedFrame that takes a time unit instead

Args:
    sequence (MovieSceneSequence): 
    mark_index (int32): 
    frame_number (FrameNumber):

<a id="unreal.MovieSceneSequenceExtensions.set_evaluation_type"></a>

#### set_evaluation_type

```python
@classmethod
def set_evaluation_type(cls, sequence: MovieSceneSequence,
                        evaluation_type: MovieSceneEvaluationType) -> None
```

X.set_evaluation_type(sequence, evaluation_type) -> None
Set the evaluation type for this sequence

Args:
    sequence (MovieSceneSequence): 
    evaluation_type (MovieSceneEvaluationType): The evaluation type to set for this sequence

<a id="unreal.MovieSceneSequenceExtensions.set_display_rate"></a>

#### set_display_rate

```python
@classmethod
def set_display_rate(cls, sequence: MovieSceneSequence,
                     display_rate: FrameRate) -> None
```

X.set_display_rate(sequence, display_rate) -> None
Sets this sequence's display rate

Args:
    sequence (MovieSceneSequence): The sequence to use
    display_rate (FrameRate): The display rate that this sequence is displayed as

<a id="unreal.MovieSceneSequenceExtensions.set_clock_source"></a>

#### set_clock_source

```python
@classmethod
def set_clock_source(cls, sequence: MovieSceneSequence,
                     clock_source: UpdateClockSource) -> None
```

X.set_clock_source(sequence, clock_source) -> None
Set the clock source for this sequence

Args:
    sequence (MovieSceneSequence): 
    clock_source (UpdateClockSource): The clock source to set for this sequence

<a id="unreal.MovieSceneSequenceExtensions.resolve_binding_id"></a>

#### resolve_binding_id

```python
@classmethod
def resolve_binding_id(
        cls, root_sequence: MovieSceneSequence,
        object_binding_id: MovieSceneObjectBindingID
) -> MovieSceneBindingProxy
```

X.resolve_binding_id(root_sequence, object_binding_id) -> MovieSceneBindingProxy
Make a binding for the given binding ID

Args:
    root_sequence (MovieSceneSequence): The root sequence that contains the sequence
    object_binding_id (MovieSceneObjectBindingID): 

Returns:
    MovieSceneBindingProxy: The new binding proxy

<a id="unreal.MovieSceneSequenceExtensions.remove_track"></a>

#### remove_track

```python
@classmethod
def remove_track(cls, sequence: MovieSceneSequence,
                 track: MovieSceneTrack) -> bool
```

X.remove_track(sequence, track) -> bool
Removes a track

Args:
    sequence (MovieSceneSequence): The sequence to use
    track (MovieSceneTrack): The track to remove

Returns:
    bool: Whether the track was successfully removed

<a id="unreal.MovieSceneSequenceExtensions.remove_root_folder_from_sequence"></a>

#### remove_root_folder_from_sequence

```python
@classmethod
def remove_root_folder_from_sequence(cls, sequence: MovieSceneSequence,
                                     folder: MovieSceneFolder) -> None
```

X.remove_root_folder_from_sequence(sequence, folder) -> None
Remove a root folder from the given sequence. Will throw an exception if the specified folder is not valid or not a root folder.

Args:
    sequence (MovieSceneSequence): The sequence That the folder belongs to
    folder (MovieSceneFolder): The folder to remove

<a id="unreal.MovieSceneSequenceExtensions.make_range_seconds"></a>

#### make_range_seconds

```python
@classmethod
def make_range_seconds(cls, sequence: MovieSceneSequence, start_time: float,
                       duration: float) -> SequencerScriptingRange
```

X.make_range_seconds(sequence, start_time, duration) -> SequencerScriptingRange
Make a new range for this sequence in seconds

Args:
    sequence (MovieSceneSequence): The sequence within which to find the binding
    start_time (float): The time in seconds at which to start the range
    duration (float): The length of the range in seconds

Returns:
    SequencerScriptingRange: Specified sequencer range

<a id="unreal.MovieSceneSequenceExtensions.make_range"></a>

#### make_range

```python
@classmethod
def make_range(cls, sequence: MovieSceneSequence, start_frame: int,
               duration: int) -> SequencerScriptingRange
```

X.make_range(sequence, start_frame, duration) -> SequencerScriptingRange
Make a new range for this sequence in its display rate

Args:
    sequence (MovieSceneSequence): The sequence within which to find the binding
    start_frame (int32): The frame at which to start the range
    duration (int32): The length of the range

Returns:
    SequencerScriptingRange: Specified sequencer range

<a id="unreal.MovieSceneSequenceExtensions.locate_bound_objects"></a>

#### locate_bound_objects

```python
@classmethod
def locate_bound_objects(cls, sequence: MovieSceneSequence,
                         binding: MovieSceneBindingProxy,
                         context: Object) -> Array[Object]
```

X.locate_bound_objects(sequence, binding, context) -> Array[Object]
Locate all the objects that correspond to the specified object ID, using the specified context

Args:
    sequence (MovieSceneSequence): The sequence to locate bound objects for
    binding (MovieSceneBindingProxy): The object binding
    context (Object): Optional context to use to find the required object

Returns:
    Array[Object]: An array of all bound objects

<a id="unreal.MovieSceneSequenceExtensions.is_read_only"></a>

#### is_read_only

```python
@classmethod
def is_read_only(cls, sequence: MovieSceneSequence) -> bool
```

X.is_read_only(sequence) -> bool
* Is read only
*
*

Args:
    sequence (MovieSceneSequence): 

Returns:
    bool: Whether the movie scene is read only or not

<a id="unreal.MovieSceneSequenceExtensions.is_playback_range_locked"></a>

#### is_playback_range_locked

```python
@classmethod
def is_playback_range_locked(cls, sequence: MovieSceneSequence) -> bool
```

X.is_playback_range_locked(sequence) -> bool
* Is playback ranged locked
*
*

Args:
    sequence (MovieSceneSequence): 

Returns:
    bool: Whether the movie scene playback range is locked

<a id="unreal.MovieSceneSequenceExtensions.get_work_range_start"></a>

#### get_work_range_start

```python
@classmethod
def get_work_range_start(cls, sequence: MovieSceneSequence) -> float
```

X.get_work_range_start(sequence) -> double
Get the sequence work range start in seconds

Args:
    sequence (MovieSceneSequence): 

Returns:
    double: The work range start time in seconds for this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_work_range_end"></a>

#### get_work_range_end

```python
@classmethod
def get_work_range_end(cls, sequence: MovieSceneSequence) -> float
```

X.get_work_range_end(sequence) -> double
Get the sequence work range end in seconds

Args:
    sequence (MovieSceneSequence): 

Returns:
    double: The work range end time in seconds for this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_view_range_start"></a>

#### get_view_range_start

```python
@classmethod
def get_view_range_start(cls, sequence: MovieSceneSequence) -> float
```

X.get_view_range_start(sequence) -> double
Get the sequence view range start in seconds

Args:
    sequence (MovieSceneSequence): 

Returns:
    double: The view range start time in seconds for this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_view_range_end"></a>

#### get_view_range_end

```python
@classmethod
def get_view_range_end(cls, sequence: MovieSceneSequence) -> float
```

X.get_view_range_end(sequence) -> double
Get the sequence view range end in seconds

Args:
    sequence (MovieSceneSequence): 

Returns:
    double: The view range end time in seconds for this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_tracks"></a>

#### get_tracks

```python
@classmethod
def get_tracks(cls, sequence: MovieSceneSequence) -> Array[MovieSceneTrack]
```

X.get_tracks(sequence) -> Array[MovieSceneTrack]
Get all tracks

Args:
    sequence (MovieSceneSequence): The sequence to use

Returns:
    Array[MovieSceneTrack]: An array containing all tracks in this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_tick_resolution"></a>

#### get_tick_resolution

```python
@classmethod
def get_tick_resolution(cls, sequence: MovieSceneSequence) -> FrameRate
```

X.get_tick_resolution(sequence) -> FrameRate
Gets this sequence's tick resolution

Args:
    sequence (MovieSceneSequence): The sequence to use

Returns:
    FrameRate: The tick resolution of the sequence, defining the smallest unit of time representable on this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_spawnables"></a>

#### get_spawnables

```python
@classmethod
def get_spawnables(
        cls, sequence: MovieSceneSequence) -> Array[MovieSceneBindingProxy]
```

X.get_spawnables(sequence) -> Array[MovieSceneBindingProxy]
Get all the spawnables in this sequence. For Level Sequences, this includes bindings with binding type UMovieSceneSpawnableActorBinding.

Args:
    sequence (MovieSceneSequence): The sequence to get spawnables for

Returns:
    Array[MovieSceneBindingProxy]: Spawnables in this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_root_folders_in_sequence"></a>

#### get_root_folders_in_sequence

```python
@classmethod
def get_root_folders_in_sequence(
        cls, sequence: MovieSceneSequence) -> Array[MovieSceneFolder]
```

X.get_root_folders_in_sequence(sequence) -> Array[MovieSceneFolder]
Get the root folders in the provided sequence

Args:
    sequence (MovieSceneSequence): The sequence to retrieve folders from

Returns:
    Array[MovieSceneFolder]: The folders contained within the given sequence

<a id="unreal.MovieSceneSequenceExtensions.get_possessables"></a>

#### get_possessables

```python
@classmethod
def get_possessables(
        cls, sequence: MovieSceneSequence) -> Array[MovieSceneBindingProxy]
```

X.get_possessables(sequence) -> Array[MovieSceneBindingProxy]
Get all the possessables in this sequence. It is understood for the purpose of this function that this means the bindings are not custom.

Args:
    sequence (MovieSceneSequence): The sequence to get possessables for

Returns:
    Array[MovieSceneBindingProxy]: Possessables in this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_portable_binding_id"></a>

#### get_portable_binding_id

```python
@classmethod
def get_portable_binding_id(
        cls, root_sequence: MovieSceneSequence,
        destination_sequence: MovieSceneSequence,
        binding: MovieSceneBindingProxy) -> MovieSceneObjectBindingID
```

X.get_portable_binding_id(root_sequence, destination_sequence, binding) -> MovieSceneObjectBindingID
Get a portable binding ID for a binding that resides in a different sequence to the one where this binding will be resolved.
note:: This function must be used over GetBindingID when the target binding resides in different shots or sub-sequences.
note:: Only unique instances of sequences within a root sequences are supported

Args:
    root_sequence (MovieSceneSequence): The root sequence that contains both the destination sequence (that will resolve the binding ID) and the target sequence that contains the actual binding
    destination_sequence (MovieSceneSequence): The sequence that will own or resolve the resulting binding ID. For example, if the binding ID will be applied to a camera cut section pass the sequence that contains the camera cut track to this parameter.
    binding (MovieSceneBindingProxy): 

Returns:
    MovieSceneObjectBindingID: The binding's id

<a id="unreal.MovieSceneSequenceExtensions.get_playback_start_seconds"></a>

#### get_playback_start_seconds

```python
@classmethod
def get_playback_start_seconds(cls, sequence: MovieSceneSequence) -> float
```

X.get_playback_start_seconds(sequence) -> float
Get playback start of this sequence in seconds

Args:
    sequence (MovieSceneSequence): The sequence within which to get the playback start

Returns:
    float: Playback start of this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_playback_start"></a>

#### get_playback_start

```python
@classmethod
def get_playback_start(cls, sequence: MovieSceneSequence) -> int
```

X.get_playback_start(sequence) -> int32
Get playback start of this sequence in display rate resolution

Args:
    sequence (MovieSceneSequence): The sequence within which to get the playback start

Returns:
    int32: Playback start of this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_playback_range"></a>

#### get_playback_range

```python
@classmethod
def get_playback_range(
        cls, sequence: MovieSceneSequence) -> SequencerScriptingRange
```

X.get_playback_range(sequence) -> SequencerScriptingRange
Get playback range of this sequence in display rate resolution

Args:
    sequence (MovieSceneSequence): The sequence within which to get the playback range

Returns:
    SequencerScriptingRange: Playback range of this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_playback_end_seconds"></a>

#### get_playback_end_seconds

```python
@classmethod
def get_playback_end_seconds(cls, sequence: MovieSceneSequence) -> float
```

X.get_playback_end_seconds(sequence) -> float
Get playback end of this sequence in seconds

Args:
    sequence (MovieSceneSequence): The sequence within which to get the playback end

Returns:
    float: Playback end of this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_playback_end"></a>

#### get_playback_end

```python
@classmethod
def get_playback_end(cls, sequence: MovieSceneSequence) -> int
```

X.get_playback_end(sequence) -> int32
Get playback end of this sequence in display rate resolution

Args:
    sequence (MovieSceneSequence): The sequence within which to get the playback end

Returns:
    int32: Playback end of this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_movie_scene"></a>

#### get_movie_scene

```python
@classmethod
def get_movie_scene(cls, sequence: MovieSceneSequence) -> MovieScene
```

X.get_movie_scene(sequence) -> MovieScene
Get this sequence's movie scene data

Args:
    sequence (MovieSceneSequence): The sequence to use

Returns:
    MovieScene: This sequence's movie scene data object

<a id="unreal.MovieSceneSequenceExtensions.get_marked_frames_from_sequence"></a>

#### get_marked_frames_from_sequence

```python
@classmethod
def get_marked_frames_from_sequence(
    cls,
    sequence: MovieSceneSequence,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[MovieSceneMarkedFrame]
```

X.get_marked_frames_from_sequence(sequence, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[MovieSceneMarkedFrame]
* Get the marked frames for this sequence
*
*

Args:
    sequence (MovieSceneSequence): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    Array[MovieSceneMarkedFrame]: Return the user marked frames

<a id="unreal.MovieSceneSequenceExtensions.get_marked_frames"></a>

#### get_marked_frames

```python
@classmethod
def get_marked_frames(
        cls, sequence: MovieSceneSequence) -> Array[MovieSceneMarkedFrame]
```

X.get_marked_frames(sequence) -> Array[MovieSceneMarkedFrame]
Get Marked Frames
deprecated: GetMarkedFrames is deprecated. Please use GetMarkedFrames that takes a time unit instead

Args:
    sequence (MovieSceneSequence): 

Returns:
    Array[MovieSceneMarkedFrame]:

<a id="unreal.MovieSceneSequenceExtensions.get_evaluation_type"></a>

#### get_evaluation_type

```python
@classmethod
def get_evaluation_type(
        cls, sequence: MovieSceneSequence) -> MovieSceneEvaluationType
```

X.get_evaluation_type(sequence) -> MovieSceneEvaluationType
Get the evaluation type for this sequence

Args:
    sequence (MovieSceneSequence): 

Returns:
    MovieSceneEvaluationType: The evaluation type for this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_display_rate"></a>

#### get_display_rate

```python
@classmethod
def get_display_rate(cls, sequence: MovieSceneSequence) -> FrameRate
```

X.get_display_rate(sequence) -> FrameRate
Gets this sequence's display rate

Args:
    sequence (MovieSceneSequence): The sequence to use

Returns:
    FrameRate: The display rate that this sequence is displayed as

<a id="unreal.MovieSceneSequenceExtensions.get_clock_source"></a>

#### get_clock_source

```python
@classmethod
def get_clock_source(cls, sequence: MovieSceneSequence) -> UpdateClockSource
```

X.get_clock_source(sequence) -> UpdateClockSource
Get the clock source for this sequence

Args:
    sequence (MovieSceneSequence): 

Returns:
    UpdateClockSource: The clock source for this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_bindings"></a>

#### get_bindings

```python
@classmethod
def get_bindings(
        cls, sequence: MovieSceneSequence) -> Array[MovieSceneBindingProxy]
```

X.get_bindings(sequence) -> Array[MovieSceneBindingProxy]
Get all the bindings in this sequence

Args:
    sequence (MovieSceneSequence): The sequence to get bindings for

Returns:
    Array[MovieSceneBindingProxy]: An array of unique identifiers for all the bindings in this sequence

<a id="unreal.MovieSceneSequenceExtensions.get_binding_id"></a>

#### get_binding_id

```python
@classmethod
def get_binding_id(
        cls, sequence: MovieSceneSequence,
        binding: MovieSceneBindingProxy) -> MovieSceneObjectBindingID
```

X.get_binding_id(sequence, binding) -> MovieSceneObjectBindingID
Get the binding ID for a binding within a sequence.
note:: The resulting binding is only valid when applied to properties within the same sequence as this binding. Use GetPortableBindingID for bindings which live in different sub-sequences.

Args:
    sequence (MovieSceneSequence): 
    binding (MovieSceneBindingProxy): 

Returns:
    MovieSceneObjectBindingID: The binding's id

<a id="unreal.MovieSceneSequenceExtensions.find_tracks_by_type"></a>

#### find_tracks_by_type

```python
@classmethod
def find_tracks_by_type(cls, sequence: MovieSceneSequence,
                        track_type: Class) -> Array[MovieSceneTrack]
```

X.find_tracks_by_type(sequence, track_type) -> Array[MovieSceneTrack]
Find all tracks of the specified type

Args:
    sequence (MovieSceneSequence): The sequence to use
    track_type (type(Class)): A UMovieSceneTrack class type specifying which types of track to return

Returns:
    Array[MovieSceneTrack]: An array containing any tracks that match the type specified

<a id="unreal.MovieSceneSequenceExtensions.find_tracks_by_exact_type"></a>

#### find_tracks_by_exact_type

```python
@classmethod
def find_tracks_by_exact_type(cls, sequence: MovieSceneSequence,
                              track_type: Class) -> Array[MovieSceneTrack]
```

X.find_tracks_by_exact_type(sequence, track_type) -> Array[MovieSceneTrack]
Find all tracks of the specified type, not allowing sub-classed types

Args:
    sequence (MovieSceneSequence): The sequence to use
    track_type (type(Class)): A UMovieSceneTrack class type specifying the exact types of track to return

Returns:
    Array[MovieSceneTrack]: An array containing any tracks that are exactly the same as the type specified

<a id="unreal.MovieSceneSequenceExtensions.find_next_marked_frame_in_sequence"></a>

#### find_next_marked_frame_in_sequence

```python
@classmethod
def find_next_marked_frame_in_sequence(
        cls,
        sequence: MovieSceneSequence,
        frame_number: FrameNumber,
        forward: bool,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> int
```

X.find_next_marked_frame_in_sequence(sequence, frame_number, forward, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> int32
* Find the next/previous user marked frame from the given frame number
*
*
InFrameNumber: The frame number to find the next/previous user marked frame from *
bForward: Find forward from the given frame number.

Args:
    sequence (MovieSceneSequence): 
    frame_number (FrameNumber): 
    forward (bool): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    int32:

<a id="unreal.MovieSceneSequenceExtensions.find_next_marked_frame"></a>

#### find_next_marked_frame

```python
@classmethod
def find_next_marked_frame(cls, sequence: MovieSceneSequence,
                           frame_number: FrameNumber, forward: bool) -> int
```

X.find_next_marked_frame(sequence, frame_number, forward) -> int32
Find Next Marked Frame
deprecated: FindNextMarkedFrame is deprecated. Please use FindNextMarkedFrame that takes a time unit and defaults to display rate instead

Args:
    sequence (MovieSceneSequence): 
    frame_number (FrameNumber): 
    forward (bool): 

Returns:
    int32:

<a id="unreal.MovieSceneSequenceExtensions.find_marked_frame_by_label"></a>

#### find_marked_frame_by_label

```python
@classmethod
def find_marked_frame_by_label(cls, sequence: MovieSceneSequence,
                               label: str) -> int
```

X.find_marked_frame_by_label(sequence, label) -> int32
* Find the user marked frame by label
*
*
InLabel: The label to the user marked frame to find

Args:
    sequence (MovieSceneSequence): 
    label (str): 

Returns:
    int32:

<a id="unreal.MovieSceneSequenceExtensions.find_marked_frame_by_frame_number_in_sequence"></a>

#### find_marked_frame_by_frame_number_in_sequence

```python
@classmethod
def find_marked_frame_by_frame_number_in_sequence(
        cls,
        sequence: MovieSceneSequence,
        frame_number: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> int
```

X.find_marked_frame_by_frame_number_in_sequence(sequence, frame_number, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> int32
* Find the user marked frame by frame number
*
*
InFrameNumber: The frame number of the user marked frame to find

Args:
    sequence (MovieSceneSequence): 
    frame_number (FrameNumber): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    int32:

<a id="unreal.MovieSceneSequenceExtensions.find_marked_frame_by_frame_number"></a>

#### find_marked_frame_by_frame_number

```python
@classmethod
def find_marked_frame_by_frame_number(cls, sequence: MovieSceneSequence,
                                      frame_number: FrameNumber) -> int
```

X.find_marked_frame_by_frame_number(sequence, frame_number) -> int32
Find Marked Frame by Frame Number
deprecated: FindMarkedFrameByFrameNumber is deprecated. Please use FindMarkedFrameByFrameNumber that takes a time unit instead

Args:
    sequence (MovieSceneSequence): 
    frame_number (FrameNumber): 

Returns:
    int32:

<a id="unreal.MovieSceneSequenceExtensions.find_binding_by_name"></a>

#### find_binding_by_name

```python
@classmethod
def find_binding_by_name(cls, sequence: MovieSceneSequence,
                         name: str) -> MovieSceneBindingProxy
```

X.find_binding_by_name(sequence, name) -> MovieSceneBindingProxy
Attempt to locate a binding in this sequence by its name

Args:
    sequence (MovieSceneSequence): The sequence within which to find the binding
    name (str): The display name of the binding to look up

Returns:
    MovieSceneBindingProxy: A unique identifier for the binding, or invalid

<a id="unreal.MovieSceneSequenceExtensions.find_binding_by_id"></a>

#### find_binding_by_id

```python
@classmethod
def find_binding_by_id(cls, sequence: MovieSceneSequence,
                       binding_id: Guid) -> MovieSceneBindingProxy
```

X.find_binding_by_id(sequence, binding_id) -> MovieSceneBindingProxy
Attempt to locate a binding in this sequence by its Id

Args:
    sequence (MovieSceneSequence): The sequence within which to find the binding
    binding_id (Guid): The binding Id to look up

Returns:
    MovieSceneBindingProxy: A unique identifier for the binding, or invalid

<a id="unreal.MovieSceneSequenceExtensions.delete_marked_frames"></a>

#### delete_marked_frames

```python
@classmethod
def delete_marked_frames(cls, sequence: MovieSceneSequence) -> None
```

X.delete_marked_frames(sequence) -> None
* Delete all user marked frames

Args:
    sequence (MovieSceneSequence):

<a id="unreal.MovieSceneSequenceExtensions.delete_marked_frame"></a>

#### delete_marked_frame

```python
@classmethod
def delete_marked_frame(cls, sequence: MovieSceneSequence,
                        delete_index: int) -> None
```

X.delete_marked_frame(sequence, delete_index) -> None
* Delete the user marked frame by index.
*
*
DeleteIndex: The index to the user marked frame to delete

Args:
    sequence (MovieSceneSequence): 
    delete_index (int32):

<a id="unreal.MovieSceneSequenceExtensions.are_marked_frames_locked"></a>

#### are_marked_frames_locked

```python
@classmethod
def are_marked_frames_locked(cls, sequence: MovieSceneSequence) -> bool
```

X.are_marked_frames_locked(sequence) -> bool
* Are marked frames locked
*
*

Args:
    sequence (MovieSceneSequence): 

Returns:
    bool: Whether the movie scene marked frames are locked

<a id="unreal.MovieSceneSequenceExtensions.add_track"></a>

#### add_track

```python
@classmethod
def add_track(cls, sequence: MovieSceneSequence,
              track_type: Class) -> MovieSceneTrack
```

X.add_track(sequence, track_type) -> MovieSceneTrack
Add a new track of the specified type

Args:
    sequence (MovieSceneSequence): The sequence to use
    track_type (type(Class)): A UMovieSceneTrack class type to create

Returns:
    MovieSceneTrack: The newly created track, if successful

<a id="unreal.MovieSceneSequenceExtensions.add_spawnable_from_instance"></a>

#### add_spawnable_from_instance

```python
@classmethod
def add_spawnable_from_instance(
        cls, sequence: MovieSceneSequence,
        object_to_spawn: Object) -> MovieSceneBindingProxy
```

X.add_spawnable_from_instance(sequence, object_to_spawn) -> MovieSceneBindingProxy
Add a new binding to this sequence that will spawn the specified object.
For level sequences this will make a custom binding of type UMovieSceneSpawnableActorBinding.

Args:
    sequence (MovieSceneSequence): The sequence to add to
    object_to_spawn (Object): An object instance to use as a template for spawning

Returns:
    MovieSceneBindingProxy: A unique identifier for the new binding

<a id="unreal.MovieSceneSequenceExtensions.add_spawnable_from_class"></a>

#### add_spawnable_from_class

```python
@classmethod
def add_spawnable_from_class(cls, sequence: MovieSceneSequence,
                             class_to_spawn: Class) -> MovieSceneBindingProxy
```

X.add_spawnable_from_class(sequence, class_to_spawn) -> MovieSceneBindingProxy
Add a new binding to this sequence that will spawn the specified object
For level sequences this will make a custom binding of type UMovieSceneSpawnableActorBinding.

Args:
    sequence (MovieSceneSequence): The sequence to add to
    class_to_spawn (type(Class)): A class or blueprint type to spawn for this binding

Returns:
    MovieSceneBindingProxy: A unique identifier for the new binding

<a id="unreal.MovieSceneSequenceExtensions.add_root_folder_to_sequence"></a>

#### add_root_folder_to_sequence

```python
@classmethod
def add_root_folder_to_sequence(cls, sequence: MovieSceneSequence,
                                new_folder_name: str) -> MovieSceneFolder
```

X.add_root_folder_to_sequence(sequence, new_folder_name) -> MovieSceneFolder
Add a root folder to the given sequence

Args:
    sequence (MovieSceneSequence): The sequence to add a folder to
    new_folder_name (str): The name to give the added folder

Returns:
    MovieSceneFolder: The newly created folder

<a id="unreal.MovieSceneSequenceExtensions.add_possessable"></a>

#### add_possessable

```python
@classmethod
def add_possessable(cls, sequence: MovieSceneSequence,
                    object_to_possess: Object) -> MovieSceneBindingProxy
```

X.add_possessable(sequence, object_to_possess) -> MovieSceneBindingProxy
Add a new binding to this sequence that will possess the specified object

Args:
    sequence (MovieSceneSequence): The sequence to add a possessable to
    object_to_possess (Object): The object that this sequence should possess when evaluating

Returns:
    MovieSceneBindingProxy: A unique identifier for the new binding

<a id="unreal.MovieSceneSequenceExtensions.add_marked_frame_to_sequence"></a>

#### add_marked_frame_to_sequence

```python
@classmethod
def add_marked_frame_to_sequence(
        cls,
        sequence: MovieSceneSequence,
        marked_frame: MovieSceneMarkedFrame,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> int
```

X.add_marked_frame_to_sequence(sequence, marked_frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> int32
* Add a given user marked frame.
* A unique label will be generated if the marked frame label is empty
*
*
InMarkedFrame: The given user marked frame to add *

Args:
    sequence (MovieSceneSequence): 
    marked_frame (MovieSceneMarkedFrame): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    int32: The index to the newly added marked frame

<a id="unreal.MovieSceneSequenceExtensions.add_marked_frame"></a>

#### add_marked_frame

```python
@classmethod
def add_marked_frame(cls, sequence: MovieSceneSequence,
                     marked_frame: MovieSceneMarkedFrame) -> int
```

X.add_marked_frame(sequence, marked_frame) -> int32
Add Marked Frame
deprecated: AddMarkedFrame is deprecated. Please use AddMarkedFrame that takes a time unit instead

Args:
    sequence (MovieSceneSequence): 
    marked_frame (MovieSceneMarkedFrame): 

Returns:
    int32:

<a id="unreal.MovieSceneTimeWarpExtensions"></a>