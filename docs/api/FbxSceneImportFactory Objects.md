## FbxSceneImportFactory Objects

```python
class FbxSceneImportFactory(SceneImportFactory)
```

Fbx Scene Import Factory

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxSceneImportFactory.h

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

<a id="unreal.FbxSceneImportFactory.scene_import_options"></a>

#### scene_import_options

```python
@property
def scene_import_options() -> FbxSceneImportOptions
```

(FbxSceneImportOptions):  [Read-Write] Import options UI detail when importing fbx scene

<a id="unreal.FbxSceneImportFactory.scene_import_options"></a>

#### scene_import_options

```python
@scene_import_options.setter
def scene_import_options(value: FbxSceneImportOptions) -> None
```

<a id="unreal.FbxSceneImportFactory.scene_import_options_static_mesh"></a>

#### scene_import_options_static_mesh

```python
@property
def scene_import_options_static_mesh() -> FbxSceneImportOptionsStaticMesh
```

(FbxSceneImportOptionsStaticMesh):  [Read-Write] Import options UI detail when importing fbx scene static mesh

<a id="unreal.FbxSceneImportFactory.scene_import_options_static_mesh"></a>

#### scene_import_options_static_mesh

```python
@scene_import_options_static_mesh.setter
def scene_import_options_static_mesh(
        value: FbxSceneImportOptionsStaticMesh) -> None
```

<a id="unreal.FbxSceneImportFactory.scene_import_options_skeletal_mesh"></a>

#### scene_import_options_skeletal_mesh

```python
@property
def scene_import_options_skeletal_mesh() -> FbxSceneImportOptionsSkeletalMesh
```

(FbxSceneImportOptionsSkeletalMesh):  [Read-Write] Import options UI detail when importing fbx scene skeletal mesh

<a id="unreal.FbxSceneImportFactory.scene_import_options_skeletal_mesh"></a>

#### scene_import_options_skeletal_mesh

```python
@scene_import_options_skeletal_mesh.setter
def scene_import_options_skeletal_mesh(
        value: FbxSceneImportOptionsSkeletalMesh) -> None
```

<a id="unreal.FbxSceneImportOptions"></a>