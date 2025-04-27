## EditorAssetSubsystem Objects

```python
class EditorAssetSubsystem(EditorSubsystem)
```

UEditorAssetSubsystem
Subsystem for exposing asset related utilities to scripts.
Asset Paths can be represented in the following ways:
             (Reference/Text Path)   StaticMesh'/Game/MyFolder/MyAsset.MyAsset'
             (Full Name)                             StaticMesh /Game/MyFolder/MyAsset.MyAsset
             (Path Name)                             /Game/MyFolder/MyAsset.MyAsset
             (Package Name)                  /Game/MyFolder/MyAsset
Directory Paths can be represented in the following ways:
             /Game/MyNewFolder/
             /Game/MyNewFolder

**C++ Source:**

- **Module**: UnrealEd
- **File**: EditorAssetSubsystem.h

<a id="unreal.EditorAssetSubsystem.sort_by_meta_data"></a>

#### sort_by_meta_data

```python
def sort_by_meta_data(
        assets: Array[AssetData], meta_data_tag: Name,
        meta_data_type: EditorAssetMetaDataSortType,
        sort_order: EditorAssetSortOrder) -> Optional[Array[AssetData]]
```

x.sort_by_meta_data(assets, meta_data_tag, meta_data_type, sort_order) -> Array[AssetData] or None
Sorts the assets based on their meta data's type.
Supported types: FString, int, float, FDateTime.

Args:
    assets (Array[AssetData]): The assets to sort
    meta_data_tag (Name): The on which the sort is based
    meta_data_type (EditorAssetMetaDataSortType): The meta data type of MetaDataTag
    sort_order (EditorAssetSortOrder): Whether to sort ascending or descending

Returns:
    Array[AssetData] or None: Whether the data was sorted, e.g. false if not all assets have the MetaDataTag.

    assets (Array[AssetData]): The assets to sort

<a id="unreal.EditorAssetSubsystem.set_metadata_tag"></a>

#### set_metadata_tag

```python
def set_metadata_tag(object: Object, tag: Name, value: str) -> None
```

x.set_metadata_tag(object, tag, value) -> None
Set the value associated with a given tag of a loaded asset's metadata.

Args:
    object (Object): The object from which to retrieve the metadata.
    tag (Name): The tag to set in the metadata.
    value (str): The string value to associate with the tag.

<a id="unreal.EditorAssetSubsystem.set_dirty_flag"></a>

#### set_dirty_flag

```python
def set_dirty_flag(object: Object, dirty_state: bool) -> bool
```

x.set_dirty_flag(object, dirty_state) -> bool
Set the package dirty flag for an asset

Args:
    object (Object): Object we want to set the package dirty state.
    dirty_state (bool): The dirty state, true mean the asset package need to be save.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.save_loaded_assets"></a>

#### save_loaded_assets

```python
def save_loaded_assets(assets_to_save: Array[Object],
                       only_if_is_dirty: bool = True) -> bool
```

x.save_loaded_assets(assets_to_save, only_if_is_dirty=True) -> bool
Save the packages the assets live in. All objects that live in the packages will be saved. Will try to checkout the files.

Args:
    assets_to_save (Array[Object]): Assets that we want to save.
    only_if_is_dirty (bool): Only checkout asset that are dirty.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.save_loaded_asset"></a>

#### save_loaded_asset

```python
def save_loaded_asset(asset_to_save: Object,
                      only_if_is_dirty: bool = True) -> bool
```

x.save_loaded_asset(asset_to_save, only_if_is_dirty=True) -> bool
Save the package the asset lives in. All objects that live in the package will be saved. Will try to checkout the file.

Args:
    asset_to_save (Object): Asset that we want to save.
    only_if_is_dirty (bool): Only checkout asset that are dirty.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.save_directory"></a>

#### save_directory

```python
def save_directory(directory_path: str,
                   only_if_is_dirty: bool = True,
                   recursive: bool = True) -> bool
```

x.save_directory(directory_path, only_if_is_dirty=True, recursive=True) -> bool
Save the packages the assets live in inside the directory. All objects that are in the directory will be saved.
Will try to checkout the file first. Assets will be loaded before being saved.

Args:
    directory_path (str): Directory that will be checked out and saved.
    only_if_is_dirty (bool): Only checkout asset that are dirty.
    recursive (bool): The search will be recursive and it will save the asset in the sub folders.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.save_asset"></a>

#### save_asset

