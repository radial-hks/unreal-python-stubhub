## MovieSceneUserImportFBXSettings Objects

```python
class MovieSceneUserImportFBXSettings(Object)
```

Movie Scene User Import FBXSettings

**C++ Source:**

- **Module**: MovieSceneTools
- **File**: MovieSceneToolsUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``convert_scene_unit`` (bool):  [Read-Write] Convert the scene from FBX unit to UE unit(centimeter)
- ``create_cameras`` (bool):  [Read-Write] Whether to create cameras if they don't already exist in the level.
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y
- ``import_uniform_scale`` (float):  [Read-Write] Import Uniform Scale
- ``match_by_name_only`` (bool):  [Read-Write] Match fbx node names to sequencer node names
- ``reduce_keys`` (bool):  [Read-Write] Whether to remove keyframes within a tolerance from the imported tracks
- ``reduce_keys_tolerance`` (float):  [Read-Write] The tolerance for reduce keys
- ``replace_transform_track`` (bool):  [Read-Write] Whether to replace the existing transform track or create a new track/section

<a id="unreal.MovieSceneUserImportFBXControlRigSettings"></a>