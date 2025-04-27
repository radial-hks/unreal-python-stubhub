## FileMediaSource Objects

```python
class FileMediaSource(BaseMediaSource)
```

File Media Source

**C++ Source:**

- **Module**: MediaAssets
- **File**: FileMediaSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``file_path`` (str):  [Read-Write] The path to the media file to be played.
  see: SetFilePath
- ``platform_player_names`` (Map[str, Name]):  [Read-Write] Override native media player plug-ins per platform (Empty = find one automatically).
- ``precache_file`` (bool):  [Read-Write] Load entire media file into memory and play from there (if possible).

<a id="unreal.FileMediaSource.file_path"></a>

#### file_path

```python
@property
def file_path() -> str
```

(str):  [Read-Write] The path to the media file to be played.
see: SetFilePath

<a id="unreal.FileMediaSource.file_path"></a>

#### file_path

```python
@file_path.setter
def file_path(value: str) -> None
```

<a id="unreal.FileMediaSource.precache_file"></a>

#### precache_file

```python
@property
def precache_file() -> bool
```

(bool):  [Read-Write] Load entire media file into memory and play from there (if possible).

<a id="unreal.FileMediaSource.precache_file"></a>

#### precache_file

```python
@precache_file.setter
def precache_file(value: bool) -> None
```

<a id="unreal.FileMediaSource.set_file_path"></a>

#### set_file_path

```python
def set_file_path(path: str) -> None
```

x.set_file_path(path) -> None
Set the path to the media file that this source represents.

Automatically converts full paths to media sources that reside in the
Engine's or project's /Content/Movies directory into relative paths.
see: FilePath, GetFilePath

Args:
    path (str): The path to set.

<a id="unreal.MediaComponent"></a>