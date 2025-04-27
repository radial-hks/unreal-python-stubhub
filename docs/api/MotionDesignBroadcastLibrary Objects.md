## MotionDesignBroadcastLibrary Objects

```python
class MotionDesignBroadcastLibrary(BlueprintFunctionLibrary)
```

Ava Broadcast Library

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaBroadcastLibrary.h

<a id="unreal.MotionDesignBroadcastLibrary.get_channel_viewport_size"></a>

#### get_channel_viewport_size

```python
@classmethod
def get_channel_viewport_size(cls, world_context_object: Object) -> Vector2D
```

X.get_channel_viewport_size(world_context_object) -> Vector2D
Returns the current channel's viewport size.

Args:
    world_context_object (Object): 

Returns:
    Vector2D:

<a id="unreal.MotionDesignBroadcastLibrary.get_channel_type"></a>

#### get_channel_type

```python
@classmethod
def get_channel_type(cls, channel_name: Name) -> AvaBroadcastChannelType
```

X.get_channel_type(channel_name) -> AvaBroadcastChannelType
Returns the channel type.

Args:
    channel_name (Name): 

Returns:
    AvaBroadcastChannelType:

<a id="unreal.MotionDesignBroadcastLibrary.get_channel_status"></a>

#### get_channel_status

```python
@classmethod
def get_channel_status(cls, channel_name: Name) -> AvaBroadcastChannelState
```

X.get_channel_status(channel_name) -> AvaBroadcastChannelState
Returns the channel status.

Args:
    channel_name (Name): 

Returns:
    AvaBroadcastChannelState:

<a id="unreal.MotionDesignBroadcastLibrary.get_channel_name"></a>

#### get_channel_name

```python
@classmethod
def get_channel_name(cls, world_context_object: Object) -> Name
```

X.get_channel_name(world_context_object) -> Name
Returns the current channel's name. Will return "None" if not running as part of the broadcast framework.

Args:
    world_context_object (Object): 

Returns:
    Name:

<a id="unreal.AvaBroadcastRenderTargetMediaCapture"></a>