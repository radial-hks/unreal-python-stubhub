## DisplayClusterConfigurationNetworkSettings Objects

```python
class DisplayClusterConfigurationNetworkSettings(StructBase)
```

Display Cluster Configuration Network Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``connect_retries_amount`` (int32):  [Read-Write] Advanced: amount of times nDisplay tries to reconnect before dropping
- ``connect_retry_delay`` (int32):  [Read-Write] Advanced: delay in between connection retries
- ``frame_end_barrier_timeout`` (int32):  [Read-Write] Advanced: timeout value for End Frame Barrier
- ``frame_start_barrier_timeout`` (int32):  [Read-Write] Advanced: timeout value for Start Frame Barrier
- ``game_start_barrier_timeout`` (int32):  [Read-Write] Advanced: timeout for Game Thread Barrier
- ``render_sync_barrier_timeout`` (int32):  [Read-Write] Advanced: timeout value for Render Sync

<a id="unreal.DisplayClusterConfigurationNetworkSettings.__init__"></a>

#### __init__

```python
def __init__(connect_retries_amount: int = 0,
             connect_retry_delay: int = 0,
             game_start_barrier_timeout: int = 0,
             frame_start_barrier_timeout: int = 0,
             frame_end_barrier_timeout: int = 0,
             render_sync_barrier_timeout: int = 0) -> None
```

<a id="unreal.DisplayClusterConfigurationNetworkSettings.connect_retries_amount"></a>

#### connect_retries_amount

```python
@property
def connect_retries_amount() -> int
```

(int32):  [Read-Write] Advanced: amount of times nDisplay tries to reconnect before dropping

<a id="unreal.DisplayClusterConfigurationNetworkSettings.connect_retries_amount"></a>

#### connect_retries_amount

```python
@connect_retries_amount.setter
def connect_retries_amount(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationNetworkSettings.connect_retry_delay"></a>

#### connect_retry_delay

```python
@property
def connect_retry_delay() -> int
```

(int32):  [Read-Write] Advanced: delay in between connection retries

<a id="unreal.DisplayClusterConfigurationNetworkSettings.connect_retry_delay"></a>

#### connect_retry_delay

```python
@connect_retry_delay.setter
def connect_retry_delay(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationNetworkSettings.game_start_barrier_timeout"></a>

#### game_start_barrier_timeout

```python
@property
def game_start_barrier_timeout() -> int
```

(int32):  [Read-Write] Advanced: timeout for Game Thread Barrier

<a id="unreal.DisplayClusterConfigurationNetworkSettings.game_start_barrier_timeout"></a>

#### game_start_barrier_timeout

```python
@game_start_barrier_timeout.setter
def game_start_barrier_timeout(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationNetworkSettings.frame_start_barrier_timeout"></a>

#### frame_start_barrier_timeout

```python
@property
def frame_start_barrier_timeout() -> int
```

(int32):  [Read-Write] Advanced: timeout value for Start Frame Barrier

<a id="unreal.DisplayClusterConfigurationNetworkSettings.frame_start_barrier_timeout"></a>

#### frame_start_barrier_timeout

```python
@frame_start_barrier_timeout.setter
def frame_start_barrier_timeout(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationNetworkSettings.frame_end_barrier_timeout"></a>

#### frame_end_barrier_timeout

```python
@property
def frame_end_barrier_timeout() -> int
```

(int32):  [Read-Write] Advanced: timeout value for End Frame Barrier

<a id="unreal.DisplayClusterConfigurationNetworkSettings.frame_end_barrier_timeout"></a>

#### frame_end_barrier_timeout

```python
@frame_end_barrier_timeout.setter
def frame_end_barrier_timeout(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationNetworkSettings.render_sync_barrier_timeout"></a>

#### render_sync_barrier_timeout

```python
@property
def render_sync_barrier_timeout() -> int
```

(int32):  [Read-Write] Advanced: timeout value for Render Sync

<a id="unreal.DisplayClusterConfigurationNetworkSettings.render_sync_barrier_timeout"></a>

#### render_sync_barrier_timeout

```python
@render_sync_barrier_timeout.setter
def render_sync_barrier_timeout(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationFailoverSettings"></a>