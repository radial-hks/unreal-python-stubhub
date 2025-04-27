## MovieSceneSequencePlayer Objects

```python
class MovieSceneSequencePlayer(Object)
```

Abstract class that provides consistent player behaviour for various animation players

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_finished`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player finishes naturally (without explicitly calling stop)
- ``on_pause`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is paused
- ``on_play`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played
- ``on_play_reverse`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played in reverse
- ``on_stop`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is stopped

<a id="unreal.MovieSceneSequencePlayer.on_play"></a>

#### on_play

```python
@property
def on_play() -> OnMovieSceneSequencePlayerEvent
```

(OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played

<a id="unreal.MovieSceneSequencePlayer.on_play"></a>

#### on_play

```python
@on_play.setter
def on_play(value: OnMovieSceneSequencePlayerEvent) -> None
```

<a id="unreal.MovieSceneSequencePlayer.on_play_reverse"></a>

#### on_play_reverse

```python
@property
def on_play_reverse() -> OnMovieSceneSequencePlayerEvent
```

(OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played in reverse

<a id="unreal.MovieSceneSequencePlayer.on_play_reverse"></a>

#### on_play_reverse

```python
@on_play_reverse.setter
def on_play_reverse(value: OnMovieSceneSequencePlayerEvent) -> None
```

<a id="unreal.MovieSceneSequencePlayer.on_stop"></a>

#### on_stop

```python
@property
def on_stop() -> OnMovieSceneSequencePlayerEvent
```

(OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is stopped

<a id="unreal.MovieSceneSequencePlayer.on_stop"></a>

#### on_stop

```python
@on_stop.setter
def on_stop(value: OnMovieSceneSequencePlayerEvent) -> None
```

<a id="unreal.MovieSceneSequencePlayer.on_pause"></a>

#### on_pause

```python
@property
def on_pause() -> OnMovieSceneSequencePlayerEvent
```

(OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is paused

<a id="unreal.MovieSceneSequencePlayer.on_pause"></a>

#### on_pause

```python
@on_pause.setter
def on_pause(value: OnMovieSceneSequencePlayerEvent) -> None
```

<a id="unreal.MovieSceneSequencePlayer.on_finished"></a>

#### on_finished

```python
@property
def on_finished() -> OnMovieSceneSequencePlayerEvent
```

(OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player finishes naturally (without explicitly calling stop)

<a id="unreal.MovieSceneSequencePlayer.on_finished"></a>

#### on_finished

```python
@on_finished.setter
def on_finished(value: OnMovieSceneSequencePlayerEvent) -> None
```

<a id="unreal.MovieSceneSequencePlayer.stop_at_current_time"></a>

#### stop_at_current_time

```python
def stop_at_current_time() -> None
```

x.stop_at_current_time() -> None
Stop playback without moving the cursor.

<a id="unreal.MovieSceneSequencePlayer.stop"></a>

#### stop

```python
def stop() -> None
```

x.stop() -> None
Stop playback and move the cursor to the end (or start, for reversed playback) of the sequence.

<a id="unreal.MovieSceneSequencePlayer.set_weight"></a>

#### set_weight

```python
def set_weight(weight: float) -> None
```

x.set_weight(weight) -> None
Set a manual weight to be multiplied with all blendable elements within this sequence
note:: It is recommended that a weight between 0 and 1 is supplied, though this is not enforced
note:: It is recommended that either FMovieSceneSequencePlaybackSettings::DynamicWeighting should be true for this player or the asset it's playing back should be set to enable dynamic weight to avoid undesirable behavior

Args:
    weight (double): The weight to suuply to all elements in this sequence

<a id="unreal.MovieSceneSequencePlayer.set_time_range"></a>

#### set_time_range

```python
def set_time_range(start_time: float, duration: float) -> None
```

x.set_time_range(start_time, duration) -> None
Set the valid play range for this sequence, determined by a starting time  and a duration (in seconds)

Args:
    start_time (float): The time to start playing back the sequence in seconds
    duration (float): The length to play for

<a id="unreal.MovieSceneSequencePlayer.set_play_rate"></a>

#### set_play_rate

```python
def set_play_rate(play_rate: float) -> None
```

x.set_play_rate(play_rate) -> None
Set the playback rate of this player. Negative values will play the animation in reverse.

Args:
    play_rate (float): The new rate of playback for the animation.

<a id="unreal.MovieSceneSequencePlayer.set_playback_position"></a>

#### set_playback_position

```python
def set_playback_position(
        playback_params: MovieSceneSequencePlaybackParams) -> None
