## AssetTools Objects

```python
class AssetTools(Interface)
```

Asset Tools

**C++ Source:**

- **Module**: AssetTools
- **File**: IAssetTools.h

<a id="unreal.AssetTools.rename_referencing_soft_object_paths"></a>

#### rename_referencing_soft_object_paths

```python
def rename_referencing_soft_object_paths(
        packages_to_check: Array[Package],
        asset_redirector_map: Map[SoftObjectPath, SoftObjectPath]) -> None
```

x.rename_referencing_soft_object_paths(packages_to_check, asset_redirector_map) -> None
Function that renames all FSoftObjectPath object with the old asset path to the new one.

Args:
    packages_to_check (Array[Package]): Packages to check for referencing FSoftObjectPath.
    asset_redirector_map (Map[SoftObjectPath, SoftObjectPath]): Map from old asset path to new asset path

<a id="unreal.AssetTools.rename_assets_with_dialog"></a>

#### rename_assets_with_dialog

```python
def rename_assets_with_dialog(
        assets_and_names: Array[AssetRenameData],
        auto_checkout: bool = False) -> AssetRenameResult
```

x.rename_assets_with_dialog(assets_and_names, auto_checkout=False) -> AssetRenameResult
Renames assets using the specified names.

Args:
    assets_and_names (Array[AssetRenameData]): 
    auto_checkout (bool): 

Returns:
    AssetRenameResult:

<a id="unreal.AssetTools.rename_assets"></a>

#### rename_assets

```python
def rename_assets(assets_and_names: Array[AssetRenameData]) -> bool
```

x.rename_assets(assets_and_names) -> bool
Renames assets using the specified names.

Args:
    assets_and_names (Array[AssetRenameData]): 

Returns:
    bool:

<a id="unreal.AssetTools.open_editor_for_assets"></a>

#### open_editor_for_assets

```python
def open_editor_for_assets(assets: Array[Object]) -> None
```

x.open_editor_for_assets(assets) -> None
Opens editor for assets
deprecated: Please use UAssetEditorSubsystem::OpenEditorForAssets instead.

Args:
    assets (Array[Object]):

<a id="unreal.AssetTools.migrate_packages"></a>

#### migrate_packages

```python
def migrate_packages(
    package_names_to_migrate: Array[Name],
    destination_path: str,
    options: MigrationOptions = [
        False, False, AssetMigrationConflict.SKIP, ""
    ]
) -> None
```

x.migrate_packages(package_names_to_migrate, destination_path, options=[False, False, AssetMigrationConflict.SKIP, ""]) -> None
Migrate packages and dependencies to another folder

Args:
    package_names_to_migrate (Array[Name]): 
    destination_path (str): 
    options (MigrationOptions):

<a id="unreal.AssetTools.import_asset_tasks"></a>

#### import_asset_tasks

```python
def import_asset_tasks(import_tasks: Array[AssetImportTask]) -> None
```

x.import_asset_tasks(import_tasks) -> None
Imports assets using tasks specified.

Args:
    import_tasks (Array[AssetImportTask]): Tasks that specify how to import each file

<a id="unreal.AssetTools.import_assets_with_dialog"></a>

#### import_assets_with_dialog

```python
def import_assets_with_dialog(destination_path: str) -> Array[Object]
```

x.import_assets_with_dialog(destination_path) -> Array[Object]
Opens a file open dialog to choose files to import to the destination path.

Args:
    destination_path (str): Path to import files to

Returns:
    Array[Object]: list of successfully imported assets

<a id="unreal.AssetTools.import_assets_automated"></a>

#### import_assets_automated

```python
def import_assets_automated(
        import_data: AutomatedAssetImportData) -> Array[Object]
```

x.import_assets_automated(import_data) -> Array[Object]
Imports assets using data specified completely up front.  Does not ever ask any questions of the user or show any modal error messages

Args:
    import_data (AutomatedAssetImportData): 

Returns:
    Array[Object]: list of successfully imported assets

<a id="unreal.AssetTools.find_soft_references_to_object"></a>

#### find_soft_references_to_object

```python
def find_soft_references_to_object(
        target_object: SoftObjectPath) -> Array[Object]
```

x.find_soft_references_to_object(target_object) -> Array[Object]
Returns list of objects that soft reference the given soft object path. This will load assets into memory to verify

Args:
    target_object (SoftObjectPath): 

Returns:
    Array[Object]: 

    referencing_objects (Array[Object]):

<a id="unreal.AssetTools.export_assets_with_dialog"></a>

#### export_assets_with_dialog

```python
def export_assets_with_dialog(assets_to_export: Array[str],
                              prompt_for_individual_filenames: bool) -> None
```

x.export_assets_with_dialog(assets_to_export, prompt_for_individual_filenames) -> None
Exports the specified objects to file. First prompting the user to pick an export directory and optionally prompting the user to pick a unique directory per file

Args:
    assets_to_export (Array[str]): List of assets to export
    prompt_for_individual_filenames (bool):

<a id="unreal.AssetTools.export_assets"></a>

#### export_assets

```python
def export_assets(assets_to_export: Array[str], export_path: str) -> None
```

x.export_assets(assets_to_export, export_path) -> None
Exports the specified objects to file.

Args:
    assets_to_export (Array[str]): List of full asset names (e.g /Game/Path/Asset) to export
    export_path (str): The directory path to export to.

