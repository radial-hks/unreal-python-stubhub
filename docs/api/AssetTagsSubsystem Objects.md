## AssetTagsSubsystem Objects

```python
class AssetTagsSubsystem(EngineSubsystem)
```

Asset Tags Subsystem

**C++ Source:**

- **Plugin**: AssetTags
- **Module**: AssetTags
- **File**: AssetTagsSubsystem.h

<a id="unreal.AssetTagsSubsystem.reparent_collection"></a>

#### reparent_collection

```python
def reparent_collection(name: Name, new_parent_name: Name) -> bool
```

x.reparent_collection(name, new_parent_name) -> bool
Re-parent the given collection.

Args:
    name (Name): Name of the collection to re-parent.
    new_parent_name (Name): Name of the new parent collection, or None to have the collection become a root collection.

Returns:
    bool: True if the collection was renamed, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.rename_collection"></a>

#### rename_collection

```python
def rename_collection(name: Name, new_name: Name) -> bool
```

x.rename_collection(name, new_name) -> bool
Rename the given collection.

Args:
    name (Name): Name of the collection to rename.
    new_name (Name): Name to give to the collection.

Returns:
    bool: True if the collection was renamed, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.remove_assets_from_collection"></a>

#### remove_assets_from_collection

```python
def remove_assets_from_collection(name: Name,
                                  asset_path_names: Array[Name]) -> bool
```

x.remove_assets_from_collection(name, asset_path_names) -> bool
Remove Assets from Collection

Args:
    name (Name): 
    asset_path_names (Array[Name]): 

Returns:
    bool:

<a id="unreal.AssetTagsSubsystem.remove_asset_ptrs_from_collection"></a>

#### remove_asset_ptrs_from_collection

```python
def remove_asset_ptrs_from_collection(name: Name,
                                      asset_ptrs: Array[Object]) -> bool
```

x.remove_asset_ptrs_from_collection(name, asset_ptrs) -> bool
Remove the given assets from the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_ptrs (Array[Object]): Assets to remove.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.remove_asset_ptr_from_collection"></a>

#### remove_asset_ptr_from_collection

```python
def remove_asset_ptr_from_collection(name: Name, asset_ptr: Object) -> bool
```

x.remove_asset_ptr_from_collection(name, asset_ptr) -> bool
Remove the given asset from the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_ptr (Object): Asset to remove.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.remove_asset_from_collection"></a>

#### remove_asset_from_collection

```python
def remove_asset_from_collection(name: Name, asset_path_name: Name) -> bool
```

x.remove_asset_from_collection(name, asset_path_name) -> bool
Remove Asset from Collection

Args:
    name (Name): 
    asset_path_name (Name): 

Returns:
    bool:

<a id="unreal.AssetTagsSubsystem.remove_asset_datas_from_collection"></a>

#### remove_asset_datas_from_collection

```python
def remove_asset_datas_from_collection(name: Name,
                                       asset_datas: Array[AssetData]) -> bool
```

x.remove_asset_datas_from_collection(name, asset_datas) -> bool
Remove the given assets from the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_datas (Array[AssetData]): Assets to remove.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.remove_asset_data_from_collection"></a>

#### remove_asset_data_from_collection

```python
def remove_asset_data_from_collection(name: Name,
                                      asset_data: AssetData) -> bool
```

x.remove_asset_data_from_collection(name, asset_data) -> bool
Remove the given asset from the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_data (AssetData): Asset to remove.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.k2_remove_assets_from_collection"></a>

#### k2_remove_assets_from_collection

```python
def k2_remove_assets_from_collection(
        name: Name, asset_paths: Array[SoftObjectPath]) -> bool
```

x.k2_remove_assets_from_collection(name, asset_paths) -> bool
Remove the given assets from the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_paths (Array[SoftObjectPath]): 

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.k2_remove_asset_from_collection"></a>

#### k2_remove_asset_from_collection

```python
def k2_remove_asset_from_collection(name: Name,
                                    asset_path: SoftObjectPath) -> bool
```

x.k2_remove_asset_from_collection(name, asset_path) -> bool
Remove the given asset from the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_path (SoftObjectPath): Asset to remove (its path, eg) /Game/MyFolder/MyAsset.MyAsset).

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.k2_get_collections_containing_asset"></a>

#### k2_get_collections_containing_asset

```python
def k2_get_collections_containing_asset(
        asset_path: SoftObjectPath) -> Array[Name]
```

x.k2_get_collections_containing_asset(asset_path) -> Array[Name]
Get the names of the collections that contain the given asset.

Args:
    asset_path (SoftObjectPath): 

Returns:
    Array[Name]: Names of the collections that contain the asset.

<a id="unreal.AssetTagsSubsystem.k2_add_asset_to_collection"></a>

#### k2_add_asset_to_collection

```python
def k2_add_asset_to_collection(name: Name, asset_path: SoftObjectPath) -> bool
```

x.k2_add_asset_to_collection(name, asset_path) -> bool
Add the given asset to the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_path (SoftObjectPath): 

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.k2_add_assets_to_collection"></a>

#### k2_add_assets_to_collection

```python
def k2_add_assets_to_collection(name: Name,
                                asset_paths: Array[SoftObjectPath]) -> bool
```

x.k2_add_assets_to_collection(name, asset_paths) -> bool
Add the given assets to the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_paths (Array[SoftObjectPath]): 

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.get_collections_containing_asset_ptr"></a>

#### get_collections_containing_asset_ptr

