## MovieScene3DConstraintSection Objects

```python
class MovieScene3DConstraintSection(MovieSceneSection)
```

Base class for 3D constraint section

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieScene3DConstraintSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``constraint_binding_id`` (MovieSceneObjectBindingID):  [Read-Write] The constraint binding that this movie Constraint uses
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieScene3DConstraintSection.set_constraint_binding_id"></a>

#### set_constraint_binding_id

```python
def set_constraint_binding_id(
        constraint_binding_id: MovieSceneObjectBindingID) -> None
```

x.set_constraint_binding_id(constraint_binding_id) -> None
Sets the constraint binding for this Constraint section

Args:
    constraint_binding_id (MovieSceneObjectBindingID):

<a id="unreal.MovieScene3DConstraintSection.get_constraint_binding_id"></a>

#### get_constraint_binding_id

```python
def get_constraint_binding_id() -> MovieSceneObjectBindingID
```

x.get_constraint_binding_id() -> MovieSceneObjectBindingID
Gets the constraint binding for this Constraint section

Returns:
    MovieSceneObjectBindingID:

<a id="unreal.MovieScene3DAttachSection"></a>