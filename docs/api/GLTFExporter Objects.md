## GLTFExporter Objects

```python
class GLTFExporter(Exporter)
```

GLTFExporter

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFExporter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``export_task`` (AssetExportTask):  [Read-Write]
- ``format_description`` (Array[str]):  [Read-Write] Descriptiong of the export format
- ``format_extension`` (Array[str]):  [Read-Write] File extension to use for this exporter
- ``supported_class`` (type(Class)):  [Read-Write] Supported class of this exporter
- ``text`` (bool):  [Read-Write] If true, this will export the data as text

<a id="unreal.GLTFExporter.export_to_gltf"></a>

#### export_to_gltf

```python
@classmethod
def export_to_gltf(
        cls, object: Object, file_path: str, options: GLTFExportOptions,
        selected_actors: Set[Actor]) -> Optional[GLTFExportMessages]
```

X.export_to_gltf(object, file_path, options, selected_actors) -> GLTFExportMessages or None
Export the specified object to a glTF file (.gltf or .glb)

Args:
    object (Object): The object to export (supported types are UMaterialInterface, UStaticMesh, USkeletalMesh, UWorld, UAnimSequence, ULevelSequence, ULevelVariantSets). Will default to the currently active world if null.
    file_path (str): The filename on disk to save as. Associated textures and binary files will be saved in the same folder, unless file extension is .glb - which results in a self-contained binary file.
    options (GLTFExportOptions): The various options to use during export. Will default to the project's user-specific editor settings if null.
    selected_actors (Set[Actor]): The set of actors to export, only applicable if the object to export is a UWorld. An empty set results in the export of all actors.

Returns:
    GLTFExportMessages or None: true if the object was successfully exported

    out_messages (GLTFExportMessages): The resulting log messages from the export.

<a id="unreal.GLTFAnimSequenceExporter"></a>