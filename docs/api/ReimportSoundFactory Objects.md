## ReimportSoundFactory Objects

```python
class ReimportSoundFactory(SoundFactory)
```

Reimport Sound Factory

**C++ Source:**

- **Module**: AudioEditor
- **File**: ReimportSoundFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``auto_create_cue`` (bool):  [Read-Write] If enabled, a sound cue will automatically be created for the sound
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``cue_package_suffix`` (str):  [Read-Write] If not empty, generated SoundCues will be placed in PackageCuePackageSuffix, but only if bAutoCreateCue is true
- ``cue_volume`` (float):  [Read-Write] The volume of the created sound cue
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``include_attenuation_node`` (bool):  [Read-Write] If enabled, the created sound cue will include a attenuation node
- ``include_looping_node`` (bool):  [Read-Write] If enabled, the created sound cue will include a looping node
- ``include_modulator_node`` (bool):  [Read-Write] If enabled, the created sound cue will include a modulator node
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.NiagaraSystem"></a>