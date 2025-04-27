## Exporter Objects

```python
class Exporter(Object)
```

Exporter

**C++ Source:**

- **Module**: Engine
- **File**: Exporter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``export_task`` (AssetExportTask):  [Read-Write]
- ``format_description`` (Array[str]):  [Read-Write] Descriptiong of the export format
- ``format_extension`` (Array[str]):  [Read-Write] File extension to use for this exporter
- ``supported_class`` (type(Class)):  [Read-Write] Supported class of this exporter
- ``text`` (bool):  [Read-Write] If true, this will export the data as text

<a id="unreal.Exporter.supported_class"></a>

#### supported_class

```python
@property
def supported_class() -> Class
```

(type(Class)):  [Read-Write] Supported class of this exporter

<a id="unreal.Exporter.supported_class"></a>

#### supported_class

```python
@supported_class.setter
def supported_class(value: Class) -> None
```

<a id="unreal.Exporter.format_extension"></a>

#### format_extension

```python
@property
def format_extension() -> Array[str]
```

(Array[str]):  [Read-Write] File extension to use for this exporter

<a id="unreal.Exporter.format_extension"></a>

#### format_extension

```python
@format_extension.setter
def format_extension(value: Array[str]) -> None
```

<a id="unreal.Exporter.format_description"></a>

#### format_description

```python
@property
def format_description() -> Array[str]
```

(Array[str]):  [Read-Write] Descriptiong of the export format

<a id="unreal.Exporter.format_description"></a>

#### format_description

```python
@format_description.setter
def format_description(value: Array[str]) -> None
```

<a id="unreal.Exporter.text"></a>

#### text

```python
@property
def text() -> bool
```

(bool):  [Read-Write] If true, this will export the data as text

<a id="unreal.Exporter.text"></a>

#### text

```python
@text.setter
def text(value: bool) -> None
```

<a id="unreal.Exporter.export_task"></a>

#### export_task

```python
@property
def export_task() -> AssetExportTask
```

(AssetExportTask):  [Read-Write]

<a id="unreal.Exporter.export_task"></a>

#### export_task

```python
@export_task.setter
def export_task(value: AssetExportTask) -> None
```

<a id="unreal.Exporter.script_run_asset_export_task"></a>

#### script_run_asset_export_task

```python
def script_run_asset_export_task(task: AssetExportTask) -> bool
```

x.script_run_asset_export_task(task) -> bool
Export the given object to file.  Overridden by script based exporters.

Args:
    task (AssetExportTask): The task to export.

Returns:
    bool: true if overridden by script exporter.

<a id="unreal.Exporter.run_asset_export_tasks"></a>

#### run_asset_export_tasks

```python
@classmethod
def run_asset_export_tasks(cls, export_tasks: Array[AssetExportTask]) -> bool
```

X.run_asset_export_tasks(export_tasks) -> bool
Export the given objects to files.  Child classes do not override this, but they do provide an Export() function
to do the resource-specific export work.

Args:
    export_tasks (Array[AssetExportTask]): The array of tasks to export.

Returns:
    bool: true if all tasks ran without error

<a id="unreal.Exporter.run_asset_export_task"></a>

#### run_asset_export_task

```python
@classmethod
def run_asset_export_task(cls, task: AssetExportTask) -> bool
```

X.run_asset_export_task(task) -> bool
Export the given object to file.  Child classes do not override this, but they do provide an Export() function
to do the resource-specific export work.

Args:
    task (AssetExportTask): The task to export.

Returns:
    bool: true if the the object was successfully exported

<a id="unreal.ActorElementsExporterT3D"></a>