## MediaPlayer Objects

```python
class MediaPlayer(Object)
```

Implements a media player asset that can play movies and other media sources.

**C++ Source:**

- **Module**: MediaAssets
- **File**: MediaPlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affected_by_pie_handling`` (bool):  [Read-Write] Whether this player should stop when entering or exiting PIE.
- ``cache_ahead`` (Timespan):  [Read-Write] Duration of samples to cache ahead of the play head.
  see: CacheBehind, CacheBehindGame
- ``cache_behind`` (Timespan):  [Read-Write] Duration of samples to cache behind the play head (when not running as game).
  see: CacheAhead, CacheBehindGame
- ``cache_behind_game`` (Timespan):  [Read-Write] Duration of samples to cache behind the play head (when running as game).
  see: CacheAhead, CacheBehind
- ``horizontal_field_of_view`` (float):  [Read-Write] The initial horizontal field of view (in Euler degrees; default = 90).

  This setting is used only for 360 videos. It determines the portion of the
  video that is visible at a time. To modify the field of view at runtime in
  Blueprints, use the SetHorizontalFieldOfView function.
  see: GetHorizontalFieldOfView, SetHorizontalFieldOfView, VerticalFieldOfView, ViewRotation
- ``loop`` (bool):  [Read-Write] Whether the player should loop when media playback reaches the end.

  Use the SetLooping function to change this value at runtime.
  see: IsLooping, SetLooping
- ``native_audio_out`` (bool):  [Read-Write] Output any audio via the operating system's sound mixer instead of a Sound Wave asset.

  If enabled, the assigned Sound Wave asset will be ignored. The SetNativeVolume
  function can then be used to change the audio output volume at runtime. Note that
  not all media player plug-ins may support native audio output on all platforms.
  see: SetNativeVolume
