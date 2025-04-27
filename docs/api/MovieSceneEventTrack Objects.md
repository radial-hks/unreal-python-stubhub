## MovieSceneEventTrack Objects

```python
class MovieSceneEventTrack(MovieSceneNameableTrack)
```

Implements a movie scene track that triggers discrete events during playback.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneEventTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``event_position`` (FireEventsAtPosition):  [Read-Write] Defines where in the evaluation to trigger events
- ``fire_events_when_backwards`` (bool):  [Read-Write] If events should be fired when passed playing the sequence backwards.
- ``fire_events_when_forwards`` (bool):  [Read-Write] If events should be fired when passed playing the sequence forwards.
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneEventTrack.add_event_trigger_section"></a>

#### add_event_trigger_section

```python
def add_event_trigger_section() -> MovieSceneEventTriggerSection
```

x.add_event_trigger_section() -> MovieSceneEventTriggerSection
Create a new event trigger section for the given track

Returns:
    MovieSceneEventTriggerSection: The newly created event trigger section

<a id="unreal.MovieSceneEventTrack.add_event_repeater_section"></a>

#### add_event_repeater_section

```python
def add_event_repeater_section() -> MovieSceneEventRepeaterSection
```

x.add_event_repeater_section() -> MovieSceneEventRepeaterSection
Create a new event repeater section for the given track

Returns:
    MovieSceneEventRepeaterSection: The newly created event repeater section

<a id="unreal.MovieSceneFloatTrack"></a>