```

x.set_playback_position(playback_params) -> None
Set the current time of the player by evaluating from the current time to the specified time, as if the sequence is playing.
Triggers events that lie within the evaluated range. Does not alter the persistent playback status of the player (IsPlaying).

Args:
    playback_params (MovieSceneSequencePlaybackParams): The position settings (ie. the position to set playback to)

<a id="unreal.MovieSceneSequencePlayer.set_hide_hud"></a>

#### set_hide_hud

```python
def set_hide_hud(hide_hud: bool) -> None
```

x.set_hide_hud(hide_hud) -> None
Set if hiding the hud during play.

Args:
    hide_hud (bool): The new value of Hide Hud during play.

<a id="unreal.MovieSceneSequencePlayer.set_frame_rate"></a>

#### set_frame_rate

```python
def set_frame_rate(frame_rate: FrameRate) -> None
```

x.set_frame_rate(frame_rate) -> None
Set the frame-rate that this player should play with, making all frame numbers in the specified time-space

Args:
    frame_rate (FrameRate):

<a id="unreal.MovieSceneSequencePlayer.set_frame_range"></a>

#### set_frame_range

```python
def set_frame_range(start_frame: int,
                    duration: int,
                    sub_frames: float = 0.000000) -> None
```

x.set_frame_range(start_frame, duration, sub_frames=0.000000) -> None
Set the valid play range for this sequence, determined by a starting frame number (in this sequence player's plaback frame), and a number of frames duration

Args:
    start_frame (int32): The frame number to start playing back the sequence
    duration (int32): The number of frames to play
    sub_frames (float):

<a id="unreal.MovieSceneSequencePlayer.set_disable_camera_cuts"></a>

#### set_disable_camera_cuts

```python
def set_disable_camera_cuts(disable_camera_cuts: bool) -> None
```

x.set_disable_camera_cuts(disable_camera_cuts) -> None
Set whether to disable camera cuts

Args:
    disable_camera_cuts (bool):

<a id="unreal.MovieSceneSequencePlayer.set_completion_mode_override"></a>

#### set_completion_mode_override

```python
def set_completion_mode_override(
        completion_mode_override: MovieSceneCompletionModeOverride) -> None
```

x.set_completion_mode_override(completion_mode_override) -> None
Set the state of the completion mode override. Note, setting the state to force restore state will only take effect if the sequence hasn't started playing

Args:
    completion_mode_override (MovieSceneCompletionModeOverride):

<a id="unreal.MovieSceneSequencePlayer.scrub"></a>

#### scrub

```python
def scrub() -> None
```

x.scrub() -> None
Scrub playback.

<a id="unreal.MovieSceneSequencePlayer.restore_state"></a>

#### restore_state

```python
def restore_state() -> None
```

x.restore_state() -> None
Restore any changes made by this player to their original state

<a id="unreal.MovieSceneSequencePlayer.request_invalidate_binding"></a>

#### request_invalidate_binding

```python
def request_invalidate_binding(
        object_binding: MovieSceneObjectBindingID) -> None
```

x.request_invalidate_binding(object_binding) -> None
Invalidates the given binding, forcing it to be refetched. This may be useful for some custom bindings that wish their resolution code to be called again.

Args:
    object_binding (MovieSceneObjectBindingID):

<a id="unreal.MovieSceneSequencePlayer.remove_weight"></a>

#### remove_weight

```python
def remove_weight() -> None
```

x.remove_weight() -> None
Removes a previously assigned weight

<a id="unreal.MovieSceneSequencePlayer.play_to"></a>

#### play_to

```python
def play_to(playback_params: MovieSceneSequencePlaybackParams,
            play_to_params: MovieSceneSequencePlayToParams) -> None
