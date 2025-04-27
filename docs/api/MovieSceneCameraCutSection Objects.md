## MovieSceneCameraCutSection Objects

```python
class MovieSceneCameraCutSection(MovieSceneSection)
```

Movie CameraCuts are sections on the CameraCuts track, that show what the viewer "sees"

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneCameraCutSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_binding_id`` (MovieSceneObjectBindingID):  [Read-Write] The camera binding that this movie CameraCut uses
- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``lock_previous_camera`` (bool):  [Read-Write] When blending, lock the previous camera (camera cut or gameplay camera).
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneCameraCutSection.set_camera_binding_id"></a>

#### set_camera_binding_id

```python
def set_camera_binding_id(
        camera_binding_id: MovieSceneObjectBindingID) -> None
```

x.set_camera_binding_id(camera_binding_id) -> None
Sets the camera binding for this CameraCut section

Args:
    camera_binding_id (MovieSceneObjectBindingID):

<a id="unreal.MovieSceneCameraCutSection.get_camera_binding_id"></a>

#### get_camera_binding_id

```python
def get_camera_binding_id() -> MovieSceneObjectBindingID
```

x.get_camera_binding_id() -> MovieSceneObjectBindingID
Gets the camera binding for this CameraCut section

Returns:
    MovieSceneObjectBindingID:

<a id="unreal.MovieSceneShotSection"></a>