## MovieScene3DTransformSection Objects

```python
class MovieScene3DTransformSection(MovieSceneSection)
```

A 3D transform section

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieScene3DTransformSection.h

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
- ``show3d_trajectory`` (Show3DTrajectory):  [Read-Write] Whether to show the 3d trajectory
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)
- ``use_quaternion_interpolation`` (bool):  [Read-Write] Whether to use a quaternion linear interpolation between keys. This finds the 'shortest' rotation between keyed orientations.

<a id="unreal.MovieSceneActorReferenceSection"></a>