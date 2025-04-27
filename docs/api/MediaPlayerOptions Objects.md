## MediaPlayerOptions Objects

```python
class MediaPlayerOptions(StructBase)
```

Media Player Options

**C++ Source:**

- **Module**: MediaUtils
- **File**: MediaPlayerOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``loop`` (MediaPlayerOptionBooleanOverride):  [Read-Write] How to initially select looping of the media.
- ``play_on_open`` (MediaPlayerOptionBooleanOverride):  [Read-Write] How to handle automatic playback when media opens.
- ``seek_time`` (Timespan):  [Read-Write] Initial media time to start playback at.
- ``seek_time_type`` (MediaPlayerOptionSeekTimeType):  [Read-Write] How to interpret the initial seek time.
- ``track_selection`` (MediaPlayerOptionTrackSelectMode):  [Read-Write] How the initial media tracks for playback are selected
- ``tracks`` (MediaPlayerTrackOptions):  [Read-Write] Indices of the media tracks to select for playback

<a id="unreal.MediaPlayerOptions.__init__"></a>

#### __init__

```python
def __init__(
    tracks: MediaPlayerTrackOptions = [0, -1, -1, -1, -1, -1, 0],
    track_selection:
    MediaPlayerOptionTrackSelectMode = MediaPlayerOptionTrackSelectMode.
    USE_MEDIA_PLAYER_DEFAULTS,
    seek_time: Timespan = [0, 0, 0, 0, 0],
    seek_time_type:
    MediaPlayerOptionSeekTimeType = MediaPlayerOptionSeekTimeType.IGNORED,
    play_on_open:
    MediaPlayerOptionBooleanOverride = MediaPlayerOptionBooleanOverride.
    USE_MEDIA_PLAYER_SETTING,
    loop: MediaPlayerOptionBooleanOverride = MediaPlayerOptionBooleanOverride.
    USE_MEDIA_PLAYER_SETTING
) -> None
```

<a id="unreal.MediaPlayerOptions.tracks"></a>

#### tracks

```python
@property
def tracks() -> MediaPlayerTrackOptions
```

(MediaPlayerTrackOptions):  [Read-Write] Indices of the media tracks to select for playback

<a id="unreal.MediaPlayerOptions.tracks"></a>

#### tracks

```python
@tracks.setter
def tracks(value: MediaPlayerTrackOptions) -> None
```

<a id="unreal.MediaPlayerOptions.track_selection"></a>

#### track_selection

```python
@property
def track_selection() -> MediaPlayerOptionTrackSelectMode
```

(MediaPlayerOptionTrackSelectMode):  [Read-Write] How the initial media tracks for playback are selected

<a id="unreal.MediaPlayerOptions.track_selection"></a>

#### track_selection

```python
@track_selection.setter
def track_selection(value: MediaPlayerOptionTrackSelectMode) -> None
```

<a id="unreal.MediaPlayerOptions.seek_time"></a>

#### seek_time

```python
@property
def seek_time() -> Timespan
```

(Timespan):  [Read-Write] Initial media time to start playback at.

<a id="unreal.MediaPlayerOptions.seek_time"></a>

#### seek_time

```python
@seek_time.setter
def seek_time(value: Timespan) -> None
```

<a id="unreal.MediaPlayerOptions.seek_time_type"></a>

#### seek_time_type

```python
@property
def seek_time_type() -> MediaPlayerOptionSeekTimeType
```

(MediaPlayerOptionSeekTimeType):  [Read-Write] How to interpret the initial seek time.

<a id="unreal.MediaPlayerOptions.seek_time_type"></a>

#### seek_time_type

```python
@seek_time_type.setter
def seek_time_type(value: MediaPlayerOptionSeekTimeType) -> None
```

<a id="unreal.MediaPlayerOptions.play_on_open"></a>

#### play_on_open

```python
@property
def play_on_open() -> MediaPlayerOptionBooleanOverride
```

(MediaPlayerOptionBooleanOverride):  [Read-Write] How to handle automatic playback when media opens.

<a id="unreal.MediaPlayerOptions.play_on_open"></a>

#### play_on_open

```python
@play_on_open.setter
def play_on_open(value: MediaPlayerOptionBooleanOverride) -> None
```

<a id="unreal.MediaPlayerOptions.loop"></a>

#### loop

```python
@property
def loop() -> MediaPlayerOptionBooleanOverride
```

(MediaPlayerOptionBooleanOverride):  [Read-Write] How to initially select looping of the media.

<a id="unreal.MediaPlayerOptions.loop"></a>

#### loop

```python
@loop.setter
def loop(value: MediaPlayerOptionBooleanOverride) -> None
```

<a id="unreal.SubmixEffectDynamicProcessorFilterSettings"></a>