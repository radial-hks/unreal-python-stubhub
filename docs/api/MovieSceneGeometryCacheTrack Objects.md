## MovieSceneGeometryCacheTrack Objects

```python
class MovieSceneGeometryCacheTrack(MovieSceneNameableTrack)
```

Movie Scene Geometry Cache Track

**C++ Source:**

- **Plugin**: GeometryCache
- **Module**: GeometryCacheTracks
- **File**: MovieSceneGeometryCacheTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.GeometryCacheStreamerSettings"></a>