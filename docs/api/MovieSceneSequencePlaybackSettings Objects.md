## MovieSceneSequencePlaybackSettings Objects

```python
class MovieSceneSequencePlaybackSettings(StructBase)
```

Settings for the level sequence player actor.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSequencePlaybackSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_play`` (bool):  [Read-Write] Auto-play the sequence when created
- ``disable_camera_cuts`` (bool):  [Read-Write] Disable camera cuts
- ``disable_look_at_input`` (bool):  [Read-Write] Disable LookAt Input from player during play
- ``disable_movement_input`` (bool):  [Read-Write] Disable Input from player during play
- ``dynamic_weighting`` (bool):  [Read-Write] Whether to enable dynamic weighting on this player or not
- ``finish_completion_state_override`` (MovieSceneCompletionModeOverride):  [Read-Write] If set to something other than none, when a sequence ends, the completion mode of any track sections still active will be overridden
        * by the chosen value, either keep state or restore state. Otherwise, completion mode will be determined by each track section.
        * Note that any track sections that finish before the end of a sequence will have their completion mode determined by the section settings rather than this override.
- ``hide_hud`` (bool):  [Read-Write] Hide HUD during play
- ``hide_player`` (bool):  [Read-Write] Hide Player Pawn during play
- ``inherit_tick_interval_from_owner`` (bool):  [Read-Write] When checked, a custom tick interval can be provided to define how often to update this sequence
- ``loop_count`` (MovieSceneSequenceLoopCount):  [Read-Write] Number of times to loop playback. -1 for infinite, else the number of times to loop before stopping
- ``pause_at_end`` (bool):  [Read-Write] Pause the sequence when playback reaches the end rather than stopping it
- ``play_rate`` (float):  [Read-Write] The rate at which to playback the animation
- ``random_start_time`` (bool):  [Read-Write] Start playback at a random time
- ``restore_state`` (bool):  [Read-Write] Flag used to specify whether actor states should be restored on stop.
  This has been deprecated in favor of FinishCompletionStateOverride.
  deprecated: Use Settings.FinishCompletionStateOverride instead
- ``start_time`` (float):  [Read-Write] Start playback at the specified offset from the start of the sequence's playback range
- ``tick_interval`` (MovieSceneSequenceTickInterval):  [Read-Write] Overridable tick interval for this sequence to update at. When not overridden, the owning actor or component's tick interval will be used

<a id="unreal.MovieSceneSequencePlaybackSettings.__init__"></a>

#### __init__

