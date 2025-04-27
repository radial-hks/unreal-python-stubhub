## LevelSequencePlaybackSettings Objects

```python
class LevelSequencePlaybackSettings(MovieSceneSequencePlaybackSettings)
```

deprecated: 'LevelSequencePlaybackSettings' was renamed to 'MovieSceneSequencePlaybackSettings'.

<a id="unreal.LevelSequencePlaybackSettings.__init__"></a>

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

<a id="unreal.MovieSceneSequenceTickInterval"></a>