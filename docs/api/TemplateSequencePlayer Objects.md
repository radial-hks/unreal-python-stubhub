## TemplateSequencePlayer Objects

```python
class TemplateSequencePlayer(MovieSceneSequencePlayer)
```

Template Sequence Player

**C++ Source:**

- **Plugin**: TemplateSequence
- **Module**: TemplateSequence
- **File**: TemplateSequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_finished`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player finishes naturally (without explicitly calling stop)
- ``on_pause`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is paused
- ``on_play`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played
- ``on_play_reverse`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is played in reverse
- ``on_stop`` (OnMovieSceneSequencePlayerEvent):  [Read-Write] Event triggered when the level sequence player is stopped

<a id="unreal.TemplateSequencePlayer.create_template_sequence_player"></a>

#### create_template_sequence_player

```python
@classmethod
def create_template_sequence_player(
    cls, world_context_object: Object, template_sequence: TemplateSequence,
    settings: MovieSceneSequencePlaybackSettings
) -> Tuple[TemplateSequencePlayer, TemplateSequenceActor]
```

X.create_template_sequence_player(world_context_object, template_sequence, settings) -> (TemplateSequencePlayer, out_actor=TemplateSequenceActor)
Create Template Sequence Player

Args:
    world_context_object (Object): 
    template_sequence (TemplateSequence): 
    settings (MovieSceneSequencePlaybackSettings): 

Returns:
    TemplateSequenceActor: 

    out_actor (TemplateSequenceActor):

<a id="unreal.SequenceCameraShakeTestUtil"></a>