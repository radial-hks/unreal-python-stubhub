## AnimMontageFactory Objects

```python
class AnimMontageFactory(Factory)
```

Anim Montage Factory

**C++ Source:**

- **Module**: UnrealEd
- **File**: AnimMontageFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``source_animation`` (AnimSequence):  [Read-Write] Used when creating a montage from an AnimSequence, becomes the only AnimSequence contained
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``target_skeleton`` (Skeleton):  [Read-Write]
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.AnimMontageFactory.target_skeleton"></a>

#### target_skeleton

```python
@property
def target_skeleton() -> Skeleton
```

(Skeleton):  [Read-Write]

<a id="unreal.AnimMontageFactory.target_skeleton"></a>

#### target_skeleton

```python
@target_skeleton.setter
def target_skeleton(value: Skeleton) -> None
```

<a id="unreal.AnimMontageFactory.source_animation"></a>

#### source_animation

```python
@property
def source_animation() -> AnimSequence
```

(AnimSequence):  [Read-Write] Used when creating a montage from an AnimSequence, becomes the only AnimSequence contained

<a id="unreal.AnimMontageFactory.source_animation"></a>

#### source_animation

```python
@source_animation.setter
def source_animation(value: AnimSequence) -> None
```

<a id="unreal.AnimSeqExportOption"></a>