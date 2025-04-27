## MovieSceneComposureExportTrack Objects

```python
class MovieSceneComposureExportTrack(MovieSceneTrack)
```

Movie scene track that exports a single pass (either the element's output, or an internal transform pass) during burnouts

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: MovieSceneComposureExportTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``pass_`` (MovieSceneComposureExportPass):  [Read-Write] Configuration options for the pass to export
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneComposureExportSection"></a>