```python
def save_asset(asset_to_save: str, only_if_is_dirty: bool = True) -> bool
```

x.save_asset(asset_to_save, only_if_is_dirty=True) -> bool
Save the packages the assets live in. All objects that live in the package will be saved.
Will try to checkout the file first. The Asset will be loaded before being saved.

Args:
    asset_to_save (str): Asset Path of the asset that we want to save.
    only_if_is_dirty (bool): Only checkout/save the asset if it's dirty.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.rename_loaded_asset"></a>

#### rename_loaded_asset

```python
def rename_loaded_asset(source_asset: Object,
                        destination_asset_path: str) -> bool
```

x.rename_loaded_asset(source_asset, destination_asset_path) -> bool
Rename an asset that is already loaded. Equivalent to a Move operation.
Will try to checkout the file.

Args:
    source_asset (Object): Asset that we want to copy from.
    destination_asset_path (str): Asset Path of the duplicated asset.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.rename_directory"></a>

#### rename_directory

```python
def rename_directory(source_directory_path: str,
                     destination_directory_path: str) -> bool
```

x.rename_directory(source_directory_path, destination_directory_path) -> bool
Rename a directory. Equivalent to a Move operation moving all contained assets.
Will try to checkout the files. The Assets will be loaded before being renamed.

Args:
    source_directory_path (str): Directory of the assets that we want to rename from.
    destination_directory_path (str): Directory of the renamed asset.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.rename_asset"></a>

#### rename_asset

```python
def rename_asset(source_asset_path: str, destination_asset_path: str) -> bool
```

x.rename_asset(source_asset_path, destination_asset_path) -> bool
Rename an asset. Equivalent to a Move operation.
Will try to checkout the file. The Asset will be loaded before being renamed.

Args:
    source_asset_path (str): Asset Path of the asset that we want to copy from.
    destination_asset_path (str): Asset Path of the renamed asset.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.remove_on_extract_asset_from_file"></a>

#### remove_on_extract_asset_from_file

```python
def remove_on_extract_asset_from_file(
        delegate: OnExtractAssetFromFileDynamic) -> None
```

x.remove_on_extract_asset_from_file(delegate) -> None
Call this to remove a callback added with AddOnExtractAssetFromFile.

Args:
    delegate (OnExtractAssetFromFileDynamic):

<a id="unreal.EditorAssetSubsystem.remove_metadata_tag"></a>

#### remove_metadata_tag

```python
def remove_metadata_tag(object: Object, tag: Name) -> None
```

x.remove_metadata_tag(object, tag) -> None
Remove the given tag from a loaded asset's metadata.

Args:
    object (Object): The object from which to retrieve the metadata.
    tag (Name): The tag to remove from the metadata.

<a id="unreal.EditorAssetSubsystem.make_directory"></a>

#### make_directory

```python
def make_directory(directory_path: str) -> bool
```

x.make_directory(directory_path) -> bool
Create a directory on disk.

Args:
    directory_path (str): Long Path Name of the directory.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.load_blueprint_class"></a>

#### load_blueprint_class

```python
def load_blueprint_class(asset_path: str) -> Class
```

x.load_blueprint_class(asset_path) -> type(Class)
Load a Blueprint asset and return its generated class. It will verify if the object is already loaded and only load it if it's necessary.

Args:
    asset_path (str): Asset Path of the Blueprint asset.

Returns:
    type(Class): Found or loaded class.

<a id="unreal.EditorAssetSubsystem.load_asset"></a>

#### load_asset

```python
def load_asset(asset_path: str) -> Object
```

x.load_asset(asset_path) -> Object
Load an asset. It will verify if the object is already loaded and only load it if it's necessary.

Args:
    asset_path (str): Asset Path of the asset to load

Returns:
    Object: Found or loaded asset.

<a id="unreal.EditorAssetSubsystem.list_assets_by_tag_value"></a>

#### list_assets_by_tag_value

```python
def list_assets_by_tag_value(tag_name: Name, tag_value: str) -> Array[str]
```

x.list_assets_by_tag_value(tag_name, tag_value) -> Array[str]
Return the list of all the assets that have the pair of Tag/Value.

Args:
    tag_name (Name): The tag associated with the assets requested.
    tag_value (str): The value associated with the assets requested.

Returns:
    Array[str]: The list of assets found.

<a id="unreal.EditorAssetSubsystem.list_assets"></a>

#### list_assets

