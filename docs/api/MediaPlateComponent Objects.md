## MediaPlateComponent Objects

```python
class MediaPlateComponent(ActorComponent)
```

This is a component for AMediaPlate that can play and show media in the world.

**C++ Source:**

- **Plugin**: MediaPlate
- **Module**: MediaPlate
- **File**: MediaPlateComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adaptive_pole_mip_upscaling`` (bool):  [Read-Write] If true then Media Plate will attempt to load and upscale lower quality mips and display those at the poles (Sphere object only).
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_play`` (bool):  [Read-Write] If set then start playing when this object is active.
- ``cache_settings`` (MediaSourceCacheSettings):  [Read-Write] Override the default cache settings.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_audio`` (bool):  [Read-Write] If set then enable audio.
- ``enable_mip_map_upscaling`` (bool):  [Read-Write] If true then enable the use of MipLevelToUpscale as defined below.
- ``is_aspect_ratio_auto`` (bool):  [Read-Write] If true then set the aspect ratio automatically based on the media.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``is_media_plate_playing`` (bool):  [Read-Write] If true, then we want the media plate to play.
  Note that this could be true, but the player is not actually playing because
  bPlayOnlyWhenVisible = true and the plate is not visible.
- ``letterboxes`` (Array[StaticMeshComponent]):  [Read-Write] Holds the component for the mesh.
- ``loop`` (bool):  [Read-Write] If set then loop when we reach the end.
- ``media_plate_resource`` (MediaPlateResource):  [Read-Write] Which media source is used to populate the media playlist
- ``media_playlist`` (MediaPlaylist):  [Read-Write]
  deprecated: Use MediaPlateResource instead
- ``media_texture_settings`` (MediaTextureResourceSettings):  [Read-Write] Exposes Media Texture settings via Media Plate component.
- ``mip_level_to_upscale`` (int32):  [Read-Write] With exr playback, upscale into lower quality mips from this specified level. All levels including and above the specified value will be fully read.
- ``mip_map_bias`` (float):  [Read-Write] Media texture mip map bias shared between the (image sequence) loader and the media texture sampler.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``play_on_open`` (bool):  [Read-Write] If set then play when opening the media.
- ``play_only_when_visible`` (bool):  [Read-Write] If true then only allow playback when the media plate is visible.
- ``playlist_index`` (int32):  [Read-Write] The current index of the source in the play list being played.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``sound_component`` (MediaSoundComponent):  [Read-Write] Holds the component to play sound.
- ``start_time`` (float):  [Read-Write] What time to start playing from (in seconds).
- ``static_mesh_component`` (StaticMeshComponent):  [Read-Write] Holds the component for the mesh.
- ``visible_mips_tiles_calculations`` (MediaTextureVisibleMipsTiles):  [Read-Write] Visible mips and tiles calculation mode for the supported mesh types in MediaPlate. (Player restart on change.)

<a id="unreal.MediaPlateComponent.play_on_open"></a>

#### play_on_open

```python
@property
def play_on_open() -> bool
```

(bool):  [Read-Write] If set then play when opening the media.

<a id="unreal.MediaPlateComponent.play_on_open"></a>

#### play_on_open

```python
@play_on_open.setter
def play_on_open(value: bool) -> None
```

<a id="unreal.MediaPlateComponent.start_time"></a>

#### start_time

```python
@property
def start_time() -> float
```

(float):  [Read-Write] What time to start playing from (in seconds).

<a id="unreal.MediaPlateComponent.start_time"></a>

#### start_time

```python
@start_time.setter
def start_time(value: float) -> None
```

<a id="unreal.MediaPlateComponent.media_playlist"></a>

#### media_playlist

```python
@property
def media_playlist() -> MediaPlaylist
```

(MediaPlaylist):  [Read-Write]
deprecated: Use MediaPlateResource instead

<a id="unreal.MediaPlateComponent.media_playlist"></a>

#### media_playlist

```python
@media_playlist.setter
def media_playlist(value: MediaPlaylist) -> None
```

<a id="unreal.MediaPlateComponent.media_plate_resource"></a>

#### media_plate_resource

```python
@property
def media_plate_resource() -> MediaPlateResource
```

(MediaPlateResource):  [Read-Write] Which media source is used to populate the media playlist

<a id="unreal.MediaPlateComponent.media_plate_resource"></a>

#### media_plate_resource

```python
@media_plate_resource.setter
def media_plate_resource(value: MediaPlateResource) -> None
```

<a id="unreal.MediaPlateComponent.playlist_index"></a>

#### playlist_index

```python
@property
def playlist_index() -> int
```

(int32):  [Read-Write] The current index of the source in the play list being played.

<a id="unreal.MediaPlateComponent.playlist_index"></a>

#### playlist_index

```python
@playlist_index.setter
def playlist_index(value: int) -> None
```

<a id="unreal.MediaPlateComponent.is_media_plate_playing"></a>

#### is_media_plate_playing

```python
@property
def is_media_plate_playing() -> bool
```

(bool):  [Read-Only] If true, then we want the media plate to play.
Note that this could be true, but the player is not actually playing because
bPlayOnlyWhenVisible = true and the plate is not visible.

<a id="unreal.MediaPlateComponent.play_only_when_visible"></a>

