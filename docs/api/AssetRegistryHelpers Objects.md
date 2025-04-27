## AssetRegistryHelpers Objects

```python
class AssetRegistryHelpers(Object)
```

Asset Registry Helpers

**C++ Source:**

- **Module**: AssetRegistry
- **File**: AssetRegistryHelpers.h

<a id="unreal.AssetRegistryHelpers.to_soft_object_path"></a>

#### to_soft_object_path

```python
@classmethod
def to_soft_object_path(cls, asset_data: AssetData) -> SoftObjectPath
```

X.to_soft_object_path(asset_data) -> SoftObjectPath
Convert to a SoftObjectPath for loading

Args:
    asset_data (AssetData): 

Returns:
    SoftObjectPath:

<a id="unreal.AssetRegistryHelpers.sort_by_predicate"></a>

#### sort_by_predicate

```python
@classmethod
def sort_by_predicate(cls, assets: Array[AssetData],
                      sorting_predicate: SortingPredicate,
                      sort_order: AssetRegistrySortOrder) -> Array[AssetData]
```

X.sort_by_predicate(assets, sorting_predicate, sort_order) -> Array[AssetData]
Sorts the assets based on a custom Blueprint delegate.

Args:
    assets (Array[AssetData]): The assets to sort
    sorting_predicate (SortingPredicate): Implements a Left <= Right relation
    sort_order (AssetRegistrySortOrder): Whether to sort ascending or descending

Returns:
    Array[AssetData]: 

    assets (Array[AssetData]): The assets to sort

<a id="unreal.AssetRegistryHelpers.sort_by_asset_name"></a>

#### sort_by_asset_name

```python
@classmethod
def sort_by_asset_name(cls, assets: Array[AssetData],
                       sort_order: AssetRegistrySortOrder) -> Array[AssetData]
```

X.sort_by_asset_name(assets, sort_order) -> Array[AssetData]
Sorts the assets by their asset name.

Args:
    assets (Array[AssetData]): The assets to sort
    sort_order (AssetRegistrySortOrder): Whether to sort ascending or descending

Returns:
    Array[AssetData]: 

    assets (Array[AssetData]): The assets to sort

<a id="unreal.AssetRegistryHelpers.set_filter_tags_and_values"></a>

#### set_filter_tags_and_values

```python
@classmethod
def set_filter_tags_and_values(
        cls, filter: ARFilter,
        tags_and_values: Array[TagAndValue]) -> ARFilter
```

X.set_filter_tags_and_values(filter, tags_and_values) -> ARFilter
Populates the FARFilters tags and values map with the passed in tags and values

Args:
    filter (ARFilter): 
    tags_and_values (Array[TagAndValue]): 

Returns:
    ARFilter:

<a id="unreal.AssetRegistryHelpers.is_valid"></a>

#### is_valid

```python
@classmethod
def is_valid(cls, asset_data: AssetData) -> bool
```

X.is_valid(asset_data) -> bool
Checks to see if this AssetData refers to an asset or is NULL

Args:
    asset_data (AssetData): 

Returns:
    bool:

<a id="unreal.AssetRegistryHelpers.is_u_asset"></a>

#### is_u_asset

```python
@classmethod
def is_u_asset(cls, asset_data: AssetData) -> bool
```

X.is_u_asset(asset_data) -> bool
Returns true if this is the primary asset in a package, true for maps and assets but false for secondary objects like class redirectors

Args:
    asset_data (AssetData): 

Returns:
    bool:

<a id="unreal.AssetRegistryHelpers.is_redirector"></a>

#### is_redirector

```python
@classmethod
def is_redirector(cls, asset_data: AssetData) -> bool
```

X.is_redirector(asset_data) -> bool
Returns true if the this asset is a redirector.

Args:
    asset_data (AssetData): 

Returns:
    bool:

<a id="unreal.AssetRegistryHelpers.is_asset_loaded"></a>

#### is_asset_loaded

```python
@classmethod
def is_asset_loaded(cls, asset_data: AssetData) -> bool
```

