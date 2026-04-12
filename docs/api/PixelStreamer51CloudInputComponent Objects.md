## PixelStreamer51CloudInputComponent Objects

```python
class PixelStreamer51CloudInputComponent(ActorComponent)
```

This component may be attached to an actor to allow UI interactions to be
handled as the delegate will be notified about the interaction and will be
supplied with a generic descriptor string containing, for example, JSON data.
Responses back to the source of the UI interactions may also be sent.

**C++ Source:**

- **Plugin**: PixelStreaming51Cloud
- **Module**: PixelStreaming51Cloud
- **File**: PixelStreaming51CloudInputComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_input_event`` (OnInput):  [Read-Write]
- ``on_large_data_bp`` (OnLargeData_BP):  [Read-Write]
- ``on_large_string_bp`` (OnLargeString_BP):  [Read-Write]
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.PixelStreamer51CloudInputComponent.on_input_event"></a>

#### on\_input\_event

```python
@property
def on_input_event() -> OnInput
```

(OnInput):  [Read-Write]

<a id="unreal.PixelStreamer51CloudInputComponent.on_input_event"></a>

#### on\_input\_event

```python
@on_input_event.setter
def on_input_event(value: OnInput) -> None
```

<a id="unreal.PixelStreamer51CloudInputComponent.on_large_data_bp"></a>

#### on\_large\_data\_bp

```python
@property
def on_large_data_bp() -> OnLargeData_BP
```

(OnLargeData_BP):  [Read-Write]

<a id="unreal.PixelStreamer51CloudInputComponent.on_large_data_bp"></a>

#### on\_large\_data\_bp

```python
@on_large_data_bp.setter
def on_large_data_bp(value: OnLargeData_BP) -> None
```

<a id="unreal.PixelStreamer51CloudInputComponent.on_large_string_bp"></a>

#### on\_large\_string\_bp

```python
@property
def on_large_string_bp() -> OnLargeString_BP
```

(OnLargeString_BP):  [Read-Write]

<a id="unreal.PixelStreamer51CloudInputComponent.on_large_string_bp"></a>

#### on\_large\_string\_bp

```python
@on_large_string_bp.setter
def on_large_string_bp(value: OnLargeString_BP) -> None
```

<a id="unreal.PixelStreamer51CloudInputComponent.send_pixel_streaming_response"></a>

#### send\_pixel\_streaming\_response

```python
def send_pixel_streaming_response(
        descriptor: str,
        rtc_channel_type: RtcChannelType = RtcChannelType.AUTO) -> None
```

x.send_pixel_streaming_response(descriptor, rtc_channel_type=RtcChannelType.AUTO) -> None
Send a response back to the source of the UI interactions (Web).
prame: RtcChannelType - The WebRTC datachannel type.

Args:
    descriptor (str): A generic descriptor string.
    rtc_channel_type (RtcChannelType):

<a id="unreal.PixelStreamer51CloudInputComponent.send_pixel_streaming_notification"></a>

#### send\_pixel\_streaming\_notification

```python
def send_pixel_streaming_notification(type: NotificationType,
                                      msg: str) -> None
```

x.send_pixel_streaming_notification(type, msg) -> None
Send a notification back to the source of the UI interactions (Web).
prame: Msg - The message.

Args:
    type (NotificationType): The notification type.
    msg (str):

<a id="unreal.PixelStreamer51CloudInputComponent.send_pixel_streaming_large_string"></a>

#### send\_pixel\_streaming\_large\_string

```python
def send_pixel_streaming_large_string(large_string: str) -> None
```

x.send_pixel_streaming_large_string(large_string) -> None
Send a largedata as string back to the source of the UI interactions (Web).

Args:
    large_string (str): The large data as string.

<a id="unreal.PixelStreamer51CloudInputComponent.send_pixel_streaming_large_data"></a>

#### send\_pixel\_streaming\_large\_data

```python
def send_pixel_streaming_large_data(large_data: Array[int]) -> None
```

x.send_pixel_streaming_large_data(large_data) -> None
Send a largedata as binary back to the source of the UI interactions (Web).

