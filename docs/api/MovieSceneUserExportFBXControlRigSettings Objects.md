## MovieSceneUserExportFBXControlRigSettings Objects

```python
class MovieSceneUserExportFBXControlRigSettings(Object)
```

Movie Scene User Export FBXControl Rig Settings

**C++ Source:**

- **Module**: MovieSceneTools
- **File**: MovieSceneToolsUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ascii`` (bool):  [Read-Write] If enabled, save as ascii instead of binary
- ``control_channel_mappings`` (Array[ControlToTransformMappings]):  [Read-Write] Mappings for how Control Rig Control Attributes Map to the incoming Transforms
- ``export_file_name`` (str):  [Read-Write] Imported File Name
- ``export_local_time`` (bool):  [Read-Write] If enabled, export sequencer animation in its local time, relative to its sequence.
- ``export_only_selected_controls`` (bool):  [Read-Write] Whether or not import onto selected controls or all controls
- ``fbx_export_compatibility`` (FbxExportCompatibility):  [Read-Write] This will set the fbx sdk compatibility when exporting to fbx file. The default value is 2013
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y

<a id="unreal.MovieSceneUserExportFBXControlRigSettings.fbx_export_compatibility"></a>

#### fbx_export_compatibility

```python
@property
def fbx_export_compatibility() -> FbxExportCompatibility
```

(FbxExportCompatibility):  [Read-Write] This will set the fbx sdk compatibility when exporting to fbx file. The default value is 2013

<a id="unreal.MovieSceneUserExportFBXControlRigSettings.fbx_export_compatibility"></a>

#### fbx_export_compatibility

```python
@fbx_export_compatibility.setter
def fbx_export_compatibility(value: FbxExportCompatibility) -> None
```

<a id="unreal.MovieSceneUserExportFBXControlRigSettings.ascii"></a>

#### ascii

```python
@property
def ascii() -> bool
```

(bool):  [Read-Write] If enabled, save as ascii instead of binary

<a id="unreal.MovieSceneUserExportFBXControlRigSettings.ascii"></a>

#### ascii

```python
@ascii.setter
def ascii(value: bool) -> None
```

<a id="unreal.MovieSceneUserExportFBXControlRigSettings.export_local_time"></a>

#### export_local_time

```python
@property
def export_local_time() -> bool
```

(bool):  [Read-Write] If enabled, export sequencer animation in its local time, relative to its sequence.

<a id="unreal.MovieSceneUserExportFBXControlRigSettings.export_local_time"></a>

#### export_local_time

```python
@export_local_time.setter
def export_local_time(value: bool) -> None
```

<a id="unreal.MovieSceneUserExportFBXControlRigSettings.load_control_mappings_from_preset"></a>

#### load_control_mappings_from_preset

```python
def load_control_mappings_from_preset(meta_human_preset: bool) -> None
```

x.load_control_mappings_from_preset(meta_human_preset) -> None
Load the default or metahuman preset into the current mappings

Args:
    meta_human_preset (bool):

<a id="unreal.AssetExportTask"></a>