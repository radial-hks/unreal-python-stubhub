## EditorAssetLibrary Objects

```python
class EditorAssetLibrary(BlueprintFunctionLibrary)
```

Utility class to do most of the common functionalities with the ContentBrowser.
The AssetRegistryHelpers class has more complex utilities. Use FindAssetData to get a FAssetData from an Asset Path.
The Asset Path can be represented by
            ie. (Reference/Text Path)       StaticMesh'/Game/MyFolder/MyAsset.MyAsset'
            ie. (Full Name)                         StaticMesh /Game/MyFolder/MyAsset.MyAsset
            ie. (Path Name)                         /Game/MyFolder/MyAsset.MyAsset
            ie. (Package Name)                      /Game/MyFolder/MyAsset
The Directory Path can be represented by
            ie. /Game/MyNewFolder/
            ie. /Game/MyNewFolder
All operations can be slow. The editor should not be in play in editor mode. It will not work on assets of the type level.

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorAssetLibrary.h

<a id="unreal.EditorAssetLibrary.sync_browser_to_objects"></a>

#### sync_browser_to_objects

```python
@classmethod
def sync_browser_to_objects(cls, asset_paths: Array[str]) -> None
```

X.sync_browser_to_objects(asset_paths) -> None
Browses to the associated asset and selects it in the most recently used Content Browser (summoning one if necessary)
This is an asynchronous operation that can take a couple of frames to resolve the request

Args:
    asset_paths (Array[str]): The list of asset paths to sync to in the Content Browser

<a id="unreal.EditorAssetLibrary.set_metadata_tag"></a>

#### set_metadata_tag

```python
@classmethod
def set_metadata_tag(cls, object: Object, tag: Name, value: str) -> None
```

X.set_metadata_tag(object, tag, value) -> None
Set the value associated with a given tag of a loaded asset's metadata.

Args:
    object (Object): The object from which to retrieve the metadata.
    tag (Name): The tag to set in the metadata.
    value (str): The string value to associate with the tag.

<a id="unreal.EditorAssetLibrary.save_loaded_assets"></a>

#### save_loaded_assets

```python
@classmethod
def save_loaded_assets(cls,
                       assets_to_save: Array[Object],
                       only_if_is_dirty: bool = True) -> bool
```

X.save_loaded_assets(assets_to_save, only_if_is_dirty=True) -> bool
Save the packages the assets live in. All objects that live in the package will be saved. Will try to checkout the files.

Args:
    assets_to_save (Array[Object]): 
    only_if_is_dirty (bool): Only checkout asset that are dirty.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.save_loaded_asset"></a>

#### save_loaded_asset

```python
@classmethod
def save_loaded_asset(cls,
                      asset_to_save: Object,
                      only_if_is_dirty: bool = True) -> bool
```

X.save_loaded_asset(asset_to_save, only_if_is_dirty=True) -> bool
Save the packages the assets live in. All objects that live in the package will be saved. Will try to checkout the file.

Args:
    asset_to_save (Object): Asset that we want to save.
    only_if_is_dirty (bool): Only checkout asset that are dirty.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.save_directory"></a>

#### save_directory

```python
@classmethod
def save_directory(cls,
                   directory_path: str,
                   only_if_is_dirty: bool = True,
                   recursive: bool = True) -> bool
```

X.save_directory(directory_path, only_if_is_dirty=True, recursive=True) -> bool
Save the packages the assets live in inside the directory. All objects that are in the directory will be saved.
Will try to checkout the file first. Assets will be loaded before being saved.

Args:
    directory_path (str): Directory that will be checked out and saved.
    only_if_is_dirty (bool): Only checkout asset that are dirty.
    recursive (bool): The search will be recursive and it will save the asset in the sub folders.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.save_asset"></a>

#### save_asset

```python
@classmethod
def save_asset(cls, asset_to_save: str, only_if_is_dirty: bool = True) -> bool
```

X.save_asset(asset_to_save, only_if_is_dirty=True) -> bool
Save the packages the assets live in. All objects that live in the package will be saved.
Will try to checkout the file first. The Asset will be loaded before being saved.

