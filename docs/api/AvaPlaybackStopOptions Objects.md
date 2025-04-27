## AvaPlaybackStopOptions Objects

```python
class AvaPlaybackStopOptions(EnumBase)
```

EAva Playback Stop Options

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaPlaybackGraph.h

<a id="unreal.AvaPlaybackStopOptions.NONE"></a>

#### NONE

0: Default option allows for deferred execution of the request when it is safe to do so.

<a id="unreal.AvaPlaybackStopOptions.FORCE_IMMEDIATE"></a>

#### FORCE_IMMEDIATE

2: Forces the execution of the request when it is called. Typically during shut down.

<a id="unreal.AvaPlaybackStopOptions.UNLOAD"></a>

#### UNLOAD

4: Unload from memory after being stopped.

<a id="unreal.AvaPlaybackStopOptions.DEFAULT"></a>

#### DEFAULT

0: Default option allows for deferred execution of the request when it is safe to do so.

<a id="unreal.NiagaraCompileErrorSeverity"></a>