## InterchangeManager Objects

```python
class InterchangeManager(Object)
```

Interchange Manager

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangeManager.h

<a id="unreal.InterchangeManager.scripted_import_scene_async"></a>

#### scripted_import_scene_async

```python
def scripted_import_scene_async(
        content_path: str, source_data: InterchangeSourceData,
        import_asset_parameters: ImportAssetParameters) -> bool
```

x.scripted_import_scene_async(content_path, source_data, import_asset_parameters) -> bool
Call this to start a asynchronous scene import process.
This process can import many different assets and their transforms (USceneComponent).

Args:
    content_path (str): The path where the imported assets will be created.
    source_data (InterchangeSourceData): The source data input to translate. This object will be duplicated to allow thread-safe operations.
    import_asset_parameters (ImportAssetParameters): All parameters that need to be passed to the import asset function.

Returns:
    bool: true if the import was started, or false otherwise.

<a id="unreal.InterchangeManager.scripted_import_asset_async"></a>

#### scripted_import_asset_async

```python
def scripted_import_asset_async(
        content_path: str, source_data: InterchangeSourceData,
        import_asset_parameters: ImportAssetParameters) -> bool
```

x.scripted_import_asset_async(content_path, source_data, import_asset_parameters) -> bool
Call this from blueprint or python to start an asynchronous asset import process.
This process can import many different assets into the game content.

Args:
    content_path (str): The path where the imported assets will be created.
    source_data (InterchangeSourceData): The source data input to translate.
    import_asset_parameters (ImportAssetParameters): All parameters that need to be passed to the import asset function.

Returns:
    bool: true if the import was started, or false otherwise.

<a id="unreal.InterchangeManager.import_scene"></a>

#### import_scene

```python
def import_scene(content_path: str, source_data: InterchangeSourceData,
                 import_asset_parameters: ImportAssetParameters) -> bool
```

x.import_scene(content_path, source_data, import_asset_parameters) -> bool
Call this to start a synchronous scene import process.
This process can import many different assets and their transforms (USceneComponent).
Note: In blueprint depending on the event you use to start the import its possible to have a deadlock, use the async function if its what you are experimenting

Args:
    content_path (str): The path where the imported assets will be created.
    source_data (InterchangeSourceData): The source data input to translate. This object will be duplicated to allow thread-safe operations.
    import_asset_parameters (ImportAssetParameters): All parameters that need to be passed to the import asset function.

Returns:
    bool: true if the import succeeds, or false otherwise.

<a id="unreal.InterchangeManager.import_asset"></a>

#### import_asset

```python
def import_asset(
        content_path: str, source_data: InterchangeSourceData,
        import_asset_parameters: ImportAssetParameters
) -> Optional[Array[Object]]
```

x.import_asset(content_path, source_data, import_asset_parameters) -> Array[Object] or None
Call this to start a synchronous asset import process.
This process can import many different assets into the game content.
Note: In blueprint depending on the event you use to start the import its possible to have a deadlock, use the async function if its what you are experimenting

Args:
    content_path (str): The path where the imported assets will be created.
    source_data (InterchangeSourceData): The source data input to translate.
    import_asset_parameters (ImportAssetParameters): All parameters that need to be passed to the import asset function.

Returns:
    Array[Object] or None: true if the import succeeds, or false otherwise.

    out_imported_objects (Array[Object]):

<a id="unreal.InterchangeManager.get_registered_factory_class"></a>

#### get_registered_factory_class

```python
def get_registered_factory_class(class_to_make: Class) -> Class
```

x.get_registered_factory_class(class_to_make) -> type(Class)
Script helper to get a registered factory for a specified class.
return:: The registered factory class if found, or NULL if no registered factory was found.

Args:
    class_to_make (type(Class)): 

Returns:
    type(Class):

<a id="unreal.InterchangeManager.get_interchange_manager_scripted"></a>

#### get_interchange_manager_scripted

```python
@classmethod
def get_interchange_manager_scripted(cls) -> InterchangeManager
```

X.get_interchange_manager_scripted() -> InterchangeManager
Return the pointer to the Interchange Manager singleton.
note: We need to return a pointer to have a valid Blueprint-callable function.

Returns:
    InterchangeManager:

<a id="unreal.InterchangeManager.export_scene"></a>

#### export_scene

```python
def export_scene(world: Object, is_automated: bool = False) -> bool
```

x.export_scene(world, is_automated=False) -> bool
Call this to start a scene export process. The caller must specify a source data.

Args:
    world (Object): The scene to export.
    is_automated (bool): If true, the import process will not show any UI or dialogs.

Returns:
    bool: true if the export succeeds, or false otherwise.

<a id="unreal.InterchangeManager.export_asset"></a>

#### export_asset

```python
def export_asset(asset: Object, is_automated: bool = False) -> bool
```

x.export_asset(asset, is_automated=False) -> bool
Call this to start an asset export process. The caller must specify a source data.

Args:
    asset (Object): The asset to export.
    is_automated (bool): If true, the exporter will not show any UI or dialogs.

Returns:
    bool: true if the export succeeds, or false otherwise.

<a id="unreal.InterchangeManager.create_source_data"></a>

#### create_source_data

```python
@classmethod
def create_source_data(cls, file_name: str) -> InterchangeSourceData
```

X.create_source_data(file_name) -> InterchangeSourceData
* Script helper to create a source data object that points to a file on disk.
*
return:: A new UInterchangeSourceData.

Args:
    file_name (str): 

Returns:
    InterchangeSourceData:

<a id="unreal.InterchangeMeshUtilities"></a>