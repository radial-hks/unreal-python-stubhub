## TileSheetPaddingFactory Objects

```python
class TileSheetPaddingFactory(Factory)
```

Factory used to pad out each individual tile in a tile sheet texture

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2DEditor
- **File**: TileSheetPaddingFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``extrusion_amount`` (int32):  [Read-Write] The amount to extrude out from each tile (in pixels)
- ``fill_with_transparent_black`` (bool):  [Read-Write] Should we use transparent black or white when filling the texture areas that aren't covered by tiles?
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``pad_to_power_of2`` (bool):  [Read-Write] Should we pad the texture to the next power of 2?
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.

<a id="unreal.PaperSpriteSheet"></a>