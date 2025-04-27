## InterchangeAssetImportData Objects

```python
class InterchangeAssetImportData(AssetImportData)
```

Interchange Asset Import Data

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangeAssetImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``node_container`` (InterchangeBaseNodeContainer):  [Read-Write]
  deprecated: Use GetNodeContainer/SetNodeContainer instead.
- ``node_unique_id`` (str):  [Read-Only] The Node UID passed to the factory that existed in the graph that was used to create this asset.
- ``pipelines`` (Array[Object]):  [Read-Write]
  deprecated: Use GetPipelines/SetPipelines instead.
- ``scene_import_asset`` (SoftObjectPath):  [Read-Write] On a level import, set to the UInterchangeSceneImportAsset created during the import.
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.

<a id="unreal.InterchangeAssetImportData.node_container"></a>

#### node_container

```python
@property
def node_container() -> InterchangeBaseNodeContainer
```

(InterchangeBaseNodeContainer):  [Read-Write]
deprecated: Use GetNodeContainer/SetNodeContainer instead.

<a id="unreal.InterchangeAssetImportData.node_container"></a>

#### node_container

```python
@node_container.setter
def node_container(value: InterchangeBaseNodeContainer) -> None
```

<a id="unreal.InterchangeAssetImportData.pipelines"></a>

#### pipelines

```python
@property
def pipelines() -> Array[Object]
```

(Array[Object]):  [Read-Write]
deprecated: Use GetPipelines/SetPipelines instead.

<a id="unreal.InterchangeAssetImportData.pipelines"></a>

#### pipelines

```python
@pipelines.setter
def pipelines(value: Array[Object]) -> None
```

<a id="unreal.InterchangeAssetImportData.set_translator_settings"></a>

#### set_translator_settings

```python
def set_translator_settings(
        translator_settings: InterchangeTranslatorSettings) -> None
```

x.set_translator_settings(translator_settings) -> None
Set Translator Settings

Args:
    translator_settings (InterchangeTranslatorSettings):

<a id="unreal.InterchangeAssetImportData.set_pipelines"></a>

#### set_pipelines

```python
def set_pipelines(pipelines: Array[Object]) -> None
```

x.set_pipelines(pipelines) -> None
Set Pipelines

Args:
    pipelines (Array[Object]):

<a id="unreal.InterchangeAssetImportData.set_node_container"></a>

#### set_node_container

```python
def set_node_container(node_container: InterchangeBaseNodeContainer) -> None
```

x.set_node_container(node_container) -> None
Set Node Container

Args:
    node_container (InterchangeBaseNodeContainer):

<a id="unreal.InterchangeAssetImportData.script_get_first_filename"></a>

#### script_get_first_filename

```python
def script_get_first_filename() -> str
```

x.script_get_first_filename() -> str
Return the first filename stored in this data. The resulting filename will be absolute (that is, not relative to the asset).

Returns:
    str:

<a id="unreal.InterchangeAssetImportData.script_extract_filenames"></a>

#### script_extract_filenames

```python
def script_extract_filenames() -> Array[str]
```

x.script_extract_filenames() -> Array[str]
Extract all the (resolved) filenames.

Returns:
    Array[str]:

<a id="unreal.InterchangeAssetImportData.script_extract_display_labels"></a>

#### script_extract_display_labels

```python
def script_extract_display_labels() -> Array[str]
```

x.script_extract_display_labels() -> Array[str]
Extract all the filename labels.

Returns:
    Array[str]:

<a id="unreal.InterchangeAssetImportData.get_translator_settings"></a>

#### get_translator_settings

```python
def get_translator_settings() -> InterchangeTranslatorSettings
```

x.get_translator_settings() -> InterchangeTranslatorSettings
Get Translator Settings

Returns:
    InterchangeTranslatorSettings:

<a id="unreal.InterchangeAssetImportData.get_stored_node"></a>

#### get_stored_node

```python
def get_stored_node(node_unique_id: str) -> InterchangeBaseNode
```

x.get_stored_node(node_unique_id) -> InterchangeBaseNode
Get Stored Node

Args:
    node_unique_id (str): 

Returns:
    InterchangeBaseNode:

<a id="unreal.InterchangeAssetImportData.get_stored_factory_node"></a>

#### get_stored_factory_node

```python
def get_stored_factory_node(node_unique_id: str) -> InterchangeFactoryBaseNode
```

x.get_stored_factory_node(node_unique_id) -> InterchangeFactoryBaseNode
Get Stored Factory Node

Args:
    node_unique_id (str): 

Returns:
    InterchangeFactoryBaseNode:

<a id="unreal.InterchangeAssetImportData.get_pipelines"></a>

#### get_pipelines

```python
def get_pipelines() -> Array[Object]
```

x.get_pipelines() -> Array[Object]
Returns Array of non-null pipelines

Returns:
    Array[Object]:

<a id="unreal.InterchangeAssetImportData.get_number_of_pipelines"></a>

#### get_number_of_pipelines

```python
def get_number_of_pipelines() -> int
```

x.get_number_of_pipelines() -> int32
Get Number Of Pipelines

Returns:
    int32:

<a id="unreal.InterchangeAssetImportData.get_node_container"></a>

#### get_node_container

```python
def get_node_container() -> InterchangeBaseNodeContainer
```

x.get_node_container() -> InterchangeBaseNodeContainer
Get Node Container

Returns:
    InterchangeBaseNodeContainer:

<a id="unreal.InterchangePipelineStackOverride"></a>