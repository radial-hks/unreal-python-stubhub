## UsdAssetCache Objects

```python
class UsdAssetCache(Object)
```

This class is an asset that can be created via the Content Browser and assigned to AUsdStageActors.

Its main purpose is to track generated assets based on the hash of the source prim data: Whenever the AUsdStageActor needs
to generate e.g. a MaterialInstance, it will first hash the Material prim, and check whether its UUsdAssetCache3 already
has an asset of that class for the resulting hash.

The cache can then be shared by multiple AUsdStageActors to prevent recreating UObjects from identical, already translated prim data.

A "Default Asset Cache" can be set on the project settings, and will be automatically used for any AUsdStageActor that hasn't
had an asset cache manually set beforehand.

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetCache3.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_directory`` (DirectoryPath):  [Read-Write] Content directory where the asset cache will place newly created assets.

  Changing this directory to a new location will automatically try to cache any existing assets on that location, if they
  were generated from USD.
- ``clean_up_unreferenced_assets`` (bool):  [Read-Write] If this is true, every time a UsdStageActor using this asset cache closes a stage or swaps asset caches it will attempt to call
  DeleteUnreferencedAssets, potentially dropping *any* unreferenced asset, due to this operation or previous ones.

  Enable this if you want your AssetDirectory folder to be automatically cleaned up as stages close, and don't plan on keeping
  other external references to those assets.

  Note: Some asset types may have complicated setups, and may end up with references from other properties, actors and components for
  some time (e.g. due to a component in a transient package or undo/redo buffer). This means any automatically cleanup may not
  manage to clean up *all* untracked assets. Subsequent cleanups should eventually collect all assets, however.

  WARNING: This will clear the undo buffer (i.e. transaction history) and run garbage collection after any cleanup operation!
- ``hash_to_asset_paths`` (Map[str, SoftObjectPath]):  [Read-Write] This is the main internal property that maps hashes to asset paths.

  Add entries to this property (or modify existing entries) and they will be returned by the asset cache whenever that hash is queried.

  WARNING: Asset modifications are not currently tracked! Change a static mesh's vertex color from red to green, and it will show the
  green cube when opening a stage with this asset cache, even if you open stages where the prim contains red as its vertex color.
- ``only_handle_assets_within_asset_directory`` (bool):  [Read-Write] When true, it means the asset cache will only ever return assets that are currently inside of the AssetDirectory folder.
  Move the assets out of the folder or change the folder and the asset cache will act as if these assets don't exist, potentially even losing
  track of them.

  When false, it means the asset cache will fully track and use its provided assets wherever they are in the content browser.

<a id="unreal.UsdAssetCache.asset_directory"></a>

#### asset_directory

```python
@property
def asset_directory() -> DirectoryPath
```

(DirectoryPath):  [Read-Write] Content directory where the asset cache will place newly created assets.

Changing this directory to a new location will automatically try to cache any existing assets on that location, if they
were generated from USD.

<a id="unreal.UsdAssetCache.asset_directory"></a>

#### asset_directory

```python
@asset_directory.setter
def asset_directory(value: DirectoryPath) -> None
```

<a id="unreal.UsdAssetCache.only_handle_assets_within_asset_directory"></a>

#### only_handle_assets_within_asset_directory

```python
@property
def only_handle_assets_within_asset_directory() -> bool
```

(bool):  [Read-Write] When true, it means the asset cache will only ever return assets that are currently inside of the AssetDirectory folder.
Move the assets out of the folder or change the folder and the asset cache will act as if these assets don't exist, potentially even losing
track of them.

When false, it means the asset cache will fully track and use its provided assets wherever they are in the content browser.

<a id="unreal.UsdAssetCache.only_handle_assets_within_asset_directory"></a>

#### only_handle_assets_within_asset_directory

```python
@only_handle_assets_within_asset_directory.setter
def only_handle_assets_within_asset_directory(value: bool) -> None
```

<a id="unreal.UsdAssetCache.hash_to_asset_paths"></a>

