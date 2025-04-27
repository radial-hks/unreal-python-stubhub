## ContentBrowserDataObjectFilter Objects

```python
class ContentBrowserDataObjectFilter(StructBase)
```

Data used to filter object instances by their name and tags.
note: This will typically limit your query to returning assets.

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserDataFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``object_names_to_exclude`` (Array[Name]):  [Read-Write] Array of object names that should be excluded from this query
- ``object_names_to_include`` (Array[Name]):  [Read-Write] Array of object names that should be included in this query
- ``on_disk_objects_only`` (bool):  [Read-Write] Whether we should only include on-disk objects (ignoring those that exist only in memory)

<a id="unreal.ContentBrowserDataObjectFilter.__init__"></a>

#### __init__

```python
def __init__(object_names_to_include: Array[Name] = [],
             object_names_to_exclude: Array[Name] = [],
             on_disk_objects_only: bool = False) -> None
```

<a id="unreal.ContentBrowserDataObjectFilter.object_names_to_include"></a>

#### object_names_to_include

```python
@property
def object_names_to_include() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of object names that should be included in this query

<a id="unreal.ContentBrowserDataObjectFilter.object_names_to_include"></a>

#### object_names_to_include

```python
@object_names_to_include.setter
def object_names_to_include(value: Array[Name]) -> None
```

<a id="unreal.ContentBrowserDataObjectFilter.object_names_to_exclude"></a>

#### object_names_to_exclude

```python
@property
def object_names_to_exclude() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of object names that should be excluded from this query

<a id="unreal.ContentBrowserDataObjectFilter.object_names_to_exclude"></a>

#### object_names_to_exclude

```python
@object_names_to_exclude.setter
def object_names_to_exclude(value: Array[Name]) -> None
```

<a id="unreal.ContentBrowserDataObjectFilter.on_disk_objects_only"></a>

#### on_disk_objects_only

```python
@property
def on_disk_objects_only() -> bool
```

(bool):  [Read-Write] Whether we should only include on-disk objects (ignoring those that exist only in memory)

<a id="unreal.ContentBrowserDataObjectFilter.on_disk_objects_only"></a>

#### on_disk_objects_only

```python
@on_disk_objects_only.setter
def on_disk_objects_only(value: bool) -> None
```

<a id="unreal.ContentBrowserDataPackageFilter"></a>