## BlendSpaceFactoryNew Objects

```python
class BlendSpaceFactoryNew(Factory)
```

Blend Space Factory New

**C++ Source:**

- **Module**: UnrealEd
- **File**: BlendSpaceFactoryNew.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``preview_skeletal_mesh`` (SkeletalMesh):  [Read-Write] The preview mesh to use for the created blendspace
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``target_skeleton`` (Skeleton):  [Read-Write] Target skeleton for the created blendspace
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.BlendSpaceFactoryNew.target_skeleton"></a>

#### target_skeleton

```python
@property
def target_skeleton() -> Skeleton
```

(Skeleton):  [Read-Write] Target skeleton for the created blendspace

<a id="unreal.BlendSpaceFactoryNew.target_skeleton"></a>

#### target_skeleton

```python
@target_skeleton.setter
def target_skeleton(value: Skeleton) -> None
```

<a id="unreal.BlendSpaceFactoryNew.preview_skeletal_mesh"></a>

#### preview_skeletal_mesh

```python
@property
def preview_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write] The preview mesh to use for the created blendspace

<a id="unreal.BlendSpaceFactoryNew.preview_skeletal_mesh"></a>

#### preview_skeletal_mesh

```python
@preview_skeletal_mesh.setter
def preview_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.AimOffsetBlendSpaceFactoryNew"></a>