## TimeSynchronizableMediaSource Objects

```python
class TimeSynchronizableMediaSource(BaseMediaSource)
```

Base class for media sources that can be synchronized with the engine's timecode.

**C++ Source:**

- **Module**: MediaAssets
- **File**: TimeSynchronizableMediaSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_delay`` (int32):  [Read-Write] When using Time Synchronization, how many frame back should it read. Capped at 4 frames due to the potential issues with buffer sizes.
  Framelocked modes don't support this feature.
- ``platform_player_names`` (Map[str, Name]):  [Read-Write] Override native media player plug-ins per platform (Empty = find one automatically).
- ``time_delay`` (double):  [Read-Write] When not using Time Synchronization, how far back it time should it read.
- ``use_time_synchronization`` (bool):  [Read-Write] Synchronize the media with the engine's timecode.
  The media player has be able to read timecode.
  The media player will try to play the corresponding frame, base on the frame's timecode value.

<a id="unreal.TimeSynchronizableMediaSource.use_time_synchronization"></a>

#### use_time_synchronization

```python
@property
def use_time_synchronization() -> bool
```

(bool):  [Read-Write] Synchronize the media with the engine's timecode.
The media player has be able to read timecode.
The media player will try to play the corresponding frame, base on the frame's timecode value.

<a id="unreal.TimeSynchronizableMediaSource.use_time_synchronization"></a>

#### use_time_synchronization

```python
@use_time_synchronization.setter
def use_time_synchronization(value: bool) -> None
```

<a id="unreal.MediaLibrary"></a>