## ContentBrowserDataCollectionFilter Objects

```python
class ContentBrowserDataCollectionFilter(StructBase)
```

Data used to filter items by their collection.
note: This will typically limit your query to items that support being inside a collection.

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserDataFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``include_child_collections`` (bool):  [Read-Write] Whether we should include child collections in this query

<a id="unreal.ContentBrowserDataCollectionFilter.__init__"></a>

#### __init__

```python
def __init__(include_child_collections: bool = False) -> None
```

<a id="unreal.ContentBrowserDataCollectionFilter.include_child_collections"></a>

#### include_child_collections

```python
@property
def include_child_collections() -> bool
```

(bool):  [Read-Write] Whether we should include child collections in this query

<a id="unreal.ContentBrowserDataCollectionFilter.include_child_collections"></a>

#### include_child_collections

```python
@include_child_collections.setter
def include_child_collections(value: bool) -> None
```

<a id="unreal.ContentBrowserFolderContentsFilter"></a>