```python
def get_collections_containing_asset_ptr(asset_ptr: Object) -> Array[Name]
```

x.get_collections_containing_asset_ptr(asset_ptr) -> Array[Name]
Get the names of the collections that contain the given asset.

Args:
    asset_ptr (Object): Asset to test.

Returns:
    Array[Name]: Names of the collections that contain the asset.

<a id="unreal.AssetTagsSubsystem.get_collections_containing_asset_data"></a>

#### get_collections_containing_asset_data

```python
def get_collections_containing_asset_data(
        asset_data: AssetData) -> Array[Name]
```

x.get_collections_containing_asset_data(asset_data) -> Array[Name]
Get the names of the collections that contain the given asset.

Args:
    asset_data (AssetData): Asset to test.

Returns:
    Array[Name]: Names of the collections that contain the asset.

<a id="unreal.AssetTagsSubsystem.get_collections_containing_asset"></a>

#### get_collections_containing_asset

```python
def get_collections_containing_asset(asset_path_name: Name) -> Array[Name]
```

x.get_collections_containing_asset(asset_path_name) -> Array[Name]
Get Collections Containing Asset

Args:
    asset_path_name (Name): 

Returns:
    Array[Name]:

<a id="unreal.AssetTagsSubsystem.get_collections"></a>

#### get_collections

```python
def get_collections() -> Array[Name]
```

x.get_collections() -> Array[Name]
Get the names of all available collections.

Returns:
    Array[Name]: Names of all available collections.

<a id="unreal.AssetTagsSubsystem.get_assets_in_collection"></a>

#### get_assets_in_collection

```python
def get_assets_in_collection(name: Name) -> Array[AssetData]
```

x.get_assets_in_collection(name) -> Array[AssetData]
Get the assets in the given collection.

Args:
    name (Name): Name of the collection to test.

Returns:
    Array[AssetData]: Assets in the given collection.

<a id="unreal.AssetTagsSubsystem.empty_collection"></a>

#### empty_collection

```python
def empty_collection(name: Name) -> bool
```

x.empty_collection(name) -> bool
Remove all assets from the given collection.

Args:
    name (Name): Name of the collection to modify.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.destroy_collection"></a>

#### destroy_collection

```python
def destroy_collection(name: Name) -> bool
```

x.destroy_collection(name) -> bool
Destroy the given collection.

Args:
    name (Name): Name of the collection to destroy.

Returns:
    bool: True if the collection was destroyed, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.create_collection"></a>

#### create_collection

```python
def create_collection(name: Name, share_type: CollectionShareType) -> bool
```

x.create_collection(name, share_type) -> bool
Create a new collection with the given name and share type.

Args:
    name (Name): Name to give to the collection.
    share_type (CollectionShareType): Whether the collection should be local, private, or shared?

Returns:
    bool: True if the collection was created, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.collection_exists"></a>

#### collection_exists

```python
def collection_exists(name: Name) -> bool
```

x.collection_exists(name) -> bool
Check whether the given collection exists.

Args:
    name (Name): Name of the collection to test.

Returns:
    bool: True if the collection exists, false otherwise.

<a id="unreal.AssetTagsSubsystem.add_asset_to_collection"></a>

#### add_asset_to_collection

```python
def add_asset_to_collection(name: Name, asset_path_name: Name) -> bool
```

x.add_asset_to_collection(name, asset_path_name) -> bool
Add Asset to Collection

Args:
    name (Name): 
    asset_path_name (Name): 

Returns:
    bool:

<a id="unreal.AssetTagsSubsystem.add_assets_to_collection"></a>

#### add_assets_to_collection

```python
def add_assets_to_collection(name: Name,
                             asset_path_names: Array[Name]) -> bool
```

x.add_assets_to_collection(name, asset_path_names) -> bool
Add Assets to Collection

Args:
    name (Name): 
    asset_path_names (Array[Name]): 

Returns:
    bool:

<a id="unreal.AssetTagsSubsystem.add_asset_ptr_to_collection"></a>

#### add_asset_ptr_to_collection

```python
def add_asset_ptr_to_collection(name: Name, asset_ptr: Object) -> bool
```

x.add_asset_ptr_to_collection(name, asset_ptr) -> bool
Add the given asset to the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_ptr (Object): Asset to add.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.add_asset_ptrs_to_collection"></a>

#### add_asset_ptrs_to_collection

```python
def add_asset_ptrs_to_collection(name: Name,
                                 asset_ptrs: Array[Object]) -> bool
```

x.add_asset_ptrs_to_collection(name, asset_ptrs) -> bool
Add the given assets to the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_ptrs (Array[Object]): Assets to add.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.add_asset_data_to_collection"></a>

#### add_asset_data_to_collection

```python
def add_asset_data_to_collection(name: Name, asset_data: AssetData) -> bool
```

x.add_asset_data_to_collection(name, asset_data) -> bool
Add the given asset to the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_data (AssetData): Asset to add.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AssetTagsSubsystem.add_asset_datas_to_collection"></a>

#### add_asset_datas_to_collection

```python
def add_asset_datas_to_collection(name: Name,
                                  asset_datas: Array[AssetData]) -> bool
```

x.add_asset_datas_to_collection(name, asset_datas) -> bool
Add the given assets to the given collection.

Args:
    name (Name): Name of the collection to modify.
    asset_datas (Array[AssetData]): Assets to add.

Returns:
    bool: True if the collection was modified, false otherwise (see the output log for details on error).

<a id="unreal.AudioCapture"></a>