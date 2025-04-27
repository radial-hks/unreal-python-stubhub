## ImportAssetParameters Objects

```python
class ImportAssetParameters(StructBase)
```

Import Asset Parameters

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangeManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``destination_name`` (str):  [Read-Write] Optional custom name for the import.
- ``follow_redirectors`` (bool):  [Read-Write] Tell Interchange to follow redirectors when determining the location an asset will be imported.
- ``force_show_dialog`` (bool):  [Read-Write] If true this import must show the import dialog and ignore the show dialog settings.
- ``import_level`` (Level):  [Read-Write] Level to import into when doing a scene import.
- ``is_automated`` (bool):  [Read-Write] Tell Interchange that import is automated and it shouldn't present a modal window.
- ``on_asset_done`` (OnObjectImportDoneDynamic):  [Read-Write] Delegates used to track the imported objects. // This is called each time an asset is imported or reimported from the import call.
- ``on_assets_import_done`` (OnImportDoneDynamic):  [Read-Write] This is called when all the assets were imported from the source data.
- ``on_scene_import_done`` (OnImportDoneDynamic):  [Read-Write] This is called when all the scene objects were imported from the source data.
- ``on_scene_object_done`` (OnObjectImportDoneDynamic):  [Read-Write] This is called each time an object in the scene is imported or reimported from the import call.
- ``override_pipelines`` (Array[SoftObjectPath]):  [Read-Write] Adding overrides tells Interchange to use the specific custom set of pipelines instead of letting the user or the system choose.
- ``reimport_asset`` (Object):  [Read-Write] If the import is a reimport for a specific asset, set the asset to reimport here.
- ``reimport_source_index`` (int32):  [Read-Write] If we are doing a reimport, set the source index here. Some assets have more then one source file that each contains part of the asset content.
- ``replace_existing`` (bool):  [Read-Write] Determies whether to overwrite existing assets.

<a id="unreal.ImportAssetParameters.__init__"></a>

#### __init__

```python
def __init__(
    reimport_asset: Object = None,
    reimport_source_index: int = 0,
    is_automated: bool = False,
    follow_redirectors: bool = False,
    override_pipelines: Array[SoftObjectPath] = [],
    import_level: Level = None,
    destination_name: str = "",
    replace_existing: bool = False,
    force_show_dialog: bool = False,
    on_asset_done: OnObjectImportDoneDynamic = OnObjectImportDoneDynamic(),
    on_assets_import_done: OnImportDoneDynamic = OnImportDoneDynamic(),
    on_scene_object_done: OnObjectImportDoneDynamic = OnObjectImportDoneDynamic(
    ),
    on_scene_import_done: OnImportDoneDynamic = OnImportDoneDynamic()
) -> None
```

<a id="unreal.ImportAssetParameters.reimport_asset"></a>

#### reimport_asset

```python
@property
def reimport_asset() -> Object
```

(Object):  [Read-Write] If the import is a reimport for a specific asset, set the asset to reimport here.

<a id="unreal.ImportAssetParameters.reimport_asset"></a>

#### reimport_asset

```python
@reimport_asset.setter
def reimport_asset(value: Object) -> None
```

<a id="unreal.ImportAssetParameters.reimport_source_index"></a>

#### reimport_source_index

```python
@property
def reimport_source_index() -> int
```

(int32):  [Read-Write] If we are doing a reimport, set the source index here. Some assets have more then one source file that each contains part of the asset content.

<a id="unreal.ImportAssetParameters.reimport_source_index"></a>

#### reimport_source_index

```python
@reimport_source_index.setter
def reimport_source_index(value: int) -> None
```

<a id="unreal.ImportAssetParameters.is_automated"></a>

#### is_automated

```python
@property
def is_automated() -> bool
```

(bool):  [Read-Write] Tell Interchange that import is automated and it shouldn't present a modal window.

<a id="unreal.ImportAssetParameters.is_automated"></a>

#### is_automated

```python
@is_automated.setter
def is_automated(value: bool) -> None
```

<a id="unreal.ImportAssetParameters.follow_redirectors"></a>

#### follow_redirectors

```python
@property
def follow_redirectors() -> bool
```

(bool):  [Read-Write] Tell Interchange to follow redirectors when determining the location an asset will be imported.