<a id="unreal.AssetTools.duplicate_asset_with_dialog_and_title"></a>

#### duplicate_asset_with_dialog_and_title

```python
def duplicate_asset_with_dialog_and_title(asset_name: str, package_path: str,
                                          original_object: Object,
                                          dialog_title: Text) -> Object
```

x.duplicate_asset_with_dialog_and_title(asset_name, package_path, original_object, dialog_title) -> Object
Opens an asset picker dialog and creates an asset with the specified name and path.
Uses OriginalObject as the duplication source.
Uses DialogTitle as the dialog's title.

Args:
    asset_name (str): 
    package_path (str): 
    original_object (Object): 
    dialog_title (Text): 

Returns:
    Object:

<a id="unreal.AssetTools.duplicate_asset_with_dialog"></a>

#### duplicate_asset_with_dialog

```python
def duplicate_asset_with_dialog(asset_name: str, package_path: str,
                                original_object: Object) -> Object
```

x.duplicate_asset_with_dialog(asset_name, package_path, original_object) -> Object
Opens an asset picker dialog and creates an asset with the specified name and path. Uses OriginalObject as the duplication source.

Args:
    asset_name (str): 
    package_path (str): 
    original_object (Object): 

Returns:
    Object:

<a id="unreal.AssetTools.duplicate_asset"></a>

#### duplicate_asset

```python
def duplicate_asset(asset_name: str, package_path: str,
                    original_object: Object) -> Object
```

x.duplicate_asset(asset_name, package_path, original_object) -> Object
Creates an asset with the specified name and path. Uses OriginalObject as the duplication source.

Args:
    asset_name (str): 
    package_path (str): 
    original_object (Object): 

Returns:
    Object:

<a id="unreal.AssetTools.diff_assets"></a>

#### diff_assets

```python
def diff_assets(old_asset: Object, new_asset: Object,
                old_revision: RevisionInfo,
                new_revision: RevisionInfo) -> None
```

x.diff_assets(old_asset, new_asset, old_revision, new_revision) -> None
Try and diff two assets using class-specific tool. Will do nothing if either asset is NULL, or they are not the same class.

Args:
    old_asset (Object): 
    new_asset (Object): 
    old_revision (RevisionInfo): 
    new_revision (RevisionInfo):

<a id="unreal.AssetTools.diff_against_depot"></a>

#### diff_against_depot

```python
def diff_against_depot(object: Object, package_path: str,
                       package_name: str) -> None
```

x.diff_against_depot(object, package_path, package_name) -> None
Try to diff the local version of an asset against the latest one from the depot

Args:
    object (Object): The object we want to compare against the depot
    package_path (str): The fullpath to the package
    package_name (str): The name of the package

<a id="unreal.AssetTools.create_unique_asset_name"></a>

#### create_unique_asset_name

```python
def create_unique_asset_name(base_package_name: str,
                             suffix: str) -> Tuple[str, str]
```

x.create_unique_asset_name(base_package_name, suffix) -> (out_package_name=str, out_asset_name=str)
Creates a unique package and asset name taking the form InBasePackageName+InSuffix

Args:
    base_package_name (str): 
    suffix (str): 

Returns:
    tuple: 

    out_package_name (str): 

    out_asset_name (str):

<a id="unreal.AssetTools.create_asset_with_dialog"></a>

#### create_asset_with_dialog

```python
def create_asset_with_dialog(asset_name: str,
                             package_path: str,
                             asset_class: Class,
                             factory: Factory,
                             calling_context: Name = "None",
                             call_configure_properties: bool = True) -> Object
```

x.create_asset_with_dialog(asset_name, package_path, asset_class, factory, calling_context="None", call_configure_properties=True) -> Object
Opens an asset picker dialog and creates an asset with the specified name and path

Args:
    asset_name (str): 
    package_path (str): 
    asset_class (type(Class)): 
    factory (Factory): 
    calling_context (Name): 
    call_configure_properties (bool): 

Returns:
    Object:

<a id="unreal.AssetTools.create_asset"></a>

#### create_asset

```python
def create_asset(asset_name: str,
                 package_path: str,
                 asset_class: Class,
                 factory: Factory,
                 calling_context: Name = "None") -> Object
```

x.create_asset(asset_name, package_path, asset_class, factory, calling_context="None") -> Object
Creates an asset with the specified name, path, and factory

Args:
    asset_name (str): the name of the new asset
    package_path (str): the package that will contain the new asset
    asset_class (type(Class)): the class of the new asset
    factory (Factory): the factory that will build the new asset
    calling_context (Name): optional name of the module or method calling CreateAsset() - this is passed to the factory

Returns:
    Object: the new asset or NULL if it fails

<a id="unreal.AssetTools.begin_advanced_copy_packages"></a>

#### begin_advanced_copy_packages

```python
def begin_advanced_copy_packages(
        input_names_to_copy: Array[Name], target_path: str,
        on_copy_complete: AdvancedCopyCompletedEvent) -> None
```

x.begin_advanced_copy_packages(input_names_to_copy, target_path, on_copy_complete) -> None
Begin Advanced Copy Packages

Args:
    input_names_to_copy (Array[Name]): 
    target_path (str): 
    on_copy_complete (AdvancedCopyCompletedEvent):

<a id="unreal.AssetToolsHelpers"></a>