## AssetExportTask Objects

```python
class AssetExportTask(Object)
```

Contains data for a group of assets to export

**C++ Source:**

- **Module**: Engine
- **File**: AssetExportTask.h

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
- ``use_file_archive`` (bool):  [Read-Write] Save to a file archive
- ``write_empty_files`` (bool):  [Read-Write] Write even if file empty

<a id="unreal.AssetExportTask.object"></a>

#### object

```python
@property
def object() -> Object
```

(Object):  [Read-Write] Asset to export

<a id="unreal.AssetExportTask.object"></a>

#### object

```python
@object.setter
def object(value: Object) -> None
```

<a id="unreal.AssetExportTask.exporter"></a>

#### exporter

```python
@property
def exporter() -> Exporter
```

(Exporter):  [Read-Write] Optional exporter, otherwise it will be determined automatically

<a id="unreal.AssetExportTask.exporter"></a>

#### exporter

```python
@exporter.setter
def exporter(value: Exporter) -> None
```

<a id="unreal.AssetExportTask.filename"></a>

#### filename

```python
@property
def filename() -> str
```

(str):  [Read-Write] File to export as

<a id="unreal.AssetExportTask.filename"></a>

#### filename

```python
@filename.setter
def filename(value: str) -> None
```

<a id="unreal.AssetExportTask.selected"></a>

#### selected

```python
@property
def selected() -> bool
```

(bool):  [Read-Write] Export selected only

<a id="unreal.AssetExportTask.selected"></a>

#### selected

```python
@selected.setter
def selected(value: bool) -> None
```

<a id="unreal.AssetExportTask.replace_identical"></a>

#### replace_identical

```python
@property
def replace_identical() -> bool
```

(bool):  [Read-Write] Replace identical files

<a id="unreal.AssetExportTask.replace_identical"></a>

#### replace_identical

```python
@replace_identical.setter
def replace_identical(value: bool) -> None
```

<a id="unreal.AssetExportTask.prompt"></a>

#### prompt

```python
@property
def prompt() -> bool
```

(bool):  [Read-Write] Allow dialog prompts

<a id="unreal.AssetExportTask.prompt"></a>

#### prompt

```python
@prompt.setter
def prompt(value: bool) -> None
```

<a id="unreal.AssetExportTask.automated"></a>

#### automated

```python
@property
def automated() -> bool
```

(bool):  [Read-Write] Unattended export

<a id="unreal.AssetExportTask.automated"></a>

#### automated

```python
@automated.setter
def automated(value: bool) -> None
```

<a id="unreal.AssetExportTask.use_file_archive"></a>

#### use_file_archive

```python
@property
def use_file_archive() -> bool
```

(bool):  [Read-Write] Save to a file archive

<a id="unreal.AssetExportTask.use_file_archive"></a>

#### use_file_archive

```python
@use_file_archive.setter
def use_file_archive(value: bool) -> None
```

<a id="unreal.AssetExportTask.write_empty_files"></a>

#### write_empty_files

```python
@property
def write_empty_files() -> bool
```

(bool):  [Read-Write] Write even if file empty

<a id="unreal.AssetExportTask.write_empty_files"></a>

#### write_empty_files

```python
@write_empty_files.setter
def write_empty_files(value: bool) -> None
```

<a id="unreal.AssetExportTask.ignore_object_list"></a>

#### ignore_object_list

```python
@property
def ignore_object_list() -> Array[Object]
```

(Array[Object]):  [Read-Write] Array of objects to ignore exporting

<a id="unreal.AssetExportTask.ignore_object_list"></a>

#### ignore_object_list

```python
@ignore_object_list.setter
def ignore_object_list(value: Array[Object]) -> None
```

<a id="unreal.AssetExportTask.options"></a>

#### options

```python
@property
def options() -> Object
```

(Object):  [Read-Write] Exporter specific options

<a id="unreal.AssetExportTask.options"></a>

#### options

```python
@options.setter
def options(value: Object) -> None
```

<a id="unreal.AssetExportTask.errors"></a>

#### errors

```python
@property
def errors() -> Array[str]
```

(Array[str]):  [Read-Write] Array of error messages encountered during exporter

<a id="unreal.AssetExportTask.errors"></a>

#### errors

```python
@errors.setter
def errors(value: Array[str]) -> None
```

<a id="unreal.SequencerExportTask"></a>