<a id="unreal.ImportAssetParameters.follow_redirectors"></a>

#### follow_redirectors

```python
@follow_redirectors.setter
def follow_redirectors(value: bool) -> None
```

<a id="unreal.ImportAssetParameters.override_pipelines"></a>

#### override_pipelines

```python
@property
def override_pipelines() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] Adding overrides tells Interchange to use the specific custom set of pipelines instead of letting the user or the system choose.

<a id="unreal.ImportAssetParameters.override_pipelines"></a>

#### override_pipelines

```python
@override_pipelines.setter
def override_pipelines(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.ImportAssetParameters.import_level"></a>

#### import_level

```python
@property
def import_level() -> Level
```

(Level):  [Read-Write] Level to import into when doing a scene import.

<a id="unreal.ImportAssetParameters.import_level"></a>

#### import_level

```python
@import_level.setter
def import_level(value: Level) -> None
```

<a id="unreal.ImportAssetParameters.destination_name"></a>

#### destination_name

```python
@property
def destination_name() -> str
```

(str):  [Read-Write] Optional custom name for the import.

<a id="unreal.ImportAssetParameters.destination_name"></a>

#### destination_name

```python
@destination_name.setter
def destination_name(value: str) -> None
```

<a id="unreal.ImportAssetParameters.replace_existing"></a>

#### replace_existing

```python
@property
def replace_existing() -> bool
```

(bool):  [Read-Write] Determies whether to overwrite existing assets.

<a id="unreal.ImportAssetParameters.replace_existing"></a>

#### replace_existing

```python
@replace_existing.setter
def replace_existing(value: bool) -> None
```

<a id="unreal.ImportAssetParameters.force_show_dialog"></a>

#### force_show_dialog

```python
@property
def force_show_dialog() -> bool
```

(bool):  [Read-Write] If true this import must show the import dialog and ignore the show dialog settings.

<a id="unreal.ImportAssetParameters.force_show_dialog"></a>

#### force_show_dialog

```python
@force_show_dialog.setter
def force_show_dialog(value: bool) -> None
```

<a id="unreal.ImportAssetParameters.on_asset_done"></a>

#### on_asset_done

```python
@property
def on_asset_done() -> OnObjectImportDoneDynamic
```

(OnObjectImportDoneDynamic):  [Read-Write] Delegates used to track the imported objects. // This is called each time an asset is imported or reimported from the import call.

<a id="unreal.ImportAssetParameters.on_asset_done"></a>

#### on_asset_done

```python
@on_asset_done.setter
def on_asset_done(value: OnObjectImportDoneDynamic) -> None
```

<a id="unreal.ImportAssetParameters.on_assets_import_done"></a>

#### on_assets_import_done

```python
@property
def on_assets_import_done() -> OnImportDoneDynamic
```

(OnImportDoneDynamic):  [Read-Write] This is called when all the assets were imported from the source data.

<a id="unreal.ImportAssetParameters.on_assets_import_done"></a>

#### on_assets_import_done

```python
@on_assets_import_done.setter
def on_assets_import_done(value: OnImportDoneDynamic) -> None
```

<a id="unreal.ImportAssetParameters.on_scene_object_done"></a>

#### on_scene_object_done

```python
@property
def on_scene_object_done() -> OnObjectImportDoneDynamic
```

(OnObjectImportDoneDynamic):  [Read-Write] This is called each time an object in the scene is imported or reimported from the import call.

<a id="unreal.ImportAssetParameters.on_scene_object_done"></a>

#### on_scene_object_done

```python
@on_scene_object_done.setter
def on_scene_object_done(value: OnObjectImportDoneDynamic) -> None
```

<a id="unreal.ImportAssetParameters.on_scene_import_done"></a>

#### on_scene_import_done

```python
@property
def on_scene_import_done() -> OnImportDoneDynamic
```

(OnImportDoneDynamic):  [Read-Write] This is called when all the scene objects were imported from the source data.

<a id="unreal.ImportAssetParameters.on_scene_import_done"></a>

#### on_scene_import_done

```python
@on_scene_import_done.setter
def on_scene_import_done(value: OnImportDoneDynamic) -> None
```

<a id="unreal.MigrationOptions"></a>