Args:
    asset_to_save (str): 
    only_if_is_dirty (bool): Only checkout/save the asset if it's dirty.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.rename_loaded_asset"></a>

#### rename_loaded_asset

```python
@classmethod
def rename_loaded_asset(cls, source_asset: Object,
                        destination_asset_path: str) -> bool
```

X.rename_loaded_asset(source_asset, destination_asset_path) -> bool
Rename an asset from the Content Browser that is already loaded.
Equivalent to a Move operation. Will try to checkout the files.

Args:
    source_asset (Object): Asset that we want to copy from.
    destination_asset_path (str): Asset Path of the duplicated asset.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.rename_directory"></a>

#### rename_directory

```python
@classmethod
def rename_directory(cls, source_directory_path: str,
                     destination_directory_path: str) -> bool
```

X.rename_directory(source_directory_path, destination_directory_path) -> bool
Rename assets from the Content Browser that are in the folder.
Equivalent to a Move operation. Will try to checkout the files. The Assets will be loaded before being renamed.

Args:
    source_directory_path (str): Directory of the assets that we want to rename from.
    destination_directory_path (str): Directory of the renamed asset.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.rename_asset"></a>

#### rename_asset

```python
@classmethod
def rename_asset(cls, source_asset_path: str,
                 destination_asset_path: str) -> bool
```

X.rename_asset(source_asset_path, destination_asset_path) -> bool
Rename an asset from the Content Browser. Equivalent to a Move operation.
Will try to checkout the file. The Asset will be loaded before being renamed.

Args:
    source_asset_path (str): Asset Path of the asset that we want to copy from.
    destination_asset_path (str): Asset Path of the renamed asset.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.remove_metadata_tag"></a>

#### remove_metadata_tag

```python
@classmethod
def remove_metadata_tag(cls, object: Object, tag: Name) -> None
```

X.remove_metadata_tag(object, tag) -> None
Remove the given tag from a loaded asset's metadata.

Args:
    object (Object): The object from which to retrieve the metadata.
    tag (Name): The tag to remove from the metadata.

<a id="unreal.EditorAssetLibrary.make_directory"></a>

#### make_directory

```python
@classmethod
def make_directory(cls, directory_path: str) -> bool
```

X.make_directory(directory_path) -> bool
Create the directory on disk and in the Content Browser.

Args:
    directory_path (str): Long Path Name of the directory.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.load_blueprint_class"></a>

#### load_blueprint_class

```python
@classmethod
def load_blueprint_class(cls, asset_path: str) -> Class
```

X.load_blueprint_class(asset_path) -> type(Class)
Load a Blueprint asset from the Content Browser and return its generated class. It will verify if the object is already loaded and only load it if it's necessary.

Args:
    asset_path (str): Asset Path of the Blueprint asset.

Returns:
    type(Class): Found or loaded class.

<a id="unreal.EditorAssetLibrary.load_asset"></a>

#### load_asset

```python
@classmethod
def load_asset(cls, asset_path: str) -> Object
```

X.load_asset(asset_path) -> Object
Load an asset from the Content Browser. It will verify if the object is already loaded and only load it if it's necessary.

Args:
    asset_path (str): Asset Path of the asset (that is not a level).

Returns:
    Object: Found or loaded asset.

<a id="unreal.EditorAssetLibrary.list_assets"></a>

#### list_assets

```python
@classmethod
def list_assets(cls,
                directory_path: str,
                recursive: bool = True,
                include_folder: bool = False) -> Array[str]
```

X.list_assets(directory_path, recursive=True, include_folder=False) -> Array[str]
Return the list of all the assets found in the DirectoryPath.

Args:
    directory_path (str): Directory path of the asset we want the list from.
    recursive (bool): The search will be recursive and will look in sub folders.
    include_folder (bool): The result will include folders name.

Returns:
    Array[str]: The list of asset found.

<a id="unreal.EditorAssetLibrary.list_asset_by_tag_value"></a>

#### list_asset_by_tag_value

```python
@classmethod
def list_asset_by_tag_value(cls, tag_name: Name, tag_value: str) -> Array[str]
```

