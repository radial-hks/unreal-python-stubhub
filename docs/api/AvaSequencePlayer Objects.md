## AvaSequencePlayer Objects

```python
class AvaSequencePlayer(LevelSequencePlayer)
```

Ava Sequence Player

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaSequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_camera_cut`` (OnLevelSequencePlayerCameraCutEvent):  [Read-Write] Event triggered when there is a camera cut
- ``on_finished`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player finishes naturally (without explicitly calling stop)
- ``on_pause`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is paused
- ``on_play`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played
- ``on_play_reverse`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played in reverse
- ``on_stop`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is stopped

<a id="unreal.AvaCineCameraActor"></a>