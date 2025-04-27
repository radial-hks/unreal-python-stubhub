## ReimportFbxSceneFactory Objects

```python
class ReimportFbxSceneFactory(FbxSceneImportFactory)
```

Reimport Fbx Scene Factory

**C++ Source:**

- **Module**: UnrealEd
- **File**: ReimportFbxSceneFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``scene_import_options`` (FbxSceneImportOptions):  [Read-Write] Import options UI detail when importing fbx scene
- ``scene_import_options_skeletal_mesh`` (FbxSceneImportOptionsSkeletalMesh):  [Read-Write] Import options UI detail when importing fbx scene skeletal mesh
- ``scene_import_options_static_mesh`` (FbxSceneImportOptionsStaticMesh):  [Read-Write] Import options UI detail when importing fbx scene static mesh
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.ReimportFbxSceneFactory.script_reimport_helper"></a>

#### script_reimport_helper

```python
def script_reimport_helper(obj: Object) -> None
```

x.script_reimport_helper(obj) -> None
Script helper to allow fbx scene reimport from scripted language
       *

Args:
    obj (Object):

<a id="unreal.ReimportFbxSkeletalMeshFactory"></a>