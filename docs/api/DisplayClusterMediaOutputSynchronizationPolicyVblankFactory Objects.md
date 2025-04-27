## DisplayClusterMediaOutputSynchronizationPolicyVblankFactory Objects

```python
class DisplayClusterMediaOutputSynchronizationPolicyVblankFactory(Factory)
```

Factory for UDisplayClusterMediaSynchronizationPolicyVblank objects.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterMediaEditor
- **File**: DisplayClusterMediaOutputSynchronizationPolicyFactories.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.SharedMemoryMediaOutputFactory"></a>