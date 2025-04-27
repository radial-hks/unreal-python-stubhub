## MovieSceneCinematicShotSection Objects

```python
class MovieSceneCinematicShotSection(MovieSceneSubSection)
```

Implements a cinematic shot section.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneCinematicShotSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``network_mask`` (uint8):  [Read-Write]
- ``parameters`` (MovieSceneSectionParameters):  [Read-Write]
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``sub_sequence`` (MovieSceneSequence):  [Read-Write] Movie scene being played by this section
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneCinematicShotSection.set_shot_display_name"></a>

#### set_shot_display_name

```python
def set_shot_display_name(shot_display_name: str) -> None
```

x.set_shot_display_name(shot_display_name) -> None
Set the shot display name

Args:
    shot_display_name (str):

<a id="unreal.MovieSceneCinematicShotSection.get_shot_display_name"></a>

#### get_shot_display_name

```python
def get_shot_display_name() -> str
```

x.get_shot_display_name() -> str


Returns:
    str: The shot display name. if empty, returns the sequence's name

<a id="unreal.MovieSceneColorSection"></a>