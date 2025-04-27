## AvaPlayable Objects

```python
class AvaPlayable(Object)
```

* Base class for a Motion Design playable.
*
* A playable (a.k.a. graphic or page) is the basic element that can be rendered
* and controlled through the animations and remote control.
*
* Design goal:
*
* The design goal is to abstract the implementation of a playable.
* So far we have 1 implementation:
* - Level Streaming that can be streamed with other levels in the same game instance.
*
* To support multiple playable in the same channel/output, there are 2 ways:
* - rendering in the same world which can only be done with the level streaming playables.
* - compositing different renders. This is not yet supported, but the playable abstraction should help.
*
* Future Work:
* There is also another abstraction desired which is the "remote" playable. The AvaPlaybackGraph
* has a lot of logic to manage remote replication of playable commands. It would probably
* be cleaner and more reusable to have a RemotePlayable class that implements all those instead.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaPlayable.h

<a id="unreal.AvalanchePlayable"></a>