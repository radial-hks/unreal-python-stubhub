## ControlRigBlueprintFactory Objects

```python
class ControlRigBlueprintFactory(Factory)
```

Control Rig Blueprint Factory

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigBlueprintFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``parent_class`` (type(Class)):  [Read-Write] The parent class of the created blueprint
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.ControlRigBlueprintFactory.create_new_control_rig_asset"></a>

#### create_new_control_rig_asset

```python
@classmethod
def create_new_control_rig_asset(
        cls,
        desired_package_path: str,
        modular_rig: bool = False) -> ControlRigBlueprint
```

X.create_new_control_rig_asset(desired_package_path, modular_rig=False) -> ControlRigBlueprint
Create a new control rig asset within the contents space of the project.

Args:
    desired_package_path (str): The package path to use for the control rig asset
    modular_rig (bool): If true the rig will be created as a modular rig

Returns:
    ControlRigBlueprint:

<a id="unreal.ControlRigBlueprintFactory.create_control_rig_from_skeletal_mesh_or_skeleton"></a>

#### create_control_rig_from_skeletal_mesh_or_skeleton

```python
@classmethod
def create_control_rig_from_skeletal_mesh_or_skeleton(
        cls,
        selected_object: Object,
        modular_rig: bool = False) -> ControlRigBlueprint
```

X.create_control_rig_from_skeletal_mesh_or_skeleton(selected_object, modular_rig=False) -> ControlRigBlueprint
Create a new control rig asset within the contents space of the project
based on a skeletal mesh or skeleton object.

Args:
    selected_object (Object): The SkeletalMesh / Skeleton object to base the control rig asset on
    modular_rig (bool): If true the rig will be created as a modular rig

Returns:
    ControlRigBlueprint:

<a id="unreal.ControlRigShapeLibraryFactory"></a>