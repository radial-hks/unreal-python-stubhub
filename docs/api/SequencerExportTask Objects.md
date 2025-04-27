## SequencerExportTask Objects

```python
class SequencerExportTask(AssetExportTask)
```

Contains data for a group of assets to import

**C++ Source:**

- **Module**: MovieSceneTools
- **File**: SequencerExportTask.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``automated`` (bool):  [Read-Write] Unattended export
- ``errors`` (Array[str]):  [Read-Write] Array of error messages encountered during exporter
- ``exporter`` (Exporter):  [Read-Write] Optional exporter, otherwise it will be determined automatically
- ``filename`` (str):  [Read-Write] File to export as
- ``ignore_object_list`` (Array[Object]):  [Read-Write] Array of objects to ignore exporting
- ``object`` (Object):  [Read-Write] Asset to export
- ``options`` (Object):  [Read-Write] Exporter specific options
- ``prompt`` (bool):  [Read-Write] Allow dialog prompts
- ``replace_identical`` (bool):  [Read-Write] Replace identical files
- ``selected`` (bool):  [Read-Write] Export selected only
- ``sequencer_context`` (Object):  [Read-Write] A UWorld for LevelSequences, UUserWidget for WidgetAnimations, or AActor for Actor Sequences, etc...
- ``use_file_archive`` (bool):  [Read-Write] Save to a file archive
- ``write_empty_files`` (bool):  [Read-Write] Write even if file empty

<a id="unreal.SequencerExportTask.sequencer_context"></a>

#### sequencer_context

```python
@property
def sequencer_context() -> Object
```

(Object):  [Read-Write] A UWorld for LevelSequences, UUserWidget for WidgetAnimations, or AActor for Actor Sequences, etc...

<a id="unreal.SequencerExportTask.sequencer_context"></a>

#### sequencer_context

```python
@sequencer_context.setter
def sequencer_context(value: Object) -> None
```

<a id="unreal.ContentBrowserAssetContextMenuContext"></a>