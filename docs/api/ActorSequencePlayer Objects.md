## ActorSequencePlayer Objects

```python
class ActorSequencePlayer(MovieSceneSequencePlayer)
```

UActorSequencePlayer is used to actually "play" an actor sequence asset at runtime.

**C++ Source:**

- **Plugin**: ActorSequence
- **Module**: ActorSequence
- **File**: ActorSequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_finished`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player finishes naturally (without explicitly calling stop)
- ``on_pause`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is paused
- ``on_play`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played
- ``on_play_reverse`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played in reverse
- ``on_stop`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is stopped

<a id="unreal.PaperCharacter"></a>