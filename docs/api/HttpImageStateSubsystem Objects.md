## HttpImageStateSubsystem Objects

```python
class HttpImageStateSubsystem(GameInstanceSubsystem)
```

Http Image State Subsystem

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: HttpImageStateSubsystem.h

<a id="unreal.HttpImageStateSubsystem.set_http_image_state"></a>

#### set\_http\_image\_state

```python
def set_http_image_state(url: str, http_image_state: HttpImageState,
                         texture: Texture2DDynamic) -> None
```

x.set_http_image_state(url, http_image_state, texture) -> None
Set Http Image State

Args:
    url (str): 
    http_image_state (HttpImageState): 
    texture (Texture2DDynamic):

<a id="unreal.HttpImageStateSubsystem.remove_http_image_state"></a>

#### remove\_http\_image\_state

```python
def remove_http_image_state(url: str) -> bool
```

x.remove_http_image_state(url) -> bool
Remove Http Image State

Args:
    url (str): 

Returns:
    bool:

<a id="unreal.HttpImageStateSubsystem.get_http_image_state"></a>

#### get\_http\_image\_state

```python
def get_http_image_state(url: str) -> Optional[HttpImageStateData]
```

x.get_http_image_state(url) -> HttpImageStateData or None
Get Http Image State

Args:
    url (str): 

Returns:
    HttpImageStateData or None: 

    out_http_image_state_data (HttpImageStateData):

<a id="unreal.HttpImageStateSubsystem.get"></a>

#### get

```python
@classmethod
def get(cls) -> HttpImageStateSubsystem
```

X.get() -> HttpImageStateSubsystem
Get

Returns:
    HttpImageStateSubsystem:

<a id="unreal.LidarPointCloudBPLibrary"></a>