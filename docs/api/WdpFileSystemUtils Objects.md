## WdpFileSystemUtils Objects

```python
class WdpFileSystemUtils(Object)
```

Wdp File System Utils

**C++ Source:**

- **Plugin**: WdpCommon
- **Module**: WdpFileSystem
- **File**: WdpFileSystemUtils.h

<a id="unreal.WdpFileSystemUtils.normalize_path"></a>

#### normalize\_path

```python
@classmethod
def normalize_path(cls, path: str) -> str
```

X.normalize_path(path) -> str
Normalize Path

Args:
    path (str): 

Returns:
    str:

<a id="unreal.WdpFileSystemUtils.mount_pak"></a>

#### mount\_pak

```python
@classmethod
def mount_pak(cls,
              pak_filename: str,
              root_path: str,
              abs_url: bool = False) -> bool
```

X.mount_pak(pak_filename, root_path, abs_url=False) -> bool

brief: 

Args:
    pak_filename (str): 
    root_path (str): 
    abs_url (bool): 

Returns:
    bool:

<a id="unreal.WdpFileSystemUtils.mount"></a>

#### mount

```python
@classmethod
def mount(cls,
          content_path: str,
          root_path: str,
          server_prefix: str = "",
          server_list_key: str = "",
          abs_url: bool = False) -> None
```

X.mount(content_path, root_path, server_prefix="", server_list_key="", abs_url=False) -> None

brief: 

Args:
    content_path (str): 
    root_path (str): 
    server_prefix (str): 
    server_list_key (str): 
    abs_url (bool):

<a id="unreal.WdpFileSystemUtils.get_mount_point_from_root_path"></a>

#### get\_mount\_point\_from\_root\_path

```python
@classmethod
def get_mount_point_from_root_path(cls, root_path: str) -> str
```

X.get_mount_point_from_root_path(root_path) -> str
Get Mount Point from Root Path

Args:
    root_path (str): 

Returns:
    str:

<a id="unreal.WdpFileSystemUtils.create_mount_root_path"></a>

#### create\_mount\_root\_path

```python
@classmethod
def create_mount_root_path(cls,
                           root_path: str,
                           project_mount_path: str,
                           abs_url: bool = False) -> None
```

X.create_mount_root_path(root_path, project_mount_path, abs_url=False) -> None
Create Mount Root Path

Args:
    root_path (str): 
    project_mount_path (str): 
    abs_url (bool):

<a id="unreal.AesFileSystemLibrary"></a>