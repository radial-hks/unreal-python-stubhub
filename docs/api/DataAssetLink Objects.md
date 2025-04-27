## DataAssetLink Objects

```python
class DataAssetLink(NameSpacedUserData)
```

Namespaced user data which provides access to a linked data asset

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_asset`` (DataAsset):  [Read-Write] If assigned, the data asset link will provide access to the data asset's content.
- ``name_space`` (str):  [Read-Write] The namespace to use when looking up values inside of the user data.

<a id="unreal.DataAssetLink.data_asset"></a>

#### data_asset

```python
@property
def data_asset() -> DataAsset
```

(DataAsset):  [Read-Write] If assigned, the data asset link will provide access to the data asset's content.

<a id="unreal.DataAssetLink.data_asset"></a>

#### data_asset

```python
@data_asset.setter
def data_asset(value: DataAsset) -> None
```

<a id="unreal.RigVMNativized"></a>