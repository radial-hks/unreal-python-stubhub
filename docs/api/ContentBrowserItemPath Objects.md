## ContentBrowserItemPath Objects

```python
class ContentBrowserItemPath(StructBase)
```

Hold multiple versions of a path as FNames

Path conversion each time Set is called

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserItemPath.h

<a id="unreal.ContentBrowserItemPath.__init__"></a>

#### __init__

```python
def __init__(
        path: Name = "None",
        path_type: ContentBrowserPathType = ContentBrowserPathType.NONE
) -> None
```

<a id="unreal.ContentBrowserItemPath.set_path"></a>

#### set_path

```python
def set_path(path: Name, path_type: ContentBrowserPathType) -> None
```

x.set_path(path, path_type) -> None
Set the path being stored

Args:
    path (Name): 
    path_type (ContentBrowserPathType):

<a id="unreal.ContentBrowserItemPath.get_virtual_path"></a>

#### get_virtual_path

```python
def get_virtual_path() -> Name
```

x.get_virtual_path() -> Name
Returns virtual path as FName (eg, "/All/Plugins/PluginA/MyFile").

Returns:
    Name:

<a id="unreal.ContentBrowserItemPath.get_internal_path"></a>

#### get_internal_path

```python
def get_internal_path() -> Name
```

x.get_internal_path() -> Name
Returns internal path if there is one (eg,. "/PluginA/MyFile").

Returns:
    Name:

<a id="unreal.SlatePostSettings"></a>