## ReplaySubsystem Objects

```python
class ReplaySubsystem(GameInstanceSubsystem)
```

Replay Subsystem

**C++ Source:**

- **Module**: Engine
- **File**: ReplaySubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``load_default_map_on_stop`` (bool):  [Read-Write] Whether to reload the default map when StopReplay is called.

<a id="unreal.ReplaySubsystem.request_checkpoint"></a>

#### request_checkpoint

```python
def request_checkpoint() -> None
```

x.request_checkpoint() -> None
Request a checkpoint write, if currently recording.

<a id="unreal.ReplaySubsystem.is_recording"></a>

#### is_recording

```python
def is_recording() -> bool
```

x.is_recording() -> bool
Is Recording

Returns:
    bool:

<a id="unreal.ReplaySubsystem.is_playing"></a>

#### is_playing

```python
def is_playing() -> bool
```

x.is_playing() -> bool
Is Playing

Returns:
    bool:

<a id="unreal.ReplaySubsystem.get_replay_current_time"></a>

#### get_replay_current_time

```python
def get_replay_current_time() -> float
```

x.get_replay_current_time() -> float
Get current recording/playing replay time

Returns:
    float: float Current recording/playback time in seconds

<a id="unreal.ReplaySubsystem.get_active_replay_name"></a>

#### get_active_replay_name

```python
def get_active_replay_name() -> str
```

x.get_active_replay_name() -> str
Get current recording/playing replay name

Returns:
    str: FString Name of relpay (session id, file name, etc)

<a id="unreal.ReverbEffect"></a>