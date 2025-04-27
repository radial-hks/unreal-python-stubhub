## LevelSequencePlayer Objects

```python
class LevelSequencePlayer(MovieSceneSequencePlayer)
```

ULevelSequencePlayer is used to actually "play" an level sequence asset at runtime.

This class keeps track of playback state and provides functions for manipulating
an level sequence while its playing.

**C++ Source:**

- **Module**: LevelSequence
- **File**: LevelSequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_camera_cut`` (OnLevelSequencePlayerCameraCutEvent):  [Read-Write] Event triggered when there is a camera cut
- ``on_finished`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player finishes naturally (without explicitly calling stop)
- ``on_pause`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is paused
- ``on_play`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played
- ``on_play_reverse`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played in reverse
- ``on_stop`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is stopped

<a id="unreal.LevelSequencePlayer.on_camera_cut"></a>

#### on_camera_cut

```python
@property
def on_camera_cut() -> OnLevelSequencePlayerCameraCutEvent
```

(OnLevelSequencePlayerCameraCutEvent):  [Read-Write] Event triggered when there is a camera cut

<a id="unreal.LevelSequencePlayer.on_camera_cut"></a>

#### on_camera_cut

```python
@on_camera_cut.setter
def on_camera_cut(value: OnLevelSequencePlayerCameraCutEvent) -> None
```

<a id="unreal.LevelSequencePlayer.get_active_camera_component"></a>

#### get_active_camera_component

```python
def get_active_camera_component() -> CameraComponent
```

x.get_active_camera_component() -> CameraComponent
Get the active camera cut camera

Returns:
    CameraComponent:

<a id="unreal.LevelSequencePlayer.create_level_sequence_player"></a>

#### create_level_sequence_player

```python
@classmethod
def create_level_sequence_player(
    cls, world_context_object: Object, level_sequence: LevelSequence,
    settings: MovieSceneSequencePlaybackSettings
) -> Tuple[LevelSequencePlayer, LevelSequenceActor]
```

X.create_level_sequence_player(world_context_object, level_sequence, settings) -> (LevelSequencePlayer, out_actor=LevelSequenceActor)
Create a new level sequence player.

Args:
    world_context_object (Object): Context object from which to retrieve a UWorld.
    level_sequence (LevelSequence): The level sequence to play.
    settings (MovieSceneSequencePlaybackSettings): The desired playback settings

Returns:
    LevelSequenceActor: 

    out_actor (LevelSequenceActor): The level sequence actor created to play this sequence.

<a id="unreal.LevelSequenceMediaController"></a>