X.is_asset_loaded(asset_data) -> bool
Returns true if the asset is loaded

Args:
    asset_data (AssetData): 

Returns:
    bool:

<a id="unreal.AssetRegistryHelpers.get_tag_value"></a>

#### get_tag_value

```python
@classmethod
def get_tag_value(cls, asset_data: AssetData, tag_name: Name) -> Optional[str]
```

X.get_tag_value(asset_data, tag_name) -> str or None
Gets the value associated with the given tag as a string

Args:
    asset_data (AssetData): 
    tag_name (Name): 

Returns:
    str or None: 

    out_tag_value (str):

<a id="unreal.AssetRegistryHelpers.get_full_name"></a>

#### get_full_name

```python
@classmethod
def get_full_name(cls, asset_data: AssetData) -> str
```

X.get_full_name(asset_data) -> str
Returns the full name for the asset in the form: Class ObjectPath

Args:
    asset_data (AssetData): 

Returns:
    str:

<a id="unreal.AssetRegistryHelpers.get_export_text_name"></a>

#### get_export_text_name

```python
@classmethod
def get_export_text_name(cls, asset_data: AssetData) -> str
```

X.get_export_text_name(asset_data) -> str
Returns the name for the asset in the form: Class'ObjectPath'

Args:
    asset_data (AssetData): 

Returns:
    str:

<a id="unreal.AssetRegistryHelpers.get_class"></a>

#### get_class

```python
@classmethod
def get_class(cls, asset_data: AssetData) -> Class
```

X.get_class(asset_data) -> type(Class)
Get Class

Args:
    asset_data (AssetData): 

Returns:
    type(Class):

<a id="unreal.AssetRegistryHelpers.get_blueprint_assets"></a>

#### get_blueprint_assets

```python
@classmethod
def get_blueprint_assets(cls, filter: ARFilter) -> Array[AssetData]
```

X.get_blueprint_assets(filter) -> Array[AssetData]
Gets asset data for all blueprint assets that match the filter. ClassPaths in the filter specify the blueprint's parent class.

Args:
    filter (ARFilter): 

Returns:
    Array[AssetData]: 

    out_asset_data (Array[AssetData]):

<a id="unreal.AssetRegistryHelpers.get_asset_registry"></a>

#### get_asset_registry

```python
@classmethod
def get_asset_registry(cls) -> AssetRegistry
```

X.get_asset_registry() -> AssetRegistry
Get Asset Registry

Returns:
    AssetRegistry:

<a id="unreal.AssetRegistryHelpers.get_asset"></a>

#### get_asset

```python
@classmethod
def get_asset(cls, asset_data: AssetData) -> Object
```

X.get_asset(asset_data) -> Object
Returns the asset UObject if it is loaded or loads the asset if it is unloaded then returns the result

Args:
    asset_data (AssetData): 

Returns:
    Object:

<a id="unreal.AssetRegistryHelpers.find_asset_native_class"></a>

#### find_asset_native_class

```python
@classmethod
def find_asset_native_class(cls, asset_data: AssetData) -> Class
```

X.find_asset_native_class(asset_data) -> type(Class)
Returns the first native class of the asset type that can be found.  Normally this is just the FAssetData::GetClass(),
however if the class is a blueprint generated class it may not be loaded.  In which case GetAncestorClassNames will
be used to find the first native super class.  This can be slow if temporary caching mode is not on.

Args:
    asset_data (AssetData): 

Returns:
    type(Class):

<a id="unreal.AssetRegistryHelpers.create_asset_data"></a>

#### create_asset_data

```python
@classmethod
def create_asset_data(cls,
                      asset: Object,
                      allow_blueprint_class: bool = False) -> AssetData
```

X.create_asset_data(asset, allow_blueprint_class=False) -> AssetData
Creates asset data from a UObject.

Args:
    asset (Object): The asset to create asset data for
    allow_blueprint_class (bool): By default trying to create asset data for a blueprint class will create one for the UBlueprint instead

Returns:
    AssetData:

<a id="unreal.AssetRegistry"></a>