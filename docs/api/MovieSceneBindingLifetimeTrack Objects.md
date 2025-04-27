## MovieSceneBindingLifetimeTrack Objects

```python
class MovieSceneBindingLifetimeTrack(MovieSceneTrack)
```

Handles when an object binding should be activated/deactivated

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneBindingLifetimeTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneSpawnTrack"></a>