```python
def list_assets(directory_path: str,
                recursive: bool = True,
                include_folder: bool = False) -> Array[str]
```

x.list_assets(directory_path, recursive=True, include_folder=False) -> Array[str]
Return the list of all the assets found in the DirectoryPath.

Args:
    directory_path (str): Directory path of the asset we want the list from.
    recursive (bool): The search will be recursive and will look in sub folders.
    include_folder (bool): The result will include folders name.

Returns:
    Array[str]: The list of assets found.

<a id="unreal.EditorAssetSubsystem.get_tag_values"></a>

#### get_tag_values

```python
def get_tag_values(asset_path: str) -> Map[Name, str]
```

x.get_tag_values(asset_path) -> Map[Name, str]
Gets all TagValues (from Asset Registry) associated with an (unloaded) asset as strings value.

Args:
    asset_path (str): Asset Path we are trying to find.

Returns:
    Map[Name, str]: The list of all TagNames & TagValues.

<a id="unreal.EditorAssetSubsystem.get_path_name_for_loaded_asset"></a>

#### get_path_name_for_loaded_asset

```python
def get_path_name_for_loaded_asset(loaded_asset: Object) -> str
```

x.get_path_name_for_loaded_asset(loaded_asset) -> str
Return a valid AssetPath for a loaded asset.
Similar to GetPathName(). The format will be: /Game/MyFolder/MyAsset.MyAsset

Args:
    loaded_asset (Object): The loaded asset to get the path of.

Returns:
    str: If valid, the asset Path of the loaded asset.

<a id="unreal.EditorAssetSubsystem.get_metadata_tag_values"></a>

#### get_metadata_tag_values

```python
def get_metadata_tag_values(object: Object) -> Map[Name, str]
```

x.get_metadata_tag_values(object) -> Map[Name, str]
Get all tags/values of a loaded asset's metadata.

Args:
    object (Object): The object from which to retrieve the metadata.

Returns:
    Map[Name, str]: The list of all Tags and Values.

<a id="unreal.EditorAssetSubsystem.get_metadata_tag"></a>

#### get_metadata_tag

```python
def get_metadata_tag(object: Object, tag: Name) -> str
```

x.get_metadata_tag(object, tag) -> str
Get the value associated with the given tag of a loaded asset's metadata.

Args:
    object (Object): The object from which to retrieve the metadata.
    tag (Name): The tag to find in the metadata.

Returns:
    str: The string value associated with the tag.

<a id="unreal.EditorAssetSubsystem.get_loaded_asset_filename_length_for_cooking"></a>

#### get_loaded_asset_filename_length_for_cooking

```python
def get_loaded_asset_filename_length_for_cooking(asset: Object) -> int
```

x.get_loaded_asset_filename_length_for_cooking(asset) -> int32
Returns the length of the computed cooked package name and path

Args:
    asset (Object): 

Returns:
    int32:

<a id="unreal.EditorAssetSubsystem.get_asset_filename_length_for_cooking"></a>

#### get_asset_filename_length_for_cooking

```python
def get_asset_filename_length_for_cooking(asset_path: str) -> int
```

x.get_asset_filename_length_for_cooking(asset_path) -> int32
Returns the length of the computed cooked package name and path

Args:
    asset_path (str): 

Returns:
    int32:

<a id="unreal.EditorAssetSubsystem.get_all_assets_by_meta_data_tags"></a>

#### get_all_assets_by_meta_data_tags

```python
def get_all_assets_by_meta_data_tags(
        required_tags: Set[Name],
        allowed_classes: Set[Class]) -> Array[AssetData]
```

x.get_all_assets_by_meta_data_tags(required_tags, allowed_classes) -> Array[AssetData]
Gets all assets which have the given tags.
params: RequiredTags The tags the assets should have
params: AllowedClasses The class types the contained assets should have

Args:
    required_tags (Set[Name]): 
    allowed_classes (Set[type(Class)]): 

Returns:
    Array[AssetData]:

<a id="unreal.EditorAssetSubsystem.find_package_referencers_for_asset"></a>

#### find_package_referencers_for_asset

```python
def find_package_referencers_for_asset(asset_path: str,
                                       load_assets_to_confirm: bool = False
                                       ) -> Array[str]
```

