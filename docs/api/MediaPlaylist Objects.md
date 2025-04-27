## MediaPlaylist Objects

```python
class MediaPlaylist(Object)
```

Implements a media play list.

**C++ Source:**

- **Module**: MediaAssets
- **File**: MediaPlaylist.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[MediaSource]):  [Read-Write] List of media sources to play.

<a id="unreal.MediaPlaylist.replace"></a>

#### replace

```python
def replace(index: int, replacement: MediaSource) -> bool
```

x.replace(index, replacement) -> bool
Replace the media source at the specified position.
see: Add, Insert, RemoveAll, RemoveAt

Args:
    index (int32): The index of the media source to replace.
    replacement (MediaSource): The replacement media source.

Returns:
    bool: true if the media source was replaced, false otherwise.

<a id="unreal.MediaPlaylist.remove_at"></a>

#### remove_at

```python
def remove_at(index: int) -> bool
```

x.remove_at(index) -> bool
Remove the media source at the specified position.
see: Add, Insert, RemoveAll, Replace

Args:
    index (int32): The index of the media source to remove.

Returns:
    bool: true if the media source was removed, false otherwise.

<a id="unreal.MediaPlaylist.remove"></a>

#### remove

```python
def remove(media_source: MediaSource) -> bool
```

x.remove(media_source) -> bool
Remove all occurrences of the given media source in the play list.
see: Add, Insert, Remove, Replace

Args:
    media_source (MediaSource): The media source to remove.

Returns:
    bool: true if the media source was removed, false otherwise.

<a id="unreal.MediaPlaylist.num"></a>

#### num

```python
def num() -> int
```

x.num() -> int32
Get the number of media sources in the play list.

Returns:
    int32: Number of media sources.

<a id="unreal.MediaPlaylist.insert"></a>

#### insert

```python
def insert(media_source: MediaSource, index: int) -> None
```

x.insert(media_source, index) -> None
Insert a media source into the play list at the given position.
see: Add, Remove, RemoveAll, Replace

Args:
    media_source (MediaSource): The media source to insert.
    index (int32): The index to insert into.

<a id="unreal.MediaPlaylist.get_random"></a>

#### get_random

```python
def get_random() -> Tuple[MediaSource, int]
```

x.get_random() -> (MediaSource, out_index=int32)
Get a random media source in the play list.
see: Get, GetNext, GetPrevious

Returns:
    int32: The random media source, or nullptr if the list is empty.

    out_index (int32): Will contain the index of the returned media source.

<a id="unreal.MediaPlaylist.get_previous"></a>

#### get_previous

```python
def get_previous() -> Tuple[MediaSource, int]
```

x.get_previous() -> (MediaSource, out_index=int32)
Get the previous media source in the play list.
see: , GetNext, GetRandom

Returns:
    int32: The media source before the current one, or nullptr if the list is empty.

    out_index (int32): Index of the current media source (will contain the new index).

<a id="unreal.MediaPlaylist.get_next"></a>

#### get_next

```python
def get_next() -> Tuple[MediaSource, int]
```

x.get_next() -> (MediaSource, out_index=int32)
Get the next media source in the play list.
see: , GetPrevious, GetRandom

Returns:
    int32: The media source after the current one, or nullptr if the list is empty.

    out_index (int32): Index of the current media source (will contain the new index).

<a id="unreal.MediaPlaylist.get"></a>

#### get

```python
def get(index: int) -> MediaSource
```

x.get(index) -> MediaSource
Get the media source at the specified index.
see: GetNext, GetRandom

Args:
    index (int32): The index of the media source to get.

Returns:
    MediaSource: The media source, or nullptr if the index doesn't exist.

<a id="unreal.MediaPlaylist.add_url"></a>

#### add_url

```python
def add_url(url: str) -> bool
```

x.add_url(url) -> bool
Add a media URL to the play list.
see: Add, AddFile, Insert, RemoveAll, Remove, Replace

Args:
    url (str): The URL to add.

Returns:
    bool: true if the URL was added, false otherwise.

<a id="unreal.MediaPlaylist.add_file"></a>

#### add_file

```python
def add_file(file_path: str) -> bool
```

x.add_file(file_path) -> bool
Add a media file path to the play list.
see: Add, AddUrl, Insert, RemoveAll, Remove, Replace

Args:
    file_path (str): The file path to add.

Returns:
    bool: true if the file was added, false otherwise.

<a id="unreal.MediaPlaylist.add"></a>

#### add

```python
def add(media_source: MediaSource) -> bool
```

x.add(media_source) -> bool
Add a media source to the play list.
see: AddFile, AddUrl, Insert, RemoveAll, Remove, Replace

Args:
    media_source (MediaSource): The media source to append.

Returns:
    bool: true if the media source was added, false otherwise.

<a id="unreal.MediaSoundComponent"></a>