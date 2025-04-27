## MovieSceneEventTrackExtensions Objects

```python
class MovieSceneEventTrackExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieSceneEventTrack for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneEventTrackExtensions.h

<a id="unreal.MovieSceneEventTrackExtensions.get_bound_object_property_class"></a>

#### get_bound_object_property_class

```python
@classmethod
def get_bound_object_property_class(cls, event_key: MovieSceneEvent) -> Class
```

X.get_bound_object_property_class(event_key) -> type(Class)
* Return the class of the bound object property
*
*

Args:
    event_key (MovieSceneEvent): The event key to get the bound object property from *

Returns:
    type(Class): The class of the bound object property

<a id="unreal.MovieSceneEventTrackExtensions.add_event_trigger_section"></a>

#### add_event_trigger_section

```python
@classmethod
def add_event_trigger_section(
        cls, track: MovieSceneEventTrack) -> MovieSceneEventTriggerSection
```

X.add_event_trigger_section(track) -> MovieSceneEventTriggerSection
Create a new event trigger section for the given track

Args:
    track (MovieSceneEventTrack): 

Returns:
    MovieSceneEventTriggerSection: The newly created event trigger section

<a id="unreal.MovieSceneEventTrackExtensions.add_event_repeater_section"></a>

#### add_event_repeater_section

```python
@classmethod
def add_event_repeater_section(
        cls, track: MovieSceneEventTrack) -> MovieSceneEventRepeaterSection
```

X.add_event_repeater_section(track) -> MovieSceneEventRepeaterSection
Create a new event repeater section for the given track

Args:
    track (MovieSceneEventTrack): 

Returns:
    MovieSceneEventRepeaterSection: The newly created event repeater section

<a id="unreal.MovieSceneFolderExtensions"></a>