x.find_package_referencers_for_asset(asset_path, load_assets_to_confirm=False) -> Array[str]
Find Package Referencers for an asset. Only Soft and Hard dependencies will be looked for.
Soft are dependencies which don't need to be loaded for the object to be used.
Hard are dependencies which are required for correct usage of the source asset and must be loaded at the same time.
Other references may exist. The asset may be currently used in memory by another asset, by the editor or by code.
Package dependencies are cached with the asset. False positives can happen until all the assets are loaded and re-saved.

Args:
    asset_path (str): Asset Path of the asset that we are looking for.
    load_assets_to_confirm (bool): Whether the asset and any potential referencers will be loaded to confirm the dependencies.

Returns:
    Array[str]: The package paths of the referencers.

<a id="unreal.EditorAssetSubsystem.find_asset_data"></a>

#### find_asset_data

```python
def find_asset_data(asset_path: str) -> AssetData
```

x.find_asset_data(asset_path) -> AssetData
Return the AssetData for the Asset that can then be used with AssetRegistryHelpers.

Args:
    asset_path (str): Asset Path to retrieve data from.

Returns:
    AssetData: The AssetData found.

<a id="unreal.EditorAssetSubsystem.duplicate_loaded_asset"></a>

#### duplicate_loaded_asset

```python
def duplicate_loaded_asset(source_asset: Object,
                           destination_asset_path: str) -> Object
```

x.duplicate_loaded_asset(source_asset, destination_asset_path) -> Object
Duplicate an asset that is already loaded. Will try to checkout the file.

Args:
    source_asset (Object): Asset that we want to copy from.
    destination_asset_path (str): Asset Path of the duplicated asset.

Returns:
    Object: The duplicated object if the operation succeeds

<a id="unreal.EditorAssetSubsystem.duplicate_directory"></a>

#### duplicate_directory

```python
def duplicate_directory(source_directory_path: str,
                        destination_directory_path: str) -> bool
```

x.duplicate_directory(source_directory_path, destination_directory_path) -> bool
Duplicate a directory and the assets in it.
Will try to checkout the files. The Assets will be loaded before being duplicated.

Args:
    source_directory_path (str): Directory of the assets that we want to duplicate from.
    destination_directory_path (str): Directory of the duplicated asset.

Returns:
    bool: The duplicated object if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.duplicate_asset"></a>

#### duplicate_asset

```python
def duplicate_asset(source_asset_path: str,
                    destination_asset_path: str) -> Object
```

x.duplicate_asset(source_asset_path, destination_asset_path) -> Object
Duplicate an asset. Will try to checkout the file. The Asset will be loaded before being duplicated.

Args:
    source_asset_path (str): Asset Path of the asset that we want to copy from.
    destination_asset_path (str): Asset Path of the duplicated asset.

Returns:
    Object: The duplicated object if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.does_directory_exist"></a>

#### does_directory_exist

```python
def does_directory_exist(directory_path: str) -> bool
```

x.does_directory_exist(directory_path) -> bool
Check if a directory exists.

Args:
    directory_path (str): Long Path Name of the directory.

Returns:
    bool: True if it does exist and it is valid.

<a id="unreal.EditorAssetSubsystem.does_directory_contain_assets"></a>

#### does_directory_contain_assets

```python
def does_directory_contain_assets(directory_path: str,
                                  recursive: bool = True) -> bool
```

x.does_directory_contain_assets(directory_path, recursive=True) -> bool
Check if a directory contains any assets.

Args:
    directory_path (str): Long Path Name of the directory.
    recursive (bool): 

Returns:
    bool: True if there is any assets.

<a id="unreal.EditorAssetSubsystem.does_asset_exist"></a>

#### does_asset_exist

```python
def does_asset_exist(asset_path: str) -> bool
```

x.does_asset_exist(asset_path) -> bool
Check if an asset exists in the Asset Registry.

Args:
    asset_path (str): Asset Path to check for existence.

Returns:
    bool: True if the asset exists and is valid.

<a id="unreal.EditorAssetSubsystem.do_assets_exist"></a>

#### do_assets_exist

```python
def do_assets_exist(asset_paths: Array[str]) -> bool
```

x.do_assets_exist(asset_paths) -> bool
Check if assets exist in the Asset Registry.

Args:
    asset_paths (Array[str]): Asset Paths of the assets to check for existence.

Returns:
    bool: True if all assets exist and are valid.

<a id="unreal.EditorAssetSubsystem.delete_loaded_assets"></a>

#### delete_loaded_assets

```python
def delete_loaded_assets(assets_to_delete: Array[Object]) -> bool
```