```

x.play_to(playback_params, play_to_params) -> None
Play from the current position to the requested position and pause. If requested position is before the current position,
playback will be reversed. Playback to the requested position will be cancelled if Stop() or Pause() is invoked during this
playback.

Args:
    playback_params (MovieSceneSequencePlaybackParams): The position settings (ie. the position to play to)
    play_to_params (MovieSceneSequencePlayToParams):

<a id="unreal.MovieSceneSequencePlayer.play_reverse"></a>

#### play_reverse

```python
def play_reverse() -> None
```

x.play_reverse() -> None
Reverse playback.

<a id="unreal.MovieSceneSequencePlayer.play_looping"></a>

#### play_looping

```python
def play_looping(num_loops: int = -1) -> None
```

x.play_looping(num_loops=-1) -> None
Start playback from the current time cursor position, looping the specified number of times.

Args:
    num_loops (int32): The number of loops to play. -1 indicates infinite looping.

<a id="unreal.MovieSceneSequencePlayer.play"></a>

#### play

```python
def play() -> None
```

x.play() -> None
Start playback forwards from the current time cursor position, using the current play rate.

<a id="unreal.MovieSceneSequencePlayer.pause"></a>

#### pause

```python
def pause() -> None
```

x.pause() -> None
Pause playback.

<a id="unreal.MovieSceneSequencePlayer.is_reversed"></a>

#### is_reversed

```python
def is_reversed() -> bool
```

x.is_reversed() -> bool
Check whether playback is reversed.

Returns:
    bool:

<a id="unreal.MovieSceneSequencePlayer.is_playing"></a>

#### is_playing

```python
def is_playing() -> bool
```

x.is_playing() -> bool
Check whether the sequence is actively playing.

Returns:
    bool:

<a id="unreal.MovieSceneSequencePlayer.is_paused"></a>

#### is_paused

```python
def is_paused() -> bool
```

x.is_paused() -> bool
Check whether the sequence is paused.

Returns:
    bool:

<a id="unreal.MovieSceneSequencePlayer.go_to_end_and_stop"></a>

#### go_to_end_and_stop

```python
def go_to_end_and_stop() -> None
```

x.go_to_end_and_stop() -> None
Go to end of the sequence and stop. Adheres to 'When Finished' section rules.

<a id="unreal.MovieSceneSequencePlayer.get_start_time"></a>

#### get_start_time

```python
def get_start_time() -> QualifiedTime
```

x.get_start_time() -> QualifiedTime
Get the offset within the level sequence to start playing

Returns:
    QualifiedTime:

<a id="unreal.MovieSceneSequencePlayer.get_sequence_name"></a>

#### get_sequence_name

```python
def get_sequence_name(add_client_info: bool = False) -> str
```

x.get_sequence_name(add_client_info=False) -> str
Get the name of the sequence this player is playing

Args:
    add_client_info (bool): If true, add client index if running as a client

Returns:
    str: the name of the sequence, or None if no sequence is set

<a id="unreal.MovieSceneSequencePlayer.get_sequence"></a>

#### get_sequence

```python
def get_sequence() -> MovieSceneSequence
```

x.get_sequence() -> MovieSceneSequence
Access the sequence this player is playing

Returns:
    MovieSceneSequence: the sequence currently assigned to this player

<a id="unreal.MovieSceneSequencePlayer.get_play_rate"></a>

#### get_play_rate

```python
def get_play_rate() -> float
```

x.get_play_rate() -> float
Get the playback rate of this player.

Returns:
    float:

<a id="unreal.MovieSceneSequencePlayer.get_object_bindings"></a>

#### get_object_bindings

```python
def get_object_bindings(object: Object) -> Array[MovieSceneObjectBindingID]
```

x.get_object_bindings(object) -> Array[MovieSceneObjectBindingID]
Get the object bindings for the requested object

Args:
    object (Object): 

Returns:
    Array[MovieSceneObjectBindingID]:

<a id="unreal.MovieSceneSequencePlayer.get_hide_hud"></a>

#### get_hide_hud

```python
def get_hide_hud() -> bool
```

x.get_hide_hud() -> bool
Get if the hud is hidden during play.

Returns:
    bool:

<a id="unreal.MovieSceneSequencePlayer.get_frame_rate"></a>

#### get_frame_rate

```python
def get_frame_rate() -> FrameRate
```

x.get_frame_rate() -> FrameRate
Get this sequence's display rate.

Returns:
    FrameRate:

<a id="unreal.MovieSceneSequencePlayer.get_frame_duration"></a>

#### get_frame_duration

```python
def get_frame_duration() -> int
```

x.get_frame_duration() -> int32
Get this sequence's duration in frames

Returns:
    int32:

<a id="unreal.MovieSceneSequencePlayer.get_end_time"></a>

#### get_end_time

```python
def get_end_time() -> QualifiedTime
```

x.get_end_time() -> QualifiedTime
Get the offset within the level sequence to finish playing

Returns:
    QualifiedTime:

<a id="unreal.MovieSceneSequencePlayer.get_duration"></a>

#### get_duration

```python
def get_duration() -> QualifiedTime
```

x.get_duration() -> QualifiedTime
Get the total duration of the sequence

Returns:
    QualifiedTime:

<a id="unreal.MovieSceneSequencePlayer.get_disable_camera_cuts"></a>

#### get_disable_camera_cuts

```python
def get_disable_camera_cuts() -> bool
```

x.get_disable_camera_cuts() -> bool
Set whether to disable camera cuts

Returns:
    bool:

<a id="unreal.MovieSceneSequencePlayer.get_current_time"></a>

#### get_current_time

```python
def get_current_time() -> QualifiedTime
```

x.get_current_time() -> QualifiedTime
Get the current playback position

Returns:
    QualifiedTime: The current playback position

<a id="unreal.MovieSceneSequencePlayer.get_completion_mode_override"></a>

#### get_completion_mode_override

```python
def get_completion_mode_override() -> MovieSceneCompletionModeOverride
```

x.get_completion_mode_override() -> MovieSceneCompletionModeOverride
Get the state of the completion mode override

Returns:
    MovieSceneCompletionModeOverride:

<a id="unreal.MovieSceneSequencePlayer.get_bound_objects"></a>

#### get_bound_objects

```python
def get_bound_objects(
        object_binding: MovieSceneObjectBindingID) -> Array[Object]
```

x.get_bound_objects(object_binding) -> Array[Object]
Retrieve all objects currently bound to the specified binding identifier

Args:
    object_binding (MovieSceneObjectBindingID): 

Returns:
    Array[Object]:

<a id="unreal.MovieSceneSequencePlayer.change_playback_direction"></a>

#### change_playback_direction

```python
def change_playback_direction() -> None
```

x.change_playback_direction() -> None
Changes the direction of playback (go in reverse if it was going forward, or vice versa)

<a id="unreal.MovieSceneBindingLifetimeSection"></a>