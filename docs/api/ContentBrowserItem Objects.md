## ContentBrowserItem Objects

```python
class ContentBrowserItem(StructBase)
```

Representation of a Content Browser item.

FContentBrowserItem is potentially a composite of multiple internal items (eg, combining equivalent folder items from different data sources),
and defers back to these internal items to provide its functionality (via the data source that owns each internal item).

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserItem.h

<a id="unreal.ContentBrowserItem.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ContentBrowserItem.is_folder"></a>

#### is_folder

```python
def is_folder() -> bool
```

x.is_folder() -> bool
Is Folder

Returns:
    bool:

<a id="unreal.ContentBrowserItem.is_file"></a>

#### is_file

```python
def is_file() -> bool
```

x.is_file() -> bool
Is File

Returns:
    bool:

<a id="unreal.ContentBrowserItem.get_virtual_path"></a>

#### get_virtual_path

```python
def get_virtual_path() -> Name
```

x.get_virtual_path() -> Name
Get Virtual Path

Returns:
    Name:

<a id="unreal.ContentBrowserItem.get_display_name"></a>

#### get_display_name

```python
def get_display_name() -> Text
```

x.get_display_name() -> Text
Get Display Name

Returns:
    Text:

<a id="unreal.ContentBrowserItemPath"></a>