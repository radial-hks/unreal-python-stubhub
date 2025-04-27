## ContentBrowserItemPathExtensions Objects

```python
class ContentBrowserItemPathExtensions(BlueprintFunctionLibrary)
```

Content Browser Item Path Extensions

**C++ Source:**

- **Module**: ContentBrowserData
- **File**: ContentBrowserItemPath.h

<a id="unreal.ContentBrowserItemPathExtensions.set_path"></a>

#### set_path

```python
@classmethod
def set_path(cls, item_path: ContentBrowserItemPath, path: Name,
             path_type: ContentBrowserPathType) -> ContentBrowserItemPath
```

X.set_path(item_path, path, path_type) -> ContentBrowserItemPath
Set the path being stored

Args:
    item_path (ContentBrowserItemPath): 
    path (Name): 
    path_type (ContentBrowserPathType): 

Returns:
    ContentBrowserItemPath: 

    item_path (ContentBrowserItemPath):

<a id="unreal.ContentBrowserItemPathExtensions.get_virtual_path"></a>

#### get_virtual_path

```python
@classmethod
def get_virtual_path(cls, item_path: ContentBrowserItemPath) -> Name
```

X.get_virtual_path(item_path) -> Name
Returns virtual path as FName (eg, "/All/Plugins/PluginA/MyFile").

Args:
    item_path (ContentBrowserItemPath): 

Returns:
    Name:

<a id="unreal.ContentBrowserItemPathExtensions.get_internal_path"></a>

#### get_internal_path

```python
@classmethod
def get_internal_path(cls, item_path: ContentBrowserItemPath) -> Name
```

X.get_internal_path(item_path) -> Name
Returns internal path if there is one (eg,. "/PluginA/MyFile").

Args:
    item_path (ContentBrowserItemPath): 

Returns:
    Name:

<a id="unreal.SlateFXSubsystem"></a>