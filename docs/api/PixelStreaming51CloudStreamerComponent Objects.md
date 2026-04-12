## PixelStreaming51CloudStreamerComponent Objects

```python
class PixelStreaming51CloudStreamerComponent(ActorComponent)
```

Pixel Streaming 51Cloud Streamer Component

**C++ Source:**

- **Plugin**: PixelStreaming51Cloud
- **Module**: PixelStreaming51CloudBlueprint
- **File**: PixelStreaming51CloudStreamerComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``couple_framerate`` (bool):  [Read-Write]
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``signalling_server_url`` (str):  [Read-Write]
- ``stream_fps`` (int32):  [Read-Write]
- ``streamer_id`` (str):  [Read-Write]
- ``streamer_input`` (PixelStreaming51CloudStreamerInput):  [Read-Write]

<a id="unreal.PixelStreaming51CloudStreamerComponent.unfreeze_stream"></a>

#### unfreeze\_stream

```python
def unfreeze_stream() -> None
```

x.unfreeze_stream() -> None
Unfreeze Stream

<a id="unreal.PixelStreaming51CloudStreamerComponent.stop_streaming"></a>

#### stop\_streaming

```python
def stop_streaming() -> None
```

x.stop_streaming() -> None
Stop Streaming

<a id="unreal.PixelStreaming51CloudStreamerComponent.start_streaming"></a>

#### start\_streaming

```python
def start_streaming() -> None
```

x.start_streaming() -> None
Start Streaming

<a id="unreal.PixelStreaming51CloudStreamerComponent.send_player_message"></a>

#### send\_player\_message

```python
def send_player_message(type: int, descriptor: str) -> None
```

x.send_player_message(type, descriptor) -> None
Send Player Message

Args:
    type (uint8): 
    descriptor (str):

<a id="unreal.PixelStreaming51CloudStreamerComponent.is_streaming"></a>

#### is\_streaming

```python
def is_streaming() -> bool
```

x.is_streaming() -> bool
Is Streaming

Returns:
    bool:

<a id="unreal.PixelStreaming51CloudStreamerComponent.is_signalling_connected"></a>

#### is\_signalling\_connected

```python
def is_signalling_connected() -> bool
```

x.is_signalling_connected() -> bool
Is Signalling Connected

Returns:
    bool:

<a id="unreal.PixelStreaming51CloudStreamerComponent.get_id"></a>

#### get\_id

```python
def get_id() -> str
```

x.get_id() -> str
Get Id

Returns:
    str:

<a id="unreal.PixelStreaming51CloudStreamerComponent.freeze_stream"></a>

#### freeze\_stream

```python
def freeze_stream(texture: Texture2D) -> None
```

x.freeze_stream(texture) -> None
Freeze Stream

Args:
    texture (Texture2D):

<a id="unreal.PixelStreaming51CloudStreamerComponent.force_key_frame"></a>

#### force\_key\_frame

```python
def force_key_frame() -> None
```

x.force_key_frame() -> None
Force Key Frame

<a id="unreal.EnvironmentQueryFactory"></a>