X.list_asset_by_tag_value(tag_name, tag_value) -> Array[str]
Return the list of all the assets that have the pair of Tag/Value.

Args:
    tag_name (Name): The tag associated with the assets requested.
    tag_value (str): The value associated with the assets requested.

Returns:
    Array[str]: The list of asset found.

<a id="unreal.EditorAssetLibrary.get_tag_values"></a>

#### get_tag_values

```python
@classmethod
def get_tag_values(cls, asset_path: str) -> Map[Name, str]
```

X.get_tag_values(asset_path) -> Map[Name, str]
Gets all TagValues (from Asset Registry) associated with an (unloaded) asset as strings value.

Args:
    asset_path (str): Asset Path we are trying to find.

Returns:
    Map[Name, str]: The list of all TagName & TagValue.

<a id="unreal.EditorAssetLibrary.get_project_root_asset_directory"></a>

#### get_project_root_asset_directory

```python
@classmethod
def get_project_root_asset_directory(cls) -> str
```

X.get_project_root_asset_directory() -> str
Historically, all project assets were stored in the logical "/Game/" directory
when using plugins or UEFN projects, we want to ease asset reuse, and so the ambiguous
"/Game/" directory is untenable. This function will return the useful project name.

Returns:
    str: The current project name in UEFN, otherwise /Game/ for .uprojects

<a id="unreal.EditorAssetLibrary.get_path_name_for_loaded_asset"></a>

#### get_path_name_for_loaded_asset

```python
@classmethod
def get_path_name_for_loaded_asset(cls, loaded_asset: Object) -> str
```

X.get_path_name_for_loaded_asset(loaded_asset) -> str
Return a valid AssetPath for a loaded asset. The asset need to be a valid asset in the Content Browser.
Similar to GetPathName(). The format will be: /Game/MyFolder/MyAsset.MyAsset

Args:
    loaded_asset (Object): Loaded Asset that exist in the Content Browser.

Returns:
    str: If valid, the asset Path of the loaded asset.

<a id="unreal.EditorAssetLibrary.get_package_for_object"></a>

#### get_package_for_object

```python
@classmethod
def get_package_for_object(cls, object: Object) -> Package
```

X.get_package_for_object(object) -> Package
Returns the object's containing package

Args:
    object (Object): 

Returns:
    Package:

<a id="unreal.EditorAssetLibrary.get_metadata_tag_values"></a>

#### get_metadata_tag_values

```python
@classmethod
def get_metadata_tag_values(cls, object: Object) -> Map[Name, str]
```

X.get_metadata_tag_values(object) -> Map[Name, str]
Get all tags/values of a loaded asset's metadata.

Args:
    object (Object): The object from which to retrieve the metadata.

Returns:
    Map[Name, str]: The list of all Tags and Values.

<a id="unreal.EditorAssetLibrary.get_metadata_tag"></a>

#### get_metadata_tag

```python
@classmethod
def get_metadata_tag(cls, object: Object, tag: Name) -> str
```

X.get_metadata_tag(object, tag) -> str
Get the value associated with the given tag of a loaded asset's metadata.

Args:
    object (Object): The object from which to retrieve the metadata.
    tag (Name): The tag to find in the metadata.

Returns:
    str: The string value associated with the tag.

<a id="unreal.EditorAssetLibrary.find_package_referencers_for_asset"></a>

#### find_package_referencers_for_asset

```python
@classmethod
def find_package_referencers_for_asset(
        cls,
        asset_path: str,
        load_assets_to_confirm: bool = False) -> Array[str]
```

X.find_package_referencers_for_asset(asset_path, load_assets_to_confirm=False) -> Array[str]
Find Package Referencers for an asset. Only Soft and Hard dependencies would be looked for.
Soft are dependencies which don't need to be loaded for the object to be used.
Had are dependencies which are required for correct usage of the source asset and must be loaded at the same time.
Other references may exist. The asset may be currently used in memory by another asset, by the editor or by code.
Package dependencies are cached with the asset. False positive can happen until all the assets are loaded and re-saved.

