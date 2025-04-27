## TypedElementAssetDataInterface Objects

```python
class TypedElementAssetDataInterface(Interface)
```

Typed Element Asset Data Interface

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementAssetDataInterface.h

<a id="unreal.TypedElementAssetDataInterface.get_asset_data"></a>

#### get_asset_data

```python
def get_asset_data(element_handle: ScriptTypedElementHandle) -> AssetData
```

x.get_asset_data(element_handle) -> AssetData
Returns the asset data for the given handle, if it exists.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    AssetData:

<a id="unreal.TypedElementAssetDataInterface.get_all_referenced_asset_datas"></a>

#### get_all_referenced_asset_datas

```python
def get_all_referenced_asset_datas(
        element_handle: ScriptTypedElementHandle) -> Array[AssetData]
```

x.get_all_referenced_asset_datas(element_handle) -> Array[AssetData]
Returns any asset datas for content objects referenced by handle.
If the given handle itself has valid asset data, it should be returned as the last element of the array.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    Array[AssetData]: An array of valid asset datas.

<a id="unreal.TypedElementHierarchyInterface"></a>