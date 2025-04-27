## ContentBrowserDataFilter Objects

```python
class ContentBrowserDataFilter(StructBase)
```

A filter used to control what is returned from Content Browser data queries.
note: The compiled version of this, FContentBrowserDataCompiledFilter, is produced via UContentBrowserDataSubsystem::CompileFilter.

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserDataFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item_attribute_filter`` (ContentBrowserItemAttributeFilter):  [Read-Write] Flags controlling which item attributes should be included in this query
- ``item_category_filter`` (ContentBrowserItemCategoryFilter):  [Read-Write] Flags controlling which item categories should be included in this query
- ``item_type_filter`` (ContentBrowserItemTypeFilter):  [Read-Write] Flags controlling which item types should be included in this query
- ``recursive_paths`` (bool):  [Read-Write] Whether we should include sub-paths in this query

<a id="unreal.ContentBrowserDataFilter.__init__"></a>

#### __init__

```python
def __init__(
    recursive_paths: bool = False,
    item_type_filter:
    ContentBrowserItemTypeFilter = ContentBrowserItemTypeFilter.INCLUDE_NONE,
    item_category_filter:
    ContentBrowserItemCategoryFilter = ContentBrowserItemCategoryFilter.
    INCLUDE_NONE,
    item_attribute_filter:
    ContentBrowserItemAttributeFilter = ContentBrowserItemAttributeFilter.
    INCLUDE_NONE
) -> None
```

<a id="unreal.ContentBrowserDataFilter.recursive_paths"></a>

#### recursive_paths

```python
@property
def recursive_paths() -> bool
```

(bool):  [Read-Write] Whether we should include sub-paths in this query

<a id="unreal.ContentBrowserDataFilter.recursive_paths"></a>

#### recursive_paths

```python
@recursive_paths.setter
def recursive_paths(value: bool) -> None
```

<a id="unreal.ContentBrowserDataFilter.item_type_filter"></a>

#### item_type_filter

```python
@property
def item_type_filter() -> ContentBrowserItemTypeFilter
```

(ContentBrowserItemTypeFilter):  [Read-Write] Flags controlling which item types should be included in this query

<a id="unreal.ContentBrowserDataFilter.item_type_filter"></a>

#### item_type_filter

```python
@item_type_filter.setter
def item_type_filter(value: ContentBrowserItemTypeFilter) -> None
```

<a id="unreal.ContentBrowserDataFilter.item_category_filter"></a>

#### item_category_filter

```python
@property
def item_category_filter() -> ContentBrowserItemCategoryFilter
```

(ContentBrowserItemCategoryFilter):  [Read-Write] Flags controlling which item categories should be included in this query

<a id="unreal.ContentBrowserDataFilter.item_category_filter"></a>

#### item_category_filter

```python
@item_category_filter.setter
def item_category_filter(value: ContentBrowserItemCategoryFilter) -> None
```

<a id="unreal.ContentBrowserDataFilter.item_attribute_filter"></a>

#### item_attribute_filter

```python
@property
def item_attribute_filter() -> ContentBrowserItemAttributeFilter
```

(ContentBrowserItemAttributeFilter):  [Read-Write] Flags controlling which item attributes should be included in this query

<a id="unreal.ContentBrowserDataFilter.item_attribute_filter"></a>

#### item_attribute_filter

```python
@item_attribute_filter.setter
def item_attribute_filter(value: ContentBrowserItemAttributeFilter) -> None
```

<a id="unreal.ContentBrowserDataObjectFilter"></a>