Args:
    asset_path (str): Asset Path of the asset that we are looking for (that is not a level).
    load_assets_to_confirm (bool): The asset and the referencers will be loaded (if not a level) to confirm the dependencies.

Returns:
    Array[str]: The package path of the referencers.

<a id="unreal.EditorAssetLibrary.find_asset_data"></a>

#### find_asset_data

```python
@classmethod
def find_asset_data(cls, asset_path: str) -> AssetData
```

X.find_asset_data(asset_path) -> AssetData
Return the AssetData for the Asset that can then be used with the more complex lib AssetRegistryHelpers.

Args:
    asset_path (str): Asset Path we are trying to find.

Returns:
    AssetData: The AssetData found.

<a id="unreal.EditorAssetLibrary.duplicate_loaded_asset"></a>

#### duplicate_loaded_asset

```python
@classmethod
def duplicate_loaded_asset(cls, source_asset: Object,
                           destination_asset_path: str) -> Object
```

X.duplicate_loaded_asset(source_asset, destination_asset_path) -> Object
Duplicate an asset from the Content Browser that is already loaded. Will try to checkout the file.

Args:
    source_asset (Object): Asset that we want to copy from.
    destination_asset_path (str): Asset Path of the duplicated asset.

Returns:
    Object: The duplicated object if the operation succeeds

<a id="unreal.EditorAssetLibrary.duplicate_directory"></a>

#### duplicate_directory

```python
@classmethod
def duplicate_directory(cls, source_directory_path: str,
                        destination_directory_path: str) -> bool
```

X.duplicate_directory(source_directory_path, destination_directory_path) -> bool
Duplicate asset from the Content Browser that are in the folder.
Will try to checkout the files. The Assets will be loaded before being duplicated.

Args:
    source_directory_path (str): Directory of the assets that we want to duplicate from.
    destination_directory_path (str): Directory of the duplicated asset.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.duplicate_asset"></a>

#### duplicate_asset

```python
@classmethod
def duplicate_asset(cls, source_asset_path: str,
                    destination_asset_path: str) -> Object
```

X.duplicate_asset(source_asset_path, destination_asset_path) -> Object
Duplicate an asset from the Content Browser. Will try to checkout the file. The Asset will be loaded before being duplicated.

Args:
    source_asset_path (str): Asset Path of the asset that we want to copy from.
    destination_asset_path (str): Asset Path of the duplicated asset.

Returns:
    Object: The duplicated object if the operation succeeds.

<a id="unreal.EditorAssetLibrary.does_directory_have_assets"></a>

#### does_directory_have_assets

```python
@classmethod
def does_directory_have_assets(cls,
                               directory_path: str,
                               recursive: bool = True) -> bool
```

X.does_directory_have_assets(directory_path, recursive=True) -> bool
Check if there any asset that exist in the directory.

Args:
    directory_path (str): Long Path Name of the directory.
    recursive (bool): 

Returns:
    bool: True if there is any assets.

<a id="unreal.EditorAssetLibrary.does_directory_exist"></a>

#### does_directory_exist

```python
@classmethod
def does_directory_exist(cls, directory_path: str) -> bool
```

X.does_directory_exist(directory_path) -> bool
Check is the directory exist in the Content Browser.

Args:
    directory_path (str): Long Path Name of the directory.

Returns:
    bool: True if it does exist and it is valid.

<a id="unreal.EditorAssetLibrary.does_asset_exist"></a>

#### does_asset_exist

```python
@classmethod
def does_asset_exist(cls, asset_path: str) -> bool
```

X.does_asset_exist(asset_path) -> bool
Check if the asset exists in the Content Browser.

Args:
    asset_path (str): Asset Path of the asset (that is not a level).

Returns:
    bool: True if it does exist and it is valid.

<a id="unreal.EditorAssetLibrary.do_assets_exist"></a>

#### do_assets_exist

```python
@classmethod
def do_assets_exist(cls, asset_paths: Array[str]) -> bool
```

X.do_assets_exist(asset_paths) -> bool
Check if the assets exist in the Content Browser.

Args:
    asset_paths (Array[str]): Asset Path of the assets (that are not a level).

Returns:
    bool: True if they exist and it is valid.

