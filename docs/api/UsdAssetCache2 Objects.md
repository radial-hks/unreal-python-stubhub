## UsdAssetCache2 Objects

```python
class UsdAssetCache2(Object)
```

Owns the assets generated and reused by USD Stages, allowing thread-safe retrieval/storage.

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetCache2.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_storage`` (Map[str, Object]):  [Read-Only] Main hash to asset storage for all assets that we're currently using and shouldn't be GC'd
- ``persistent_asset_storage_size_mb`` (double):  [Read-Write] This limit specifies how much size is allocated to storing all persistent assets (i.e. assets that will be
  saved to disk, even if unused by any stage).
  Set this to 0 to disable persistent asset storage.
  This has no effect on temporary asset caches (e.g. the ones automatically generated when opening a stage
  without an asset cache asset assigned)
- ``unreferenced_asset_storage_size_mb`` (double):  [Read-Write] The asset cache will always retain all currently used assets.
  In addition to that, this limit specifies how much size is allocated to storing assets that remain only for the
  current session and that aren't being used by any stage.
  Set this to 0 to disable storing unreferenced assets.

<a id="unreal.UsdAssetCache2.unreferenced_asset_storage_size_mb"></a>

#### unreferenced_asset_storage_size_mb

```python
@property
def unreferenced_asset_storage_size_mb() -> float
```

(double):  [Read-Write] The asset cache will always retain all currently used assets.
In addition to that, this limit specifies how much size is allocated to storing assets that remain only for the
current session and that aren't being used by any stage.
Set this to 0 to disable storing unreferenced assets.

<a id="unreal.UsdAssetCache2.unreferenced_asset_storage_size_mb"></a>

#### unreferenced_asset_storage_size_mb

```python
@unreferenced_asset_storage_size_mb.setter
def unreferenced_asset_storage_size_mb(value: float) -> None
```

<a id="unreal.UsdAssetCache2.persistent_asset_storage_size_mb"></a>

#### persistent_asset_storage_size_mb

```python
@property
def persistent_asset_storage_size_mb() -> float
```

(double):  [Read-Write] This limit specifies how much size is allocated to storing all persistent assets (i.e. assets that will be
saved to disk, even if unused by any stage).
Set this to 0 to disable persistent asset storage.
This has no effect on temporary asset caches (e.g. the ones automatically generated when opening a stage
without an asset cache asset assigned)

<a id="unreal.UsdAssetCache2.persistent_asset_storage_size_mb"></a>

#### persistent_asset_storage_size_mb

```python
@persistent_asset_storage_size_mb.setter
def persistent_asset_storage_size_mb(value: float) -> None
```

<a id="unreal.UsdAssetCache2.touch_asset"></a>

#### touch_asset

```python
def touch_asset(asset: Object, referencer: Object = None) -> bool
```

x.touch_asset(asset, referencer=None) -> bool
Marks the provided asset as being used at this point, optionally adding a specific referencer.
This is useful because the asset cache will always prioritize retaining the most recently used assets

Args:
    asset (Object): 
    referencer (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetCache2.reset"></a>

#### reset

```python
def reset() -> None
```

x.reset() -> None
Discards all tracked assets across all storage types

<a id="unreal.UsdAssetCache2.remove_asset_reference"></a>

#### remove_asset_reference

```python
def remove_asset_reference(asset: Object, referencer: Object = None) -> bool
```

x.remove_asset_reference(asset, referencer=None) -> bool
Removes an UObject referencer from a particular asset, returning true if the operation succeeded.
If no specific Referencer is provided, all referencers to Asset will be removed.

Args:
    asset (Object): 
    referencer (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetCache2.remove_asset"></a>

#### remove_asset

```python
def remove_asset(hash: str) -> Object
```

x.remove_asset(hash) -> Object
If an asset is associated with `Hash`, it will be returned and the asset cache will stop tracking this asset
entirely. Returns nullptr otherwise. See CanRemoveAsset.

WARNING: The asset will still be outer'd to the asset cache, however. The caller is in charge of properly
placing the asset at a new Outer object.

Args:
    hash (str): 

Returns:
    Object:

<a id="unreal.UsdAssetCache2.remove_all_asset_references"></a>

#### remove_all_asset_references

```python
def remove_all_asset_references(referencer: Object) -> bool
```

x.remove_all_asset_references(referencer) -> bool
Removes the particular referencer to all assets tracked by the cache, if it was a referencer to any of them.
Returns true if at least one asset referencer count was altered by this.

Args:
    referencer (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetCache2.refresh_storage"></a>

#### refresh_storage

```python
def refresh_storage() -> None
```

x.refresh_storage() -> None
Updates which assets belong to each storage type. You must call this in case you perform direct operations on
the asset cache, after those operations are fully complete.

<a id="unreal.UsdAssetCache2.is_asset_owned_by_cache"></a>

#### is_asset_owned_by_cache

```python
def is_asset_owned_by_cache(asset_path: str) -> bool
```

x.is_asset_owned_by_cache(asset_path) -> bool
Returns true in case the asset at `AssetPath` is tracked by the cache in any way (persistent asset,
unreferenced or referenced). An example AssetPath would be "/Game/MyTextures/RedBrick.RedBrick".

Args:
    asset_path (str): 

Returns:
    bool:

<a id="unreal.UsdAssetCache2.get_num_assets"></a>

#### get_num_assets

```python
def get_num_assets() -> int
```

x.get_num_assets() -> int32
Returns how many assets are tracked by the asset cache in total (summing up persistent, referenced and
unreferenced storage)

Returns:
    int32:

<a id="unreal.UsdAssetCache2.get_hash_for_asset"></a>

#### get_hash_for_asset

```python
def get_hash_for_asset(asset: Object) -> str
```

x.get_hash_for_asset(asset) -> str
Returns the hash associated with an asset, in case we own it. Returns the empty string otherwise.
Note: This has O(1) time complexity.

Args:
    asset (Object): 

Returns:
    str:

<a id="unreal.UsdAssetCache2.get_cached_asset"></a>

#### get_cached_asset

```python
def get_cached_asset(hash: str) -> Object
```

x.get_cached_asset(hash) -> Object
Returns an asset associated with a particular `Hash`.
If the asset is persistent, unloaded and the "USD.OnDemandCachedAssetLoading" cvar is true, this may cause the
asset to be read from the asset cache's file on disk.

Args:
    hash (str): 

Returns:
    Object:

<a id="unreal.UsdAssetCache2.get_all_loaded_assets"></a>

#### get_all_loaded_assets

```python
def get_all_loaded_assets() -> Array[Object]
```

x.get_all_loaded_assets() -> Array[Object]
Returns all assets that are currently loaded in the asset cache.
This will not include persistent assets that haven't been loaded yet.

Returns:
    Array[Object]:

<a id="unreal.UsdAssetCache2.get_all_cached_asset_paths"></a>

#### get_all_cached_asset_paths

```python
def get_all_cached_asset_paths() -> Array[str]
```

x.get_all_cached_asset_paths() -> Array[str]
Returns all asset paths tracked by the asset cache, for all storage types. (e.g.
"/Game/MyTextures/RedBrick.RedBrick"). This includes unloaded persistent assets

Returns:
    Array[str]:

<a id="unreal.UsdAssetCache2.get_all_asset_hashes"></a>

#### get_all_asset_hashes

```python
def get_all_asset_hashes() -> Array[str]
```

x.get_all_asset_hashes() -> Array[str]
Returns all asset hashes tracked by the asset cache, for all storage types. This includes unloaded
persistent assets

Returns:
    Array[str]:

<a id="unreal.UsdAssetCache2.can_remove_asset"></a>

#### can_remove_asset

```python
def can_remove_asset(hash: str) -> bool
```

x.can_remove_asset(hash) -> bool
Returns true if the asset with the given hash can be removed from the cache. It will return false in case the
asset is still being used, either by another consumer asset or directly by some referencer.

Args:
    hash (str): 

Returns:
    bool:

<a id="unreal.UsdAssetCache2.cache_asset"></a>

#### cache_asset

```python
def cache_asset(hash: str, asset: Object, referencer: Object = None) -> None
```

x.cache_asset(hash, asset, referencer=None) -> None
Adds an asset to the cache attached to a particular hash, and optionally registering a referencer

Args:
    hash (str): 
    asset (Object): 
    referencer (Object):

<a id="unreal.UsdAssetCache2.add_asset_reference"></a>

#### add_asset_reference

```python
def add_asset_reference(asset: Object, referencer: Object) -> bool
```

x.add_asset_reference(asset, referencer) -> bool
Adds a new UObject referencer to a particular asset, returning true if the operation succeeded.

Assets will not be evicted or removed from the cache while the referencer is registered.
Note that internally the cache keeps FObjectKey structs constructed from the referencers, instead of direct
pointers to them.

Args:
    asset (Object): 
    referencer (Object): 

Returns:
    bool:

<a id="unreal.UsdAssetCache"></a>