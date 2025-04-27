## AssetImportTask Objects

```python
class AssetImportTask(Object)
```

Contains data for a group of assets to import

**C++ Source:**

- **Module**: UnrealEd
- **File**: AssetImportTask.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``async_`` (bool):  [Read-Write] Perform the import asynchronously for file formats where async import is available
- ``automated`` (bool):  [Read-Write] Avoid dialogs
- ``destination_name`` (str):  [Read-Write] Optional custom name to import as (if you are using interchange the name must be set in a pipeline and this field will be ignored)
- ``destination_path`` (str):  [Read-Write] Path where asset will be imported to
- ``factory`` (Factory):  [Read-Write] Optional factory to use
- ``filename`` (str):  [Read-Write] Filename to import
- ``imported_object_paths`` (Array[str]):  [Read-Write] Paths to objects created or updated after import
- ``options`` (Object):  [Read-Write] Import options specific to the type of asset
- ``replace_existing`` (bool):  [Read-Write] Overwrite existing assets
- ``replace_existing_settings`` (bool):  [Read-Write] Replace existing settings when overwriting existing assets
- ``result`` (Array[Object]):  [Read-Write]
  deprecated: Please use the GetObjects function instead.
- ``save`` (bool):  [Read-Write] Save after importing

<a id="unreal.AssetImportTask.filename"></a>

#### filename

```python
@property
def filename() -> str
```

(str):  [Read-Write] Filename to import

<a id="unreal.AssetImportTask.filename"></a>

#### filename

```python
@filename.setter
def filename(value: str) -> None
```

<a id="unreal.AssetImportTask.destination_path"></a>

#### destination_path

```python
@property
def destination_path() -> str
```

(str):  [Read-Write] Path where asset will be imported to

<a id="unreal.AssetImportTask.destination_path"></a>

#### destination_path

```python
@destination_path.setter
def destination_path(value: str) -> None
```

<a id="unreal.AssetImportTask.destination_name"></a>

#### destination_name

```python
@property
def destination_name() -> str
```

(str):  [Read-Write] Optional custom name to import as (if you are using interchange the name must be set in a pipeline and this field will be ignored)

<a id="unreal.AssetImportTask.destination_name"></a>

#### destination_name

```python
@destination_name.setter
def destination_name(value: str) -> None
```

<a id="unreal.AssetImportTask.replace_existing"></a>

#### replace_existing

```python
@property
def replace_existing() -> bool
```

(bool):  [Read-Write] Overwrite existing assets

<a id="unreal.AssetImportTask.replace_existing"></a>

#### replace_existing

```python
@replace_existing.setter
def replace_existing(value: bool) -> None
```

<a id="unreal.AssetImportTask.replace_existing_settings"></a>

#### replace_existing_settings

```python
@property
def replace_existing_settings() -> bool
```

(bool):  [Read-Write] Replace existing settings when overwriting existing assets

<a id="unreal.AssetImportTask.replace_existing_settings"></a>

#### replace_existing_settings

```python
@replace_existing_settings.setter
def replace_existing_settings(value: bool) -> None
```

<a id="unreal.AssetImportTask.automated"></a>

#### automated

```python
@property
def automated() -> bool
```

(bool):  [Read-Write] Avoid dialogs

<a id="unreal.AssetImportTask.automated"></a>

#### automated

```python
@automated.setter
def automated(value: bool) -> None
```

<a id="unreal.AssetImportTask.save"></a>

#### save

```python
@property
def save() -> bool
```

(bool):  [Read-Write] Save after importing

<a id="unreal.AssetImportTask.save"></a>

#### save

```python
@save.setter
def save(value: bool) -> None
```

<a id="unreal.AssetImportTask.async_"></a>

#### async_

```python
@property
def async_() -> bool
```

(bool):  [Read-Write] Perform the import asynchronously for file formats where async import is available

<a id="unreal.AssetImportTask.async_"></a>

#### async_

```python
@async_.setter
def async_(value: bool) -> None
```

<a id="unreal.AssetImportTask.factory"></a>

#### factory

```python
@property
def factory() -> Factory
```

(Factory):  [Read-Write] Optional factory to use

<a id="unreal.AssetImportTask.factory"></a>

#### factory

```python
@factory.setter
def factory(value: Factory) -> None
```

<a id="unreal.AssetImportTask.options"></a>

#### options

```python
@property
def options() -> Object
```

(Object):  [Read-Write] Import options specific to the type of asset

<a id="unreal.AssetImportTask.options"></a>

#### options

```python
@options.setter
def options(value: Object) -> None
```

<a id="unreal.AssetImportTask.imported_object_paths"></a>

#### imported_object_paths

```python
@property
def imported_object_paths() -> Array[str]
```

(Array[str]):  [Read-Write] Paths to objects created or updated after import

<a id="unreal.AssetImportTask.imported_object_paths"></a>

#### imported_object_paths

```python
@imported_object_paths.setter
def imported_object_paths(value: Array[str]) -> None
```

<a id="unreal.AssetImportTask.result"></a>

#### result

```python
@property
def result() -> Array[Object]
```

(Array[Object]):  [Read-Write]
deprecated: Please use the GetObjects function instead.

<a id="unreal.AssetImportTask.result"></a>

#### result

```python
@result.setter
def result(value: Array[Object]) -> None
```

<a id="unreal.AssetImportTask.is_async_import_complete"></a>

#### is_async_import_complete

```python
def is_async_import_complete() -> bool
```

x.is_async_import_complete() -> bool
Query whether this asynchronous import task is complete, and the results are ready to read.
This will always return true in the case of a blocking import.

Returns:
    bool:

<a id="unreal.AssetImportTask.get_objects"></a>

#### get_objects

```python
def get_objects() -> Array[Object]
```

x.get_objects() -> Array[Object]
Get the list of imported objects.
Note that if the import was asynchronous, this will block until the results are ready.
To test whether asynchronous results are ready or not, use IsAsyncImportComplete().

Returns:
    Array[Object]:

<a id="unreal.AutomatedAssetImportData"></a>