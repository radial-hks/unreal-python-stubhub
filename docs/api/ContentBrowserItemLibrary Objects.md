## ContentBrowserItemLibrary Objects

```python
class ContentBrowserItemLibrary(BlueprintFunctionLibrary)
```

TODO: Script API exposure

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserItem.h

<a id="unreal.ContentBrowserItemLibrary.is_folder"></a>

#### is_folder

```python
@classmethod
def is_folder(cls, item: ContentBrowserItem) -> bool
```

X.is_folder(item) -> bool
Is Folder

Args:
    item (ContentBrowserItem): 

Returns:
    bool:

<a id="unreal.ContentBrowserItemLibrary.is_file"></a>

#### is_file

```python
@classmethod
def is_file(cls, item: ContentBrowserItem) -> bool
```

X.is_file(item) -> bool
Is File

Args:
    item (ContentBrowserItem): 

Returns:
    bool:

<a id="unreal.ContentBrowserItemLibrary.get_virtual_path"></a>

#### get_virtual_path

```python
@classmethod
def get_virtual_path(cls, item: ContentBrowserItem) -> Name
```

X.get_virtual_path(item) -> Name
Get Virtual Path

Args:
    item (ContentBrowserItem): 

Returns:
    Name:

<a id="unreal.ContentBrowserItemLibrary.get_display_name"></a>

#### get_display_name

```python
@classmethod
def get_display_name(cls, item: ContentBrowserItem) -> Text
```

X.get_display_name(item) -> Text
Get Display Name

Args:
    item (ContentBrowserItem): 

Returns:
    Text:

<a id="unreal.ContentBrowserItemPathExtensions"></a>