Args:
    large_data (Array[uint8]): The large data as binary.

<a id="unreal.PixelStreamer51CloudInputComponent.send_message_to_agent"></a>

#### send\_message\_to\_agent

```python
def send_message_to_agent(msg: AgentMessage) -> None
```

x.send_message_to_agent(msg) -> None
Send a message back to the agent, and supported for the WDP5.0 and later.

Args:
    msg (AgentMessage): A message to the agent.

<a id="unreal.PixelStreamer51CloudInputComponent.send_command_to_agent"></a>

#### send\_command\_to\_agent

```python
def send_command_to_agent(descriptor: str) -> None
```

x.send_command_to_agent(descriptor) -> None
Send a command back to the agent.

Args:
    descriptor (str): A generic descriptor string.

<a id="unreal.PixelStreamer51CloudInputComponent.query_min_res_y"></a>

#### query\_min\_res\_y

```python
def query_min_res_y() -> int
```

x.query_min_res_y() -> int32
Get the minimum heigth of resolution.

Returns:
    int32: int32 The minimum heigth.

<a id="unreal.PixelStreamer51CloudInputComponent.query_min_res_x"></a>

#### query\_min\_res\_x

```python
def query_min_res_x() -> int
```

x.query_min_res_x() -> int32
Get the minimum width of resolution.

Returns:
    int32: int32 The minimum width.

<a id="unreal.PixelStreamer51CloudInputComponent.query_min_fps"></a>

#### query\_min\_fps

```python
def query_min_fps() -> float
```

x.query_min_fps() -> float
Get the minimum framerate.

Returns:
    float: float The minimum framerate.

<a id="unreal.PixelStreamer51CloudInputComponent.query_max_res_y"></a>

#### query\_max\_res\_y

```python
def query_max_res_y() -> int
```

x.query_max_res_y() -> int32
Get the maximum heigth of resolution.

Returns:
    int32: int32 The maximum heigth.

<a id="unreal.PixelStreamer51CloudInputComponent.query_max_res_x"></a>

#### query\_max\_res\_x

```python
def query_max_res_x() -> int
```

x.query_max_res_x() -> int32
Get the maximum width of resolution.

Returns:
    int32: int32 The maximum width.

<a id="unreal.PixelStreamer51CloudInputComponent.query_max_fps"></a>

#### query\_max\_fps

```python
def query_max_fps() -> float
```

x.query_max_fps() -> float
Get the maximum framerate.

Returns:
    float: float The maximum framerate.

<a id="unreal.PixelStreamer51CloudInputComponent.get_json_string_value"></a>

#### get\_json\_string\_value

```python
def get_json_string_value(descriptor: str,
                          field_name: str) -> Tuple[str, bool]
```

x.get_json_string_value(descriptor, field_name) -> (string_value=str, success=bool)
Helper function to extract a string field from a JSON descriptor of a
UI interaction given its field name.
The field name may be hierarchical, delimited by a period. For example,
to access the Width value of a Resolution command above you should use
"Resolution.Width" to get the width value.

Args:
    descriptor (str): The UI interaction JSON descriptor.
    field_name (str): The name of the field to look for in the JSON.

Returns:
    tuple: 

    string_value (str): The string value associated with the field name.

    success (bool): True if the field exists in the JSON data.

<a id="unreal.PixelStreamer51CloudInputComponent.add_json_string_value"></a>

#### add\_json\_string\_value

```python
def add_json_string_value(descriptor: str, field_name: str,
                          string_value: str) -> Tuple[str, bool]
```

x.add_json_string_value(descriptor, field_name, string_value) -> (new_descriptor=str, success=bool)
Helper function to add a string field to a JSON descriptor. This produces
a new descriptor which may then be chained to add further string fields.

Args:
    descriptor (str): The initial JSON descriptor which may be blank initially.
    field_name (str): The name of the field to add to the JSON.
    string_value (str): The string value associated with the field name.

Returns:
    tuple: 

    new_descriptor (str): The JSON descriptor with the string field added.

    success (bool): True if the string field could be added successfully.

<a id="unreal.AsyncApiResult"></a>