## MovieSceneComposureExportSection Objects

```python
class MovieSceneComposureExportSection(MovieSceneSection)
```

Movie Scene Composure Export Section

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: MovieSceneComposureExportTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneComposurePostMoveSettingsSection"></a>