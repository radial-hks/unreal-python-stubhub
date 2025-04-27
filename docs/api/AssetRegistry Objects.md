## AssetRegistry Objects

```python
class AssetRegistry(Interface)
```

Asset Registry

**C++ Source:**

- **Module**: AssetRegistry
- **File**: IAssetRegistry.h

<a id="unreal.AssetRegistry.wait_for_package"></a>

#### wait_for_package

```python
def wait_for_package(package_name: str) -> None
```

x.wait_for_package(package_name) -> None
Wait for the scan of a specific package to be complete

Args:
    package_name (str):

<a id="unreal.AssetRegistry.wait_for_completion"></a>

#### wait_for_completion

```python
def wait_for_completion() -> None
```

x.wait_for_completion() -> None
Wait for scan to be complete. If called during editor startup before OnPostEngineInit, and there are any assets that use classes in
not-yet-loaded plugin modules, WaitForCompletion will return silently with those assets still ungathered.

<a id="unreal.AssetRegistry.use_filter_to_exclude_assets"></a>

#### use_filter_to_exclude_assets

```python
def use_filter_to_exclude_assets(asset_data_list: Array[AssetData],
                                 filter: ARFilter) -> Array[AssetData]
```

x.use_filter_to_exclude_assets(asset_data_list, filter) -> Array[AssetData]
Trims items out of the asset data list that pass the supplied filter

Args:
    asset_data_list (Array[AssetData]): 
    filter (ARFilter): 

Returns:
    Array[AssetData]: 

    asset_data_list (Array[AssetData]):

<a id="unreal.AssetRegistry.search_all_assets"></a>

#### search_all_assets

```python
def search_all_assets(synchronous_search: bool) -> None
```

x.search_all_assets(synchronous_search) -> None
Look for all assets on disk (can be async or synchronous)

Args:
    synchronous_search (bool):

<a id="unreal.AssetRegistry.scan_paths_synchronous"></a>

#### scan_paths_synchronous

```python
def scan_paths_synchronous(
        paths: Array[str],
        force_rescan: bool = False,
        ignore_deny_list_scan_filters: bool = False) -> None
```

x.scan_paths_synchronous(paths, force_rescan=False, ignore_deny_list_scan_filters=False) -> None
Scan the supplied paths recursively right now and populate the asset registry. If bForceRescan is true, the paths will be scanned again, even if they were previously scanned

Args:
    paths (Array[str]): 
    force_rescan (bool): 
    ignore_deny_list_scan_filters (bool):

<a id="unreal.AssetRegistry.scan_modified_asset_files"></a>

#### scan_modified_asset_files

```python
def scan_modified_asset_files(file_paths: Array[str]) -> None
```

x.scan_modified_asset_files(file_paths) -> None
Forces a rescan of specific filenames, call this when you need to refresh from disk

Args:
    file_paths (Array[str]):

<a id="unreal.AssetRegistry.scan_files_synchronous"></a>

#### scan_files_synchronous

```python
def scan_files_synchronous(file_paths: Array[str],
                           force_rescan: bool = False) -> None
```

x.scan_files_synchronous(file_paths, force_rescan=False) -> None
Scan the specified individual files right now and populate the asset registry. If bForceRescan is true, the paths will be scanned again, even if they were previously scanned

Args:
    file_paths (Array[str]): 
    force_rescan (bool):

<a id="unreal.AssetRegistry.run_assets_through_filter"></a>

#### run_assets_through_filter

```python
def run_assets_through_filter(asset_data_list: Array[AssetData],
                              filter: ARFilter) -> Array[AssetData]
```

x.run_assets_through_filter(asset_data_list, filter) -> Array[AssetData]
Trims items out of the asset data list that do not pass the supplied filter

Args:
    asset_data_list (Array[AssetData]): 
    filter (ARFilter): 

Returns:
    Array[AssetData]: 

    asset_data_list (Array[AssetData]):

<a id="unreal.AssetRegistry.prioritize_search_path"></a>

#### prioritize_search_path

```python
def prioritize_search_path(path_to_prioritize: str) -> None
```

x.prioritize_search_path(path_to_prioritize) -> None
If assets are currently being asynchronously scanned in the specified path, this will cause them to be scanned before other assets.

Args:
    path_to_prioritize (str):

<a id="unreal.AssetRegistry.get_referencers"></a>

#### get_referencers

```python
def get_referencers(
    package_name: Name, reference_options: AssetRegistryDependencyOptions
) -> Optional[Array[Name]]
```

x.get_referencers(package_name, reference_options) -> Array[Name] or None
Gets a list of packages that reference the supplied package. (On disk references ONLY)

Args:
    package_name (Name): the name of the package for which to gather dependencies (eg, /Game/MyFolder/MyAsset)
    reference_options (AssetRegistryDependencyOptions): which kinds of references to include in the output list

Returns:
    Array[Name] or None: 

    out_referencers (Array[Name]): a list of packages that reference the package whose path is PackageName

<a id="unreal.AssetRegistry.get_dependencies"></a>

#### get_dependencies

```python
def get_dependencies(
    package_name: Name, dependency_options: AssetRegistryDependencyOptions
) -> Optional[Array[Name]]
```

x.get_dependencies(package_name, dependency_options) -> Array[Name] or None
Gets a list of paths to objects that are referenced by the supplied package. (On disk references ONLY)

Args:
    package_name (Name): the name of the package for which to gather dependencies (eg, /Game/MyFolder/MyAsset)
    dependency_options (AssetRegistryDependencyOptions): which kinds of dependencies to include in the output list

Returns:
    Array[Name] or None: 

    out_dependencies (Array[Name]): a list of packages that are referenced by the package whose path is PackageName

<a id="unreal.AssetRegistry.k2_get_asset_by_object_path"></a>

#### k2_get_asset_by_object_path

```python
def k2_get_asset_by_object_path(
        object_path: SoftObjectPath,
        include_only_on_disk_assets: bool = False,
        skip_ar_filtered_assets: bool = True) -> AssetData
```

x.k2_get_asset_by_object_path(object_path, include_only_on_disk_assets=False, skip_ar_filtered_assets=True) -> AssetData
Gets the asset data for the specified object path
see: IAssetRegistry class header for bIncludeOnlyOnDiskAssets.

Args:
    object_path (SoftObjectPath): the path of the object to be looked up
    include_only_on_disk_assets (bool): If true, use only DiskGatheredData, do not calculate from UObjects.
    skip_ar_filtered_assets (bool): If true, skips Objects that return true for IsAsset but are not assets in the current platform.

Returns:
    AssetData: the assets data;Will be invalid if object could not be found

<a id="unreal.AssetRegistry.is_search_async"></a>

#### is_search_async

```python
def is_search_async() -> bool
```

x.is_search_async() -> bool
Whether searching is done async (and was started at startup), or synchronously and on-demand, requiring ScanPathsSynchronous or SearchAllAssets.

Returns:
    bool:

<a id="unreal.AssetRegistry.is_search_all_assets"></a>

#### is_search_all_assets

```python
def is_search_all_assets() -> bool
```

x.is_search_all_assets() -> bool
Whether SearchAllAssets has been called, or was auto-called at startup. When async (editor or cooking), if SearchAllAssets has ever been called,
any newly-mounted directory will be automatically searched.

Returns:
    bool:

<a id="unreal.AssetRegistry.is_loading_assets"></a>

#### is_loading_assets

```python
def is_loading_assets() -> bool
```

x.is_loading_assets() -> bool
Returns true if the asset registry is currently loading files and does not yet know about all assets

Returns:
    bool:

<a id="unreal.AssetRegistry.has_assets"></a>

#### has_assets

```python
def has_assets(package_path: Name, recursive: bool = False) -> bool
```

x.has_assets(package_path, recursive=False) -> bool
Does the given path contain assets, optionally also testing sub-paths?

Args:
    package_path (Name): the path to query asset data in (eg, /Game/MyFolder)
    recursive (bool): if true, the supplied path will be tested recursively

Returns:
    bool:

<a id="unreal.AssetRegistry.get_sub_paths"></a>

#### get_sub_paths

```python
def get_sub_paths(base_path: str, recurse: bool) -> Array[str]
```

x.get_sub_paths(base_path, recurse) -> Array[str]
Gets a list of all paths that are currently cached below the passed-in base path

Args:
    base_path (str): 
    recurse (bool): 

Returns:
    Array[str]: 

    out_path_list (Array[str]):

<a id="unreal.AssetRegistry.get_in_memory_assets"></a>

#### get_in_memory_assets

```python
def get_in_memory_assets(
        filter: ARFilter,
        skip_ar_filtered_assets: bool = True) -> Optional[Array[AssetData]]
```

x.get_in_memory_assets(filter, skip_ar_filtered_assets=True) -> Array[AssetData] or None
Gets asset data for in-memory assets only, that match the filter.
Returns assets that would be excluded by calling GetAssets with bIncludeOnlyOnDiskAssets set to true.
note: This method IGNORES the value of bIncludeOnlyOnDiskAssets on the provided filter. Assets returned must satisfy every filter component if there is at least one element in the component's array. Assets will satisfy a component if they match any of the elements in it.

Args:
    filter (ARFilter): filter to apply to the assets in the AssetRegistry
    skip_ar_filtered_assets (bool): If true, skips Objects that return true for IsAsset but are not assets in the current platform.

Returns:
    Array[AssetData] or None: 

    out_asset_data (Array[AssetData]): the list of assets in this path

<a id="unreal.AssetRegistry.get_derived_class_names"></a>

#### get_derived_class_names

```python
def get_derived_class_names(
        class_names: Array[TopLevelAssetPath],
        excluded_class_names: Set[TopLevelAssetPath]
) -> Set[TopLevelAssetPath]
```

x.get_derived_class_names(class_names, excluded_class_names) -> Set[TopLevelAssetPath]
Returns the names of all classes derived by the supplied class names, excluding any classes matching the excluded class names. This can be slow if temporary caching mode is not on

Args:
    class_names (Array[TopLevelAssetPath]): 
    excluded_class_names (Set[TopLevelAssetPath]): 

Returns:
    Set[TopLevelAssetPath]: 

    out_derived_class_names (Set[TopLevelAssetPath]):

<a id="unreal.AssetRegistry.get_assets_by_paths"></a>

#### get_assets_by_paths

```python
def get_assets_by_paths(
        package_paths: Array[Name],
        recursive: bool = False,
        include_only_on_disk_assets: bool = False
) -> Optional[Array[AssetData]]
```

x.get_assets_by_paths(package_paths, recursive=False, include_only_on_disk_assets=False) -> Array[AssetData] or None
Gets asset data for all assets in any of the supplied folder paths
see: IAssetRegistry class header for bIncludeOnlyOnDiskAssets.

Args:
    package_paths (Array[Name]): the paths to query asset data in (eg, /Game/MyFolder)
    recursive (bool): if true, all supplied paths will be searched recursively
    include_only_on_disk_assets (bool): If true, use only DiskGatheredData, do not calculate from UObjects.

Returns:
    Array[AssetData] or None: 

    out_asset_data (Array[AssetData]): the list of assets in this path

<a id="unreal.AssetRegistry.get_assets_by_path"></a>

#### get_assets_by_path

```python
def get_assets_by_path(
        package_path: Name,
        recursive: bool = False,
        include_only_on_disk_assets: bool = False
) -> Optional[Array[AssetData]]
```

x.get_assets_by_path(package_path, recursive=False, include_only_on_disk_assets=False) -> Array[AssetData] or None
Gets asset data for all assets in the supplied folder path
see: IAssetRegistry class header for bIncludeOnlyOnDiskAssets.

Args:
    package_path (Name): the path to query asset data in (eg, /Game/MyFolder)
    recursive (bool): if true, all supplied paths will be searched recursively
    include_only_on_disk_assets (bool): If true, use only DiskGatheredData, do not calculate from UObjects.

Returns:
    Array[AssetData] or None: 

    out_asset_data (Array[AssetData]): the list of assets in this path

<a id="unreal.AssetRegistry.get_assets_by_package_name"></a>

#### get_assets_by_package_name

```python
def get_assets_by_package_name(
        package_name: Name,
        include_only_on_disk_assets: bool = False,
        skip_ar_filtered_assets: bool = True) -> Optional[Array[AssetData]]
```

x.get_assets_by_package_name(package_name, include_only_on_disk_assets=False, skip_ar_filtered_assets=True) -> Array[AssetData] or None
Gets asset data for the assets in the package with the specified package name
see: IAssetRegistry class header for bIncludeOnlyOnDiskAssets.

Args:
    package_name (Name): the package name for the requested assets (eg, /Game/MyFolder/MyAsset)
    include_only_on_disk_assets (bool): If true, use only DiskGatheredData, do not calculate from UObjects.
    skip_ar_filtered_assets (bool): If true, skips Objects that return true for IsAsset but are not assets in the current platform.

Returns:
    Array[AssetData] or None: 

    out_asset_data (Array[AssetData]): the list of assets in this path

<a id="unreal.AssetRegistry.get_assets_by_class"></a>

#### get_assets_by_class

```python
def get_assets_by_class(
        class_path_name: TopLevelAssetPath,
        search_sub_classes: bool = False) -> Optional[Array[AssetData]]
```

x.get_assets_by_class(class_path_name, search_sub_classes=False) -> Array[AssetData] or None
Gets asset data for all assets with the supplied class

Args:
    class_path_name (TopLevelAssetPath): the full path of the class name of the assets requested, in a TopLevelAssetPath structure.
    search_sub_classes (bool): if true, all subclasses of the passed in class will be searched as well

Returns:
    Array[AssetData] or None: 

    out_asset_data (Array[AssetData]): the list of assets in this path

<a id="unreal.AssetRegistry.get_assets"></a>

#### get_assets

```python
def get_assets(
        filter: ARFilter,
        skip_ar_filtered_assets: bool = True) -> Optional[Array[AssetData]]
```

x.get_assets(filter, skip_ar_filtered_assets=True) -> Array[AssetData] or None
Gets asset data for all assets that match the filter.
Assets returned must satisfy every filter component if there is at least one element in the component's array.
Assets will satisfy a component if they match any of the elements in it.

Args:
    filter (ARFilter): filter to apply to the assets in the AssetRegistry
    skip_ar_filtered_assets (bool): If true, skips Objects that return true for IsAsset but are not assets in the current platform.

Returns:
    Array[AssetData] or None: 

    out_asset_data (Array[AssetData]): the list of assets in this path

<a id="unreal.AssetRegistry.get_asset_by_object_path"></a>

#### get_asset_by_object_path

```python
def get_asset_by_object_path(
        object_path: Name,
        include_only_on_disk_assets: bool = False) -> AssetData
```

x.get_asset_by_object_path(object_path, include_only_on_disk_assets=False) -> AssetData
Get Asset by Object Path

Args:
    object_path (Name): 
    include_only_on_disk_assets (bool): 

Returns:
    AssetData:

<a id="unreal.AssetRegistry.get_ancestor_class_names"></a>

#### get_ancestor_class_names

```python
def get_ancestor_class_names(
        class_path_name: TopLevelAssetPath
) -> Optional[Array[TopLevelAssetPath]]
```

x.get_ancestor_class_names(class_path_name) -> Array[TopLevelAssetPath] or None
Returns true if the specified ClassName's ancestors could be found. If so, OutAncestorClassNames is a list of all its ancestors. This can be slow if temporary caching mode is not on

Args:
    class_path_name (TopLevelAssetPath): 

Returns:
    Array[TopLevelAssetPath] or None: 

    out_ancestor_class_names (Array[TopLevelAssetPath]):

<a id="unreal.AssetRegistry.get_all_cached_paths"></a>

#### get_all_cached_paths

```python
def get_all_cached_paths() -> Array[str]
```

x.get_all_cached_paths() -> Array[str]
Gets a list of all paths that are currently cached

Returns:
    Array[str]: 

    out_path_list (Array[str]):

<a id="unreal.AssetRegistry.get_all_assets"></a>

#### get_all_assets

```python
def get_all_assets(
        include_only_on_disk_assets: bool = False
) -> Optional[Array[AssetData]]
```

x.get_all_assets(include_only_on_disk_assets=False) -> Array[AssetData] or None
Gets asset data for all assets in the registry.
This method may be slow, use a filter if possible to avoid iterating over the entire registry.

Args:
    include_only_on_disk_assets (bool): 

Returns:
    Array[AssetData] or None: 

    out_asset_data (Array[AssetData]): the list of assets in this path

<a id="unreal.GameMapsSettings"></a>