```python
def __init__(
        auto_play: bool = False,
        loop_count: MovieSceneSequenceLoopCount = [0],
        tick_interval: MovieSceneSequenceTickInterval = [
            0.000000, 0.000000, False, True
        ],
        play_rate: float = 0.000000,
        start_time: float = 0.000000,
        random_start_time: bool = False,
        disable_movement_input: bool = False,
        disable_look_at_input: bool = False,
        hide_player: bool = False,
        hide_hud: bool = False,
        disable_camera_cuts: bool = False,
        finish_completion_state_override:
    MovieSceneCompletionModeOverride = MovieSceneCompletionModeOverride.NONE,
        pause_at_end: bool = False) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.auto_play"></a>

#### auto_play

```python
@property
def auto_play() -> bool
```

(bool):  [Read-Write] Auto-play the sequence when created

<a id="unreal.MovieSceneSequencePlaybackSettings.auto_play"></a>

#### auto_play

```python
@auto_play.setter
def auto_play(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.loop_count"></a>

#### loop_count

```python
@property
def loop_count() -> MovieSceneSequenceLoopCount
```

(MovieSceneSequenceLoopCount):  [Read-Write] Number of times to loop playback. -1 for infinite, else the number of times to loop before stopping

<a id="unreal.MovieSceneSequencePlaybackSettings.loop_count"></a>

#### loop_count

```python
@loop_count.setter
def loop_count(value: MovieSceneSequenceLoopCount) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.tick_interval"></a>

#### tick_interval

```python
@property
def tick_interval() -> MovieSceneSequenceTickInterval
```

(MovieSceneSequenceTickInterval):  [Read-Write] Overridable tick interval for this sequence to update at. When not overridden, the owning actor or component's tick interval will be used

<a id="unreal.MovieSceneSequencePlaybackSettings.tick_interval"></a>

#### tick_interval

```python
@tick_interval.setter
def tick_interval(value: MovieSceneSequenceTickInterval) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.play_rate"></a>

#### play_rate

```python
@property
def play_rate() -> float
```

(float):  [Read-Write] The rate at which to playback the animation

<a id="unreal.MovieSceneSequencePlaybackSettings.play_rate"></a>

#### play_rate

```python
@play_rate.setter
def play_rate(value: float) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.start_time"></a>

#### start_time

```python
@property
def start_time() -> float
```

(float):  [Read-Write] Start playback at the specified offset from the start of the sequence's playback range

<a id="unreal.MovieSceneSequencePlaybackSettings.start_time"></a>

#### start_time

```python
@start_time.setter
def start_time(value: float) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.random_start_time"></a>

#### random_start_time

```python
@property
def random_start_time() -> bool
```

(bool):  [Read-Write] Start playback at a random time

<a id="unreal.MovieSceneSequencePlaybackSettings.random_start_time"></a>

#### random_start_time

```python
@random_start_time.setter
def random_start_time(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.restore_state"></a>

#### restore_state

```python
@property
def restore_state() -> bool
```

(bool):  [Read-Write] Flag used to specify whether actor states should be restored on stop.
This has been deprecated in favor of FinishCompletionStateOverride.
deprecated: Use Settings.FinishCompletionStateOverride instead

<a id="unreal.MovieSceneSequencePlaybackSettings.restore_state"></a>

#### restore_state

```python
@restore_state.setter
def restore_state(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.disable_movement_input"></a>

#### disable_movement_input

```python
@property
def disable_movement_input() -> bool
```

(bool):  [Read-Write] Disable Input from player during play

<a id="unreal.MovieSceneSequencePlaybackSettings.disable_movement_input"></a>

#### disable_movement_input

```python
@disable_movement_input.setter
def disable_movement_input(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.disable_look_at_input"></a>

#### disable_look_at_input

```python
@property
def disable_look_at_input() -> bool
```

(bool):  [Read-Write] Disable LookAt Input from player during play

<a id="unreal.MovieSceneSequencePlaybackSettings.disable_look_at_input"></a>

#### disable_look_at_input

```python
@disable_look_at_input.setter
def disable_look_at_input(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.hide_player"></a>

#### hide_player

```python
@property
def hide_player() -> bool
```

(bool):  [Read-Write] Hide Player Pawn during play

<a id="unreal.MovieSceneSequencePlaybackSettings.hide_player"></a>

#### hide_player

```python
@hide_player.setter
def hide_player(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.hide_hud"></a>

#### hide_hud

```python
@property
def hide_hud() -> bool
```

(bool):  [Read-Write] Hide HUD during play

<a id="unreal.MovieSceneSequencePlaybackSettings.hide_hud"></a>

#### hide_hud

```python
@hide_hud.setter
def hide_hud(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.disable_camera_cuts"></a>

#### disable_camera_cuts

```python
@property
def disable_camera_cuts() -> bool
```

(bool):  [Read-Write] Disable camera cuts

<a id="unreal.MovieSceneSequencePlaybackSettings.disable_camera_cuts"></a>

#### disable_camera_cuts

```python
@disable_camera_cuts.setter
def disable_camera_cuts(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.finish_completion_state_override"></a>

#### finish_completion_state_override

```python
@property
def finish_completion_state_override() -> MovieSceneCompletionModeOverride
```

(MovieSceneCompletionModeOverride):  [Read-Write] If set to something other than none, when a sequence ends, the completion mode of any track sections still active will be overridden
      * by the chosen value, either keep state or restore state. Otherwise, completion mode will be determined by each track section.
      * Note that any track sections that finish before the end of a sequence will have their completion mode determined by the section settings rather than this override.

<a id="unreal.MovieSceneSequencePlaybackSettings.finish_completion_state_override"></a>

#### finish_completion_state_override

```python
@finish_completion_state_override.setter
def finish_completion_state_override(
        value: MovieSceneCompletionModeOverride) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings.pause_at_end"></a>

#### pause_at_end

```python
@property
def pause_at_end() -> bool
```

(bool):  [Read-Write] Pause the sequence when playback reaches the end rather than stopping it

<a id="unreal.MovieSceneSequencePlaybackSettings.pause_at_end"></a>

#### pause_at_end

```python
@pause_at_end.setter
def pause_at_end(value: bool) -> None
```

<a id="unreal.LevelSequencePlaybackSettings"></a>