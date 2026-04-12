## MovieSceneGameplayCueTrack Objects

```python
class MovieSceneGameplayCueTrack(MovieSceneNameableTrack)
```

Implements a movie scene track that triggers gameplay cues

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: MovieSceneGameplayCueTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneGameplayCueTrack.set_sequencer_track_handler"></a>

#### set\_sequencer\_track\_handler

```python
@classmethod
def set_sequencer_track_handler(
        cls, gameplay_cue_track_handler: MovieSceneGameplayCueEvent) -> None
```

X.set_sequencer_track_handler(gameplay_cue_track_handler) -> None
Override the default function for invoking Gameplay Cues from sequencer tracks

Args:
    gameplay_cue_track_handler (MovieSceneGameplayCueEvent):

<a id="unreal.GameplayAbilitiesBlueprintFactory"></a>