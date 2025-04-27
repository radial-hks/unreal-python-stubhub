## AnimLayerInterfaceFactory Objects

```python
class AnimLayerInterfaceFactory(AnimBlueprintFactory)
```

Anim Layer Interface Factory

**C++ Source:**

- **Module**: UnrealEd
- **File**: AnimBlueprintFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``blueprint_type`` (BlueprintType):  [Read-Write] The type of blueprint that will be created
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``parent_class`` (type(Class)):  [Read-Write] The parent class of the created blueprint
- ``preview_skeletal_mesh`` (SkeletalMesh):  [Read-Write] The preview mesh to use with this animation blueprint
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``target_skeleton`` (Skeleton):  [Read-Write] The kind of skeleton that animation graphs compiled from the blueprint will animate
- ``template`` (bool):  [Read-Write] Whether the created blueprint should be a template with no target skeleton
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.AnimBoneCompressionSettingsFactory"></a>