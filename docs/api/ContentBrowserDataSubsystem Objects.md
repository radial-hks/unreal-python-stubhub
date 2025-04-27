## ContentBrowserDataSubsystem Objects

```python
class ContentBrowserDataSubsystem(EditorSubsystem)
```

Subsystem that provides access to Content Browser data.
This type deals with the composition of multiple data sources, which provide information about the folders and files available in the Content Browser.

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserDataSubsystem.h

<a id="unreal.ContentBrowserDataSubsystem.get_items_under_path"></a>

#### get_items_under_path

```python
def get_items_under_path(
        path: Name,
        filter: ContentBrowserDataFilter) -> Array[ContentBrowserItem]
```

x.get_items_under_path(path, filter) -> Array[ContentBrowserItem]
Get the items (folders and/or files) that exist under the given virtual path.

Args:
    path (Name): 
    filter (ContentBrowserDataFilter): 

Returns:
    Array[ContentBrowserItem]:

<a id="unreal.ContentBrowserDataSubsystem.get_items_at_path"></a>

#### get_items_at_path

```python
def get_items_at_path(
    path: Name, item_type_filter: ContentBrowserItemTypeFilter
) -> Array[ContentBrowserItem]
```

x.get_items_at_path(path, item_type_filter) -> Array[ContentBrowserItem]
Get the items (folders and/or files) that exist at the given virtual path.
note: Multiple items may have the same virtual path if they are different types, or come from different data sources.

Args:
    path (Name): 
    item_type_filter (ContentBrowserItemTypeFilter): 

Returns:
    Array[ContentBrowserItem]:

<a id="unreal.ContentBrowserDataSubsystem.get_item_at_path"></a>

#### get_item_at_path

```python
def get_item_at_path(
        path: Name,
        item_type_filter: ContentBrowserItemTypeFilter) -> ContentBrowserItem
```

x.get_item_at_path(path, item_type_filter) -> ContentBrowserItem
Get the first item (folder and/or file) that exists at the given virtual path.

Args:
    path (Name): 
    item_type_filter (ContentBrowserItemTypeFilter): 

Returns:
    ContentBrowserItem:

<a id="unreal.ContentBrowserDataSubsystem.get_available_data_sources"></a>

#### get_available_data_sources

```python
def get_available_data_sources() -> Array[Name]
```

x.get_available_data_sources() -> Array[Name]
Get the list of current available data sources.

Returns:
    Array[Name]:

<a id="unreal.ContentBrowserDataSubsystem.get_active_data_sources"></a>

#### get_active_data_sources

```python
def get_active_data_sources() -> Array[Name]
```

x.get_active_data_sources() -> Array[Name]
Get the list of current active data sources.

Returns:
    Array[Name]:

<a id="unreal.ContentBrowserDataSubsystem.deactivate_data_source"></a>

#### deactivate_data_source

```python
def deactivate_data_source(name: Name) -> bool
```

x.deactivate_data_source(name) -> bool
Attempt to deactivate the named data source.

Args:
    name (Name): 

Returns:
    bool: True if the data source was available and active, false otherwise.

<a id="unreal.ContentBrowserDataSubsystem.deactivate_all_data_sources"></a>

#### deactivate_all_data_sources

```python
def deactivate_all_data_sources() -> None
```

x.deactivate_all_data_sources() -> None
Deactivate all active data sources.

<a id="unreal.ContentBrowserDataSubsystem.activate_data_source"></a>

#### activate_data_source

```python
def activate_data_source(name: Name) -> bool
```

x.activate_data_source(name) -> bool
Attempt to activate the named data source.

Args:
    name (Name): 

Returns:
    bool: True if the data source was available and not already active, false otherwise.

<a id="unreal.ContentBrowserDataSubsystem.activate_all_data_sources"></a>

#### activate_all_data_sources

```python
def activate_all_data_sources() -> None
```

x.activate_all_data_sources() -> None
Activate all available data sources.

<a id="unreal.ContentBrowserItemLibrary"></a>