- ``on_end_reached`` (OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when playback has reached the end of the media.
- ``on_media_closed`` (OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when a media source has been closed.
- ``on_media_open_failed`` (OnMediaPlayerMediaOpenFailed):  [Read-Write] A delegate that is invoked when a media source has failed to open.

  This delegate is only executed if OpenSource / OpenUrl returned true and
  the media failed to open asynchronously later. It is not executed if
  OpenSource / OpenUrl returned false, indicating an immediate failure.
  see: OnMediaOpened
- ``on_media_opened`` (OnMediaPlayerMediaOpened):  [Read-Write] A delegate that is invoked when a media source has been opened.

  Depending on whether the underlying player implementation opens the media
  synchronously or asynchronously, this event may be executed before or
  after the call to OpenSource / OpenUrl returns.
  see: OnMediaOpenFailed, OnTracksChanged
- ``on_metadata_changed`` (OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when the media metadata changed.
  see: OnMediaOpened
- ``on_playback_resumed`` (OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when media playback has been resumed.
  see: OnPlaybackSuspended
- ``on_playback_suspended`` (OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when media playback has been suspended.
  see: OnPlaybackResumed
- ``on_seek_completed`` (OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when a seek operation completed successfully.

  Depending on whether the underlying player implementation performs seeks
  synchronously or asynchronously, this event may be executed before or
  after the call to Seek returns.
- ``on_tracks_changed`` (OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when the media track collection changed.
  see: OnMediaOpened
- ``play_on_open`` (bool):  [Read-Write] Automatically start playback after media opened successfully.

  If disabled, listen to the OnMediaOpened Blueprint event to detect when
  the media finished opening, and then start playback using the Play function.
  see: OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Play
- ``playlist`` (MediaPlaylist):  [Read-Write] The play list to use, if any.

  Use the OpenPlaylist or OpenPlaylistIndex function to change this value at runtime.
  see: OpenPlaylist, OpenPlaylistIndex
- ``playlist_index`` (int32):  [Read-Write] The current index of the source in the play list being played.

  Use the Previous and Next methods to change this value at runtime.
  see: Next, Previous
- ``shuffle`` (bool):  [Read-Write] Whether playback should shuffle media sources in the play list.
  see: OpenPlaylist, OpenPlaylistIndex
- ``time_delay`` (Timespan):  [Read-Write] Delay of the player's time.
  see: SetTimeDelay, GetTimeDelay
- ``vertical_field_of_view`` (float):  [Read-Write] The initial vertical field of view (in Euler degrees; default = 60).

  This setting is used only for 360 videos. It determines the portion of the
  video that is visible at a time. To modify the field of view at runtime in
  Blueprints, use the SetHorizontalFieldOfView function.

  Please note that some 360 video players may be able to change only the
  horizontal field of view, and this setting may be ignored.
  see: GetVerticalFieldOfView, SetVerticalFieldOfView, HorizontalFieldOfView, ViewRotation
- ``view_rotation`` (Rotator):  [Read-Write] The initial view rotation.

  This setting is used only for 360 videos. It determines the rotation of
  the video's view. To modify the view orientation at runtime in Blueprints,
  use the GetViewRotation and SetViewRotation functions.

  Please note that not all players may support video view rotations.
  see: GetViewRotation, SetViewRotation, HorizontalFieldOfView, VerticalFieldOfView

<a id="unreal.MediaPlayer.on_end_reached"></a>

#### on_end_reached

```python
@property
def on_end_reached() -> OnMediaPlayerMediaEvent
```

(OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when playback has reached the end of the media.

<a id="unreal.MediaPlayer.on_end_reached"></a>

#### on_end_reached

```python
@on_end_reached.setter
def on_end_reached(value: OnMediaPlayerMediaEvent) -> None
```

<a id="unreal.MediaPlayer.on_media_closed"></a>

#### on_media_closed

```python
@property
def on_media_closed() -> OnMediaPlayerMediaEvent
```

(OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when a media source has been closed.

<a id="unreal.MediaPlayer.on_media_closed"></a>

#### on_media_closed

```python
@on_media_closed.setter
def on_media_closed(value: OnMediaPlayerMediaEvent) -> None
```

<a id="unreal.MediaPlayer.on_media_opened"></a>

#### on_media_opened

```python
@property
def on_media_opened() -> OnMediaPlayerMediaOpened
```

(OnMediaPlayerMediaOpened):  [Read-Write] A delegate that is invoked when a media source has been opened.

Depending on whether the underlying player implementation opens the media
synchronously or asynchronously, this event may be executed before or
after the call to OpenSource / OpenUrl returns.
see: OnMediaOpenFailed, OnTracksChanged

<a id="unreal.MediaPlayer.on_media_opened"></a>

#### on_media_opened

```python
@on_media_opened.setter
def on_media_opened(value: OnMediaPlayerMediaOpened) -> None
```

<a id="unreal.MediaPlayer.on_media_open_failed"></a>

#### on_media_open_failed

```python
@property
def on_media_open_failed() -> OnMediaPlayerMediaOpenFailed
```

(OnMediaPlayerMediaOpenFailed):  [Read-Write] A delegate that is invoked when a media source has failed to open.

This delegate is only executed if OpenSource / OpenUrl returned true and
the media failed to open asynchronously later. It is not executed if
OpenSource / OpenUrl returned false, indicating an immediate failure.
see: OnMediaOpened

<a id="unreal.MediaPlayer.on_media_open_failed"></a>

#### on_media_open_failed

```python
@on_media_open_failed.setter
def on_media_open_failed(value: OnMediaPlayerMediaOpenFailed) -> None
```

<a id="unreal.MediaPlayer.on_playback_resumed"></a>

#### on_playback_resumed

```python
@property
def on_playback_resumed() -> OnMediaPlayerMediaEvent
```

(OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when media playback has been resumed.
see: OnPlaybackSuspended

<a id="unreal.MediaPlayer.on_playback_resumed"></a>

#### on_playback_resumed

```python
@on_playback_resumed.setter
def on_playback_resumed(value: OnMediaPlayerMediaEvent) -> None
```

<a id="unreal.MediaPlayer.on_playback_suspended"></a>

#### on_playback_suspended

```python
@property
def on_playback_suspended() -> OnMediaPlayerMediaEvent
```

(OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when media playback has been suspended.
see: OnPlaybackResumed

<a id="unreal.MediaPlayer.on_playback_suspended"></a>

#### on_playback_suspended

```python
@on_playback_suspended.setter
def on_playback_suspended(value: OnMediaPlayerMediaEvent) -> None
```

<a id="unreal.MediaPlayer.on_seek_completed"></a>

#### on_seek_completed

```python
@property
def on_seek_completed() -> OnMediaPlayerMediaEvent
```

(OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when a seek operation completed successfully.

Depending on whether the underlying player implementation performs seeks
synchronously or asynchronously, this event may be executed before or
after the call to Seek returns.

<a id="unreal.MediaPlayer.on_seek_completed"></a>

#### on_seek_completed

```python
@on_seek_completed.setter
def on_seek_completed(value: OnMediaPlayerMediaEvent) -> None
```

<a id="unreal.MediaPlayer.on_tracks_changed"></a>

#### on_tracks_changed

```python
@property
def on_tracks_changed() -> OnMediaPlayerMediaEvent
```

(OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when the media track collection changed.
see: OnMediaOpened

<a id="unreal.MediaPlayer.on_tracks_changed"></a>

#### on_tracks_changed

```python
@on_tracks_changed.setter
def on_tracks_changed(value: OnMediaPlayerMediaEvent) -> None
```

<a id="unreal.MediaPlayer.on_metadata_changed"></a>

#### on_metadata_changed

```python
@property
def on_metadata_changed() -> OnMediaPlayerMediaEvent
```

(OnMediaPlayerMediaEvent):  [Read-Write] A delegate that is invoked when the media metadata changed.
see: OnMediaOpened

<a id="unreal.MediaPlayer.on_metadata_changed"></a>

#### on_metadata_changed

```python
@on_metadata_changed.setter
def on_metadata_changed(value: OnMediaPlayerMediaEvent) -> None
```

<a id="unreal.MediaPlayer.cache_ahead"></a>

#### cache_ahead

```python
@property
def cache_ahead() -> Timespan
```

(Timespan):  [Read-Write] Duration of samples to cache ahead of the play head.
see: CacheBehind, CacheBehindGame

<a id="unreal.MediaPlayer.cache_ahead"></a>

#### cache_ahead

```python
@cache_ahead.setter
def cache_ahead(value: Timespan) -> None
```

<a id="unreal.MediaPlayer.cache_behind"></a>

#### cache_behind

```python
@property
def cache_behind() -> Timespan
```

(Timespan):  [Read-Write] Duration of samples to cache behind the play head (when not running as game).
see: CacheAhead, CacheBehindGame

<a id="unreal.MediaPlayer.cache_behind"></a>

#### cache_behind

```python
@cache_behind.setter
def cache_behind(value: Timespan) -> None
```

<a id="unreal.MediaPlayer.cache_behind_game"></a>

#### cache_behind_game

```python
@property
def cache_behind_game() -> Timespan
```

(Timespan):  [Read-Write] Duration of samples to cache behind the play head (when running as game).
see: CacheAhead, CacheBehind

<a id="unreal.MediaPlayer.cache_behind_game"></a>

#### cache_behind_game

```python
@cache_behind_game.setter
def cache_behind_game(value: Timespan) -> None
```

<a id="unreal.MediaPlayer.native_audio_out"></a>

#### native_audio_out

```python
@property
def native_audio_out() -> bool
```

(bool):  [Read-Write] Output any audio via the operating system's sound mixer instead of a Sound Wave asset.

If enabled, the assigned Sound Wave asset will be ignored. The SetNativeVolume
function can then be used to change the audio output volume at runtime. Note that
not all media player plug-ins may support native audio output on all platforms.
see: SetNativeVolume

<a id="unreal.MediaPlayer.native_audio_out"></a>

#### native_audio_out

```python
@native_audio_out.setter
def native_audio_out(value: bool) -> None
```

<a id="unreal.MediaPlayer.play_on_open"></a>

#### play_on_open

```python
@property
def play_on_open() -> bool
```

(bool):  [Read-Write] Automatically start playback after media opened successfully.

If disabled, listen to the OnMediaOpened Blueprint event to detect when
the media finished opening, and then start playback using the Play function.
see: OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Play

<a id="unreal.MediaPlayer.play_on_open"></a>

#### play_on_open

```python
@play_on_open.setter
def play_on_open(value: bool) -> None
```

<a id="unreal.MediaPlayer.shuffle"></a>

#### shuffle

```python
@property
def shuffle() -> bool
```

(bool):  [Read-Write] Whether playback should shuffle media sources in the play list.
see: OpenPlaylist, OpenPlaylistIndex

<a id="unreal.MediaPlayer.shuffle"></a>

#### shuffle

```python
@shuffle.setter
def shuffle(value: bool) -> None
```

<a id="unreal.MediaPlayer.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Only] Whether the player should loop when media playback reaches the end.

Use the SetLooping function to change this value at runtime.
see: IsLooping, SetLooping

<a id="unreal.MediaPlayer.playlist"></a>

#### playlist

```python
@property
def playlist() -> MediaPlaylist
```

(MediaPlaylist):  [Read-Only] The play list to use, if any.

Use the OpenPlaylist or OpenPlaylistIndex function to change this value at runtime.
see: OpenPlaylist, OpenPlaylistIndex

<a id="unreal.MediaPlayer.playlist_index"></a>

#### playlist_index

```python
@property
def playlist_index() -> int
```

(int32):  [Read-Only] The current index of the source in the play list being played.

Use the Previous and Next methods to change this value at runtime.
see: Next, Previous

<a id="unreal.MediaPlayer.time_delay"></a>

#### time_delay

```python
@property
def time_delay() -> Timespan
```

(Timespan):  [Read-Only] Delay of the player's time.
see: SetTimeDelay, GetTimeDelay

<a id="unreal.MediaPlayer.affected_by_pie_handling"></a>

#### affected_by_pie_handling

```python
@property
def affected_by_pie_handling() -> bool
```

(bool):  [Read-Write] Whether this player should stop when entering or exiting PIE.

<a id="unreal.MediaPlayer.affected_by_pie_handling"></a>

#### affected_by_pie_handling

```python
@affected_by_pie_handling.setter
def affected_by_pie_handling(value: bool) -> None
```

<a id="unreal.MediaPlayer.supports_seeking"></a>

#### supports_seeking

```python
def supports_seeking() -> bool
```

x.supports_seeking() -> bool
Check whether the currently loaded media can jump to a certain position.
see: SupportsRate, SupportsScrubbing

Returns:
    bool: true if seeking is supported, false otherwise.

<a id="unreal.MediaPlayer.supports_scrubbing"></a>

#### supports_scrubbing

```python
def supports_scrubbing() -> bool
```

x.supports_scrubbing() -> bool
Check whether the currently loaded media supports scrubbing.
see: SupportsRate, SupportsSeeking

Returns:
    bool: true if scrubbing is supported, false otherwise.

<a id="unreal.MediaPlayer.supports_rate"></a>

#### supports_rate

```python
def supports_rate(rate: float, unthinned: bool) -> bool
```

x.supports_rate(rate, unthinned) -> bool
Check whether the specified playback rate is supported.
see: SupportsScrubbing, SupportsSeeking

Args:
    rate (float): The playback rate to check.
    unthinned (bool): Whether no frames should be dropped at the given rate.

Returns:
    bool:

<a id="unreal.MediaPlayer.supports_playback_time_range"></a>

#### supports_playback_time_range

```python
def supports_playback_time_range() -> bool
```

x.supports_playback_time_range() -> bool
Check whether the player supports playing back of range within the media.
see: GetPlaybackTimeRange, SetPlaybackTimeRange

Returns:
    bool: true if playing back a range is supported, false otherwise.

<a id="unreal.MediaPlayer.set_view_rotation"></a>

#### set_view_rotation

```python
def set_view_rotation(rotation: Rotator, absolute: bool) -> bool
```

x.set_view_rotation(rotation, absolute) -> bool
Set the view's rotation (only for 360 videos).
see: GetViewRotation, SetViewField

Args:
    rotation (Rotator): The desired view rotation.
    absolute (bool): 

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.set_view_field"></a>

#### set_view_field

```python
def set_view_field(horizontal: float, vertical: float, absolute: bool) -> bool
```

x.set_view_field(horizontal, vertical, absolute) -> bool
Set the field of view (only for 360 videos).
see: GetHorizontalFieldOfView, GetVerticalFieldOfView, SetViewRotation

Args:
    horizontal (float): Horizontal field of view (in Euler degrees).
    vertical (float): Vertical field of view (in Euler degrees).
    absolute (bool): 

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.set_video_track_frame_rate"></a>

#### set_video_track_frame_rate

```python
def set_video_track_frame_rate(track_index: int, format_index: int,
                               frame_rate: float) -> bool
```

x.set_video_track_frame_rate(track_index, format_index, frame_rate) -> bool
Set the frame rate of the specified video track.
see: GetVideoTrackAspectRatio, GetVideoTrackDimensions, GetVideoTrackFrameRate, GetVideoTrackFrameRates, GetVideoTrackType

Args:
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.
    frame_rate (float): The frame rate to set (must be in range of format's supported frame rates).

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.set_track_format"></a>

#### set_track_format

```python
def set_track_format(track_type: MediaPlayerTrack, track_index: int,
                     format_index: int) -> bool
```

x.set_track_format(track_type, track_index, format_index) -> bool
Set the format on the specified track.

Selecting the format will not switch to the specified track. To switch
tracks, use SelectTrack instead. If the track is already selected, the
format change will be applied immediately.
see: GetNumTrackFormats, GetNumTracks, GetTrackFormat, SelectTrack

Args:
    track_type (MediaPlayerTrack): The type of track to update.
    track_index (int32): The index of the track to update.
    format_index (int32): The index of the format to select (must be valid).

Returns:
    bool: true if the track was selected, false otherwise.

<a id="unreal.MediaPlayer.set_time_delay"></a>

#### set_time_delay

```python
def set_time_delay(time_delay: Timespan) -> None
```

x.set_time_delay(time_delay) -> None
Delay of the player's time.

This setting can be used to manually sync multiple sources.
Set to 1 seconds, if you would like that Player to play 1 second behind its current time.
If the value is too big, it is possible that the player would not hold that frame for that long.
see: GetTimeDelay

Args:
    time_delay (Timespan):

<a id="unreal.MediaPlayer.set_rate"></a>

#### set_rate

```python
def set_rate(rate: float) -> bool
```

x.set_rate(rate) -> bool
Changes the media's playback rate.
see: GetRate, SupportsRate

Args:
    rate (float): The playback rate to set.

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.set_playback_time_range"></a>

#### set_playback_time_range

```python
def set_playback_time_range(time_range: FloatInterval) -> bool
```

x.set_playback_time_range(time_range) -> bool
Blueprint accessible version of SetPlaybackTimeRange().
The range is set through a blueprint usable float interval which may not have enough
precision to represent the range accurately.

Args:
    time_range (FloatInterval): 

Returns:
    bool:

<a id="unreal.MediaPlayer.set_native_volume"></a>

#### set_native_volume

```python
def set_native_volume(volume: float) -> bool
```

x.set_native_volume(volume) -> bool
Set the volume on the native player if not mixing with Sound Wave asset.

The SetNativeVolume can be used to change the audio output volume at runtime. Note that
not all media player plug-ins may support native audio output on all platforms.
see: NativeAudioOut

Args:
    volume (float): The volume to set.

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.set_media_options"></a>

#### set_media_options

```python
def set_media_options(options: MediaSource) -> None
```

x.set_media_options(options) -> None
Sets the media options used by the player.

Args:
    options (MediaSource): Options to pass to the player.

<a id="unreal.MediaPlayer.set_looping"></a>

#### set_looping

```python
def set_looping(looping: bool) -> bool
```

x.set_looping(looping) -> bool
Enables or disables playback looping.
see: IsLooping

Args:
    looping (bool): Whether playback should be looped.

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.set_desired_player_name"></a>

#### set_desired_player_name

```python
def set_desired_player_name(player_name: Name) -> None
```

x.set_desired_player_name(player_name) -> None
Set the name of the desired native player.
see: GetDesiredPlayerName

Args:
    player_name (Name): The name of the player to set.

<a id="unreal.MediaPlayer.set_block_on_time"></a>

#### set_block_on_time

```python
def set_block_on_time(time: Timespan) -> None
```

x.set_block_on_time(time) -> None
Set the time on which to block.

If set, this player will block in TickInput or TickFetch until the video sample
for the specified time are actually available.

Args:
    time (Timespan): The time to block on, or FTimespan::MinValue to disable.

<a id="unreal.MediaPlayer.select_track"></a>

#### select_track

```python
def select_track(track_type: MediaPlayerTrack, track_index: int) -> bool
```

x.select_track(track_type, track_index) -> bool
Select the active track of the given type.

The selected track will use its currently active format. Active formats will
be remembered on a per track basis. The first available format is active by
default. To switch the track format, use SetTrackFormat instead.
see: GetNumTracks, GetSelectedTrack, SetTrackFormat

Args:
    track_type (MediaPlayerTrack): The type of track to select.
    track_index (int32): The index of the track to select, or INDEX_NONE to deselect.

Returns:
    bool: true if the track was selected, false otherwise.

<a id="unreal.MediaPlayer.seek"></a>

#### seek

```python
def seek(time: Timespan) -> bool
```

x.seek(time) -> bool
Seeks to the specified playback time.
see: GetTime, Rewind

Args:
    time (Timespan): The playback time to set.

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.rewind"></a>

#### rewind

```python
def rewind() -> bool
```

x.rewind() -> bool
Rewinds the media to the beginning.

This is the same as seeking to zero time.
see: GetTime, Seek

Returns:
    bool: true if rewinding, false otherwise.

<a id="unreal.MediaPlayer.reopen"></a>

#### reopen

```python
def reopen() -> bool
```

x.reopen() -> bool
Reopens the currently opened media or play list.
see: Close, Open, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl

Returns:
    bool: true if the media will be opened, false otherwise.

<a id="unreal.MediaPlayer.previous"></a>

#### previous

```python
def previous() -> bool
```

x.previous() -> bool
Open the previous item in the current play list.

The player will start playing the new media source if it was playing
something previously, otherwise it will only open the media source.
see: Close, Next, OpenUrl, OpenSource, Play, SetPlaylist

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.play_and_seek"></a>

#### play_and_seek

```python
def play_and_seek() -> None
```

x.play_and_seek() -> None
Starts playback from the media opened event, but can be used elsewhere.

<a id="unreal.MediaPlayer.play"></a>

#### play

```python
def play() -> bool
```

x.play() -> bool
Starts media playback.

This is the same as setting the playback rate to 1.0.
see: CanPlay, GetRate, Next, Pause, Previous, SetRate

Returns:
    bool: true if playback is starting, false otherwise.

<a id="unreal.MediaPlayer.pause"></a>

#### pause

```python
def pause() -> bool
```

x.pause() -> bool
Pauses media playback.

This is the same as setting the playback rate to 0.0.
see: CanPause, Close, Next, Play, Previous, Rewind, Seek

Returns:
    bool: true if playback is being paused, false otherwise.

<a id="unreal.MediaPlayer.open_url"></a>

#### open_url

```python
def open_url(url: str) -> bool
```

x.open_url(url) -> bool
Opens the specified media URL.

A return value of true indicates that the player will attempt to open
the media, but it may fail to do so later for other reasons, i.e. if
a connection to the media server timed out. Use the OnMediaOpened and
OnMediaOpenFailed delegates to detect if and when the media is ready!
see: GetUrl, Close, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, Reopen

Args:
    url (str): The URL to open.

Returns:
    bool: true if the URL will be opened, false otherwise.

<a id="unreal.MediaPlayer.open_source_with_options"></a>

#### open_source_with_options

```python
def open_source_with_options(media_source: MediaSource,
                             options: MediaPlayerOptions) -> bool
```

x.open_source_with_options(media_source, options) -> bool
Open the specified media source with supplied options applied.

A return value of true indicates that the player will attempt to open
the media, but it may fail to do so later for other reasons, i.e. if
a connection to the media server timed out. Use the OnMediaOpened and
OnMediaOpenFailed delegates to detect if and when the media is ready!
see: Close, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenUrl, Reopen

Args:
    media_source (MediaSource): The media source to open.
    options (MediaPlayerOptions): The media player options to apply.

Returns:
    bool: true if the source will be opened, false otherwise.

<a id="unreal.MediaPlayer.open_source_latent"></a>

#### open_source_latent

```python
def open_source_latent(world_context_object: Object,
                       latent_info: LatentActionInfo,
                       media_source: MediaSource,
                       options: MediaPlayerOptions) -> bool
```

x.open_source_latent(world_context_object, latent_info, media_source, options) -> bool
Open the specified media source with options using a latent action.

A result of true indicates that the player successfully completed all requested operations.
see: Close, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenUrl, Reopen

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    media_source (MediaSource): The media source to open.
    options (MediaPlayerOptions): The media player options to apply.

Returns:
    bool: 

    success (bool): All requested operations have completed successfully.

<a id="unreal.MediaPlayer.open_source"></a>

#### open_source

```python
def open_source(media_source: MediaSource) -> bool
```

x.open_source(media_source) -> bool
Open the specified media source.

A return value of true indicates that the player will attempt to open
the media, but it may fail to do so later for other reasons, i.e. if
a connection to the media server timed out. Use the OnMediaOpened and
OnMediaOpenFailed delegates to detect if and when the media is ready!
see: Close, OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenUrl, Reopen

Args:
    media_source (MediaSource): The media source to open.

Returns:
    bool: true if the source will be opened, false otherwise.

<a id="unreal.MediaPlayer.open_playlist_index"></a>

#### open_playlist_index

```python
def open_playlist_index(playlist: MediaPlaylist, index: int) -> bool
```

x.open_playlist_index(playlist, index) -> bool
Open a particular media source in the specified play list.
see: Close, OpenFile, OpenPlaylist, OpenSource, OpenUrl, Reopen

Args:
    playlist (MediaPlaylist): The play list to open.
    index (int32): The index of the source to open.

Returns:
    bool: true if the source will be opened, false otherwise.

<a id="unreal.MediaPlayer.open_playlist"></a>

#### open_playlist

```python
def open_playlist(playlist: MediaPlaylist) -> bool
```

x.open_playlist(playlist) -> bool
Open the first media source in the specified play list.
see: Close, OpenFile, OpenPlaylistIndex, OpenSource, OpenUrl, Reopen

Args:
    playlist (MediaPlaylist): The play list to open.

Returns:
    bool: true if the source will be opened, false otherwise.

<a id="unreal.MediaPlayer.open_file"></a>

#### open_file

```python
def open_file(file_path: str) -> bool
```

x.open_file(file_path) -> bool
Opens the specified media file path.

A return value of true indicates that the player will attempt to open
the media, but it may fail to do so later for other reasons, i.e. if
a connection to the media server timed out. Use the OnMediaOpened and
OnMediaOpenFailed delegates to detect if and when the media is ready!
see: GetUrl, Close, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Reopen

Args:
    file_path (str): The file path to open.

Returns:
    bool: true if the file path will be opened, false otherwise.

<a id="unreal.MediaPlayer.next"></a>

#### next

```python
def next() -> bool
```

x.next() -> bool
Open the next item in the current play list.

The player will start playing the new media source if it was playing
something previously, otherwise it will only open the media source.
see: Close, OpenUrl, OpenSource, Play, Previous, SetPlaylist

Returns:
    bool: true on success, false otherwise.

<a id="unreal.MediaPlayer.is_ready"></a>

#### is_ready

```python
def is_ready() -> bool
```

x.is_ready() -> bool
Check whether media is ready for playback.

A player is ready for playback if it has a media source opened that
finished preparing and is not in an error state.
see: HasError, IsBuffering, IsConnecting, IsLooping, IsPaused, IsPlaying, IsPreparing

Returns:
    bool: true if media is ready, false otherwise.

<a id="unreal.MediaPlayer.is_preparing"></a>

#### is_preparing

```python
def is_preparing() -> bool
```

x.is_preparing() -> bool
Check whether the media is currently opening or buffering.
see: CanPlay, IsBuffering, IsConnecting, IsLooping, IsPaused, IsPlaying, IsReady, Play

Returns:
    bool: true if playback is being prepared, false otherwise.

<a id="unreal.MediaPlayer.is_playing"></a>

#### is_playing

```python
def is_playing() -> bool
```

x.is_playing() -> bool
Check whether playback has started.
see: CanPlay, IsBuffering, IsConnecting, IsLooping, IsPaused, IsPlaying, IsPreparing, IsReady, Play

Returns:
    bool: true if playback has started, false otherwise.

<a id="unreal.MediaPlayer.is_paused"></a>

#### is_paused

```python
def is_paused() -> bool
```

x.is_paused() -> bool
Check whether playback is currently paused.
see: CanPause, IsBuffering, IsConnecting, IsLooping, IsPaused, IsPlaying, IsPreparing, IsReady, Pause

Returns:
    bool: true if playback is paused, false otherwise.

<a id="unreal.MediaPlayer.is_looping"></a>

#### is_looping

```python
def is_looping() -> bool
```

x.is_looping() -> bool
Check whether playback is looping.
see: IsBuffering, IsConnecting, IsPaused, IsPlaying, IsPreparing, IsReady, SetLooping

Returns:
    bool: true if looping, false otherwise.

<a id="unreal.MediaPlayer.is_connecting"></a>

#### is_connecting

```python
def is_connecting() -> bool
```

x.is_connecting() -> bool
Check whether the player is currently connecting to a media source.
see: IsBuffering, IsLooping, IsPaused, IsPlaying, IsPreparing, IsReady

Returns:
    bool: true if connecting, false otherwise.

<a id="unreal.MediaPlayer.is_closed"></a>

#### is_closed

```python
def is_closed() -> bool
```

x.is_closed() -> bool
Whether media is currently closed.

Returns:
    bool: true if media is closed, false otherwise.

<a id="unreal.MediaPlayer.is_buffering"></a>

#### is_buffering

```python
def is_buffering() -> bool
```

x.is_buffering() -> bool
Check whether playback is buffering data.
see: IsConnecting, IsLooping, IsPaused, IsPlaying, IsPreparing, IsReady

Returns:
    bool: true if looping, false otherwise.

<a id="unreal.MediaPlayer.has_error"></a>

#### has_error

```python
def has_error() -> bool
```

x.has_error() -> bool
Check whether the player is in an error state.

When the player is in an error state, no further operations are possible.
The current media must be closed, and a new media source must be opened
before the player can be used again. Errors are usually caused by faulty
media files or interrupted network connections.
see: IsReady

Returns:
    bool:

<a id="unreal.MediaPlayer.get_view_rotation"></a>

#### get_view_rotation

```python
def get_view_rotation() -> Rotator
```

x.get_view_rotation() -> Rotator
Get the current view rotation (only for 360 videos).
see: GetHorizontalFieldOfView, GetVerticalFieldOfView, SetViewRotation

Returns:
    Rotator: View rotation, or zero rotator if not available.

<a id="unreal.MediaPlayer.get_video_track_type"></a>

#### get_video_track_type

```python
def get_video_track_type(track_index: int, format_index: int) -> str
```

x.get_video_track_type(track_index, format_index) -> str
Get the type of the specified video track format.
see: GetVideoTrackAspectRatio, GetVideoTrackDimensions, GetVideoTrackFrameRate, GetVideoTrackFrameRates

Args:
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.

Returns:
    str: Video format type string.

<a id="unreal.MediaPlayer.get_video_track_frame_rates"></a>

#### get_video_track_frame_rates

```python
def get_video_track_frame_rates(track_index: int,
                                format_index: int) -> FloatRange
```

x.get_video_track_frame_rates(track_index, format_index) -> FloatRange
Get the supported range of frame rates of the specified video track.
see: GetVideoTrackAspectRatio, GetVideoTrackDimensions, GetVideoTrackFrameRate, GetVideoTrackType

Args:
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.

Returns:
    FloatRange: Frame rate range (in frames per second).

<a id="unreal.MediaPlayer.get_video_track_frame_rate"></a>

#### get_video_track_frame_rate

```python
def get_video_track_frame_rate(track_index: int, format_index: int) -> float
```

x.get_video_track_frame_rate(track_index, format_index) -> float
Get the frame rate of the specified video track.
see: GetVideoTrackAspectRatio, GetVideoTrackDimensions, GetVideoTrackFrameRates, GetVideoTrackType, SetVideoTrackFrameRate

Args:
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.

Returns:
    float: Frame rate (in frames per second).

<a id="unreal.MediaPlayer.get_video_track_dimensions"></a>

#### get_video_track_dimensions

```python
def get_video_track_dimensions(track_index: int,
                               format_index: int) -> IntPoint
```

x.get_video_track_dimensions(track_index, format_index) -> IntPoint
Get the current dimensions of the specified video track.
see: GetVideoTrackAspectRatio, GetVideoTrackFrameRate, GetVideoTrackFrameRates, GetVideoTrackType

Args:
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.

Returns:
    IntPoint: Video dimensions (in pixels).

<a id="unreal.MediaPlayer.get_video_track_aspect_ratio"></a>

#### get_video_track_aspect_ratio

```python
def get_video_track_aspect_ratio(track_index: int, format_index: int) -> float
```

x.get_video_track_aspect_ratio(track_index, format_index) -> float
Get the aspect ratio of the specified video track.
see: GetVideoTrackDimensions, GetVideoTrackFrameRate, GetVideoTrackFrameRates, GetVideoTrackType

Args:
    track_index (int32): Index of the video track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.

Returns:
    float: Aspect ratio.

<a id="unreal.MediaPlayer.get_vertical_field_of_view"></a>

#### get_vertical_field_of_view

```python
def get_vertical_field_of_view() -> float
```

x.get_vertical_field_of_view() -> float
Get the current vertical field of view (only for 360 videos).
see: GetHorizontalFieldOfView, GetViewRotation, SetVerticalFieldOfView

Returns:
    float: Vertical field of view (in Euler degrees), or 0.0 if not available.

<a id="unreal.MediaPlayer.get_url"></a>

#### get_url

```python
def get_url() -> str
```

x.get_url() -> str
Get the URL of the currently loaded media, if any.
see: OpenUrl

Returns:
    str: Media URL, or empty string if no media was loaded.

<a id="unreal.MediaPlayer.get_track_language"></a>

#### get_track_language

```python
def get_track_language(track_type: MediaPlayerTrack, track_index: int) -> str
```

x.get_track_language(track_type, track_index) -> str
Get the language tag of the specified track.
see: GetNumTracks, GetTrackDisplayName

Args:
    track_type (MediaPlayerTrack): The type of track.
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.

Returns:
    str: Language tag, i.e. "en-US" for English, or "und" for undefined.

<a id="unreal.MediaPlayer.get_track_format"></a>

#### get_track_format

```python
def get_track_format(track_type: MediaPlayerTrack, track_index: int) -> int
```

x.get_track_format(track_type, track_index) -> int32
Get the index of the active format of the specified track type.
see: GetNumTrackFormats, GetSelectedTrack, SetTrackFormat

Args:
    track_type (MediaPlayerTrack): The type of track.
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.

Returns:
    int32: The index of the selected format.

<a id="unreal.MediaPlayer.get_track_display_name"></a>

#### get_track_display_name

```python
def get_track_display_name(track_type: MediaPlayerTrack,
                           track_index: int) -> Text
```

x.get_track_display_name(track_type, track_index) -> Text
Get the human readable name of the specified track.
see: GetNumTracks, GetTrackLanguage

Args:
    track_type (MediaPlayerTrack): The type of track.
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.

Returns:
    Text: Display name.

<a id="unreal.MediaPlayer.get_time_stamp"></a>

#### get_time_stamp

```python
def get_time_stamp() -> MediaTimeStampInfo
```

x.get_time_stamp() -> MediaTimeStampInfo
Get the media's current playback timestamp.
see: GetDuration, Seek

Returns:
    MediaTimeStampInfo: Playback timestamp.

<a id="unreal.MediaPlayer.get_time_delay"></a>

#### get_time_delay

```python
def get_time_delay() -> Timespan
```

x.get_time_delay() -> Timespan
Delay of the player's time.
see: SetTimeDelay

Returns:
    Timespan: Delay added to the player's time used to manually sync multiple sources.

<a id="unreal.MediaPlayer.get_time"></a>

#### get_time

```python
def get_time() -> Timespan
```

x.get_time() -> Timespan
Get the media's current playback time.
see: GetDuration, Seek

Returns:
    Timespan: Playback time.

<a id="unreal.MediaPlayer.get_supported_rates"></a>

#### get_supported_rates

```python
def get_supported_rates(unthinned: bool) -> Array[FloatRange]
```

x.get_supported_rates(unthinned) -> Array[FloatRange]
Get the supported playback rates.
see: SetRate, SupportsRate

Args:
    unthinned (bool): Whether the rates are for unthinned playback.

Returns:
    Array[FloatRange]: 

    out_rates (Array[FloatRange]):

<a id="unreal.MediaPlayer.get_selected_track"></a>

#### get_selected_track

```python
def get_selected_track(track_type: MediaPlayerTrack) -> int
```

x.get_selected_track(track_type) -> int32
Get the index of the currently selected track of the given type.
see: GetNumTracks, GetTrackFormat, SelectTrack

Args:
    track_type (MediaPlayerTrack): The type of track to get.

Returns:
    int32: The index of the selected track, or INDEX_NONE if no track is active.

<a id="unreal.MediaPlayer.get_rate"></a>

#### get_rate

```python
def get_rate() -> float
```

x.get_rate() -> float
Get the media's current playback rate.
see: SetRate, SupportsRate

Returns:
    float: The playback rate.

<a id="unreal.MediaPlayer.get_playlist_index"></a>

#### get_playlist_index

```python
def get_playlist_index() -> int
```

x.get_playlist_index() -> int32
Get the current play list index.
see: GetPlaylist

Returns:
    int32: Play list index.

<a id="unreal.MediaPlayer.get_playlist"></a>

#### get_playlist

```python
def get_playlist() -> MediaPlaylist
```

x.get_playlist() -> MediaPlaylist
Get the current play list.

Media players always have a valid play list. In C++ code you can use
the GetPlaylistRef to get a reference instead of a pointer to it.
see: GetPlaylistIndex, GetPlaylistRef

Returns:
    MediaPlaylist: The play list.

<a id="unreal.MediaPlayer.get_player_name"></a>

#### get_player_name

```python
def get_player_name() -> Name
```

x.get_player_name() -> Name
Get the name of the current native media player.
see: GetMediaName

Returns:
    Name: Player name, or NAME_None if not available.

<a id="unreal.MediaPlayer.get_playback_time_range"></a>

#### get_playback_time_range

```python
def get_playback_time_range(
        range_to_get: MediaTimeRangeBPType) -> FloatInterval
```

x.get_playback_time_range(range_to_get) -> FloatInterval
Blueprint accessible version of GetPlaybackTimeRange.
This returns the range truncated into a blueprint usable float interval and should not
be used for live streams as 32 bit floats can not store wallclock times with enough precision.

Args:
    range_to_get (MediaTimeRangeBPType): 

Returns:
    FloatInterval:

<a id="unreal.MediaPlayer.get_num_tracks"></a>

#### get_num_tracks

```python
def get_num_tracks(track_type: MediaPlayerTrack) -> int
```

x.get_num_tracks(track_type) -> int32
Get the number of tracks of the given type.
see: GetNumTrackFormats, GetSelectedTrack, SelectTrack

Args:
    track_type (MediaPlayerTrack): The type of media tracks.

Returns:
    int32: Number of tracks.

<a id="unreal.MediaPlayer.get_num_track_formats"></a>

#### get_num_track_formats

```python
def get_num_track_formats(track_type: MediaPlayerTrack,
                          track_index: int) -> int
```

x.get_num_track_formats(track_type, track_index) -> int32
Get the number of formats of the specified track.
see: GetNumTracks, GetSelectedTrack, SelectTrack

Args:
    track_type (MediaPlayerTrack): The type of media tracks.
    track_index (int32): The index of the track.

Returns:
    int32: Number of formats.

<a id="unreal.MediaPlayer.get_media_name"></a>

#### get_media_name

```python
def get_media_name() -> Text
```

x.get_media_name() -> Text
Get the human readable name of the currently loaded media source.
see: GetPlayerName, GetUrl

Returns:
    Text: Media source name, or empty text if no media is opened

<a id="unreal.MediaPlayer.get_media_metadata_items"></a>

#### get_media_metadata_items

```python
def get_media_metadata_items() -> Map[str, MediaMetadataItemsBPT]
```

x.get_media_metadata_items() -> Map[str, MediaMetadataItemsBPT]
This is the blueprint accessible version of the GetMediaMetadata.
note: Listen to EMediaEvent::MetadataChanged to catch updates to this data

Returns:
    Map[str, MediaMetadataItemsBPT]: Map with arrays of FMediaMetaDataItem entries describing any metadata found in the current stream

<a id="unreal.MediaPlayer.get_horizontal_field_of_view"></a>

#### get_horizontal_field_of_view

```python
def get_horizontal_field_of_view() -> float
```

x.get_horizontal_field_of_view() -> float
Get the current horizontal field of view (only for 360 videos).
see: GetVerticalFieldOfView, GetViewRotation, SetHorizontalFieldOfView

Returns:
    float: Horizontal field of view (in Euler degrees).

<a id="unreal.MediaPlayer.get_duration"></a>

#### get_duration

```python
def get_duration() -> Timespan
```

x.get_duration() -> Timespan
Get the media's duration.
see: GetTime, Seek

Returns:
    Timespan: A time span representing the duration.

<a id="unreal.MediaPlayer.get_display_time_stamp"></a>

#### get_display_time_stamp

```python
def get_display_time_stamp() -> MediaTimeStampInfo
```

x.get_display_time_stamp() -> MediaTimeStampInfo
Get the media's current playback timestamp as appropriate for display.
see: GetDuration, Seek

Returns:
    MediaTimeStampInfo: Playback timestamp.

<a id="unreal.MediaPlayer.get_display_time"></a>

#### get_display_time

```python
def get_display_time() -> Timespan
```

x.get_display_time() -> Timespan
Get the media's current playback time as appropriate for display.
see: GetDuration, Seek

Returns:
    Timespan: Playback time.

<a id="unreal.MediaPlayer.get_desired_player_name"></a>

#### get_desired_player_name

```python
def get_desired_player_name() -> Name
```

x.get_desired_player_name() -> Name
Get the name of the current desired native player.
see: SetDesiredPlayerName

Returns:
    Name: The name of the desired player, or NAME_None if not set.

<a id="unreal.MediaPlayer.get_audio_track_type"></a>

#### get_audio_track_type

```python
def get_audio_track_type(track_index: int, format_index: int) -> str
```

x.get_audio_track_type(track_index, format_index) -> str
Get the type of the specified audio track format.
see: GetAudioTrackSampleRate, GetAudioTrackSampleRate

Args:
    track_index (int32): The index of the track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.

Returns:
    str: Audio format type string.

<a id="unreal.MediaPlayer.get_audio_track_sample_rate"></a>

#### get_audio_track_sample_rate

```python
def get_audio_track_sample_rate(track_index: int, format_index: int) -> int
```

x.get_audio_track_sample_rate(track_index, format_index) -> int32
Get the sample rate of the specified audio track.
see: GetAudioTrackChannels, GetAudioTrackType

Args:
    track_index (int32): Index of the audio track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.

Returns:
    int32: Samples per second.

<a id="unreal.MediaPlayer.get_audio_track_channels"></a>

#### get_audio_track_channels

```python
def get_audio_track_channels(track_index: int, format_index: int) -> int
```

x.get_audio_track_channels(track_index, format_index) -> int32
Get the number of channels in the specified audio track.
see: GetAudioTrackSampleRate, GetAudioTrackType

Args:
    track_index (int32): Index of the audio track, or INDEX_NONE for the selected one.
    format_index (int32): Index of the track format, or INDEX_NONE for the selected one.

Returns:
    int32: Number of channels.

<a id="unreal.MediaPlayer.close"></a>

#### close

```python
def close() -> None
```

x.close() -> None
Close the currently open media, if any.
see: OnMediaClosed, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Pause, Play

<a id="unreal.MediaPlayer.can_play_url"></a>

#### can_play_url

```python
def can_play_url(url: str) -> bool
```

x.can_play_url(url) -> bool
Check whether the specified URL can be played by this player.

If a desired player name is set for this player, it will only check
whether that particular player type can play the specified URL.
see: CanPlaySource, SetDesiredPlayerName

Args:
    url (str): The URL to check.

Returns:
    bool:

<a id="unreal.MediaPlayer.can_play_source"></a>

#### can_play_source

```python
def can_play_source(media_source: MediaSource) -> bool
```

x.can_play_source(media_source) -> bool
Check whether the specified media source can be played by this player.

If a desired player name is set for this player, it will only check
whether that particular player type can play the specified source.
see: CanPlayUrl, SetDesiredPlayerName

Args:
    media_source (MediaSource): The media source to check.

Returns:
    bool: true if the media source can be opened, false otherwise.

<a id="unreal.MediaPlayer.can_pause"></a>

#### can_pause

```python
def can_pause() -> bool
```

x.can_pause() -> bool
Check whether media playback can be paused right now.

Playback can be paused if the media supports pausing and if it is currently playing.
see: CanPlay, Pause

Returns:
    bool: true if pausing playback can be paused, false otherwise.

<a id="unreal.MediaPlaylist"></a>