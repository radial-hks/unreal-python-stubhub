## ContentBrowserAssetContextMenuContext Objects

```python
class ContentBrowserAssetContextMenuContext(Object)
```

Content Browser Asset Context Menu Context

**C++ Source:**

- **Module**: ContentBrowser
- **File**: ContentBrowserMenuContexts.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``contains_unsupported_assets`` (bool):  [Read-Write]
- ``selected_assets`` (Array[AssetData]):  [Read-Write] The currently selected assets in the content browser.

<a id="unreal.ContentBrowserAssetContextMenuContext.selected_assets"></a>

#### selected_assets

```python
@property
def selected_assets() -> Array[AssetData]
```

(Array[AssetData]):  [Read-Only] The currently selected assets in the content browser.

<a id="unreal.ContentBrowserAssetContextMenuContext.contains_unsupported_assets"></a>

#### contains_unsupported_assets

```python
@property
def contains_unsupported_assets() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ContentBrowserAssetContextMenuContext.load_selected_objects_if_needed"></a>

#### load_selected_objects_if_needed

```python
def load_selected_objects_if_needed() -> Array[Object]
```

x.load_selected_objects_if_needed() -> Array[Object]
Loads the selected assets (if needed) which is based on AssetViewUtils::LoadAssetsIfNeeded, this exists primarily
for backwards compatability.  Reliance on a black box to determine 'neededness' is not recommended, this function
will likely be deprecated a few versions after GetSelectedObjects.

Returns:
    Array[Object]:

<a id="unreal.ContentBrowserAssetContextMenuContext.load_selected_objects"></a>

#### load_selected_objects

```python
def load_selected_objects(load_tags: Set[Name]) -> Array[Object]
```

x.load_selected_objects(load_tags) -> Array[Object]
Loads all the selected assets and returns an array of the objects.

Args:
    load_tags (Set[Name]): 

Returns:
    Array[Object]:

<a id="unreal.ContentBrowserAssetContextMenuContext.get_selected_objects"></a>

#### get_selected_objects

```python
def get_selected_objects() -> Array[Object]
```

x.get_selected_objects() -> Array[Object]
Get Selected Objects
deprecated: GetSelectedObjects has been deprecated.  We no longer automatically load assets on right click.  If you can work without loading the assets, please use SelectedAssets.  Otherwise call LoadSelectedObjects

Returns:
    Array[Object]:

<a id="unreal.ContentBrowserMenuContext"></a>