## UsdUnrealAssetInfo Objects

```python
class UsdUnrealAssetInfo(StructBase)
```

Metadata added to a prim to indicate it was exported from a particular Unreal asset

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDUnrealAssetInfo.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``identifier`` (str):  [Read-Write] Filepath to the layer where the asset was exported to
- ``name`` (str):  [Read-Write] Name of the Unreal asset
- ``unreal_asset_type`` (str):  [Read-Write] Class name of the exported asset (e.g. "StaticMesh")
- ``unreal_content_path`` (str):  [Read-Write] Path to the exported asset (e.g. "/Game/MyMaterials/Red.Red")
- ``unreal_engine_version`` (str):  [Read-Write] Engine version string describing the engine that exported this asset (e.g. "5.1.0-21000000+UE5")
- ``unreal_export_time`` (str):  [Read-Write] DateTime string of the moment of export (e.g. "2022.06.17-14.19.54")
- ``version`` (str):  [Read-Write] Identifier string for the current asset version. Whenever the asset is updated inside Unreal, this will change

<a id="unreal.UsdUnrealAssetInfo.__init__"></a>

#### __init__

```python
def __init__(name: str = "",
             identifier: str = "",
             version: str = "",
             unreal_content_path: str = "",
             unreal_asset_type: str = "",
             unreal_export_time: str = "",
             unreal_engine_version: str = "") -> None
```

<a id="unreal.UsdUnrealAssetInfo.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] Name of the Unreal asset

<a id="unreal.UsdUnrealAssetInfo.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.UsdUnrealAssetInfo.identifier"></a>

#### identifier

```python
@property
def identifier() -> str
```

(str):  [Read-Write] Filepath to the layer where the asset was exported to

<a id="unreal.UsdUnrealAssetInfo.identifier"></a>

#### identifier

```python
@identifier.setter
def identifier(value: str) -> None
```

<a id="unreal.UsdUnrealAssetInfo.version"></a>

#### version

```python
@property
def version() -> str
```

(str):  [Read-Write] Identifier string for the current asset version. Whenever the asset is updated inside Unreal, this will change

<a id="unreal.UsdUnrealAssetInfo.version"></a>

#### version

```python
@version.setter
def version(value: str) -> None
```

<a id="unreal.UsdUnrealAssetInfo.unreal_content_path"></a>

#### unreal_content_path

```python
@property
def unreal_content_path() -> str
```

(str):  [Read-Write] Path to the exported asset (e.g. "/Game/MyMaterials/Red.Red")

<a id="unreal.UsdUnrealAssetInfo.unreal_content_path"></a>

#### unreal_content_path

```python
@unreal_content_path.setter
def unreal_content_path(value: str) -> None
```

<a id="unreal.UsdUnrealAssetInfo.unreal_asset_type"></a>

#### unreal_asset_type

```python
@property
def unreal_asset_type() -> str
```

(str):  [Read-Write] Class name of the exported asset (e.g. "StaticMesh")

<a id="unreal.UsdUnrealAssetInfo.unreal_asset_type"></a>

#### unreal_asset_type

```python
@unreal_asset_type.setter
def unreal_asset_type(value: str) -> None
```

<a id="unreal.UsdUnrealAssetInfo.unreal_export_time"></a>

#### unreal_export_time

```python
@property
def unreal_export_time() -> str
```

(str):  [Read-Write] DateTime string of the moment of export (e.g. "2022.06.17-14.19.54")

<a id="unreal.UsdUnrealAssetInfo.unreal_export_time"></a>

#### unreal_export_time

```python
@unreal_export_time.setter
def unreal_export_time(value: str) -> None
```

<a id="unreal.UsdUnrealAssetInfo.unreal_engine_version"></a>

#### unreal_engine_version

```python
@property
def unreal_engine_version() -> str
```

(str):  [Read-Write] Engine version string describing the engine that exported this asset (e.g. "5.1.0-21000000+UE5")

<a id="unreal.UsdUnrealAssetInfo.unreal_engine_version"></a>

#### unreal_engine_version

```python
@unreal_engine_version.setter
def unreal_engine_version(value: str) -> None
```

<a id="unreal.Matrix2D"></a>