## StreamMediaSource Objects

```python
class StreamMediaSource(BaseMediaSource)
```

Stream Media Source

**C++ Source:**

- **Module**: MediaAssets
- **File**: StreamMediaSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``platform_player_names`` (Map[str, Name]):  [Read-Write] Override native media player plug-ins per platform (Empty = find one automatically).
- ``stream_url`` (str):  [Read-Write] The URL to the media stream to be played.

<a id="unreal.StreamMediaSource.stream_url"></a>

#### stream_url

```python
@property
def stream_url() -> str
```

(str):  [Read-Write] The URL to the media stream to be played.

<a id="unreal.StreamMediaSource.stream_url"></a>

#### stream_url

```python
@stream_url.setter
def stream_url(value: str) -> None
```

<a id="unreal.TimeSynchronizableMediaSource"></a>