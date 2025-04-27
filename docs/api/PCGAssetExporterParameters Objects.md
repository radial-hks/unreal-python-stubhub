## PCGAssetExporterParameters Objects

```python
class PCGAssetExporterParameters(StructBase)
```

Common structure to hold saving options required to export or update PCG assets.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAssetExporter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_name`` (str):  [Read-Write] Target asset path name
- ``asset_path`` (str):  [Read-Write] Target asset path to write the PCG assets to.
- ``open_save_dialog`` (bool):  [Read-Write] Controls whether we will open a Save... dialog, works only when a single level is exported. Overrides update anywhere.
- ``save_on_export_ended`` (bool):  [Read-Write] Controls whether the assets will be saved at the end of the process or not.

<a id="unreal.PCGAssetExporterParameters.__init__"></a>

#### __init__

```python
def __init__(open_save_dialog: bool = False,
             asset_name: str = "",
             asset_path: str = "",
             save_on_export_ended: bool = False) -> None
```

<a id="unreal.PCGAssetExporterParameters.open_save_dialog"></a>

#### open_save_dialog

```python
@property
def open_save_dialog() -> bool
```

(bool):  [Read-Write] Controls whether we will open a Save... dialog, works only when a single level is exported. Overrides update anywhere.

<a id="unreal.PCGAssetExporterParameters.open_save_dialog"></a>

#### open_save_dialog

```python
@open_save_dialog.setter
def open_save_dialog(value: bool) -> None
```

<a id="unreal.PCGAssetExporterParameters.asset_name"></a>

#### asset_name

```python
@property
def asset_name() -> str
```

(str):  [Read-Write] Target asset path name

<a id="unreal.PCGAssetExporterParameters.asset_name"></a>

#### asset_name

```python
@asset_name.setter
def asset_name(value: str) -> None
```

<a id="unreal.PCGAssetExporterParameters.asset_path"></a>

#### asset_path

```python
@property
def asset_path() -> str
```

(str):  [Read-Write] Target asset path to write the PCG assets to.

<a id="unreal.PCGAssetExporterParameters.asset_path"></a>

#### asset_path

```python
@asset_path.setter
def asset_path(value: str) -> None
```

<a id="unreal.PCGAssetExporterParameters.save_on_export_ended"></a>

#### save_on_export_ended

```python
@property
def save_on_export_ended() -> bool
```

(bool):  [Read-Write] Controls whether the assets will be saved at the end of the process or not.

<a id="unreal.PCGAssetExporterParameters.save_on_export_ended"></a>

#### save_on_export_ended

```python
@save_on_export_ended.setter
def save_on_export_ended(value: bool) -> None
```

<a id="unreal.PCGAttributeFilterThresholdSettings"></a>