## MovieSceneUserImportFBXControlRigSettings Objects

```python
class MovieSceneUserImportFBXControlRigSettings(Object)
```

Movie Scene User Import FBXControl Rig Settings

**C++ Source:**

- **Module**: MovieSceneTools
- **File**: MovieSceneToolsUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_channel_mappings`` (Array[ControlToTransformMappings]):  [Read-Write] Mappings for how Control Rig Control Attributes Map to the incoming Transforms
- ``convert_scene_unit`` (bool):  [Read-Write] Convert the scene from FBX unit to UE unit(centimeter)
- ``end_time_range`` (FrameNumber):  [Read-Write] End Time Range To Import
- ``find_and_replace_strings`` (Array[ControlFindReplaceString]):  [Read-Write] Strings In Imported Node To Find And Replace
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y
- ``import_onto_selected_controls`` (bool):  [Read-Write] Whether or not import onto selected controls or all controls
- ``import_uniform_scale`` (float):  [Read-Write] Import Uniform Scale
- ``imported_end_time`` (FrameNumber):  [Read-Only] Imported File
- ``imported_file_name`` (str):  [Read-Only] Imported File Name
- ``imported_frame_rate`` (str):  [Read-Only] Incoming File Frame Rate
- ``imported_node_names`` (Array[str]):  [Read-Only] List Of Imported Names in FBX File
- ``imported_start_time`` (FrameNumber):  [Read-Only] Imported File Duration in Seconds
- ``insert_animation`` (bool):  [Read-Write] Whether or not we insert or replace, by default we insert
- ``specify_time_range`` (bool):  [Read-Write] Whether to import over specific Time Range
- ``start_time_range`` (FrameNumber):  [Read-Write] Start Time Range To Import
- ``strip_namespace`` (bool):  [Read-Write] Will strip any namespace from the FBX node names
- ``time_to_insert_or_replace_animation`` (FrameNumber):  [Read-Write] Time that we insert or replace the imported animation

<a id="unreal.MovieSceneUserImportFBXControlRigSettings.load_control_mappings_from_preset"></a>

#### load_control_mappings_from_preset

```python
def load_control_mappings_from_preset(meta_human_preset: bool) -> None
```

x.load_control_mappings_from_preset(meta_human_preset) -> None
Load the default or metahuman preset into the current mappings

Args:
    meta_human_preset (bool):

<a id="unreal.MovieSceneUserExportFBXControlRigSettings"></a>