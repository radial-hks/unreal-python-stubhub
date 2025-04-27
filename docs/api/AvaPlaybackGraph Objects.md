## AvaPlaybackGraph Objects

```python
class AvaPlaybackGraph(Object)
```

A Playback Graph is used for playing Motion Design assets integrated with the broadcast framework.
It allows the creation of a playback graph with some logic and inputs routed to player nodes, the results of which can be routed
to broadcast channels. This is the lowest implementation layer that supports distributed playback (over message bus).

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaPlaybackGraph.h

<a id="unreal.AvaPlaybackGraph.unload_instances"></a>

#### unload_instances

```python
def unload_instances(unload_options: AvaPlaybackUnloadOptions) -> None
```

x.unload_instances(unload_options) -> None
Unload all game instance's worlds from this playback.

Args:
    unload_options (AvaPlaybackUnloadOptions):

<a id="unreal.AvaPlaybackGraph.stop"></a>

#### stop

```python
def stop(stop_options: AvaPlaybackStopOptions) -> None
```

x.stop(stop_options) -> None
Stop

Args:
    stop_options (AvaPlaybackStopOptions):

<a id="unreal.AvaPlaybackGraph.play"></a>

#### play

```python
def play() -> None
```

x.play() -> None
Play

<a id="unreal.AvaPlaybackGraph.load_instances"></a>

#### load_instances

```python
def load_instances() -> None
```

x.load_instances() -> None
Load Instances

<a id="unreal.AvaPlaybackGraph.is_playing"></a>

#### is_playing

```python
def is_playing() -> bool
```

x.is_playing() -> bool
Is Playing

Returns:
    bool:

<a id="unreal.AvalanchePlayback"></a>