#### hash_to_asset_paths

```python
@property
def hash_to_asset_paths() -> Map[str, SoftObjectPath]
```

(Map[str, SoftObjectPath]):  [Read-Write] This is the main internal property that maps hashes to asset paths.

Add entries to this property (or modify existing entries) and they will be returned by the asset cache whenever that hash is queried.

WARNING: Asset modifications are not currently tracked! Change a static mesh's vertex color from red to green, and it will show the
green cube when opening a stage with this asset cache, even if you open stages where the prim contains red as its vertex color.

<a id="unreal.UsdAssetCache.hash_to_asset_paths"></a>

#### hash_to_asset_paths

```python
@hash_to_asset_paths.setter
def hash_to_asset_paths(value: Map[str, SoftObjectPath]) -> None
```

<a id="unreal.UsdAssetCache.clean_up_unreferenced_assets"></a>

#### clean_up_unreferenced_assets

```python
@property
def clean_up_unreferenced_assets() -> bool
```

(bool):  [Read-Write] If this is true, every time a UsdStageActor using this asset cache closes a stage or swaps asset caches it will attempt to call
DeleteUnreferencedAssets, potentially dropping *any* unreferenced asset, due to this operation or previous ones.

Enable this if you want your AssetDirectory folder to be automatically cleaned up as stages close, and don't plan on keeping
other external references to those assets.

Note: Some asset types may have complicated setups, and may end up with references from other properties, actors and components for
some time (e.g. due to a component in a transient package or undo/redo buffer). This means any automatically cleanup may not
manage to clean up *all* untracked assets. Subsequent cleanups should eventually collect all assets, however.

WARNING: This will clear the undo buffer (i.e. transaction history) and run garbage collection after any cleanup operation!

<a id="unreal.UsdAssetCache.clean_up_unreferenced_assets"></a>

#### clean_up_unreferenced_assets

```python
@clean_up_unreferenced_assets.setter
def clean_up_unreferenced_assets(value: bool) -> None
```

<a id="unreal.UsdAssetCache.stop_tracking_asset"></a>

#### stop_tracking_asset

```python
def stop_tracking_asset(hash: str) -> SoftObjectPath
```

x.stop_tracking_asset(hash) -> SoftObjectPath
Removes all info about the asset associated with Hash from this cache, if there is any.
Note: This will not delete the asset however: Only tracked, *unreferenced* assets can be deleted by the asset cache,
and only when manually created by it or if flagged with SetAssetDeletable

Args:
    hash (str): 

Returns:
    SoftObjectPath:

<a id="unreal.UsdAssetCache.set_asset_deletable"></a>

#### set_asset_deletable

```python
def set_asset_deletable(asset: Object, is_deletable: bool) -> None
```

x.set_asset_deletable(asset, is_deletable) -> None
Sets a particular asset as deletable or not.
Assets not flagged as deletable will never be deleted by the asset cache when DeleteUnreferencedAssets is called.
Assets the cache creates itself via GetOrCreateCachedAsset or GetOrCreateCustomCachedAsset are automatically
set as deletable.

Args:
    asset (Object): 
    is_deletable (bool):

<a id="unreal.UsdAssetCache.rescan_asset_directory"></a>

#### rescan_asset_directory

```python
def rescan_asset_directory() -> None
```

x.rescan_asset_directory() -> None
Checks the current AssetDirectory for any new assets that were generated from USD, and automatically caches
them if possible.

Note: This will never overwrite any existing information on the asset cache (i.e. if the newly found asset
is associated with a hash that is already in use, it will be ignored)

<a id="unreal.UsdAssetCache.remove_asset_referencer"></a>

#### remove_asset_referencer

```python
def remove_asset_referencer(asset: Object, referencer: Object) -> bool
```

x.remove_asset_referencer(asset, referencer) -> bool
Removes an UObject referencer from a particular asset, returning true if anything was removed.
Will do nothing in case Asset or Referencer are invalid.

