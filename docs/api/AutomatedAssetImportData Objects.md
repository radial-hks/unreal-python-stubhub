## AutomatedAssetImportData Objects

```python
class AutomatedAssetImportData(Object)
```

Contains data for a group of assets to import

**C++ Source:**

- **Module**: UnrealEd
- **File**: AutomatedAssetImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``destination_path`` (str):  [Read-Write] Content path in the projects content directory where assets will be imported
- ``factory`` (Factory):  [Read-Write] Pointer to the factory currently being used
- ``factory_name`` (str):  [Read-Write] Name of the factory to use when importing these assets. If not specified the factory type will be auto detected
- ``filenames`` (Array[str]):  [Read-Write] Filenames to import
- ``group_name`` (str):  [Read-Write] Display name of the group. This is for logging purposes only.
- ``level_to_load`` (str):  [Read-Write] Full path to level to load before importing this group (only matters if importing assets into a level)
- ``replace_existing`` (bool):  [Read-Write] Whether or not to replace existing assets
- ``skip_read_only`` (bool):  [Read-Write] Whether or not to skip importing over read only assets that could not be checked out

<a id="unreal.AutomatedAssetImportData.group_name"></a>

#### group_name

```python
@property
def group_name() -> str
```

(str):  [Read-Write] Display name of the group. This is for logging purposes only.

<a id="unreal.AutomatedAssetImportData.group_name"></a>

#### group_name

```python
@group_name.setter
def group_name(value: str) -> None
```

<a id="unreal.AutomatedAssetImportData.filenames"></a>

#### filenames

```python
@property
def filenames() -> Array[str]
```

(Array[str]):  [Read-Write] Filenames to import

<a id="unreal.AutomatedAssetImportData.filenames"></a>

#### filenames

```python
@filenames.setter
def filenames(value: Array[str]) -> None
```

<a id="unreal.AutomatedAssetImportData.destination_path"></a>

#### destination_path

```python
@property
def destination_path() -> str
```

(str):  [Read-Write] Content path in the projects content directory where assets will be imported

<a id="unreal.AutomatedAssetImportData.destination_path"></a>

#### destination_path

```python
@destination_path.setter
def destination_path(value: str) -> None
```

<a id="unreal.AutomatedAssetImportData.factory_name"></a>

#### factory_name

```python
@property
def factory_name() -> str
```

(str):  [Read-Write] Name of the factory to use when importing these assets. If not specified the factory type will be auto detected

<a id="unreal.AutomatedAssetImportData.factory_name"></a>

#### factory_name

```python
@factory_name.setter
def factory_name(value: str) -> None
```

<a id="unreal.AutomatedAssetImportData.replace_existing"></a>

#### replace_existing

```python
@property
def replace_existing() -> bool
```

(bool):  [Read-Write] Whether or not to replace existing assets

<a id="unreal.AutomatedAssetImportData.replace_existing"></a>

#### replace_existing

```python
@replace_existing.setter
def replace_existing(value: bool) -> None
```

<a id="unreal.AutomatedAssetImportData.skip_read_only"></a>

#### skip_read_only

```python
@property
def skip_read_only() -> bool
```

(bool):  [Read-Write] Whether or not to skip importing over read only assets that could not be checked out

<a id="unreal.AutomatedAssetImportData.skip_read_only"></a>

#### skip_read_only

```python
@skip_read_only.setter
def skip_read_only(value: bool) -> None
```

<a id="unreal.AutomatedAssetImportData.factory"></a>

#### factory

```python
@property
def factory() -> Factory
```

(Factory):  [Read-Write] Pointer to the factory currently being used

<a id="unreal.AutomatedAssetImportData.factory"></a>

#### factory

```python
@factory.setter
def factory(value: Factory) -> None
```

<a id="unreal.AutomatedAssetImportData.level_to_load"></a>

#### level_to_load

```python
@property
def level_to_load() -> str
```

(str):  [Read-Write] Full path to level to load before importing this group (only matters if importing assets into a level)

<a id="unreal.AutomatedAssetImportData.level_to_load"></a>

#### level_to_load

```python
@level_to_load.setter
def level_to_load(value: str) -> None
```

<a id="unreal.BlueprintFactory"></a>