<a id="unreal.EditorAssetLibrary.delete_loaded_assets"></a>

#### delete_loaded_assets

```python
@classmethod
def delete_loaded_assets(cls, assets_to_delete: Array[Object]) -> bool
```

X.delete_loaded_assets(assets_to_delete) -> bool
Delete assets from the Content Browser that are already loaded.
This is a Force Delete. It doesn't check if the assets have references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the files as deleted.

Args:
    assets_to_delete (Array[Object]): Assets that we want to delete.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.delete_loaded_asset"></a>

#### delete_loaded_asset

```python
@classmethod
def delete_loaded_asset(cls, asset_to_delete: Object) -> bool
```

X.delete_loaded_asset(asset_to_delete) -> bool
Delete an asset from the Content Browser that is already loaded.
This is a Force Delete. It doesn't check if the asset has references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted.

Args:
    asset_to_delete (Object): Asset that we want to delete.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.delete_directory"></a>

#### delete_directory

```python
@classmethod
def delete_directory(cls, directory_path: str) -> bool
```

X.delete_directory(directory_path) -> bool
Delete the packages inside a directory. If the directory is then empty, delete the directory.
This is a Force Delete. It doesn't check if the assets have references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted. Assets will be loaded before being deleted.
The search is always recursive. It will try to delete the sub folders.

Args:
    directory_path (str): Directory that will be mark for delete and deleted.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.delete_asset"></a>

#### delete_asset

```python
@classmethod
def delete_asset(cls, asset_path_to_delete: str) -> bool
```

X.delete_asset(asset_path_to_delete) -> bool
Delete the package the assets live in. All objects that live in the package will be deleted.
This is a Force Delete. It doesn't check if the asset has references in other Levels or by Actors.
It will close all the asset editors and may clear the Transaction buffer (Undo History).
Will try to mark the file as deleted. The Asset will be loaded before being deleted.

Args:
    asset_path_to_delete (str): Asset Path of the asset that we want to delete.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.consolidate_assets"></a>

#### consolidate_assets

```python
@classmethod
def consolidate_assets(cls, asset_to_consolidate_to: Object,
                       assets_to_consolidate: Array[Object]) -> bool
```

X.consolidate_assets(asset_to_consolidate_to, assets_to_consolidate) -> bool
Consolidates an asset by replacing all references/uses of the provided AssetsToConsolidate with references to AssetToConsolidateTo.
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

<a id="unreal.EditorAssetLibrary.checkout_loaded_assets"></a>

#### checkout_loaded_assets

```python
@classmethod
def checkout_loaded_assets(cls, assets_to_checkout: Array[Object]) -> bool
```

X.checkout_loaded_assets(assets_to_checkout) -> bool
Checkout the assets from the Content Browser.

Args:
    assets_to_checkout (Array[Object]): 

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.checkout_loaded_asset"></a>

#### checkout_loaded_asset

```python
@classmethod
def checkout_loaded_asset(cls, asset_to_checkout: Object) -> bool
```

X.checkout_loaded_asset(asset_to_checkout) -> bool
Checkout the asset from the Content Browser.

Args:
    asset_to_checkout (Object): Asset to checkout.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.checkout_directory"></a>

#### checkout_directory

```python
@classmethod
def checkout_directory(cls,
                       directory_path: str,
                       recursive: bool = True) -> bool
```

X.checkout_directory(directory_path, recursive=True) -> bool
Checkout assets from the Content Browser. It will load the assets if needed.
All objects that are in the directory will be checkout. Assets will be loaded before being checkout.

Args:
    directory_path (str): Directory of the assets that to checkout.
    recursive (bool): If the AssetPath is a folder, the search will be recursive and will checkout the asset in the sub folders.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorAssetLibrary.checkout_asset"></a>

#### checkout_asset

```python
@classmethod
def checkout_asset(cls, asset_to_checkout: str) -> bool
```

X.checkout_asset(asset_to_checkout) -> bool
Checkout the asset from the Content Browser.

Args:
    asset_to_checkout (str): Asset Path of the asset that we want to checkout.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorDialog"></a>