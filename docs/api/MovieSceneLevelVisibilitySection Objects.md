## MovieSceneLevelVisibilitySection Objects

```python
class MovieSceneLevelVisibilitySection(MovieSceneSection)
```

A section for use with the movie scene level visibility track, which controls streamed level visibility.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneLevelVisibilitySection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``level_names`` (Array[Name]):  [Read-Write] The short names of the levels who's visibility is controlled by this section.
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)
- ``visibility`` (LevelVisibility):  [Read-Write] Whether or not the levels in this section should be visible or hidden.

<a id="unreal.MovieSceneLevelVisibilitySection.set_visibility"></a>

#### set_visibility

```python
def set_visibility(visibility: LevelVisibility) -> None
```

x.set_visibility(visibility) -> None
Set Visibility

Args:
    visibility (LevelVisibility):

<a id="unreal.MovieSceneLevelVisibilitySection.set_level_names"></a>

#### set_level_names

```python
def set_level_names(level_names: Array[Name]) -> None
```

x.set_level_names(level_names) -> None
Set Level Names

Args:
    level_names (Array[Name]):

<a id="unreal.MovieSceneLevelVisibilitySection.get_visibility"></a>

#### get_visibility

```python
def get_visibility() -> LevelVisibility
```

x.get_visibility() -> LevelVisibility
Get Visibility

Returns:
    LevelVisibility:

<a id="unreal.MovieSceneLevelVisibilitySection.get_level_names"></a>

#### get_level_names

```python
def get_level_names() -> Array[Name]
```

x.get_level_names() -> Array[Name]
Get Level Names

Returns:
    Array[Name]:

<a id="unreal.MovieSceneObjectPropertySection"></a>