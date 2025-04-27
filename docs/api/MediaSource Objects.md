## MediaSource Objects

```python
class MediaSource(Object)
```

Abstract base class for media sources.

Media sources describe the location and/or settings of media objects that can
be played in a media player, such as a video file on disk, a video stream on
the internet, or a web cam attached to or built into the target device. The
location is encoded as a media URL string, whose URI scheme and optional file
extension will be used to locate a suitable media player.

**C++ Source:**

- **Module**: MediaAssets
- **File**: MediaSource.h

<a id="unreal.MediaSource.validate"></a>

#### validate

```python
def validate() -> bool
```

x.validate() -> bool
Validate the media source settings (must be implemented in child classes).

Returns:
    bool: true if validation passed, false otherwise.

<a id="unreal.MediaSource.set_media_option_string"></a>

#### set_media_option_string

```python
def set_media_option_string(key: Name, value: str) -> None
```

x.set_media_option_string(key, value) -> None
Set a string parameter to pass to the player.

Args:
    key (Name): 
    value (str):

<a id="unreal.MediaSource.set_media_option_int64"></a>

#### set_media_option_int64

```python
def set_media_option_int64(key: Name, value: int) -> None
```

x.set_media_option_int64(key, value) -> None
Set an integer64 parameter to pass to the player.

Args:
    key (Name): 
    value (int64):

<a id="unreal.MediaSource.set_media_option_float"></a>

#### set_media_option_float

```python
def set_media_option_float(key: Name, value: float) -> None
```

x.set_media_option_float(key, value) -> None
Set a float parameter to pass to the player.

Args:
    key (Name): 
    value (float):

<a id="unreal.MediaSource.set_media_option_bool"></a>

#### set_media_option_bool

```python
def set_media_option_bool(key: Name, value: bool) -> None
```

x.set_media_option_bool(key, value) -> None
Set a boolean parameter to pass to the player.

Args:
    key (Name): 
    value (bool):

<a id="unreal.MediaSource.get_url"></a>

#### get_url

```python
def get_url() -> str
```

x.get_url() -> str
Get the media source's URL string (must be implemented in child classes).
see: GetProxies

Returns:
    str: The media URL.

<a id="unreal.BaseMediaSource"></a>