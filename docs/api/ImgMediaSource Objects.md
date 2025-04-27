## ImgMediaSource Objects

```python
class ImgMediaSource(BaseMediaSource)
```

Media source for EXR image sequences.

Image sequence media sources point to a directory that contains a series of
image files in which each image represents a single frame of the sequence.
BMP, EXR, PNG and JPG images are currently supported. EXR image sequences
are optimized for performance. The first frame of an image sequence is used
to determine the image dimensions (all formats) and frame rate (EXR only).

The image sequence directory may contain sub-directories, which are called
'proxies'. Proxies can be used to provide alternative media for playback
during development and testing of a game. One common scenario is the use
of low resolution versions of image sequence media on computers that are
too slow or don't have enough storage to play the original high-res media.

**C++ Source:**

- **Plugin**: ImgMedia
- **Module**: ImgMedia
- **File**: ImgMediaSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fill_gaps_in_sequence`` (bool):  [Read-Write] If true, then any gaps in the sequence will be filled with blank frames.
- ``frame_rate_override`` (FrameRate):  [Read-Write] Overrides the default frame rate stored in the image files (0/0 = do not override).
- ``platform_player_names`` (Map[str, Name]):  [Read-Write] Override native media player plug-ins per platform (Empty = find one automatically).
- ``proxy_override`` (str):  [Read-Write] Name of the proxy directory to use.
- ``sequence_path`` (DirectoryPath):  [Read-Write] The directory that contains the image sequence files.

  - Relative paths will be with respect to the current Project directory.
  - You may use {engine_dir} or {project_dir} tokens.
- ``sequence_proxy`` (ImgMediaSourceCustomizationSequenceProxy):  [Read-Write] This is only used so we can customize editing of SequencePath.
- ``start_timecode`` (Timecode):  [Read-Write] Specification of a timecode associated with the start of the sequence.

<a id="unreal.ImgMediaSource.frame_rate_override"></a>

#### frame_rate_override

```python
@property
def frame_rate_override() -> FrameRate
```

(FrameRate):  [Read-Write] Overrides the default frame rate stored in the image files (0/0 = do not override).

<a id="unreal.ImgMediaSource.frame_rate_override"></a>

#### frame_rate_override

```python
@frame_rate_override.setter
def frame_rate_override(value: FrameRate) -> None
```

<a id="unreal.ImgMediaSource.proxy_override"></a>

#### proxy_override

```python
@property
def proxy_override() -> str
```

(str):  [Read-Write] Name of the proxy directory to use.

<a id="unreal.ImgMediaSource.proxy_override"></a>

#### proxy_override

```python
@proxy_override.setter
def proxy_override(value: str) -> None
```

<a id="unreal.ImgMediaSource.fill_gaps_in_sequence"></a>

#### fill_gaps_in_sequence

```python
@property
def fill_gaps_in_sequence() -> bool
```

(bool):  [Read-Write] If true, then any gaps in the sequence will be filled with blank frames.

<a id="unreal.ImgMediaSource.fill_gaps_in_sequence"></a>

#### fill_gaps_in_sequence

```python
@fill_gaps_in_sequence.setter
def fill_gaps_in_sequence(value: bool) -> None
```

<a id="unreal.ImgMediaSource.start_timecode"></a>

#### start_timecode

```python
@property
def start_timecode() -> Timecode
```

(Timecode):  [Read-Only] Specification of a timecode associated with the start of the sequence.

<a id="unreal.ImgMediaSource.sequence_path"></a>

#### sequence_path

```python
@property
def sequence_path() -> DirectoryPath
```

(DirectoryPath):  [Read-Only] The directory that contains the image sequence files.

- Relative paths will be with respect to the current Project directory.
- You may use {engine_dir} or {project_dir} tokens.

<a id="unreal.ImgMediaSource.set_tokenized_sequence_path"></a>

#### set_tokenized_sequence_path

```python
def set_tokenized_sequence_path(path: str) -> None
```

x.set_tokenized_sequence_path(path) -> None
Set the path to the image sequence directory this source represents.
see: GetSequencePath

Args:
    path (str): The path to the desired image sequence directory. May contain supported tokens.

<a id="unreal.ImgMediaSource.set_sequence_path"></a>

#### set_sequence_path

```python
def set_sequence_path(path: str) -> None
```

x.set_sequence_path(path) -> None
Set the path to the image sequence directory this source represents.
see: GetSequencePath

Args:
    path (str): The path to an image file in the desired directory.

<a id="unreal.ImgMediaSource.remove_target_object"></a>

#### remove_target_object

```python
def remove_target_object(actor: Actor) -> None
```

x.remove_target_object(actor) -> None
This object is no longer using our img sequence.

Args:
    actor (Actor): Object no longer using our img sequence.

<a id="unreal.ImgMediaSource.get_sequence_path"></a>

#### get_sequence_path

```python
def get_sequence_path() -> str
```

x.get_sequence_path() -> str
Get the path to the image sequence directory to be played. Supported tokens will be expanded.
see: SetSequencePath

Returns:
    str: The file path.

<a id="unreal.ImgMediaSource.get_proxies"></a>

#### get_proxies

```python
def get_proxies() -> Array[str]
```

x.get_proxies() -> Array[str]
Get the names of available proxy directories.
see: GetSequencePath

Returns:
    Array[str]: 

    out_proxies (Array[str]): Will contain the names of available proxy directories, if any.

<a id="unreal.ImgMediaSource.add_target_object"></a>

#### add_target_object

```python
def add_target_object(actor: Actor) -> None
```

x.add_target_object(actor) -> None
This object is using our img sequence.

Args:
    actor (Actor): Object using our img sequence.

<a id="unreal.MovieSceneMediaPlayerPropertySection"></a>