x.delete_loaded_assets(assets_to_delete) -> bool
Delete assets that are already loaded.
This is a Force Delete. It does not check if the assets have references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the files as deleted.

Args:
    assets_to_delete (Array[Object]): Loaded assets to delete.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.delete_loaded_asset"></a>

#### delete_loaded_asset

```python
def delete_loaded_asset(asset_to_delete: Object) -> bool
```

x.delete_loaded_asset(asset_to_delete) -> bool
Delete an asset that is already loaded.
This is a Force Delete. It does not check if the asset has references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted.

Args:
    asset_to_delete (Object): Asset to delete.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.delete_directory"></a>

#### delete_directory

```python
def delete_directory(directory_path: str) -> bool
```

x.delete_directory(directory_path) -> bool
Delete the packages inside a directory. If the directory is then empty, delete the directory.
This is a Force Delete. It does not check if the assets have references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted. Assets will be loaded before being deleted.
The search is always recursive. It will try to delete the sub folders.

Args:
    directory_path (str): Directory that will be marked for deletion and deleted.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.delete_asset"></a>

#### delete_asset

```python
def delete_asset(asset_path_to_delete: str) -> bool
```

x.delete_asset(asset_path_to_delete) -> bool
Delete the package an asset is in. All objects in the package will be deleted.
This is a Force Delete. It does not check if the asset has references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted. The Asset will be loaded before being deleted.

Args:
    asset_path_to_delete (str): Asset Path of the asset to delete.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.consolidate_assets"></a>

#### consolidate_assets

```python
def consolidate_assets(asset_to_consolidate_to: Object,
                       assets_to_consolidate: Array[Object]) -> bool
```

x.consolidate_assets(asset_to_consolidate_to, assets_to_consolidate) -> bool
Consolidates assets by replacing all references/uses of the provided AssetsToConsolidate with references to AssetToConsolidateTo.
This is useful when you want all references of assets to be replaced by a single asset.
The function first attempts to directly replace all relevant references located within objects that are already loaded and in memory.
Next, it deletes the AssetsToConsolidate, leaving behind object redirectors to AssetToConsolidateTo.
note: The AssetsToConsolidate are DELETED by this function.
note: Modified objects will be saved if the operation succeeds.

Args:
    asset_to_consolidate_to (Object): Asset to which all references of the AssetsToConsolidate will instead refer to after this operation completes.
    assets_to_consolidate (Array[Object]): All references to these assets will be modified to reference AssetToConsolidateTo instead.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.checkout_loaded_assets"></a>

#### checkout_loaded_assets

```python
def checkout_loaded_assets(assets_to_checkout: Array[Object]) -> bool
```

x.checkout_loaded_assets(assets_to_checkout) -> bool
Checkout the assets.

Args:
    assets_to_checkout (Array[Object]): Assets to checkout.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.checkout_loaded_asset"></a>

#### checkout_loaded_asset

```python
def checkout_loaded_asset(asset_to_checkout: Object) -> bool
```

x.checkout_loaded_asset(asset_to_checkout) -> bool
Checkout the asset corresponding to an object.

Args:
    asset_to_checkout (Object): Asset to checkout.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.checkout_directory"></a>

#### checkout_directory

```python
def checkout_directory(directory_path: str, recursive: bool = True) -> bool
```

x.checkout_directory(directory_path, recursive=True) -> bool
Checkout all assets in a directory. It will load the assets if needed.
All objects that are in the directory will be checked out. Assets will be loaded before being checked out.

Args:
    directory_path (str): Directory of the assets to be checked out.
    recursive (bool): If the AssetPath is a folder, the search will be recursive and will checkout the assets in the sub folders.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.checkout_asset"></a>

#### checkout_asset

```python
def checkout_asset(asset_to_checkout: str) -> bool
```

x.checkout_asset(asset_to_checkout) -> bool
Checkout an asset.

Args:
    asset_to_checkout (str): Asset Path of the asset that we want to checkout.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetSubsystem.add_on_extract_asset_from_file"></a>

#### add_on_extract_asset_from_file

```python
def add_on_extract_asset_from_file(
        delegate: OnExtractAssetFromFileDynamic) -> None
```

x.add_on_extract_asset_from_file(delegate) -> None
Call this to add a callback to extract an asset from a file,
for example from a drag and drop operation.

Args:
    delegate (OnExtractAssetFromFileDynamic):

<a id="unreal.EditorCompositeSection"></a>