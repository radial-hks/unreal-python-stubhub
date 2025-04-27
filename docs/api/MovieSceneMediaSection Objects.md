## MovieSceneMediaSection Objects

```python
class MovieSceneMediaSection(MovieSceneSection)
```

Implements a movie scene section for media playback.

**C++ Source:**

- **Plugin**: MediaCompositing
- **Module**: MediaCompositing
- **File**: MovieSceneMediaSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_settings`` (MediaSourceCacheSettings):  [Read-Write] Override the default cache settings. Not used if we have a player proxy as the settings come from the proxy instead.
- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``external_media_player`` (MediaPlayer):  [Read-Write] The external media player this track should control.
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``looping`` (bool):  [Read-Write] Should the media player be set to loop? This can be helpful for media formats that can use this information (such as exr sequences) to pre-cache the starting data when nearing the end of playback. Does not cause the media to continue playing after the end of the section is reached.
- ``media_sound_component`` (MediaSoundComponent):  [Read-Write] The media sound component that receives the track's audio output.
- ``media_source`` (MediaSource):  [Read-Write] The source to play with this video track if MediaSourceProxy is not available.
- ``media_source_proxy_binding_id`` (MovieSceneObjectBindingID):  [Read-Write] The object to get the source to play from if you don't want to directly specify a media source.
- ``media_source_proxy_index`` (int32):  [Read-Write] The index to pass to MediaSourceProxy to get the media source.
- ``media_texture`` (MediaTexture):  [Read-Write] The media texture that receives the track's video output.
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``start_frame_offset`` (FrameNumber):  [Read-Write] Offset into the source media.
- ``texture_index`` (int32):  [Read-Write] If using an object like a MediaPlate, then this determines which texture to use for crossfading purposes.
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)
- ``use_external_media_player`` (bool):  [Read-Write] If true, this track will control a previously created media player instead of automatically creating one.

<a id="unreal.MovieSceneMediaSection.media_source"></a>

#### media_source

```python
@property
def media_source() -> MediaSource
```

(MediaSource):  [Read-Write] The source to play with this video track if MediaSourceProxy is not available.

<a id="unreal.MovieSceneMediaSection.media_source"></a>

#### media_source

```python
@media_source.setter
def media_source(value: MediaSource) -> None
```

<a id="unreal.MovieSceneMediaSection.media_source_proxy_index"></a>

#### media_source_proxy_index

```python
@property
def media_source_proxy_index() -> int
```

(int32):  [Read-Write] The index to pass to MediaSourceProxy to get the media source.

<a id="unreal.MovieSceneMediaSection.media_source_proxy_index"></a>

#### media_source_proxy_index

```python
@media_source_proxy_index.setter
def media_source_proxy_index(value: int) -> None
```

<a id="unreal.MovieSceneMediaSection.looping"></a>

#### looping

```python
@property
def looping() -> bool
```

(bool):  [Read-Write] Should the media player be set to loop? This can be helpful for media formats that can use this information (such as exr sequences) to pre-cache the starting data when nearing the end of playback. Does not cause the media to continue playing after the end of the section is reached.

<a id="unreal.MovieSceneMediaSection.looping"></a>

#### looping

```python
@looping.setter
def looping(value: bool) -> None
```

<a id="unreal.MovieSceneMediaSection.start_frame_offset"></a>

#### start_frame_offset

```python
@property
def start_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] Offset into the source media.

<a id="unreal.MovieSceneMediaSection.start_frame_offset"></a>

#### start_frame_offset

```python
@start_frame_offset.setter
def start_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneMediaSection.media_texture"></a>

#### media_texture

```python
@property
def media_texture() -> MediaTexture
```

(MediaTexture):  [Read-Write] The media texture that receives the track's video output.

<a id="unreal.MovieSceneMediaSection.media_texture"></a>

#### media_texture

```python
@media_texture.setter
def media_texture(value: MediaTexture) -> None
```

<a id="unreal.MovieSceneMediaSection.media_sound_component"></a>

#### media_sound_component

```python
@property
def media_sound_component() -> MediaSoundComponent
```

(MediaSoundComponent):  [Read-Write] The media sound component that receives the track's audio output.

<a id="unreal.MovieSceneMediaSection.media_sound_component"></a>

#### media_sound_component

```python
@media_sound_component.setter
def media_sound_component(value: MediaSoundComponent) -> None
```

<a id="unreal.MovieSceneMediaSection.use_external_media_player"></a>

#### use_external_media_player

```python
@property
def use_external_media_player() -> bool
```

(bool):  [Read-Write] If true, this track will control a previously created media player instead of automatically creating one.

<a id="unreal.MovieSceneMediaSection.use_external_media_player"></a>

#### use_external_media_player

```python
@use_external_media_player.setter
def use_external_media_player(value: bool) -> None
```

<a id="unreal.MovieSceneMediaSection.external_media_player"></a>

#### external_media_player

```python
@property
def external_media_player() -> MediaPlayer
```

(MediaPlayer):  [Read-Write] The external media player this track should control.

<a id="unreal.MovieSceneMediaSection.external_media_player"></a>

#### external_media_player

```python
@external_media_player.setter
def external_media_player(value: MediaPlayer) -> None
```

<a id="unreal.MovieSceneMediaSection.cache_settings"></a>

#### cache_settings

```python
@property
def cache_settings() -> MediaSourceCacheSettings
```

(MediaSourceCacheSettings):  [Read-Write] Override the default cache settings. Not used if we have a player proxy as the settings come from the proxy instead.

<a id="unreal.MovieSceneMediaSection.cache_settings"></a>

#### cache_settings

```python
@cache_settings.setter
def cache_settings(value: MediaSourceCacheSettings) -> None
```

<a id="unreal.MovieSceneMediaSection.texture_index"></a>

#### texture_index

```python
@property
def texture_index() -> int
```

(int32):  [Read-Write] If using an object like a MediaPlate, then this determines which texture to use for crossfading purposes.

<a id="unreal.MovieSceneMediaSection.texture_index"></a>

#### texture_index

```python
@texture_index.setter
def texture_index(value: int) -> None
```

<a id="unreal.MovieSceneMediaTrack"></a>