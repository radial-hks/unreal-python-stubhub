## PoseAssetFactory Objects

```python
class PoseAssetFactory(Factory)
```

Pose Asset Factory

**C++ Source:**

- **Module**: UnrealEd
- **File**: PoseAssetFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``pose_names`` (Array[str]):  [Read-Write] Optional. If specified the poses will be named according to this array.
        If you don't specify, or you don't specify enough names for all poses, then default names will be generated.
- ``source_animation`` (AnimSequence):  [Read-Write] Used when creating a composite from an AnimSequence, becomes the only AnimSequence contained
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.PoseAssetFactory.source_animation"></a>

#### source_animation

```python
@property
def source_animation() -> AnimSequence
```

(AnimSequence):  [Read-Write] Used when creating a composite from an AnimSequence, becomes the only AnimSequence contained

<a id="unreal.PoseAssetFactory.source_animation"></a>

#### source_animation

```python
@source_animation.setter
def source_animation(value: AnimSequence) -> None
```

<a id="unreal.PoseAssetFactory.pose_names"></a>

#### pose_names

```python
@property
def pose_names() -> Array[str]
```

(Array[str]):  [Read-Write] Optional. If specified the poses will be named according to this array.
      If you don't specify, or you don't specify enough names for all poses, then default names will be generated.

<a id="unreal.PoseAssetFactory.pose_names"></a>

#### pose_names

```python
@pose_names.setter
def pose_names(value: Array[str]) -> None
```

<a id="unreal.MaterialInterface"></a>