#### play_only_when_visible

```python
@property
def play_only_when_visible() -> bool
```

(bool):  [Read-Only] If true then only allow playback when the media plate is visible.

<a id="unreal.MediaPlateComponent.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Write] If set then loop when we reach the end.

<a id="unreal.MediaPlateComponent.loop"></a>

#### loop

```python
@loop.setter
def loop(value: bool) -> None
```

<a id="unreal.MediaPlateComponent.is_aspect_ratio_auto"></a>

#### is_aspect_ratio_auto

```python
@property
def is_aspect_ratio_auto() -> bool
```

(bool):  [Read-Write] If true then set the aspect ratio automatically based on the media.

<a id="unreal.MediaPlateComponent.is_aspect_ratio_auto"></a>

#### is_aspect_ratio_auto

```python
@is_aspect_ratio_auto.setter
def is_aspect_ratio_auto(value: bool) -> None
```

<a id="unreal.MediaPlateComponent.set_play_only_when_visible"></a>

#### set_play_only_when_visible

```python
def set_play_only_when_visible(play_only_when_visible: bool) -> None
```

x.set_play_only_when_visible(play_only_when_visible) -> None
Call this to set bPlayOnlyWhenVisible.

Args:
    play_only_when_visible (bool):

<a id="unreal.MediaPlateComponent.set_mesh_range"></a>

#### set_mesh_range

```python
def set_mesh_range(mesh_range: Vector2D) -> None
```

x.set_mesh_range(mesh_range) -> None
Set the arc size in degrees used for visible mips and tiles calculations, specific to the sphere.

Args:
    mesh_range (Vector2D):

<a id="unreal.MediaPlateComponent.set_letterbox_aspect_ratio"></a>

#### set_letterbox_aspect_ratio

```python
def set_letterbox_aspect_ratio(aspect_ratio: float) -> None
```

x.set_letterbox_aspect_ratio(aspect_ratio) -> None
Call this to set the aspect ratio of the screen.

Args:
    aspect_ratio (float):

<a id="unreal.MediaPlateComponent.set_is_aspect_ratio_auto"></a>

#### set_is_aspect_ratio_auto

```python
def set_is_aspect_ratio_auto(is_aspect_ratio_auto: bool) -> None
```

x.set_is_aspect_ratio_auto(is_aspect_ratio_auto) -> None
Sets whether automatic aspect ratio is enabled.

Args:
    is_aspect_ratio_auto (bool):

<a id="unreal.MediaPlateComponent.seek"></a>

#### seek

```python
def seek(time: Timespan) -> bool
```

x.seek(time) -> bool
Call this to seek to the specified playback time.

Args:
    time (Timespan): Time to seek to.

Returns:
    bool: True on success, false otherwise.

<a id="unreal.MediaPlateComponent.rewind"></a>

#### rewind

```python
def rewind() -> bool
```

x.rewind() -> bool
Rewinds the media to the beginning.

This is the same as seeking to zero time.

Returns:
    bool: True if rewinding, false otherwise.

<a id="unreal.MediaPlateComponent.play"></a>

#### play

```python
def play() -> None
```

x.play() -> None
Call this to start playing.
Open must be called before this.

<a id="unreal.MediaPlateComponent.pause"></a>

#### pause

```python
def pause() -> None
```

x.pause() -> None
Call this to pause playback.
Play can be called to resume playback.

<a id="unreal.MediaPlateComponent.open"></a>

#### open

```python
def open() -> None
```

x.open() -> None
Call this to open the media.

<a id="unreal.MediaPlateComponent.get_mesh_range"></a>

#### get_mesh_range

```python
def get_mesh_range() -> Vector2D
```

x.get_mesh_range() -> Vector2D
Return the arc size in degrees used for visible mips and tiles calculations, specific to the sphere.

Returns:
    Vector2D:

<a id="unreal.MediaPlateComponent.get_media_texture"></a>

#### get_media_texture

```python
def get_media_texture(index: int = 0) -> MediaTexture
```

x.get_media_texture(index=0) -> MediaTexture
Call this get our media texture.

Args:
    index (int32): 

Returns:
    MediaTexture:

<a id="unreal.MediaPlateComponent.get_media_player"></a>

#### get_media_player

```python
def get_media_player() -> MediaPlayer
```

x.get_media_player() -> MediaPlayer
Call this get our media player.

Returns:
    MediaPlayer:

<a id="unreal.MediaPlateComponent.get_letterbox_aspect_ratio"></a>

#### get_letterbox_aspect_ratio

```python
def get_letterbox_aspect_ratio() -> float
```

x.get_letterbox_aspect_ratio() -> float
Call this to get the aspect ratio of the screen.

Returns:
    float:

<a id="unreal.MediaPlateComponent.get_is_aspect_ratio_auto"></a>

#### get_is_aspect_ratio_auto

```python
def get_is_aspect_ratio_auto() -> bool
```

x.get_is_aspect_ratio_auto() -> bool
Gets whether automatic aspect ratio is enabled.

Returns:
    bool:

<a id="unreal.MediaPlateComponent.close"></a>

#### close

```python
def close() -> None
```

x.close() -> None
Call this to close the media.

<a id="unreal.AvaEditorSettings"></a>