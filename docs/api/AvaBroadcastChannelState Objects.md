## AvaBroadcastChannelState Objects

```python
class AvaBroadcastChannelState(EnumBase)
```

Channel state is a union summary of the output's states.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaMediaDefines.h

<a id="unreal.AvaBroadcastChannelState.OFFLINE"></a>

#### OFFLINE

0: Indicates that all channel outputs are offline.

<a id="unreal.AvaBroadcastChannelState.IDLE"></a>

#### IDLE

1: Indicates that at least some of the channel outputs are idle (but none are live).

<a id="unreal.AvaBroadcastChannelState.LIVE"></a>

#### LIVE

2: Indicates that at least some of the channel outputs are live.

<a id="unreal.AvaChannelState"></a>