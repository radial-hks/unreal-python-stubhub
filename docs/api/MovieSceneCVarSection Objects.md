## MovieSceneCVarSection Objects

```python
class MovieSceneCVarSection(MovieSceneSection)
```

A CVar section is responsible for applying a user-supplied value to the specified cvar, and then restoring the previous value after the section ends.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneCVarSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``console_variable_collections`` (Array[MovieSceneConsoleVariableCollection]):  [Read-Write] Array of console variable preset assets that this track should operate on
- ``console_variables`` (MovieSceneCVarOverrides):  [Read-Write] The name of the console variable and the value, separated by ' ' or '=', ie: "foo.bar=1" or "foo.bar 1".
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneCVarSection.set_from_string"></a>

#### set_from_string

```python
def set_from_string(string: str) -> None
```

x.set_from_string(string) -> None
Set from String

Args:
    string (str):

<a id="unreal.MovieSceneCVarSection.get_string"></a>

#### get_string

```python
def get_string() -> str
```

x.get_string() -> str
Get String

Returns:
    str:

<a id="unreal.MovieSceneDataLayerSection"></a>