Args:
    asset (Object): 
    referencer (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetCache.remove_all_referencers_for_asset"></a>

#### remove_all_referencers_for_asset

```python
def remove_all_referencers_for_asset(asset: Object) -> bool
```

x.remove_all_referencers_for_asset(asset) -> bool
Removes all UObject referencers from a particular asset, returning true if anything was removed.
Will do nothing in case Asset is invalid.

Args:
    asset (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetCache.remove_all_referencer_assets"></a>

#### remove_all_referencer_assets

```python
def remove_all_referencer_assets(referencer: Object) -> bool
```

x.remove_all_referencer_assets(referencer) -> bool
Removes a particular UObject referencer from all tracked assets, returning true if anything was removed.
Will do nothing in case Referencer is invalid.

Args:
    referencer (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetCache.remove_all_asset_referencers"></a>

#### remove_all_asset_referencers

```python
def remove_all_asset_referencers() -> bool
```

x.remove_all_asset_referencers() -> bool
Removes all UObject referencer from all tracked assets, returning true if anything was removed.

Returns:
    bool:

<a id="unreal.UsdAssetCache.load_and_get_all_tracked_assets"></a>

#### load_and_get_all_tracked_assets

```python
def load_and_get_all_tracked_assets() -> Map[str, Object]
```

x.load_and_get_all_tracked_assets() -> Map[str, Object]
The same as GetAllTrackedAssets, except that it will automatically try loading all the asset paths before
returning, which should be convenient for Python or Blueprint callers.

WARNING: As this may try loading a package from disk, this can only be called from the game thread!

Returns:
    Map[str, Object]:

<a id="unreal.UsdAssetCache.is_asset_tracked_by_cache"></a>

#### is_asset_tracked_by_cache

```python
def is_asset_tracked_by_cache(asset_path: SoftObjectPath) -> bool
```

x.is_asset_tracked_by_cache(asset_path) -> bool
Returns true if this asset is currently tracked by the asset cache's main hash to asset maps

Args:
    asset_path (SoftObjectPath): 

Returns:
    bool:

<a id="unreal.UsdAssetCache.is_asset_deletable"></a>

#### is_asset_deletable

```python
def is_asset_deletable(asset: Object) -> bool
```

x.is_asset_deletable(asset) -> bool
Returns whether a particular asset is currently marked as deletable or not

Args:
    asset (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetCache.get_or_create_cached_asset"></a>

#### get_or_create_cached_asset

```python
def get_or_create_cached_asset(
        hash: str,
        class_: Class,
        desired_name: str,
        desired_flags: int,
        referencer: Object = None) -> Tuple[Object, bool]
```

x.get_or_create_cached_asset(hash, class_, desired_name, desired_flags, referencer=None) -> (Object, out_created_asset=bool)
Returns the cached UObject of the provided Class for the provided Hash if one exists.
Otherwise, finds a new package for it on the cache's AssetDirectory and creates the asset
via a NewObject<Class> call, using with a sanitized version of the desired name and flags.

WARNING: As this may try loading a package from disk or call NewObject, this can only be called from the game thread!

Args:
    hash (str): The string key to check with
    class_ (type(Class)): The class of the object that we want to retrieve or create from the asset cache
    desired_name (str): The name we want the created object to have (the actual name may have additional suffixes)
    desired_flags (int32): The flags we want the created object to have (the actual applied flags may differ depending on context)
    referencer (Object): The asset will not be deleted or untracked until this referencer is removed (via any of the RemoveAssetReferencer member functions)

Returns:
    bool: The asset that was returned or created

    out_created_asset (bool): Set to true if we created the asset that was return, but false if we returned an existing asset

<a id="unreal.UsdAssetCache.get_num_assets"></a>

#### get_num_assets

```python
def get_num_assets() -> int
```

x.get_num_assets() -> int32
Returns the total number of cached asset paths, whether these resolve to assets or not

Returns:
    int32:

<a id="unreal.UsdAssetCache.get_hash_for_asset"></a>

#### get_hash_for_asset

```python
def get_hash_for_asset(asset_path: SoftObjectPath) -> str
```

x.get_hash_for_asset(asset_path) -> str
Returns the hash associated with a particular asset, or the empty string if there isn't any.
Note: The asset cache keeps internal reverse maps, so this should be O(1)

Args:
    asset_path (SoftObjectPath): 

Returns:
    str:

<a id="unreal.UsdAssetCache.get_cached_asset_path"></a>

#### get_cached_asset_path

```python
def get_cached_asset_path(hash: str) -> SoftObjectPath
```

x.get_cached_asset_path(hash) -> SoftObjectPath
Returns the internal FSoftObjectPath associated with Hash, without trying to load the asset.
If there is no asset associated with Hash, will return an invalid (empty) FSoftObjectPath.

Args:
    hash (str): 

Returns:
    SoftObjectPath:

<a id="unreal.UsdAssetCache.get_cached_asset"></a>

#### get_cached_asset

```python
def get_cached_asset(hash: str) -> Object
```

x.get_cached_asset(hash) -> Object
Returns the asset associated with a particular Hash, if any. Returns nullptr if there isn't any
associated path to this Hash, or if the associated path doesn't resolve to an asset.

WARNING: As this may try loading a package from disk, this can only be called from the game thread!

Args:
    hash (str): 

Returns:
    Object:

<a id="unreal.UsdAssetCache.get_all_tracked_assets"></a>

#### get_all_tracked_assets

```python
def get_all_tracked_assets() -> Map[str, SoftObjectPath]
```

x.get_all_tracked_assets() -> Map[str, SoftObjectPath]
Returns a copy of the internal mapping between hashes and asset paths

Returns:
    Map[str, SoftObjectPath]:

<a id="unreal.UsdAssetCache.delete_unreferenced_assets_with_confirmation"></a>

#### delete_unreferenced_assets_with_confirmation

```python
def delete_unreferenced_assets_with_confirmation() -> None
```

x.delete_unreferenced_assets_with_confirmation() -> None
This is the same as calling DeleteUnreferencedAssets and providing true for bShowConfirmation.
It is just exposed in this manner so we automatically get a button for calling this function on details panels of the
asset cache.

WARNING: This will clear the undo buffer (i.e. transaction history) and run garbage collection after deleting.

<a id="unreal.UsdAssetCache.delete_unreferenced_assets"></a>

#### delete_unreferenced_assets

```python
def delete_unreferenced_assets(show_confirmation: bool = False) -> None
```

x.delete_unreferenced_assets(show_confirmation=False) -> None
Deletes all assets that:
  - Are currently tracked by the asset cache;
  - Are set as deletable;
  - Are not used by other UObjects (by external assets, components, undo buffer, Python scripting variables, etc.).
  - Have no referencers;
  - Have not been saved to disk;

If bShowConfirmation is true, this will fallback to using engine code for deleting the assets, showing a
confirmation dialog listing the assets that will be deleted. If false, it will silently try deleting the assets it can.

WARNING: This will clear the undo buffer (i.e. transaction history) and run garbage collection after deleting.

Args:
    show_confirmation (bool):

<a id="unreal.UsdAssetCache.cache_asset"></a>

#### cache_asset

```python
def cache_asset(hash: str,
                asset_path: SoftObjectPath,
                referencer: Object = None) -> None
```

x.cache_asset(hash, asset_path, referencer=None) -> None
Adds an existing asset to the cache attached to a particular hash, and optionally registering a referencer

Args:
    hash (str): 
    asset_path (SoftObjectPath): 
    referencer (Object):

<a id="unreal.UsdAssetCache.add_asset_referencer"></a>

#### add_asset_referencer

```python
def add_asset_referencer(asset: Object, referencer: Object) -> bool
```

x.add_asset_referencer(asset, referencer) -> bool
Adds a new UObject referencer to a particular asset, returning true if the operation succeeded.
Assets will not be deleted or untracked by the asset cache while the referencer is registered.

Args:
    asset (Object): 
    referencer (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetImportData"></a>