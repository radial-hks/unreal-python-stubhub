## MovieSceneLensComponentSection Objects

```python
class MovieSceneLensComponentSection(MovieSceneHookSection)
```

Movie Scene section for Lens Component

**C++ Source:**

- **Plugin**: LensComponent
- **Module**: LensComponentEditor
- **File**: MovieSceneLensComponentSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_lens_file`` (LensFile):  [Read-Only] Saved duplicate of the LensFile asset used by the recorded Lens Component at the time of recording
- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``override_lens_file`` (LensFile):  [Read-Write] LensFile asset that should be used instead of the cached LensFile during playback
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``reapply_nodal_offset`` (bool):  [Read-Write] If true, then every Update, the nodal offset will be re-evaluated on the lens component
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneLensComponentTrack"></a>