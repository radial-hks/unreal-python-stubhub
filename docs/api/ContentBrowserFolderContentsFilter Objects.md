## ContentBrowserFolderContentsFilter Objects

```python
class ContentBrowserFolderContentsFilter(StructBase)
```

* Structure used to optionally filter folders by their broad contents

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserDataFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item_attribute_filter`` (ContentBrowserItemAttributeFilter):  [Read-Write]
- ``item_category_filter`` (ContentBrowserItemCategoryFilter):  [Read-Write]
- ``item_type_filter`` (ContentBrowserItemTypeFilter):  [Read-Write]

<a id="unreal.ContentBrowserFolderContentsFilter.__init__"></a>

#### __init__

```python
def __init__(
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

<a id="unreal.ContentBrowserFolderContentsFilter.item_type_filter"></a>

#### item_type_filter

```python
@property
def item_type_filter() -> ContentBrowserItemTypeFilter
```

(ContentBrowserItemTypeFilter):  [Read-Write]

<a id="unreal.ContentBrowserFolderContentsFilter.item_type_filter"></a>

#### item_type_filter

```python
@item_type_filter.setter
def item_type_filter(value: ContentBrowserItemTypeFilter) -> None
```

<a id="unreal.ContentBrowserFolderContentsFilter.item_category_filter"></a>

#### item_category_filter

```python
@property
def item_category_filter() -> ContentBrowserItemCategoryFilter
```

(ContentBrowserItemCategoryFilter):  [Read-Write]

<a id="unreal.ContentBrowserFolderContentsFilter.item_category_filter"></a>

#### item_category_filter

```python
@item_category_filter.setter
def item_category_filter(value: ContentBrowserItemCategoryFilter) -> None
```

<a id="unreal.ContentBrowserFolderContentsFilter.item_attribute_filter"></a>

#### item_attribute_filter

```python
@property
def item_attribute_filter() -> ContentBrowserItemAttributeFilter
```

(ContentBrowserItemAttributeFilter):  [Read-Write]

<a id="unreal.ContentBrowserFolderContentsFilter.item_attribute_filter"></a>

#### item_attribute_filter

```python
@item_attribute_filter.setter
def item_attribute_filter(value: ContentBrowserItemAttributeFilter) -> None
```

<a id="unreal.ContentBrowserItem"></a>