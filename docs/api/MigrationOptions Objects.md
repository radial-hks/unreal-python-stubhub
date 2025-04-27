## MigrationOptions Objects

```python
class MigrationOptions(StructBase)
```

Migration Options

**C++ Source:**

- **Module**: AssetTools
- **File**: IAssetTools.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_conflict`` (AssetMigrationConflict):  [Read-Write] What to do when Assets are conflicting on the destination
- ``ignore_dependencies`` (bool):  [Read-Write] Ignore dependencies of assets, only migrate the given assets. usefull for automation. This will not migrate the actors of a OFPA (one file per actor) level
- ``orphan_folder`` (str):  [Read-Write] Destination for assets that don't have a corresponding content folder. If left empty those assets are not migrated. (Not used by the new migration)
- ``prompt`` (bool):  [Read-Write] Prompt user for confirmation (always false through scripting)

<a id="unreal.MigrationOptions.__init__"></a>

#### __init__

```python
def __init__(
        prompt: bool = False,
        ignore_dependencies: bool = False,
        asset_conflict: AssetMigrationConflict = AssetMigrationConflict.SKIP,
        orphan_folder: str = "") -> None
```

<a id="unreal.MigrationOptions.prompt"></a>

#### prompt

```python
@property
def prompt() -> bool
```

(bool):  [Read-Write] Prompt user for confirmation (always false through scripting)

<a id="unreal.MigrationOptions.prompt"></a>

#### prompt

```python
@prompt.setter
def prompt(value: bool) -> None
```

<a id="unreal.MigrationOptions.ignore_dependencies"></a>

#### ignore_dependencies

```python
@property
def ignore_dependencies() -> bool
```

(bool):  [Read-Write] Ignore dependencies of assets, only migrate the given assets. usefull for automation. This will not migrate the actors of a OFPA (one file per actor) level

<a id="unreal.MigrationOptions.ignore_dependencies"></a>

#### ignore_dependencies

```python
@ignore_dependencies.setter
def ignore_dependencies(value: bool) -> None
```

<a id="unreal.MigrationOptions.asset_conflict"></a>

#### asset_conflict

```python
@property
def asset_conflict() -> AssetMigrationConflict
```

(AssetMigrationConflict):  [Read-Write] What to do when Assets are conflicting on the destination

<a id="unreal.MigrationOptions.asset_conflict"></a>

#### asset_conflict

```python
@asset_conflict.setter
def asset_conflict(value: AssetMigrationConflict) -> None
```

<a id="unreal.MigrationOptions.orphan_folder"></a>

#### orphan_folder

```python
@property
def orphan_folder() -> str
```

(str):  [Read-Write] Destination for assets that don't have a corresponding content folder. If left empty those assets are not migrated. (Not used by the new migration)

<a id="unreal.MigrationOptions.orphan_folder"></a>

#### orphan_folder

```python
@orphan_folder.setter
def orphan_folder(value: str) -> None
```

<a id="unreal.SourceControlState"></a>