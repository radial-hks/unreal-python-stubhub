## MovieSceneTrackEvalOptions Objects

```python
class MovieSceneTrackEvalOptions(StructBase)
```

Generic evaluation options for any track

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eval_nearest_section`` (bool):  [Read-Write] When evaluating empty space on a track, will evaluate the last position of the previous section (if possible), or the first position of the next section, in that order of preference.
- ``evaluate_in_postroll`` (bool):  [Read-Write] Evaluate this track as part of its parent sub-section's post-roll, if applicable
- ``evaluate_in_preroll`` (bool):  [Read-Write] Evaluate this track as part of its parent sub-section's pre-roll, if applicable

<a id="unreal.MovieSceneTrackEvalOptions.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MovieSceneTrackDisplayOptions"></a>