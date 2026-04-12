## TraceUtilLibrary Objects

```python
class TraceUtilLibrary(BlueprintFunctionLibrary)
```

Trace Util Library

**C++ Source:**

- **Plugin**: TraceUtilities
- **Module**: TraceUtilities
- **File**: TraceUtilLibrary.h

<a id="unreal.TraceUtilLibrary.trace_screenshot"></a>

#### trace\_screenshot

```python
@classmethod
def trace_screenshot(cls, name: str, show_ui: bool) -> None
```

X.trace_screenshot(name, show_ui) -> None
Triggers an Unreal Insights screenshot

Args:
    name (str): 
    show_ui (bool):

<a id="unreal.TraceUtilLibrary.trace_mark_region_start"></a>

#### trace\_mark\_region\_start

```python
@classmethod
def trace_mark_region_start(cls, name: str) -> None
```

X.trace_mark_region_start(name) -> None
Traces a begin event for a region with specified name.

Args:
    name (str):

<a id="unreal.TraceUtilLibrary.trace_mark_region_end"></a>

#### trace\_mark\_region\_end

```python
@classmethod
def trace_mark_region_end(cls, name: str) -> None
```

X.trace_mark_region_end(name) -> None
Traces an end event for a region with specified name.

Args:
    name (str):

<a id="unreal.TraceUtilLibrary.trace_bookmark"></a>

#### trace\_bookmark

```python
@classmethod
def trace_bookmark(cls, name: str) -> None
```

X.trace_bookmark(name) -> None
Traces a bookmark with specified name.

Args:
    name (str):

<a id="unreal.TraceUtilLibrary.toggle_channel"></a>

#### toggle\_channel

```python
@classmethod
def toggle_channel(cls, channel_name: str, enabled: bool) -> bool
```

X.toggle_channel(channel_name, enabled) -> bool
Toggle Channel

Args:
    channel_name (str): 
    enabled (bool): 

Returns:
    bool:

<a id="unreal.TraceUtilLibrary.stop_tracing"></a>

#### stop\_tracing

```python
@classmethod
def stop_tracing(cls) -> bool
```

X.stop_tracing() -> bool
Stop Tracing

Returns:
    bool:

<a id="unreal.TraceUtilLibrary.start_trace_to_file"></a>

#### start\_trace\_to\_file

```python
@classmethod
def start_trace_to_file(cls, file_name: str, channels: Array[str]) -> bool
```

X.start_trace_to_file(file_name, channels) -> bool
Start Trace to File

Args:
    file_name (str): 
    channels (Array[str]): 

Returns:
    bool:

<a id="unreal.TraceUtilLibrary.start_trace_send_to"></a>

#### start\_trace\_send\_to

```python
@classmethod
def start_trace_send_to(cls, target: str, channels: Array[str]) -> bool
```

X.start_trace_send_to(target, channels) -> bool
Start Trace Send To

Args:
    target (str): 
    channels (Array[str]): 

Returns:
    bool:

<a id="unreal.TraceUtilLibrary.resume_tracing"></a>

#### resume\_tracing

```python
@classmethod
def resume_tracing(cls) -> bool
```

X.resume_tracing() -> bool
Resume Tracing

Returns:
    bool:

<a id="unreal.TraceUtilLibrary.pause_tracing"></a>

#### pause\_tracing

```python
@classmethod
def pause_tracing(cls) -> bool
```

X.pause_tracing() -> bool
Pause Tracing

Returns:
    bool:

<a id="unreal.TraceUtilLibrary.is_tracing"></a>

#### is\_tracing

```python
@classmethod
def is_tracing(cls) -> bool
```

X.is_tracing() -> bool
Is Tracing

Returns:
    bool:

<a id="unreal.TraceUtilLibrary.is_channel_enabled"></a>

#### is\_channel\_enabled

```python
@classmethod
def is_channel_enabled(cls, channel_name: str) -> bool
```

X.is_channel_enabled(channel_name) -> bool
Is Channel Enabled

Args:
    channel_name (str): 

Returns:
    bool:

<a id="unreal.TraceUtilLibrary.get_enabled_channels"></a>

#### get\_enabled\_channels

```python
@classmethod
def get_enabled_channels(cls) -> Array[str]
```

X.get_enabled_channels() -> Array[str]
Get Enabled Channels

Returns:
    Array[str]:

<a id="unreal.TraceUtilLibrary.get_all_channels"></a>

#### get\_all\_channels

```python
@classmethod
def get_all_channels(cls) -> Array[str]
```

X.get_all_channels() -> Array[str]
Get All Channels

Returns:
    Array[str]:

<a id="unreal.AnimationSharingSetupFactory"></a>