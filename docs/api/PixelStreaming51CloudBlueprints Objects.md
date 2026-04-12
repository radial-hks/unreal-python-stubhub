## PixelStreaming51CloudBlueprints Objects

```python
class PixelStreaming51CloudBlueprints(BlueprintFunctionLibrary)
```

Pixel Streaming 51Cloud Blueprints

**C++ Source:**

- **Plugin**: PixelStreaming51Cloud
- **Module**: PixelStreaming51Cloud
- **File**: PixelStreaming51CloudBlueprints.h

<a id="unreal.PixelStreaming51CloudBlueprints.unfreeze_frame"></a>

#### unfreeze\_frame

```python
@classmethod
def unfreeze_frame(cls) -> None
```

X.unfreeze_frame() -> None
Unfreeze Pixel Streaming for 51Cloud.

<a id="unreal.PixelStreaming51CloudBlueprints.streamer_unfreeze_stream"></a>

#### streamer\_unfreeze\_stream

```python
@classmethod
def streamer_unfreeze_stream(cls, streamer_id: str) -> None
```

X.streamer_unfreeze_stream(streamer_id) -> None
Unfreeze Pixel Streaming for 51Cloud.

Args:
    streamer_id (str): The id of the streamer to unfreeze.

<a id="unreal.PixelStreaming51CloudBlueprints.streamer_send_file_as_byte_array"></a>

#### streamer\_send\_file\_as\_byte\_array

```python
@classmethod
def streamer_send_file_as_byte_array(cls, streamer_id: str,
                                     byte_array: Array[int], mime_type: str,
                                     file_extension: str) -> None
```

X.streamer_send_file_as_byte_array(streamer_id, byte_array, mime_type, file_extension) -> None
Send a specified byte array over the WebRTC peer connection data channel. The extension and mime type are used for file reconstruction on the front end

Args:
    streamer_id (str): The streamer use when sending the data
    byte_array (Array[uint8]): The raw data that will be sent over the data channel
    mime_type (str): The mime type of the file. Used for reconstruction on the front end
    file_extension (str): The file extension. Used for file reconstruction on the front end

<a id="unreal.PixelStreaming51CloudBlueprints.streamer_send_file"></a>

#### streamer\_send\_file

```python
@classmethod
def streamer_send_file(cls, streamer_id: str, filepath: str, mime_type: str,
                       file_extension: str) -> None
```

X.streamer_send_file(streamer_id, filepath, mime_type, file_extension) -> None
Send a specified file over the WebRTC peer connection data channel. The extension and mime type are used for file reconstruction on the front end

Args:
    streamer_id (str): The streamer use when sending the data
    filepath (str): The path to the file that will be sent
    mime_type (str): The mime type of the file. Used for file reconstruction on the front end
    file_extension (str): The file extension. Used for file reconstruction on the front end

<a id="unreal.PixelStreaming51CloudBlueprints.streamer_kick_player"></a>

#### streamer\_kick\_player

```python
@classmethod
def streamer_kick_player(cls, streamer_id: str, player_id: str) -> None
```

X.streamer_kick_player(streamer_id, player_id) -> None
Kick a player.

Args:
    streamer_id (str): The streamer which the player belongs
    player_id (str): The ID of the player to kick.

<a id="unreal.PixelStreaming51CloudBlueprints.streamer_freeze_stream"></a>

#### streamer\_freeze\_stream

```python
@classmethod
def streamer_freeze_stream(cls, streamer_id: str, texture: Texture2D) -> None
```

X.streamer_freeze_stream(streamer_id, texture) -> None
Freeze Pixel Streaming for 51Cloud.

Args:
    streamer_id (str): The id of the streamer to freeze.
    texture (Texture2D): The freeze frame to display. If null then the back buffer is captured.

<a id="unreal.PixelStreaming51CloudBlueprints.send_file_as_byte_array"></a>

#### send\_file\_as\_byte\_array

```python
@classmethod
def send_file_as_byte_array(cls, byte_array: Array[int], mime_type: str,
                            file_extension: str) -> None
```

X.send_file_as_byte_array(byte_array, mime_type, file_extension) -> None
Send a specified byte array over the WebRTC peer connection data channel. The extension and mime type are used for file reconstruction on the front end

Args:
    byte_array (Array[uint8]): The raw data that will be sent over the data channel
    mime_type (str): The mime type of the file. Used for reconstruction on the front end
    file_extension (str): The file extension. Used for file reconstruction on the front end

<a id="unreal.PixelStreaming51CloudBlueprints.send_file"></a>

#### send\_file

```python
@classmethod
def send_file(cls, filepath: str, mime_type: str, file_extension: str) -> None
```

X.send_file(filepath, mime_type, file_extension) -> None
Send a specified file over the WebRTC peer connection data channel. The extension and mime type are used for file reconstruction on the front end

Args:
    filepath (str): The path to the file that will be sent
    mime_type (str): The mime type of the file. Used for file reconstruction on the front end
    file_extension (str): The file extension. Used for file reconstruction on the front end

<a id="unreal.PixelStreaming51CloudBlueprints.kick_player"></a>

#### kick\_player

```python
@classmethod
def kick_player(cls, player_id: str) -> None
```

X.kick_player(player_id) -> None
Kick a player.

Args:
    player_id (str): The ID of the player to kick.

<a id="unreal.PixelStreaming51CloudBlueprints.get_pixel_streaming51_cloud_delegates"></a>

#### get\_pixel\_streaming51\_cloud\_delegates

```python
@classmethod
def get_pixel_streaming51_cloud_delegates(
        cls) -> PixelStreaming51CloudDelegates
```

X.get_pixel_streaming51_cloud_delegates() -> PixelStreaming51CloudDelegates
Get the singleton. This allows application-specific blueprints to bind
to delegates of interest.

Returns:
    PixelStreaming51CloudDelegates:

<a id="unreal.PixelStreaming51CloudBlueprints.get_default_streamer_id"></a>

#### get\_default\_streamer\_id

```python
@classmethod
def get_default_streamer_id(cls) -> str
```

X.get_default_streamer_id() -> str
Get the default Streamer ID

Returns:
    str:

<a id="unreal.PixelStreaming51CloudBlueprints.freeze_frame"></a>

#### freeze\_frame

```python
@classmethod
def freeze_frame(cls, texture: Texture2D) -> None
```

X.freeze_frame(texture) -> None
Freeze Pixel Streaming for 51Cloud.

Args:
    texture (Texture2D): The freeze frame to display. If null then the back buffer is captured.

<a id="unreal.PixelStreaming51CloudBlueprints.force_key_frame"></a>

#### force\_key\_frame

```python
@classmethod
def force_key_frame(cls) -> None
```

X.force_key_frame() -> None
Force a key frame to be sent.

<a id="unreal.PixelStreaming51CloudDelegates"></a>