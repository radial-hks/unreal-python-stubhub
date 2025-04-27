## ImportSubsystem Objects

```python
class ImportSubsystem(EditorSubsystem)
```

UImportSubsystem
Subsystem for importing assets in the editor,
Contains utility functions and callbacks for hooking into importing.

**C++ Source:**

- **Module**: UnrealEd
- **File**: ImportSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_asset_post_import`` (OnAssetPostImport_Dyn):  [Read-Write]
- ``on_asset_post_lod_import`` (OnAssetPostLODImport_Dyn):  [Read-Write]
- ``on_asset_pre_import`` (OnAssetPreImport_Dyn):  [Read-Write]
- ``on_asset_reimport`` (OnAssetReimport_Dyn):  [Read-Write]

<a id="unreal.ImportSubsystem.on_asset_pre_import"></a>

#### on_asset_pre_import

```python
@property
def on_asset_pre_import() -> OnAssetPreImport_Dyn
```

(OnAssetPreImport_Dyn):  [Read-Write]

<a id="unreal.ImportSubsystem.on_asset_pre_import"></a>

#### on_asset_pre_import

```python
@on_asset_pre_import.setter
def on_asset_pre_import(value: OnAssetPreImport_Dyn) -> None
```

<a id="unreal.ImportSubsystem.on_asset_post_import"></a>

#### on_asset_post_import

```python
@property
def on_asset_post_import() -> OnAssetPostImport_Dyn
```

(OnAssetPostImport_Dyn):  [Read-Write]

<a id="unreal.ImportSubsystem.on_asset_post_import"></a>

#### on_asset_post_import

```python
@on_asset_post_import.setter
def on_asset_post_import(value: OnAssetPostImport_Dyn) -> None
```

<a id="unreal.ImportSubsystem.on_asset_reimport"></a>

#### on_asset_reimport

```python
@property
def on_asset_reimport() -> OnAssetReimport_Dyn
```

(OnAssetReimport_Dyn):  [Read-Write]

<a id="unreal.ImportSubsystem.on_asset_reimport"></a>

#### on_asset_reimport

```python
@on_asset_reimport.setter
def on_asset_reimport(value: OnAssetReimport_Dyn) -> None
```

<a id="unreal.ImportSubsystem.on_asset_post_lod_import"></a>

#### on_asset_post_lod_import

```python
@property
def on_asset_post_lod_import() -> OnAssetPostLODImport_Dyn
```

(OnAssetPostLODImport_Dyn):  [Read-Write]

<a id="unreal.ImportSubsystem.on_asset_post_lod_import"></a>

#### on_asset_post_lod_import

```python
@on_asset_post_lod_import.setter
def on_asset_post_lod_import(value: OnAssetPostLODImport_Dyn) -> None
```

<a id="unreal.LayersSubsystem"></a>